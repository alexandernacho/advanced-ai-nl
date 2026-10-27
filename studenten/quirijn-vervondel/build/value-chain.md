# Value chain, 27 oktober 2026

Alle bedragen per jaar, bij 10 plaatsbezoeken per maand (120 per jaar). Midden van de foutmarge v1: 78,5 van 96 onderdelen, dus 18,2% fout.

| Schakel | Waarde | Bron |
|---|---|---|
| 1. Met de hand | 2 u = 120 min per plaatsbezoek. Het uitschrijven en het rondgaan zijn niet apart gemeten. Aanname: 2 u totaal. | Week 4 post, schatting |
| 2. Met de tool | Draaien 16 s (0,27 min) + nakijken 5 min + fouten herstellen 21,9 min (18,2% × 120 min). Samen 27,1 min. | Week 4 post (draaien en nakijken). Fout uit foutmarge v1, midden 78,5 van 96 |
| 3. Winst per taak | 120 − 27,1 = 92,9 min per plaatsbezoek (ongeveer 1 u 33 min) | Berekend |
| 4. Volume | 10 per maand, 120 per jaar | Aanname, kosten.md: "ongeveer 10 plaatsbezoeken per maand, volgens mij" |
| 5. Uren per jaar | 92,9 min × 120 = 185,7 u per jaar | Berekend |
| 6. Uurkost | €30 per uur voor de werkgever (€20 bruto × 1,5) | Aanname, bron Acerta/Securex. Week 4 rekende met €40 per uur, zonder uitleg over bruto en werkgever |
| 7. Kost van de tool | €3,18 per jaar (Opus 5.5, 120 runs) | build/modellen.md |
| 8. Netto per jaar | 185,7 u × €30 = €5.572 − €3,18 = **€5.568** | Berekend |
| 9. Bereik | Score 77 van 96: €5.456. Score 80 van 96: €5.681. | Berekend met de grenzen van foutmarge v1 |
| 10. Zwakste cijfer | Handtijd (2 u). Is die 1 u, dan is het netto €2.625. | Berekend, zie hieronder |

## Handtijd uitgesplitst

De 120 minuten van schakel 1 splits ik in vier stappen. Bron: geschat door mij, niet gemeten.

| Stap | Minuten |
|---|---:|
| Notities van het plaatsbezoek teruglezen | 15 |
| Lengtes koelleiding, communicatiekabel en voedingskabel berekenen | 40 |
| Bochten, tussenstukken, beugels en kabelgoten tellen | 35 |
| Lijst uittypen en nakijken | 30 |
| **Totaal** | **120** |

Het totaal is gelijk aan de 2 uur die in de rest van deze tabel staat, dus de cijfers hierboven veranderen niet.

## Extra regel: met Opus (87 van 96, één run)

Fout 9,4%, herstellen 11,3 min, tool in totaal 16,5 min, winst 103,5 min per plaatsbezoek. Netto per jaar: **€6.206**. Dit is één run. De kost van de tool is hetzelfde (€3,18).

## Zwakste cijfer

Het zwakste cijfer is de handtijd: 2 u per plaatsbezoek, een schatting en niet gesplitst. Als die de helft is (1 u), dan:

- Herstellen: 10,9 min.
- Tool in totaal: 16,2 min. Winst: 43,8 min per plaatsbezoek.
- Netto per jaar: **€2.625**. Dat is €2.944 minder dan €5.568.

De foutmarge geeft een bereik van €5.456 tot €5.681, een spreiding van €225. De handtijd beweegt het netto dus ruim 13 keer zoveel als de foutmarge. Het handwerk bepaalt het resultaat meer dan de score.

## Aannames

- Handtijd 2 u per plaatsbezoek: schatting uit week 4, nog niet gemeten. De vier stappen zijn ook geschat door mij, niet gemeten.
- Nakijken 5 min per plaatsbezoek: schatting uit week 4.
- Uurkost €30: bruto €20 × 1,5. Met de €40 uit week 4 zou het netto €7.425 zijn.
- 10 plaatsbezoeken per maand: schatting uit kosten.md.
