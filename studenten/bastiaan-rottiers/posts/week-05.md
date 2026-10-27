# Week 5: Wat we nog moeten doen

## Mijn foutmarge

v6 (gereconstrueerd) en v7 draaiden elk drie rondes op T06–T10, met GPT-6.1 Sol medium. v6: 2/5, 2/5 en 3/5; v7: 3/5, 3/5 en 4/5. De bereiken overlappen bij 3/5, dus ik trek de algemene verbeterclaim in. T10 haalde met v7 vaker de gewenste eindstatus. Het foute verwachte antwoord van T08 is openlijk gecorrigeerd in build/log.md. Ik keek T07 en T10 zelf na.

## Model en effort

Mijn gok vooraf: Astra medium scoort het best en Luna low is goed genoeg. Eén ronde per setup (n = 5): Sol medium 4/5, Luna low 2/5 en Astra medium 4/5. Kosten per taak: circa €0,049, €0,0024 en €0,242. Luna valt onder mijn foutmarge; Sol en Astra erin. Ik kies Sol medium: dezelfde score als Astra tegen lagere kost.

## Mijn value chain, met de foutmarge erin

Mijn stappen: lezen 5–10 min, begrijpen/zoeken 20–25 min en plannen minstens 5 min. Ik reken met 35 min handwerk. De tool verwerkt in maximaal 5 min; controleren kost circa 3 min.

v7 haalde gemiddeld 10/15. Herstel per fout duurt naar schatting 35 min: gemiddeld 11,67 min extra. Samen met draaien en nakijken is dat 19,67 min, tegenover 35 min handwerk: 15,33 min winst per taak.

Acht taken per maand zijn 96 per jaar of 24,53 uur. Tegen mijn tijdwaarde van €20/uur is dat €490,67; Sol kost zonder cache circa €3,08 per jaar, dus netto blijft circa €488. Het bereik is €413–€637. Met een hypothetische werkgeverskost van €30/uur (€20 bruto × 1,5) is de netto waarde circa €733, met bereik €621–€957. Mijn zwakste cijfer is handwerktijd: bij 17,5 min daalt netto aan €20 naar €114.

## Mijn dashboard

[Mijn publieke dashboard](https://raw.githack.com/BastiaanRottiers/advanced-ai-nl/week-05/studenten/bastiaan-rottiers/build/dashboard.html). Bekijk eerst de overlappende scorebereiken; set v2 is een eerste controle met twintig inputs en één run. Mijn volgende gebruik wordt vooral het nalezen van financieel plan en marktonderzoek, ook zonder Canvas-opdracht.

## Mijn AI-ismen

**Week 2:**
> Dit toont dat een taalmodel vaak dingen verzint omdat het denkt dat je daar naar op zoek bent, terwijl je die instructie niet gaf.

Herschreven: Bij T01 verzon de eerste run onder andere een ritssluiting, een logo en een QR-code die niet in mijn input stonden.

**Week 3:**
> Ook de buurtest maakte duidelijk dat de context nog niet scherp genoeg was.

Herschreven: Mijn broer las alleen de prompt, beantwoordde drie inputs en miste velden in de uitvoer.

**Week 3:**
> De testset helpt mij om niet alleen te kijken of een antwoord goed klinkt, maar ook of elk onderdeel werkelijk uit mijn eigen input komt.

Herschreven: Bij T01 stonden vilt en klikgespen in het antwoord, hoewel ik die niet had opgegeven.

**Week 4:**
> De tool is dus niet foutloos, maar de testset toont wel dat ik fouten kan vinden, een oorzaak kan benoemen en daarna gericht kan verbeteren.

Herschreven: In week 4 waren tien van de veertien beoordeelde antwoorden juist.

**Week 4:**
> Hij helpt mij niet alleen tijd winnen, maar geeft ook het team eenzelfde overzicht van wat we al hebben en wat er nog ontbreekt.

Herschreven: Bij ons financieel plan wil ik laten nakijken wat al ingevuld is en wat we nog moeten doen.

## Mijn testset groeit

Ik koos T11–T20 uit onze grote, complexe bestanden; de inputs vragen meer dan 15 minuten voorbereiding. De v7-run scoorde **10 op 20 (set v2, 1 run; n = 20)**. Het meest verraste me dat de tool bij T19 niet uit een lege logboekregel afleidde of ik erbij was. Hij vroeg of ik deelnam, zodat ik dat kan bevestigen en mijn logboek kan aanvullen.
