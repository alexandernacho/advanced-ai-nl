# Modellen

## Mijn gok, geschreven vóór de runs (27 oktober 2026)

- **Welke setup scoort het best?** Opus 5.5. De moeilijke gevallen (zoals T03 en T08) vragen meer nadenken.
- **Valt het verschil binnen mijn foutmarge (9–10)?** Ik denk van wel.
- **Welke is goed genoeg voor mijn echte plek?** Haiku 5.5. Labelen in vijf klassen is een eenvoudige taak, Haiku scoort nu al 9–10, en hij is veel goedkoper.

## Resultaat, 27 oktober 2026

Prompt v3 (`build/prompt.md`), 10 inputs uit `build/test-set.md`, 1 run per setup, elke run in een aparte sessie: `claude -p --model <model> [--effort medium] --tools "" --no-session-persistence`. Verwachte antwoorden niet aangepast. Mijn foutmarge uit `build/foutmarge.md` is 9–10 (Haiku 5.5, 3 runs per versie).

| Setup | Model | Effort | Score (n = 10, 1 run) | Binnen mijn foutmarge? | Input-tokens per run (gemeten) | Output-tokens per run | Kost per run | Per jaar (7.200 runs, oud) | Per jaar (1.100 runs, gecorrigeerd in week 5) |
|---|---|---|---:|---|---:|---:|---:|---:|---:|
| A | Claude Sonnet 5.5 | medium | 8/10 | Nee, 1 punt onder het minimum van 9 | 6.120 | 83,8 | $0,00604 (€0,00544) | $43,47 (€39,13) | $6,64 (€5,98) |
| B | Claude Haiku 5.5 | standaard (niet ingesteld) | 10/10 | Ja | 5.334 | 319,4 | $0,00042 (€0,00038) | $3,02 (€2,72) | $0,46 (€0,42) |
| C | Claude Opus 5.5 | standaard (niet ingesteld) | 10/10 | Ja | 4.506 | 154,0 | $0,01348 (€0,01213) | $97,06 (€87,35) | $14,83 (€13,35) |

**Fouten:**
- A (Sonnet): T01 neutraal (juist onzeker), T02 onzeker (juist negatief).
- B en C: geen fouten.
- T03 en T08 gingen in alle drie de setups juist.

**Hoe ik de kost rekende:**
- Prijzen per miljoen tokens uit `cursus/week-05/README.md`: Sonnet 5.5 $2 in / $10 uit, Haiku 5.5 $0,10 / $0,50, Opus 5.5 $4 / $20. Niet met `/cost`.
- Input: mijn deel uit week 4, 2.600 tokens, voor elke setup gelijk. De gemeten input in de tabel is hoger, omdat `claude -p` ook een systeemprompt meestuurt (niet het jouwe deel).
- Output: het gemiddelde van deze setup over de 10 runs, inclusief denktokens.
- Voorbeeld B: 2.600 × $0,10 + 319,4 × $0,50 = $420 per miljoen runs = $0,00042 per run.
- Per jaar: 7.200 runs (600 per maand, uit `build/kosten.md`). 1 dollar = 0,90 euro (aanname, zoals in `build/kosten.md`).
- Gecorrigeerd in week 5: mijn volume is 5 berichten per werkdag, dus 1.100 runs per jaar (zie `build/kosten.md`). De kolom met 7.200 runs blijft staan. Voorbeeld B: 1.100 × $0,00042 = $0,46 per jaar. De conclusie verandert niet: bij gelijke score is Haiku 5.5 het goedkoopst.

**Zwakke punten:**
- 1 run per setup, n = 10. Eén fout is 10 procentpunt. Sonnet's 8 had ook toeval kunnen zijn: mijn foutmarge komt van Haiku, niet van Sonnet.
- Haiku gaf gemiddeld 319 output-tokens, meer dan Sonnet (84) en Opus (154). Hij denkt dus langer, en dat betaal je als output. Zijn week 4-meting gaf 1,2k, uit een run in Claude Code.
- Effort van B en C heb ik niet ingesteld. Ik weet niet welke standaard ze gebruiken.

## Klopte mijn gok?

- **"Opus 5.5 scoort het best": half.** Opus haalde 10/10, maar Haiku ook. Opus scoort dus gelijk met Haiku, niet beter. Sonnet scoorde het laagst.
- **"De moeilijke gevallen (T03, T08) vragen meer nadenken": niet te zien.** Alle drie de setups hadden T03 en T08 juist. De twee fouten van Sonnet zaten op T01 en T02.
- **"Het verschil valt binnen mijn foutmarge": voor Opus en Haiku wel (beide 10). Voor Sonnet niet (8, onder 9–10).**
- **"Haiku 5.5 is goed genoeg voor mijn echte plek": ja.** 10/10, binnen de foutmarge, en $3,02 per jaar tegen $97,06 voor Opus: ongeveer 32 keer goedkoper bij gelijke score.
