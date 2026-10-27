# Foutmarge, 27 oktober 2026

Model: Claude Haiku 5.5 (`claude-haiku-5-5`, gecontroleerd in de uitvoer van elke run). n = 10 (T01–T10), 3 runs per versie. Zelfde inputs voor beide.
Elke run een nieuwe sessie, alleen de prompt en het bericht, zonder tools (`claude -p --model claude-haiku-5-5 --tools ""`), vanuit een lege map. Verwachte antwoorden niet aangepast.

- v1 = `prompt-v1.md` (zonder de regel voor `A x B`)
- v2 = `prompt.md` (met de regel voor `A x B` en `12X12`, week 3)

Nagekeken met dezelfde regel als in week 4: kleine verschillen in de naam of extra woorden in `notitie` zijn geen fout.

| Versie | Run 1 | Run 2 | Run 3 | Foutmarge (min–max) |
|---|---:|---:|---:|---:|
| v1 | 7/10 | 9/10 | 8/10 | 7–9 |
| v2 | 9/10 | 9/10 | 9/10 | 9–9 |

## Per input: aantal juist op 3 runs

| ID | v1 | v2 | Fout |
|---|---:|---:|---|
| T01 | 3 | 3 | |
| T02 | 1 | 0 | F3: lopen niet herkend, `5 km in 36 min` in notitie |
| T03 | 3 | 3 | |
| T04 | 3 | 3 | |
| T05 | 3 | 3 | |
| T06 | 3 | 3 | |
| T07 | 3 | 3 | |
| T08 | 3 | 3 | |
| T09 | 2 | 3 | v1 run 1: F3, lopen niet herkend |
| T10 | 0 | 3 | v1: gewicht `?` in plaats van 12 |

Twijfelgeval: v2 run 1 van T01 gaf een lege `notitie` in plaats van `?`. De cijfers kloppen, dus geteld als juist.

Mijn claim (week 3): "De regel voor `12X12` lost T10 op."
Bevestigd of ingetrokken: **ingetrokken** voor de totale score, want de bereiken raken elkaar (v1 7–9, v2 9–9). De laagste score van v2 (9) ligt niet hoger dan de hoogste van v1 (9).
Wel: T10 ging van 0 op 3 naar 3 op 3. Die ene input is wel beter. T02 blijft de zwakke plek (1 op 6 juist over beide versies).

Kost van de 60 runs samen: $0,087 (hele run, inclusief systeemprompt van Claude Code). Gemiddeld ± 600 output-tokens per run.
