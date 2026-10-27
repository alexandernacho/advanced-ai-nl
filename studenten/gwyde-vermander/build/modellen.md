# Modellen, 21 oktober 2026

## Mijn gok (geschreven vóór de runs)

De beste score zal komen van model C. Zelf denk ik dat voor mijn versie 1 (de teksten lezen) model A goed genoeg zal zijn. Later, wanneer ik statistieken erbij wil betrekken, denk ik dat ik model C nodig zal hebben. Het model dat ik nu denk dat nodig is, is model A.

## Resultaat

Eén run per input per setup, met mijn laatste prompt (`build/prompt.md`, v3) en de inputs T01 tot T10 uit `build/test-set.md`, datum van vandaag ingevuld als 7 oktober 2026. Elke run een nieuwe, aparte sessie zonder tools en zonder mijn contextbestanden: `claude -p --model <model> --effort medium --tools ""` vanuit een lege map. Het model kreeg nooit de verwachte antwoorden te zien; die zijn niet aangepast.

Kost per run = 13.400 input-tokens (mijn deel uit week 4) × de inputprijs + de gemiddelde output-tokens van die setup × de outputprijs. Prijzen per miljoen tokens: Haiku 5.5 $ 0,10 / $ 0,50, Sonnet 5.5 $ 2 / $ 10, Opus 5.5 $ 4 / $ 20. 1 dollar = 0,90 euro. Zelf gerekend, niet overgenomen uit `/cost` of de JSON-uitvoer.

| Setup | Model | Effort | Score (n = 10, 1 run) | Binnen mijn foutmarge (7 tot 8 op 10)? | Output-tokens per run (gemiddeld) | Kost per run | Per jaar (950 runs) |
|---|---|---|---:|---|---:|---:|---:|
| A | Sonnet 5.5 | medium | 8/10 | ja | 191 | $ 0,02871 = € 0,0258 | € 24,55 |
| B | Haiku 5.5 | medium | 7/10 | ja | 611 | $ 0,00165 = € 0,0015 | € 1,41 |
| C | Opus 5.5 | medium | 8/10 | ja | 237 | $ 0,05835 = € 0,0525 | € 49,89 |

## Antwoord per input per setup

`(fout)` = wijkt af van het juiste antwoord uit mijn testset.

| ID | Juiste antwoord | A (Sonnet 5.5) | B (Haiku 5.5) | C (Opus 5.5) |
|---|---|---|---|---|
| T01 | uitgeschakeld | uitgeschakeld | uitgeschakeld | uitgeschakeld |
| T02 | in herstel | uitgeschakeld (fout) | in herstel | in herstel |
| T03 | vermoeid | vermoeid | geen info (fout) | geen info (fout) |
| T04 | goed | goed | goed | goed |
| T05 | geen info | geen info | geen info | geen info |
| T06 | geen info | geen info | geen info | geen info |
| T07 | geen info | geen info | geen info | geen info |
| T08 | vermoeid | vermoeid | vermoeid | vermoeid |
| T09 | vermoeid | geen info (fout) | geen info (fout) | geen info (fout) |
| T10 | in herstel | in herstel | geen info (fout) | in herstel |


## Foutmarge Haiku 5.5 (3 runs)

Model: `claude-haiku-5-5`, effort medium. n = 10, 3 runs. Run 1 is de bestaande run uit de modeltest hierboven; run 2 en 3 zijn op exact dezelfde manier gedraaid: prompt v3, dezelfde inputs, datum van vandaag 7 oktober 2026, `claude -p --model claude-haiku-5-5 --effort medium --tools ""` in een nieuwe, aparte sessie vanuit een lege map. Het model kreeg nooit de verwachte antwoorden te zien; die zijn niet aangepast.

| Run 1 | Run 2 | Run 3 | Laagste | Hoogste |
|---:|---:|---:|---:|---:|
| 7/10 | 8/10 | 7/10 | 7/10 | 8/10 |

Gemiddelde output-tokens per run: run 1 611, run 2 530, run 3 526. Over de drie runs samen: 555 per run.

| ID | Juiste antwoord | Run 1 | Run 2 | Run 3 |
|---|---|---|---|---|
| T01 | uitgeschakeld | uitgeschakeld | uitgeschakeld | uitgeschakeld |
| T02 | in herstel | in herstel | in herstel | in herstel |
| T03 | vermoeid | geen info (fout) | vermoeid | geen info (fout) |
| T04 | goed | goed | goed | goed |
| T05 | geen info | geen info | geen info | geen info |
| T06 | geen info | geen info | geen info | geen info |
| T07 | geen info | geen info | geen info | geen info |
| T08 | vermoeid | vermoeid | vermoeid | vermoeid |
| T09 | vermoeid | geen info (fout) | geen info (fout) | geen info (fout) |
| T10 | in herstel | geen info (fout) | geen info (fout) | geen info (fout) |

