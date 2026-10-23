# Waardeberekening — week 5

Bijgewerkt op 23 oktober 2026. Gekozen werkwijze: GPT-6.1 Sol, effort low, met handmatige schuldcontrole. Persoonlijke kwartaalopvolging, geen betaalde werknemerstaak.

## Vaste uitgangspunten van de student

| Schakel | Waarde | Bron en status |
|---|---|---|
| Handmatig rapport zoeken | 5 minuten | Eigen schatting, week 4 |
| Cijfers verzamelen, invoeren en berekenen | 45 minuten | Eigen schatting, week 4 |
| Handmatige cijfercontrole | 10 minuten | Eigen schatting, week 4 |
| Handmatig totaal | **60 minuten per bedrijfsupdate** | Som van de drie stappen; geen chronometermeting |
| Tool uitvoeren | 8 minuten | Eigen schatting, week 4 |
| Controleren met de tool | 7 minuten | Eigen schatting, week 4 |
| Schuldcontrole | Maximaal 5 minuten | Eigen schatting, 23 oktober; voorlopig binnen de bestaande 7 minuten, geen automatische extra tijd |
| Tooltijd vóór afzonderlijk foutherstel | **15 minuten per bedrijfsupdate** | 8 + 7; voorlopige afbakening, overlap en correctietijd niet apart gemeten |
| Herstellen van een gevonden fout | **Ongeveer 7 minuten extra per niet volledig geslaagde update** | Eigen schatting, 23 oktober; inclusief feedback doorgeven, geen gemeten herstelduur |
| Volume | 10 bedrijven × 4 kwartalen = **40 updates per volledig jaar** | Eigen plan; 10 per kwartaal en gemiddeld 3,33 per maand |
| Persoonlijke uurwaarde | **€5 per uur** | Eigen waardering wegens training en familietijd; geen werkgeversloonkost of gerealiseerd inkomen |
| Zwakste aanname | **40 updates per jaar** | Eerder door student gekozen; gevoeligheid bij 20 updates |

De oorspronkelijke tijdschattingen gaan over gegevens verzamelen, noteren en controleren. Eigen analyses, risicoanalyse en beleggingsbeslissingen vallen erbuiten. Mogelijk betere beleggingsresultaten worden niet als opbrengst meegenomen.

## Score en herstel

De oorspronkelijke Sol-herhaaltest heeft n = 5 inputs, 3 herhalingen, scores 5/5, 5/5, 5/5. De afzonderlijke modeltest voegt één Sol-ronde van 4/5 toe. Beschrijvend waargenomen bereik over die vier rondes: **4–5/5, oftewel 80–100%**. Dit is geen statistisch betrouwbaarheidsinterval of garantie voor toekomstig gebruik. Zie `foutmarge.md` en `modellen.md` voor de verschillende testcondities.

Voor een scenario komt dit overeen met **0–20% niet volledig geslaagde bedrijfsupdates**. Dat percentage betreft hele beoordeelde antwoorden, niet het percentage foutieve cijfercellen. De score is gemeten voor de extractievariant, niet voor de volledige Excel-workflow en niet voor de werking na menselijke correctie. Toepassing op het jaarplan is dus een scenarioaanname.

De student schat het herstellen van één gevonden fout op **ongeveer 7 minuten extra**, boven op de bestaande 15 minuten uitvoeren en controleren. Toelichting: “want ik geef dit dan ook door zodat die hopelijk dit niet meer doet in de toekomst”. De schatting omvat correctie en het doorgeven van feedback; het vinden van de fout tijdens de gewone controle wordt niet nogmaals geteld. De berekening veronderstelt één herstelactie van zeven minuten per niet volledig geslaagde bedrijfsupdate; meer fouten of herhaalde correcties zijn hiermee niet apart gemodelleerd.

De hoop op minder herhaling is geen gemeten kwaliteitsverbetering. Feedback in een gesprek garandeert niet dat een nieuwe, onafhankelijke sessie die correctie gebruikt. Een blijvende instructiewijziging moet expliciet worden vastgelegd en opnieuw getest; het toekomstige foutaandeel wordt hier niet alvast verlaagd.

## Value chain met zeven minuten herstel

