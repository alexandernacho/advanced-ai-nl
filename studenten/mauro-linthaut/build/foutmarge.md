# Foutmarge, 21 oktober 2026

Model: Claude Sonnet 5.5 (`claude-sonnet-5-5`), hetzelfde model als de testset. Claude Code 2.1.306. n = 10 inputs (T01 tot T10), 3 runs per versie. Zelfde inputs voor beide versies.

Score = het aantal KID's (van 10) waarvan alle 8 velden juist zijn.

| Versie | Run 1 | Run 2 | Run 3 | Foutmarge (min–max) |
|---|---:|---:|---:|---:|
| v1 (week 2, vorige versie in git) | 3/10 | 4/10 | 4/10 | 3–4 |
| v1.2 (laatste) | 10/10 | 10/10 | 9/10 | 9–10 |

Mijn claim (week 3 en 4): "Met mijn laatste prompt (v1.2) kwam ik op 79 op 80 juist (n = 10, 1 run)" en de regel die het rendement controleert herstelde de fout bij T04 (−33,5% werd 6,3%). Mijn prompt werd dus beter door de wijzigingen van week 3.

Bevestigd of ingetrokken: **bevestigd**, want de laagste score van v1.2 (9/10) ligt hoger dan de hoogste score van v1 (4/10). De bereiken overlappen niet. Ook op velden gerekend (hieronder) is dat zo: 79 tot 80 van 80 tegenover 70 tot 71 van 80. Wat de claim niet bewijst: dat het aan één regel ligt (zie de afwijking over v1.1), en dat 79/80 uit week 3 een vaste score is. In deze 3 runs schommelde v1.2 tussen 79 en 80 velden.

Hieronder het volledige verslag: de afwijking van de opdracht, hoe ik draaide, de score per KID en de fouten.

## Wat ik vergeleek

| | Prompt | Waar vandaan |
|---|---|---|
| **Laatste versie (v1.2)** | `build/prompt.md` zoals nu: twee voorbeelden, optelregel voor lopende kosten, notatieregel, rendement "in stilte" controleren | `build/prompt.md` (zelfde als git `d6acc91`) |
| **Versie ervoor (v1)** | de prompt van week 2: geen voorbeelden, geen optelregel, geen notatieregel, geen rendementscontrole | git `5f8639c` (`build/prompt.md` van toen) |

**Let op, afwijking van "de versie ervoor":** v1.1 (v1 plus alleen de rendementscontrole, met de extra tekst) is nooit apart gecommit. In git staat alleen v1 en daarna v1.2 (`d6acc91`), en de precieze tekst van v1.1 staat nergens. Ik heb die tekst niet nagemaakt, want dan meet ik mijn eigen gok en niet jouw prompt. De vorige versie in git is v1; dat is dus een grotere stap dan v1.1 naar v1.2. Het verschil tussen v1 en v1.2 is de som van alle wijzigingen van week 3 samen. Kun je v1.1 terugvinden (bijvoorbeeld in een eerder gesprek), dan kan ik die er als derde versie bij draaien.

## Hoe ik het draaide

- Inputs: alle 10 KID's uit `build/test-set.md` (T01 tot T10), de pdf's in `build/kid/`, als tekst uitgelezen met `pdftotext -enc UTF-8` en op de plaats van `<hier komt het KID>` in de prompt gezet. Bij beide versies exact dezelfde tekst.
- 3 runs per versie per input: 2 versies × 10 inputs × 3 runs = **60 runs**.
- Elke run een eigen, nieuwe sessie in een lege map, met alleen de prompt met het KID erin als input:
  `claude -p --tools "" --model claude-sonnet-5-5 --no-session-persistence --disable-slash-commands --strict-mcp-config --setting-sources ""`.
  Geen tools, geen `CLAUDE.md`, geen context, geen geheugen, geen skills. Tien runs tegelijk (parallel).
- Het model kreeg nooit een verwacht antwoord te zien.
- Het verwachte antwoord is de kolom "Juiste antwoord" van `build/test-set.md`, onaangeraakt. Ik heb er niets aan veranderd.
- Een veld telt als juist als de waarde klopt én in de notatie staat die de prompt vraagt: Nederlandse notatie (punt bij duizendtallen, komma bij decimalen). "13,600 USD", "6.3%" en "10 650 USD" tellen dus als fout, zoals bij T04 in week 2. Bij de index telt de kern van de naam (zoals eerder: "(Net)" of "®" weglaten mag). "0,00%" en "0%" zijn dezelfde waarde. De bronzinnen heb ik niet gescoord (alleen de acht waarden).
- Eerst automatisch gescoord met een script, daarna elke afwijking en alle scenario- en kostenregels van v1.2 met de hand nagelezen. Eén tikfout in mijn eigen script (de verwachte indexnaam van T02 en T07) heb ik gevonden en hersteld voor de cijfers hieronder.

## Score per run (velden juist, van 8)

