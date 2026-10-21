# Week 5

## Mijn foutmarge
Ik vergeleek v1 (week 2) met v1.2 (de laatste versie), elk 3 runs op dezelfde 10 KID’s met Sonnet 5.5. v1 haalde 3 tot 4 van de 10 KID’s volledig juist en v1.2 haalde 9 tot 10 van de 10 KID’s volledig juist. Mijn claim uit week 3 is bevestigd, want de laagste score van v1.2 (9) ligt boven de hoogste van v1 (4). v1.1 is nooit apart bewaard, dus ik heb v1 en v1.2 vergeleken.

## Model en effort
Ik gokte 9 op 10 bij alle drie. Eruit kwam: Haiku 9, Sonnet 10 en Opus 10. Mijn gok klopte dus gedeeltelijk. Het verschil viel binnen mijn foutmarge (9 tot 10). Ik zet Sonnet in productie, want 2,61 euro per jaar is redelijk klein vergeleken met de 230 tot 262 euro per jaar die de tool netto oplevert.

## Mijn value chain, met de foutmarge erin
Met de hand kost een ETF me 12,5 minuten. Met de tool zit ik op 2,7 tot 3,9 minuten. Dat scheelt 9,8 tot 8,6 minuten per ETF.

Ik reken op 72 ETF’s per jaar. Een uur kost de werkgever €22,50 (€15 bruto maal 1,5).

Netto blijft er ongeveer €262 per jaar over als de tool 10 op 10 haalt. Bij 9 op 10 is het ongeveer €230.

Mijn zwakste cijfer is het nakijken. Die 2 minuten heb ik geschat en niet gemeten. Duurt het 5 minuten, dan blijft er bij 10 op 10 nog ongeveer €177 netto over.

## Mijn dashboard
https://claude.ai/artifact/AwLrnBTkroBbuSVqQ4HuSE

Een lezer ziet eerst mijn score met de foutmarge (v1.2: 9 tot 10 van de 10 KID’s volledig juist) en of mijn claim bevestigd is. Daaronder staan de testset, de drie setups, de kost en de value chain.

## Mijn AI-ismen
Week 2: "Een taalmodel helpt me om snel te zien of een ETF iets voor mij is. Het bespaart me tijd, want ik moet geen saaie documenten meer lezen."
Herschreven: Met de hand duurde het ongeveer 12,5 minuten per ETF en met de tool ongeveer 2,8 minuten (allebei een schatting), dus de winst is ongeveer 9,7 minuten per ETF.

Week 3: "Elke regel die ik toevoeg, lost dus vooral de vorige fout op en niet de onderliggende onzekerheid."
Herschreven: Dezelfde prompt haalde eerst 10/10, dan 10/10 en dan 9/10, dus het is nog geen scherpe prompt.

Week 4: "Ik vind 79 op 80 een goed resultaat, maar niet goed genoeg voor een AI: een AI moet dit gewoon kunnen aflezen."
Herschreven: Bij v1.2 zat er 1 fout in 240 velden (30 runs): de tool pakte één keer de verkeerde kolom, en in de andere 2 runs van dezelfde input ging het goed.

Week 2: "Dat is geen reden om het taalmodel te laten vallen."
Herschreven: Bij 5 van de 10 KID’s waren de lopende kosten fout door twee botsende regels in mijn prompt, daarna in 30 runs nergens meer.

Week 4: "Mijn prompt is dus nog niet perfect, en er is altijd plaats voor verbetering."
Herschreven: Bij v1.2 pakte hij in 1 van de 30 runs de verkeerde kolom, en bij 4 KID’s met een andere bewaartermijn dan 5 jaar pakte hij wel de juiste.

## Mijn testset groeit
Ik koos 10 echte KID’s via Saxo Investor, 7 randgevallen en 5 onzekere, met een andere taal en bewaartermijn, express moeilijk. Ik dacht dat mijn tool zou falen bij een bewaartermijn langer dan 5 jaar (T30: 7 jaar, T31: 10 jaar), maar hij had het nog steeds juist. Mijn score op set v2 is 32 van 32 inputs volledig juist (n = 32, 1 run). Omdat de eerste 30 allemaal juist waren, voegde ik er nog 2 toe die het moeilijker konden maken.
