# Waardeketen — Canvas-assistent WATTZAK

Datum: 20 oktober 2026

| Schakel | Waarde | Bron / aanname |
| --- | --- | --- |
| Met de hand | 30 min per belangrijk Canvas-document of opdracht: lezen, begrijpen en in de agenda zetten of ermee starten | inschatting Bastiaan, 20 oktober 2026 |
| Met de tool | maximaal 4 min per run, inclusief de uitvoer nakijken | inschatting Bastiaan, 20 oktober 2026 |
| Winst per taak | 30 − 4 = **26 min** | berekening |
| Volume | 8 runs per maand | minstens 6 belangrijke documenten + 1 à 2 opdrachten per maand; voorzichtig afgerond |
| Winst per week | 2 taken × 26 min = **52 min** (≈ 0,87 uur) | aanname: 4 weken per maand |
| Winst per maand | 8 taken × 26 min = **208 min** (≈ 3,47 uur) | berekening |
| Winst per jaar | 96 taken × 26 min = **2.496 min** = **41,6 uur** | aanname: 12 maanden per jaar |
| Kost van de tool per jaar | €0,40 × 12 = **≈ €4,80** met GPT-6.1 Sol | kostenmeting in `build/kosten.md` |

## Jaarwaarde

| Schakel | Waarde | Bron / aanname |
| --- | ---: | --- |
| Uurkost | €20 per uur | voorzichtige uurwaarde voor één WATTZAK-teamlid; aanname van Bastiaan, geen werkelijk loon |
| Brutowaarde per jaar | 41,6 uur × €20 = **€832,00** | berekening |
| Kost van de tool per jaar | **€4,80** | `build/kosten.md` |
| Netto waarde per jaar | €832,00 − €4,80 = **€827,20** | berekening |

## Zwakste cijfer

De 30 minuten handmatig werk is een schatting, geen tijdsmeting. Als de werkelijke tijd maar 15 minuten is, blijft de winst 11 min per taak: 96 × 11 min = **17,6 uur per jaar**, vóór aftrek van de toolkost.

## Week 5: waardeketen met fouten herstellen

Datum: 27 oktober 2026. De laatste uitsplitsing van de tijdschattingen vervangt voor deze berekening de eerdere 30 minuten handwerk en 4 minuten tooltijd. De week-4-berekening hierboven blijft als historiek staan. Alle tijden hieronder zijn eigen schattingen, geen chronometermetingen.

### Tijd per stap

| Zonder de tool | Eigen schatting | Middenwaarde voor de berekening |
|---|---:|---:|
| Opdracht en bijhorende documenten lezen | 5–10 min | 7,5 min |
| Begrijpen, controleren en zoeken wat al gedaan is | 20–25 min | 22,5 min |
| Bepalen en plannen wat nog moet gebeuren | minstens 5 min | 5 min |
| Totaal bij 5 minuten plannen | 30–40 min | **35 min** |

De laatste concrete uitsplitsing telt op tot 30–40 minuten bij 5 minuten plannen. Die vervangt de eerdere globale schatting van 25–30 minuten. De middenwaarde van 35 minuten is een rekenkeuze op basis van de opgegeven stappen. Omdat plannen minstens 5 minuten duurt, is 40 minuten geen harde bovengrens.

| Met de tool | Eigen schatting |
|---|---:|
| Input geven, bestanden verwerken en antwoord afwachten | maximaal 5 min |
| Zelf nalezen en controleren | ongeveer 3 min |
| Draaien + nakijken samen, vóór extra fouten herstellen | **8 min** |

De drie minuten nakijken veronderstellen dat de tool duidelijk aangeeft waar informatie staat, zodat een betwijfeld antwoord terug te vinden is. Dat is een gebruiksvoorwaarde, nog geen gemeten eigenschap van v7. Extra fouten herstellen wordt hier apart opgeteld.

Voor deze berekening: v7 met Sol medium. In de foutmargetest: **3/5, 3/5 en 4/5**, n = 5 inputs, drie rondes; samen 10/15 juist. Gemiddelde juistheid 66,7%, geobserveerd bereik 60–80%. Dit gemiddelde is geen extra vierde run.

### Eigen tijdwaarde: €20 per uur

| Schakel | Gemiddeld scenario | Bron / aanname |
|---|---|---|
| Handmatig werk | **35 min** | Middenwaarde van de eigen tijdschattingen hierboven; plannen op 5 min gezet. |
| Draaien + nakijken | 5 + 3 = **8 min** | Eigen schattingen; bronverwijzingen nodig om snel na te kijken. |
| Fouten herstellen | (1 − 10/15) × 35 = **11,67 min per taak** | Lesformule; één fout volledig herstellen kost evenveel als de taak handmatig doen. |
| Totale tooltijd | 8 + 11,67 ≈ **19,67 min** | Fouten herstellen boven op draaien/nakijken. |
| Winst per taak | 35 − 19,67 ≈ **15,33 min** | Berekening met ongeronde tussenwaarden. |
| Volume | **0,4 taak per werkdag · 2 per week · 8 per maand · 96 per jaar** | Bestaande volumeschatting. Weergave met 20 werkdagen en 4 weken per maand; jaar met 12 maanden. |
| Urenwinst | **0,102 uur per werkdag · 0,511 per week · 2,044 per maand · 24,53 per jaar** | Tijdwinst × volume / 60; geen vermenigvuldiging met vier groepsleden. |
| Uurwaarde | **€20** | Eigen tijdwaarde uit week 4; geen werkelijk loon en geen gemeten werkgeverskost. |
| Jaarwaarde vóór toolkost | 24,53 × €20 ≈ **€490,67** | Berekend met ongeronde uren. |
| Toolkost per taak | **€0,03212532** | API-equivalente raming op gemeten gemiddelde Sol-tokens, zonder cachekorting; zie kosten.md. |
| Toolkost per maand / jaar | **€0,25700256 / €3,08403072** | 8 / 96 taken; standaardtarief en aanname $1 = €0,90. |
| Netto per jaar | €490,67 − €3,08403072 ≈ **€487,58** | Geschatte tijdwaarde minus API-equivalente kost; geen werkelijk gerealiseerde kasbesparing. |

