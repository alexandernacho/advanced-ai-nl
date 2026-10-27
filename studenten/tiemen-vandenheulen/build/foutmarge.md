# Foutmargetest — review-sorteerder

- **Datum:** 21 oktober 2026
- **Model:** GPT-6.1 Sol (via `codex exec`)
- **Testset:** de 10 oorspronkelijke inputs uit `test-set.md`; de verwachte labels zijn niet aangepast of aan het model gegeven.
- **Opzet:** per promptversie drie runs. Elke combinatie van prompt en review draaide in een nieuwe, tijdelijke Codex-sessie zonder projectcontext of hulpmiddelen.

## Scores

| Versie | Run 1 | Run 2 | Run 3 | Laagste score | Hoogste score |
|---|---:|---:|---:|---:|---:|
| Huidige — `prompt.md` | 8/10 | 8/10 | 8/10 | 8/10 | 8/10 |
| Vorige — `prompt.md v2.txt` | 8/10 | 8/10 | 8/10 | 8/10 | 8/10 |

## Vergelijking met de verwachte labels

De uitkomst was in alle zes runs identiek. Acht reviews waren juist. Bij deze twee reviews gaf het model een extra label:

| Test | Verwacht | Gekregen | Beoordeling |
|---:|---|---|---|
| 2 | `organisatie, wachttijden` | `organisatie, sfeer, wachttijden` | fout: extra `sfeer` |
| 5 | `locatie` | `locatie, organisatie` | fout: extra `organisatie` |

De foutmarge is dus stabiel: **2 fouten op 10 reviews per run (20%)**. In deze meting is er geen verschil tussen de twee bewaarde promptversies.