| Schakel | Bij 5/5 | Bij 4/5 |
|---|---:|---:|
| Foutaandeel in het scenario | 0% | 20% |
| Verwachte herstelminuten per update | 0 | 0,20 × 7 = 1,4 minuten |
| Tooltijd inclusief controle en herstel | 15 minuten | 16,4 minuten gemiddeld |
| Winst per update tegenover 60 minuten | 45 minuten | 43,6 minuten gemiddeld |
| Winst per jaar, 40 updates | 30 uur | 29,07 uur (29 uur 4 minuten) |
| Persoonlijke waarde vóór toolkosten | €150 | €145,33 |

Bij 4/5 en 40 updates zijn er in dit scenario acht niet volledig geslaagde updates per jaar; 8 × 7 = **56 herstelminuten** worden bij de tien uur basis-tooltijd opgeteld. Dat geeft 10 uur 56 minuten met de tool tegenover 40 uur handmatig. Het is geen voorspelling van exact acht feitelijke fouten. Eén update die herstel nodig heeft duurt in dit scenario 22 minuten; 16,4 minuten is het gemiddelde over foutloze en herstelde updates.

## Toolkosten met gelijke scope

De nieuwe Sol-modeltest kost gemiddeld **$0,1739412 per extractie**, dus **$6,957648 voor 40 extracties**. Die meting sluit Excel en wisselkoersen uit; zie `modellen.md` en `kosten.md`. Dit bedrag wordt niet als volledige workflowkost bij de 15 minuten gebruikt en niet opgeteld bij de oude volledige-runmeting.

Voor een voorlopig nettoscenario met de bestaande volledige workflow gebruiken we het al vastgelegde AMZN-meetpunt van 15 oktober: **$0,2244944 per volledige agentrun**. Met de reeds opgeslagen historische koers van die datum, **€1 = $1,1208**, is dat **€0,2002983583 per update**, oftewel **€8,0119343323 bij 40 updates**. Dit is een expliciete scenarioaanname: één oudere volledige run als vervangende kost voor toekomstige updates, geen actuele wisselkoers, gemiddelde productieprijs of afzonderlijke Plus-factuur.

Daarmee is de voorlopige persoonlijke nettowaarde:

- Bij 5/5: **€141,99 per jaar** (€150 persoonlijke tijdwaarde − circa €8,01 toolkosten).
- Bij 4/5: **€137,32 per jaar** (€145,33 persoonlijke tijdwaarde − circa €8,01 toolkosten; gerekend vóór afronding).
- Voorlopig persoonlijk nettobereik: **€137,32–€141,99 per volledig jaar**, onder de vastgelegde aannames. Dit is geen gerealiseerde financiële opbrengst.

## Gevoeligheid voor de zwakste aanname

Bij de helft van het volume, **20 updates per jaar**, blijven de overige aannames gelijk:

| Schakel | Bij 5/5 | Bij 4/5 |
|---|---:|---:|
| Jaarlijkse tijdwinst | 15 uur | 14,53 uur (14 uur 32 minuten) |
| Persoonlijke waarde vóór toolkosten | €75 | €72,67 |
| Volledige toolkosten, oud meetpunt als scenario | €4,0059671662 | €4,0059671662 |
| Netto per jaar | **€70,99** | **€68,66** |

Zonder vaste kosten halveert dit persoonlijke nettoscenario bij halvering van het volume: het bereik wordt **€68,66–€70,99 per jaar**. Een eventueel vast abonnement wordt niet automatisch gehalveerd of bij het API-equivalent opgeteld.

Bij 40 updates verschuift de score van 5/5 naar 4/5 het netto met **€4,67 per jaar**. Halvering van het volume verschuift het netto bij gelijke score met **€68,66–€70,99 per jaar**. Onder deze aannames heeft de zwakste aanname, het aantal werkelijk uitgevoerde updates, dus veel meer invloed dan het waargenomen scoreverschil.

## Grenzen van het resultaat

De tijdschattingen, het jaarvolume, de persoonlijke uurwaarde en de representativiteit van de vijf testinputs zijn aannames. Herstelduur en kwaliteit na menselijke controle zijn nog niet gemeten. De volledige workflowkost gebruikt één historisch meetpunt en een historische koers. Als de student het handmatige werk zonder tool niet zou uitvoeren, is dit mogelijke tijdwinst tegenover een hypothetische werkwijze. Er is geen werkgeversuurkost verzonnen voor deze persoonlijke toepassing.