| ID | Input | v1 run 1 | v1 run 2 | v1 run 3 | v1.2 run 1 | v1.2 run 2 | v1.2 run 3 |
|---|---|---:|---:|---:|---:|---:|---:|
| T01 | Xtrackers NASDAQ 100 (NL) | 7 | 8 | 8 | 8 | 8 | 8 |
| T02 | Invesco MSCI World EW (FR) | 6 | 6 | 6 | 8 | 8 | 8 |
| T03 | Defiance Memory (NL) | 7 | 7 | 7 | 8 | 8 | 8 |
| T04 | L&G Artificial Intelligence (FR) | 6 | 6 | 6 | 8 | 8 | 8 |
| T05 | VanEck Semiconductor (NL) | 8 | 8 | 8 | 8 | 8 | 8 |
| T06 | SPDR S&P 500 (FR) | 8 | 8 | 8 | 8 | 8 | 8 |
| T07 | Invesco MSCI World EW (NL) | 7 | 7 | 7 | 8 | 8 | 7 |
| T08 | SPDR S&P 500 (NL) | 8 | 8 | 8 | 8 | 8 | 8 |
| T09 | VanEck Semiconductor (FR) | 7 | 7 | 7 | 8 | 8 | 8 |
| T10 | Vanguard FTSE All-World (NL) | 6 | 6 | 6 | 8 | 8 | 8 |
| | **Totaal van 80 velden (10 KID's × 8)** | **70** | **71** | **71** | **80** | **80** | **79** |
| | Inputs volledig juist (van 10) | 3 | 4 | 4 | 10 | 10 | 9 |

## Samenvatting per versie (in velden, van 80 = 10 KID's × 8 velden)

| Versie | Run 1 | Run 2 | Run 3 | **Laagste** | **Hoogste** | Gemiddeld |
|---|---:|---:|---:|---:|---:|---:|
| v1 (week 2, `5f8639c`) | 70/80 = 87,5% | 71/80 = 88,8% | 71/80 = 88,8% | **70/80 = 87,5%** | **71/80 = 88,8%** | 70,7/80 = 88,3% |
| v1.2 (laatste, `d6acc91`) | 80/80 = 100% | 80/80 = 100% | 79/80 = 98,8% | **79/80 = 98,8%** | **80/80 = 100%** | 79,7/80 = 99,6% |

Het bereik van v1.2 (79 tot 80) ligt volledig boven dat van v1 (70 tot 71): de laagste run van v1.2 is nog 8 velden beter dan de hoogste run van v1.

## Welke fouten

**v1 (30 runs):** bijna elke fout komt in alle drie de runs van dezelfde input terug, dus dit zijn vaste fouten van de prompt, geen toeval.
- Lopende kosten niet opgeteld: T02 en T07 (0,20% of 0,3% in plaats van 0,25%), T04 (0,49% in plaats van 0,53%), T10 (0.14% in plaats van 0,16%), T03 ("niet vermeld" in plaats van 0,75%).
- Notatie niet omgezet: T04 ("13,600 USD", "6.3%"), T10 ("12,170 USD", "4.01%"), T02 ("10 650 USD" met spatie), T09 ("USD 20 210" met spatie). Het bedrag zelf was telkens wel juist.
- T01 run 1: uitkerend of accumulerend "niet vermeld" (runs 2 en 3 wel juist: wisselend).
- T04 run 1: extra tekst na het antwoord ("Opmerking: de tabel … door elkaar geraakt …"). Dat is de enige vormfout in v1; de vorm van de overige 29 runs is zuiver.
- Het scenario van de verkeerde kolom of een verschoven rendement (F1) kwam in v1 niet voor.

**v1.2 (30 runs):** één fout in 240 velden.
- T07 run 3: scenario 4.280 USD en -15,59% in plaats van 10.650 USD en 1,27% (verkeerde kolom, F1). Runs 1 en 2 van T07 waren juist: wisselend (F6).
- Alle 30 antwoorden hebben een zuivere vorm: geen extra tekst, geen tweede regel.
- Lopende kosten, notatie, uitkerend/accumulerend en de rendementen van T04, T05 en T06 (de plekken van de fouten in week 3) waren in alle drie de runs juist.

## Wat dit wel en niet zegt

- Bij v1 staat alles vast op 70 tot 71: de fouten zijn systematisch. Bij v1.2 is de overgebleven fout een scenariofout op één input in één van de drie runs. Dat past bij je eerdere bevinding (F1/F6 in de scenariotabel), maar met 3 runs is "kans op de scenariofout is ongeveer 1 op 30 per input" een schatting, geen meting.
- De foutmarge van v1.2 is op deze tien inputs ongeveer 0 tot 1 veld op 80 (0 tot 1,3%). Ze geldt voor deze tien KID's, deze pdf-uitlezing en dit model; een nieuw KID kan fouten geven die hier niet voorkomen.
- Dit is geen zuivere vergelijking van alleen de rendementsregel (zie de afwijking bovenaan), maar van v1 tegenover v1.2 als geheel.
- De 60 ruwe antwoorden staan in `build/foutmarge-runs/` (bestandsnaam `<versie>_<ID>_r<run>.txt`, bijvoorbeeld `v1.2_T07_r3.txt`), samen met `prompt-v1.md` (de prompt van week 2 uit git) en `score.py` (het scorescript, met de verwachte waarden overgenomen uit `test-set.md`). Lees er zelf een paar na, bijvoorbeeld `v1.2_T07_r3.txt` (de enige fout van v1.2) en `v1_T04_r1.txt` (de extra tekst).
