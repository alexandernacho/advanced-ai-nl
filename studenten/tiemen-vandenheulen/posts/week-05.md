# Week 5 — Meer testen maakt mijn score eerlijker

## Mijn foutmarge

Met mijn huidige en vorige promptversie haalde ik telkens 8 op 10 in drie runs. De foutmarge is dus 8–8/10, met n = 10. Mijn oude claim dat de tool bijna waterdicht was, trek ik in: twee reviews kregen telkens een extra label. De tool blijft bruikbaar als eerste sortering, maar iemand moet de labels nakijken.

## Model en effort

Ik schreef vooraf mijn voorspelling voor T26 op: Haiku en Opus zouden `veiligheid, organisatie` kiezen; Sonnet vooral `veiligheid`. De volledige vergelijking met Haiku, Sonnet en Opus is nog niet gemeten, omdat ik geen Claude-abonnement heb. Ik gebruik daarom voorlopig GPT-6.1 Sol met laag redeneerniveau: die haalde eerder 9/10 en gebruikte gemiddeld 76,3 outputtokens. Dit is een voorlopige keuze, geen bewezen vergelijking met de drie Claude-modellen.

## Mijn value chain, met de foutmarge erin

Handmatig kost één review mij twee minuten. Met de tool reken ik 20 seconden voor draaien, nakijken en overnemen. Door de foutmarge moet ik bij 20% van de reviews nog twee minuten fout herstellen. Dat maakt 44 seconden met de tool en 76 seconden tijdwinst per review. Bij 240 reviews per jaar is dat 5 uur en 4 minuten. Met een werkgeverskost van €19,50 per uur is de tijdwaarde €98,80. De AI-kost is ongeveer €0,39 per jaar, dus netto blijft €98,41. Omdat mijn foutmarge 8–8/10 is, verandert dit cijfer in deze meting niet door het bereik. Mijn zwakste cijfer blijft de 20 seconden: bij 40 seconden zakt het netto naar €72,41.

## Mijn dashboard

Mijn publieke dashboard staat hier: https://review-sorteerder-dashboard-2026.candymango32.chatgpt.site. Een lezer ziet eerst de score, de foutmarge en de netto waarde per jaar.

## Mijn AI-ismen

- Week 1: “Woensdag verraste me dat je zoveel meer met AI kunt doen dan ik al kende.” Ik herschreef dit naar: AI kan een bezoekersreview indelen in categorieën, zoals wachttijden bij een lange rij aan de ingang.
- Week 1: “Ik wil AI verkennen in de bedrijfswereld, vastgoed, evenementen en sport.” Ik wil onderzoeken hoe AI organisatoren helpt om terugkerende thema’s in bezoekersreviews sneller te herkennen.
- Week 2: “Een taalmodel past bij deze taak omdat het de betekenis van vrije tekst moet interpreteren.” Bij “De rij aan de ingang duurde twintig minuten” moet de tool `wachttijden` kiezen.
- Week 4: “De AI-kost is dus opvallend laag voor mijn scenario.” Voor mijn scenario kost de AI €0,0324 per maand, of €0,39 per jaar.
- Week 4: “De tool blijft dan nuttig.” Bij 20 seconden controle per antwoord blijft de controle nodig, omdat de tool soms een extra label toevoegt.

## Mijn testset groeit

Mijn testset is nu set v2 met T01–T30. T11–T20 komen uit mijn ervaringen op Modul'air, Sweet Seduction en Bambata. T21–T26 zijn randgevallen en T27–T30 zijn vage reviews waarvoor `andere` het juiste antwoord is. In één run haalde de tool eerst 25/30. Na twee openlijke correcties van onvolledige verwachte antwoorden bij T12 en T26 werd dat 27/30 (set v2, n = 30, 1 run). T12 verraste mij het meest: een dure friet gaat tegelijk over prijs en catering.
