# Taak — Leads voor DBA Hardwoods

- **De taak:** uit de website van één bedrijf beslissen of het een mogelijke klant is voor DBA Hardwoods (focus: rubberwood), dus of het zelf iets maakt in massief hout, en de contactgegevens eruit halen.
- **Wat erin gaat:** de tekst van de homepage (waar de contactgegevens meestal onderaan staan) van een bedrijf dat ik op Google Maps vond.
- **Wat eruit komt:** `doelgroep`: `ja` / `nee` / `onzeker`. Bij `ja`: bedrijfsnaam, e-mail, telefoon, adres, gemeente, btw-nummer, website.
- **De uitweg:** geen e-mailadres op de site → `geen e-mail`, en dan is het geen lead. Een veld dat niet op de site staat → `onbekend`. Nooit raden.
- **Soort AI:** een taalmodel. Tekst in, vaste velden uit. Een vaste regel kan niet beslissen of "maatwerk in eik" een trappenmaker is.
- **Checken:** per veld nakijken of het letterlijk op de site staat. Een e-mailadres dat er niet staat, is verzonnen (F2).

## Vijf testinputs (ideeën)

1. Een trappenmaker met een duidelijk e-mailadres op de contactpagina.
2. Een schrijnwerker met alleen een contactformulier, geen e-mailadres.
3. Een bedrijf dat geen doelgroep is, bijvoorbeeld een meubelwinkel of een aannemer die alleen renoveert.
4. Een Franstalige website van een menuisier of fabricant d'escaliers.
5. Een twijfelgeval: een bedrijf dat "interieurmaatwerk" doet, zonder trappen te vermelden.
