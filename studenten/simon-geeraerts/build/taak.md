# Build — Chatassistent voor de aankomst van een bestelde wagen

1. **Taak:** klanten laten zien wanneer hun bestelde Ford ongeveer bij Ford Geeraerts aankomt.
2. **Invoer:** de klantvraag, het vijfcijferige bestelbonnummer op de bestelbon, de naam waarop de wagen gekocht is en fictieve bestel- en leveringsgegevens uit een Excelbestand. De assistent vraagt eerst vriendelijk om het bestelbonnummer en daarna om de naam.
3. **Uitvoer:** model, huidige status en verwachte aankomstdatum. Bij geen match krijgt de klant een duidelijke melding. Is er nog geen datum, dan meldt de assistent dat duidelijk; de klant kan later opnieuw kijken.
4. **AI:** een taalmodel begrijpt de vraag van de klant en formuleert het antwoord in gewone taal. De gegevens uit Excel zijn altijd de bron van waarheid.
5. **Controle:** Simon vergelijkt elk antwoord met de juiste rij in Excel en controleert of de AI niets verzint.

## Vijf inputideeën van Simon

1. “Ik heb een wagen besteld, wanneer zou deze geleverd kunnen worden?”
2. “Is de levering van mijn wagen vertraagd?”
3. “Mijn wagen zou deze week aankomen. Klopt dat nog?”
4. “Ik vind mijn bestelbonnummer niet. Kunnen jullie mijn bestelling terugvinden?”
5. “Wanneer kan ik de wagen afhalen?”

Vragen 1 en 5 zijn door Simon geformuleerd. Vragen 2 tot en met 4 zijn door AI voorgesteld en door Simon geselecteerd; ze zijn nog niet bevestigd als echte klantvragen.

De juiste antwoorden schrijft Simon later zelf in `test-set.md`.

## Aankomst en afhalen volgens Simon

Na aankomst moet de wagen nog gekuist worden en moet de verzekering geregeld zijn. Daar is extra tijd voor nodig. De assistent kan de geregistreerde verwachte aankomstdatum al geven, maar die datum betekent niet dat de klant de wagen dan kan afhalen. Er is nog geen vaste voorbereidingstijd bepaald; de assistent mag die niet zelf verzinnen.

## Gewenste vervolgvraag volgens Simon

Bij de eerste testvraag vraagt de assistent naar zowel het bestelbonnummer op de bestelbon als de naam waarop de wagen gekocht is. Hoe de klant wordt gecontroleerd voordat bestelgegevens worden getoond, moet nog worden bepaald.

## Gegevensbron en beperking volgens Simon

De leveringsgegevens komen uit een Excelbestand met fictieve gegevens. Er is geen koppeling met echte leveringsgegevens of het Ford-programma. De assistent gebruikt de verwachte aankomstdatum uit Excel; die bevestigt dus geen werkelijke leverdatum.

## Nog uit te zoeken voor eventueel later gebruik door echte klanten

- Of en hoe de garage een geanonimiseerde export uit het Ford-programma kan maken.
- Of het bestelbonnummer en de naam in die export beschikbaar zijn om de bestelling terug te vinden.
- Hoe de website actuele bestelgegevens krijgt.
- Hoe klanten alleen hun eigen bestelling kunnen bekijken.
