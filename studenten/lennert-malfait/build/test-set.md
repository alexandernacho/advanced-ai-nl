# Testset

**Set v2: T01–T30, 27 oktober 2026**

De oude T01–T10 zijn hieronder ongewijzigd overgenomen. T11–T30 zijn 20 nieuwe, geanonimiseerde inputs uit mijn eigen Outlook-inbox. De verwachte antwoorden en redenen voor T11–T30 zijn vooraf vastgelegd vóór de classifier-run.

## Oude T01–T10 — ongewijzigd

| T01 | Onderwerp: Laptop meenemen naar les<br><br>Beste studenten,<br><br>Voor les 2 op [datum] zou het handig zijn om jullie laptop mee te brengen.<br><br>Zo niet, dan doe je de oefening met twee.<br><br>Met vriendelijke groeten,<br>Dhr. [naam] | No | lezen | The laptop is recommended, but the message says an alternative is available; no required action follows. | Own school email, anonymised | doen ✗ — F1 | lezen ✓ — v3 rerun |
| T02 | Onderwerp: Laptop meenemen naar les<br><br>Beste studenten,<br><br>Voor les 2 op [datum] zou het handig zijn om jullie laptop mee te brengen.<br><br>Zo niet, dan doe je de oefening met twee.<br><br>Met vriendelijke groeten,<br>Dhr. [naam] | Yes — T01 | herhaling | This is the second identical copy of T01 and contains no new information. | Own school email, anonymised | herhaling ✓ | Not run |
| T03 | Onderwerp: Studieprogramma controleren<br><br>Beste student,<br><br>[Onderwijsinstelling] heeft jouw studieprogramma aan jou overgemaakt. Geef hier zo snel mogelijk gevolg aan via [platform].<br><br>Mededeling: Je traject staat nog niet op punt. Zie voor verdere info de eerdere mail.<br><br>Bedankt voor jouw medewerking,<br>[Onderwijsinstelling] | No | doen | The student is asked to take prompt action, and the study trajectory is not yet in order. | Own school email, anonymised | doen ✓ | Not run |
| T04 | Onderwerp: Wekelijks Canvas-rapport<br><br>Je bent aangemeld voor een wekelijks rapport over belangrijke meldingen van jouw Canvas-account. Hieronder staat het rapport voor de week die eindigt op [datum].<br><br>Opdracht aangemaakt — [naam opdracht/cursus].<br><br>Inleverdatum: geen inleverdatum.<br><br>[link verwijderd] | No | negeren | This is a routine weekly Canvas report. The student receives many of these reports and normally checks Canvas directly instead. | Own school email, anonymised | negeren ✓ | Not run |
| T05 | Onderwerp: Activiteiten en externe opleidingen<br><br>Beste studenten,<br><br>Bekijk de activiteiten van [organisatie] via [link verwijderd]. Deze week vindt ook een business- en technologie-evenement plaats in [locatie], met sessies en masterclasses. Actieve deelname kan meetellen als externe opleiding, tot maximaal twee van de vier opleidingen.<br><br>Veel succes! | No | lezen | This is relevant information about optional activities and external education, but it contains no required action. | Own school email, anonymised | lezen ✓ | Not run |
| T06 | Onderwerp: Herinnering: GitHub-link posten<br><br>Post de link naar je GitHub-pull-request in de juiste week op Canvas. Punten worden alleen via Canvas gegeven; zonder link in de juiste week is er geen score. | No | doen | This message requires Lennert to post a specific PR link in Canvas in time. | Own school email, anonymised | doen ✓ | Not run |
| T07 | Onderwerp: Correctie les Frans<br><br>Vanaf deze week bestaat het eerste deel van de les uit marketing- of sociaaleconomische actualiteit; het tweede deel gaat over een ander cursusthema. | No | lezen | This is relevant information about the format of a course, but it asks for no concrete action. | Own school email, anonymised | lezen ✓ | Not run |
| T08 | Subject: Sign up to win a Web Summit ticket<br><br>Final week to enter the challenge and compete for event tickets. | No | negeren | This is an optional external promotion, not required information or an action for Lennert. | Own inbox email, anonymised | negeren ✓ | Not run |
| T09 | Onderwerp: Welkom bij Canva<br><br>Je account is klaar. Ontdek de functies van Canva. | No | negeren | This is an automated welcome email. It contains no action that Lennert must take and no urgent school information. | Own inbox email, anonymised | negeren ✓ | Not run |
| T10 | Onderwerp: Herinnering: GitHub-link posten<br><br>Post de link naar je GitHub-pull-request in de juiste week op Canvas. Punten worden alleen via Canvas gegeven; zonder link in de juiste week is er geen score. | Yes — T06 | herhaling | It is the same sender, subject and message as T06, with no useful new information. | Own school email, anonymised | herhaling ✓ | Not run |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Nieuwe T11–T30 — vooraf beantwoord

