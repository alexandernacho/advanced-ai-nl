# Week 5: Ik had Luna anders ingeschat

## Mijn foutmarge

Mijn tool verwerkt één bedrijf per prompt. De extractievariant van v3 draaide op GPT-6.1 Sol, effort low, drie keer op dezelfde vijf inputs: telkens 5/5 (n = 5). De agent beoordeelde de antwoorden; ik controleerde Netflix en Amazon en keurde die goed. De verwachte antwoorden bleven ongewijzigd.

In de modeltest scoorde Sol daarna 4/5. Bij Amazon ontbraken financiële leases en financieringsverplichtingen in de schuldhoofdwaarde. Over vier Sol-rondes is 4–5/5 waargenomen. Dat is geen statistisch betrouwbaarheidsinterval. Een vorige promptversie is niet vergeleken: v2 vergeleek twee bedrijven, v3 verwerkt er één. Een verbeterclaim is niet getoetst.

## Model en effort

Ik gebruikte Sol al en het kon mijn taak aan. Op dezelfde vijf inputs, één run per model en effort low, scoorden Sol 4/5, Luna 0/5 en Astra 5/5. Luna’s nul verraste mij. Veel bedragen klopten, maar per antwoord ontbrak minstens één controlepunt, zoals schuldafbakening of onzekerheid.

Het gemiddelde API-equivalent per extractie was $0,174 voor Sol, $0,009 voor Luna en $0,882 voor Astra. Dit zijn tokenkosten, geen extra Plus-factuur. Mijn model gebruikt gemiddeld 85.847 inputtokens en 1.733 outputtokens; hardwarebelasting is niet gemeten. Astra scoort deze ronde hoger, maar valt binnen het waargenomen Sol-bereik. Ik verkies Sol met schuldcontrole; ik werk er momenteel al mee.

## Mijn value chain, met de foutmarge erin

Handmatig schat ik 5 minuten zoeken, 45 minuten verzamelen en invoeren, en 10 minuten controleren: 60 minuten. Met de tool schat ik 8 minuten uitvoeren en 7 minuten controleren. De maximaal 5 minuten schuldcontrole vallen voorlopig binnen die controle. Een gevonden fout herstellen en feedback doorgeven schat ik op 7 minuten extra.

Bij 80–100% volledig geslaagde updates wordt de gemiddelde tooltijd 15–16,4 minuten. De winst is 43,6–45 minuten per update. Tien bedrijven per kwartaal geven 40 updates en 29,07–30 uur mogelijke jaarwinst. Mijn persoonlijke uurwaarde is €5, geen werkgeversloonkost. Dat geeft €145,33–€150 vóór toolkosten. Met het historische volledige-runkostscenario van circa €8,01 per jaar blijft €137,32–€141,99 over. De extractiekosten hierboven hebben een andere scope.

Mijn zwakste aanname blijft het volume. Bij twintig updates wordt het netto €68,66–€70,99. Zonder tool laat ik de verwerking vaak liggen; dit is mogelijke tijdwinst tegenover handwerk, geen gerealiseerde opbrengst. Feedback garandeert geen lager toekomstig foutaandeel.

## Mijn dashboard

[Mijn publieke dashboard](https://kwartaalopvolging-week-vijf.socialmorel1025.chatgpt.site) toont eerst het scorebereik en de mogelijke tijdwaarde, met de aannames erbij.

## Mijn AI-ismen

Week 2:

> Zo hoef ik niet alle informatie zelf op te zoeken en kan ik aandelen in één oogopslag vergelijken op belangrijke factoren.

Herschreven: In week 2 liet ik de tool FCF, schuld, omzetgroei en risico’s van twee bedrijven naast elkaar zetten.

Week 3:

> Een duidelijke tabel met de belangrijkste informatie en de onderbouwing eronder maakt die vergelijking voor mij makkelijker.

Herschreven: Eerst stond de redenering onder elk cijfer; na de aanpassing stonden alle cijfers bij elkaar, met de redenering en bronpagina’s eronder.

Week 3:

> De tabellen werden ook steeds duidelijker na aanpassingen aan de instructies.

Herschreven: Na de aanpassing vergeleek ik voor beide bedrijven cijfers over dezelfde verslagperiode, bijvoorbeeld een kwartaal of een halfjaar.

Week 4:

> De tool maakt de opvolging vooral haalbaar.

Herschreven: Met de tool verwerk ik gepubliceerde kwartaalresultaten sneller in Excel; zonder die hulp laat ik het vaak liggen.

Week 4:

> Eerst wil ik mijn huidige werkwijze consequent gebruiken.

Herschreven: Ik wil elk kwartaal de resultaten van tien bedrijven verwerken zodra die gepubliceerd zijn.
