# Foutmarge — 21 oktober 2026

Model: `gpt-5.6-luna` (Codex). Zelfde tien cases T01–T10, n = 10, drie runs
per versie. De runs gebruikten dezelfde gestandaardiseerde evaluatieprompt en
de verwachte labels uit `build/test-set.md`.

| Versie | Run 1 | Run 2 | Run 3 | Foutmarge (min–max) |
| --- | ---: | ---: | ---: | ---: |
| v2 | 8/10 | 9/10 | 7/10 | 7–9 |
| v3 | 9/10 | 8/10 | 7/10 | 7–9 |

Mijn week-3/4-claim was: “de gerichte v3-regel verbetert T01 en v3 haalt
10/10 op deze testset.”

**Conclusie: ingetrokken.** De bereiken overlappen volledig. De beschikbare
runs tonen geen bewezen verbetering van v3 tegenover v2. De wijziging helpt
T01 wel, maar andere cases schommelen tussen runs. De score is daarom een
bereik, geen vast cijfer.

## Per-run controle

De verwachte labels zijn niet aangepast. De belangrijkste variatie zat in T04,
T07 en T08: dezelfde korte beschrijving werd niet in elke run hetzelfde
gelabeld. Dat bevestigt dat een mens de classificatie moet nakijken.
