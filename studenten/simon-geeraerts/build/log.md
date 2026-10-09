# Logboek

## v1 — 7 oktober 2026

- Gebouwd: lokale website met een formulier voor bestelbonnummer, naam en klantvraag.
- Gegevens: drie volledig fictieve bestellingen in `orders.mjs`.
- Regel: de assistent antwoordt alleen uit de gevonden bestelling en behandelt een aankomstdatum bij de garage niet als afhaaldatum.
- Nog niet gemeten: de testset moet eerst door Simon worden aangevuld met vooraf bepaalde juiste antwoorden.

## v1.1 — 7 oktober 2026

- Toegevoegd: de assistent leest automatisch het bestand `data/bestellingen.xlsx` wanneer de garage dit wekelijks bijwerkt.
- De klant ziet geen uploadscherm. De assistent gebruikt bij de volgende vraag de nieuwste opgeslagen Excelversie.
- Nog te verbeteren voor echt gebruik: de map met het Excelbestand mag alleen toegankelijk zijn voor bevoegde medewerkers.

## v1.2 — 7 oktober 2026

- Toegevoegd: bij elke bekende aankomstdatum staat verplicht dat dit geen afhaaldatum is.
- De assistent vermeldt ook dat tijd voor ombouw, reiniging, nummerplaten en papieren niet in de aankomstdatum is meegerekend. Hij berekent geen afhaaldatum.

## v1.3 — 7 oktober 2026

- Beslist: elk bestelbonnummer bestaat uit precies vijf cijfers.
- De website en het Excelbestand controleren dit formaat.

## v1.4 — 7 oktober 2026

- De assistent vraagt eerst vriendelijk om het vijfcijferige bestelbonnummer en daarna om de naam op de bestelling.
- Bij een bekende aankomstdatum zegt hij dat dit geen leverings- of afhaaldatum is. De verkoper neemt contact op om de levering verder af te spreken.

## v1.5 — 7 oktober 2026

- Aangepast naar de gewenste klantvriendelijke formulering: de assistent vraagt om het bestelbonnummer met “uw”.
- De verkoper legt daarna met de klant een datum voor de levering vast.

## v1.6 — 7 oktober 2026

- Toegevoegd: een demomodus zonder API-sleutel, zodat Simon de klantstroom met fictieve gegevens kan testen.
- De demo vermeldt duidelijk dat het antwoord nog zonder AI wordt gemaakt.

## v1.7 — 9 oktober 2026

- Gemeten: 3 op 5 juist (n = 5, 1 run). Twee antwoorden misten de naam Ford Geeraerts; beide kregen foutcode F3 (gemist).
- Gewijzigd: elk antwoord krijgt nu de vaste aanhef “Ford Geeraerts”.
- Hertest: de twee eerdere F3-fouten zijn allebei opgelost (2 op 2).

## v1.8 — 9 oktober 2026

- Buurtest: een medestudent vond de regel over de vaste uitleg na aankomst tegenstrijdig met het voorbeeld.
- Gewijzigd: de AI noemt alleen status en verwachte aankomst; de toepassing voegt daarna de uitleg over afhaling toe.
- Hertest met de medestudent: de verdeling is nu duidelijk.
