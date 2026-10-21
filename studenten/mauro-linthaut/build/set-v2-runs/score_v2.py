import re, sys, os, json
# Score voor set v2 (T01-T30). Verwachte antwoorden overgenomen uit build/test-set.md, kolom "Juiste antwoord".
# Het model krijgt dit bestand nooit te zien.
# Per input: (risico, bewaartermijn, lopende kosten, instap, uitstap, index, uitkerend/accumulerend, (bedrag, munt, rendement))
# None = het juiste antwoord is "niet vermeld". Instap/uitstap: 0 = geen kosten, None = niet vermeld.
NV = None
E = {
 "T01": (5, "5 jaar", "0,20", 0, 0, "nasdaq100index", "accumulerend", ("12.060", "USD", "3,8")),
 "T02": (4, "5 jaar", "0,25", 0, 0, "msciworldequalweightedindex", "accumulerend", ("10.650", "USD", "1,27")),
 "T03": (5, "5 jaar", "0,75", 0, 0, "indxxdefianceglobalmemorychipselectindex", "accumulerend", ("14.390", "USD", "7,5")),
 "T04": (5, "5 jaar", "0,53", 0, 0, "roboglobalartificialintelligenceindex", "accumulerend", ("13.600", "USD", "6,3")),
 "T05": (6, "5 jaar", "0,35", 0, 0, "marketvectorus listedsemiconductor10%cappedscreenedindex".replace(" ", ""), "accumulerend", ("20.210", "USD", "15,11")),
 "T06": (4, "5 jaar", "0,03", 0, 0, "sp500index", "accumulerend", ("12.010", "USD", "3,7")),
 "T07": (4, "5 jaar", "0,25", 0, 0, "msciworldequalweightedindex", "accumulerend", ("10.650", "USD", "1,27")),
 "T08": (4, "5 jaar", "0,03", 0, 0, "sp500index", "accumulerend", ("12.010", "USD", "3,7")),
 "T09": (6, "5 jaar", "0,35", 0, 0, "marketvectorus listedsemiconductor10%cappedscreenedindex".replace(" ", ""), "accumulerend", ("20.210", "USD", "15,11")),
 "T10": (4, "5 jaar", "0,16", 0, 0, "ftseallworldindex", "accumulerend", ("12.170", "USD", "4,01")),
 "T11": (4, "5 jaar", "0,12", 0, 0, "solactivegbsglobalmarketslargemidcapindex", "accumulerend", ("12.370", "USD", "4,3")),
 "T12": (5, "5 jaar", "0,56", 0, 0, "marketvectorglobaluraniumandnuclearenergyinfrastructureindex", "accumulerend", ("13.140", "USD", "5,61")),
 "T13": (5, "5 jaar", "0,58", 0, 0, "marketvectorglobalspaceindustryscreenedindex", "accumulerend", ("10.690", "USD", "1,35")),
 "T14": (4, "5 jaar", "0,60", 0, 0, "solactivevideogamesesportsv2index", "accumulerend", ("7.560", "USD", "-5,44")),
 "T15": (4, "5 jaar", "0,74", 0, 0, "spglobalwaterindex", "uitkerend", ("11.090", "USD", "2,1")),
 "T16": (4, "5 jaar", "0,44", 0, 0, "stoxxglobalageingpopulationindex", "accumulerend", ("10.110", "USD", "0,2")),
 "T17": (4, "5 jaar", "0,49", 0, 0, "eqmfutureofdefenceindex", "accumulerend", ("12.620", "USD", "4,8")),
 "T18": (5, "5 jaar", "0,76", 0, 0, "isecybersecurityucitsindexnettotalreturn", "accumulerend", ("12.220", "USD", "4,1")),
 "T19": (6, "5 jaar", "0,62", 0, 0, "mvisglobalrareearthstrategicmetalsindex", "accumulerend", ("5.180", "USD", "-12,32")),
 "T20": (4, "5 jaar", "0,68", 0, 0, "msciindiaindexnetusd", "accumulerend", ("8.710", "USD", "-2,7")),
 "T21": (3, "3 jaar", "0,13", 0, 0, "ftseeurogovernmentbondindex", "uitkerend", ("7.870", "EUR", "-7,7")),
 "T22": (3, "5 jaar", "0,22", 0, 0, "msciworldselectscreenedindex", "accumulerend", ("11.360", "USD", "2,6")),
 "T23": (4, "5 jaar", "0,20", 0, 0, "sp500index", "accumulerend", ("11.210", "EUR", "2,3")),
 "T24": (4, "5 jaar", "0,11", 0, 0, "ftse100index", "accumulerend", ("11.290", "GBP", "2,5")),
 "T25": (1, "30 dagen", "0,10", 0, 0, "solactivestr85dailytotalreturnindex", "accumulerend", ("9.990", "EUR", "-0,1")),
 "T26": (4, "5 jaar", "0,22", 0, 0, NV, "accumulerend", ("11.680", "USD", "3,1")),
 "T27": (4, "5 jaar", "0,47", 0, 0, NV, "uitkerend", ("11.070", "EUR", "2,1")),
 "T28": (NV, NV, NV, NV, NV, NV, "accumulerend", NV),
 "T29": (NV, NV, NV, NV, NV, NV, "accumulerend", NV),
 "T30": (5, "7 jaar", "0,12", 0, 0, "msciusainformationtechnology2035customindex", "uitkerend", ("12.140", "USD", "2,8")),
 "T31": (6, "10 jaar", "3,35", "3", "3", NV, "accumulerend", ("9.970", "EUR", "-0,03")),
 "T32": (3, "5 jaar", "2,2", 0, 0, NV, "niet vermeld", ("6.690", "EUR", "-7,71")),
}
NAMES = ["Risico-indicator", "Aanbevolen bewaartermijn", "Lopende kosten per jaar", "Instapkosten", "Uitstapkosten", "Gevolgde index", "Uitkerend of accumulerend", "Ongunstig scenario"]
FIELDS = ["risico", "termijn", "lopende kosten", "instap", "uitstap", "index", "uitk/acc", "scenario"]

