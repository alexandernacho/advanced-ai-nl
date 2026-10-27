# Modellen en effort, 27 oktober 2026

## Mijn gok (geschreven vóór de runs)

Welke setup scoort het best: Opus

Welke setup is goed genoeg voor mijn echte plek: Sonnet

Waarom: Opus is de grootste en de slimste, maar ik denk dat Sonnet ookwel meer dan genoeg zal zijn.

## De drie setups

| Setup | Model | Effort |
|---|---|---|
| A, standaard | Sonnet 5.5 | medium |
| B, omlaag | Haiku 5.5 | medium |
| C, omhoog | Opus 5.5 | medium |

Inputs: T01 tot T14 uit `test-set.md`. Prompt: v2 (`prompt.md`). Elke setup 1 run.

## Resultaten

Inputs T01 tot T14, prompt v2, 1 run per setup. Scores vergeleken met het verwachte antwoord in `test-set.md`.

| Setup | Model | Score interessant | Score soort werk | Kost per run (schatting) | Kost per jaar, laag (5.952) | Kost per jaar, hoog (19.344) |
|---|---|---:|---:|---:|---:|---:|
| A, standaard | Sonnet 5.5 | 14/14 | 14/14 | €0,0056 | €34 | €109 |
| B, omlaag | Haiku 5.5 | 10/14 | 12/14 | €0,0003 | €2 | €5 |
| C, omhoog | Opus 5.5 | 14/14 | 13/14 | €0,0113 | €67 | €219 |

**Let op de kost.** De output-tokens per setup zijn niet gemeten. De kost is berekend met de tokens van de Haiku 4.5-meting in week 4 (560 in, 514 uit), en de prijzen per model uit de tabel. Dat is een schatting, geen meting.

**Let op de scores.** Elke setup is één run. Een verschil van één input kan door de schommeling van de tool komen: in je foutmarge zag je dat al bij v2 (11 tot 13). Haiku 5.5 valt buiten dat bereik. Sonnet en Opus scoren hetzelfde.
