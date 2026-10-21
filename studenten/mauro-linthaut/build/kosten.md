# Kosten per run

Datum meting: 14 oktober 2026. Input: T01 (Xtrackers NASDAQ 100, `kid/3.pdf`), prompt v1 met voorbeelden.

## Ronde 1: één run

Jouw deel = alleen de prompt met het KID erin (zonder Claude Code zelf), zo afgesproken met de docent. Schatting: ± 13k tokens in en ± 0,5k uit. Bron: de Haiku-regel van `/cost` (12,9k in, 339 uit), die qua grootte past bij prompt + KID van T01 (27 KB). Niet exact gescheiden van Claude Code. Prijzen uit de README, 1 dollar = 0,90 euro (koers van de dag 0,89, verschil ± 1%).

| Model | Jouw deel | Kost per run | Per maand (6) | 10× (60) | 1.000× (6.000) |
|---|---|---:|---:|---:|---:|
| Sonnet 5.5 (2 / 10 dollar) | 13k in + 0,5k uit | $0,031 = ± €0,028 | ± €0,17 | ± €1,67 | ± €167 |
| Haiku 4.5 (1 / 5 dollar) | 13k in + 0,5k uit | $0,0155 = ± €0,014 | ± €0,08 | ± €0,84 | ± €84 |
| **Haiku 5.5 (0,10 / 0,50 dollar), gecorrigeerd in week 5** | 13k in + 0,5k uit | $0,00155 = ± €0,0014 | ± €0,008 | ± €0,084 | ± €8,40 |

**Gecorrigeerd in week 5:** de regel "Haiku 4.5" hierboven is fout. In week 4 typte ik `/model haiku` en kreeg waarschijnlijk Haiku 5.5, maar rekende met de prijs van 4.5. Prijzen per miljoen tokens van 21 oktober 2026 (README week 5, bron: Anthropic): Haiku 5.5 0,10 input en 0,50 output. Rekensom voor mijn deel: 13.000 × 0,10 / 1.000.000 = $0,0013, plus 500 × 0,50 / 1.000.000 = $0,00025. Samen $0,00155, met 1 dollar = €0,90 ± €0,0014. De oude regel laat ik staan. Ik heb niet zelf `/cost` opnieuw gedraaid om de modelnaam te zien. Dat het 5.5 was, volgt uit de rekensom (zie het open punt hieronder), niet uit een nieuwe meting.

