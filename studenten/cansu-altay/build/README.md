# Trainingsnotities omzetten naar een overzicht

Korte notities na een oefening omzetten naar oefening, gewicht, sets en herhalingen. Zo kan Cansu later haar laatst gebruikte gewicht terugvinden. Ontbrekende of onduidelijke gegevens krijgen `onbekend`.

## Status

De taak is gekozen op 7 oktober 2026. De huidige prompt v3 is getest op tien echte trainingsnotities, elk tweemaal: **17 van 20 runs correct (85%)** volgens inhoud en afgesproken uitvoer. Eén run heeft F4 (verkeerde uitvoervorm), twee runs F3 (gemiste informatie). Bij input 8 is F6 waargenomen: wisselende naleving van de uitvoerregel.

De testset is klein en input 6 is dubbelzinnig. Uitvoerafspraken zijn tussen versies gewijzigd; scores zijn geen zuivere vergelijking onder dezelfde regels. Cansu rapporteert het gebruikte model/de instelling in ChatGPT als `GPT 5.6 terra hoog` (letterlijk overgenomen; geen technische model-ID vastgesteld). Automatisch opslaan en het laatste gewicht opzoeken zijn nog niet gebouwd.

## Bestanden

- `promptaudit.md`: annotaties per regel van v4 op basis van de gezamenlijke bespreking; door Cansu nagelezen en goedgekeurd op 8 oktober.

- `taak.md`: de goedgekeurde taak en de reden voor de overstap.
- `prompt.md`: v4; bevat drie door Cansu aangeleverde voorbeelden en haar regel met een waarom. Inputs 8 en 9 elk tweemaal correct hertest (4/4).
- `prompt-v3.md`: geteste v3, bewaard vóór het toevoegen van voorbeelden.
- `prompt-v2.md`: prompt met de failure-regel, vóór de wijziging voor spelfouten.
- `prompt-v1.md`: oorspronkelijke prompt, bewaard voor vergelijking met eerdere tests.
- `test-set.md`: tien echte inputs, vooraf vastgelegde antwoorden en de testresultaten.
- `log.md`: de geschiedenis van keuzes, tests en wijzigingen.
- `archief/horecareviews/`: de bestanden van de eerdere Build, bewaard als geschiedenis.

## De huidige versie gebruiken

1. Lees `prompt.md` en controleer de instructies zelf.
2. Kopieer de volledige prompt naar een nieuw tijdelijk gesprek in ChatGPT of een incognitogesprek in Claude. Gebruik geen web search.
3. Vervang de invultekst tussen `<notitie>` en `</notitie>` door één eigen trainingsnotitie.
4. Het model geeft een tabel terug. Vergelijk die met het juiste antwoord dat je zelf vooraf hebt vastgelegd.

Gebruik voor elke test een nieuw gesprek. Geef het model de juiste antwoorden en de volledige testset niet mee.

## Volgende stap

De gerichte hertest van 8 oktober is afgerond: v3 met alleen voorbeelden gaf 4/4 correcte antwoorden op inputs 8 en 9, elk tweemaal getest; oorspronkelijke v3 gaf 1/4 correct op dezelfde selectie. Alleen bouwsteen voorbeelden is gewijzigd en de verwachte antwoorden zijn gelijk gebleven. Dit is een kleine geselecteerde hertest, geen score op de volledige testset. Eerdere versies en resultaten blijven bewaard. Post bijwerken; schriftelijke promptannotaties en buurtest blijven open.

Op 8 oktober is een aparte versie `prompt-v3-met-voorbeelden.md` voorbereid: exact v3 plus alleen de drie voorbeelden. De waarom-zin van v4 is niet toegevoegd. Test inputs 9 en 8 elk tweemaal met deze versie en hetzelfde model; verwachte antwoorden blijven gelijk aan v3. Nog niet getest. V4 en eerdere resultaten blijven bewaard.

De hertests van inputs 8 en 9 zijn afgerond: v3 gaf 1/4 correcte runs op deze selectie, v4 4/4, met identieke antwoorden per input. Verwachte antwoorden zijn gelijk gebleven. V4 is niet op de volledige testset getest; de volledige v3-score blijft 17/20 (85%). Voorbeelden en waarom-zin zijn tegelijk toegevoegd, dus hun afzonderlijke effect is niet vastgesteld. Buurtest niet uitgevoerd omdat Cansu niet meer in de les was; die blijft open. Volgende stap: de week-3-post in Cansu's eigen woorden uitwerken en de nog ontbrekende schriftelijke annotaties per promptregel vastleggen.

V4 bevat nu alle zes bouwstenen, drie voorbeelden en een door Cansu geschreven waarom-zin. De buurtest en schriftelijke annotaties per promptregel zijn nog niet vastgelegd. Laat een klasgenoot alleen de prompt lezen en drie inputs beantwoorden zonder de verwachte antwoorden te zien. Noteer de verschillen. Test daarna de foute inputs opnieuw met de aangepaste context. Input 7 is een voorbeeld in v4; houd tests ervan apart van ongeziene inputs. De stand hieronder betreft v3.

Controleer de prompt met de zes bouwstenen van week 3. Bespreek daarna een gerichte verbetering voor het weglaten van failure, schrijf de reden vooraf op en test opnieuw met dezelfde inputs en beoordelingsregels.

## Versiegeschiedenis

- V1: letterlijke oefennamen, ontbrekende gegevens als onbekend. Inputs 1–6 elk tweemaal getest: 10/12 correct; input 6 dubbelzinnig.
- V2: failure behouden als tot failure (aantal onbekend). Inputs 1–5 en variant 6b elk tweemaal correct (12/12). Oorspronkelijke input 6 eenmaal getest, met een afwijking in de oefennaam; tweede run niet uitgevoerd.
- V3: duidelijke spelfouten in oefennamen verbeteren. Inputs 1–10 elk tweemaal getest: 17/20 correct (85%). Negen van tien inputs gaven identieke antwoorden; acht van tien waren in beide runs correct. Variant 6b niet getest met v3.

Alle eerdere runs en wijzigingen blijven bewaard in log.md en test-set.md.
