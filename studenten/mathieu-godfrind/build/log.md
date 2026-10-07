# Logboek

Elke run, elk resultaat, elke wijziging. Wis nooit een fout.

| Datum | Versie | Wat ik deed | Resultaat | Fout of opvallend | Volgende stap |
|---|---|---|---|---|---|
| 2026-09-30 | v1 | Eerste prompt, vijf inputs in de testset, elk twee keer gedraaid | 10 op 10 juist (n = 5, 2 runs) | Geen fouten: testset te makkelijk? | Lastige inputs toevoegen |
| 2026-10-07 | v2 | Audit op de prompt: bouwsteen 4 (voorbeelden) ontbrak. Vier voorbeelden toegevoegd: GO, NO-GO (B + C), ONZEKER, NO-GO (A) | | | Testset naar tien |
| 2026-10-07 | v2 | Citatenregel aangepast: bij ontbrekende CE de lijst met certificaten citeren als die er is | | Voorbeeld 2 botste met de oude regel | |
| 2026-10-07 | v2 | Regel B herschreven met een "want": zonder CE mag je het niet verkopen in de EU, risico op blokkering en onverkoopbare stock | | | |
| 2026-10-07 | v2 | Telregel bovenaan de testset: label en juiste risico moeten kloppen, extra risico met echt citaat is geen fout, verzonnen citaat is altijd F2 | | T07 kan extra risico B uitlokken | |
| 2026-10-07 | v2 | Telregel aangevuld: bij `NO-GO` moeten alle verwachte risico's erbij, een gemist risico is F3 | | T08 is de eerste input met twee verwachte risico's (A, B) | |
