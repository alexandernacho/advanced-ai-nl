# Testset v3 — extractie van één bedrijf

## Opzet

Deze reeks test de extractie van `prompt-v3-enkel-bedrijf.md`, niet de Excel-update. De bestaande Excel en productieruns worden niet gewijzigd. De runner moet een afzonderlijke extractievariant vastleggen: dezelfde financiële regels, rapporttekst als input en controletabel plus JSON als antwoord; geen bestanden schrijven, Excel openen of koersen ophalen. Dit is een afgebakende variant, geen volledige validatie van v3.

Verwachtingen worden vóór nieuwe runs door de student bevestigd. Historische extracties zijn geen nieuwe testresultaten. Verwachte antwoorden worden nooit aan het geteste model meegegeven. Elke herhaling krijgt dezelfde bron en instructies in een onafhankelijke sessie. Model en effort moeten bij de runs worden vastgelegd.

## V3-T01 — Novo Nordisk, Q2 2026

Bevestigd door de student op 22 oktober 2026, vóór nieuwe runs.

Input: ticker NVO; `build/rapporten/NVO/NVO-2026-06-30.pdf`.

| Controlepunt | Bevestigde verwachting |
|---|---|
| FCF | 42.524 miljoen DKK, Q2 2026 |
| Schuld | 140.127 miljoen DKK op 30 juni 2026, inclusief leases; afbakening Onzeker |
| Omzetgroei | 2% gerapporteerd; circa 2,1% berekend, apart vermeld |

Bevestigde beoordelingsregel: een run slaagt als cijfers, perioden, valuta en schuldbeperking correct zijn. Andere v3-eisen kunnen afzonderlijk worden genoteerd, maar worden niet achteraf aan deze succesregel toegevoegd.

## V3-T02 — Eli Lilly, Q2 2026

Bevestigd door de student op 22 oktober 2026, vóór nieuwe runs.

Input: ticker LLY; `build/rapporten/LLY/LLY-2026-06-30.pdf`.

| Controlepunt | Bevestigde verwachting |
|---|---|
| FCF | 10.764 miljoen USD, eerste halfjaar 2026, na periodekeuze door de student |
| Schuld | 54.908 miljoen USD op 30 juni 2026; Onzeker wegens ontbrekende lease-uitsplitsing |
| Omzetgroei | 48% gerapporteerd; circa 47,7% berekend, apart vermeld |

Bevestigde beoordelingsregel: cijfers, perioden, valuta en schuldbeperking moeten correct zijn. De FCF-uitkomst geldt na de vooraf bevestigde keuze voor het eerste halfjaar 2026. De verwachte waarde wordt niet aan het geteste model meegegeven.

## V3-T03 — Amazon, Q2 2026

De student bevestigt op 22 oktober 2026 dat de voorgelegde cijfers kloppen, na de expliciete vraag naar eigen broncontrole. Vastgelegd vóór nieuwe runs.

Input: ticker AMZN; `build/rapporten/AMZN/AMZN-2026-06-30.pdf`.

| Controlepunt | Bevestigde verwachting |
|---|---|
| FCF | −8.821 miljoen USD, Q2 2026 |
| Schuld | Circa 155.315 miljoen USD op 30 juni 2026, inclusief financiële leases en financieringsverplichtingen, exclusief operationele leases |
| Omzetgroei | 20% gerapporteerd; circa 19,6% berekend, apart vermeld |

De schuld is een benadering doordat de langlopende financieringsverplichtingen in de bron afgerond zijn. De beoordelingsregel blijft: cijfers, perioden, valuta en schuldbeperking moeten correct zijn. De bevestiging van deze drie controlepunten valideert niet automatisch alle aanvullende claims in de oude extractie.

## V3-T04 — Netflix, Q3 2026

De student bevestigt op 22 oktober 2026 de voorgelegde cijfers en beperking met “klopt”, vóór nieuwe runs.

Input: ticker NFLX; `build/rapporten/NFLX/2026-Q3/NFLX-2026-09-30-aandeelhoudersbrief.pdf`. Officiële aandeelhoudersbrief met financiële bijlagen, gepubliceerd op 20 oktober 2026; geen Form 10-Q.

| Controlepunt | Bevestigde verwachting | Bronpagina |
|---|---|---|
| FCF | 2.883,513 miljoen USD, Q3 (1 juli t/m 30 september 2026), gerapporteerd; operationele kasstroom 3.162,279 minus investeringen 278,766 miljoen USD | 11, Non-GAAP Free Cash Flow |
| Schuld | 15.132,394 miljoen USD op 30 september 2026; kortlopend 2.474,796 plus langlopend 12.657,598 miljoen USD | 9, Consolidated Balance Sheets |
| Omzetgroei | 11,8% gerapporteerd in de overzichtstabel; controleberekening circa 11,8491%, afgerond 11,8%; omzet 12.874,176 tegenover 11.510,307 miljoen USD | 1, overzichtstabel; 8, Consolidated Statements of Operations |

Schuldbeperking: de som betreft de twee balansposten. Een afzonderlijke lease-uitsplitsing ontbreekt in deze brief; volledigheid van de schuldafbakening blijft onzeker. De oorspronkelijke financiële tabellen staan in duizenden USD; bovenstaande bedragen zijn omgerekend naar miljoenen USD.

De beoordelingsregel blijft: cijfers, perioden, valuta en schuldbeperking moeten correct zijn. Deze bevestiging valideert niet automatisch andere bronclaims of de volledige v3-workflow.

## V3-T05 — Uber, Q2 2026

De student bevestigt op 22 oktober 2026 de voorgelegde verwachtingen met “klopt”, vóór nieuwe runs.

Input: ticker UBER; `build/rapporten/UBER/UBER-2026-06-30.pdf`, gekopieerd van het bestaande lokale bestand `Documents/Sem 1 2026/AI/uber-20260630.pdf`.

| Controlepunt | Bevestigde verwachting |
|---|---|
| FCF | 5.078 miljoen USD, januari–juni 2026, na periodekeuze door de student |
| Schuld | 12.723 miljoen USD op 30 juni 2026, inclusief 0%-obligaties; afbakening Onzeker doordat de afzonderlijke financiële leases niet volledig zijn vastgesteld |
| Omzetgroei | 12% gerapporteerd; circa 12,2% berekend, apart vermeld |

De beoordelingsregel blijft: cijfers, perioden, valuta en schuldbeperking moeten correct zijn. De verwachte FCF geldt na de vooraf bevestigde keuze voor januari–juni 2026. De verwachte waarde wordt niet aan het geteste model meegegeven. De eerdere bronpaginaverwijzingen moeten nog bij dit lokale bestand worden gecontroleerd; verwijzingen uit historische runs niet zonder controle overnemen.

Aantal vooraf bevestigde inputs: n = 5. Op 22 oktober 2026 zijn drie onafhankelijke herhalingen per input uitgevoerd: vijftien antwoorden. Resultaat en condities staan in `build/foutmarge.md`; de verwachte antwoorden hierboven zijn niet aangepast. De agent beoordeelt 15/15 antwoorden als geslaagd binnen de bevestigde scope. De student heeft Netflix T04 Run 1 en Amazon T03 Run 3 op 22 oktober 2026 gecontroleerd en goedgekeurd. De steekproef van twee antwoorden is afgerond; de overige dertien antwoorden zijn alleen door de agent beoordeeld.
