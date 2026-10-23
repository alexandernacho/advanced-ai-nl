# Kosten van de leveringsassistent

Datum van meting: 16 oktober 2026.

## Correctie in week 5

De oorspronkelijke meting hieronder gebruikte 36 output-tokens in één run. In de modeltest van 22 oktober 2026 gebruikte Luna gemiddeld 39,1 output-tokens per run op 13 vaste testgevallen. De input blijft 376 tokens. Met de Luna-prijs van $0,10 input en $0,50 output per miljoen tokens is de gecorrigeerde kost:

| Onderdeel | Berekening | Kost in dollar |
| --- | --- | ---: |
| Input | 376 × $0,10 / 1.000.000 | $0,0000376 |
| Output | 39,1 × $0,50 / 1.000.000 | $0,0000196 |
| **Kost per run, gecorrigeerd in week 5** | input + output | **$0,0000572** |

Met de cursusaanname van $1 = €0,90 is dat **€0,0000514 per run**, **€0,00154 per maand** en **€0,0185 per jaar** bij 30 klantvragen per maand. De oude berekening blijft hieronder staan als oorspronkelijke meting.

## Gemeten run

De meting gebeurde met de API en `gpt-6-luna`. In het OpenAI-dashboard telde één klantvraag 376 inputtokens en 36 outputtokens. De website stuurt alleen de klantvraag en de gevonden fictieve bestelgegevens naar de API; er is geen Codex-sessiecontext in deze productierun.

| Onderdeel | Berekening | Kost in dollar |
| --- | --- | ---: |
| Input | 376 × $0,10 / 1.000.000 | $0,0000376 |
| Output | 36 × $0,50 / 1.000.000 | $0,0000180 |
| **Kost per run** | input + output | **$0,0000556** |

Met de cursusaanname van $1 = €0,90 is dat **€0,0000500 per run**.

## Op schaal

Mijn aanname is 30 klantvragen per maand bij Ford Geeraerts.

| Model | Kost per run | Per maand: 30 vragen | 10×: 300 vragen | 1.000×: 30.000 vragen |
| --- | ---: | ---: | ---: | ---: |
| GPT-6 Luna, gecorrigeerd in week 5 | €0,0000514 | €0,00154 | €0,0154 | €1,5431 |
| GPT-6.1 Sol | €0,0010008 | €0,0300 | €0,3002 | €30,0240 |

Voor GPT-6.1 Sol is dezelfde gemeten hoeveelheid tokens gebruikt, met $2 per miljoen inputtokens en $10 per miljoen outputtokens. Dat model is ongeveer twintig keer duurder, maar blijft bij dit volume goedkoop.

## Geschatte waarde van tijdswinst

| Schakel | Waarde | Bron |
| --- | ---: | --- |
| Manueel antwoord | 10 minuten per vraag | eigen schatting |
| Met de tool | 30 seconden menselijke controle per vraag | eigen schatting |
| Winst | 9,5 minuten per vraag | berekening |
| Volume | 30 vragen per maand, 360 per jaar | eigen schatting |
| Tijdswinst | 4,75 uur per maand, 57 uur per jaar | berekening |
| Uurkost verkoper | €40 | eigen aanname |
| Waarde tijdswinst | €2.280 per jaar | 57 uur × €40 |
| API-kost | ongeveer €0,02 per jaar | 360 runs × €0,0000514 |
| Netto geschatte waarde | ongeveer €2.279,98 per jaar | waarde tijdswinst − API-kost |

## Value chain met foutmarge — week 5

De foutmargetest geeft een bereik van 12–13 juiste antwoorden op 13. Bij een fout antwoord gaat de verkoper ervan uit dat het antwoord eerst wordt nagekeken en daarna in **3 minuten** wordt gecorrigeerd. Die drie minuten zijn mijn eigen schatting.

| Schakel | Laagste score: 12/13 | Hoogste score: 13/13 | Bron |
| --- | ---: | ---: | --- |
| Met de hand | 10 min per vraag | 10 min per vraag | eigen schatting |
| Met de tool | 0,5 min nakijken + 1/13 × 3 min herstellen = **0,73 min** | 0,5 min nakijken + 0 × 3 min herstellen = **0,50 min** | eigen schatting + foutmarge |
| Winst per vraag | **9,27 min** | **9,50 min** | berekening |
| Volume | 360 vragen per jaar | 360 vragen per jaar | eigen aanname: 30 per maand |
| Tijdswinst | **55,62 uur per jaar** | **57,00 uur per jaar** | berekening |
| Uurkost verkoper | €40 | €40 | eigen aanname |
| Waarde tijdswinst | **€2.224,62 per jaar** | **€2.280,00 per jaar** | berekening |
| API-kost | €0,0185 per jaar | €0,0185 per jaar | gecorrigeerde Luna-kost in week 5 |
| Netto per jaar | **€2.224,60** | **€2.279,98** | waarde min API-kost |

Mijn zwakste cijfer blijft het volume van 30 vragen per maand. Als dat volume halveert, halveert ook de netto waarde bijna volledig; de invloed daarvan is groter dan die van mijn foutmarge.

## Zwakste cijfer

Ik vertrouw de 30 vragen per maand het minst, omdat dit voorlopig vooral een inschatting is en ik nog niet echt heb gemeten hoeveel klanten maandelijks bellen met vragen over hun levering. Als het werkelijke volume de helft lager ligt, zijn er 15 vragen per maand en 180 per jaar. Dan bedraagt de tijdswinst 28,5 uur per jaar, de geschatte waarde €1.140 per jaar en de API-kost ongeveer €0,01 per jaar.

## Beperking

Dit is één gemeten run. Langere klantvragen of langere antwoorden kunnen meer tokens en dus een hogere kost veroorzaken.
