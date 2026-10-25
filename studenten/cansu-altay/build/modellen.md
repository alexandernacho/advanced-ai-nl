# Modeltest — week 5

## Voorspelling van Cansu — vóór de runs

> Ik denk dat een kleiner model de eenvoudige en duidelijke trainingsnotities waarschijnlijk goed kan verwerken, omdat de taak vrij afgebakend is. Bij onduidelijke of rommelige notities verwacht ik wel meer fouten dan bij een groter model, vooral bij het correct toepassen van de regel om “onbekend” te noteren en niets zelf in te vullen.

## Testafspraken

Prompt: v5, ongewijzigd. De tien oorspronkelijke inputs uit `test-set.md`, één run per input per setup. Dezelfde beoordelingsregels als bij de foutmargetest, inclusief uitsluitend `onbekend` bij Sets voor input 6. Input 7 is ook een voorbeeld in de prompt; rapporteer die afzonderlijk. De gewenste antwoorden worden niet meegestuurd.

De voorspelling blijft ongewijzigd bewaard. Alle drie modellen staan in de lokale Codex-modellijst. Het denkniveau blijft gelijk, zodat alleen het model verandert.

| Setup | Rol | Model | Effort |
|---|---|---|---|
| A | Huidig | gpt-5.6-terra | high |
| B | Kleiner | gpt-5.6-luna | high |
| C | Groter | gpt-5.6-sol | high |

Uitvoering zoals de foutmargetest: losse Codex-sessies in een lege tijdelijke map, zonder gebruikersconfiguratie of projectdocumenten; shell, web en apply_patch uitgeschakeld. Codex voegt eigen systeeminstructies toe. Nieuwe runs per setup, geen selectie uit de eerdere drie Terra-rondes. Script en ruwe antwoorden in `week-05-modelruns/`. Alle 30 aanroepen zijn afgerond; 30 verschillende sessies en geen toolgebruik in de logs.

## Resultaten — 24 oktober 2026

Beoordeling door Codex, volgens de vooraf afgesproken regels. De compacte failure-uitvoer bij input 8 blijft beoordeeld volgens de oorspronkelijke testafspraak; Cansu's afwijkende oordeel bij de zelfcontrole staat in `foutmarge.md`.

| Setup | Model | Effort | Score (n = 10, 1 run) | Tegenover Terra-bereik 8–9/10 | Gem. outputtokens per notitie | Raming per notitie | Raming per jaar |
|---|---|---|---:|---|---:|---:|---:|
| A | gpt-5.6-terra | high | 9/10 | Binnen bereik | 46,5 | $0,001946 | $1,52–$1,82 |
| B | gpt-5.6-luna | high | 10/10 | Boven bereik; geen gemeten achteruitgang | 163,0 | $0,0003344 | $0,26–$0,31 |
| C | gpt-5.6-sol | high | 8/10 | Binnen bereik | 61,7 | $0,004010 | $3,13–$3,75 |

De jaarlijkse volumes zijn Cansu's bestaande schatting van 780–936 notities. Kosten zijn losse-toolramingen met 694 inputtokens als vaste benadering uit week 4 en de werkelijk geregistreerde gemiddelde output van deze test. De werkelijke hoeveelheid inputtekst verschilt iets per notitie. Dit zijn geen gemeten factuurbedragen of extra afschrijvingen van een abonnement.

### Beoordeling per input

| Input | A: Terra | B: Luna | C: Sol |
|---|---|---|---|
| 1 | Correct | Correct | Correct |
| 2 | Correct | Correct | Correct |
| 3 | Correct | Correct | Correct |
| 4 | Correct | Correct | Correct |
| 5 | Correct | Correct | Correct |
| 6 | Correct | Correct | F3 |
| 7 (promptvoorbeeld) | Correct | Correct | Correct |
| 8 | F4 | Correct | Correct |
| 9 | Correct | Correct | F3/F4 |
| 10 | Correct | Correct | Correct |

