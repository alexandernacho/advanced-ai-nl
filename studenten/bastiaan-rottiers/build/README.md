# Canvas-assistent voor WATTZAK

## De taak

De tool maakt van één Canvas-opdracht, bijhorende documenten, beoordelingscriteria en lesnotities een voorbereidingskaart voor de bachelorproefgroep achter WATTZAK.

## De uitvoer

De voorbereidingskaart bevat wat de groep moet opleveren, concrete stappen in een logische volgorde, deadline, inleverwijze, beoordelingscriteria en een agenda-voorstel. Alleen datums die in de bronnen staan worden vermeld; ontbrekende of dubbelzinnige informatie krijgt het label `onzeker`.

## Zo test ik

1. Open een nieuw gesprek met een AI.
2. Plak `prompt.md` en vul één Canvas-opdracht in.
3. Vergelijk elk veld met het vooraf bepaalde juiste antwoord in `test-set.md`.
4. Noteer de run en eventuele fout in `log.md`.

## Versies

| Versie | Datum | Wat veranderde | Waarom |
|---|---|---|---|
| v1 | 2026-10-07 | Eerste prompt opgesteld | Eerste testbare context |
| v2 | 2026-10-09 | Verbod op niet-onderbouwde informatie toegevoegd | T01 verzon prototype- en gadgetdetails (F2) |
| v3 | 2026-10-09 | Expliciete voorwaarden onder beoordelingscriteria toegevoegd | T06 miste een expliciet criterium |
| v4 | 2026-10-09 | Korte vergelijkingsvorm voor documenten toegevoegd | T09 was te lang en niet per onderdeel bruikbaar (F4) |
| v5 | 2026-10-09 | Vergelijkingsvorm beperkt tot expliciete documentvergelijkingen | De korte vorm mag gewone Canvas-opdrachten niet veranderen |
| v6 | 2026-10-20 | Regels voor aantallen, deadline, inleverwijze en status toegevoegd | T06–T08 hadden fouten rond die vier onderdelen |
| v7 | 2026-10-20 | Statusregel voor voortgangsvergelijkingen verduidelijkt | T10 had duidelijke vervolgstappen maar gaf ten onrechte `onzeker` |
