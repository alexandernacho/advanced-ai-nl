# Kostenmeting

Datum meting: 20 oktober 2026

| Model | Context | Totaal tokens | Mijn deel | Kost per run | Per maand: 12 runs | 10x: 120 runs | 1.000x: 12.000 runs |
|---|---:|---:|---:|---:|---:|---:|---:|
| GPT-5.6-Terra | 0 | 18.800 | 18.800 | €0,034* | €0,41 | €4,06 | €406,08 |

## Opmerking

Ik heb een nieuwe, lege Codex-sessie gebruikt. Daarna plakte ik mijn prompt en testinput T01 rechtstreeks in één bericht. De run gebruikte 18.800 tokens.

* GPT-5.6-Terra staat niet in de prijstabel van de les. Daarom is dit een vergelijking met GPT-6.1 Sol: 18.800 / 1.000.000 × $2 × 0,90 = €0,034 per run. Dit is een aanname en houdt alleen rekening met de inputprijs; outputtokens zouden de echte kost verhogen.

## Gecorrigeerd in week 5, 28 oktober 2026

De oude regel hierboven blijft staan. De nieuwe Codex-run gebruikte exact het model `gpt-5.6-terra`, effort medium. De prijs is $2 per miljoen gewone invoertokens, $0,20 per miljoen cache-gelezen tokens en $12 per miljoen uitvoertokens. Bron: [OpenAI](https://developers.openai.com/api/docs/models/gpt-5.6-terra).

| Model | Invoer | Cache gelezen | Uitvoer | Kost per run | Per maand: 12 runs | 10x: 120 runs | 1.000x: 12.000 runs |
|---|---:|---:|---:|---:|---:|---:|---:|
| GPT-5.6 Terra, medium | 36.869 | 28.544 | 448 | €0,025 | €0,30 | €3,00 | €299,54 |

Berekening: (8.325 niet-gecachete invoertokens × $2 + 28.544 cache-gelezen tokens × $0,20 + 448 uitvoertokens × $12) / 1.000.000 = $0,0277. Met dezelfde aanname als de oude regel, $1 = €0,90, is dat €0,025 per run.
