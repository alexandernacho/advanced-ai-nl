# Modeltest — week 5

## Mijn gok vooraf

Mijn verwachting was dat lage effort voldoende zou zijn. Deze taak heeft vier vaste labels en korte input; meer reasoning lijkt waarschijnlijk weinig extra waarde te geven.

## Gevraagde modelopstellingen

De opdracht noemt Sonnet, Haiku en Opus. Deze namen waren niet beschikbaar als uitvoerbare modellen in mijn lokale Codex-runner. Ik verzin daarom geen scores of prijzen voor die drie modellen. De werkelijk gemeten opstellingen staan hieronder.

| Gevraagde setup | Score | Kost | Status |
| --- | ---: | ---: | --- |
| Sonnet | — | — | niet beschikbaar in deze runner |
| Haiku | — | — | niet beschikbaar in deze runner |
| Opus | — | — | niet beschikbaar in deze runner |

## Werkelijk gemeten setups

| Setup | Model | Effort | Score (n = 10, 1 run) | Kost/run (benadering) |
| --- | --- | ---: | ---: | ---: |
| A standaard | `gpt-5.6-luna` | medium | 8/10 | ± €0,00080 |
| B omlaag | `gpt-5.6-luna` | low | 9/10 | ± €0,00080 |
| C omhoog | `gpt-5.6-luna` | high | 8/10 | ± €0,00080 |

Alle drie gemeten Codex-setups vielen binnen de foutmarge 7–9/10. Ik kies voorlopig low effort. De nieuwe set v2 scoorde daarna 19/30 met één low-effort run; die score is niet achteraf gebruikt om de prompt aan te passen.
