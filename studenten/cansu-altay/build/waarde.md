# Tijdwinst en waarde — week 5

## Correctietijd — schatting van Cansu

> Gemiddeld denk ik ongeveer 45 seconden nodig te hebben om één verkeerde tabel te corrigeren met de oorspronkelijke trainingsnotitie erbij. Bij een kleine fout kan dat sneller gaan, ongeveer 20 seconden, maar bij onduidelijke sets of meerdere fouten kan het eerder 1 tot 2 minuten duren.

Bron: eigen inschatting van Cansu, geen tijdmeting. Voor de voorlopige berekening gebruiken we 45 seconden per fout antwoord; meerdere fouten in één tabel tellen als één te herstellen tabel. De 20 seconden en 1–2 minuten beschrijven variatie in correctietijd, niet de gemeten foutmarge van het model.

Cansu verduidelijkt:

> Bij een kleine fout denk ik dat dit meestal nog binnen mijn gewone rustpauze past, omdat ik mijn trainingsnotitie er al bij heb. Bij een moeilijkere correctie van één à twee minuten kan mijn rustpauze soms wel iets langer worden, maar gemiddeld zou ik die 45 seconden niet volledig als extra trainingstijd aftrekken.

Het extra deel is nog niet gemeten. Daarom rekenen we met twee grenzen: geen extra correctietijd en de volledige gemiddelde 45 seconden als extra tijd. Dit zijn scenario's, geen gemeten grenzen; individuele moeilijke correcties kunnen langer duren.

## Uitgangspunten uit week 4

- Drie trainingen per week, vijf à zes notities per training; 52 weken per jaar als aanname.
- Zonder overzicht: geschat drie minuten extra uitproberen per training.
- Met overzicht: voorlopig twee raadplegingen van elk geschat 30 seconden per training.
- Typen, wachten en controleren vallen volgens Cansu's voorgenomen gebruik binnen bestaande rust, zonder verlenging; dit is nog niet gemeten.
- Voorlopige winst vóór extra correctietijd: twee minuten per training, 5,2 uur per jaar.
- Persoonlijke waarderingsaanname: €15–€17 per uur vrije tijd, geen werkelijk verdiend loon of werkgeversloonkost.
- Het gewenste overzicht met bewaren en terugzoeken is nog niet gebouwd. Tijdwinst is een scenario, geen gemeten resultaat.

## Scores en gekozen model

Terra met v5 heeft een waargenomen bereik van 8–9/10 over drie runs: 10–20% fout onder de vooraf afgesproken uitvoerregels. Luna is voorlopig gekozen en scoorde 10/10 in één ronde, maar heeft nog geen eigen gemeten bereik over herhalingen. Het Terra-bereik mag alleen als expliciet benoemd gevoeligheidsscenario voor Luna worden gebruikt, niet als gemeten Luna-foutmarge. Zie `foutmarge.md` en `modellen.md`.

## Berekening — uitgewerkt op 25 oktober 2026

Voor het gevoeligheidsscenario gebruiken we 10–20% foute tabellen, ontleend aan Terra met v5. Dit is geen gemeten Luna-foutpercentage. We rekenen niet met gegarandeerd nul fouten op basis van Luna's ene ronde van 10/10.

| Schakel | Berekening | Onderbouwing |
|---|---|---|
| Zonder overzicht | 180 s extra uitproberen per training | Eigen schatting; gewone sets, rust en klaarzetten tellen niet mee |
| Met overzicht, vóór fouten herstellen | 2 × 30 s terugzoeken = 60 s extra per training | Eigen schatting; overzicht nog niet gebouwd |
| Typen, draaien en nakijken | Samen 48–53 s per notitie, maar 0 s extra als alles binnen gewone rust past | Eerdere schattingen; overlap nog niet gemeten |
| Volume | 5–6 notities per training; 3 trainingen per week; 156 trainingen per jaar | Eigen inschatting, 52 weken als aanname |
| Verwachte foute tabellen | 5–6 × 10–20% = 0,5–1,2 per training | Gevoeligheidsscenario, geen gemeten Luna-foutmarge |
| Herstelwerk | 0,5–1,2 × 45 s = 22,5–54 s per training | Gemiddelde correctietijd geschat door Cansu |
| Extra herstelwerk bovenop training | 0 s bij volledige overlap; 22,5–54 s bij geen overlap | Werkelijke overlap onbekend |
| Winst per training | 180 − 60 − extra herstelwerk | Hieronder uitgesplitst |

