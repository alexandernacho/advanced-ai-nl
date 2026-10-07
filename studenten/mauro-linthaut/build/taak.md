# Taak — velden uit een kwartaalpersbericht halen

## De vijf regels

1. **De taak:** uit het persbericht met de kwartaalresultaten (*earnings release*) van een beursgenoteerd bedrijf vijf vaste velden halen, met de bron erbij.
2. **Wat erin gaat:** één persbericht van één bedrijf voor één kwartaal, als tekst. De tool analyseert steeds één bedrijf. De testset bestaat uit meerdere bedrijven.
3. **Wat eruit komt:** vijf velden, elk met getal, eenheid, periode en de zin uit het persbericht waar het vandaan komt:
   - omzet
   - nettowinst
   - vrije kasstroom (*free cash flow*)
   - totale schulden
   - rentelasten op die schulden

   **Uitweg:** staat een veld er niet in, dan zegt de tool "niet vermeld". Hij rekent niets uit en gokt niet.
4. **De soort AI:** een taalmodel, want het is tekst in en gestructureerde velden uit. Ticker invoeren, vergelijken met vorig kwartaal, grafieken, waarderatio's (P/E, PEG, forward) en vergelijken met concurrenten zijn geen AI. Dat is rekenen en tekenen op de uitvoer, en komt later.
5. **Hoe check je of een antwoord juist is:** ik lees het getal zelf in het persbericht en schrijf het juiste antwoord op vóór de tool draait.

## Later (buiten deze Build)
- De ticker als voordeur: ticker in, persbericht vinden en downloaden.
- Vergelijken met vorig kwartaal, cirkeldiagrammen en grafieken.
- Waarderatio's en vergelijken met concurrenten.
- Tekstvelden zoals grote partners, partners in onderhandeling en toekomstverwachtingen. Moeilijker te meten, en een taalmodel kan hier verzinnen.

## Nog te beslissen
- **Nettowinst:** de echte, of de aangepaste (zonder eenmalige posten)? Een regel in de prompt moet het zeggen.
- **Testset:** vijf bedrijven met elk twee kwartalen (A), of één bedrijf met tien kwartalen (C)? Bij C geldt het cijfer maar voor dat ene bedrijf, en dat moet in de post staan.
- **Backlog** (getekende bestellingen die nog geen omzet zijn) is niet opgenomen, want "wat ze over hebben na de kosten" bleek nettowinst en vrije kasstroom te zijn. Wil ik backlog er toch bij?

## Vijf inputideeën
(in te vullen door mezelf, met echte persberichten)

1.
2.
3.
4.
5.

Het juiste antwoord bij elke input schrijf ik zelf, later, in `build/test-set.md`.
