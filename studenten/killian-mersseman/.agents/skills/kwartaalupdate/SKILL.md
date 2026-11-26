---
name: kwartaalupdate
description: Werk één bedrijf bij met het nieuwste officiële kwartaalrapport in de bestaande Excel-werkmap voor kwartaalopvolging en controleer of de cijfers zichtbaar zijn in de grafieken.
---

# Kwartaalupdate

1. Bepaal welk bedrijf aan de beurt is op basis van de vraag en de bestaande opvolging. Vraag om de ticker als de keuze onduidelijk blijft.
2. Zoek en download het nieuwste officiële kwartaalrapport via Investor Relations of de toezichthouder. Controleer de verslagperiode en publicatiedatum. Bewaar de bronlinks en bronpagina’s. Bundel meerdere bronbestanden voor hetzelfde bedrijf in één PDF met de oorspronkelijke pagina’s en herkenbare brononderdelen.
3. Lees `build/prompt-v3-enkel-bedrijf.md` en `build/excel/README.md` vanuit de studentenmap. Gebruik de bestaande definities voor de drie maatstaven en schrijf een JSON-run zoals in `build/excel/runs/`. Leg ontbrekende waarden, afleidingen en werkelijke verslagdatums vast. Vul `report_quarter` (Q1–Q4) en `fiscal_year` in volgens het officiële rapport. Houd de werkmap gesloten tijdens de import met `node build/excel/werk-bij.mjs build/excel/runs/<run>.json`. Registreer bronbevestiging nadat de gebruiker de cijfers heeft gecontroleerd.
4. Controleer in `outputs/kwartaalopvolging/kwartaalopvolging.xlsx` per maatstaf de ticker, periode, waarde en bron op het blad **Historiek**. Controleer op **Grafieken** de gekoppelde reeksen voor het kalenderjaar van de einddatum, het gerapporteerde kwartaal en het FCF-periodetype. Vergelijk de weergegeven waarden met Historiek, inclusief de USD-omrekening waar van toepassing. Meld welke cijfers ontbreken of buiten de gekozen selectie vallen. De update is volledig geslaagd als alle gevraagde cijfers in Excel staan en zichtbaar zijn in de grafieken.
5. Geef het bedrijf, de verslagperiode, de publicatiedatum, de bronlink, het werkmapbestand en de benodigde grafiekfilters. Vermeld welke controles gelukt zijn.
