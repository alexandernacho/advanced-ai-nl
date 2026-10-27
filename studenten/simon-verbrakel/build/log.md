# Log

## Week 2
- v1-prompt gemaakt en 5 testinputs elk twee keer gedraaid: 2 van 5 juist, in beide runs telkens hetzelfde antwoord.
- Opgemerkt: bij T01 stond de belangrijke info pas in de tweede alinea, en bij T05 twijfel ik aan mijn eigen label.

## Week 3
- Audit van de prompt: bouwsteen 4 (voorbeelden) ontbrak. Vijf voorbeelden toegevoegd, één per label, geen enkele uit de testset.
- Regel "baseer je alleen op de tekst" herschreven met een want, zodat het model weet waarom die regel er staat.
- Testset uitgebreid van 5 naar 10 inputs (T06 tot T10). T09 en T10 achteraf aangepast na controle van de eerste alinea: T09 nieuwe reden, T10 van onzeker naar niet over defensie.
- Buurtest: geen klasgenoot beschikbaar, dus Claude in een apart gesprek speelde de buur en las alleen prompt.md. Op T05 koos de buur positief (mijn antwoord: onzeker), op T08 onzeker (gelijk), op T09 positief (gelijk).
- Opgemerkt: de buur twijfelde bij T05 en T09 omdat de prompt niet zegt wat te doen met (1) extra defensiegeld dat met besparingen elders betaald wordt, en (2) een defensiebedrijf dat uitbreidt. Daar mist een regel. Bij T05 gaven de buur en het model allebei positief, dus mijn eigen antwoord is misschien fout.
- Na de buurtest mijn juiste antwoord bij T05 aangepast van onzeker naar positief: er komt extra geld voor defensie, de besparingen gebeuren elders, dus voor defensiebedrijven is dit meer vraag.
- Twee regels met een want toegevoegd aan de prompt: extra defensiegeld dat met besparingen elders betaald wordt is positief, en een defensiebedrijf dat een fabriek bouwt of uitbreidt is positief.
- Run 1 op T06 tot T10 met de nieuwe prompt, twee keer gedraaid: 8 op 10 juist (n = 5 inputs, 2 runs). Enige fout: T08, F1 (fout), in beide runs negatief.
- Wijziging: regel toegevoegd dat gesprekken zonder akkoord onzeker zijn. T08 opnieuw gedraaid: Run 1 negatief, Run 2 onzeker. De fout ging van F1 (zeker fout) naar F6 (wisselend). De regel helpt, maar niet altijd. Het woord 'productieve' trekt het model nog richting negatief. Dit is één input, dus het bewijst weinig.
- Alle tien inputs gedraaid met de huidige prompt (T01 tot T05 nu ook): 17 op 20 juist (85%) (n = 10 inputs, 2 runs). Fouten: T01 in beide runs, F5 (onzeker, terwijl het juiste antwoord positief is; de alinea noemt geen budget), en T08 in 1 van 2 runs, F1.
- Achteraf het juiste antwoord van T01 aangepast van positief naar onzeker. Reden: de kop en eerste alinea noemen geen budget of uitgaven. Mijn oude label kwam uit mijn eigen voorkennis over de NAVO-top, en dat verbiedt mijn taak. Het cijfer wordt daardoor 19 op 20 juist (95%) (n = 10 inputs, 2 runs). Het cijfer vóór de aanpassing was 17 op 20 (85%). Een label achteraf aanpassen maakt een cijfer mooier, dus ik meld het.

## Week 5
- T03: model zegt onzeker, mijn verwachte antwoord is neutraal. Twijfelgeval, verwacht antwoord aanpassen vóór een volgende run, niet nu.
- Set v2 (T01–T30), prompt v3, Haiku 5.5, `claude -p --tools ""`, elke input in een aparte sessie: 23 op 30 (set v2, 1 run). T01–T10: 10 op 10 (set v2, 1 run). T11–T30: 13 op 20 (set v2, 1 run). Verwachte antwoorden voor de run vastgelegd en niet aangepast, prompt niet aangepast.
- Fouten bij T11–T30 (model zei, ik verwachtte): T11 neutraal, positief. T15 onzeker, neutraal. T16 onzeker, positief. T26 onzeker, neutraal. T27 niet over defensie, positief. T28 onzeker, positief. T29 onzeker, neutraal.