### Twee grenzen voor overlap met rust

| Scenario | Winst per training | Per week (3 trainingen) | Per gemiddelde maand (13 trainingen) | Per jaar (156 trainingen) |
|---|---:|---:|---:|---:|
| Alle gemiddelde correctietijd past binnen gewone rust | 120 s | 6 min | 26 min | 5,2 uur |
| Alle gemiddelde correctietijd komt erbovenop | 66–97,5 s | 3 min 18 s–4 min 52,5 s | 14 min 18 s–21 min 7,5 s | 2,86–4,225 uur |

De tweede rij gebruikt de ongunstigste combinatie (6 notities, 20% fout) en gunstigste combinatie (5 notities, 10% fout). Dit is een scenario met zowel volumeverschil als scoreverschil. Bij vast volume is het effect van uitsluitend de score:

| Vast volume | Winst per training bij 8/10 | Winst per training bij 9/10 | Uren per jaar bij 8/10–9/10 |
|---|---:|---:|---:|
| 5 notities, volledig extra herstelwerk | 75 s | 97,5 s | 3,25–4,225 |
| 6 notities, volledig extra herstelwerk | 66 s | 93 s | 2,86–4,03 |

Het werkelijke scenario kan tussen de twee overlapgrenzen liggen. Hoeveel gemiddeld extra tijd ontstaat, moet nog tijdens trainingen worden gemeten.

## Persoonlijke vergelijkingswaarde, geen inkomsten

Cansu gebruikte eerder haar eigen uurloon (€15–€17) als persoonlijke vergelijkingswaarde voor vrije tijd. Dit is geen werkgeversloonkost en geen werkelijk verdiend geld. De opdracht vraagt een werkgeversuurkost; die is voor deze persoonlijke sporttoepassing niet vastgesteld en wordt niet verzonnen.

De voorlopige Luna-modelkosten zijn €0,233–€0,280 per jaar bij 780–936 notities, volgens `kosten.md`. Deze losse-toolraming gebruikt de historische rekenkoers uit week 4, geen actuele koers, en sluit opslag, hosting en andere softwarekosten uit.

| Scenario | Persoonlijke jaarwaarde vóór modelkosten | Na aftrek van geraamde Luna-modelkosten |
|---|---:|---:|
| Volledige overlap met rust | €78–€88,40 | circa €77,72–€88,17 |
| Geen overlap van gemiddelde correctietijd, 10–20% fout als scenario | €42,90–€71,83 | circa €42,62–€71,59 |

Ondergrens: laagste uren × €15 − hoogste modelkosten. Bovengrens: hoogste uren × €17 − laagste modelkosten. Dit zijn ruime scenariogrenzen, geen gerealiseerd rendement.

## Zwakke cijfers en halvering van de zoektijd

Cansu gaf eerder aan alle tijdschattingen onvoldoende te vertrouwen; ze zijn nog niet gemeten. Daar komt de onbekende overlap van correcties met rust bij.

Cansu kiest ervoor eerst de geschatte 30 seconden terugzoeken per oefening te meten, omdat zij dit meerdere keren wil kunnen meten en optellen tot een trainingstotaal. De meting van het geplande overzicht kan pas zodra het overzicht gebouwd is; er is nog geen gemeten terugzoektijd. Hoe vaak ze werkelijk raadpleegt moet tegelijk worden genoteerd, in plaats van automatisch alle oefeningen te tellen.

Als de geschatte 180 s uitproberen zonder overzicht de helft is (90 s), blijft vóór extra correcties 90 − 60 = 30 s winst per training over: 1,3 uur per jaar. Als de volledige gemiddelde herstelduur ook extra trainingstijd is, wordt dit 30 − (22,5–54) = **−24 tot +7,5 s per training**, oftewel **−1,04 tot +0,325 uur per jaar**. Tijdverlies is dus mogelijk als deze aannames ongunstig uitvallen.

Bij 5 notities en volledig extra herstelwerk verandert de jaartijd door de score van 8 naar 9 op 10 met 0,975 uur; bij 6 notities met 1,17 uur. Halvering van de uitprobeertijd verlaagt de jaartijd met 3,9 uur. Die tijdschatting beïnvloedt dit scenario dus meer dan het gemeten Terra-scorebereik. Eerst echt meten is nodig voordat we tijdwinst claimen.
