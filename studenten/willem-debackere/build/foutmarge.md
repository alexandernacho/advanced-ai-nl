# Foutmarge, 21 oktober 2026

Model: Claude Sonnet 5.5 (`claude-sonnet-5-5`), standaard effort. n = 10 inputs, 3 runs per versie. Zelfde inputs voor beide.
Elke run een aparte sessie met `claude -p --tools ""`: alleen de prompt en de input, geen verwachte antwoorden.
Juist = doelgroep én lead juist, bij lead `ja` het juiste e-mailadres, bij `geen e-mail` geen verzonnen adres.

| Versie | Run 1 | Run 2 | Run 3 | Foutmarge (min–max) |
|---|---:|---:|---:|---:|
| v1 (`prompt-v1.md`) | 9/10 | 9/10 | 9/10 | 9–9 |
| v2 (`prompt.md`) | 9/10 | 9/10 | 9/10 | 9–9 |

Fout in alle 6 runs: T07 Bautier, `ja · ja · info@bautier.com` (F1). Verwacht: `nee · nee`.
Geen enkel verzonnen e-mailadres (F2) in 60 runs.

Mijn claim (week 3): "Ik voegde één regel toe [...] Daarna gaf Bautier twee keer `nee`."
**Ingetrokken**, want de bereiken overlappen: v1 9–9, v2 9–9. De nieuwe regel deed op Bautier niets: beide versies gaven 3 keer `ja`. De 2× `nee` uit week 3 was toeval.
