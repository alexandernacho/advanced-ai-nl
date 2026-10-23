# Modeltest — week 5

## Mijn voorspelling, vóór de modeltest

Vastgelegd op 22 oktober 2026. De student zegt: “ik verwacht sol ik werk hier momenteel mee en deze kan het aan”.

Ik verwacht dat Sol het beste scoort. Ik werk er momenteel mee en het kan mijn taak aan. Daarom verwacht ik dat Sol ook goed genoeg is voor mijn kwartaalopvolging.

Met Sol bedoelen we hier GPT-6.1 Sol, het model van de voorafgaande herhaaltest, met effort low. De voorspelling is na die herhaaltest maar vóór de vergelijking met andere modellen vastgelegd. Nog geen definitieve productiekeuze op basis van een modelvergelijking.

## Modeltest

### Opzet vóór de runs

Vastgelegd op 22 oktober 2026, na de voorspelling en vóór uitvoering. Vijf inputs, elk één nieuwe onafhankelijke sessie per setup (15 antwoorden). Dezelfde opgeslagen inputteksten en hashes als bij de herhaaltest. Geen verwachte antwoorden in de modelinput; geen Excel-update. Dezelfde extractiescope en vooraf gekozen halfjaarperioden voor LLY en UBER.

| Setup | Model | Effort |
|---|---|---|
| A, standaard | GPT-6.1 Sol (`gpt-6.1-sol`) | low |
| B, kleiner | GPT-6 Luna (`gpt-6-luna`) | low |
| C, groter | GPT-6 Astra (`gpt-6-astra`) | low |

De lokale CLI-catalogus bevat alle drie modellen met effort low. Werkelijke accounttoegang wordt pas door de runs vastgesteld. Gelijke effort is gekozen om het modeleffect te vergelijken; geen afzonderlijke effortvergelijking.

De runner gebruikt dezelfde isolatie als de herhaaltest. De eerder genegeerde optie `tools.disable_defaults` is verwijderd. `service_tier` wordt expliciet `default`; geen Fast-tarief. Ruwe logs blijven bewaard en worden op toolacties gecontroleerd.

### Kostenafbakening, vooraf vastgelegd

Standaard API-equivalent in USD, geen Plus-factuur of volledige Excel-workflow. Tarieven per miljoen tokens, officiële modelpagina's gecontroleerd op 22 oktober 2026:

| Model | Input | Cache lezen | Cache schrijven | Output |
|---|---:|---:|---:|---:|
| Sol | $2 | $0,10 | $2,50 | $10 |
| Luna | $0,10 | $0,01 | $0,125 | $0,50 |
| Astra | $10 | $1 | $12,50 | $50 |

