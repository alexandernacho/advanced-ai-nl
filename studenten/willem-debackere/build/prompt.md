# v1 — prompt

Plak dit in een nieuw gesprek. Vervang de websitetekst onderaan.

```text
Je beoordeelt één bedrijf als mogelijke klant voor DBA Hardwoods, een houthandel die nu vooral rubberwood verkoopt aan bedrijven die in massief hout werken. Geef precies één JSON-object terug, en verder niets.

Stap 1: kies "doelgroep":
- "ja": het bedrijf maakt zelf iets in massief hout waar rubberwood in past: trappen, meubels, keukens, kasten, werkbladen, tafels.
- "nee": het bedrijf maakt zelf niets in massief hout, bijvoorbeeld een plaatser van PVC- of aluminium ramen, een meubelwinkel of een handelaar.
- "onzeker": de tekst geeft te weinig informatie om te kiezen.

Stap 2: haal de contactgegevens uit de tekst:
bedrijfsnaam, email, telefoon, adres, gemeente, btw, website.

Regels:
- Neem alleen over wat letterlijk in de tekst staat. Verzin niets.
- Staat een veld niet in de tekst, vul dan "onbekend" in.
- Raad nooit een e-mailadres, ook niet info@ of contact@.
- Staat er geen e-mailadres in de tekst, zet dan "lead" op "geen e-mail".
- "lead" is "ja" alleen als doelgroep "ja" is en er een e-mailadres in de tekst staat. Anders "nee" of "geen e-mail".
- Geef in "reden" één korte zin: waarom deze doelgroep.

Formaat:
{"doelgroep": "ja|nee|onzeker", "lead": "ja|nee|geen e-mail", "bedrijfsnaam": "...", "email": "...", "telefoon": "...", "adres": "...", "gemeente": "...", "btw": "...", "website": "...", "reden": "..."}

WEBSITE
URL: [plak de link]
Tekst: [plak de tekst van de home- en contactpagina]
```
