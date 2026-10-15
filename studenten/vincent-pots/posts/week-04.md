# Week 4 — Mijn tool mist niets, maar voegt soms te veel toe

## Mijn tool in cijfers
Mijn tool haalt opdrachten en deadlines uit de tekst van een Canvas-vakpagina. In mijn testset (prompt v2, run 1) is het resultaat **1 op 5 juist (n = 5, 1 run)**. Alleen T07 (het Teamcharter) was volledig goed. De andere vier hadden een fout:

- **F1 (fout), 1×, T09:** bij een modulepagina met alleen lesmateriaal nam de tool drie items op, onder andere "Exam information", terwijl dat een lege kop is.
- **F2 (verzonnen), 1×, T10:** de tool voegde een derde opdracht toe ("Groepsopdracht … case uitwerken") die niet in de tekst staat. Items 1 en 2 waren juist.
- **F4 (vorm), 2×, T06 en T08:** bij T06 klopten de opdracht en de inleverdatum, maar de tool zette er een extra datum bij ("beschikbaar tot"). Bij T08 kwam een lange beschrijving tussen haakjes met de opmerking dat de tekst geen nieuwe datum vermeldt, terwijl de titel zegt dat de deadline verlengd is.

Wat opvalt: in mijn 5 tests miste de tool geen enkele opdracht. De fouten zijn altijd te veel in de lijst, nooit te weinig. Dat past bij mijn prompt, want een opdracht te veel is minder erg dan een die ontbreekt. Het cijfer is wel klein: n = 5 en één run. Ik reken T06 nu als fout, terwijl ik het eerst als juist telde omdat mijn prompt om alle datums vraagt.

## Wat kost één run?
Ik mat in Claude Code met Haiku (`claude-haiku-5-5`) op 14 oktober 2026. Meting 1 was een bericht "hoi": $0,0003. Meting 2 was mijn prompt met T01: $0,0042. Het verschil is **$0,0039 per run** (± €0,0035 met 1 dollar = 0,90 euro, een aanname). Dat is mijn deel: mijn prompt, mijn input en het antwoord. Een bedrijf dat mijn tool via de API gebruikt, betaalt alleen dat, en niet de context die Claude Code zelf meestuurt.

Ik heb de context (`/context`) en de tokens niet kunnen meten, dus de kolommen met tokens zijn leeg in mijn `kosten.md`. Ook staat de prijs van Haiku 5.5 niet in de tabel van de cursus. Mijn bedrag komt rechtstreeks uit `/cost`.

| Volume | Runs per maand | Haiku (gemeten) | Sonnet 5.5 (berekend) |
|---|---:|---:|---:|
| Mijn volume | 20 | $0,078 | $0,156 |
| 10× | 200 | $0,78 | $1,56 |
| 1.000× | 20.000 | $78 | $156 |

De Sonnet-cijfers zijn niet gemeten. Ik rekende × 2, omdat Sonnet in de tabel op input en output twee keer zoveel kost als Haiku 4.5, en ik ga ervan uit dat het evenveel tokens gebruikt. Op mijn eigen volume maakt het model niets uit. Bij 1.000× betaal je met Sonnet ongeveer $78 meer per maand.

## Met de hand of met de tool?
- **Met de hand:** Canvas openen, doorlezen en datums opschrijven kost ongeveer 5 minuten. Bron: schatting.
- **Met de tool:** draaien 1 minuut en nakijken 1 minuut, samen 2 minuten. Bron: schatting.
- **Winst per run:** 5 − 2 = 3 minuten.
- **Volume:** 1 per dag, 5 per week, 20 per maand en 180 per jaar. Aanname: 5 dagen per week, 4 weken per maand en 9 maanden (schooljaar).
- **Uren per jaar:** 180 × 3 minuten = 540 minuten = 9 uur.
- **Uurkost:** €17. Bron: mijn loon bij Deboever Ramen en Deuren.
- **Waarde:** 9 × €17 = €153 per jaar.
- **Kost van de tool:** 180 × $0,0039 = $0,70, ongeveer €0,63 per jaar.
- **Netto:** ongeveer **€152 per jaar**.

De kost van de tool is bijna niets. Het getal hangt vooral af van de minuten, en die zijn geschat.

## Mijn zwakste cijfer
Mijn zwakste cijfer is de **20 runs per maand**. Als ik de deadlines van de dag ervoor al genoteerd heb, hoef ik de volgende dag niet opnieuw te runnen. Bij de helft (10 per maand) wint de tool 4,5 uur per jaar. Dat is €76,50 waarde, min ongeveer €0,32 kost, dus ongeveer **€76 netto per jaar** in plaats van €152. Mijn conclusie blijft dan dezelfde: de tool is de moeite, zolang ik de lijst nakijk op te veel.
