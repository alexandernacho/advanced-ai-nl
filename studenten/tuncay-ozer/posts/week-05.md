# Week 5 — Eén input verschil

## Mijn foutmarge
Ik draaide mijn vorige versie (v1, zonder de regel voor `A x B`) en mijn laatste versie (v2, met die regel) elk 3 keer op dezelfde tien inputs, met Claude Haiku 5.5. Elke run was een nieuwe sessie zonder tools.

v1 scoorde 7, 9 en 8 op 10: een bereik van 7–9. v2 scoorde drie keer 9 op 10: een bereik van 9–9 (n = 10, 3 runs).

Mijn claim uit week 3 was: "De regel voor `12X12` lost T10 op." Voor de totale score is die claim ingetrokken. De laagste score van v2 (9) ligt niet hoger dan de hoogste van v1 (9), dus de bereiken raken elkaar. Op T10 alleen werkte de regel wel: van 0 op 3 naar 3 op 3. T02 (`5km 36min`) blijft mijn zwakke plek: 1 keer juist op 6 runs.

## Model en effort
Mijn gok vooraf: Opus scoort het best, omdat het het slimste model is. Sonnet vond ik goed genoeg voor de prijs.

Ik draaide drie setups op mijn laatste prompt, effort medium, 1 run op tien inputs:

| Setup | Score | Kost per run | Per jaar |
|---|---:|---:|---:|
| Sonnet 5.5 | 10/10 | $0,0051 | ± €1,22 |
| Haiku 5.5 | 9/10 | $0,0005 | ± €0,12 |
| Opus 5.5 | 9/10 | $0,0122 | ± €2,89 |

Mijn gok over Opus klopte niet. Haiku miste weer T02. Opus zette bij T06 geen notitie, maar dat staat eigenlijk zo in mijn prompt. Dat moet ik later rechtzetten in mijn prompt of mijn testset.

Het verschil is telkens één input. Haiku en Opus vallen binnen mijn foutmarge, Sonnet net erboven, maar met maar 1 run. Ik kies Sonnet 5.5, effort medium, omdat Sonnet alles juist had en bijna 2× goedkoper is dan Opus.

## Mijn value chain, met de foutmarge erin
Met de hand kost een training mij 145 s: Excel openen en 4,5 oefeningen invullen. Met de tool is het 43 s, plus fouten herstellen: bij 9/10 is dat 10% × 145 s = 14,5 s. De winst is 87,5 s per training bij 9/10, en 102 s bij 10/10.

Ik train gemiddeld 4 keer per week, 208 keer per jaar. Dat is 5,1 tot 5,9 uur per jaar. Aan €16 per uur (mijn uurloon) en min €0,95 voor Sonnet blijft er netto €80 tot €93 per jaar over. Met de regel bruto × 1,5 (€24) zou het €120 tot €140 zijn, maar dat is wat een werkgever betaalt, en deze tool gebruik ik in mijn eigen tijd.

Mijn zwakste cijfer is de tijd met de hand. Beide getallen zijn geschat, maar mijn aantal trainingen ken ik beter. Is de tijd met de hand de helft, dan zakt mijn netto naar €20 tot €26. Dat beweegt meer dan mijn foutmarge (± €13).

## Mijn dashboard
https://claude.ai/artifact/JcrkkxWZyUzz6b66yMiVm3

Kijk eerst naar de vier cijfers bovenaan: score, netto per jaar, kost per run en mijn claim.

## Mijn AI-ismen
1. Week 2: "Het is belangrijk dat ik de reps en het gewicht zeker zie, aangezien ik mijn progressie wil tracken."
   Herschreven: "Ik noteer per oefening de reps en het gewicht, zodat ik elke week kan vergelijken."
2. Week 3: "Het gewicht is een van de belangrijkste dingen om je progressie te volgen."
   Herschreven: "Aan het gewicht zie ik mijn progressie het duidelijkst: incline dumbbell press van 32 kg in week 1 naar 36 kg nu."
3. Week 3: "Dat is een verwachting, geen meting."
   Herschreven: "Dat heb ik nog niet gemeten, het is een schatting."
4. Week 3: "Geen enkele regel die er nu in staat, is een garantie dat alles werkt."
   Herschreven: "Mijn regels lossen niet alles op: mijn loopbericht `5km 36min` herkende hij maar 1 keer op 6 runs."
5. Week 4: "Maar tijd is niet het belangrijkste."
   Herschreven: "Belangrijker dan de tijd: ongeveer de helft van mijn trainingen komt nu nooit in mijn Excel."