Wisselt tussen de runs: T03 (geen info / vermoeid / geen info, juist: vermoeid).

Alle drie de runs fout: T09 (vermoeid verwacht, geen info gekregen); T10 (in herstel verwacht, geen info gekregen).


## Foutmarge Sonnet 5.5 (3 runs)

Model: `claude-sonnet-5-5`, effort medium. n = 10, 3 runs. Run 1 is de bestaande run uit de modeltest hierboven; run 2 en 3 zijn op exact dezelfde manier gedraaid: prompt v3, dezelfde inputs, datum van vandaag 7 oktober 2026, `claude -p --model claude-sonnet-5-5 --effort medium --tools ""` in een nieuwe, aparte sessie vanuit een lege map. Het model kreeg nooit de verwachte antwoorden te zien; die zijn niet aangepast.

| Run 1 | Run 2 | Run 3 | Laagste | Hoogste |
|---:|---:|---:|---:|---:|
| 8/10 | 8/10 | 8/10 | 8/10 | 8/10 |

Gemiddelde output-tokens per run: run 1 191, run 2 206, run 3 176. Over de drie runs samen: 191 per run.

| ID | Juiste antwoord | Run 1 | Run 2 | Run 3 |
|---|---|---|---|---|
| T01 | uitgeschakeld | uitgeschakeld | uitgeschakeld | uitgeschakeld |
| T02 | in herstel | uitgeschakeld (fout) | in herstel | in herstel |
| T03 | vermoeid | vermoeid | geen info (fout) | geen info (fout) |
| T04 | goed | goed | goed | goed |
| T05 | geen info | geen info | geen info | geen info |
| T06 | geen info | geen info | geen info | geen info |
| T07 | geen info | geen info | geen info | geen info |
| T08 | vermoeid | vermoeid | vermoeid | vermoeid |
| T09 | vermoeid | geen info (fout) | geen info (fout) | geen info (fout) |
| T10 | in herstel | in herstel | in herstel | in herstel |

Wisselt tussen de runs: T02 (uitgeschakeld / in herstel / in herstel, juist: in herstel); T03 (vermoeid / geen info / geen info, juist: vermoeid).

Alle drie de runs fout: T09 (vermoeid verwacht, geen info gekregen).

## Drie modellen, 3 runs elk

| Model | Run 1 | Run 2 | Run 3 | Bereik | Kost per run | Per jaar (950 runs) |
|---|---:|---:|---:|---|---:|---:|
| Haiku 5.5 | 7/10 | 8/10 | 7/10 | 7 tot 8 op 10 | € 0,0015 | € 1,41 |
| Sonnet 5.5 | 8/10 | 8/10 | 8/10 | 8 op 10 | € 0,0258 | € 24,55 |
| Opus 5.5 | 8/10 | 7/10 | 8/10 | 7 tot 8 op 10 | € 0,0525 | € 49,89 |

Waar de runs vandaan komen: Haiku 5.5 uit "Foutmarge Haiku 5.5" hierboven, Sonnet 5.5 uit "Foutmarge Sonnet 5.5" hierboven, Opus 5.5 uit de drie v3-runs in `build/foutmarge.md`. Kost per run en per jaar zijn overgenomen uit de tabel bij "Resultaat" bovenaan dit bestand.

Let op bij het vergelijken: de Haiku- en Sonnet-runs zijn gedraaid met `--effort medium`, de Opus-runs in `build/foutmarge.md` zonder die vlag, dus met de standaard effort. Op dat ene punt zijn de drie reeksen niet identiek.

## Mijn keuze

Deze taak draait op Sonnet 5.5, met effort medium, omdat het in 3 runs telkens 8/10 haalt (n = 10), al wisselt het per input bij T02 en T03. Haiku 5.5 haalt 7 tot 8 op 10 en is 17 keer goedkoper, maar ik wil een model dat consequenter scoort. Voor Sporza is het verschil in kost klein: ± € 24,55 per jaar met Sonnet tegenover ± € 1,41 met Haiku (950 runs).

Klopte mijn gok? Deels: ik gokte dat Opus het best zou scoren, maar Sonnet scoorde even goed of beter, voor de helft van de prijs. Dat Sonnet goed genoeg is, klopte wel.

Later wil ik statistieken aan mijn taak toevoegen. Daarvoor is misschien Opus nodig. Dan moet ik mijn testset opnieuw laten draaien om te zien welk model het meest accuraat is.

## Drie modellen met n = 20 (27 oktober 2026)

Prompt v3 (`build/prompt.md`) voor alle drie de modellen. Exacte model-ID's, gecheckt via `--output-format json`: `claude-haiku-5-5`, `claude-sonnet-5-5`, `claude-opus-5-5`.

