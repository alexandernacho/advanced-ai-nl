# Modeltest — 22 oktober 2026

## Mijn gok vóór de meting

Ik verwacht dat een kleiner model goed genoeg scoort voor de leveringsassistent, omdat het vooral vaste bestelgegevens correct moet verwoorden en geen complexe redenering nodig heeft.

| Setup | Model | Effort | Score (n = 13, 1 run) | Binnen mijn foutmarge? | Output-tokens per run | Kost per run | Per jaar |
| --- | --- | --- | ---: | --- | ---: | ---: | ---: |
| A · standaard | `gpt-6-luna` | standaard | 12/13 | Ja: 12 ligt binnen 12–13 | 39,1 | €0,0000514 | €0,0185 |
| B · omlaag | `gpt-5.6-terra` | standaard | 12/13 | Ja: 12 ligt binnen 12–13 | 35,1 | €0,0010559 | €0,3801 |
| C · omhoog | `gpt-6.1-sol` | standaard | 12/13 | Ja: 12 ligt binnen 12–13 | 39,3 | €0,0010305 | €0,3710 |

## Werkwijze

Elke setup kreeg één nieuwe, aparte run op dezelfde 13 gevallen en dezelfde huidige prompt. De verwachte antwoorden gingen niet mee naar het model. Een score van 12/13 valt voor alle drie de setups binnen mijn foutmarge van 12–13/13.

De gemiddelde output-tokens komen uit de 13 gemeten modelruns. Voor de kost gebruikte ik de 376 inputtokens uit `kosten.md`, de gemeten gemiddelde output, 30 klantvragen per maand (= 360 per jaar) en $1 = €0,90.

- Luna: $0,10 input en $0,50 output per miljoen tokens.
- Terra: $2 input en $12 output per miljoen tokens. [Officiële OpenAI-documentatie](https://developers.openai.com/api/docs/models/gpt-5.6-terra)
- Sol: $2 input en $10 output per miljoen tokens.

## Conclusie

Mijn gok dat een minder zwaar model goed genoeg zou zijn, klopt op score: alle drie de modellen zijn binnen de foutmarge niet van elkaar te onderscheiden. Ik kies toch `gpt-6-luna` voor de echte toepassing, omdat het even goed scoort en veruit de laagste gemeten kost heeft. Terra is een kleiner model dan Luna, maar door zijn prijs per token in deze vergelijking niet goedkoper.
