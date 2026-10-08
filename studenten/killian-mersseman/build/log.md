# Logboek

Elke run, elk resultaat, elke wijziging. Wis nooit een fout.

| Datum | Versie | Wat ik deed | Resultaat | Fout of opvallend | Volgende stap |
|---|---|---|---|---|---|
| Vóór 8 oktober 2026; exacte datum niet vastgelegd | v1 | v1 gemaakt | Eerste prompt voor het vergelijken van twee kwartaalrapporten. | Eerdere resultaten staan in test-set.md. | Prompt verbeteren op basis van de tests. |
| Vóór 8 oktober 2026; exacte datums niet vastgelegd | v1 en eerdere v2, soms met aanvullende instructies | Vijf testinputs minstens tweemaal uitgevoerd. | Resultaten en verschillen vastgelegd in test-set.md. | Promptversies en bronvormen verschillen; bronclaims en enkele invoerinstructies zijn nog te controleren. Nog geen volledig beoordeeld succespercentage. | Resterende controles uitvoeren en fouten classificeren. |
| 8 oktober 2026 | Aangepaste v2 | Promptaudit: bouwstenen B1–B6 besproken en gelabeld; doel, drie voorbeelden en een regel met “want” toegevoegd op basis van mijn antwoorden. | Alle zes bouwstenen zijn aanwezig. | De audit bewijst nog niet dat de prompt werkt. | Buurtest uitvoeren. |
| 8 oktober 2026 | Aangepaste v2 | FCF-perioderegel gewijzigd: voorkeur voor hetzelfde kwartaal; anders beschikbare gemeenschappelijke perioden tonen en op mijn keuze wachten. | Automatische halfjaarkeuze vervangen door een keuzevraag. | Nog niet getest. | Relevante inputs opnieuw draaien met deze regel. |
| 8 oktober 2026 | Aangepaste v2 | Omzetgroeiregel aangevuld: gerapporteerd percentage als hoofdwaarde; controleberekening en verschil in procentpunten in de onderbouwing. | AMD-voorbeeld toegevoegd op basis van mijn antwoorden. | Afronding is een mogelijke verklaring voor het verschil, geen vastgestelde oorzaak. Nog niet getest. | Omzetgroei en bronbewijs controleren bij een nieuwe run. |

## Nog te registreren

T07, lokale Run 2: ontvangen na 1 minuut en 2 seconden. Dezelfde omzetbedragen, gerapporteerde en berekende groei, verschillen, kalenderperioden en eigen valuta als Run 1. Geen webzoekacties zichtbaar. Student beoordeelt Run 2 als geslaagd, maar verkiest de compacte vorm van Run 1. T07 afgerond voor omzetgroei: 2 op 2 juist, 100% (n = 1 input, 2 runs). Daarna één vormregel toegevoegd aan v2: bij alleen omzetgroei bevat de eerste tabel alleen de hoofdpercentages en periode; bedragen en berekeningen gaan in de onderbouwing. Die nieuwe regel is nog niet getest.

T07, lokale Run 1: ontvangen na 1 minuut en 7 seconden. JLR −9,6% gerapporteerd en Ferrari +8,0% gerapporteerd, met controleberekening +8,4% voor Ferrari. Bedragen, verschillen in procentpunten, eigen valuta en gelijke datums ondanks afwijkende kwartaalnamen komen overeen met verwachtingen. Geen webzoekacties zichtbaar. Student bevestigde de bedragen en percentages op de lokale bronpagina’s. Run 1 geslaagd voor omzetgroei: 1 op 1 juist (n = 1 input, 1 run). Run 2 ontbreekt.

T06, tweede lokale run: ontvangen na 2 minuten en 19 seconden, zonder zichtbare webzoekacties. Omzetbedragen, groeipercentages, gerapporteerd/berekend labels en perioden zijn gelijk aan lokale Run 1 en de gecontroleerde verwachtingen. Student beoordeelt ook Run 2 als geslaagd. T06 afgerond voor omzetgroei: 2 op 2 juist, 100% (n = 1 input, 2 runs). Geen inhoudelijke fouten binnen deze scope vastgesteld. Aanvullende bronclaims blijven afzonderlijk te controleren.

T06, nieuwe lokale run: uitvoer ontvangen na 2 minuten en 12 seconden. Transcript toont uitsluitend lokale rapportverwerking, zonder webzoekacties. VST −5,5% berekend en CEG 23,0% gerapporteerd komen overeen met de goedgekeurde verwachtingen. Student beoordeelt de omzetgroeitest als geslaagd: 1 op 1 juist (n = 1 input, 1 run), alleen voor omzetgroei. Aanvullende bronclaims blijven afzonderlijk te controleren. Nog één onafhankelijke run onder dezelfde lokale testcondities nodig.

