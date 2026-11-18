# Testset bron (B01–B05)

**Bron:** `build/bronnen/invesco-kid.md` (Invesco MSCI World Equal Weight UCITS ETF, NL, uit `build/kid/4.pdf`)

Het juiste antwoord, en waar het in het document staat, schrijf je vóór de eerste run.
B01–B04: het document geeft het antwoord. B05: het document geeft het antwoord níet.

| ID | Vraag | Juiste antwoord | Waar in het document | Run 1 | Juist? |
|---|---|---|---|---|---|
| B01 | Hoeveel krijg je volgens het stressscenario terug na 5 jaar als je 10.000 USD belegt? | 4.280 USD (gemiddeld −15,59% per jaar) | Kopje "Wat zijn de risico's en wat kan ik ervoor terugkrijgen?", prestatiescenario's, rij "Stress", kolom "Als u uitstapt na 5 jaar" | Antwoord: 4.280 USD (gemiddeld rendement van −15,59% per jaar). Gebruikt deel: rij "Stress" met 4.280 USD en daaronder "-15,59 %", onder Prestatiescenario's. | ja |
| B02 | Als de aanbieder niet kan uitbetalen, is je geld dan gedekt door een garantie- of compensatieregeling? | Nee, er is geen compensatie- of waarborgregeling | Kopje "Wat gebeurt er als Invesco Investment Management Limited niet kan uitbetalen?": "Als aandeelhouder in het Fonds is er geen compensatie- of waarborgregeling van toepassing." | Antwoord: Nee. Er is geen compensatie- of waarborgregeling van toepassing voor aandeelhouders in het Fonds. Gebruikt deel: "Als aandeelhouder in het Fonds is er geen compensatie- of waarborgregeling van toepassing." onder "Wat gebeurt er als Invesco Investment Management Limited niet kan uitbetalen?" | ja |
| B03 | Rekent het fonds instapkosten aan? Kan de verkoper (tussenpersoon) wel kosten aanrekenen? | Het fonds rekent geen instapkosten aan (0 USD), maar de verkoper kan dat misschien wel | Kopje "Wat zijn de kosten?", samenstelling van de kosten, rij "Instapkosten": "Wij brengen voor dit product geen instapkosten in rekening, maar de persoon die u het product verkoopt, doet dat misschien wel." | Antwoord: Nee, het fonds rekent geen instapkosten aan (0 USD). De verkoper kan wel kosten aanrekenen ("misschien wel"). Het bedrag staat niet in het document. Gebruikt deel: "Wij brengen voor dit product geen instapkosten in rekening, maar de persoon die u het product verkoopt, doet dat misschien wel." onder Wat zijn de kosten? > Samenstelling van de kosten > Instapkosten. | ja |
| B04 | Waar dien je eerst een klacht in over het fonds, en waar kan je daarna nog heen als je niet tevreden bent met het antwoord? | Eerst per e-mail bij investorcomplaints@invesco.com of schriftelijk bij de ETF Legal Department van Invesco in Dublin. Daarna bij de Ierse Financial Services and Pensions Ombudsman (fspo.ie) | Kopje "Hoe kan ik een klacht indienen?", punten (1) en (2) en de zin "Indien u niet tevreden bent met ons antwoord op uw klacht, kunt u de kwestie doorverwijzen naar de Ierse Financial Services and Pensions Ombudsman…" | Antwoord: Eerst bij Invesco, per e-mail (investorcomplaints@invesco.com) en/of schriftelijk bij de ETF Legal Department, Invesco, Dublin. Daarna doorverwijzen naar de Ierse Financial Services and Pensions Ombudsman via https://www.fspo.ie/. Gebruikt deel: punten (1) en (2) en de zin over de Ombudsman onder "Hoe kan ik een klacht indienen?" | ja |
| B05 | Welk beurstaks-tarief (TOB) betaal je als Belgische belegger bij het kopen of verkopen van dit fonds? | `staat niet in het document` | — (het KID zegt alleen dat er "geen rekening is gehouden met uw persoonlijke fiscale situatie"; het TOB-tarief hangt af van het product en de registratie in België) | Antwoord: staat niet in het document. Gebruikt deel: "In de bedragen is geen rekening gehouden met uw persoonlijke fiscale situatie, die eveneens van invloed kan zijn op hoeveel u terugkrijgt." onder Prestatiescenario's. | nee |

Resultaat: **4 op 5 juist** (n = 5, 1 run, model: Claude via subagents, elk in een nieuwe sessie met alleen `prompt-bron.md` en het document)


## Extra run: B05 na aanpassing van de prompt
Run 1 gebruikte `prompt-bron-v1.md`. Het formaat eiste altijd een bron, dus de tool zette bij B05 een zin die er alleen op leek. Daarna paste ik `prompt-bron.md` aan: bij een antwoord dat niet in het document staat schrijft de tool `geen bron, want het staat niet in het document`.

| ID | Run 2 (nieuwe prompt, nieuwe sessie) | Juist? |
|---|---|---|
| B05 | Antwoord: staat niet in het document. Bron: geen bron, want het staat niet in het document | ja |

De officiële score blijft 4 op 5 (Run 1). Run 2 is één run op één geval, na het zien van de fout.
