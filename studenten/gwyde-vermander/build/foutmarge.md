# Foutmarge, 21 oktober 2026

Model: Opus 5.5. n = 10, 3 runs per versie. Zelfde inputs voor beide.

Exact model-ID: `claude-opus-5-5` (de alias `opus` loste hiernaar op, gecheckt via `--output-format json`). v3 = `build/prompt.md`, v2 = `build/prompt-v2.md`. Inputs T01 tot T10 uit `build/test-set.md`, datum van vandaag ingevuld als 7 oktober 2026. Elke run een nieuwe, aparte sessie zonder tools en zonder mijn contextbestanden: `claude -p --model opus --tools ""` vanuit een lege map. Het model kreeg nooit de verwachte antwoorden te zien.

## Score per run

| Versie | Run 1 | Run 2 | Run 3 | Laagste | Hoogste | Spreiding |
|---|---:|---:|---:|---:|---:|---:|
| v2 | 7/10 | 8/10 | 7/10 | 7/10 | 8/10 | 1 |
| v3 | 8/10 | 7/10 | 8/10 | 7/10 | 8/10 | 1 |

## Antwoord per input per run

`(fout)` = wijkt af van het juiste antwoord uit mijn testset. Die verwachte antwoorden zijn niet aangepast.

| ID | Juiste antwoord | v2 run 1 | v2 run 2 | v2 run 3 | v3 run 1 | v3 run 2 | v3 run 3 |
|---|---|---|---|---|---|---|---|
| T01 | uitgeschakeld | uitgeschakeld | uitgeschakeld | uitgeschakeld | uitgeschakeld | uitgeschakeld | uitgeschakeld |
| T02 | in herstel | in herstel | in herstel | in herstel | in herstel | in herstel | in herstel |
| T03 | vermoeid | geen info (fout) | geen info (fout) | geen info (fout) | geen info (fout) | geen info (fout) | geen info (fout) |
| T04 | goed | goed | goed | goed | goed | goed | goed |
| T05 | geen info | geen info | geen info | geen info | geen info | geen info | geen info |
| T06 | geen info | goed (fout) | goed (fout) | goed (fout) | geen info | geen info | geen info |
| T07 | geen info | geen info | geen info | geen info | geen info | geen info | geen info |
| T08 | vermoeid | vermoeid | vermoeid | vermoeid | vermoeid | geen info (fout) | vermoeid |
| T09 | vermoeid | in herstel (fout) | vermoeid | goed (fout) | geen info (fout) | geen info (fout) | geen info (fout) |
| T10 | in herstel | in herstel | in herstel | in herstel | in herstel | in herstel | in herstel |

## Waar de schommeling zit

- v2, T09: in herstel / vermoeid / goed (juist: vermoeid)
- v3, T08: vermoeid / geen info / vermoeid (juist: vermoeid)

Alle andere inputs gaven drie keer hetzelfde label, juist of fout.

## Altijd fout, in alle drie de runs

- v2: T03 (vermoeid verwacht, geen info gekregen); T06 (geen info verwacht, goed gekregen)
- v3: T03 (vermoeid verwacht, geen info gekregen); T09 (vermoeid verwacht, geen info gekregen)

## Mijn claim

Mijn claim uit week 3 en 4: "v3 werkt beter dan v2."

Ingetrokken, want de bereiken overlappen volledig: v2 7 tot 8 op 10, v3 7 tot 8 op 10 (n = 10, 3 runs per versie, Opus 5.5). v3 lost T06 op, maar maakt T09 fout. Het verschil valt binnen de foutmarge.

## Correctie

In week 3 schreef ik dat mijn regel over gemengde signalen T03 fout maakte. Dat klopt niet: ook v2 heeft T03 drie keer fout. In week 4 schreef ik dat v3 stabiel is (geen F6); in deze test wisselt v3 bij T08.

## Foutmarge met n = 20 (27 oktober 2026)

Model: Opus 5.5, exact model-ID `claude-opus-5-5` (de alias `opus` loste hiernaar op, opnieuw gecheckt via `--output-format json`). n = 20, 3 runs per versie. v3 = `build/prompt.md`, v2 = `build/prompt-v2.md`.

