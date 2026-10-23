# Foutmarge — 22 oktober 2026

## Resultaat

Model: **GPT-6.1 Sol**, effort **low** (expliciet aangevraagd bij iedere run). **n = 5 verschillende inputs**, **3 onafhankelijke herhalingen per input**, dus **15 antwoorden**. Eén huidige extractievariant van v3; geen vergelijking met een vorige versie.

Beoordelaar: de agent, tegenover de vooraf door de student bevestigde verwachtingen in `test-set-v3.md`. De student heeft Netflix Run 1 en Amazon Run 3 gecontroleerd en goedgekeurd; de steekproef van twee antwoorden is afgerond. De verwachte antwoorden zijn niet aangepast en niet meegegeven aan het geteste model.

| Versie | Run 1 | Run 2 | Run 3 | Waargenomen bereik (min–max) |
|---|---:|---:|---:|---:|
| v3, extractievariant | 5/5 | 5/5 | 5/5 | **5–5/5 (100–100%)** |

Een runnummer in deze tabel bundelt de gelijkgenummerde onafhankelijke antwoorden op alle vijf inputs. **15/15 antwoorden voldoen volgens de agent aan de bevestigde beoordelingsregel:** juiste cijfers, perioden, valuta en schuldbeperking. Er is geen variatie in deze totaalscore waargenomen. Dit min–max-bereik is geen statistisch betrouwbaarheidsinterval en bewijst geen foutloze werking buiten deze vijf gevallen.

## Beoordeling per input

Alle geldbedragen hieronder zijn miljoenen in de vermelde valuta. De omzetgroei is het gerapporteerde hoofdpercentage; de eigen controleberekening staat afzonderlijk in elk antwoord.

| Input | Bevestigde controlepunten, teruggevonden in alle drie antwoorden | Run 1 | Run 2 | Run 3 |
|---|---|---|---|---|
| T01 NVO | FCF 42.524 DKK, Q2 2026; schuld 140.127 DKK op 30 juni, inclusief leases en Onzeker; omzetgroei 2%, controle circa 2,1% | Geslaagd | Geslaagd | Geslaagd |
| T02 LLY | FCF 10.764 USD, H1 2026; schuld 54.908 USD op 30 juni, Onzeker wegens ontbrekende leasegegevens; omzetgroei 48%, controle circa 47,7% | Geslaagd | Geslaagd | Geslaagd |
| T03 AMZN | FCF −8.821 USD, Q2 2026; schuld circa 155.315 USD op 30 juni, inclusief financiële leases/financieringsverplichtingen, exclusief operationele leases, afronding benoemd; omzetgroei 20%, controle circa 19,6% | Geslaagd | Geslaagd | Geslaagd |
| T04 NFLX | FCF 2.883,513 USD, Q3 2026; schuld 15.132,394 USD op 30 september, leaseafbakening onzeker; omzetgroei 11,8%, controle circa 11,8491% | Geslaagd | Geslaagd | Geslaagd |
| T05 UBER | FCF 5.078 USD, H1 2026; schuld 12.723 USD op 30 juni, inclusief 0%-obligaties, financiële leases onvolledig vastgesteld en Onzeker; omzetgroei 12%, controle circa 12,2% | Geslaagd | Geslaagd | Geslaagd |

Deze score beoordeelt de vastgelegde controlepunten, niet automatisch elke aanvullende bronclaim of bronpaginaverwijzing. De verschillende FCF-perioden zijn per bedrijf vooraf vastgelegd en niet als gelijksoortige kwartaalbedragen behandeld.

## Wat wel wisselt

- Amazon-schuld: Run 1 en Run 2 gebruiken `Onzeker`; Run 3 `Nog te controleren`. Alle drie geven dezelfde componenten, hetzelfde benaderende totaal en de beperking door het afgeronde langlopende financieringsbedrag. De vooraf bevestigde Amazon-regel schrijft geen verplicht statuslabel voor. Daarom geen afkeuring achteraf; wel wisselend labelgedrag, relevant voor verder onderzoek naar F6.
- Amazon-omzetgroei: de eerste twee antwoorden beschrijven berekend minus gerapporteerd (circa −0,3795 procentpunt), de derde gerapporteerd minus berekend (+0,3795). De richting is expliciet benoemd; dit is geen numerieke tegenstelling.
- Toelichtingen verschillen in formulering en detail. Er is op de beoordeelde hoofdwaarden, perioden en valuta geen verschil gevonden.

## Claim

**Geen verbeterclaim getoetst.** De student koos voor de huidige één-bedrijf-v3, die een andere taak heeft dan de oudere twee-bedrijven-v2. Daarom is geen oude versie op deze testopzet gedraaid. Een claim dat v3 beter is, kan op basis van deze reeks niet worden bevestigd of ingetrokken. De eerdere gemengde telling 15/20 uit week 4 is geen vergelijkbare baseline.

## Vastgelegde testcondities en grenzen

