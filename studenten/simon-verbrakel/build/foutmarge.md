# Foutmarge, 27 oktober 2026

Model: Claude Haiku 5.5 (`claude-haiku-5-5`), hetzelfde model als mijn testset. n = 10 inputs (T01 tot T10), 3 runs per versie. Zelfde inputs voor beide.

| Versie | Run 1 | Run 2 | Run 3 | Foutmarge (min–max) |
|---|---:|---:|---:|---:|
| v1 (prompt van week 2, git `c6297f3`) | 9/10 | 10/10 | 9/10 | 9–10 |
| v3 (laatste prompt, `build/prompt.md`) | 9/10 | 9/10 | 10/10 | 9–10 |

De laatste prompt heeft in het bestand nog de titel "Prompt v1". Hier noem ik hem v3, zoals in `build/kosten.md`.

Mijn claim: "Opvallend: T03 ging in week 2 nog fout en is nu twee keer juist. Dat komt volgens mij door de vijf voorbeelden die ik in week 3 aan mijn prompt toevoegde, maar ik heb dat niet apart getest." (week 4). In week 3 schreef ik over de nieuwe regel voor gesprekken zonder akkoord: "De regel helpt een beetje, maar niet altijd."

Bevestigd of ingetrokken: **ingetrokken**, want de bereiken overlappen (v1 9–10, v3 9–10). De laagste score van v3 (9) ligt niet hoger dan de hoogste score van v1 (10). Het verschil valt binnen de foutmarge. Mijn verbetering is niet bewezen. Ze is niet slechter, ik kan het gewoon niet zeggen.

## Welke inputs fout gingen

| Run | Input | Model zei | Juist |
|---|---|---|---|
| v1 run 1 | T01 | neutraal | onzeker |
| v1 run 3 | T09 | onzeker | positief |
| v3 run 1 | T03 | onzeker | neutraal |
| v3 run 2 | T06 | onzeker | positief |

- Elke fout komt in maar één van de drie runs voor. Het is telkens een andere input per run, dus de fouten zijn wisselend (F6) en geen vast gat in de prompt.
- T03 was in mijn claim het bewijs voor de voorbeelden. v3 had T03 in 2 van 3 runs juist, en v1 in 3 van 3. Mijn claim klopt dus ook niet op die ene input.
- T08 (de regel over gesprekken zonder akkoord) was in alle 6 runs onzeker, ook bij v1, die de regel niet heeft.

## Hoe ik het gedaan heb

- Elke run in een nieuwe sessie met alleen de prompt en één input, zonder tools: `claude -p --tools "" --model claude-haiku-5-5 --no-session-persistence`. 60 runs, parallel.
- Het model kreeg nooit de verwachte antwoorden. Ik heb ze niet aangepast.
- De prompt van v1 komt uit git (commit `c6297f3`), want in `build/` staat alleen de laatste versie.

## Let op

- Mijn eerdere runs (week 2 tot 4) draaiden in Claude Code, met zijn eigen context (26,8k tokens). Deze 60 draaiden kaal. Dat kan verschillen verklaren, bijvoorbeeld dat T08 hier steeds onzeker is en in week 3 nog negatief.
- v1 scoort hier 9–10, terwijl mijn week 2-cijfer 2 op 5 was. Dat cijfer was met een kleinere testset en andere inputs, dus niet te vergelijken.
- n = 10 is weinig. Eén fout is 10 procentpunt.
- De agent heeft de antwoorden vergeleken met `build/test-set.md` en zeven ruwe antwoorden nagelezen (de vier fouten en drie keer T08): de beoordeling klopte. Ik heb zelf twee ruwe antwoorden nagekeken, T03 (v3 run 1) en T08 (v3 run 1), en ben het eens met de beoordeling.
