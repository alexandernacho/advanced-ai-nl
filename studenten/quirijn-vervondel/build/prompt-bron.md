# Prompt v1 + bron: notities plaatsbezoek naar stuklijst

Dit is een uitbreiding van `build/prompt.md` (v1). Het verschil zit alleen in de regels over de bron en de kolom Bron. Alle rekenregels en de uitvoertabel blijven gelijk.

Je krijgt de getypte notities van een plaatsbezoek voor een airco- of warmtepompinstallatie. Maak er een stuklijst met hoeveelheden van.

Je krijgt ook een technisch document als bron, tussen `<bron>` en `</bron>`. Gebruik het alleen om technische gegevens in te vullen die de notities niet geven, zoals leidingdiameter, isolatie, elektrische kabel en condensafvoer. Het vervangt de rekenregels niet.

## Regels
- Gebruik alleen wat in de notities staat, wat in het document staat, of wat volgt uit de rekenregels hieronder. Verzin geen afstanden, aantallen, types of onderdelen.
- Staat iets niet in de notities, het document, en volgt het niet uit een rekenregel? Schrijf dan: `onbekend, na te vragen`.
- Gebruik het document alleen voor het model dat erin staat. Staat er een ander model of een andere installatie in de notities? Gebruik het document dan niet, en schrijf `onbekend, na te vragen`.
- Leidingen of onderdelen die hergebruikt worden, komen niet op de stuklijst.
- Rond elke hoeveelheid naar boven af op een heel getal.
- Wat je aansnijdt, reken je volledig aan. Een overschot wordt ook aangerekend.

## Rekenregels
- Koelleiding: in meter, één lengte per leidingpaar (vloeistof- en gasleiding samen). Geef per binnenunit de lengte naar de buitenunit, en daaronder het totaal.
- Communicatiekabel: in meter, altijd gelijk aan het totaal van de koelleiding.
- Voedingskabel: in meter. Er is geen vaste regel. Vul alleen in als de lengte in de notities staat.
- Aansluitpunt voeding: `zekeringkast` of `stopcontact`, zoals in de notities staat.
- Elektriciteitsbuis: in meter, zoals in de notities staat.
- Kabelgoot: in stuks. Eén stuk is 2 meter. Aantal stuks = meters kabelgoot gedeeld door 2, naar boven afgerond. Voorbeeld: 7 meter kabelgoot is 4 stuks.
- Bochten en tussenstukken: per soort, bijvoorbeeld bocht 90 graden, T-stuk, dakrandstuk. Neem alleen soorten en aantallen over die in de notities staan. Staat er een route maar geen aantal? Schrijf `onbekend, na te vragen`.
- Condensafvoer: lengte in meter, en het type: `gravitair naar buiten` of `druk-PVC`. Neem het type alleen over als het in de notities staat. Kies het niet zelf.

## Uitvoer
Geef alleen deze tabel, niets anders. Voeg per binnenunit een rij koelleiding toe, en per soort bocht of tussenstuk een rij.

| Onderdeel | Hoeveelheid | Eenheid | Bron |
|---|---|---|---|
| Koelleiding unit 1 | | m | |
| Koelleiding unit 2 | | m | |
| Koelleiding totaal | | m | |
| Communicatiekabel | | m | |
| Voedingskabel | | m | |
| Aansluitpunt voeding | | - | |
| Elektriciteitsbuis | | m | |
| Kabelgoot | | stuks | |
| Condensafvoer lengte | | m | |
| Condensafvoer type | | - | |
| Leidingdiameter vloeistofleiding | | mm | |
| Isolatiedikte gasleiding (minimum) | | mm | |
| Verbindingskabel binnen-buiten | | - | |
| Muurgat diameter (FTXTM30R2V1B) | | mm | |
| Maximale koelleidinglengte | | m | |
| <soort bocht of tussenstuk> | | stuks | |

Voor de rijen Leidingdiameter, Isolatiedikte, Verbindingskabel, Muurgat en Maximale koelleidinglengte geldt: vul ze alleen in uit het document, en zet dan het document als bron. Staat het niet in het document, schrijf `onbekend, na te vragen`.

Bron:
- `notities` als het letterlijk in de notities staat.
- `rekenregel` als je het afleidde met een rekenregel.
- `document, p. <nummer> (sectie <nummer>)` als het uit het brondocument komt. Geef het paginanummer en het sectienummer van het document.
- Leeg bij `onbekend, na te vragen`.

## Bron
<bron>
<plak hier de inhoud van build/bronnen/<bestandsnaam>>
</bron>

## Notities
<plak hier de notities van het plaatsbezoek>
