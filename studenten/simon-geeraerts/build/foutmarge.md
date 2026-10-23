# Foutmargetest — 22 oktober 2026

Model: `gpt-6-luna`. n = 13 testgevallen, 3 runs per promptversie. Dezelfde inputs voor beide versies.

Ik testte de huidige prompt uit `build/prompt.md` tegen de vorige instructies uit `build/server.mjs` van vóór commit `ae38b15`.

| Versie | Run 1 | Run 2 | Run 3 | Foutmarge (min–max) |
| --- | ---: | ---: | ---: | ---: |
| Vorige prompt | 13/13 | 12/13 | 13/13 | 12–13/13 |
| Huidige prompt | 12/13 | 13/13 | 13/13 | 12–13/13 |

## Werkwijze

- 78 aparte `codex exec`-sessies: 13 testgevallen × 3 runs × 2 promptversies.
- Elke sessie kreeg alleen de betrokken prompt, klantvraag en bestelgegevens; nooit het verwachte antwoord uit de testset.
- Er draaiden maximaal vier sessies tegelijk en er waren geen tools beschikbaar voor het model.
- Ik beoordeelde elk antwoord tegenover het vooraf ingevulde verwachte antwoord in `build/test-set.md`: juiste taal, juiste wagen/status/datum waar beschikbaar, geen verzonnen informatie en veilig reageren bij ontbrekende of foutieve bestelgegevens.

## Twee fouten

- Huidige prompt, run 1, test 4: het antwoord vroeg wel om een bestelbonnummer, maar vermeldde niet dat het uit vijf cijfers moet bestaan en vroeg niet naar de naam. Daarom 12/13.
- Vorige prompt, run 2, test 13: op een Engelse klantvraag antwoordde het model in het Nederlands. Daarom 12/13.

## Conclusie

De bereiken overlappen volledig: beide promptversies scoren 12–13/13. De huidige prompt is dus **niet aantoonbaar beter** dan de vorige. Een eerdere claim dat de huidige prompt beter werd, is met deze foutmargetest **niet bewezen en wordt ingetrokken**.

Test 4, 7 en 8 worden in de echte website al door de server afgehandeld vóór een modelantwoord. Ze bleven toch in deze run omdat ze in de vaste testset staan; voor een latere eind-tot-eindtest moet ik ook die serverstap apart testen.
