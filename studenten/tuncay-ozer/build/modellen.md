# Modellen, 27 oktober 2026

## Mijn gok (geschreven vóór de runs)

- Best scoort: **Opus 5.5**, want het is het slimste model.
- Goed genoeg voor mijn echte plek: **Sonnet 5.5**, voor de prijs/kwaliteit.

## Resultaat

Laatste prompt (`prompt.md`, v2), T01–T10, één run per setup, elke run een nieuwe sessie zonder tools, vanuit een lege map: `claude -p --model <model> --effort medium --tools ""`. Model gecontroleerd in de uitvoer van elke run. Verwachte antwoorden niet aangepast.

| Setup | Model | Effort | Score (n = 10, 1 run) | Binnen mijn foutmarge? | Output-tokens per run | Kost per run | Per jaar |
|---|---|---|---:|---|---:|---:|---:|
| A | Sonnet 5.5 | medium | 10/10 | Net erboven (foutmarge v2: 9–9), maar 1 run | 93 | $0,0051 | $1,35 ≈ €1,22 |
| B | Haiku 5.5 | medium | 9/10 | Ja | 567 | $0,0005 | $0,13 ≈ €0,12 |
| C | Opus 5.5 | medium | 9/10 | Ja | 189 | $0,0122 | $3,22 ≈ €2,89 |

Fouten:
- B, T02: F3, lopen niet herkend (`5 km in 36 min` in notitie). Zelfde fout als in de foutmargetest.
- C, T06: `notitie` is `?`, verwacht was `vorige week 77,5`. Let op: mijn prompt zegt "Anders is `notitie` `?`" als er een oefening is. Opus volgde de prompt, mijn verwachte antwoord zegt iets anders. Te beslissen voor de volgende run, niet nu aangepast.

Kost per run = 2,1k input-tokens (mijn deel, uit week 4) × inputprijs + gemiddelde output-tokens × outputprijs. Per jaar = 264 runs (22 per maand × 12). Prijzen: README week 5. Euro: 1 dollar = 0,90 euro.

Opvallend: Haiku denkt het meest (567 output-tokens), Sonnet het minst (93). Toch blijft Haiku de goedkoopste, door de lage prijs.

Mijn foutmarge is gemeten op Haiku. Of Sonnet ook schommelt, weet ik niet: daarvoor heb ik maar 1 run.

## Mijn keuze

Deze taak draait op **Sonnet 5.5, effort medium**, omdat Sonnet alles juist had en bijna 2× goedkoper is dan Opus.

Mijn gok: Opus het best, klopte niet (Sonnet 10/10, Opus 9/10). Sonnet als goed genoeg, klopte wel.
