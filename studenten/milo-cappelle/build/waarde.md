# Waarde — hoeveel tijd wint mijn tool?

18 oktober 2026. Deprez leest nu geen bouwaanvragen: werk komt via aannemers, telefoontjes en mond-tot-mondreclame. De ketting vergelijkt de tool dus met iemand die het met de hand zou doen, niet met vandaag (0 uur).

| Schakel | Laag | Hoog | Bron |
|---|---|---|---|
| 1. Met de hand | openen 10 s · lezen 40 s · beslissen 30 s · noteren 10 s = **90 s** | idem | zelf, met een aanvraag van Roeselare |
| 2. Met de tool | erin krijgen 15 s · draaien 5 s · nakijken 30 s = **50 s** | idem | zelf geschat; draaien: meting week 4 |
| 3. Winst per aanvraag | 90 − 50 = **40 s** | idem | |
| 4. Volume | ± 25 per dag · 124 per week · 496 per maand · **5.952 per jaar** | ± 81 per dag · 403 per week · 1.612 per maand · **19.344 per jaar** | geteld: Zonnebeke 8, Roeselare 26 aanvragen (18/9–18/10/2026), × 62 gemeenten West-Vlaanderen. Aanname: 20 werkdagen en 4 weken per maand, 12 maanden per jaar |
| 5. Uren gewonnen | ± 17 min per dag · 1,4 u per week · 5,5 u per maand · **66 u per jaar** | ± 54 min per dag · 4,5 u per week · 17,9 u per maand · **215 u per jaar** | |
| 6. Uurkost | **€21,25** (€3.500 bruto ÷ 164,7 u) | **€24,29** (€4.000 bruto ÷ 164,7 u) | brutoloon bediende bij Deprez, eigen schatting; 38 u per week. Loonkost voor de werkgever ligt hoger, dus voorzichtig |
| 7. Kost van de tool | 5.952 × €0,0028 = **± €17 per jaar** | 19.344 × €0,0028 = **± €54 per jaar** | `kosten.md`, Haiku 4.5, jouw deel |
| 8. Netto per jaar | 66 u × €21,25 − €17 = **± €1.388** | 215 u × €24,29 − €54 = **± €5.166** | |
| 9. Zwakste cijfer | het volume: maar twee gemeenten geteld. Is het de helft: 33 u en **± €694** per jaar | de helft: 107 u en **± €2.583** per jaar | |

---

## Week 5: de value chain met de foutmarge erin

27 oktober 2026. Hieronder staat dezelfde ketting als hierboven, met twee veranderingen. Eén: de tool heeft fouten, en iemand moet die herstellen. Twee: de uurkost is wat de werkgever betaalt, niet het bruto.

**Welke score?** De score op "interessant" van v2, want dat is de versie die je in week 4 gebruikte. Uit `foutmarge.md`: 11 tot 13 van 14 juist. Het gemiddelde is 12. Het fouten-percentage is dus 1/14 tot 3/14, en het gemiddelde 2/14.

**Welk volume?** Het lage volume uit week 4 (496 per maand, 5.952 per jaar). Het hoge volume staat in de laatste kolom.

**Welke uurkost?** Bruto €3.500 per maand is €21,25 per uur (÷ 164,7 uur). Vuistregel bruto × 1,5 geeft €31,88 voor de werkgever. Bron: vuistregel uit de week-5-README (Acerta, Securex, Teamed). Brutoloon is een eigen schatting.

**Fouten herstellen** = foutenpercentage × 90 s (de tijd om één aanvraag met de hand te doen).

| Schakel | Score 11/14 (laag) | Score 12/14 (gemiddeld) | Score 13/14 (hoog) |
|---|---:|---:|---:|
| 1. Met de hand | 90 s | 90 s | 90 s |
| 2. Met de tool: erin 15 s + draaien 5 s + nakijken 30 s + fouten herstellen | 50 + 19,3 = **69,3 s** | 50 + 12,9 = **62,9 s** | 50 + 6,4 = **56,4 s** |
| 3. Winst per aanvraag | 90 − 69,3 = **20,7 s** | **27,1 s** | **33,6 s** |
| 4. Volume | 5.952 per jaar | 5.952 per jaar | 5.952 per jaar |
| 5. Uren gewonnen per jaar | **34 u** | **45 u** | **56 u** |
| 6. Uurkost werkgever | €31,88 | €31,88 | €31,88 |
| 7. Waarde | €1.092 | €1.430 | €1.769 |
| 8. Min kost tool (5.952 × €0,0028) | − €17 | − €17 | − €17 |
| **Netto per jaar** | **± €1.075** | **± €1.414** | **± €1.753** |

**Bij het hoge volume** (19.344 per jaar) en dezelfde uurkost van de werkgever: netto ± €4.001 (11/14), ± €5.259 (12/14), ± €6.517 (13/14). De kost van de tool: 19.344 × €0,0028 = ± €54 per jaar.

**Het bereik** (stap 9): van ± €1.075 tot ± €1.753 per jaar bij het lage volume. Een groot deel van dat bereik komt door de score: elke extra juiste score op 14 is ± 340 euro per jaar, en het verschil tussen 11 en 13 is dus ± 680 euro.

**Zwakste cijfer** (stap 10). De 90 s voor het handwerk is geschat, niet gemeten. Dat cijfer weegt het zwaarst:
- Bij 60 s in plaats van 90 s, en score 12/14: de winst per aanvraag is nog maar 1,4 s. Dan verdwijnt bijna alle waarde.
- De uurkost is een schatting van het brutoloon. Dat is de tweede onzekerheid.

Conclusie: de score (11 tot 13 van 14) verschuift het netto met ± €680 per jaar. De schatting van het handwerk verschuift het veel meer.
