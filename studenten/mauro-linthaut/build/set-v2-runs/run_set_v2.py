import subprocess, sys, os, tempfile
from concurrent.futures import ThreadPoolExecutor
# Draait prompt v1.2 (build/prompt.md) één keer op alle 30 inputs van set v2.
# Per run een eigen, nieuwe sessie in een lege map, alleen de prompt met het KID erin. Het model ziet nooit een verwacht antwoord.
BUILD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.dirname(os.path.abspath(__file__))
PDF = {1: 3, 2: 1, 3: 5, 4: 6, 5: 8, 6: 2, 7: 4, 8: 7, 9: 9, 10: 10}
PDF.update({n: n for n in range(11, 33)})
prompt = open(os.path.join(BUILD, "prompt.md"), encoding="utf-8").read()
assert "<hier komt het KID>" in prompt
empty = tempfile.mkdtemp(prefix="leeg_")

def run(n):
    t = f"T{n:02d}"
    out = os.path.join(OUT, f"{t}.txt")
    if os.path.exists(out):
        return t, "bestaat al"
    kid = subprocess.run(["pdftotext", "-enc", "UTF-8", os.path.join(BUILD, "kid", f"{PDF[n]}.pdf"), "-"], capture_output=True, text=True, encoding="utf-8").stdout
    p = prompt.replace("<hier komt het KID>", kid)
    cmd = ["claude", "-p", "--tools", "", "--model", "claude-sonnet-5-5", "--no-session-persistence",
           "--disable-slash-commands", "--strict-mcp-config", "--setting-sources", ""]
    r = subprocess.run(cmd, input=p, capture_output=True, text=True, encoding="utf-8", cwd=empty, timeout=600)
    open(out, "w", encoding="utf-8").write(r.stdout)
    return t, f"klaar ({len(r.stdout)} tekens)" + (f" fout: {r.stderr[:100]}" if r.returncode else "")

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=10) as ex:
        for t, msg in ex.map(run, range(1, 33)):
            print(t, msg, flush=True)