T01 tot T10 komen uit de bestaande reeksen hierboven (21 oktober 2026, datum van vandaag ingevuld als 7 oktober 2026): Haiku uit "Foutmarge Haiku 5.5", Sonnet uit "Foutmarge Sonnet 5.5", Opus uit de drie v3-runs in `build/foutmarge.md`. T11 tot T20 zijn nieuw gedraaid op 27 oktober 2026 met dezelfde werkwijze: elke run een nieuwe, aparte sessie zonder tools en zonder mijn contextbestanden, vanuit een lege map, datum van vandaag ingevuld als 27 oktober 2026, met `claude -p --model claude-haiku-5-5 --effort medium --tools ""`, `claude -p --model claude-sonnet-5-5 --effort medium --tools ""` en voor Opus de v3-runs met `claude -p --model opus --tools ""`. Het model kreeg nooit de verwachte antwoorden te zien; die zijn niet aangepast.

| Model | Run 1 | Run 2 | Run 3 | Bereik (op 20) | Gemiddelde output-tokens per run |
|---|---:|---:|---:|---|---:|
| Haiku 5.5 | 13/20 | 14/20 | 13/20 | 13 tot 14 op 20 | 498 |
| Sonnet 5.5 | 14/20 | 14/20 | 14/20 | 14 op 20 | 191 |
| Opus 5.5 | 14/20 | 13/20 | 14/20 | 13 tot 14 op 20 | 236 |

De output-tokens zijn gemeten op de nieuwe runs (T11 tot T20), per input gemiddeld over de drie runs: Haiku 497, 509 en 487; Sonnet 191, 188 en 194; Opus 230, 245 en 235. Voor T01 tot T10 staan de output-tokens in de delen hierboven. Ik tel ze niet samen tot één getal over twintig inputs, omdat voor Opus alleen van run 1 van de eerste tien een tokenaantal genoteerd staat.

## Antwoord per input per model per run (T11 tot T20)

`(fout)` = wijkt af van het juiste antwoord uit mijn testset. Voor T01 tot T10 staan de antwoorden in de tabellen hierboven.

| ID | Juiste antwoord | Haiku r1 | Haiku r2 | Haiku r3 | Sonnet r1 | Sonnet r2 | Sonnet r3 | Opus r1 | Opus r2 | Opus r3 |
|---|---|---|---|---|---|---|---|---|---|---|
| T11 | uitgeschakeld | uitgeschakeld | uitgeschakeld | uitgeschakeld | uitgeschakeld | uitgeschakeld | uitgeschakeld | uitgeschakeld | uitgeschakeld | uitgeschakeld |
| T12 | in herstel | uitgeschakeld (fout) | uitgeschakeld (fout) | uitgeschakeld (fout) | uitgeschakeld (fout) | uitgeschakeld (fout) | uitgeschakeld (fout) | uitgeschakeld (fout) | uitgeschakeld (fout) | uitgeschakeld (fout) |
| T13 | goed | goed | goed | goed | goed | goed | goed | goed | goed | goed |
| T14 | uitgeschakeld | uitgeschakeld | uitgeschakeld | uitgeschakeld | uitgeschakeld | uitgeschakeld | uitgeschakeld | uitgeschakeld | uitgeschakeld | uitgeschakeld |
| T15 | vermoeid | vermoeid | vermoeid | vermoeid | vermoeid | vermoeid | vermoeid | vermoeid | vermoeid | vermoeid |
| T16 | goed | geen info (fout) | geen info (fout) | geen info (fout) | geen info (fout) | geen info (fout) | geen info (fout) | geen info (fout) | geen info (fout) | geen info (fout) |
| T17 | geen info | vermoeid (fout) | vermoeid (fout) | vermoeid (fout) | vermoeid (fout) | vermoeid (fout) | vermoeid (fout) | vermoeid (fout) | vermoeid (fout) | vermoeid (fout) |
| T18 | goed | goed | goed | goed | goed | goed | goed | goed | goed | goed |
| T19 | in herstel | geen info (fout) | geen info (fout) | geen info (fout) | geen info (fout) | geen info (fout) | geen info (fout) | geen info (fout) | geen info (fout) | geen info (fout) |
| T20 | goed | goed | goed | goed | goed | goed | goed | goed | goed | goed |

Op de nieuwe tien inputs geven de drie modellen exact dezelfde tien labels, in alle drie de runs: 6 op 10, met T12, T16, T17 en T19 altijd fout. Het verschil tussen de modellen op n = 20 komt dus volledig van de eerste tien inputs.

Let op bij het vergelijken: Haiku en Sonnet zijn gedraaid met `--effort medium`, Opus zonder die vlag, dus met de standaard effort. Op dat ene punt zijn de drie reeksen niet identiek, net als in de test van 21 oktober.
