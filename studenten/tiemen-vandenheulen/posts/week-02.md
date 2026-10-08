# Week 2 — Reviews ordenen

## Wat bouw ik?

Ik bouw een tool die een organisator helpt om korte bezoekersreviews na een evenement snel te sorteren. De invoer is één review per keer; de uitvoer is één of meer labels, zoals `organisatie`, `sfeer`, `locatie` of `wachttijden`.

## Waarom een taalmodel?

Een taalmodel past bij deze taak omdat het de betekenis van vrije tekst moet interpreteren en die aan de juiste categorieën moet koppelen.

## Eén testinput

De testinput was: “Leuke locatie en genoeg te doen. Het was op sommige momenten wel erg druk.” Mijn vooraf gekozen juiste antwoord was `locatie`, omdat de review de locatie expliciet benoemt. In beide runs gaf de tool `organisatie` en `locatie` terug. `locatie` was juist, maar `organisatie` was extra. De tool kwam bij deze input dus niet volledig overeen met mijn verwachte antwoord.
