"""Losse Codex-sessies; alleen prompt en één input, nooit verwachte antwoorden."""
import concurrent.futures
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parent
INPUTS = [
    "bulgarian split squat, 20kg, 4 sets, 12 reps",
    "RDL, 40kg, 4 sets, 12 reps",
    "cable kickbaks, 15kg, 4 sets, 12 reps",
    "hip thrusts, 60kg, 4 x 12",
    "seated hamstring curl, 20kg, 4 x 12",
    "cable strght arm pull down 20kg 3x12 + laatste set tot faillure",
    "Dumbbell Row (Single‑Arm), 4 x 15",
    "dumbbell pullover, eerst 10kg, dan 12, dan 14 3xtot faillure",
    "faceplls, 30kg, 4, laatste set tot faillure",
    "lat puldwon, 35kg, 3 sets, 12 herhalingen per set",
]


def run(job):
    version, repeat, number = job
    stem = ROOT / f"{version}-run-{repeat}-input-{number:02d}"
    answer = stem.with_suffix(".txt")
    if answer.exists() and answer.read_text().strip():
        return f"bewaard: {stem.name}"
    prompt = (ROOT.parent / f"prompt-{version}.md").read_text()
    prompt = prompt.replace("[Plak hier één eigen trainingsnotitie over één oefening.]", INPUTS[number - 1])
    with tempfile.TemporaryDirectory(prefix="cansu-eval-") as isolated:
        cmd = ["codex", "exec", "--ignore-user-config", "--ephemeral",
               "--skip-git-repo-check", "-C", isolated, "--sandbox", "read-only",
               "-m", "gpt-5.6-terra", "-c", 'model_reasoning_effort="high"',
               "-c", "project_doc_max_bytes=0", "-c", 'developer_instructions=""',
               "-c", "features.shell_tool=false", "-c", "features.apply_patch_freeform=false",
               "-c", 'web_search="disabled"', "--json", "-o", str(answer), "-"]
        started = time.monotonic()
        result = subprocess.run(cmd, input=prompt, text=True, capture_output=True, timeout=180)
    stem.with_suffix(".jsonl").write_text(result.stdout)
    stem.with_suffix(".stderr").write_text(result.stderr)
    stem.with_suffix(".meta.json").write_text(json.dumps({
        "model_requested": "gpt-5.6-terra", "effort": "high",
        "version": version, "run": repeat, "input": number,
        "returncode": result.returncode, "seconds": round(time.monotonic()-started, 2),
        "isolated_session": True,
    }, indent=2))
    if result.returncode or not answer.exists() or not answer.read_text().strip():
        raise RuntimeError(f"{stem.name}: {result.stderr[-1500:]} {result.stdout[-1500:]}")
    return f"klaar: {stem.name}"


if __name__ == "__main__":
    jobs = [(v, r, i) for v in ("v4", "v5") for r in range(1, 4) for i in range(1, 11)]
    if "--pilot" in sys.argv:
        jobs = jobs[:1]
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        for outcome in pool.map(run, jobs):
            print(outcome, flush=True)
