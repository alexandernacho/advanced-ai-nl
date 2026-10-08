# Build — Review-sorteerder voor evenementen

- **Taak:** een organisator helpen om korte bezoekersreviews na een evenement snel te sorteren.
- **Invoer:** één korte bezoekersreview per keer.
- **Uitvoer:** één of meer labels uit `organisatie`, `prijs`, `sfeer`, `locatie`, `wachttijden`, `catering` en `veiligheid`; anders `andere`.
- **AI:** een taalmodel, omdat het de betekenis van vrije tekst moet interpreteren en die aan passende thema’s koppelt.
- **Check:** de student labelt vooraf een testset; een antwoord is juist wanneer de tool dezelfde relevante categorieën kiest.

## Vijf inputideeën

1. “Leuke sfeer en alles was goed geregeld. We hebben ons de hele avond prima vermaakt.”
2. “Fijn evenement met een goede mix van activiteiten. De wachtrij bij de ingang duurde wel even.”
3. “Gezellige dag gehad! Vooral de optredens maakten het voor mij de moeite waard.”
4. “Goed georganiseerd en vriendelijk personeel. Ik kom volgend jaar graag weer.”
5. “Leuke locatie en genoeg te doen. Het was op sommige momenten wel erg druk.”

_De juiste antwoorden schrijft de student vooraf in `build/test-set.md`._
