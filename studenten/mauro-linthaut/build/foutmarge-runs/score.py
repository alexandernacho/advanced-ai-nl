import re,sys,os,json
S=sys.argv[1]
# verwachte antwoorden: overgenomen uit build/test-set.md, kolom "Juiste antwoord"
E={
"T01":(5,5,"0,20",None,"nasdaq100index","12.060","3,8"),
"T02":(4,5,"0,25",None,"msciworldequalweightedindex","10.650","1,27"),
"T03":(5,5,"0,75",None,"indxxdefianceglobalmemorychipselectindex","14.390","7,5"),
"T04":(5,5,"0,53",None,"roboglobalartificialintelligenceindex","13.600","6,3"),
"T05":(6,5,"0,35",None,"marketvectorus listedsemiconductor10%cappedscreenedindex".replace(" ",""),"20.210","15,11"),
"T06":(4,5,"0,03",None,"sp500index","12.010","3,7"),
"T07":(4,5,"0,25",None,"msciworldequalweightedindex","10.650","1,27"),
"T08":(4,5,"0,03",None,"sp500index","12.010","3,7"),
"T09":(6,5,"0,35",None,"marketvectorus listedsemiconductor10%cappedscreenedindex".replace(" ",""),"20.210","15,11"),
"T10":(4,5,"0,16",None,"ftseallworldindex","12.170","4,01"),
}
NAMES=["Risico-indicator","Aanbevolen bewaartermijn","Lopende kosten per jaar","Instapkosten","Uitstapkosten","Gevolgde index","Uitkerend of accumulerend","Ongunstig scenario"]
def num(s):  # eerste getal in Nederlandse notatie, als string zonder %, spaties
    m=re.search(r"-?\d[\d\.]*(?:,\d+)?",s); return m.group(0) if m else None
def pc(a,b):
    if a is None: return False
    return a.rstrip("0").rstrip(",")==b.rstrip("0").rstrip(",") if "," in a and "," in b else a==b
def score(t,txt):
    e=E[t]; vals={}
    extra=[]
    for line in txt.splitlines():
        l=line.strip()
        if not l or l.startswith("```") or l.startswith("ETF:"): continue
        hit=False
        for n in NAMES:
            if l.startswith(n+":"):
                v=l[len(n)+1:].split("| bron")[0].strip()
                if n in vals: extra.append("dubbel:"+n)
                vals[n]=v; hit=True; break
        if not hit: extra.append(l[:80])
    r={}
    g=lambda n: vals.get(n,"")
    r[0]=bool(re.match(r"\s*"+str(e[0])+r"\b",g(NAMES[0])))
    r[1]=bool(re.match(r"\s*"+str(e[1])+r"\b",g(NAMES[1])))
    r[2]=pc(num(g(NAMES[2])),e[2])
    r[3]=bool(re.match(r"\s*0([,\.]0+)?\s*%",g(NAMES[3])))
    r[4]=bool(re.match(r"\s*0([,\.]0+)?\s*%",g(NAMES[4])))
    r[5]=e[4] in re.sub(r"[^a-z0-9%]","",g(NAMES[5]).lower().replace("&",""))
    r[6]=g(NAMES[6]).lower().startswith("accumul")
    sc=g(NAMES[7]); m=re.search(r"([\d\.,]+)\s*USD|USD\s*([\d\.,]+)",sc)
    amt=(m.group(1) or m.group(2)) if m else None
    rest=sc.split("en",1)[1] if " en " in sc else ""
    ret=re.search(r"-?[\d]+(?:,\d+)?(?=\s*%)",rest.replace(".",",") if False else rest)
    rr=ret.group(0) if ret else None
    r[7]=(amt==e[5]) and rr is not None and pc(rr,e[6]) and "USD" in sc and not re.search(r"\d\.\d+\s*%",rest)
    return r,vals,extra
if __name__=="__main__":
    res={}
    for v in ("vOud","vNieuw"):
        for t in sorted(E):
            for run in (1,2,3):
                p=f"{S}/out/{v}_{t}_r{run}.txt"
                if not os.path.exists(p): continue
                txt=open(p,encoding="utf-8").read()
                r,vals,extra=score(t,txt)
                res[f"{v}|{t}|{run}"]={"fields":[int(r[i]) for i in range(8)],"n":sum(r.values()),"extra":extra,"nvals":len(vals),"scen":vals.get(NAMES[7],""),"cost":vals.get(NAMES[2],"")}
    json.dump(res,open(f"{S}/scores.json","w"),ensure_ascii=False,indent=1)
    for k,x in res.items():
        flag="" if x["n"]==8 and not x["extra"] else "  <-- "+str(x["fields"])+" "+str(x["extra"])[:100]
        print(k,x["n"],flag)
