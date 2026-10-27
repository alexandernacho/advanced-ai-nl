# Week 5: Is mijn verbetering echt bewezen?

## Mijn foutmarge
Ik draaide v1 (week 2) en v3 elk 3 keer op dezelfde 10 inputs, met Claude Haiku 5.5. v1 haalde 9, 10 en 9 op 10. v3 haalde 9, 9 en 10. Beide bereiken zijn 9 tot 10 en overlappen. Mijn claim uit week 4 dat de voorbeelden de score verbeterden, trek ik in. T03 is een twijfelgeval: het model zegt onzeker, mijn verwachte antwoord is neutraal. Ik pas dat vóór een volgende run aan.

## Model en effort
Mijn gok: Opus 5.5 scoort het best, het verschil valt binnen mijn foutmarge en Haiku 5.5 is goed genoeg. Uitkomst, 1 run per setup op 10 inputs: Sonnet 5.5 (effort medium) 8 op 10, Haiku 5.5 10 op 10, Opus 5.5 10 op 10. Per run kost Haiku $0,00042, Sonnet $0,00604 en Opus $0,01348. Mijn gok klopte half. Deze taak draait op Haiku 5.5, met standaard effort, omdat hij 10 op 10 haalde, net als Opus, en bij 1.100 runs per jaar $0,46 kost tegen $14,83 voor Opus.

## Mijn value chain, met de foutmarge erin
Met de hand kost een bericht ongeveer 95 seconden. Met de tool is het 43 tot 52,5 seconden. Bij 5 berichten per werkdag is het netto ± €280 tot ± €342 per jaar. Mijn zwakste cijfer zijn die 95 seconden: bij de helft is het netto ± −€2 tot ± €29.

| Schakel | Waarde | Bron |
|---|---|---|
| 1. Met de hand | Openen 15 s · lezen 30 s · beslissen 30 s · noteren 20 s = **95 s** | geschat (uit week 4), nog niet met een stopwatch gemeten |
| 2. Score | 9 tot 10 op 10 (foutmarge, n = 10, 3 runs) | gemeten (`build/foutmarge.md`) |
| 2. Met de tool | Vinden en openen 15 s · kopiëren en plakken 10 s · wachten 8 s · nakijken 10 s = 43 s. Fouten herstellen = deel fout × 95 s: bij 9/10 is dat 10% × 95 = 9,5 s, bij 10/10 is dat 0 s. Samen **52,5 s** (9/10) of **43 s** (10/10) | wachttijd gemeten (week 4), rest geschat (uit week 4), foutdeel gemeten |
| 3. Winst per bericht | 95 − 52,5 = **42,5 s** (9/10) · 95 − 43 = **52 s** (10/10) | berekend |
| 4. Volume | 5 per dag · 25 per week · 100 per maand · **1.100 per jaar** | geschat. Ik gebruik de tool zelf als particuliere belegger: ik volg elke werkdag ongeveer 5 nieuwsberichten over defensie op voor ik beslis over mijn aandelen. Dat schreef ik ook in week 4. De 30 per dag in `build/kosten.md` was te hoog. Aanname: 220 werkdagen per jaar (zoals in de README), dus 1.100 en niet 12 × 100 |
| 5. Uren per jaar | 42,5 s × 1.100 = **13 u** (9/10) · 52 s × 1.100 = **15,9 u** (10/10) | berekend |
| 6. Uurkost | €14,38 bruto × 1,5 = **€21,57** | bruto gemeten bij Indeed België (gemiddeld basisloon student, 11 oktober 2026, https://be.indeed.com/career/student/salaries). Factor 1,5: vuistregel uit `cursus/week-05/README.md` (Acerta, Securex, Teamed), aanname |
| 7. Kost van de tool | 1.100 × $0,00042 = $0,46 = **€0,42 per jaar** (Haiku 5.5, 2.600 tokens in, 319 uit, 1 dollar = 0,90 euro) | gemeten (`build/modellen.md`, prijs uit de tabel van week 5); wisselkoers is een aanname |
| 8. Netto per jaar | 13 × 21,57 − 0,42 = **± €280** (9/10) · 15,9 × 21,57 − 0,42 = **± €342** (10/10) | berekend |
| 9. Bereik | **± €280 tot ± €342 per jaar**. Midden (9,5/10): ± €311 | foutmarge |
| 10. Zwakste cijfer | De 95 s met de hand: geschat, niet gemeten. Is het de helft (47,5 s), dan is het netto **± €29** (10/10) of **± −€2** (9/10), midden ± €14. Bij 9/10 wint de tool dan niets meer. Daarbij daalt ook het fouten herstellen, want dat is 10% van de handtijd. | geschat |

## Mijn testset groeit
Mijn testset (set v2) groeide van 10 naar 30 inputs. De 20 nieuwe zijn echte berichten uit De Tijd en VRT NWS. De juiste antwoorden schreef ik op vóór ik draaide. 13 zijn gewone gevallen. Zes zijn randgevallen, zoals een lange alinea, tien onderwerpen in één bericht, een misleidend woord en afgebroken alinea's. Maar 2 hebben onzeker als antwoord, omdat ik er niet meer vond.

De input die mijn tool het meest verraste is T16: onzeker, terwijl ik positief verwachtte, omdat het bericht herstel van Starlink en vrees voor Washington noemt.

Mijn score is 23 op 30 (set v2, 1 run). Op T01–T10 is dat 10 op 10, op T11–T30 13 op 20. Zes van de zeven fouten zijn "onzeker" of "neutraal" waar ik positief of neutraal verwachtte, omdat de tekst geen budget of bestelling noemt.

## Mijn dashboard
https://claude.ai/artifact/E19YfPwAF885qHUM1b3pz9

Een lezer moet eerst zien dat mijn score 9 tot 10 op 10 is en dat mijn claim is ingetrokken.

## Mijn AI-ismen

> Week 1: "Koersen opvolgen in functie van de actualiteit: linken leggen met bijvoorbeeld nieuwe oorlogen, en advies geven om bijvoorbeeld in de wapenindustrie te investeren."

Herschreven: Ik bouw een tool die per nieuwsbericht zegt of de vraag naar defensiebedrijven stijgt of daalt; beleggingsadvies geeft hij niet, en de beurskoers voorspelt hij niet.

> Week 2: "Met deze tool zie je dat in een paar seconden."

Herschreven: De tool wacht ongeveer 8 seconden op een label (gemeten), tegenover ongeveer 95 seconden met de hand (geschat).

> Week 2: "Ik wil dat omdat er elke dag veel nieuws is over oorlog, de NAVO en defensiebudgetten, en het veel tijd kost om zelf in te schatten welk bericht echt iets verandert voor die bedrijven."

Herschreven: Ik volg elke werkdag ongeveer 5 nieuwsberichten over defensie op en ik doe er zelf ongeveer 95 seconden over per bericht.

> Week 2: "De fout zit niet in het model, maar in mijn keuze om alleen de kop en de eerste alinea te gebruiken."

Herschreven: Bij T01 stond het budget pas in de tweede alinea, dus mijn prompt kon het niet zien en ik paste het verwachte antwoord aan naar onzeker.

> Week 3: "Dit cijfer zegt dat de prompt goed werkt op deze vijf berichten en dat het model consistent is."

Herschreven: Op T06 tot T10 had het model 8 van de 10 antwoorden juist. De enige fout was T08, in beide runs negatief.

> Week 4: "De kosten zijn dus geen probleem, zelfs niet met het duurdere model."

Herschreven: Bij 100 runs per maand kost Haiku 5.5 €0,08 en Sonnet 5.5 €1,55.
