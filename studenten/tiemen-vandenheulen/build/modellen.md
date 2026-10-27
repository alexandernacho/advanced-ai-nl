# Modeltest — review-sorteerder

## Mijn gok

Ik verwachtte dat het hoge redeneerniveau beter zou scoren.

## Resultaat

- **Datum:** 21 oktober 2026
- **Testset:** de 10 oorspronkelijke reviews uit `test-set.md`. De verwachte labels zijn niet gewijzigd en niet aan het model gegeven.
- **Prompt:** de huidige versie van `prompt.md`.
- **Opzet:** elke review draaide in een nieuwe, tijdelijke Codex-sessie zonder projectcontext. De score vergelijkt de volledige labelset per review met de verwachte labels.

| Setup | Model | Redeneerniveau | Score | Gemiddelde outputtokens per review |
|---|---|---:|---:|---:|
| A | GPT-6.1 Sol via `codex exec` | hoog | 7/10 | 107,5 |
| B | GPT-6.1 Sol via `codex exec` | gemiddeld | 9/10 | 76,1 |
| C | GPT-6.1 Sol via `codex exec` | laag | 9/10 | 76,3 |

De twee beste scores zijn gelijk: B en C halen 9 op 10. In beide gevallen is review 5 fout door het extra label `organisatie`; verwacht was alleen `locatie`.

Ik kies voorlopig voor setup C, omdat die even goed scoorde als B maar met gemiddeld 76,3 outputtokens het zuinigst is. Dit besluit is voorlopig: elke setup kreeg slechts één run.

## Week 5 — gok vóór de nieuwe modeltest

Voor T26, over de geblokkeerde nooduitgang en de medewerker, verwacht ik:

| Model | Verwachte labels | Waarom? |
|---|---|---|
| Haiku | `veiligheid, organisatie` | Het model kan zowel de geblokkeerde uitgang als het optreden van de medewerker labelen. |
| Sonnet | `veiligheid` | Het model kan vooral focussen op het hoofdprobleem: de geblokkeerde nooduitgang. |
| Opus | `veiligheid, organisatie` | Het model kan beide genoemde thema’s meenemen, omdat de prompt personeel onder organisatie rekent. |

Deze voorspelling is geschreven vóór de runs op set v2.
