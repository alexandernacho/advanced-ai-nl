# Taak — Bouwaanvragen sorteren voor een grond- en afbraakbedrijf

1. **Taak:** de tool leest de beschrijving van een bouwaanvraag en zegt of er werk in zit voor een grond- en afbraakbedrijf.
2. **Wat erin gaat:** de beschrijving uit een bekendmaking van een openbaar onderzoek van een Vlaamse gemeente, zonder namen.
3. **Wat eruit komt:** *Interessant* (ja / nee / onzeker) + *Soort werk* (afbraak / grondwerk / beide / geen) + één zin reden. "Onzeker" is de uitweg.
4. **Soort AI:** een taalmodel. Het is vrije tekst, en hetzelfde wordt op veel manieren gezegd ("slopen", "afbreken", "na afbraak van", "herbouw").
5. **Check:** twee mensen kunnen per veld los van elkaar beslissen wat juist is. De juiste antwoorden staan vooraf in `test-set.md`.

## Vijf inputideeën

1. Een hangar afgebroken
2. Een kelder voor een appartementsgebouw uitgegraven
3. Een afbraak van een rijwoning
4. Renovatie/afbraak van 11 sociale woningen
5. Plaatsen van L-panelen en parking van een Lidl
