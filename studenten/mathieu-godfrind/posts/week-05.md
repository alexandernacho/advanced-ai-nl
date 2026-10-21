# Week 5: Mijn grootste twijfel zit bij mezelf, niet bij de AI

## Mijn foutmarge
Ik heb v2 en v3 elk 3 keer gedraaid op dezelfde 13 inputs, allebei met Haiku 5.5. v2 haalde 12 of 13 op 13, v3 haalde elke keer 12 op 13. v3 is dus heel stabiel, maar niet beter dan v2. De fout bij v3 is altijd T05, de pagina met alleen vage zoekwoorden. Daar moet de tool ONZEKER zeggen, maar hij zegt elke keer NO-GO.

In week 3 zei ik dat mijn nieuwe regel het woord licht uit de uitleg haalde. Dat klopt, maar het verschil is klein: bij v2 stond licht 2 keer in de uitleg zonder dat er een gewicht op de pagina stond, bij v3 0 keer, op 39 antwoorden elk.

## Model en effort
Ik gokte dat Opus het best zou zijn en dat Haiku goed genoeg was. Uiteindelijk haalden Haiku en Opus allebei 12 op 13, en Sonnet maar 10 op 13. Ik heb elk model wel maar 1 keer gedraaid, dus dat is nog geen hard bewijs. Sonnet valt wel buiten mijn foutmarge. De kost per setup heb ik niet gemeten.

Voor mijn Vinted verkoop kies ik Haiku. Het scoort even goed als Opus en het is het goedkoopste model.
## Mijn value chain, met de foutmarge erin
Met 19,50 euro per uur (13 euro bruto keer 1,5), levert mijn tool tussen 767 en 883 euro per jaar op.
Mijn zwakste cijfer is de 4 minuten 50 die ik met de hand nodig heb per pagina. Dat heb ik geschat, niet gemeten. Als het maar de helft is, blijft er nog maar 71 euro per jaar over. Dat verschil is veel groter dan het verschil door de foutmarge. Mijn grootste onzekerheid zit dus niet bij de AI, maar bij mijn eigen schatting. Daarom ga ik de komende weken met een timer bijhouden hoe lang ik echt bezig ben.

## Mijn dashboard
Mijn dashboard: https://raw.githack.com/mathieugodfrind/advanced-ai-nl/week-05/studenten/mathieu-godfrind/build/dashboard.html

Kijk eerst naar het stuk over de value chain en mijn zwakste cijfer.
Claude hielp me deze week om de stappen te snappen en de berekeningen na te kijken, de keuzes maakte ik zelf.

## Mijn AI-ismen

**Week 1:** "Wat ik merk: AI is sterk om snel een eerste versie te maken, maar ik moet het resultaat altijd nog zelf nalezen."

Nu: Claude vertaalde mijn CV naar het Frans, veel sneller dan zelf, maar ik moest nog zelf dingen verbeteren.

**Week 2:** "Zo zag ik dat mijn testset ook mijn eigen regels test, niet alleen de AI."

Nu: Bij T02 zag mijn regel A de merknaam AirPods Pro al als risico, terwijl een hoesje "voor AirPods Pro" GO moest zijn, dus ik paste mijn regel aan.

**Week 4:** "Er waren ook 2 dingen die me verrasten."

Nu: /context startte mijn context-skill in plaats van de tokenteller, en /model haiku gaf mij Haiku 5.5 en niet 4.5 zoals in de les.

**Week 4:** "Wat het kost is eigenlijk bijna niets."

Nu: 1 run kost met Haiku 5.5 ongeveer 0,0012 dollar, dus voor 960 pagina's per jaar betaal ik ongeveer 1 euro.

**Week 4:** "Let op: deze runs liepen via claude -p en niet via claude.ai zoals vorige weken, dus de cijfers zijn niet helemaal te vergelijken."

Nu: In week 2 en 3 draaide ik mijn tool op claude.ai, in week 4 via claude -p met Haiku 5.5, dus de cijfers zijn niet op dezelfde manier gemeten.
