"""Drie modellen, exact dezelfde opgeslagen inputs, geen verwachte antwoorden."""
import concurrent.futures
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import time

ROOT = Path(__file__).resolve().parent.parent
INPUT = ROOT / 'build/runs-week05-v3'
OUT = ROOT / 'build/runs-week05-modellen'
SETUPS = {'A': 'gpt-6.1-sol', 'B': 'gpt-6-luna', 'C': 'gpt-6-astra'}

def run_one(setup, cid):
    base = OUT / f'{setup}-{cid}'
    if base.with_suffix('.meta.json').exists():
        return 'Reeds uitgevoerd: ' + base.name
    model = SETUPS[setup]
    clean = Path('/private/tmp/week05-eval-empty')
    clean.mkdir(exist_ok=True)
    command = ['codex', '--no-daemon', 'exec', '--ignore-user-config', '--ephemeral', '--skip-git-repo-check',
        '-C', str(clean), '-s', 'read-only', '-m', model, '-c', 'model_reasoning_effort="low"',
        '-c', 'service_tier="default"', '-c', 'project_doc_max_bytes=0', '-c', 'web_search="disabled"',
        '--disable', 'shell_tool', '--disable', 'apps', '--disable', 'plugins',
        '--disable', 'hooks', '--disable', 'multi_agent', '--disable', 'memories',
        '--json', '-o', str(base.with_suffix('.txt')), '-']
    start = time.time()
    with (INPUT / f'{cid}-input.txt').open() as inp, base.with_suffix('.events.jsonl').open('w') as log, base.with_suffix('.stderr.txt').open('w') as err:
        result = subprocess.run(command, stdin=inp, stdout=log, stderr=err, timeout=900)
    meta = {'case': cid, 'setup': setup, 'model_requested': model, 'effort': 'low',
        'started_utc': datetime.fromtimestamp(start, timezone.utc).isoformat(), 'seconds': round(time.time()-start,2),
        'returncode': result.returncode, 'command': command}
    base.with_suffix('.meta.json').write_text(json.dumps(meta,indent=2)+'\n')
    return f'{setup} {cid}: exit {result.returncode}, {meta["seconds"]} s'

if __name__ == '__main__':
    OUT.mkdir(exist_ok=True)
    source = json.loads((INPUT / 'manifest.json').read_text())
    for case in source['cases']:
        data = (INPUT / (case['id']+'-input.txt')).read_bytes()
        assert hashlib.sha256(data).hexdigest() == case['input_sha256']
    manifest = {'created_utc': datetime.now(timezone.utc).isoformat(), 'setups': SETUPS,
        'effort': 'low', 'service_tier_requested': 'default', 'n': 5, 'runs_per_input_per_setup': 1,
        'input_manifest': 'build/runs-week05-v3/manifest.json', 'cases': source['cases'],
        'changes_from_repeat_test': ['Onbekende en genegeerde tools.disable_defaults-optie verwijderd.', 'service_tier expliciet default voor standaardtariefvergelijking.'],
        'prices_usd_per_million': {'A': {'input':2,'cached_input':0.1,'cache_write':2.5,'output':10},
            'B': {'input':0.1,'cached_input':0.01,'cache_write':0.125,'output':0.5},
            'C': {'input':10,'cached_input':1,'cache_write':12.5,'output':50}},
        'price_sources': ['https://developers.openai.com/api/docs/models/gpt-6.1-sol','https://developers.openai.com/api/docs/models/gpt-6-luna','https://developers.openai.com/api/docs/models/gpt-6-astra']}
    manifest_path = OUT / 'manifest.json'
    if not manifest_path.exists():
        manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    jobs = [(setup, case['id']) for case in source['cases'] for setup in SETUPS]
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        for future in concurrent.futures.as_completed([pool.submit(run_one,*j) for j in jobs]):
            print(future.result(),flush=True)
