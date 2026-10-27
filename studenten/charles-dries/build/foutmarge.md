# Foutmargetest

Datum: 21 oktober 2026
Model: **GPT-6 Luna** (`gpt-6-luna` via `codex exec`)

## Opzet

- **v1:** `fc7378b` — `# v1 — prompt`
- **v2:** `a7ef8e1` — `# v2 — meerdere labels per reactie`
- Testset: de 10 bestaande inputs in `build/test-set.md`.
- Per promptversie zijn er drie runs uitgevoerd. Elke combinatie van run en testinput draaide in een nieuwe, tijdelijke `codex exec`-sessie met alleen de prompt en die input. Er zijn geen toolaanroepen gedaan.
- De verwachte antwoorden zijn niet aan het model gegeven en zijn niet aangepast. De score vergelijkt uitsluitend de teruggegeven JSON-label(s) met het bestaande verwachte label/de bestaande verwachte labels.

## Scores

| Versie | Run 1 | Run 2 | Run 3 | Laagste score | Hoogste score |
|---|---:|---:|---:|---:|---:|
| v1 | 9/10 (90%) | 9/10 (90%) | 9/10 (90%) | 9/10 (90%) | 9/10 (90%) |
| v2 | 8/10 (80%) | 9/10 (90%) | 9/10 (90%) | 8/10 (80%) | 9/10 (90%) |

## Vergelijking met de verwachte antwoorden

Alle niet-vermelde antwoorden kwamen exact overeen met het verwachte label of de verwachte labels.

| Versie | Run | Test | Verwacht | Teruggegeven | Beoordeling |
|---|---:|---|---|---|---|
| v1 | 1 | T07 | `onzeker/anders` | `locatie/bereikbaarheid` | fout |
| v1 | 2 | T07 | `onzeker/anders` | `locatie/bereikbaarheid` | fout |
| v1 | 3 | T07 | `onzeker/anders` | `locatie/bereikbaarheid` | fout |
| v2 | 1 | T07 | `onzeker/anders` | `locatie/bereikbaarheid` | fout |
| v2 | 1 | T10 | `programma` | `onzeker/anders` | fout |
| v2 | 2 | T07 | `onzeker/anders` | `locatie/bereikbaarheid` | fout |
| v2 | 3 | T07 | `onzeker/anders` | `locatie/bereikbaarheid` | fout |

## Korte conclusie

Op deze testset is v1 consistenter: drie keer 9/10. v2 behaalt maximaal ook 9/10, maar heeft één extra fout in run 1. Beide versies classificeren T07 telkens anders dan het vooraf vastgelegde verwachte antwoord.

## Mijn oorspronkelijke claim

Mijn oorspronkelijke claim was dat **v2, die meerdere labels kan teruggeven, beter zou zijn dan v1**. Die claim is **ingetrokken**. Het bereik van v1 is 90%–90% en dat van v2 is 80%–90%; de bereiken overlappen op 90%. Ik kan dus niet bewijzen dat v2 beter is. Voor de volgende stappen gebruik ik v1: die was in drie runs stabieler en past ook beter bij mijn oorspronkelijke taak, die precies één label vraagt.
