# Week 3 — Een AI-tool uitwerken en testen

Deze week werkte ik mijn idee verder uit: een eventreactiesorteerder. De tool moet een bezoekersreactie over een event in precies één categorie plaatsen, zoals prijs, catering, programma of bereikbaarheid. Zo kan een organisator sneller zien welke verbeterpunten het vaakst terugkomen.

Ik merkte dat duidelijke afspraken vooraf heel belangrijk zijn. Daarom heb ik per label uitgelegd wanneer het gebruikt mag worden. Als een reactie meerdere onderwerpen bevat of niet duidelijk is, kiest de tool voor `onzeker/anders`. Zo vermijdt de tool dat ze zomaar gokt.

Daarna maakte ik een testset met vooraf bepaalde juiste antwoorden. Ik testte de prompt twee keer met tien reacties. In beide rondes gaf de tool tien van de tien juiste labels. Dat resultaat is positief, maar ik wil later nog testen met meer en moeilijkere reacties.

Wat ik vooral leer: AI werkt beter als je een taak klein en concreet maakt. Het is niet genoeg om gewoon te vragen om reacties te sorteren; je moet ook duidelijke categorieën, regels en controles voorzien.