| ID | Geanonimiseerde input | Bron/type | Verwacht label vooraf | Eigen reden |
| --- | --- | --- | --- | --- |
| T11 | **Onderwerp:** Info Team United — Vraag schoolopdracht Copywriting & Storytelling. **Bericht:** Een externe opdrachtgever vraagt om de opdrachtomschrijving en extra informatie. | echte inbox, werk | `doen` | De opdrachtgever vraagt extra informatie om duidelijk te maken wat er verwacht wordt. |
| T12 | **Onderwerp:** Copywriting & Storytelling — Tweede deadline op vrijdag 30 oktober om 9 uur. **Bericht:** De tweede deadline nadert en de mail verwijst naar de briefing en het stappenplan. | echte inbox, werk | `lezen` | Je moet weten wanneer het moet ingediend zijn. Het is informatie |
| T13 | **Onderwerp:** Copywriting & Storytelling — Tweede deadline op vrijdag 30 oktober om 9 uur. **Bericht:** Een tweede bericht heeft dezelfde deadline en inhoud. | echte inbox, herhaling | `herhaling` | Zelfde mail als mail 2 |
| T14 | **Onderwerp:** Groep Canva: Graphic Design. **Bericht:** Je wordt uitgenodigd om toe te treden tot de Canva-groep van Graphic Design. | echte inbox, school | `doen` | Je word verwacht de uitnodiging te accepteren |
| T15 | **Onderwerp:** Copywriting & Storytelling — Eerste deadline niet gehaald? Een paar gouden tips!. **Bericht:** De eerste deadline is niet gehaald; de mail legt de gevolgen voor het eindcijfer uit. | echte inbox, school | `lezen` | Informatie wat betreft de deadline die je gemist hebt |
| T16 | **Onderwerp:** Bedankt voor je deelname aan de UBA Online Master Class. **Bericht:** De presentatie staat klaar en feedback geven is mogelijk maar vrijblijvend. | echte inbox, opleiding | `lezen` | Je krijgt te weten dat je het materiaal kunt herbekijken, feedback is vrijblijvend, daarom is doen hier niet gepast |
| T17 | **Onderwerp:** Tussentijdse feedback, coaching en planning eindpresentaties. **Bericht:** De mail beschrijft coaching, feedbackmomenten en planning; inschrijven is alleen nodig als je feedback wilt. | echte inbox, school | `doen` | indien je feedback wil moet je inschrijven zoniet hoef je dat niet te doen |
| T18 | **Onderwerp:** Mondeling examen: Case Groep 1 - 16/10/2026. **Bericht:** De case en praktische informatie zijn bedoeld voor groep 1. | echte inbox, examen | `negeren` | als je in groep 1 zit is deze cased van toepassing voor jou, ik zat in groep 2 dus deze mail is niet voor mij bedoeld |
| T19 | **Onderwerp:** Mondeling examen: Case Groep 2 - 19/10/2026. **Bericht:** De case en praktische informatie zijn bedoeld voor groep 2. | echte inbox, examen | `lezen` | dit is mijn groep, dus deze case is van toepassing voor mijn mondeling examen. Ik moet het dus lezen |
| T20 | **Onderwerp:** Herinnering: je betaalde je studiegeld nog niet. **Bericht:** De betaling ontbreekt ondanks een eerdere herinnering en moet in orde worden gebracht. | echte inbox, administratie | `doen` | Ik had het studiegeld nog niet betaald ondanks een herinnering, dit moet je doen om toegang te behouden tot de digitale leeromgeving |
| T21 | **Onderwerp:** Recente opmerkingen op Canvas. **Bericht:** Een Canvas-rapport meldt dat een inleverdatum is gewijzigd. | echte inbox, school | `lezen` | Kijken naar de deadlines die gemaakt zijn. Niets doen voorlopig |
| T22 | **Onderwerp:** [GitHub] Your fine-grained personal access token is about to expire. **Bericht:** GitHub meldt dat de token binnenkort vervalt en opnieuw aangemaakt kan worden. | echte inbox, beveiliging | `doen` | de token is nogsteeds nodig, dus ik hernieuw het. |
| T23 | **Onderwerp:** KEMPES BV: Service Rating Request. **Bericht:** Een externe dienst vraagt om een beoordeling van de service. | echte inbox, irrelevante service-mail | `negeren` | irrelevante mail |
| T24 | **Onderwerp:** Inlevering gepost: BUR evaluatie 1. **Bericht:** Een Canvas-melding zegt dat punten en nieuwe opmerkingen zichtbaar zijn. | echte inbox, examen | `lezen` | indien je de punten wilt weten van je mondeling examen is dit nuttig om te lezen, als dit je helemaal niets intereseert kan negeren van toepassing zijn, maar dat is in mijn geval niet zo, dus lezen. |
| T25 | **Onderwerp:** Feedbacksessie Perceptieproces. **Bericht:** Voor feedback op de opdracht kan je via Canvas een moment inschrijven; dat is niet voor iedereen nodig. | echte inbox, opleiding | `lezen` | als je feedback wilt op je opdracht, dan laat de mail je weten dat je kunt inschrijven, dat is niet voor iedereen van toepassing, ik weet het nog niet dus mometeel lezen voor mij. |
| T26 | **Onderwerp:** Nieuwsbrief 23 oktober 2026. **Bericht:** Een algemene nieuwsbrief bevat nieuws van Arteveldehogeschool. | echte inbox, nieuwsbrief | `negeren` | nieuwsbrieven lees ik nooit. Niet nuttig voor mij. |
| T27 | **Onderwerp:** Arteveldehogeschool Daily Digest. **Bericht:** Een automatische digest herhaalt algemene meldingen zonder nieuwe actie. | echte inbox, automatische digest | `negeren` | deze mail biedt geen nieuwe informatie die ik nog niet weet. Irrelevant. |
| T28 | **Onderwerp:** Cours du 13/10 ou du 16/10: rectification. **Bericht:** De leerkracht verduidelijkt waarover de volgende les zal gaan. | echte inbox, andere taal | `lezen` | De leerkracht laat weten waarover de les zal gaan de volgende keer |
| T29 | **Onderwerp:** Publicatie punten en feedbackdag: Data skills (2025-26 S1). **Bericht:** Een bericht van vorig semester bevat algemene punten- en feedbackinformatie. | echte inbox, vorig semester | `negeren` | dit is van vorig semester en dus niet meer van toepassing |
| T30 | **Onderwerp:** Welcome to Canva. **Bericht:** Canva geeft algemene informatie over een bestaand account en functies. | echte inbox, software | `negeren` | algemene informatie over de canva app die eigenlijk niet nodig is. |

## Verdeling nieuwe inputs

- 10 echte inboxinputs met bron/type: T11–T20.
- 6 randgevallen: T17, T18, T23, T25, T27 en T28.
- 4 inputs waarbij `negeren` de juiste keuze is door irrelevantie, herhaling of ontbrekende persoonlijke relevantie: T23, T26, T27 en T29.

## Meting

Eén run van de laatste v3-prompt op alle 30 inputs. De score wordt genoteerd als `n/30 (set v2, 1 run)`. De verwachte labels zijn vooraf vastgelegd en worden na de run niet aangepast.
