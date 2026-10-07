# Taak — velden uit een kwartaalpersbericht halen

## De vijf regels

1. **De taak:** uit het persbericht met de kwartaalresultaten (*earnings release*) van een Amerikaans beursgenoteerd bedrijf vijf vaste velden halen, met de bron erbij. Het persbericht staat bij de SEC op EDGAR, als bijlage (Exhibit 99.1) bij een 8-K.
2. **Wat erin gaat:** één persbericht van één bedrijf voor één kwartaal, als tekst. De tool analyseert steeds één bedrijf. De testset bestaat uit vijf bedrijven, elk met twee kwartalen: tien inputs.
3. **Wat eruit komt:** vijf velden, elk met getal, eenheid, periode en de zin uit het persbericht waar het vandaan komt:
   - omzet
   - nettowinst (de echte, niet de aangepaste)
   - vrije kasstroom (*free cash flow*)
   - totale schulden
   - rentelasten op die schulden

   **Uitweg:** staat een veld er niet in, dan zegt de tool "niet vermeld". Hij rekent niets uit en gokt niet.
4. **De soort AI:** een taalmodel, want het is tekst in en gestructureerde velden uit. Ticker invoeren, vergelijken met vorig kwartaal, grafieken, waarderatio's (P/E, PEG, forward) en vergelijken met concurrenten zijn geen AI. Dat is rekenen en tekenen op de uitvoer, en komt later.
5. **Hoe check je of een antwoord juist is:** ik lees het getal zelf in het persbericht en schrijf het juiste antwoord op vóór de tool draait.

## Einddoel
Een ticker invullen en automatisch een analyse krijgen van het bedrijf. De Build is stap 1; elke stap bouwt op de vorige, want als stap 1 niet klopt, zijn de grafieken en ratio's van stap 2 fout.

| Stap | Wat | Meetbaar? |
|---|---|---|
| 1 | De vijf velden uit een persbericht halen (**deze Build**) | Ja |
| 2 | Vergelijken met vorig kwartaal, grafieken, waarderatio's (P/E, PEG, forward) | Rekenwerk op de uitvoer van stap 1 |
| 3 | Ticker invoeren: het laatste persbericht automatisch vinden en downloaden | Ja, bron vinden of niet |
| 4 | Meerdere bedrijven naast elkaar, concurrenten | Hangt af van stap 1 tot 3 |

Beperkingen die ik erbij zeg:
- Ik focus voor dit eindwerk op Amerikaanse bedrijven (US GAAP, dollar, Engels), want daar bestaat een centrale bron (SEC, EDGAR). Voor Europese bedrijven niet, dus die komen later.
- Mijn cijfer geldt voor Amerikaanse bedrijven en voor de bedrijven die ik getest heb, niet voor elk bedrijf.
- Door de focus op de VS valt variatie in valuta en taal weg. Mijn lastige inputs zoek ik in sector, grootte, opmaak van het persbericht, en in een veld dat niet genoemd wordt.
- De velden zijn meetbaar, een mening over de koers niet. De tool geeft materiaal, ik beslis zelf.

## Later (buiten deze Build)
- Europese bedrijven (IFRS, euro, geen centrale bron).
- Tekstvelden zoals grote partners, partners in onderhandeling en toekomstverwachtingen. Moeilijker te meten, en een taalmodel kan hier verzinnen.

## Gekozen
- **Nettowinst:** de echte (GAAP), niet de aangepaste (non-GAAP). Een regel in de prompt moet dat zeggen, met een waarom.
- **Testset:** vijf bedrijven met elk twee kwartalen.
- **Backlog** (getekende bestellingen die nog geen omzet zijn) laat ik weg. Later toevoegen kan.

## Vijf inputideeën
Vijf Amerikaanse bedrijven, elk met de twee meest recent gepubliceerde kwartalen: Q2 2026 en Q1 2026 (het derde kwartaal is nog niet gepubliceerd). Ik controleer op EDGAR of alle tien persberichten bestaan. De link naar elk persbericht vul ik zelf in.

1. Alphabet (Google) — Q1 2026, Q2 2026
2. Palantir — Q1 2026, Q2 2026
3. Amazon — Q1 2026, Q2 2026
4. JPMorgan Chase (bank) — Q1 2026, Q2 2026
5. Vistra (energie) — Q1 2026, Q2 2026

Het juiste antwoord bij elke input schrijf ik zelf, later, in `build/test-set.md`.