T06 (alleen omzetgroei): ontvangen poging met onleesbare Vistra-link stopte volgens de prompt. Vervolg in hetzelfde gesprek met lokaal Vistra-PDF leverde de verwachte omzetcijfers en percentages op. Bronverwijzingen nog controleren. Transcript bevat webzoekacties, dus de poging voldoet niet aan de afgesproken conditie zonder web search. Bronwijziging en beperkingen zijn vastgelegd in test-set.md; geen definitieve succesbeoordeling.

- Buurtest: datum, drie gebruikte inputs, antwoorden van de klasgenoot en eventuele verschillen.
- Nieuwe runs: gebruikte promptversie, eventuele aanvullende instructies en mijn eventuele periodekeuze.
- Foutklassen F1–F6 en succespercentage met aantal inputs en runs.
- Resultaat vóór en na een afzonderlijke wijziging. De aangepaste v2 bevat meerdere wijzigingen; een verschil in resultaat is daardoor niet zonder meer aan één wijziging toe te schrijven.

- T08 Run 1: student beoordeelt de lokale omzetgroeivergelijking PepsiCo/Coca-Cola als geslaagd en noemt de tabel met onderbouwing zeer duidelijk. Kerncijfers en afzonderlijke kwartaalperioden stemmen overeen met vooraf goedgekeurde verwachtingen. Tussenstand 1/1 (n = 1 input, 1 run); Run 2 nog te doen.

- T08 Run 2: student beoordeelt de uitvoer als geslaagd en gelijklopend met Run 1. Eindstand T08: 2/2 geslaagd, 100% (n = 1 input, 2 runs), voor omzetgroei met expliciet verschillende kwartaalperioden. Geen wisselende kernuitvoer vastgesteld.

- T09 Run 1: student beoordeelt de vergelijking Rheinmetall/Lockheed Martin als geslaagd. Kerncijfers stemmen overeen met vooraf goedgekeurde verwachtingen; verschillende kwartaalperioden en voortgezette activiteiten vermeld. Tussenstand 1/1 (n = 1 input, 1 run); Run 2 nog te doen.

- T09 Run 2: student beoordeelt de uitvoer als geslaagd. T09 afgerond: 2/2 geslaagd, 100% (n = 1 input, 2 runs), voor omzetgroei. Kerncijfers blijven gelijk; inleidende USD-zin in Run 2 is een formuleringverbeterpunt.

- T10: student beoordeelt beide lokale runs als geslaagd. Eindstand 2/2, 100% (n = 1 input, 2 runs). T06–T10 samen: 10/10 geslaagde omzetgroeiruns (n = 5 inputs, 2 runs per input); geen totaalscore voor alle tien inputs vastgesteld.

- Controle T01–T05: T03 aanvullende invoer niet meer bekend volgens student; FCF-afwijking blijft zichtbaar zonder bewezen instructiefout. T05 studentbeoordeling voor omzetgroei: Run 1 niet geslaagd, Run 2 geslaagd; 1/2 (50%, n = 1 input, 2 runs). Persoonlijke voorkeur voor gerapporteerde cijfers volgens student pas vanaf T06 expliciet meegegeven; niet achteraf toepassen als instructie. Overige T05-bronclaims niet volledig gevalideerd.

- T04: student beoordeelt beide runs als geslaagd voor financiële kerncijfers (FCF, schuld, omzetgroei, eigen valuta). Score 2/2, 100% (n = 1 input, 2 runs). Risicobronnen en aanvullende claims blijven niet volledig gecontroleerd.

- B5 aangescherpt op verzoek student: bij onzekerheid concreet onderdeel, bronbeperking, invloed en benodigde aanvullende informatie vermelden, zodat student zelf kan beslissen. Bestaande regel vroeg al om uitleg; verduidelijking na T10, nog niet getest. Geen eerdere runbeoordelingen gewijzigd.

- T02: beide runs volgens student bruikbaar, maar niet volledig geslaagd vanwege schuldonzekerheid en wisselende zekerheid. Score volledig geslaagde financiële kernruns 0/2 (n = 1 input, 2 runs); F6 in onzekerheidslabel, geen bewezen fout schuldentotaal. FCF en omzetgroei blijven numeriek overeenkomstig.

- T01: eerdere interpretatie als goedkeuring van v1 Run 2 gecorrigeerd door student: “ik bedoel enkel V2 niet V1”. Alleen de ontvangen oudere v2-run is bruikbaar en geslaagd: 1/1 (n = 1 input, 1 run). V1-runs blijven zonder definitieve studentbeoordeling; geen geldige v1-score 1/2. Tweede onafhankelijke oudere v2-run ontbreekt.

