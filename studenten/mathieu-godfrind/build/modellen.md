## Mijn gok (voor ik iets draaide)
1. Best op mijn 13 pagina's: Opus, want dat is het slimste model.
2. Goed genoeg voor Vinted: Haiku, want het is goedkoop en een fout kost mij max 60 euro.

## Resultaten (13 inputs, 1 run per setup, huidige prompt v3)

| Setup | Model | Effort | Score (n = 13) | Fouten | Binnen foutmarge? |
|---|---|---|---:|---|---|
| A | claude-sonnet-5-5 | medium | 10/13 | T05 (NO-GO, B; juist ONZEKER), T06 (NO-GO, C; juist GO), T11 (GO; juist NO-GO, A) | Nee: 10 ligt onder 12–12 van v3 |
| B | claude-haiku-5-5 | standaard | 12/13 | T05 (NO-GO, B; juist ONZEKER) | Ja |
| C | claude-opus-5-5 | standaard | 12/13 | T05 (NO-GO, B; juist ONZEKER) | Ja |

Het bereik 12–12 komt uit de foutmarge van v3 (3 runs). Setups A, B en C hebben elk maar één run.

- **Geen F2:** alle citaten in de 39 antwoorden staan letterlijk op de pagina.
- **Geen F3:** geen enkel verwacht risico is gemist.
- **T05 gaat in alle drie fout:** juist is ONZEKER, alle setups zeggen NO-GO (B). Dat is hetzelfde patroon als in de foutmarge van v3.
- **A, T07:** naast het juiste risico D staat een risico B dat het model zelf ongeldig noemt ("dus dit is geen geldig risico"). Het is geen fout volgens de testset, maar wel opvallend. Het staat zo in `build/runs-modellen/A-T07.txt`.
- **Kost en output-tokens:** niet gemeten. De uitvoer van `claude -p` gaf die niet mee, dus die kolommen laat ik leeg.
- **Vergelijking met de gok:** Opus scoort gelijk aan Haiku (beide 12/13). Op score is Opus dus niet beter op deze 13 pagina's.

Ruwe antwoorden staan in `build/runs-modellen/`. Ik heb niets gecommit.

## Mijn gok vs de uitkomst
1. Opus best: klopt niet. Opus had 12 op 13, net als Haiku. Niet beter dus.
2. Haiku goed genoeg: klopt. Zelfde score als Opus en het goedkoopste.
Sonnet deed het slechtst (10 op 13), dat had ik niet verwacht.
Let op: elk model maar 1 run, dus dit is geen bewijs.
