# Week 5: Mijn cijfers met de marge erbij

## Mijn foutmarge
Ik draaide mijn laatste prompt (v1) en de versie ervoor (v2) elk drie keer, op tien inputs, met Haiku 5.5. Mijn score per input is streng: één ontbrekende rij telt als fout. Daarom tel ik ook per onderdeel. v2 heb ik gereconstrueerd uit mijn log, want de tekst was niet bewaard.

Per input haalde v1 0 tot 2 van de 10. Per onderdeel haalde v1 77 tot 80 van de 96, en v2 74 tot 77.

Mijn claim uit week 3 was: "Mijn foute v2 scoorde slechter (19 op 30)." Die claim is ingetrokken. Op T06 tot T10 overlappen de bereiken (v1 24 tot 26, v2 22 tot 25). Op T08 zat het grootste verschil, maar één input bewijst niets.

## Model en effort
Elke setup draaide ik één keer, met effort medium. Opus haalde 87 van de 96 onderdelen, Sonnet 79 en Haiku 76. Mijn gok klopte deels: Opus scoorde het best, maar of Sonnet goed genoeg is, weet ik niet. Dat is één run per setup, dus het is een meting en geen zekerheid.

Een run met Opus kost € 0,026. Bij 120 runs per jaar is dat € 3,18, tegen € 1,43 voor Sonnet. Ik kies Opus 5.5, met effort medium, omdat het als enige boven mijn foutmarge scoort. Het kost maar € 1,75 per jaar meer dan Sonnet.

## Mijn value chain met de foutmarge erin
Met de hand kost één plaatsbezoek 2 uur. Dat is een schatting. Met de tool kost het 16 seconden draaien, 5 minuten nakijken en 22 minuten herstellen, want 18 procent is fout. Samen is dat 27 minuten, dus 93 minuten winst per plaatsbezoek.

Bij 120 plaatsbezoeken per jaar is dat 186 uur. Tegen € 30 per uur (€ 20 bruto maal 1,5, een aanname) is dat € 5.572. Min € 3,18 voor de tool is het netto € 5.568 per jaar. In week 4 nam ik nog € 40 zonder uitleg.

Bereik: met 77 van 96 is het € 5.456, met 80 van 96 is het € 5.681.

Mijn zwakste cijfer is de handtijd. Is die 1 uur, dan is het netto € 2.625. De foutmarge verschuift het netto € 225, een halve handtijd € 2.944.

## Mijn dashboard
Mijn dashboard staat in `build/dashboard.html`. De publieke link: https://claude.ai/artifact/KvYNaQpE1VLvEpdAmQJSgA

Kijk eerst naar het netto per jaar en het bereik, dan naar de handtijd.

## Mijn AI-ismen
Twee zinnen zijn echte AI-ismen, vier zijn twijfelgevallen.

- Week 4: "Wat een fout kost is het andere deel van het verhaal." Herschreven: Een vergeten onderdeel kost een extra rit van een half uur, ongeveer € 20.
- Week 3: "Een testset beschermt je alleen als je juiste antwoorden kloppen." Herschreven: Mijn verwachte antwoord op T08 volgde de foute regels, en daardoor leek v2 eerst beter.
- Week 4: "Zelfs met de besparing is de tool de moeite waard, maar alleen als hij vollediger wordt." Herschreven: De tool bespaart € 9.200 per jaar op mijn schatting, als hij de units, steunblokken en beugels meeneemt.
- Week 3: "Dit is geen bewijs: maar 5 nieuwe inputs, 1 run per versie, en de wijziging raakte maar 1 input." Herschreven: Vijf inputs en één run per versie zijn te weinig.
- Week 3: "Mijn grootste les: een AI stelde twee regels voor die logisch klonken maar fout waren." Herschreven: Een AI stelde twee foute regels voor, en mijn score zakte van 20 naar 19 op 30.
- Week 4: "Cache lezen is goedkoop, maar het gebeurt bij elke vraag, en daardoor kost de context ($0,0070) toch meer dan mijn deel ($0,0019)." Herschreven: De context kost $0,0070 per run, mijn deel $0,0019, omdat de cache bij elke vraag opnieuw gelezen wordt.