# Kosten

Laatst berekend: 27 oktober 2026. **Gecorrigeerd in week 5:** de eerdere €0,55 per reactie was een verdeling van mijn Plus-abonnement en geen API-prijs. Voor de value chain reken ik daarom met de API-prijs van het gekozen model.

## Gekozen setup

Ik kies **GPT-6 Luna met medium reasoning effort** (setup B). Die haalde 9/10, hetzelfde als de twee andere setups, en gebruikte met 28,4 outputtokens per reactie het minst.

## Berekening per reactie

De prompt plus een gemiddelde testreactie is geschat op **480 inputtokens**. Het aantal outputtokens komt uit de modeltest. Prijzen uit de cursustabel: GPT-6 Luna kost $0,10 per miljoen inputtokens en $0,50 per miljoen outputtokens. Ik reken met de cursusaanname **$1 = €0,90**.

| Onderdeel | Berekening | Kost |
|---|---:|---:|
| Input | 480 × $0,10 / 1.000.000 | $0,000048 |
| Output | 28,4 × $0,50 / 1.000.000 | $0,0000142 |
| Samen, in euro | ($0,0000622) × 0,90 | **€0,000056** |

Bij 500 reacties per jaar is dat **€0,028**, afgerond **€0,03 per jaar**. De kost per reactie is dus afgerond minder dan één eurocent.

## Vergelijking met de andere gemeten setups

| Setup | Kost per run | Kost bij 500 reacties/jaar |
|---|---:|---:|
| A — GPT-6 Luna, high | €0,000070 | €0,035 |
| B — GPT-6 Luna, medium | **€0,000056** | **€0,028** |
| C — GPT-6.1 Sol, high | €0,00191 | €0,96 |

De inputtokens zijn een schatting; de outputtokens zijn gemeten. Zelfs bij de duurdere setup C blijft de kost bij dit volume onder €1 per jaar.
