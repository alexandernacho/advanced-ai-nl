# Week 5: Het kleinste model was het beste

## Mijn foutmarge
Ik draaide v1 en v2 elk 3 keer op dezelfde 10 bedrijven, met Claude Sonnet 5.5, elke run in een aparte sessie. Beide versies haalden 9/10 in elke run: bereik 9–9.

In week 3 schreef ik dat mijn nieuwe regel Bautier oploste. Die claim trek ik in. Bautier ging in alle 6 runs fout. De 2 juiste runs van week 3 waren toeval.

## Model en effort
Mijn gok vooraf: Opus scoort het best en is ook nodig, omdat er toch wel wat onderzoekswerk nodig is.

- Sonnet 5.5, medium: 9/10 (3 runs: 9–9), € 0,0067 per run
- Haiku 5.5: 10/10 (3 runs: 10–10), € 0,0006 per run
- Opus 5.5: 10/10 (1 run), € 0,0154 per run

Mijn gok was deels fout. Opus haalde 10/10, maar Haiku 5.5 ook, drie keer na elkaar. Het bereik van Haiku (10–10) overlapt niet met dat van Sonnet (9–9). Het hele verschil is wel één bedrijf: Bautier. Met n = 10 is dat weinig bewijs.

In productie kies ik Haiku 5.5: het heeft dezelfde resultaten maar is veel goedkoper.

## Mijn value chain, met de foutmarge erin
- **Met de hand:** 15 minuten per bedrijf. Eigen schatting.
- **Met de tool:** opzoeken 1 minuut, kopiëren, plakken en draaien 2 minuten, nakijken of het een e-mailadres is 10 seconden, fouten herstellen 0% × 15 minuten. Samen ± 3 minuten 10 seconden.
- **Winst:** ± 11 minuten 50 seconden per bedrijf.
- **Volume:** 100 bedrijven per maand, 1.200 per jaar. Een gok.
- **Uren:** ± 237 uur per jaar × € 45 voor de werkgever (aanname, les week 4) = ± € 10.650.
- **Kost van de tool:** ± € 0,72 per jaar met Haiku 5.5. Gemeten.
- **Netto:** ± € 10.650 per jaar.
- **Bereik:** Haiku haalde 10–10, dus ik mat geen bereik. Zit hij in het echt 1 op 10 fout, zoals Sonnet, dan kost herstellen 1 minuut 30 seconden per bedrijf en blijft er ± € 9.290 over.
- **Zwakste cijfer:** het volume. Het hangt af van de maand en het andere werk. Bij de helft blijft er ± € 5.325 over. Het volume beweegt het netto 4 keer meer dan de score.

## Mijn dashboard
https://claude.ai/artifact/TsQTiPeKBYAaPJ5YgujuqK

Kijk eerst naar de foutmarge: mijn claim van week 3 is ingetrokken.

## Mijn AI-ismen
1. Week 2: "Het AI-model moet ervoor zorgen dat ze in elke taal klanten kunnen vinden."
   Herschreven: Ik testte 1 Franstalige site (T04) en 2 Engelstalige sites (T07 en T09). Met Haiku 5.5 gaven alle 3 het juiste resultaat, met Sonnet ging T07 fout.
2. Week 3: "Daarvoor heb ik meer testgevallen nodig waar het verleidelijk is om iets te verzinnen."
   Herschreven: Maar 3 van de 10 bedrijven hebben geen e-mailadres, dus ik kon maar bij 3 bedrijven testen of het model een adres verzint.
3. Week 4: "Het opvallendste: met exact dezelfde v2-prompt gaf Bautier in week 3 twee keer `nee` en in week 4 twee keer `ja`."
   Herschreven: Met Sonnet was Bautier in 6 van de 6 runs fout, met Haiku 5.5 was het in 3 van de 3 runs juist.
4. Week 4: "Hoe je de tool draait, bepaalt de kost meer dan welk model je kiest."
   Herschreven: Eén run kost € 0,066 in Claude Code en € 0,005 via de API, dus Claude Code is 13 keer duurder.
5. Week 4: "Mijn zwakste cijfer bepaalt dus de hele waarde."
   Herschreven: Als het niet 100 maar 50 bedrijven zijn, daalt de nettowaarde van ongeveer € 10.650 naar ongeveer € 5.325.
