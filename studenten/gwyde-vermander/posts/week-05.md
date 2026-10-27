# Week 5: Twintig inputs, geen verschil

## Mijn foutmarge
Ik draaide mijn laatste versie (v3) en de versie ervoor (v2) elk drie keer op dezelfde twintig inputs, met Opus 5.5. v2 haalde 13 tot 14 op 20, v3 ook 13 tot 14 op 20 (n = 20, 3 runs). Mijn claim uit week 3, "v3 werkt beter dan v2", trek ik dus in: de bereiken overlappen volledig. v3 lost T06 op, maar maakt T09 fout. Ook T03 bleek al fout met v2, dus dat lag niet aan mijn nieuwe regel. Opvallend: bij T12, T16, T17 en T19 gaf het model negen keer op negen een ander label dan ik. Mogelijk ligt de fout daar bij mijn labels, niet bij mijn tool.

## Model en effort
Voor de runs gokte ik dat Opus het best zou scoren en dat Sonnet goed genoeg zou zijn. Over drie runs op twintig inputs haalde Haiku 5.5 13 tot 14 op 20, Sonnet 5.5 telkens 14 op 20 en Opus 5.5 13 tot 14 op 20. Alle verschillen vallen binnen mijn foutmarge, dus op score zijn de modellen niet te onderscheiden. Ik kies toch Sonnet 5.5 met effort medium, omdat het het consequentst scoort. Voor Sporza kost dat ± € 24,55 per jaar, tegenover ± € 1,41 met Haiku en ± € 49,89 met Opus. Mijn gok klopte half: Opus was niet beter dan Sonnet, maar Sonnet was wel goed genoeg.

## Mijn value chain, met de foutmarge erin
Met de hand kost één renner ongeveer 10 minuten: berichten zoeken, verschillende artikels lezen en een label kiezen (geschat). Met de tool is dat 346 seconden: zoeken, plakken, draaien (7 s, gemeten) en nakijken, plus 30% fouten die ik met de hand herstel (480 s per fout). Dat is 254 seconden winst per renner. Voor 950 renners per jaar is dat ± 67 uur. Een werkgever betaalt ongeveer 1,5 keer het brutoloon, dus € 29,25 per uur (€ 19,50 bruto). Dat is € 1.960, min € 24,55 voor de tool: ± € 1.935 netto per jaar. Bij mijn laagste score (13 op 20) is het ± € 1.751. Mijn zwakste cijfer is de leestijd: halveert die, dan zakt het netto met € 1.215, terwijl mijn foutmarge maar € 184 verschil maakt.

## Mijn dashboard
Mijn dashboard: https://claude.ai/artifact/2SZCo8tKVB1iNmoDQDsgsk. Een lezer moet eerst zien dat mijn tool 13 tot 14 op 20 haalt, en dat het verschil tussen de drie modellen binnen die foutmarge valt.

## Mijn AI-ismen
Week 1: "Alles is uiteindelijk gelukt na wat opzoekwerk: de eerste pull request, git installeren en mijn weg vinden in de cursus."
Herschreven: Ik moest eerst git installeren, daarna kon ik mijn eerste pull request (#25) openen.

Week 2: "...en kan je dus een pronostiek maken op betrouwbare feiten."
Herschreven: ...en kan je een pronostiek maken op basis van artikels van Sporza, Wielerflits, NOS en Spaanse sportsites.

Week 3: "Het is positief omdat de basis van mijn AI al goed gebouwd is."
Herschreven: Al met v1 gaf mijn tool 8 van de 10 keer het juiste label (n = 5, 2 runs).

Week 4: "Mijn tool is dus stabiel: hij gaf bij elke input twee keer hetzelfde antwoord."
Herschreven: In 3 runs per versie gaf v3 bij 9 van de 10 inputs telkens hetzelfde label; alleen T08 wisselde.

Week 4: "Pas bij dat laatste volume doet het bedrag er echt toe."
Herschreven: Pas bij 1.000 keer mijn volume (950.000 runs per jaar) kost het ± € 24.500 per jaar met Sonnet 5.5; bij 950 runs is dat maar ± € 25.
