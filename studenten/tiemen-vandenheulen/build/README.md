# Review-sorteerder voor evenementen

## De taak

De tool geeft aan een korte bezoekersreview één of meer vaste categorieën, zodat een evenementorganisator sneller terugkerende thema's ziet.

## De categorieën

`organisatie`, `prijs`, `sfeer`, `locatie`, `wachttijden`, `catering`, `veiligheid` en, wanneer niets past, `andere`.

## De uitvoer

De tool antwoordt met JSON: een lijst met labels en een korte reden die naar de review verwijst.

## Zo test je

1. Start voor elke review een nieuw, tijdelijk gesprek zonder web search.
2. Plak `prompt.md` en vervang de placeholder onder **Review** door één input uit `test-set.md`.
3. Vergelijk de labels met jouw vooraf geschreven juiste antwoord.
4. Noteer het resultaat en eventuele fout in `log.md`.

## Versies

| Versie | Datum | Wat veranderde | Waarom |
|---|---|---|---|
| v1 | 7 oktober 2026 | Eerste prompt met acht labels | Eerste testbare versie |
| v2 | 7 oktober 2026 | `andere` mag niet samen met een ander label voorkomen | Review 8 gaf onterecht zowel `sfeer` als `andere`. |
