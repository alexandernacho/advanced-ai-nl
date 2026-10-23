"""Gecontroleerde v3-extractietest; verwachte antwoorden worden hier niet ingelezen."""
import concurrent.futures
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'build/runs-week05-v3'
CASES = [
    ('T01', 'NVO', 'build/rapporten/NVO/NVO-2026-06-30.pdf', ''),
    ('T02', 'LLY', 'build/rapporten/LLY/LLY-2026-06-30.pdf', 'Als afzonderlijke kwartaal-FCF ontbreekt, kies ik vooraf 1 januari tot en met 30 juni 2026. Deze periodekeuze is al gemaakt; je hoeft daar niet opnieuw op te wachten.'),
    ('T03', 'AMZN', 'build/rapporten/AMZN/AMZN-2026-06-30.pdf', ''),
    ('T04', 'NFLX', 'build/rapporten/NFLX/2026-Q3/NFLX-2026-09-30-aandeelhoudersbrief.pdf', ''),
    ('T05', 'UBER', 'build/rapporten/UBER/UBER-2026-06-30.pdf', 'Als afzonderlijke kwartaal-FCF ontbreekt, kies ik vooraf 1 januari tot en met 30 juni 2026. Deze periodekeuze is al gemaakt; je hoeft daar niet opnieuw op te wachten.'),
]

def digest(data):
    return hashlib.sha256(data).hexdigest()

def prepare():
    from pypdf import PdfReader
    OUT.mkdir(exist_ok=True)
    source = ROOT / 'build/prompt-v3-enkel-bedrijf.md'
    original = source.read_text()
    financial = original.split('## Instructies om te kopiëren\n', 1)[1].split('\n7. Sla de extractie', 1)[0]
    schema = original.split('```json\n', 1)[1].split('\n```', 1)[0]
    prompt = ('# V3 — afgebakende extractievariant voor de herhaaltest\n\n'
        'De volledige rapporttekst staat hieronder als bronmateriaal. Gebruik geen tools, web, bestanden of geheugen. '
        'Voer alleen de financiële extractie uit; sla niets op en werk Excel niet bij. '
        'De regels over externe wisselkoersen beschrijven de productieomgeving; haal voor deze test geen koersen op.\n\n'
        + financial + '\n\nGeef na de controletabel JSON met één record per maatstaf, volgens dit schema:\n```json\n'
        + schema + '\n```\nSchuld heeft start null en period_type Peildatum; omzetgroei heeft currency null. '
        'Bedragen zijn miljoenen in de oorspronkelijke valuta en percentages zijn fracties.\n')
    (OUT / 'prompt-extractie.md').write_text(prompt)
    manifest = {'created_utc': datetime.now(timezone.utc).isoformat(), 'model': 'gpt-6.1-sol', 'effort': 'low',
        'n': 5, 'repetitions': 3, 'scope': 'extractie na vooraf vastgelegde periodekeuze; geen Excel-update',
        'original_prompt_sha256': digest(source.read_bytes()), 'extraction_prompt_sha256': digest(prompt.encode()),
        'pdf_reader': 'pypdf; volledige tekst per pagina; geen OCR of paginafilter', 'cases': []}
    for cid, ticker, path, choice in CASES:
        pdf = ROOT / path
        reader = PdfReader(pdf)
        raw_pages = [(p.extract_text() or '') for p in reader.pages]
        pages = ['\n--- PDF-pagina ' + str(i + 1) + ' ---\n' + t for i,t in enumerate(raw_pages)]
        text = '\n'.join(pages)
        full = prompt + '\n\n# Input\nTicker: ' + ticker + '\nBronbestand: ' + pdf.name + '\n' + choice + '\n\n<rapport>\n' + text + '\n</rapport>\n'
        target = OUT / (cid + '-input.txt')
        target.write_text(full)
        manifest['cases'].append({'id': cid, 'ticker': ticker, 'pdf': path, 'pdf_sha256': digest(pdf.read_bytes()),
            'pages': len(reader.pages), 'textless_pages': [i+1 for i,t in enumerate(raw_pages) if not t.strip()], 'input_sha256': digest(full.encode()), 'input_characters': len(full), 'period_choice': choice})
    (OUT / 'manifest.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + '\n')
    print(json.dumps(manifest, indent=2, ensure_ascii=False), flush=True)

def run_one(cid, repeat):
    base = OUT / f'{cid}-run{repeat}'
    if base.with_suffix('.meta.json').exists():
        return 'Reeds uitgevoerd: ' + base.name
    clean = Path('/private/tmp/week05-eval-empty')
    clean.mkdir(exist_ok=True)
    command = ['codex', '--no-daemon', 'exec', '--ignore-user-config', '--ephemeral', '--skip-git-repo-check',
        '-C', str(clean), '-s', 'read-only', '-m', 'gpt-6.1-sol', '-c', 'model_reasoning_effort="low"',
        '-c', 'project_doc_max_bytes=0', '-c', 'web_search="disabled"',
        '-c', 'tools.disable_defaults=true', '--disable', 'shell_tool', '--disable', 'apps', '--disable', 'plugins',
        '--disable', 'hooks', '--disable', 'multi_agent', '--disable', 'memories',
        '--json', '-o', str(base.with_suffix('.txt')), '-']
    start = time.time()
    with (OUT / f'{cid}-input.txt').open() as inp, base.with_suffix('.events.jsonl').open('w') as log, base.with_suffix('.stderr.txt').open('w') as err:
        result = subprocess.run(command, stdin=inp, stdout=log, stderr=err, timeout=900)
    meta = {'case': cid, 'run': repeat, 'model_requested': 'gpt-6.1-sol', 'effort': 'low',
        'started_utc': datetime.fromtimestamp(start, timezone.utc).isoformat(), 'seconds': round(time.time()-start, 2),
        'returncode': result.returncode, 'command': command}
    base.with_suffix('.meta.json').write_text(json.dumps(meta, indent=2) + '\n')
    return f'{cid} run {repeat}: exit {result.returncode}, {meta["seconds"]} s'

if __name__ == '__main__':
    if sys.argv[1:] == ['prepare']:
        prepare()
    elif sys.argv[1:] == ['first']:
        print(run_one('T01', 1), flush=True)
    elif sys.argv[1:] == ['all']:
        jobs = [(cid, n) for cid, *_ in CASES for n in range(1,4)]
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
            for result in concurrent.futures.as_completed([pool.submit(run_one, *j) for j in jobs]):
                print(result.result(), flush=True)
    else:
        raise SystemExit('Gebruik: prepare, first of all')
