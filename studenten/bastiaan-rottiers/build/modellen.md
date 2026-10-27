# Modeltest, 27 oktober 2026

Testset: **set v1**, vaste deelset T06–T10 uit de oorspronkelijke tien. De scores hieronder zijn geen set-v2-resultaten.

## Gok vóór de runs

Mijn gok vóór de modeltest: **C, GPT-6 Astra medium, scoort het best. B, GPT-6 Luna low, is goed genoeg voor mijn eigen gebruik.** Vastgelegd op 27 oktober 2026, vóór de modeltest.

## Vastgelegd testplan

n = 5, T06–T10, één nieuwe sessie per input en setup. Laatste prompt: v7. Volledige documenttekst bij T09 en T10. Geen verwachte antwoorden naar het geteste model. Beoordeling achteraf op de bestaande testset, zonder die te wijzigen.

| Setup | Model | Effort | Score /5 | Binnen foutmarge? | Gemiddelde outputtokens per taak | Kost per taak | Per jaar (96 taken) |
|---|---|---|---|---|---|---|---|
| A | GPT-6.1 Sol | medium | 4/5 | Ja, binnen v7: 3–4/5 | 347,2 | €0,048636 | €4,669056 |
| B | GPT-6 Luna | low | 2/5 | Nee, onder v7: 3–4/5 | 323,4 | €0,00242109 | €0,23242464 |
| C | GPT-6 Astra | medium | 4/5 | Ja, binnen v7: 3–4/5 | 316,6 | €0,241803 | €23,213088 |

A versus B verandert model én effort. Dit meet een goedkopere setup; het afzonderlijke effect van effort kan daarmee niet worden vastgesteld.

De effort van de historische week-4-runs is niet opgeslagen. Voor alle foutmargeruns wordt medium vastgezet; dit is dus een nieuwe gecontroleerde meting, geen exacte reproductie van de historische sessie-instellingen.

## Beoordeling

| Input | A: Sol medium | B: Luna low | C: Astra medium | Reden |
|---|---|---|---|---|
| T06 | juist | juist | juist | Ieder groepslid, twee events, criteria, deadline en onzekere inleverwijze behouden. |
| T07 | juist | fout | juist | Luna mist de vastgelegde datum en de stappen invullen/indienen, en eindigt met onzeker. Sol en Astra nemen de datum over. |
| T08 | fout | fout | fout | De vooraf vastgelegde antwoordkolom verlangt Sustainable Business Canvas; alle drie antwoorden spreken over BMC. Deze beperking van de testset staat in foutmarge.md. Luna mist bovendien de concrete Canvas-datum. |
| T09 | juist | juist | juist | De hoofdstukken krijgen een status en volgende stap. Luna neemt meer eisen uit de leidraad over en is duidelijk langer; de vereiste inhoud is wel aanwezig. |
| T10 | juist | fout | juist | Luna geeft alleen onzekere voorbereidingsvelden en geen overzicht per bouwsteen. Sol en Astra analyseren de bouwstenen en eindigen met nog in te plannen. |

Dezelfde beoordelingswijze als bij de foutmargetest. De verwachte antwoorden zijn niet gewijzigd. Er zijn vijftien afzonderlijke nieuwe antwoorden gegenereerd, geen antwoorden uit Lus 1 hergebruikt. De ruwe uitvoer blijft lokaal; de tokenmetingen staan in `modelmetingen-week-05.csv`.

## Berekening van de vergelijkingstabel

Volgens de lesformule is de input voor alle setups gelijkgezet op **25.284 inputtokens** uit de week-4-raming. Dat getal was toen een aanname (98% van 25.800), geen afzonderlijke inputmeting. De nieuwe outputtokens zijn wel rechtstreeks uit de vijf CLI-runs per setup gemeten. De tabelkosten zijn daarom een gestandaardiseerde API-raming, geen werkelijk gefactureerde kosten of zuivere meting van alleen de taakprompt.

`kost in euro = (25.284 × inputprijs + gemiddelde outputtokens × outputprijs) / 1.000.000 × 0,90`

Jaarvolume: 8 taken per maand × 12 = 96 taken. $1 = €0,90 is de bestaande rekenaanname uit week 4, geen actuele wisselkoersmeting.

| Model | Input / miljoen (USD) | Output / miljoen (USD) | Cache lezen / miljoen (USD) |
|---|---:|---:|---:|
| GPT-6.1 Sol | 2 | 10 | 0,10 |
| GPT-6 Luna | 0,10 | 0,50 | 0,01 |
| GPT-6 Astra | 10 | 50 | 1 |

Bron: [OpenAI API-prijzen](https://developers.openai.com/api/docs/pricing), geraadpleegd op 27 oktober 2026, standaardtarief. Voor een begroting met de werkelijk gemeten gemiddelde input en de waargenomen caching: zie `kosten.md`.

## Wat kwam eruit?

Astra scoort even hoog als Sol, niet hoger. Het verschil tussen deze twee setups is op deze beperkte test niet aantoonbaar; Astra kost in de gestandaardiseerde vergelijking ongeveer vijf keer zoveel. Luna is veel goedkoper, maar de score 2/5 valt onder het geobserveerde v7-bereik van 3–4/5.

De gok dat Astra het best scoort is alleen als gedeelde eerste plaats uitgekomen; de gok dat Luna low goed genoeg is, wordt door deze test niet ondersteund. Eén ronde per setup is geen eigen foutmargetest voor Luna of Astra.

Mijn keuze: **Sol medium**, vastgelegd na de vergelijking op 27 oktober 2026. Sol haalt dezelfde score als Astra tegen een lagere kost; Luna scoort onder het geobserveerde v7-bereik. Voor de nieuwe toepassing op financieel plan en marktonderzoek zijn aparte praktijkgevallen nodig; de huidige vergelijking betreft v7 op T06–T10.
