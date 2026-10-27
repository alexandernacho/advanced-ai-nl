# Kostenmeting — Canvas-assistent WATTZAK

Datum van meting: 20 oktober 2026

## Eén run

Meet in een nieuwe Codex-sessie met `prompt.md` en testinput T01. Noteer `/status` vóór en na de run. Het verschil is het aantal tokens voor deze run.

| Model | Tokens vóór | Tokens na | Jouw deel | Kost per run (USD) | Kost per run (EUR) |
| --- | ---: | ---: | ---: | ---: | ---: |
| GPT-6.1 Sol | nieuwe sessie | 25.800 | ± 25.800 | ± $0,056 | ± €0,050 |

Prijsaanname: GPT-6.1 Sol kost $2 per miljoen inputtokens en $10 per miljoen outputtokens. Voor de euroberekening gebruiken we $1 = €0,90, zoals in het lesmateriaal.

Berekening van de werkraming: `/status` toont geen opsplitsing tussen input en output. Daarom nemen we voor deze korte voorbereidingskaart voorlopig 98% input (25.284 tokens) en 2% output (516 tokens):

`(25.284 / 1.000.000 × $2) + (516 / 1.000.000 × $10) = ± $0,056 = ± €0,050`.

Het absolute bereik als alle 25.800 tokens input of output zouden zijn, loopt van €0,046 tot €0,232. De 98/2-verdeling is dus een expliciete aanname die we in de post vermelden.

## Op schaal

Echte volume: **8 runs per maand**.

Bron voor dit volume: inschatting van Bastiaan voor WATTZAK: minstens 6 belangrijke Canvas-documenten en 1 à 2 opdrachten per maand. Voorzichtig afgerond naar 8 afzonderlijke runs. Als één run meerdere documenten tegelijk verwerkt, valt de werkelijke kost lager uit.

| Scenario | Berekening | Kost per maand (EUR) |
| --- | --- | ---: |
| Eigen volume | €0,050 × 8 | **≈ €0,40** |
| 10× volume | €0,050 × 80 | **≈ €4,00** |
| 1.000× volume | €0,050 × 8.000 | **≈ €400,00** |

## Vergelijking met een ander model

| Model | Prijsinput / miljoen | Prijsoutput / miljoen | Kost per run | Kost bij eigen volume |
| --- | ---: | ---: | ---: | ---: |
| GPT-6 Luna | $0,10 | $0,50 | ≈ €0,0025 | ≈ €0,02 per maand |
| GPT-6.1 Sol | $2 | $10 | ≈ €0,050 | ≈ €0,40 per maand |

## Wat betekent dit?

Bij het eigen volume is de API-kost vrijwel verwaarloosbaar: ongeveer 40 cent per maand met Sol. Zelfs bij duizend keer het volume wordt de kost merkbaar (ongeveer €400 per maand). Luna is in deze prijstabel twintig keer goedkoper, maar moet nog met dezelfde testset worden vergeleken op kwaliteit.