T01 tot T10 komen uit de eerste foutmargetest hierboven (21 oktober 2026, datum van vandaag ingevuld als 7 oktober 2026). T11 tot T20 zijn nieuw gedraaid op 27 oktober 2026 met dezelfde werkwijze: dezelfde prompts, hetzelfde model, elke run een nieuwe, aparte sessie zonder tools en zonder mijn contextbestanden, `claude -p --model opus --tools ""` vanuit een lege map, datum van vandaag ingevuld als 27 oktober 2026. Het model kreeg nooit de verwachte antwoorden te zien; die zijn niet aangepast.

Score per run = run 1 van T01–T10 samen met run 1 van T11–T20, enzovoort.

## Score per run (n = 20)

| Versie | Run 1 | Run 2 | Run 3 | Laagste | Hoogste | Spreiding |
|---|---:|---:|---:|---:|---:|---:|
| v2 | 13/20 | 14/20 | 13/20 | 13/20 | 14/20 | 1 |
| v3 | 14/20 | 13/20 | 14/20 | 13/20 | 14/20 | 1 |

Opgesplitst: v2 haalde 7, 8 en 7 op de eerste tien en 6, 6 en 6 op de nieuwe tien. v3 haalde 8, 7 en 8 op de eerste tien en 6, 6 en 6 op de nieuwe tien.

## Antwoord per input per run (T11 tot T20)

`(fout)` = wijkt af van het juiste antwoord uit mijn testset. Die verwachte antwoorden zijn niet aangepast. Voor T01 tot T10 staan de antwoorden in de tabel van de eerste test hierboven.

| ID | Juiste antwoord | v2 run 1 | v2 run 2 | v2 run 3 | v3 run 1 | v3 run 2 | v3 run 3 |
|---|---|---|---|---|---|---|---|
| T11 | uitgeschakeld | uitgeschakeld | uitgeschakeld | uitgeschakeld | uitgeschakeld | uitgeschakeld | uitgeschakeld |
| T12 | in herstel | uitgeschakeld (fout) | uitgeschakeld (fout) | uitgeschakeld (fout) | uitgeschakeld (fout) | uitgeschakeld (fout) | uitgeschakeld (fout) |
| T13 | goed | goed | goed | goed | goed | goed | goed |
| T14 | uitgeschakeld | uitgeschakeld | uitgeschakeld | uitgeschakeld | uitgeschakeld | uitgeschakeld | uitgeschakeld |
| T15 | vermoeid | vermoeid | vermoeid | vermoeid | vermoeid | vermoeid | vermoeid |
| T16 | goed | geen info (fout) | geen info (fout) | geen info (fout) | geen info (fout) | geen info (fout) | geen info (fout) |
| T17 | geen info | vermoeid (fout) | vermoeid (fout) | vermoeid (fout) | vermoeid (fout) | vermoeid (fout) | vermoeid (fout) |
| T18 | goed | goed | goed | goed | goed | goed | goed |
| T19 | in herstel | vermoeid (fout) | geen info (fout) | vermoeid (fout) | geen info (fout) | geen info (fout) | geen info (fout) |
| T20 | goed | goed | goed | goed | goed | goed | goed |

## Waar de schommeling zit (T11 tot T20)

- v2, T19: vermoeid / geen info / vermoeid (juist: in herstel) — fout in alle drie de runs, maar niet met hetzelfde label
- v3: geen enkele input wisselt; alle tien geven drie keer hetzelfde label, juist of fout

## Altijd fout, in alle drie de runs (T11 tot T20)

- v2: T12, T16, T17, T19
- v3: T12, T16, T17, T19

Samen met de eerste tien: v2 is altijd fout op T03, T06, T12, T16, T17, T19; v3 op T03, T09, T12, T16, T17, T19.

## Wat dit verandert aan mijn claim

Niets. De bereiken overlappen nog steeds volledig: v2 13 tot 14 op 20, v3 13 tot 14 op 20 (n = 20, 3 runs per versie, Opus 5.5). Met tien inputs meer is het verschil tussen v2 en v3 nog steeds niet aantoonbaar. De nieuwe tien inputs zijn wel moeilijker: beide versies halen daar 6 op 10, tegenover 7 tot 8 op 10 op de eerste tien.
