# v1 — prompt

Plak deze prompt in een nieuw, tijdelijk gesprek. Vervang alleen de tekst onder `REACTIE`.

```text
Je helpt een eventorganisator om één bezoekersreactie te ordenen. Geef precies één JSON-object terug, en verder niets.

Kies precies één label:
- "locatie/bereikbaarheid": een verbeterpunt over de eventlocatie, aanduiding, route, werken of bereikbaarheid.
- "programma": een verbeterpunt over optredens, stages of het programma.
- "catering": een verbeterpunt over eten of drinken.
- "prijs": een verbeterpunt over de kostprijs, tickets of consumpties.
- "personeel": een verbeterpunt over medewerkers, vrijwilligers of security.
- "veiligheid": een verbeterpunt over veiligheid, onveilig gedrag of drugs.
- "geen verbeterpunt": de reactie is uitsluitend positief of neutraal en bevat geen verbeterpunt.
- "onzeker/anders": de reactie is onduidelijk, bevat meerdere onderwerpen of past in geen label.

Regels:
- Kies "onzeker/anders" liever dan te gokken, want één reactie met meerdere of onduidelijke problemen kan niet eerlijk één specifiek verbeterpunt voorstellen.
- Verzin geen feiten die niet in de reactie staan.
- Geef in "reden" één korte zin die alleen op de reactie steunt.

Formaat:
{"label": "locatie/bereikbaarheid|programma|catering|prijs|personeel|veiligheid|geen verbeterpunt|onzeker/anders", "reden": "..."}

Voorbeeld:
Reactie: De straten lagen open, dus het was moeilijker bereikbaar. De locatie was niet zo goed aangeduid. Het eten was wel heel lekker.
Uitvoer: {"label": "locatie/bereikbaarheid", "reden": "De reactie gaat over aanduiding en bereikbaarheid van de locatie."}

Voorbeeld:
Reactie: Muziek was top!
Uitvoer: {"label": "geen verbeterpunt", "reden": "De reactie is uitsluitend positief over de muziek."}

Voorbeeld:
Reactie: Ik vond het te duur.
Uitvoer: {"label": "prijs", "reden": "De bezoeker vindt de kostprijs te hoog."}

REACTIE
[plak hier één bezoekersreactie]
```
