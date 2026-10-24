# Modellen en effort

## Mijn gok (vóór de runs, 24 oktober 2026)
- Scoort het best: **C, Opus 5.5**, omdat er toch wel wat onderzoekswerk nodig is.
- Goed genoeg voor DBA Hardwoods: **C, Opus 5.5**.

## Resultaat
24 oktober 2026, prompt v2, `claude -p --model <model> --tools ""`, 1 run per setup, alle 10 inputs.
Kost per run = jouw deel input uit week 4 (gemiddeld 2.697 tokens) × inputprijs + output-tokens van deze setup × outputprijs. 1 dollar = 0,90 euro. Per jaar = 1.200 runs.

| Setup | Model | Effort | Score (n = 10, 1 run) | Binnen mijn foutmarge (9–9)? | Output-tokens per run | Kost per run | Per jaar |
|---|---|---|---:|---|---:|---:|---:|
| A | Sonnet 5.5 | medium | 9/10 | ja | 202 | $0,0074 · € 0,0067 | € 8,00 |
| B | Haiku 5.5 | standaard | 10/10 | net erboven, maar n = 1 run | 797 | $0,00067 · € 0,0006 | € 0,72 |
| C | Opus 5.5 | standaard | 10/10 | net erboven, maar n = 1 run | 318 | $0,0172 · € 0,0154 | € 18,50 |

Het enige verschil is T07 Bautier: A zei `ja` (fout), B en C zeiden `nee` (juist). Op de andere 9 inputs gaven alle drie hetzelfde juiste antwoord.
Haiku 5.5 schrijft 4× meer output dan Sonnet (denkwerk), maar is per token 20× goedkoper: per run 11× goedkoper dan Sonnet.

Gok: Opus het best, en Opus nodig. **Deels fout.** Opus haalde 10/10, maar Haiku 5.5 ook, voor 1/25 van de prijs.
## Haiku 5.5, 3 runs (zelfde inputs, zelfde manier als de foutmargetest)

| Setup | Run 1 | Run 2 | Run 3 | Bereik | Output-tokens per run (gem.) |
|---|---:|---:|---:|---:|---:|
| Sonnet 5.5 (v2, uit `foutmarge.md`) | 9/10 | 9/10 | 9/10 | 9–9 | ± 200 |
| Haiku 5.5 | 10/10 | 10/10 | 10/10 | 10–10 | ± 825 |

De bereiken overlappen niet: op deze 10 inputs scoort Haiku 5.5 beter dan Sonnet 5.5. Maar het hele verschil is één input (Bautier). Met n = 10 is dat nog weinig bewijs.
