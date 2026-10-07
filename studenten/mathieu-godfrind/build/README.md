# Leveranciersproduct screenen voor bol.com

## De taak

De tool checkt één productpagina van een leverancier (bv. Alibaba) en zegt of het product veilig in te kopen is om door te verkopen op bol.com.

## De labels

| Label | Betekent |
|---|---|
| `GO` | Geen enkel risico gevonden |
| `NO-GO` | Minstens één risico gevonden, met een citaat van de pagina |
| `ONZEKER` | De pagina geeft te weinig info om te weten wat het product is |

## De risico's

| Letter | Risico |
|---|---|
| A | Namaak of merkrecht |
| B | Wettelijke eisen (bv. geen CE waar dat verplicht is) |
| C | Moeilijk te verzenden (breekbaar, groot, vloeistof, losse batterijen) |
| D | Verboden of beperkt op bol.com |

## Waarom `ONZEKER`?

Een model zonder uitweg gokt. Het kiest dan toch `GO` of `NO-GO`, en het klinkt zeker. Met `ONZEKER` mag het zeggen: dit weet ik niet. Dan kijk ik zelf.

## De uitvoer

```
OORDEEL: NO-GO
RISICO'S:
- B: "Certification: RoHS" — Elektronica met een batterij, CE niet vermeld.
UITLEG: <één zin>
```

Het label is juist of fout, en elk citaat staat op de pagina of niet. Twee mensen kunnen dat los van elkaar beslissen. Daarom is het meetbaar.

## Zo draai je het

1. Open een nieuw, tijdelijk gesprek (zonder geheugen, zonder web search).
2. Plak de prompt uit `prompt.md`. Plak onderaan de tekst van één productpagina.
3. Lees het oordeel. Vergelijk met `test-set.md`. Check of elk citaat echt op de pagina staat.
4. Doe elke pagina twee keer, telkens in een nieuw gesprek.
5. Schrijf het resultaat in `log.md`.

## Versies

| Versie | Datum | Wat veranderde | Waarom |
|---|---|---|---|
| v1 | 2026-09-30 | Eerste prompt met vier risico's en drie labels | |
| v2 | 2026-10-07 | Vier voorbeelden, citatenregel voor CE aangepast, regel B met een "want". Na de buurtest: beslisregel 4, speelgoedregel, "want" bij beslisregel 3 | Audit: bouwsteen 4 ontbrak. Buurtest: 0 op 3 gelijk |
