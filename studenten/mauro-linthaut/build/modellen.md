# Modeltest, 21 oktober 2026

## Mijn gok

Ik denk dat alle drie de modellen op 9 van de 10 KID's volledig juist uitkomen.

Uitkomst: Sonnet 10/10, Haiku 9/10, Opus 10/10. Haiku zat er precies op. Sonnet en Opus deden het één KID beter dan mijn gok. De resultaten hieronder zijn niet aangepast aan de gok.

## Resultaat

Prompt: v1.2 (`build/prompt.md` zoals nu). Inputs: T01 tot T10 uit `build/test-set.md`, de pdf's in `build/kid/` uitgelezen met `pdftotext -enc UTF-8`. Verwachte antwoorden: kolom "Juiste antwoord", niet aangepast. Score met `build/foutmarge-runs/score.py`, hetzelfde script als bij de foutmargetest. Claude Code 2.1.306. Eén run per input, 10 runs per setup, elk in een nieuwe sessie in een lege map.

Opdracht per run: `claude -p --model <model> --effort medium --tools "" --output-format json --no-session-persistence --disable-slash-commands --strict-mcp-config --setting-sources ""`. Het niveau `medium` is voor alle drie gebruikt en bevestigd.

| Setup | Model | Niveau | Score (velden) | KID's volledig juist | Gem. input-tokens per run | Gem. output-tokens per run | Kost per run | Kost per jaar (72 runs) |
|---|---|---|---:|---:|---:|---:|---:|---:|
| A | Sonnet 5.5 (`claude-sonnet-5-5`) | medium | 80/80 | 10/10 | 12.953 | 1.440 | $0,0403 = ± €0,036 | ± €2,61 |
| B | Haiku 5.5 (`claude-haiku-5-5`) | medium | 79/80 | 9/10 | 13.777 | 4.021 | $0,0034 = ± €0,0031 | ± €0,22 |
| C | Opus 5.5 (`claude-opus-5-5`) | medium | 80/80 | 10/10 | 12.950 | 1.414 | $0,0801 = ± €0,072 | ± €5,19 |

Setup A tot C zijn mijn labels: je gaf geen letters bij de modellen.

**Hoe de kost is berekend:** input-tokens × inputprijs plus output-tokens × outputprijs, per miljoen tokens (README week 5, 21 oktober 2026): Sonnet 2 / 10 dollar, Haiku 5.5 0,10 / 0,50, Opus 4 / 20. Input = `input_tokens` plus `cache_creation_input_tokens` uit de uitvoer van de run (de prompt met het KID erin), tegen de gewone inputprijs. De 649 tokens `cache_read` zijn Claude Code zelf en tellen niet mee. 1 dollar = €0,90. Volume: 72 per jaar (`scenario.md`).

De dollars uit de uitvoer (`total_cost_usd`: $0,066 / $0,0048 / $0,132 per run) wijken hiervan af, onder meer door het cache-toeslagtarief. Haiku 5.5 kent Claude Code nog niet, zie de README. Ik reken daarom zelf, niet met die dollars.

## Wat opvalt

- **Enige fout:** Haiku bij T04 (L&G Artificial Intelligence, FR). Scenario "1.300 USD en -33,5% per jaar" in plaats van 13.600 USD en 6,3%. Dat is dezelfde scenariofout (verschoven rij in de uitgelezen pdf-tekst) als in week 3. De andere 7 velden van T04 waren juist.
- **Output-tokens:** de teller uit `usage.output_tokens` omvat vermoedelijk ook het redeneren van het model, niet alleen de acht regels. Haiku gebruikte ruim het dubbele van de andere twee. Of dat aan het redeneren ligt, heb ik niet nagekeken.
- **Kosten:** zie de tabel. Op 72 runs per jaar is het verschil tussen de setups ± €5 per jaar, klein tegenover de waarde van ± €150 tot ± €175 (zie `kosten.md`).
- **Hoe zeker dit is:** één run per input. Bij v1.2 schommelde de score tussen 79 en 80 (zie `foutmarge.md`), dus 80 tegenover 79 hier is geen bewezen verschil. Alleen de fout bij Haiku is zeker een echte fout, maar of Haiku die vaker maakt, weet ik pas met meer runs.
- Ruwe antwoorden: `C:\Users\mauro\AppData\Local\Temp\claude\C--Users-mauro\8b759b07-43db-464f-80ff-adbdabe581f2\scratchpad\out\` (`<model>_<ID>.json`). Het zijn tijdelijke bestanden, buiten je repo.
