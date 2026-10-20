# Kosten

Gemeten op 20 oktober 2026, met T01 en prompt v3 (toen zonder de regel over gesprekken zonder akkoord) in een lege sessie. Model: **Claude Haiku 5.5**, niet 4.5.

## Meting

| Wat | Waarde |
|---|---|
| Context (`/context` vóór de run) | 26,8k tokens (systeemprompt 3,7k, tools 17,3k, skills 5,9k) |
| `/cost` na de run | totaal $0,0044 |
| Input (niet in de cache) | 2,6k tokens |
| Output | 1,2k tokens |
| Cache read / cache write | 24,8k / 16,4k tokens |
| Antwoord op T01 | onzeker |

## Prijs Haiku 5.5, prompts tot 100.000 tokens (per miljoen tokens)

Bron: [Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing), geraadpleegd op 20 oktober 2026.

| Input | Output | Cache read | Cache write (1 uur) |
|---:|---:|---:|---:|
| $0,10 | $0,50 | $0,01 | $0,20 |

Controle: 2,6k × 0,10 + 1,2k × 0,50 + 24,8k × 0,01 + 16,4k × 0,20 per miljoen = $0,0044. Dat klopt met `/cost`.

## Kost per run

Jouw deel is alleen wat een bedrijf via de API zou sturen: je prompt, de input en het antwoord. De context van Claude Code (de 26,8k) en de cache horen daar niet bij.

- Jouw deel: 2,6k input + 1,2k output = **3,8k tokens**
- Kost: 2.600 × $0,10 / 1.000.000 + 1.200 × $0,50 / 1.000.000 = $0,00026 + $0,00060 = **$0,00086**
- In euro (1 dollar = 0,90 euro, aanname): **€0,00077 per run**

| Model | Context (`/context`) | Totaal (`/cost`) | Jouw deel | Kost per run | Per maand, jouw volume | 10× | 1.000× |
|---|---:|---:|---:|---:|---:|---:|---:|
| Haiku 5.5 | 26,8k | $0,0044 | 3,8k tokens | $0,00086 (€0,00077) | $0,52 (€0,46) | $5,16 (€4,64) | $516 (€464) |
| Sonnet 5.5 (zelfde 2,6k in / 1,2k uit) | | | 3,8k tokens | $0,0172 (€0,0155) | $10,32 (€9,29) | $103,20 (€92,88) | $10.320 (€9.288) |

## Volume en berekening

- **Volume:** 600 runs per maand. Bron: schatting. Ongeveer 30 relevante berichten per werkdag over defensie, NAVO en oorlog (als ik zelf VRT NWS, De Tijd en Reuters volg) × 20 werkdagen per maand. Niet precies geteld.
- **Per maand:** kost per run × 600.
- **10×:** 6.000 runs per maand. **1.000×:** 600.000 runs per maand.
- **Haiku 5.5:** 2.600 × $0,10 + 1.200 × $0,50 = $860 per miljoen runs, dus $0,00086 per run.
- **Sonnet 5.5 ($2 input, $10 output per miljoen tokens):** 2.600 × $2 + 1.200 × $10 = $17.200 per miljoen runs, dus $0,0172 per run. Aanname: dezelfde tokens als bij Haiku. In werkelijkheid kan de output anders zijn.
- Sonnet 5.5 is 20× duurder per run dan Haiku 5.5.
- Wisselkoers: 1 dollar = 0,90 euro (aanname).

## Waarde: met de hand of met de tool?

| Schakel | Waarde | Bron |
|---|---|---|
| Met de hand | Openen 15 s · lezen 30 s · beslissen 30 s · noteren 20 s = **95 s** | eigen schatting, niet met een stopwatch gemeten |
| Met de tool | Vinden en openen 15 s · kopiëren en plakken 10 s · wachten 8 s = 33 s. Nakijken 10 s + 12 s voor fouten (60 s × 1 op 5) = 22 s. Totaal **55 s** | wachttijd gemeten (`/cost`), foutpercentage uit eigen testset (1 op 5 inputs), rest geschat |
| Winst per bericht | 95 − 55 = **40 s** | |
| Volume | 30 per dag · 150 per week · 600 per maand · 7.200 per jaar | schatting; aanname: 20 werkdagen per maand, 12 maanden |
| Uren gewonnen | 20 min per dag · 1 u 40 min per week · 6 u 40 min per maand · **80 u per jaar** | |
| Uurkost | **€14,38** | Indeed België, gemiddeld basisloon student, bijgewerkt 11 oktober 2026: https://be.indeed.com/career/student/salaries |
| Waarde | 80 × 14,38 = **€1.150,40 per jaar** | |
| Kost van de tool | 7.200 × $0,00086 = $6,19 = **€5,57 per jaar** (Haiku 5.5) | gemeten |
| Netto | **± €1.145 per jaar** | |
| Zwakste cijfer | De 95 s met de hand. Is het de helft (47,5 s), dan is de tool 7,5 s trager per bericht: −15 u en −€216 per jaar, plus €5,57 toolkost, dus **± −€221 per jaar**. Is het 55 s of minder, dan wint de tool niets. | |
| Tweede zwak punt | Foutpercentage 1 op 5 komt van 5 inputs. Vandaag gaf T01 ook een fout. Bij 2 op 5 is de winst 28 s per bericht. | |
| Te doen | Handtijd meten met een stopwatch op enkele berichten. | |
