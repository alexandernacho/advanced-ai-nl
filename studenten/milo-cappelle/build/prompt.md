# v1 — prompt

Plak dit in een nieuw gesprek. Vervang de beschrijving onderaan.

```text
Je leest de beschrijving van één bouwaanvraag uit een openbaar onderzoek van een Vlaamse gemeente. Je werkt voor een bedrijf in grond- en afbraakwerken. Geef precies één JSON-object terug, en verder niets.

Veld "soort_werk", kies precies één:
- "afbraak": er wordt iets gesloopt of afgebroken.
- "grondwerk": er wordt gegraven, bv. een kelder, funderingen, riolering of een parking.
- "beide": afbraak én grondwerk.
- "geen": geen afbraak en geen grondwerk.

Veld "interessant", kies precies één:
- "ja": er is afbraak of grondwerk, en het werk duurt langer dan één dag. Er is geen bovengrens, want het bedrijf doet ook projecten waar het een jaar aan werkt.
- "nee": er is geen afbraak en geen grondwerk, of het werk duurt ongeveer één dag, zoals een tuinhuis afbreken of een oprit uitgraven. Want zulke kleine werken neemt het bedrijf alleen aan in rustige periodes.
- "onzeker": de beschrijving geeft te weinig informatie om te kiezen.

Regels:
- Kies "onzeker" liever dan te gokken.
- Verzin geen werken die niet in de beschrijving staan.
- Geef in "reden" één korte zin: waarom deze keuze.

Formaat:
{"interessant": "ja|nee|onzeker", "soort_werk": "afbraak|grondwerk|beide|geen", "reden": "..."}

BESCHRIJVING
[plak de beschrijving]
```
