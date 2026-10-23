# Schuldcontrole bij kwartaalupdates

Keuze van de student, 23 oktober 2026: GPT-6.1 Sol, effort low, met extra handmatige schuldcontrole. Deze procedure is een aanvulling op de geteste v3-extractie; het effect en de tijd zijn nog niet gemeten.

## Tijdsinschatting van de student

De student schat de schuldcontrole op **maximaal 5 minuten per bedrijfsupdate**, met als toelichting: “want ik doe altijd al controle bij ai”. Dit is een eigen inschatting, geen chronometermeting of gegarandeerde bovengrens bij moeilijke rapporten.

De bestaande tijdsinschatting bevat al 7 minuten controleren binnen 15 minuten totale tooltijd. Daarom wordt de schuldcontrole voorlopig als onderdeel van die bestaande controle behandeld en niet automatisch als 5 extra minuten opgeteld. Evenmin wordt de volledige controletijd vervangen door 5 minuten: die uitspraak betreft de schuldcontrole. Werkelijke overlap en tijd voor eventuele correcties zijn nog niet afzonderlijk gemeten.

De student schat daarna het **herstellen van een gevonden fout op ongeveer 7 minuten extra**, inclusief feedback doorgeven. Dit is een afzonderlijke schatting voor corrigeren, boven op de gewone controle; geen gemeten tijd. De hoop dat feedback herhaling voorkomt is niet getest. Leg een blijvende instructieverbetering expliciet vast en test die opnieuw voordat een lager foutaandeel wordt geclaimd. Zie `waarde.md` voor de berekening met zeven minuten herstel.

## Per update

1. Controleer de bedrijfsnaam, peildatum, oorspronkelijke valuta en eenheid van de schuldbedragen in het rapport.
2. Zoek kortlopende schuld, het kortlopende deel van langlopende schuld en langlopende schuld. Controleer of het kortlopende deel al in een totaal zit voordat je optelt.
3. Zoek daarnaast kredietfaciliteiten, financiële leases en financieringsverplichtingen. Toon per component bedrag, bronpagina, opname in het totaal en eventuele dubbeltelling. Voor de gekozen brede schuldafbakening tellen financiële leases en financieringsverplichtingen mee voor zover ze niet al inbegrepen zijn. Operationele leases worden afzonderlijk getoond en uitgesloten. Als de bron leasecategorieën niet scheidt, benoem de beperking en gebruik Onzeker.
4. Renteloze obligaties blijven meetellen tegen hun gerapporteerde boekwaarde. Trek kasmiddelen niet af en gebruik geen totale verplichtingen als vervanging voor financiële schuld.
5. Reken de som opnieuw uit. Benoem afgeronde bronbedragen en presenteer een daardoor benaderend totaal ook als benadering. Ontbrekende informatie is onbekend, niet nul; gebruik Onzeker als de volledigheid of afbakening niet vaststaat.
6. Vergelijk de gekozen hoofdwaarde met de componenten in tabel en JSON. Een toelichting met apart genoemde leases is onvoldoende als ze volgens de gekozen afbakening ook in de hoofdwaarde moeten zitten.
7. Laat de student deze aansluiting controleren vóór de schuldwaarde als Gecontroleerd wordt gemarkeerd. De agent kan de aansluiting voorbereiden, maar kent die status niet zelfstandig toe. Bewaar beperkingen ook na controle van het berekenbare bedrag.

## Aanleiding: Amazon in de modeltest

Sol gaf 132.549 miljoen USD als hoofdwaarde en hield financiële leases en financieringsverplichtingen erbuiten. De vooraf vastgelegde verwachting was circa 155.315 miljoen USD:

`132.549 leningen en obligaties + 13.451 financiële leases + circa 9.315 financieringsverplichtingen = circa 155.315 miljoen USD`.

Operationele leases van 96.320 miljoen USD blijven apart. Het totaal is benaderend doordat de langlopende financieringsverplichtingen afgerond zijn. Dit is een testvoorbeeld, geen standaardbedrag voor andere rapporten of perioden.

## Vastleggen

Noteer per update het bedrijf en de peildatum, de gecontroleerde aansluiting, de bronpagina's, resterende onzekerheid en het oordeel van de student. Gebruik maximaal 5 minuten voorlopig als eigen tijdsinschatting voor de schuldcontrole; noteer bij een latere tijdmeting welk deel al binnen de bestaande controle valt en hoeveel tijd eventuele correcties kosten. Een eventueel aangepaste prompt krijgt een nieuwe versie en een nieuwe test; eerdere scores blijven bij de oorspronkelijke opzet horen.