1. Financiële regels van v3 zijn vastgelegd als `runs-week05-v3/prompt-extractie.md`. De oorspronkelijke prompt is ongewijzigd gebleven; hashes staan in `manifest.json`.
2. Het model krijgt de volledige vooraf geëxtraheerde PDF-tekst met paginamarkeringen. Dit test een tekstpipeline, geen visuele PDF-inspectie of volledige agentworkflow. pypdf-waarschuwingen over PDF-objectverwijzingen zijn tijdens de voorbereiding zichtbaar geworden; Amazon-pagina 192 leverde geen tekst. Die paginamarkering blijft aanwezig. Niet vastgesteld of daar visuele inhoud staat; dus geen garantie dat alle visuele broninhoud in de modelinput zit.
3. Voor Lilly en Uber is de door de student bevestigde halfjaarperiode vooraf meegegeven, zonder financiële antwoorden. Het vragen en afwachten van een keuze is niet getest.
4. Elke sessie startte in een lege tijdelijke map, met gebruikersconfiguratie en projectinstructies uitgeschakeld, read-only-sandbox en expliciet uitgeschakelde shell, web, apps, plugins, hooks, geheugen en delegatie. **De logs van alle vijftien voltooide runs bevatten nul toolacties.** De extra optie `tools.disable_defaults=true` werd door deze CLI niet herkend en genegeerd; dit is in de ruwe logs bewaard. De andere beperkingen en het ontbreken van geregistreerde toolacties zijn de feitelijke basis voor de controle, niet die genegeerde optie.
5. De eerste opstartpoging werd door de buitenste sandbox geblokkeerd, vóór een modelantwoord. Bewaard als `T01-run1-startfout.*`; niet als inhoudelijke run geteld. Daarna zijn precies vijftien voltooide antwoorden verzameld, zonder inhoudelijke herselectie of retries.
6. Dezelfde inputhash is gebruikt voor de drie herhalingen per bedrijf. De runner leest de testset met verwachtingen niet.
7. Excel, bestaande productie-JSON en financiële bronbestanden zijn niet door de testruns bijgewerkt. Er zijn geen koersen opgehaald.

## Bewijsbestanden en tokenverbruik

- `runs-week05-v3/T01-input.txt` t/m `T05-input.txt`: exacte modelinputs, zonder verwachte antwoorden.
- `runs-week05-v3/T01-run1.txt` t/m `T05-run3.txt`: vijftien volledige antwoorden.
- `*.events.jsonl`: sessiegebeurtenissen en gemeld tokenverbruik; `*.meta.json`: commando, duur en exitcode.
- `runs-week05-v3/audit.json`: samengebracht tokenverbruik en geëxtraheerde JSON-records per antwoord.
- `week05-test.py`: voorbereiding en uitvoering, maximaal drie sessies tegelijk.

De vijftien voltooide runs melden samen **1.287.702 inputtokens**, waarvan **125.440 uit cache**, en **25.287 outputtokens**, waaronder **1.126 reasoningtokens** (al onderdeel van output). Dit is CLI-sessieverbruik voor deze tekstpipeline, geen afzonderlijke factuur of kostmeting van de productie-update met Excel. Er is hier geen prijs op toegepast.

## Steekproef door de student — afgerond

De student heeft deze twee nieuwe antwoorden naast de bronrapporten gecontroleerd:

1. `runs-week05-v3/T04-run1.txt`: Netflix, Q3 2026 — FCF, schuld en het onderscheid tussen 11,8% en 12% in de bron.
2. `runs-week05-v3/T03-run3.txt`: Amazon, Q2 2026 — schuldcomponenten, uitgesloten operationele leases en het afgeronde financieringsbedrag.

Voor beide antwoorden heeft de student de beoordeling Geslaagd bevestigd. Dit is een steekproef van 2 uit 15 antwoorden; de overige 13 zijn door de agent beoordeeld. De verwachte antwoorden zijn niet aangepast.

## Studentcontrole — Netflix

Op 22 oktober 2026 bevestigt de student met ‘netflix klopt’ dat T04 Run 1 volgens de besproken controlepunten klopt: FCF, schuld, omzetgroei, perioden, eenheden en de beperking bij de schuldafbakening. De agentbeoordeling Geslaagd is voor dit antwoord bevestigd. Amazon T03 Run 3 is vervolgens ook goedgekeurd, zoals hieronder vastgelegd. De verwachtingen en scores zijn niet aangepast.

### Studentcontrole — Amazon, gedeeltelijk

De student bevestigt daarna schuld en omzetgroei van T03 Run 3 met ‘de rest is al ok’. De FCF is nog niet teruggevonden en blijft open voor studentcontrole; geen volledige studentgoedkeuring van Amazon vastgelegd. De agentbeoordeling en verwachte antwoorden blijven ongewijzigd.

### Studentcontrole — Amazon, afgerond

De student bevestigt met ‘oke klopt gevonden’ ook de berekende FCF van T03 Run 3: 45.387 − 54.208 = −8.821 miljoen USD voor Q2 2026, op PDF-pagina 3. Schuld en omzetgroei waren al goedgekeurd. Daarmee is de agentbeoordeling Geslaagd voor dit tweede steekproefantwoord bevestigd. De eerdere gedeeltelijke beoordeling hierboven blijft als voorgeschiedenis bewaard; er staat geen controlepunt voor deze steekproef meer open. De verwachtingen en scores blijven ongewijzigd.

## Aanvulling na de modeltest — 23 oktober 2026

De afzonderlijke modeltest geeft voor één extra Sol-ronde **4/5**, door een andere afbakening van Amazon-schuld (132.549 tegenover de verwachte circa 155.315 miljoen USD). Zie `modellen.md` voor de afwijkingen in uitvoering en volledige beoordeling. De oorspronkelijke drie herhalingen blijven 5/5, 5/5 en 5/5; geen resultaat is vervangen of achteraf herlabeld. Over de vier beschikbare Sol-rondes is beschrijvend **4–5/5** waargenomen. Het oorspronkelijke bereik 5–5 was dus geen garantie voor toekomstige antwoorden. Astra scoort in de modeltest 5/5, binnen dit uitgebreid waargenomen Sol-bereik; één ronde bewijst geen algemeen kwaliteitsvoordeel van Astra.
