# Waarde: met de hand of met de tool?

Gemaakt op 14 oktober 2026. Plek: Sporza, de vormstatus van renners als input voor de prijzen in de Sporza Wielermanager (voorjaarsklassiekers).

| Schakel | Waarde | Bron |
|---|---|---|
| 1. Met de hand | zoeken 120 s + lezen 450 s (300 tot 600 s) + label kiezen 30 s = 600 s per renner | geschat |
| 2. Met de tool | zoeken 120 s + kopiëren en plakken 60 s + draaien 7 s + nakijken 15 s = 202 s | draaien gemeten (/cost), de rest geschat |
| 3. Winst per renner | 398 s (± 6,6 min) | |
| 4. Volume | ± 950 renners per jaar: één beoordeling per renner vóór het voorjaarsspel | Sporza (17 april 2026): 900 tot 1.000 renners in de voorjaarsklassiekers; aanname: één beoordeling per jaar |
| 5. Uren gewonnen | 950 × 398 s = ± 105 uur per jaar | |
| 6. Uurkost | € 16 tot € 23 per uur (midden € 19,50) | aanname: brutoloon van een medewerker of journalist |
| Waarde | 105 × € 16 tot € 23 = € 1.680 tot € 2.415 per jaar | |
| 7. Kost van de tool | 950 × € 0,017 = ± € 16 per jaar (lage schatting: € 8) | gemeten, zie kosten.md |
| 8. Netto | ± € 1.660 tot € 2.400 per jaar | |

Bron volume: https://sporza.be/nl/2026/04/17/1-keer-als-kopman-900-renners-zijn-populairder-de-straffe-wielermanager-cijfers-achter-stuntwinnaar-anders-foldager~1776462670069/

## Zwakste cijfer

| Als... | Netto per jaar (bij € 19,50 per uur) |
|---|---:|
| Basis | ± € 2.030 |
| Lezen duurt 5 min in plaats van 7,5 | ± € 1.290 |
| Uurkost is de echte loonkost (€ 45, voorbeeld uit het lesmateriaal) | ± € 4.710 |
| Sporza beoordeelt de vorm nu helemaal niet met de hand | ± € 0 tijdwinst, maar wel betere prijzen |

Mijn zwakste punt: ik weet niet of Sporza vandaag de vorm van renners opvolgt bij het bepalen van de prijzen. Doet niemand dat, dan bespaart de tool geen tijd en zit de waarde in betere prijzen en een spannender spel.

## Kanttekeningen
- De tool zoekt nu zelf geen artikels; het zoeken zit in beide kanten van de vergelijking.
- € 16 tot € 23 is een brutoloon; de echte loonkost voor de werkgever ligt hoger. Ik reken dus voorzichtig.
- De kost van de tool is verwaarloosbaar tegenover de tijdwinst.

## Week 5: value chain met foutmarge (21 oktober 2026)

Model in productie: Sonnet 5.5, effort medium (zie modellen.md). Bereik uit mijn foutmarge: 7 tot 8 op 10 (n = 10, 3 runs). Uurkost voor de werkgever = bruto × 1,5 (vuistregel week 5: vakantiegeld, dertiende maand en sociale bijdragen).

| Schakel | Bij 8/10 (Sonnet) | Bij 7/10 (ondergrens) | Bron |
|---|---|---|---|
| 1. Met de hand | 600 s (zoeken 120 + lezen 450 + label 30) | 600 s | geschat |
| Score | 8/10 (Sonnet, 3 runs) | 7/10 (laagste uit foutmarge) | gemeten |
| 2. Met de tool | zoeken 120 + plakken 60 + draaien 7 + nakijken 15 + fouten herstellen 20% × 480 = 96 → 298 s | ... + fouten herstellen 30% × 480 = 144 → 346 s | gemeten en geschat |
| 3. Winst per renner | 302 s | 254 s | |
| 4. Volume | 950 renners per jaar | 950 | Sporza, voorjaarsklassiekers |
| 5. Uren gewonnen | ± 80 u per jaar | ± 67 u per jaar | |
| 6. Uurkost werkgever | € 19,50 bruto × 1,5 = € 29,25 (bereik € 24 tot € 34,50) | idem | aanname |
| Waarde | € 2.331 per jaar | € 1.960 per jaar | |
| 7. Kost van de tool | ± € 24,55 per jaar (Sonnet 5.5) | idem | gemeten, modellen.md |
| 8. Netto | ± € 2.307 per jaar | ± € 1.935 per jaar | |

Een fout herstellen = 480 s (lezen 450 + label 30): het zoeken is bij de tool al gebeurd.

### Bereik

Met mijn foutmarge: ± € 1.935 tot ± € 2.307 per jaar. Met ook de onzekerheid op het loon (€ 24 tot € 34,50 per uur): ± € 1.580 tot ± € 2.725 per jaar.

### Zwakste cijfer

| Wat verandert | Effect op het netto (bij 8/10) |
|---|---|
| Foutmarge: 8/10 naar 7/10 | − € 372 |
| Leestijd de helft (225 s in plaats van 450 s) | − € 1.390 (van € 2.307 naar ± € 917) |

Mijn leestijd beweegt het netto bijna vier keer meer dan mijn foutmarge. Mijn zwakste cijfer is dus de leestijd, niet mijn score.

Waarom ik met 10 minuten met de hand reken: om een heel goed antwoord te krijgen, moet je verschillende artikels lezen, en dat is ook wat mijn tool doet (twee tot vier berichten). De meeste mensen lezen maar één artikel. Dat kost de helft van de tijd, maar geeft een minder accuraat antwoord. De vergelijking met de helft van de leestijd is dus eigenlijk een vergelijking met slechter werk.

De grootste open vraag blijft of Sporza vandaag al iemand de vorm van renners laat opvolgen.

## Week 5: value chain met n = 20 (27 oktober 2026)

| Schakel | Bij 14/20 (Sonnet) | Bij 13/20 (ondergrens) |
|---|---|---|
| Met de hand | 600 s | 600 s |
| Fouten herstellen | 30% × 480 s = 144 s | 35% × 480 s = 168 s |
| Met de tool | 346 s | 370 s |
| Winst per renner | 254 s | 230 s |
| Uren per jaar (950 renners) | ± 67 u | ± 61 u |
| Waarde (× € 29,25) | € 1.960 | € 1.775 |
| Kost van de tool (Sonnet 5.5) | € 24,55 | € 24,55 |
| Netto | ± € 1.935 | ± € 1.751 |

Zwakste cijfer: de foutmarge verschuift het netto met − € 184, een halve leestijd (225 s) met − € 1.215 (naar ± € 720). De leestijd blijft mijn zwakste cijfer.
