# Foutmarge, 27 oktober 2026

Model: claude-haiku-4-5 (Haiku 4.5). n = 14 inputs (T01–T14), 3 runs per versie. Zelfde inputs voor beide versies. Ruwe antwoorden: `runs-foutmarge.txt`.

Score = aantal juiste antwoorden op 14. Juist = gelijk aan het verwachte antwoord in `test-set.md`.

## Score per run

| Versie | Veld | Run 1 | Run 2 | Run 3 | Foutmarge (min–max) |
|---|---|---:|---:|---:|---:|
| v1 | interessant | 13/14 | 13/14 | 14/14 | 13–14 |
| v1 | soort werk | 12/14 | 13/14 | 13/14 | 12–13 |
| v2 | interessant | 11/14 | 13/14 | 12/14 | 11–13 |
| v2 | soort werk | 12/14 | 13/14 | 12/14 | 12–13 |

## Stabiliteit: inputs met hetzelfde antwoord in alle 3 runs (interessant)

- v1: 12 van 14 stabiel. Wisselend: T12, T14.
- v2: 11 van 14 stabiel. Wisselend: T12, T13, T14.

## Mijn claim

Claim: v1 scoort hoger op "interessant" dan v2.

Bevestigd of ingetrokken: ingetrokken, want de slechtste run van v1 (13) is niet hoger dan de beste run van v2 (13).

Hoe je beslist: bevestigd als de laagste score van v1 hoger ligt dan de hoogste van v2. Ingetrokken als de bereiken overlappen.
