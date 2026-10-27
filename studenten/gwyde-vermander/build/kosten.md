Gemeten op 14 oktober 2026. 1 dollar = 0,90 euro (aanname). Prijzen uit de tabel van week 4 (Haiku 4.5: input $1, output $5 per miljoen tokens).

| Model | Context (/context) | Totaal (/cost) | Mijn deel | Kost per run | Per maand, jouw volume | 10× | 1.000× |
|---|---:|---:|---:|---:|---:|---:|---:|
| Haiku 4.5 (tabelprijs) | 32,3k | 46,8k | 14,5k (± 13,4k input, 1,1k output) | $0,0189 = € 0,017 | € 24,49 (1.440 runs) | € 244,90 | € 24.494 |

Opmerkingen onder de tabel:
- Gemeten in een lege map, omdat /context in mijn studentenmap de cursus-skill "context" start in plaats van de ingebouwde opdracht.
- /cost toonde het model claude-haiku-5-5 en een echte kost van $0,0042 (studentenmap) en $0,0045 (andere map). Het verschil komt door de cache.
- Studentenmap: 3,2k input, 1,1k output, 31,5k cache read, 15,0k cache write.
- Mijn deel is mogelijk te hoog: met alleen gewone input en output (3,2k + 1,1k) is de kost per run $0,0087 = € 0,008.

Volume: eigen gebruik voor een wielermanager. 160 renners per koers × 6 tot 12 koersdagen per maand = 960 tot 1.920 runs per maand; gerekend met het midden: 1.440 runs per maand. Bron: geschat.
Met de lage kost per run (€ 0,008): € 11,28 per maand, € 112,80 bij 10×, € 11.275 bij 1.000×.

Ander model, zelfde volume (1.440 runs, 13,4k input + 1,1k output per run):

| Model | Kost per run | Kost per maand |
|---|---:|---:|
| GPT-6 Luna | € 0,0017 | € 2,45 |
| Haiku 4.5 | € 0,017 | € 24,49 |
| Sonnet 5.5 | € 0,034 | € 48,99 |
| Opus 5.5 | € 0,068 | € 97,98 |

Volume voor Sporza (scenario vanaf 14 oktober 2026): ± 950 renners, één beoordeling per jaar vóór het voorjaarsspel (bron: Sporza, 900 tot 1.000 renners). Kost: 950 × € 0,017 = ± € 16 per jaar (lage schatting: € 8). Bij 10× (9.500 runs): ± € 162. Bij 1.000× (950.000 runs): ± € 16.150. Het volume 'eigen gebruik' hierboven hoort bij mijn eerste scenario.

## Gecorrigeerd in week 5 (21 oktober 2026)

In week 4 rekende ik met de prijs van Haiku 4.5, maar /cost toonde claude-haiku-5-5. Haiku 5.5 kost een tiende: input $ 0,10, output $ 0,50 per miljoen tokens (prijstabel week 5). De dollars in /cost waren ook fout: Claude Code rekende Haiku 5.5 aan de prijs van Opus.

| Model | Mijn deel | Kost per run | Sporza per jaar (950 runs) | 10× | 1.000× |
|---|---:|---:|---:|---:|---:|
| Haiku 5.5 (gecorrigeerd) | 14,5k (± 13,4k input, 1,1k output) | $ 0,00189 = € 0,0017 | ± € 1,62 | ± € 16 | ± € 1.615 |

Lage schatting (3,2k input + 1,1k output): $ 0,00087 = € 0,0008 per run.