**Volume:** 4 tot 12 runs per maand, gemiddeld 6 (2 onderzoeken x 2 tot 4 ETF's, eigen schatting, zie `scenario.md`).

**Open punt:** `/cost` toonde $0,0015 voor de Haiku-regel, de README-prijs geeft $0,0146 voor hetzelfde. Factor 10 verschil, nog uitzoeken (prijspagina Anthropic). Ook bij een factor 10 meer blijft de kost op jaarbasis klein tegenover de waarde.

**Gecorrigeerd in week 5:** het verschil is verklaard. De $0,0015 van `/cost` past op Haiku 5.5: 12,9k in × 0,10 / 1M = $0,00129, plus 339 uit × 0,50 / 1M = $0,00017, samen $0,00146. Mijn README-prijs was die van Haiku 4.5, en die is tien keer duurder. Open punt gesloten.

## Vanaf welk volume doet de kost ertoe?

- Winst per run: 9,7 min x 15 euro per uur = 2,42 euro. Kost per run: ± 0,028 euro (Sonnet), dus ± 1% van de winst.
- De kost wint van de winst pas bij ± 86 keer de kost per run, of als nakijken ± 11,7 min duurt. Op mijn volume gebeurt dat niet.
- De kost wordt een budgetpost rond 100 euro per maand: ± 3.600 runs per maand met Sonnet, ± 7.100 met Haiku (600 keer mijn volume).
  Gecorrigeerd in week 5: met Haiku 5.5 is dat ± 71.000 runs per maand (100 / €0,0014), dus ± 12.000 keer mijn volume.
- Bij 1.000x (6.000 runs, 167 euro per maand) is nakijken het probleem: 6.000 x 2,8 min = ± 280 uur per maand.

**Conclusie:** voor mij is de API-kost nooit het argument (± 2 euro per jaar). Bij een groot volume is het nakijken de beperking.

## Waarde: met de hand of met de tool? (geschat, 14 oktober 2026)

| Schakel | Waarde | Bron |
|---|---|---|
| Met de hand | KID zoeken ± 10 s · velden opzoeken 7 tot 10 min · noteren 3 tot 5 min = **± 12,5 min per ETF** (10 tot 15) | eigen schatting |
| Met de tool | zoeken 10 s · draaien ± 40 s · nakijken 2 min (ik controleer, ook het scenario) = **± 2,8 min** | draaien gemeten (wall 40 s), nakijken geschat |
| Winst per ETF | 12,5 − 2,8 = **± 9,7 min** (7,2 tot 12,2) | |
| Volume | 6 per maand, 72 per jaar (48 tot 144) | 2 onderzoeken × 2 tot 4 ETF's, eigen schatting |
| Uren per jaar | 72 × 9,7 min = **± 11,6 u** (5,7 tot 29) | |
| Uurkost | **€15** | aanname: studentenjob-uurloon |
| Waarde | 11,6 × 15 = **± €174 per jaar** (€85 tot €438) | |
| Kost van de tool | ± €2 per jaar (voorlopig, meting klopt nog niet). Gecorrigeerd in week 5: de meting klopt nu. Voor Sonnet blijft het ± €2 (72 × €0,028), voor Haiku 5.5 is het ± €0,10 (72 × €0,0014) | |
| Netto | **± €172 per jaar** | |
| Zwakste cijfer | **Nakijken: 2 min.** Geschat, en de tool maakte fouten bij het scenario (verkeerde kolom). Is het 5 min: tool 5,8 min, winst 6,7 min per ETF, 8 u per jaar, ± €120 waarde, netto ± €118. De tool levert pas niets meer op bij ± 11,7 min nakijken. | berekend |

## Value chain met de foutmarge erin (week 5, 21 oktober 2026)

Tool: Sonnet 5.5, medium (setup A in `modellen.md`). Score: v1.2, 9 tot 10 van 10 KID's volledig juist (n = 10, 3 runs, `foutmarge.md`), dus 0 tot 10% van de KID's heeft een fout.

| Schakel | Waarde | Bron |
|---|---|---|
| Met de hand | KID zoeken ± 10 s · velden opzoeken 7 tot 10 min · noteren 3 tot 5 min = **± 12,5 min per ETF** | eigen schatting |
| Met de tool | draaien ± 40 s · nakijken 2 min · fouten herstellen (deel fout × 12,5 min) | draaien gemeten, nakijken geschat |
| Met de tool, per score | 10/10: 2,7 min · 9/10: 3,9 min (met 1,25 min voor fouten herstellen) | berekend |
| Winst per ETF | **9,8 min** bij 10/10 · **8,6 min** bij 9/10 | berekend |
| Volume | 72 per jaar (48 tot 144) | eigen schatting, `scenario.md` |
| Uren per jaar | **11,8 u** bij 10/10 · **10,3 u** bij 9/10 | berekend |
| Uurkost | **€22,50 per uur voor de werkgever** (€15 bruto × 1,5). Gecorrigeerd in week 5: eerst €15 | aanname: mijn bruto uurloon × 1,5 (README week 5, stap 6) |
| Waarde | **€265** bij 10/10 · **€232** bij 9/10. Gecorrigeerd in week 5: eerst €177 en €154 | berekend |
| Kost van de tool | 72 × €0,036 = **± €2,61 per jaar** | `modellen.md` (gemeten tokens, README-prijs) |
| Netto per jaar | **± €262** bij 10/10 · **± €230** bij 9/10. Gecorrigeerd in week 5: eerst ± €174 en ± €152 | berekend |
| Bereik | **± €230 tot ± €262** per jaar. Gecorrigeerd in week 5: eerst ± €152 tot ± €174 | foutmarge |
| Zwakste cijfer | **Nakijken: 2 min.** Geschat, en de tool maakte fouten in het scenario. Is het 5 min, dan blijft er ± €177 netto over bij 10/10 en ± €144 bij 9/10. Gecorrigeerd in week 5: eerst ± €120 (met €15 per uur). | berekend |

**Wat zwaarder weegt dan de foutmarge:** de foutmarge verschuift het netto met ± €32. Het volume doet veel meer: bij 48 per jaar ± €153 tot ± €175, bij 144 per jaar ± €459 tot ± €524. Ook de nakijktijd weegt zwaarder dan de score.

**Gecorrigeerd in week 5:** ik rekende eerst met €15 per uur, mijn bruto uurloon. De README vraagt de kost voor de werkgever: bruto × 1,5 = €22,50. Alle cijfers van deze value chain zijn daarom opnieuw berekend. De oude waarden staan er telkens bij. De eerdere kopjes in dit bestand (week 4, "Waarde: met de hand of met de tool?" en "Vanaf welk volume doet de kost ertoe?") staan nog op €15.
