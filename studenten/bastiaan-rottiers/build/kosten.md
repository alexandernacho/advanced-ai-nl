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

## Gecorrigeerd in week 5: echte tokenverdeling

Datum: 27 oktober 2026. **gecorrigeerd in week 5**: de oude raming hierboven blijft staan. Er is geen Haiku-model gebruikt; de Haiku-correctie is niet van toepassing. De prijzen voor Sol en Luna komen overeen met de geraadpleegde prijstabel. De correctie betreft de meetmethode: de CLI geeft nu input-, cache- en outputtokens afzonderlijk weer, in plaats van de aangenomen 98/2-verdeling.

Dit is een nieuwe meting op **T06–T10 (n = 5, één antwoord per input per setup)**, geen hertelling van de historische T01-run. De gemiddelde input omvat ook de standaard Codex-omgeving. Het zuivere taakdeel is niet afzonderlijk geteld. De bedragen hieronder zijn API-equivalenten tegen standaardtarief, geen rekening voor het Codex-abonnement.

| Setup | Gemiddelde inputtokens | Daarvan cache gelezen | Gemiddelde outputtokens | Kost per taak zonder cache (EUR) | Per maand, 8 taken | Per jaar, 96 taken |
|---|---:|---:|---:|---:|---:|---:|
| Sol medium | 16.111,4 | 7.936 | 347,2 | €0,03212532 | €0,25700256 | €3,08403072 |
| Luna low | 15.038,2 | 6.937,6 | 323,4 | €0,001498968 | €0,011991744 | €0,143900928 |
| Astra medium | 15.666,2 | 6.144 | 316,6 | €0,1552428 | €1,2419424 | €14,9033088 |

Gebruik voor een voorzichtige begroting de kolom zonder cache: gemiddeld ongeveer **€0,032 per taak, €0,26 per maand en €3,08 per jaar voor Sol medium** op deze vijf voorbeelden. De prijs hangt sterk af van de documentlengte; dit gemiddelde voorspelt niet de prijs van elk toekomstig financieel document.

### Caching

Cachelezen is in deze runs werkelijk geregistreerd. Met de waargenomen cacheverdeling komt de gemiddelde API-equivalente kost per taak uit op **€0,01855476 voor Sol**, **€0,0009370224 voor Luna** en **€0,1054764 voor Astra**. Cachebeschikbaarheid bij volgende taken is niet gegarandeerd. Er zijn geen cache-schrijfinputtokens geregistreerd.

`zonder cache = (inputtokens × inputprijs + outputtokens × outputprijs) / 1.000.000 × 0,90`

`met waargenomen cache = ((inputtokens − cachetokens) × inputprijs + cachetokens × cacheleesprijs + outputtokens × outputprijs) / 1.000.000 × 0,90`

Reasoning wordt door de provider als output gefactureerd. Voor de berekening wordt het veld `output_tokens` uit de CLI-usage gebruikt; het afzonderlijke veld `reasoning_output_tokens` wordt niet nogmaals opgeteld. Ruwe gebruiksgegevens blijven lokaal; de openbare samenvatting staat in `modelmetingen-week-05.csv` en `modelkosten-week-05.json`.

### Bronnen en vergelijkbaarheid

Bron: [OpenAI API-prijzen](https://developers.openai.com/api/docs/pricing), geraadpleegd op 27 oktober 2026. Standaardprijs per miljoen tokens: Sol $2 in, $10 uit, $0,10 cache lezen; Luna $0,10 in, $0,50 uit, $0,01 cache lezen; Astra $10 in, $50 uit, $1 cache lezen. Voor de omrekening blijft de bestaande aanname $1 = €0,90 gelden.

De tabel in `modellen.md` volgt de lesformule met dezelfde 25.284 aangenomen inputtokens uit week 4 voor alle setups. Deze kostentabel gebruikt de werkelijk gemeten gemiddelde input per setup. Daarom verschillen de bedragen; beide rekenbasissen staan expliciet vermeld en mogen niet door elkaar worden gebruikt in de waardeketen.