### Bereik door de score, met handwerk vast op 35 minuten

| Schakel | 3/5 juist: 60% | Gemiddeld 10/15: 66,7% | 4/5 juist: 80% |
|---|---:|---:|---:|
| Fouten herstellen (min) | 14,00 | 11,67 | 7,00 |
| Totale tooltijd (min) | 22,00 | 19,67 | 15,00 |
| Winst per taak (min) | 13,00 | 15,33 | 20,00 |
| Uren per jaar | 20,80 | 24,53 | 32,00 |
| Waarde aan €20 per uur | €416,00 | €490,67 | €640,00 |
| Toolkost per jaar | €3,08403072 | €3,08403072 | €3,08403072 |
| Netto per jaar | **€412,92** | **€487,58** | **€636,92** |

Dit bereik van **€412,92–€636,92** komt alleen van de drie geobserveerde scores. Het is geen statistisch betrouwbaarheidsinterval.

### Apart scenario: werkgeverskost €30 per uur

De les gebruikt als vuistregel bruto × 1,5. **Als** het brutoloon €20 per uur is, wordt de werkgeverskost €30. Dit is een aparte loonaanname: de eigen €20 tijdwaarde hierboven is geen gemeten brutoloon. Er is voor WATTZAK geen werkelijke loonkost gemeten.

| Schakel | Gemiddeld | Bij 3/5 | Bij 4/5 |
|---|---:|---:|---:|
| Uren gewonnen per jaar | 24,53 | 20,80 | 32,00 |
| Werkgeverskost per uur | €30 | €30 | €30 |
| Jaarwaarde vóór toolkost | €736,00 | €624,00 | €960,00 |
| Netto na €3,08403072 toolkost | **€732,92** | **€620,92** | **€956,92** |

Bron voor de vuistregel: [les week 5, value chain](../../../cursus/week-05/README.md#waarde-de-value-chain-met-de-foutmarge-erin). Dit is een rekenaanname, geen loonberekening voor een concrete werkgever.

### Apart bereik door de tijdschatting

Bij de gemiddelde score 10/15 en dezelfde 8 minuten draaitijd plus nakijken geeft 30–40 minuten handwerk een netto jaarwaarde aan €20 van **€380,92–€594,25**.

Als zowel de handwerktijd als de score varieert, geven het scenario met 30 minuten en 3/5 en het scenario met 40 minuten en 4/5 samen **€316,92–€764,92**. Dit is een gecombineerd rekenscenario, niet de scorefoutmarge. De bovengrens veronderstelt 5 minuten plannen.

### Zwakste cijfer: de geschatte handwerktijd

Halveer de middenwaarde van 35 tot **17,5 minuten** en gebruik ook 17,5 minuten om één fout volledig met de hand te herstellen. Draaien/nakijken blijft 8 minuten en het volume blijft 96 taken per jaar.

| Schakel bij 17,5 min handwerk | Gemiddeld | Bij 3/5 | Bij 4/5 |
|---|---:|---:|---:|
| Fouten herstellen (min) | 5,83 | 7,00 | 3,50 |
| Totale tooltijd (min) | 13,83 | 15,00 | 11,50 |
| Winst per taak (min) | 3,67 | 2,50 | 6,00 |
| Uren per jaar | 5,87 | 4,00 | 9,60 |
| Netto aan €20 tijdwaarde | **€114,25** | **€76,92** | **€188,92** |
| Netto aan €30 werkgeverskost, apart scenario | **€172,92** | **€116,92** | **€284,92** |

Aan €20 tijdwaarde verlaagt halvering van de handwerktijd het gemiddelde netto met **€373,33**. Het volledige scorebereik bij 35 minuten verschuift het netto met **€224,00**. Aan €30 werkgeverskost zijn die effecten **€560,00** en **€336,00**. De handwerktijd beweegt de uitkomst dus sterker dan de geobserveerde scorevariatie.

### Nog te meten

Alle tijden zijn nu per stap geschat, maar nog niet met een chronometer gemeten. Ook de werkelijke herstelduur, de nakijktijd als bronverwijzingen ontbreken, en de kwaliteit op nieuwe taken rond financieel plan en marktonderzoek zijn nog niet afzonderlijk getest. T08 bevat een bekende tegenstrijdigheid in de testset. Deze scenario's bewijzen geen financiële besparing in de praktijk.