def num(s):
    m = re.search(r"-?\d[\d\.]*(?:,\d+)?", s)
    return m.group(0) if m else None

def pc(a, b):
    if a is None:
        return False
    return a.rstrip("0").rstrip(",") == b.rstrip("0").rstrip(",") if "," in a and "," in b else a == b

def nv(s):
    return s.strip().lower().startswith("niet vermeld")

def parse(txt):
    vals, extra = {}, []
    for line in txt.splitlines():
        l = line.strip()
        if not l or l.startswith("```") or l.startswith("ETF:"):
            continue
        hit = False
        for n in NAMES:
            if l.startswith(n + ":"):
                v = l[len(n) + 1:].split("| bron")[0].strip()
                if n in vals:
                    extra.append("dubbel:" + n)
                vals[n] = v
                hit = True
                break
        if not hit:
            extra.append(l[:80])
    return vals, extra

def score(t, txt):
    e = E[t]
    vals, extra = parse(txt)
    g = lambda n: vals.get(n, "")
    r = {}
    r[0] = nv(g(NAMES[0])) if e[0] is None else bool(re.match(r"\s*" + str(e[0]) + r"\b", g(NAMES[0])))
    if e[1] is None:
        r[1] = nv(g(NAMES[1]))
    else:
        n, unit = e[1].split()
        r[1] = bool(re.match(r"\s*" + n + r"\s*" + unit[:3], g(NAMES[1]).lower()))
    r[2] = nv(g(NAMES[2])) if e[2] is None else pc(num(g(NAMES[2])), e[2])
    for i in (3, 4):
        want = "0" if e[i] == 0 else str(e[i])
        r[i] = nv(g(NAMES[i])) if e[i] is None else bool(re.match(r"\s*(tot\s+|maximaal\s+|max\.?\s+)?" + want + r"([,\.]0+)?\s*(%|usd|eur|gbp)", g(NAMES[i]).lower()))
    if e[5] is None:
        r[5] = nv(g(NAMES[5]))
    else:
        r[5] = e[5] in re.sub(r"[^a-z0-9%]", "", g(NAMES[5]).lower().replace("&", ""))
    r[6] = g(NAMES[6]).lower().startswith(e[6][:7])
    sc = g(NAMES[7])
    if e[7] is None:
        r[7] = nv(sc)
    else:
        amt_exp, cur, ret_exp = e[7]
        m = re.search(r"([\d\.,]+)\s*" + cur + r"|" + cur + r"\s*([\d\.,]+)", sc)
        amt = (m.group(1) or m.group(2)) if m else None
        rest = sc.split(" en ", 1)[1] if " en " in sc else ""
        ret = re.search(r"-?[\d]+(?:,\d+)?(?=\s*%)", rest)
        rr = ret.group(0) if ret else None
        r[7] = (amt == amt_exp) and rr is not None and pc(rr, ret_exp) and not re.search(r"\d\.\d+\s*%", rest)
    return r, vals, extra

if __name__ == "__main__":
    S = sys.argv[1]
    res = {}
    for t in sorted(E):
        p = f"{S}/{t}.txt"
        if not os.path.exists(p):
            continue
        txt = open(p, encoding="utf-8").read()
        r, vals, extra = score(t, txt)
        res[t] = {"fields": [int(r[i]) for i in range(8)], "n": sum(r.values()), "extra": extra, "scen": vals.get(NAMES[7], "")}
    json.dump(res, open(f"{S}/scores.json", "w"), ensure_ascii=False, indent=1)
    tot_ok = tot_all = 0
    for t, x in res.items():
        flag = "" if x["n"] == 8 and not x["extra"] else "  <-- fout: " + ", ".join(FIELDS[i] for i in range(8) if not x["fields"][i]) + (" | extra: " + str(x["extra"])[:100] if x["extra"] else "")
        print(t, f"{x['n']}/8", flag)
        tot_ok += x["n"]; tot_all += 8
    full = sum(1 for x in res.values() if x["n"] == 8)
    print(f"\nTotaal: {tot_ok} van {tot_all} velden juist; {full} van {len(res)} inputs volledig juist (set v2, 1 run)")
    for lo, hi, name in ((1, 10, "T01-T10 (oud)"), (11, 30, "T11-T30 (controle)")):
        ts = [f"T{n:02d}" for n in range(lo, hi + 1) if f"T{n:02d}" in res]
        if ts:
            print(f"{name}: {sum(res[t]['n'] for t in ts)} van {8*len(ts)} velden; {sum(1 for t in ts if res[t]['n']==8)} van {len(ts)} inputs volledig juist")
