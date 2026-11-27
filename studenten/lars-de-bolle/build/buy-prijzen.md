# Buy: wat kan Joeri kopen?

Voor de Buy-rij van week 7. Drie sub-agents van Claude Code zochten op 25
november 2026 elk één programma, op de eigen site van de leverancier. Zelf
nagekeken op dezelfde pagina's: de prijzen, bij Vertuoza ook de AI-functie,
export, API en MCP, en de MCP-pagina van Robaws. De rest komt van de
sub-agents. Geen van de drie pagina's zegt of de prijs excl. of
incl. btw is.

| | Robaws | Trustup Pro | Vertuoza |
|---|---|---|---|
| Wat | Cloud-ERP voor aannemers: offertes, facturen, calculatie, projecten | Offertes, facturen, werkenbibliotheek en werfopvolging voor vakmensen | Bouwsoftware: offertes, facturen, planning, werfopvolging |
| Offerte uit spraak of met AI? | Niet gevonden | Niet gevonden. Alleen OCR voor aankoopfacturen | **Ja**: "Mondelinge offertes met AI", in alle vier de pakketten |
| Plan voor Joeri | Starter, 1 gebruiker | Essential, 1 gebruiker, onbeperkt offertes | Niet publiek |
| Prijs per maand | 29 euro bij jaarbetaling, 39 euro maandelijks | 39 euro bij jaarbetaling, 49 euro maandelijks | "Neem contact met ons op" |
| Per jaar, bij jaarbetaling | 348 euro | 468 euro | onbekend |
| Datum van de prijs | Geen datum op de pagina. Gelezen op 25 november 2026 | Pagina "Tarieven 2026", gewijzigd 18 februari 2026. Gelezen op 25 november 2026 | Gelezen op 25 november 2026 |
| Wat zit er vast? | Exporteren moet vóór het einde van het contract, daarna nog 30 dagen tegen betaling. Bij jaarbetaling loopt het contract tot het einde van het jaar. Excel-export van overzichten, onder meer offertes. API pas vanaf Go (59 euro) | Alleen "boekhoudkundige export" gevonden. Export van offertes, klanten of werkenbibliotheek: niet gevonden. API "binnenkort", alleen in Business | Lijst van offertes exporteren, formaat niet vermeld. Open API en MCP: optie, inbegrepen in Expert+ |
| Koppelen aan een AI (MCP) | Gratis voor klanten. Leest offertes, projecten, werkbonnen en facturen; met schrijfrechten kan het ook dingen aanpassen. Of het een offerte kan aanmaken, staat er niet | Niet gevonden | Optie, inbegrepen in Expert+ |
| Bron | robaws.com/en/pricing, algemene voorwaarden | pro.trustup.be/nl/prijzen | vertuoza.com/nl-be/onze-packs |

Trustup Starter is gratis, maar tot 30 offertes en facturen per jaar. Joeri maakt
96 offertes per jaar (`waarde.md`), dus dat volstaat niet.

Ook gezien, niet nagekeken: Voice to Quote (voicetoquote.ai), Engelstalig, 49,99
dollar per maand plus 149 dollar opstart.

## Wat opviel bij het zoeken

De prijs van Robaws staat niet in de tekst van de pagina, alleen in de HTML
(`data-price-*`). Een sub-agent vond via een vergelijkingssite "niet publiek, op
aanvraag"; een andere vond de bedragen pas in de HTML. Dat is criterium 2 uit
`geo-audit.md`: geen bedrag dat een AI kan lezen.

Trustup toont de jaarprijs pas na een schakelaar, en een gewone download van de
pagina botst op Cloudflare.
