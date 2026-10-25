# Kostenmeting — gecorrigeerd in week 5

## Meting uit week 4

De vorige notitie gebruikte `gpt-5.6-luna` en rekende met de tijdelijke
cursusaanname voor GPT-6 Luna. De run rapporteerde 14.784 inputtokens,
waarvan 6.656 cached, en 10 outputtokens.

| Modelnotitie | Jouw deel | Kost per run | 100 runs/maand | 1.200 runs/jaar |
| --- | ---: | ---: | ---: | ---: |
| Oude berekening: Codex / GPT-5.6 Luna | 14.784 input + 10 output | €0,00080 | €0,08 | €0,96 |
| Oude vergelijking: GPT-6.1 Sol | 14.784 input + 10 output | €0,01532 | €1,53 | €18,38 |

## Correctie

De cursusweek-5-prijstabel noemt `GPT-6 Luna` met $0,10 per miljoen gewone
inputtokens, $0,01 per miljoen cached inputtokens en $0,50 per miljoen
outputtokens. Met $1 = €0,90 blijft de transparante schatting voor dezelfde
tokenmeting ongeveer **€0,00080 per run**: 8.128 gewone inputtokens kosten
ongeveer €0,00073, 6.656 cached inputtokens ongeveer €0,00006 en 10 output-
tokens ongeveer €0,000005.

De naam die de CLI rapporteerde was `gpt-5.6-luna`, niet letterlijk de naam
`GPT-6 Luna` uit de cursus. Daarom is dit een cursusprijs-aanname en geen
factuurbedrag van mijn account. De oude berekening blijft hierboven staan;
deze correctie vervangt ze niet stilletjes.

## Schaal

Bij 100 berichten per maand kost dit ongeveer €0,08 per maand. Bij tien keer
dat volume is dat €0,80 per maand; bij duizend keer dat volume €79,59 per
maand. Bij mijn scenario van 100 berichten per maand is de jaarlijkse
toolkost ongeveer €0,96.
