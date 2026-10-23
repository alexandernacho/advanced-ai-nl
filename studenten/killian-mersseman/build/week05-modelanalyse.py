"""Audit en kosten; semantische beoordelingen zijn na lezing expliciet vastgelegd."""
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / 'build/runs-week05-modellen'
M = json.loads((D / 'manifest.json').read_text())
EXPECTED = {
    'T01': (42524,140127,.02,'DKK','2026-04-01','2026-06-30'),
    'T02': (10764,54908,.48,'USD','2026-01-01','2026-06-30'),
    'T03': (-8821,155315,.2,'USD','2026-04-01','2026-06-30'),
    'T04': (2883.513,15132.394,.118,'USD','2026-07-01','2026-09-30'),
    'T05': (5078,12723,.12,'USD','2026-01-01','2026-06-30'),
}
FAILURES = {
    'A-T03': 'Schuld 132.549 in plaats van circa 155.315 miljoen USD; financiële leases en financieringsverplichtingen expliciet uitgesloten van de hoofdwaarde.',
    'B-T01': 'Schuldtoelichting zegt ten onrechte dat 8.622 miljoen DKK leases zijn uitgesloten; verwachting inclusief leases en Onzeker, maar status Nog te controleren.',
    'B-T02': 'Verwachte schuldstatus Onzeker ontbreekt (Nog te controleren). Controleberekening omzetgroei circa 47,61% in plaats van 47,6668%, afgerond 47,7%.',
    'B-T03': 'Twaalfmaands-FCF -7.604 in plaats van kwartaal-FCF -8.821; schuld 132.224 in plaats van circa 155.315 miljoen USD.',
    'B-T04': 'Hoofdpercentage omzetgroei 12% in plaats van vooraf vastgelegde 11,8% uit de overzichtstabel. Beide staan in de bron; beoordeeld tegenover de vaste verwachting.',
    'B-T05': 'Hoofdwaarden kloppen, maar de vooraf verwachte schuldstatus Onzeker ontbreekt (Nog te controleren); geen expliciet oordeel dat het schuldtotaal door ontbrekende financiële-leaseboekwaarden onvolledig kan zijn.',
}
rows = []
for case in M['cases']:
    cid = case['id']
    data = (ROOT / 'build/runs-week05-v3' / (cid+'-input.txt')).read_bytes()
    assert hashlib.sha256(data).hexdigest() == case['input_sha256']
    for setup in M['setups']:
        name = setup+'-'+cid
        meta = json.loads((D/(name+'.meta.json')).read_text())
        assert meta['returncode'] == 0
        events = [json.loads(line) for line in (D/(name+'.events.jsonl')).read_text().splitlines()]
        kinds = {e.get('item',{}).get('type') for e in events if e.get('type','').startswith('item.')}
        assert kinds <= {'agent_message','error'}, (name,kinds)
        completed = [e for e in events if e.get('type')=='turn.completed']
        assert len(completed)==1
        usage = completed[0]['usage']
        answer = (D/(name+'.txt')).read_text()
        records = json.loads(re.search(r'```json\s*(.*?)```',answer,re.S).group(1))['records']
        rs = {r['metric']:r for r in records}
        expected = EXPECTED[cid]
        numeric = {k: abs(rs[k]['value']-v)<.000001 for k,v in zip(['FCF','Schuld','Omzetgroei'],expected[:3])}
        dates_currency = (all(rs[k]['currency']==expected[3] for k in ['FCF','Schuld'])
            and rs['Omzetgroei']['currency'] is None and all(r['end']==expected[5] for r in rs.values())
            and rs['FCF']['start']==expected[4] and rs['Schuld']['start'] is None
            and rs['Omzetgroei']['start']==('2026-07-01' if cid=='T04' else '2026-04-01'))
        passed = name not in FAILURES
        if passed:
            assert all(numeric.values()) and dates_currency, name
        rates = M['prices_usd_per_million'][setup]
        inp = usage['input_tokens']; cached = usage.get('cached_input_tokens',0)
        writes = usage.get('cache_write_input_tokens',0); output = usage['output_tokens']
        assert writes==0, 'Controleer cache-write-semantiek voordat extra kosten worden berekend'
        long = inp > 272000
        im = 2 if long else 1; om = 1.5 if long else 1
        cost = ((inp-cached)*rates['input']*im+cached*rates['cached_input']*im+output*rates['output']*om)/1e6
        nocache = (inp*rates['input']*im+output*rates['output']*om)/1e6
        rows.append({'id':name,'model_requested':meta['model_requested'],'effort':meta['effort'],
            'started_utc':meta['started_utc'],'seconds':meta['seconds'],'usage':usage,'tool_actions':0,
            'long_context_multiplier':long,'usd_api_equivalent':cost,'usd_without_cache_discount':nocache,
            'numeric_matches':numeric,'dates_and_currency_match':dates_currency,'passed':passed,
            'assessment':FAILURES.get(name,'Geslaagd: hoofdwaarden, perioden, valuta, controleberekening en schuldbeperking komen overeen met de vooraf vastgelegde verwachting; toelichtingen door agent gelezen.'),
            'records':records})
summary = {}
for setup in M['setups']:
    group=[r for r in rows if r['id'].startswith(setup+'-')]
    summary[setup]={'model':M['setups'][setup],'n':len(group),'passed':sum(r['passed'] for r in group),
        'avg_output_tokens':sum(r['usage']['output_tokens'] for r in group)/5,
        'avg_input_tokens':sum(r['usage']['input_tokens'] for r in group)/5,
        'avg_cached_input_tokens':sum(r['usage'].get('cached_input_tokens',0) for r in group)/5,
        'avg_reasoning_tokens':sum(r['usage'].get('reasoning_output_tokens',0) for r in group)/5,
        'max_input_tokens':max(r['usage']['input_tokens'] for r in group),
        'avg_seconds':sum(r['seconds'] for r in group)/5,
        'avg_usd':sum(r['usd_api_equivalent'] for r in group)/5,
        'year_40_usd':sum(r['usd_api_equivalent'] for r in group)/5*40,
        'avg_nocache_usd':sum(r['usd_without_cache_discount'] for r in group)/5,
        'numeric_matches_out_of_15':sum(sum(r['numeric_matches'].values()) for r in group)}
(D/'audit.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
(D/'samenvatting.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))