- Terra input 8: alleen `tot failure (aantal onbekend)`; niet expliciet voor alle drie sets zoals vooraf afgesproken.
- Sol input 6: Sets is correct `onbekend`, maar Herhalingen is `12, laatste set tot failure (aantal onbekend)`; de genoemde drie keer twaalf is niet volledig behouden.
- Sol input 9: Sets is correct `4`, maar Herhalingen is alleen `tot failure (aantal onbekend)`; de onbekende herhalingen van de eerste drie sets en de koppeling van failure aan alleen de laatste set zijn niet expliciet behouden.
- Luna: alle tien antwoorden komen inhoudelijk en qua uitvoer overeen met de vooraf vastgelegde afspraken, ook bij inputs 6, 8 en 9.

Zonder promptvoorbeeld 7: Terra 8/9, Luna 9/9, Sol 7/9. De laatste prompt blijft ongewijzigd.

## Kosten en bronnen

Standaard API-prijzen per miljoen tokens, gecontroleerd op 24 oktober 2026:

| Model | Input | Output | Cache lezen |
|---|---:|---:|---:|
| GPT-5.6 Terra | $2 | $12 | $0,20 |
| GPT-5.6 Luna | $0,20 | $1,20 | $0,02 |
| GPT-5.6 Sol | $4 | $20 | $0,40 |

Bronnen: officiële OpenAI-modeldocumentatie voor [Terra](https://developers.openai.com/api/docs/models/gpt-5.6-terra), [Luna](https://developers.openai.com/api/docs/models/gpt-5.6-luna) en [Sol](https://developers.openai.com/api/docs/models/gpt-5.6-sol). De Sol-prijs is een promotietarief, volgens de bron minstens tot 21 november 2026; de jaarbedragen veronderstellen een gelijkblijvend tarief.

Formule: `(694 × inputprijs + gemiddelde outputtokens × outputprijs) / 1.000.000`. Geen cachekorting aangenomen voor de losse tool. De outputtelling uit `turn.completed.usage.output_tokens` omvat reasoning al; reasoning wordt niet opnieuw opgeteld. Gemiddelde reasoning-output: Terra 0, Luna 113,3, Sol 15 tokens. Meer geregistreerde output bij Luna maakt het hier niet duurder dan de andere modellen door het lagere tarief.

De volledige Codex-sessies hebben daarnaast eigen systeemcontext (ongeveer 10.000–11.500 inputtokens inclusief onze prompt) en soms inputcache; die is geen onderdeel van de losse-toolraming. De systeemcontext en tokenizer kunnen per model verschillen. De antwoorden zijn dus onder gelijke gebruikersprompt en instellingen verzameld, maar niet met gegarandeerd identieke systeemcontext. Het script registreert de aangevraagde model-ID; de eventlogs geven geen afzonderlijke model-snapshot terug.

## Wat deze ronde laat zien

Luna houdt hier stand: ook de onduidelijke en rommelige notities zijn correct verwerkt. De verwachting van extra fouten met het kleinere model is in deze ronde niet uitgekomen. Sol toont geen gemeten voordeel boven Terra. Luna is bij de gebruikte ramingen de goedkoopste setup en een kandidaat voor verder gebruik.

Eén ronde per setup bewijst geen blijvende rangorde. De foutmarge 8–9/10 is alleen bij Terra met v5 gemeten, niet bij Luna of Sol. Een score boven dat bereik in één ronde bewijst niet dat Luna altijd beter is. De kleine, eerder voor promptverbeteringen gebruikte testset bevat bovendien een promptvoorbeeld.

Een lager denkniveau is nog niet getest; deze vergelijking houdt effort bewust op high.

## Voorlopige modelkeuze van Cansu

> Ik zou voorlopig Luna kiezen, omdat dit model in deze testronde 10/10 scoorde en ook het goedkoopst is. Ik zou het wel nog op extra onduidelijke of rommelige trainingsnotities testen, omdat één testronde nog niet bewijst dat Luna altijd foutloos werkt.

Gekozen setup voor het voorlopige gebruiksscenario: `gpt-5.6-luna`, effort `high`, met prompt v5. De keuze voor het model is voorlopig; high is het geteste denkniveau, niet bewezen het goedkoopste voldoende denkniveau. Extra testnotities en hun verwachte antwoorden moeten van Cansu komen en vóór nieuwe tests worden vastgelegd. Ze zijn nog niet verzameld of getest.