- T01 nieuwe lokale run met opgeslagen week-2-v2: student beoordeelt financiële kerncijfers als geslaagd. 1/1 (n = 1 input, 1 run), zonder zichtbare webzoekacties. Historische v2-run apart wegens niet volledig gereconstrueerde invoer; tweede run onder dezelfde lokale condities nog te doen.

- T01 lokale Run 2: student beoordeelt financiële kerncijfers als geslaagd. Nieuwe lokale reeks met opgeslagen oudere v2 afgerond: 2/2, 100% (n = 1 input, 2 runs). Kernbedragen gelijk; schuldafbakening explicieter in Run 2. Historische run en aanvullende ongecontroleerde claims blijven apart.

- T03 afgesloten op keuze student: bruikbaar met beperking; geen nieuwe test. Twee PDF-runs met S&P-bedrijfs-FCF 2.249 versus gekozen uniforme 2.411 blijven zichtbaar. Aanvullende invoer onbekend; geen bewezen instructiefout en niet meetellen als volledig gecontroleerd geslaagd.

## Gekozen wijziging voor reflectie — antwoord student

Student kiest de FCF-perioderegel: “kwartaalresultaten direct te veranderen naar halfjaarcijfers, nu moet hij dit vragen en de mogelijkheden meegeven”.

Voorheen koos de oudere v2 bij ontbrekende kwartaal-FCF automatisch het gemeenschappelijke halfjaar. De huidige v2 moet beschikbare gemeenschappelijke perioden tonen, om de periodekeuze vragen en op het antwoord wachten. Dit is de door student gekozen wijziging voor de week-3-reflectie. De nieuwe lokale T01-runs gebruiken de oudere v2 en bewijzen dus niet dat de nieuwe keuzevraagregel werkt. Een afzonderlijke test van die regel is nog niet vastgelegd. De eigen motivatie van de student nog uitvragen voordat de post wordt geschreven.

### Eigen motivatie van de student

“Ik wil zelf kiezen omdat soms de kwartalen wat afwijken en ik als mens toch kan beslissen dat dit bruikbaar is of niet.”

De student wil dus zelf de bruikbaarheid van afwijkende verslagperioden beoordelen, met de verschillen zichtbaar. Onderscheid voor reflectie: de huidige FCF-regel vraagt om beschikbare gemeenschappelijke perioden en verbiedt rechtstreekse FCF-vergelijking zonder gemeenschappelijke periode; bij omzetgroeitests T08/T09 accepteerde de student expliciet eigen kwartaalperioden met verschillen vermeld. De motivatie verandert de FCF-regel niet automatisch in toestemming om ongelijke FCF-perioden rechtstreeks te vergelijken. Nog geen afzonderlijke test van de nieuwe FCF-keuzevraag geregistreerd.

- Gerichte T01-hertest met huidige v2, zonder vooraf gekozen FCF-periode: tool toont halfjaar 2026/2025, vraagt keuze en wacht zonder berekening. Gewenst gedrag waargenomen (n = 1 input, 1 run), studentbeoordeling nog gevraagd. Oudere v2 koos automatisch halfjaar 2026. Andere promptwijzigingen en ongecontroleerde bronpaginanummers beperken de conclusie; geen volledige financiële succesrun claimen.

- Student beoordeelt de gerichte FCF-keuzevraagtest als geslaagd: 1/1 (n = 1 input, 1 run), alleen voor keuze tonen/vraag stellen/wachten. Resultaat voor gekozen wijziging vastgelegd; één test en meerdere overige promptwijzigingen vormen geen bewijs van algemene betrouwbaarheid.

### Wat de student verraste tijdens het testen

“hoe gelijk de 2 tests altijd zijn, ik weet dat het dezelfde cijfers zijn maar toch klopt het altijd. De tabels verbeteren met elke input”

Voor de post feitelijk begrenzen: de student is verrast door hoe gelijk de herhaalde uitvoer vaak is. T06–T10 hebben dezelfde gecontroleerde kerncijfers in beide runs; T05 AMD en T02 Alphabet-zekerheid hadden wel verschillen. De student vindt de tabellen gaandeweg beter. De vormregels zijn tijdens het traject aangepast; geen bewijs dat het model zelfstandig leert van onafhankelijke inputs. De eigen uitleg van de student waarom herhaalbaarheid geen bewijs van juistheid is, nog uitvragen.

- Conceptpost posts/week-03.md gemaakt op basis van studentantwoorden, inclusief correctie “zo goed als altijd overeen”, eigen uitleg waarom herhaling geen bewijs is, scope van succespercentage, fouten en ontbrekende buurtest. Nog door student te lezen; niet ingediend.

- Student keurt posts/week-03.md goed met “is goed”. Post bevat 382 woorden en is klaar voor indiening. Nog niet gecommit, gepusht of als pull request ingediend. Ontbrekende buurtest en beperkingen staan expliciet vermeld.
