# Foutmarge, 21 oktober 2026

Model: claude-haiku-5-5, via `claude -p --tools ""`. Elke run een nieuwe sessie, zonder CLAUDE.md. n = 13 inputs (T01–T13), 3 runs per versie. Zelfde inputs voor beide.

- **v2:** de prompt uit git-commit `a56d7b8` (week 3, vóór de "licht"-regel).
- **v3:** de huidige `build/prompt.md`.

Beoordeling: het label (GO / NO-GO / ONZEKER) en de risico's, tegen de verwachte antwoorden in `build/test-set.md`. De verwachte antwoorden zijn niet aangepast.

| Versie | Run 1 | Run 2 | Run 3 | Foutmarge (min–max) |
|---|---:|---:|---:|---:|
| v2 | 13/13 | 12/13 | 12/13 | 12–13 (92–100%) |
| v3 | 12/13 | 12/13 | 12/13 | 12–12 (92%) |

## Per input (label, 6 runs per input)

| ID | Juist antwoord | v2 (r1 / r2 / r3) | v3 (r1 / r2 / r3) |
|---|---|---|---|
| T01 | GO | GO / GO / GO | GO / GO / GO |
| T02 | GO | GO / GO / GO | GO / GO / GO |
| T03 | GO | GO / GO / GO | GO / GO / GO |
| T04 | NO-GO (C) | NO-GO / NO-GO / NO-GO | NO-GO / NO-GO / NO-GO |
| T05 | ONZEKER | ONZEKER / **NO-GO** / **NO-GO** | **NO-GO** / **NO-GO** / **NO-GO** |
| T06 | GO | GO / GO / GO | GO / GO / GO |
| T07 | NO-GO (D) | NO-GO / NO-GO / NO-GO | NO-GO / NO-GO / NO-GO |
| T08 | NO-GO (A, B) | NO-GO / NO-GO / NO-GO | NO-GO / NO-GO / NO-GO |
| T09 | NO-GO (B) | NO-GO / NO-GO / NO-GO | NO-GO / NO-GO / NO-GO |
| T10 | GO | GO / GO / GO | GO / GO / GO |
| T11 | NO-GO (A) | NO-GO / NO-GO / NO-GO | NO-GO / NO-GO / NO-GO |
| T12 | NO-GO (B) | NO-GO / NO-GO / NO-GO | NO-GO / NO-GO / NO-GO |
| T13 | NO-GO (B) | NO-GO / NO-GO / NO-GO | NO-GO / NO-GO / NO-GO |

**Fouten:**
- v2 run 2 en run 3: T05, NO-GO (B) terwijl ONZEKER juist is. 2 × F1.
- v3 run 1, 2 en 3: T05, NO-GO (B). 3 × F1.
- Geen F2 (citaat niet op de pagina) en geen F3 (gemist risico) in alle 78 runs.

**Opvallend, geen fout:** bij T12 gaf v2 run 1 en run 3, en v3 run 1, een extra risico A ("Niuniu Energy Drink"). Het citaat staat op de pagina.

## Mijn claim

Mijn claim uit week 3: [vul hier de precieze tekst in uit `posts/week-03.md`]

**Bevestigd of ingetrokken:** deze meting bevestigt de claim niet. De bereiken overlappen (v2: 12–13, v3: 12). Het verschil valt binnen de foutmarge.

Let op: deze meting scoort label en risico's. De "licht"-regel gaat over de uitleg, en die scoort deze test niet. Over die regel zegt deze meting dus niets.

Opmerking: T05 is bij beide versies het zwakke punt. v2 was er 2 van de 3 keer fout, v3 3 van de 3 keer. Dat is het verschil tussen de twee versies op deze inputs.