Bronnen: [Sol](https://developers.openai.com/api/docs/models/gpt-6.1-sol), [Luna](https://developers.openai.com/api/docs/models/gpt-6-luna), [Astra](https://developers.openai.com/api/docs/models/gpt-6-astra).

Gemeten sessiekost: ongecachete input × inputtarief + cache-input × cachetarief + eventueel cache schrijven × schrijftarief + output × outputtarief, gedeeld door een miljoen. Reasoningtokens zitten al in output. Controleer per aanvraag of de grens van 272.000 inputtokens wordt overschreden; dan gelden volgens de bron hogere tarieven.

Vergelijk daarnaast een scenario zonder cachekorting om toevallige cacheverschillen zichtbaar te maken. Dezelfde inputtekst is geen garantie voor exact evenveel geregistreerde sessie-inputtokens. Rapporteer gemiddelde kost per bedrijfsupdate over de vijf testgevallen en vermenigvuldig voor het jaarscenario met de bestaande volumeaanname van 40 updates. Dit veronderstelt dat de vijf gevallen representatief zijn; geen gemeten productiejaarkost.

### Resultaten

Uitgevoerd op **22 en 23 oktober 2026**. De eerste twaalf antwoorden zijn van 22 oktober. De drie Uber-pogingen stopten die dag door de gebruikslimiet, zonder antwoord. Die meldingen zijn bewaard in `runs-week05-modellen/gebruikslimiet-22okt/`; alleen deze drie ontbrekende antwoorden zijn op 23 oktober opnieuw aangevraagd. Geen inhoudelijk antwoord is vervangen of geselecteerd na het zien van de score.

**Beoordelaar: de agent**, volgens dezelfde vooraf bevestigde regel als de herhaaltest: juiste cijfers, perioden, valuta en schuldbeperking. Nog geen studentcontrole van deze vijftien nieuwe antwoorden. De studentcontrole van Netflix en Amazon bij de eerdere herhaaltest betreft andere antwoorden en geldt niet automatisch voor deze modeltest.

| Setup | Model | Effort | Score (n = 5, 1 run) | Gem. outputtokens per bedrijfsupdate | Gem. API-equivalent per update | Scenario 40 updates/jaar |
|---|---|---|---:|---:|---:|---:|
| A | GPT-6.1 Sol | low | **4/5 (80%)** | 1.732,6 | **$0,17394** | **$6,96** |
| B | GPT-6 Luna | low | **0/5 (0%)** | 1.371,4 | **$0,00851** | **$0,34** |
| C | GPT-6 Astra | low | **5/5 (100%)** | 1.762,4 | **$0,88236** | **$35,29** |

0/5 betekent nul volledig geslaagde antwoorden binnen deze beoordelingsregel, niet dat alle Luna-cijfers fout zijn. Als aanvullende beschrijving komen 12/15 hoofdwaarden van Luna overeen met de verwachtingen, tegenover 14/15 bij Sol en 15/15 bij Astra. Dat is geen vervanging van de vooraf vastgelegde beoordeling: een juist schuldbedrag met een onjuiste of ontbrekende schuldbeperking slaagt niet volledig.

### Waar het verschil zit

| Input | Sol A | Luna B | Astra C |
|---|---|---|---|
| T01 NVO | Geslaagd | Niet geslaagd: 140.127 miljoen DKK klopt, maar Luna zegt dat leases zijn uitgesloten en gebruikt niet de verwachte status Onzeker. Verwachting: leases inbegrepen, afbakening onzeker. | Geslaagd |
| T02 LLY | Geslaagd | Niet geslaagd: schuldstatus Onzeker ontbreekt; bovendien is de omzetgroeicontrole circa 47,61% in plaats van circa 47,6668% (afgerond 47,7%). | Geslaagd |
| T03 AMZN | Niet geslaagd: schuldhoofdwaarde 132.549 in plaats van circa 155.315 miljoen USD. Financiële leases en financieringsverplichtingen staan apart maar zijn expliciet uitgesloten. | Niet geslaagd: twaalfmaands-FCF −7.604 in plaats van kwartaal-FCF −8.821; schuld 132.224 in plaats van circa 155.315 miljoen USD. | Geslaagd |
| T04 NFLX | Geslaagd | Niet geslaagd tegenover de vaste verwachting: hoofdwaarde 12% in plaats van 11,8% uit de overzichtstabel. Beide percentages staan in de bron; de verwachte keuze wordt na de run niet aangepast. | Geslaagd |
| T05 UBER | Geslaagd | Niet geslaagd: bedragen en renteloze obligaties kloppen, maar schuldstatus is Nog te controleren in plaats van Onzeker; de onzekere volledigheid door ontbrekende financiële-leaseboekwaarden wordt niet expliciet als oordeel over het totaal gegeven. | Geslaagd |

De financiële lezingen en statuskeuzes zijn door de agent nagekeken in tabel en JSON, niet alleen met een numerieke vergelijking. Een afwijking is geteld tegenover de eerder vastgelegde verwachting; er zijn geen nieuwe vereisten aan de succesregel toegevoegd. Bij Luna's Uber-antwoord wijkt ook `period_type: Zes maanden` af van het v3-schema, maar dat is niet als extra reden gebruikt om de vastgelegde financiële score te verlagen.

### Mijn voorspelling tegenover de meting

De student voorspelde dat Sol het beste zou scoren en goed genoeg is. **Sol scoort in deze ene ronde 4/5 en Astra 5/5; Sol is hier dus niet de hoogste scorer.** Of Sol met menselijke controle goed genoeg is, is nog een keuze van de student. De meting toont geen foutloos resultaat voor Sol en valideert geen volledige Excel-workflow.

### Verschil tegenover het waargenomen bereik

De eerdere Sol-herhaaltest gaf 5/5, 5/5 en 5/5. De nieuwe Sol-run geeft 4/5. Dit bewijst dat het oude min–max-bereik 5–5 geen harde grens aan toekomstige scores was. Over de vier beschikbare Sol-rondes is nu beschrijvend een bereik van **4–5/5** waargenomen. De aparte opzetgegevens en oorspronkelijke resultaten blijven bewaard; dit is geen nieuwe statistische foutmarge of vooraf gepland vierde herhaalexperiment.

- Sol 4/5 en Astra 5/5 liggen beide binnen dit waargenomen Sol-bereik van 4–5/5.
- Luna 0/5 ligt eronder volgens de volledige beoordelingsregel.
- Astra heeft de hoogste score in deze ronde, maar met vijf inputs en één run per model is een betrouwbaar algemeen kwaliteitsverschil tegenover Sol niet aangetoond. Van Luna en Astra is ook geen eigen herhaalbereik gemeten.

### Kostencontrole

| Model | Gem. inputtokens, incl. cache | Gem. cache-input | Gem. outputtokens | Gem. API-equivalent met gemeten cache | Scenario zonder cachekorting |
|---|---:|---:|---:|---:|---:|
| Sol | 85.846,8 | 7.936,0 | 1.732,6 | $0,1739412 | $0,1890196 |
| Luna | 85.154,8 | 7.628,8 | 1.371,4 | $0,008514588 | $0,00920118 |
| Astra | 85.782,8 | 7.065,6 | 1.762,4 | $0,8823576 | $0,9459480 |

Alle vijftien antwoorden hebben één `turn.completed`, nul geregistreerde toolacties en een succesvolle exitcode. Cache-schrijftokens zijn overal nul. De grootste gemelde input is per model 201.201 (Sol), 200.509 (Luna) en 201.137 (Astra) tokens; alle blijven onder 272.000, zodat de lange-contexttoeslag niet is toegepast. Reasoning zit al in output en wordt niet nogmaals opgeteld.

Voorbeeld Sol: `((85.846,8 − 7.936) × 2 + 7.936 × 0,10 + 1.732,6 × 10) / 1.000.000 = $0,1739412` gemiddeld per update. Jaarscenario: dit gemiddelde × 40. Het verschil in inputtokens bij dezelfde rapporttekst komt voort uit de modelsessies, niet uit anders gekozen financiële inputs. De kosten omvatten de CLI-context en het volledige rapport, geen afzonderlijk gemeten eigen promptdeel uit week 4.

Astra is in dit API-scenario circa **5,07×** zo duur als Sol; Luna kost circa **4,9%** van Sol. Deze verhoudingen zijn berekeningen met de vastgelegde standaardtarieven, geen abonnementsfactuur of actuele creditmeting. Fouten herstellen en menselijke controle zijn niet in deze API-kosten opgenomen. Vanwege de financiële fouten is de goedkoopste tokenkost niet automatisch de laagste totale werkkost.

### Bewijs en beperkingen

- `runs-week05-modellen/manifest.json`: vooraf vastgelegde setups, tarieven, inputhashes en bronlinks.
- `[A/B/C]-T01.txt` t/m `[A/B/C]-T05.txt` in die map: alle vijftien antwoorden; daarnaast events, stderr en meta per sessie.
- `runs-week05-modellen/audit.json`: financiële records, oordelen, tokenverbruik en berekende kosten per antwoord.
- `runs-week05-modellen/samenvatting.json`: totalen en gemiddelden per setup.
- `week05-modeltest.py`: uitvoerscript; `week05-modelanalyse.py`: audit en kostenberekening met expliciet vastgelegde semantische oordelen.
- Buitenste sandbox-opstartfouten zijn apart bewaard in `startfouten/`; zij bevatten geen modelantwoord en tellen niet als financiële mislukking.
- Voor de drie Uber-antwoorden zit een dag tussen de overige runs en de afronding. Cachegebruik kan verschillen; daarom is ook een scenario zonder cachekorting gegeven.
- Scope blijft tekstextractie na vooraf gekozen halfjaarperioden, zonder tools of Excel. De bron- en tekstextractiebeperkingen uit `foutmarge.md` blijven gelden.

### Productiekeuze

De student kiest op 23 oktober 2026: **“sol met schuldcontrole”**. Voorlopige werkwijze: **GPT-6.1 Sol, effort low, met aanvullende handmatige schuldcontrole per bedrijfsupdate**. De praktische controle staat in `schuldcontrole.md`. De student heeft geen verdere persoonlijke motivatie opgegeven; die wordt niet ingevuld door de agent.

Deze keuze verandert de gemeten score van Sol (4/5) niet. Het effect en de extra tijd van de schuldcontrole zijn nog niet gemeten; geen hogere nauwkeurigheid of nieuwe nettowaarde claimen. De geteste v3-prompt en historische runs blijven behouden. Het vastleggen van de modelkeuze verandert niet automatisch het model van iedere toekomstige sessie; gebruik bij de uitvoering expliciet deze setup.

De student schat de schuldcontrole vervolgens op **maximaal 5 minuten per update**, omdat die AI-uitvoer altijd al controleert. Eigen inschatting, geen gemeten tijd. De eerdere 15 minuten tooltijd omvatten al 7 minuten controleren. Voorlopig behandelen we schuldcontrole als onderdeel daarvan; geen automatische extra 5 minuten of verkorting van de totale controle. Correctietijd en het kwaliteitseffect van deze werkwijze blijven ongemeten.
