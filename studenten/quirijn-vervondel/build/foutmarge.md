# Foutmarge, 27 oktober 2026

Model: Claude Haiku 5.5 (`claude-haiku-5-5`), via `claude -p --tools ""`. n = 10 inputs (T01 tot T10), 3 runs per versie. Zelfde inputs voor beide. Elke run in een nieuwe sessie, alleen de prompt en de input.

Versies:
- **v1** = de laatste versie, `prompt.md`.
- **v2** = de versie ervoor: v1 plus twee regels (kabelgoot per route apart naar boven afronden, en een condenspompje betekent condensafvoer type druk-PVC). v2 is niet bewaard in git, ik heb hem gereconstrueerd uit `log.md`.

## Tabel 1: per input

Score = aantal inputs (van 10) die helemaal juist zijn.

| Versie | Run 1 | Run 2 | Run 3 | Foutmarge (min–max) |
|---|---:|---:|---:|---:|
| v1 (laatste, `prompt.md`) | 0/10 | 2/10 | 1/10 | 0 tot 2 |
| v2 (versie ervoor) | 1/10 | 0/10 | 0/10 | 0 tot 1 |

## Tabel 2: per onderdeel

Score = aantal onderdelen (rijen uit de verwachte stuklijst) die juist zijn. T01 tot T10 zijn samen 96 onderdelen. T06 tot T10 zijn samen 34 onderdelen, het deel waar je claim over ging.

| Versie | Run 1 | Run 2 | Run 3 | Foutmarge (min–max) |
|---|---:|---:|---:|---:|
| v1 (laatste), T01 tot T10 (van 96) | 77 | 80 | 79 | 77 tot 80 |
| v2 (versie ervoor), T01 tot T10 (van 96) | 77 | 76 | 74 | 74 tot 77 |
| v1 (laatste), T06 tot T10 (van 34) | 24 | 24 | 26 | 24 tot 26 |
| v2 (versie ervoor), T06 tot T10 (van 34) | 24 | 25 | 22 | 22 tot 25 |

Per input, aantal onderdelen juist (van het totaal per input):

| Input | Onderdelen | v1 Run 1 | v1 Run 2 | v1 Run 3 | v2 Run 1 | v2 Run 2 | v2 Run 3 |
|---|---:|---:|---:|---:|---:|---:|---:|
| T01 | 11 | 10 | 11 | 10 | 9 | 9 | 10 |
| T02 | 12 | 11 | 11 | 11 | 11 | 10 | 10 |
| T03 | 12 | 9 | 10 | 8 | 9 | 8 | 9 |
| T04 | 17 | 14 | 14 | 14 | 14 | 15 | 14 |
| T05 | 10 | 9 | 10 | 10 | 10 | 9 | 9 |
| T06 | 8 | 6 | 6 | 6 | 6 | 7 | 6 |
| T07 | 5 | 2 | 2 | 4 | 4 | 4 | 2 |
| T08 | 11 | 9 | 9 | 9 | 7 | 7 | 7 |
| T09 | 4 | 2 | 2 | 2 | 2 | 2 | 2 |
| T10 | 6 | 5 | 5 | 5 | 5 | 5 | 5 |

## Claim en beslissing

Mijn claim: "Mijn foute v2 scoorde slechter (19 op 30)."

Bevestigd of ingetrokken, op de score per onderdeel: **ingetrokken**.

- Op de inputs van de claim (T06 tot T10) overlappen de bereiken: v1 24 tot 26, v2 22 tot 25. De laagste v1-score (24) ligt niet boven de hoogste v2-score (25).
- Op alle tien inputs raken de bereiken elkaar op 77: v1 77 tot 80, v2 74 tot 77.
- Het grootste verschil zit in T08 (v2 scoort gemiddeld 2 onderdelen lager). Dat is de input waar de twee v2-regels op ingrijpen, en die regels waren fout: kabelgoot 4 stuks in plaats van 3, en druk-PVC in plaats van condensbuis. Dat verschil is dus een echt effect van de regels. Op de andere inputs gaat het beide kanten op: T04, T06 en T07 scoort v2 hoger, T01 en T02 lager. Daar is het ruis.
- Ik kan dus niet aantonen dat v2 als geheel slechter was: de bereiken overlappen. Wel weet ik nu waarom v2 op T08 slechter scoort.

## Hoe ik beoordeelde

- Een onderdeel is juist als de rij bestaat en de waarde klopt, of als de rij "onbekend, na te vragen" zegt waar de verwachting onbekend is. Een ontbrekende rij telt als fout, ook als het verwachte antwoord "onbekend" is.
- Een input is juist als alle onderdelen juist zijn én er niets verzonnen is. Een verzonnen rij, zoals het verloopstuk bij T04, maakt de input fout, maar telt niet mee in het onderdelen-totaal.
- Het verwachte antwoord is niet aangepast na het zien van de uitvoer.
- De beoordeling is door de agent gedaan, niet door een klasgenoot.
- Mijn telling van onderdelen (34 voor T06 tot T10) wijkt af van de telling in week 3 (30). Daardoor zijn de cijfers niet één op één vergelijkbaar met "19 op 30".
