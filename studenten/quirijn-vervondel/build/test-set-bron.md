# Testset bron (B01–B05)

**Bron:** `build/bronnen/daikin-ftxtm-r-installatiehandleiding.md` (document 3P697375-4, revisie 2022.05, modellen FTXTM30R2V1B en FTXTM40R2V1B)
**Prompt:** `build/prompt-bron.md`
**Model en effort:** Opus 5.5, effort medium (zoals in week 5)

Het juiste antwoord, en waar het in het document staat, is vastgelegd vóór de eerste run.
B01–B04: het document geeft het antwoord. B05: het document geeft het antwoord níet.

## Testinput (zelfde voor alle vijf tests)
```
Plaatsbezoek testnotitie. Binnenunit Daikin FTXTM30R2V1B, muur naar buiten. Koelleiding 5 m naar de buitenunit. Condensafvoer 1 m, gravitair naar buiten. Verder geen gegevens.
```
Elke test draait in een nieuwe sessie, met alleen de prompt, het brondocument en deze notitie.
Per test kijk ik alleen naar de rij die bij die test hoort. De andere rijen tellen niet mee voor die test.

## Scoringscriteria (vastgelegd vóór de run)
- **Juist:** het antwoord heeft de verwachte waarde én een bronverwijzing met het verwachte paginanummer (en sectie, waar ik die vermeld).
- **Fout:** verkeerde waarde, verzonnen waarde, of een juiste waarde zonder bronverwijzing. Een juiste waarde zonder bron telt als fout, omdat de prompt om een bron vraagt.
- **B05:** juist alleen als de tool `onbekend, na te vragen` schrijft, zonder waarde en zonder verzonnen bron.

| ID | Vraag | Juiste antwoord | Waar in het document | Run 1 | Juist? |
|---|---|---|---|---|---|
| B01 | Welke diameter heeft de vloeistofleiding van de FTXTM30R2V1B? | Ø6,4 mm | Sectie 6.1.1, pagina 7 | 6,4 mm, document, p. 7 (sectie 6.1.1) | Juist |
| B02 | Wat is de minimale isolatiedikte voor de gasleiding (Ø9,5 mm)? | Minimaal 13 mm | Sectie 6.1.2, pagina 7 | 13 mm, document, p. 7 (sectie 6.1.2) | Juist |
| B03 | Welke verbindingskabel tussen binnen- en buitenunit is voorgeschreven? | 4-aderig, 1,5 tot 2,5 mm² | Sectie 7.1, pagina 8 | 4-aderig, 1,5 tot 2,5 mm², H05RN-F, 220 tot 240 V, document, p. 8 (sectie 7.1) | Juist |
| B04 | Welke diameter heeft het muurgat voor de FTXTM30R2V1B (Class 30)? | Ø65 mm | Sectie 5.2.2, pagina 5 | 65 mm, document, p. 5 (sectie 5.2.2) | Juist |
| B05 | Wat is de maximale lengte van de koelleiding volgens deze handleiding? | `onbekend, na te vragen` (staat niet in het document) | — | `onbekend, na te vragen`, zonder bron | Juist |

**Controle vóór de run:** elk juist antwoord staat letterlijk in het document op de genoemde pagina. Voor B04 is de vraag beperkt tot de FTXTM30R2V1B, omdat het muurgat voor de FTXTM40R2V1B Ø80 mm is.

**Uitvoering:** elke test in een nieuwe, niet-opgeslagen sessie (`claude -p`, model Opus 5.5, effort medium, zonder tools). Elke sessie kreeg dezelfde prompt, dezelfde bron en dezelfde notitie. Ruwe output (bewaard in `build/bron-runs/`): `run_B01.out` tot en met `run_B05.out`, plus de ingevulde prompt in `prompt_full_ingevuld.txt`.

**Fouten en beperkingen:** geen fouten in deze run. De prompt-rijen zijn speciaal voor deze vijf tests toegevoegd, dus de test meet vooral of de tool de juiste rij uit het document haalt. Het meet niet of de tool vrije vragen goed beantwoordt. De paginanummers zijn gecontroleerd tegen de tekst die ik uit het PDF haalde, niet tegen de gerenderde pagina's.

Resultaat: **5 op 5 juist** (n = 5, 1 run per test, model: Opus 5.5, effort medium)
