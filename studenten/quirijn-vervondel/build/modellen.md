# Modellen en effort, 27 oktober 2026

Gok (geschreven vóór de runs, 27 oktober 2026): C (Opus) scoort het best, maar A (Sonnet) is goed genoeg voor Jasper. B (Haiku) mist meer onderdelen.

## Modeltest

Prompt: `prompt.md` (v1, de laatste versie), met dezelfde 10 inputs uit `test-set.md`. Elke setup één run, elke run in een nieuwe sessie zonder tools: `claude -p --model <model> --effort medium --tools ""`. Effort is medium voor alle drie, want alleen A was met een effort genoemd. Dezelfde verwachte antwoorden en dezelfde beoordeling als in `foutmarge.md`.

Foutmarge om mee te vergelijken: alleen gemeten met Haiku (v1, 3 runs): 0 tot 2 inputs, en 77 tot 80 onderdelen van 96.

| Setup | Model | Effort | Score | Binnen foutmarge? | Output-tokens per run | Kost per run | Per jaar |
|---|---|---|---|---|---:|---:|---:|
| A | claude-sonnet-5-5 | medium | 1/10 inputs, 79/96 onderdelen (T06 tot T10: 26/34) | Ja: 79 ligt binnen 77 tot 80 | 828 | € 0,012 | € 1,43 |
| B | claude-haiku-5-5 | medium | 0/10 inputs, 76/96 onderdelen (T06 tot T10: 25/34) | Net nee: 76 ligt 1 onder 77 tot 80 | 1.630 | € 0,0010 | € 0,12 |
| C | claude-opus-5-5 | medium | 3/10 inputs, 87/96 onderdelen (T06 tot T10: 26/34) | Nee: 87 ligt boven 77 tot 80 | 971 | € 0,026 | € 3,18 |

Per input juist: A alleen T05. B geen. C T01, T02 en T05. Verzonnen rij: A en C bij T04 (een verloopstuk dat niet in de notities staat).

Kost per run: jouw formule, 2.500 input-tokens × inputprijs + output-tokens × outputprijs, met $1 = € 0,90. Per jaar: × 120 runs (10 per maand). De CLI rekende gemiddeld meer, omdat Claude Code zijn eigen systeemprompt meestuurt (ongeveer 3.500 tokens input per run): gemiddeld $0,022 voor A, $0,0009 voor B en $0,037 voor C per run.

Let op: elke setup is één run. Het verschil van 8 onderdelen tussen A en C is dus één meting. Alleen het Haiku-bereik is met drie runs gemeten.

**Gok en uitkomst:** C scoort inderdaad het best (87 tegenover 79 en 76). B mist meer onderdelen dan A, maar het verschil is klein (3 onderdelen). Of A "goed genoeg" is, hangt af van hoeveel Jasper mag missen: A mist 17 onderdelen, C mist 9.

Deze taak draait op Opus 5.5, met effort medium, omdat het in deze run 87 van 96 onderdelen haalde (Sonnet 79, Haiku 76) en het kostenverschil minder dan € 2 per jaar is.
