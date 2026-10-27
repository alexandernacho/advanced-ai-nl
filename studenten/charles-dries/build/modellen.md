# Modeltest

## Mijn gok

Ik gokte dat setup C het beste zou presteren.

## Meting — 21 oktober 2026

Elke setup kreeg elk van de tien bestaande inputs één keer, in een nieuwe tijdelijke `codex exec`-sessie, met de ongewijzigde laatste prompt. De verwachte antwoorden zijn niet aan de modellen gegeven en niet aangepast. Het gemiddelde hieronder is het gemiddelde aantal gemeten outputtokens per testinput.

Voor de kost reken ik met 480 geschatte inputtokens per reactie, de gemeten outputtokens, de cursustabel en $1 = €0,90. De foutmarge uit de prompttest loopt van 80% tot 90%: alle drie de scores van 90% vallen daarbinnen.

| Setup | Model | Reasoning effort | Score | Binnen foutmarge? | Gemiddelde outputtokens per run | Kost per run | Kost bij 500/jaar |
|---|---|---:|---:|---|---:|---:|---:|
| A | `gpt-6-luna` | high | 9/10 (90%) | ja | 58,9 | €0,000070 | €0,035 |
| B | `gpt-6-luna` | medium | 9/10 (90%) | ja | 28,4 | **€0,000056** | **€0,028** |
| C | `gpt-6.1-sol` | high | 9/10 (90%) | ja | 116,7 | €0,00191 | €0,96 |

## Resultaat

Mijn gok is niet bevestigd: C scoort niet beter dan A of B. Ik kies B voor verder gebruik, omdat de score gelijk is en B de minste outputtokens en de laagste kost heeft.
