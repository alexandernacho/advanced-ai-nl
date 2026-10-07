# Taak — eventreactiesorteerder

De tool helpt een eventorganisator om bezoekersreacties te ordenen en te zien welke verbeterpunten het vaakst terugkomen.

## Input

Eén geanonimiseerde bezoekersreactie uit een enquête of van sociale media.

## Uitvoer

De tool geeft precies één label met een korte reden:

| Label | Betekenis |
|---|---|
| `locatie/bereikbaarheid` | Een verbeterpunt over de eventlocatie, aanduiding, route, werken of bereikbaarheid. |
| `programma` | Een verbeterpunt over optredens, stages of het programma. |
| `catering` | Een verbeterpunt over eten of drinken. |
| `prijs` | Een verbeterpunt over de kostprijs, tickets of consumpties. |
| `personeel` | Een verbeterpunt over medewerkers, vrijwilligers of security. |
| `veiligheid` | Een verbeterpunt over veiligheid, onveilig gedrag of drugs. |
| `geen verbeterpunt` | De reactie is uitsluitend positief of neutraal en bevat geen verbeterpunt. |
| `onzeker/anders` | De reactie is onduidelijk, bevat meerdere onderwerpen of past in geen label. |

Daarna kan de organisator de labels tellen om de drie meest voorkomende verbeterpunten te zien.

## Controle

Voor elke testreactie leg ik vooraf zelf het juiste label vast. Bij twijfel kiest de tool `onzeker/anders` in plaats van te gokken.
