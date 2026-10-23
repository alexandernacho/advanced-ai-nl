# Herhaaltest v3 — 22 oktober 2026

Vijf vooraf door de student bevestigde inputs, elk drie nieuwe onafhankelijke sessies. Model: GPT-6.1 Sol, effort low. De runbestanden zijn ruwe uitvoer; een aanwezig bestand is nog geen geslaagde run.

## Afbakening vóór de runs

- `prompt-extractie.md` is een afzonderlijk vastgelegde extractievariant van v3: financiële regels behouden, output als controletabel en JSON in het antwoord, geen Excel-update of wisselkoersen ophalen.
- Volledige PDF-tekst wordt vooraf met pypdf geëxtraheerd, met PDF-paginamarkeringen. Het model krijgt tekst, geen visuele PDF. Dit kan fouten door tekstextractie veroorzaken; de test meet die tekstpipeline mee.
- Voor Lilly en Uber wordt de eerder bevestigde halfjaarperiode vooraf meegegeven, zonder de verwachte cijfers. Deze test beoordeelt de extractie na de keuze, niet het interactieve wachten op een keuze.
- Alleen de input en extractieprompt worden via stdin meegegeven. Sessies starten in een lege tijdelijke map, zonder projectinstructies en zonder gebruikersconfiguratie. Shell, web, apps, plugins, hooks, geheugen en delegatie worden voor de run uitgezet. Eventuele geregistreerde toolacties maken de run ongeschikt voor deze proef.
- De runner leest `test-set-v3.md` niet. Verwachte antwoorden blijven apart voor beoordeling achteraf.
- `manifest.json` bewaart bron- en inputhashes, paginatellingen, model en effort. Dezelfde input gaat naar elk van de drie herhalingen.
- `*.events.jsonl` bewaart sessiegebeurtenissen en beschikbaar tokenverbruik; `*.txt` het laatste antwoord; `*.meta.json` starttijd, duur, exitcode en commando.

Dit is één huidige promptvariant met n = 5 en drie herhalingen. Het is geen vergelijking met v2 en geen bewijs dat v3 beter is. De financiële beoordeling volgt uitsluitend de vooraf bevestigde regel: juiste cijfers, perioden, valuta en schuldbeperking.
