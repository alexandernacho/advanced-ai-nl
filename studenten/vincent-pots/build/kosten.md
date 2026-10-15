# Kosten — Vincent Pots

Datum: 14 oktober 2026
Koers: 1 dollar = 0,90 euro (aanname)
Model: `claude-haiku-5-5` (niet Haiku 4.5 uit de tabel van de README; prijs van Haiku 5.5 nog te controleren)

| Model | Context (`/context`) | Totaal (`/cost`) | Jouw deel | Kost per run | Per maand, jouw volume | 10× | 1.000× |
|---|---:|---:|---:|---:|---:|---:|---:|
| Haiku 5.5 | | | | $0,0039 (± €0,0035) | $0,078 (± €0,07) | $0,78 (± €0,70) | $78 (± €70) |
| Sonnet 5.5 (berekend) | | | | $0,0078 (± €0,007) | $0,156 (± €0,14) | $1,56 (± €1,40) | $156 (± €140) |

## Sonnet 5.5: hoe berekend
- Niet gemeten, maar geschaald: in de tabel van de README kost Sonnet 5.5 op input en output 2× zoveel als Haiku 4.5 (2 en 10 dollar tegenover 1 en 5 per miljoen tokens). Dus kost per run = 2 × $0,0039.
- Voorbehoud 1: ik ga ervan uit dat de prijs van mijn Haiku (`claude-haiku-5-5`) bij de tabel past. Is Haiku 5.5 goedkoper, dan is Sonnet relatief duurder (bij een tiende van de tabelprijs ongeveer 20×: ± $0,078 per run en ± $1.560 bij 1.000× het volume).
- Voorbehoud 2: ik ga ervan uit dat Sonnet evenveel tokens gebruikt als Haiku. Sonnet kan anders denken. Voor een echt cijfer: dezelfde meting draaien met `/model sonnet`.

## Hoe gemeten
- Meting 1: nieuwe sessie, `/model haiku`, bericht "hoi", `/cost` gaf $0,0003 (2,6k input, 25 output).
- Meting 2: prompt + T01 in één bericht, `/cost` gaf $0,0042 (eerder genoteerd als $0,0041).
- Kost per run = meting 2 − meting 1 = $0,0039. Dit is jouw deel: prompt, input en antwoord.

## Volume
20 runs per maand = 5 dagen per week × 4 weken. Bron: schatting van mijn eigen gebruik (elke werkdag deadlines checken), niet geteld.

## Nog open
- Tokens van meting 2 (input en output) invullen, zodat Totaal en Jouw deel in tokens kloppen.
- Prijs van Haiku 5.5 controleren, want de bedragen hierboven komen rechtstreeks uit `/cost`.
- Een ander model met hetzelfde volume doorrekenen (ronde 2, stap 4).
