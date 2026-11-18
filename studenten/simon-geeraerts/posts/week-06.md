# Week 6: Vindbaarheid voor AI

## Mijn live query

**Vraag:** Welke Ford-garages in het Pajottenland zijn goed voor de aankoop van een nieuwe wagen?

| Run | Genoemde garages | Pagina's die de AI las | Opmerking |
| --- | --- | --- | --- |
| Eigen AI 1 | Ford Geeraerts Lennik, Thoen Ninove, Vanspringel Anderlecht | Europages, LinkedIn, Reddit en andere zoekresultaten | Ford Geeraerts stond als eerste keuze. De zoekopdrachten van de AI waren niet zichtbaar in het bronnenpaneel. |
| Eigen AI 2 | Ford Geeraerts Lennik, Thoen Ninove, Thoen Aalst | LinkedIn, GoCar, Groep Thoen, Reddit en andere zoekresultaten | Ford Geeraerts stond opnieuw als eerste keuze. |
| Google AI-modus | Ford Geeraerts Lennik, Thoen en AB Automotive | Vooral de website van Geeraerts, Facebook en Autogroep Thoen | Ford Geeraerts werd als voornaamste officiële Ford-concessiehouder genoemd. |

Een kenner van de markt zou dezelfde garages noemen: alle belangrijke Ford-garages in deze regio werden genoemd. Er ontbrak dus geen belangrijke Ford-garage. Run 2 en Google AI-modus noemden niet exact dezelfde lijst, maar Ford Geeraerts en Thoen kwamen wel telkens terug.

Ford Geeraerts wordt wel genoemd omdat het bedrijf veel positieve online reviews en vermeldingen heeft, zichtbaar is op LinkedIn en Facebook, officieel Ford-verdeler is en als familiaal, gerenommeerd bedrijf in het Pajottenland bekendstaat. Het won ook meerdere Ford President's Awards voor klantentevredenheid.

## Kan AI dit bedrijf vinden?

| Criterium | Score en bewijs |
| --- | --- |
| 1. Gestructureerde data | **1/3.** De pagina [Nieuwe voertuigen](https://www.geeraerts.be/product) toont in validator.schema.org alleen `BreadcrumbList`. Er staat geen `Product`, `Service`, `FAQPage`, prijs of review-data in de gestructureerde data. |
| 2. Leesbaar voor AI | **3/3.** De productpagina is duidelijk opgebouwd per model, met categorieën bovenaan. Per wagen staat een prijs of “prijs op aanvraag”, plus een knop voor meer informatie. |
| 3. Vermeldingen door anderen | **2/3.** Google Maps toont Ford Geeraerts met een score van 4,6 op 5 op basis van 335 reviews. Dat is sterke externe klantfeedback, maar ik gebruikte hier maar één externe bron. |
| 4. Echt genoemd in AI-antwoorden | **3/3.** In mijn drie Live Query-runs werd Ford Geeraerts telkens genoemd en als eerste keuze getoond. |
| 5. Autoriteit | **3/3.** Persinfo schrijft dat Garage Geeraerts de Europese Ford President's Award al 12 keer won voor klantentevredenheid in verkoop en service. |
| 6. Zoeken op merknaam | **3/3.** Bij een Google-zoekopdracht naar “Ford Geeraerts” staat de officiële website bovenaan. Ook Google Maps, reviews, Facebook, Instagram, Companyweb en een AI-overzicht zijn zichtbaar. |

**Totaal: 15/18 — aanwezig.**

Mijn eerste tactiek voor Ford Geeraerts: de dealerwebsite wordt vanuit Ford op dezelfde manier gemaakt voor dealers, waardoor Ford Geeraerts dit zelf niet gemakkelijk kan aanpassen. Ik zou Ford daarom aanraden om meer gestructureerde data toe te voegen, zodat de vindbaarheid voor AI verbetert.

## Mijn tool leest een bron

Ik gebruikte de officiële Ford Mustang Mach-E-prijslijst in `build/bronnen/prijslijst-ford-mustang-mach-e.md`.

Ik koos dit document omdat de prijslijst veel informatie bevatte, terwijl openingsuren slechts enkele lijnen met dagen en uren zijn.

Deze oefening sloot niet rechtstreeks aan bij mijn usecase rond bestellingen, maar ik heb dit met de docent besproken.

Mijn score was **5 op 5 juist**. Er ging geen testgeval fout: bij B01 tot en met B04 gaf de bron het gevraagde antwoord, en bij B05 zei de assistent eerlijk dat het document niet vermeldde of twee kleuren tegelijk kunnen worden gekozen.
