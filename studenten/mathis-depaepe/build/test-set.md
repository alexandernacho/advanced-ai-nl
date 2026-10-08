# Testset

Het juiste antwoord staat er vóór de eerste run. Namen van verkopers zijn weggelaten. De volledige advertenties staan onder de tabel.

Beoordelingsregel: bij `servicegeschiedenis` telt dezelfde inhoud in andere woorden als juist.

| ID | Input | Juiste antwoord | Waarom | Run 1 | Run 2 |
|---|---|---|---|---|---|
| T01 | Rolex Datejust 1603, particulier, NL (zie onder) | merk: Rolex<br>model: Datejust<br>referentienummer: 1603<br>bouwjaar: 1970<br>staat: zeer goed<br>doos_papieren: geen<br>vraagprijs: 4195<br>munt: EUR<br>verkoper: particulier<br>servicegeschiedenis: onbekend | Merk, model, referentienummer, bouwjaar, staat, ontbreken van doos en papieren, prijs en particuliere verkoper staan rechtstreeks in de advertentie. Servicegeschiedenis wordt niet vermeld. Bouwjaar 1970, omdat de advertentie letterlijk "Bouwjaar 1970 (Schatting)" vermeldt. | 10/10 juist | 10/10 juist |
| T02 | Omega Seamaster Dynamic vintage, particulier, FR (zie onder) | merk: Omega<br>model: Seamaster Dynamic<br>referentienummer: onbekend<br>bouwjaar: onbekend<br>staat: gedragen<br>doos_papieren: onbekend<br>vraagprijs: 650<br>munt: EUR<br>verkoper: particulier<br>servicegeschiedenis: onbekend | De advertentie noemt Omega Seamaster Dynamic, calibre 1430, gebruikssporen en kleine krassen en een prijs van €650. Er wordt geen referentienummer, bouwjaar, informatie over doos of papieren of servicegeschiedenis vermeld. De staat is "gedragen" omdat de advertentie enkele gebruikssporen en kleine krassen vermeldt. "Calibre 1430" is geen referentienummer. Bouwjaar niet afleiden uit "vintage" of het kaliber. | 10/10 juist | 10/10 juist |
| T03 | Rolex Datejust 41, handelaar, DE (zie onder) | merk: Rolex<br>model: Datejust 41<br>referentienummer: onbekend<br>bouwjaar: 2025<br>staat: zeer goed<br>doos_papieren: enkel doos<br>vraagprijs: 10500<br>munt: EUR<br>verkoper: handelaar<br>servicegeschiedenis: onbekend | De advertentie vermeldt Rolex Datejust 41, bouwjaar/koopdatum 2025, zeer goede staat, een aanwezige Rolex-box en geen expliciete garantiekaart of certificaat. De overige documenten worden alleen vaag genoemd als "weitere Unterlagen/Zubehör", waardoor dit volgens onze regel niet als papieren telt. Ook "Papieren" in de titel telt niet: alleen een expliciet genoemde garantiekaart of certificaat telt als papieren. Het referentienummer en de servicegeschiedenis worden niet vermeld. "Gewerblicher Nutzer" = handelaar. | 10/10 juist | 10/10 juist |
| T04 | Audemars Piguet Royal Oak Offshore Safari, handelaar, NL (zie onder) | merk: Audemars Piguet<br>model: Royal Oak Offshore<br>referentienummer: 26020ST.OO.D091CR.01<br>bouwjaar: 2012<br>staat: zeer goed<br>doos_papieren: enkel doos<br>vraagprijs: 16995<br>munt: EUR<br>verkoper: handelaar<br>servicegeschiedenis: laatste revisie 8 mei 2026 (interne revisie) | Staat "zeer goed": lichte gebruikssporen, een paar krasjes die niet opvallen. "Full set" in de titel en "met originele papieren" in de vaste velden zijn algemene vermeldingen en tellen niet als papieren. Het "echtheidscertificaat" op de pagina is uitleg van Chrono24, niet iets dat de verkoper meelevert. | 9/10 juist (doos_papieren fout, F1) | 9/10 juist (doos_papieren fout, F1) |
| T05 | Tudor Black Bay Chrono Panda, particulier, NL (zie onder) | merk: Tudor<br>model: Black Bay Chrono<br>referentienummer: onbekend<br>bouwjaar: onbekend<br>staat: zeer goed<br>doos_papieren: onbekend<br>vraagprijs: 3999<br>munt: EUR<br>verkoper: particulier<br>servicegeschiedenis: onbekend | Referentienummer en bouwjaar staan niet in de tekst, dus "onbekend", ook al is het referentienummer van dit model bekend. Het hoogste bod (€ 3.800) is geen vraagprijs. Staat "zeer goed": "zeer weinig gedragen" betekent gedragen, dus niet "nieuw", ondanks "zo goed als nieuw". Doos, papieren en service worden niet vermeld. | 10/10 juist | 10/10 juist |

Resultaat na run 1 en 2: 98 op 100 velden juist. Beide fouten: T04 doos_papieren (F1), in beide runs hetzelfde.

## Inputs

### T01

```
Titel: Rolex Datejust 36 Rolex Oyster Perpetual Datejust – Tijdloze Klassieker – Zond

Tekst:
Tweedehands (Zeer goed) | Bouwjaar 1970 (Schatting) | Zonder originele doos | Zonder originele papieren

€ 4.195

Basisgegevens:
* Merk: Rolex
* Collectie: Datejust
* Model: Datejust
* Referentienummer: 1603
* Opwinden: Automatisch
* Materiaal horlogekast: Staal
* Materiaal horlogeband: Staal
* Bouwjaar: 1970 (Schatting)
* Staat: Tweedehands (Zeer goed)
* Het product heeft lichte gebruikssporen, zoals een paar krasjes, maar deze vallen niet op.
* Inbegrepen bij de levering: Zonder originele doos, zonder originele papieren
* Geslacht: Herenhorloge/Unisex
* Locatie: Nederland
* Prijs: € 4.195 (Vraagprijs)
* Beschikbaarheid: Product op voorraad

Beschrijving:
Mooi klassiek horloge. Verkeerd in zeer goede staat. Lichte gebruikssporen van het dragen. Ik heb het horloge uit een erfenis en vindt het een te duur horloge om zelf te dragen.

Verkoper: particulier
```

### T02

```
Titel: Omega Seamaster Dynamic vintage – Calibre 1430

Tekst:
Je vends une Omega Seamaster Dynamic vintage, avec mouvement quartz Omega calibre 1430. Très jolie montre avec son cadran noir/crème et ses détails rouges. Bracelet d’origine Omega. La montre présente quelques traces d’usure et petites rayures liées à son âge, visibles sur les photos. Vendue dans son état actuel. Prix : 650 €. Faire offre raisonnable. Possibilité seulement de remise en main propre.

Verkoper: particulier
```

### T03

Bron: kleinanzeigen.de, advertentie 3534218681.

```
Titel: Rolex Datejust 41mm mit Box und Papieren

Tekst:
Zum Verkauf steht eine Rolex Datejust 41 mit dem begehrten Wimbledon-Zifferblatt aus 2025.

Die Uhr befindet sich in einem sehr guten, unpolierten Zustand. Dadurch sind die originalen Konturen und Oberflächen erhalten. Die Kombination aus dem grauen Wimbledon-Zifferblatt mit grünen römischen Indizes, glatter Lünette und Jubilee-Band wirkt sportlich und gleichzeitig elegant.

Ausstattung / Details:
* Rolex Datejust 41
* Wimbledon-Zifferblatt
* Glatte Lünette
* Jubilee-Armband
* Edelstahl
* Baujahr / Kaufdatum: 2025
* Unpoliert
* Sehr guter Zustand
* Rolex Box vorhanden
* Weitere Unterlagen/Zubehör je nach Lieferumfang

Preis: 10.500 € VB
Art: Uhren
Zustand: Sehr Gut
Material: Stahl

Verkoper: handelaar (Gewerblicher Nutzer)
```

### T04

Bron: chrono24.nl, advertentie id46293295.

```
Titel: Audemars Piguet Royal Oak Offshore
Safari 26020s ''Full set 2012'' Like new!

Tekst:
Tweedehands (Zeer goed) | Bouwjaar 2012 | Met originele doos | Met originele papieren
€ 16.995

Locatie: Nederland, Franeker

Basisgegevens
Merk: Audemars Piguet
Collectie: Royal Oak Offshore
Model: Royal Oak Offshore
Referentienummer: 26020ST.OO.D091CR.01
Opwinden: Automatisch
Materiaal horlogekast: Staal
Materiaal horlogeband: Leer
Bouwjaar: 2012
Staat: Tweedehands (Zeer goed)
Het product heeft lichte gebruikssporen, zoals een paar krasjes, maar deze vallen niet op.
Most Recent Servicing: 8 mei 2026 Interne revisie
Inbegrepen bij de levering: Met originele doos, met originele papieren
Prijs: € 16.995

Verkoper: handelaar (Professionele handelaar)
```

### T05

Bron: 2dehands.be, advertentie m2422923233.

```
Titel: Tudor Black Bay (panda)

Tekst:
€ 3.999,00
Conditie: Zo goed als nieuw
Beschrijving:
Tudor Black Bay Chrono - Panda
Zeer weinig gedragen - uitstekende conditie
Biedingen: hoogste bod € 3.800,00

Verkoper: particulier
```

## Runs

Letterlijke uitvoer van elke run.

### T01 run 1

```json
{"merk":"Rolex","model":"Datejust","referentienummer":"1603","bouwjaar":1970,"staat":"zeer goed","doos_papieren":"geen","vraagprijs":4195,"munt":"EUR","verkoper":"particulier","servicegeschiedenis":"onbekend"}
```

### T01 run 2

```json
{"merk":"Rolex","model":"Datejust","referentienummer":"1603","bouwjaar":1970,"staat":"zeer goed","doos_papieren":"geen","vraagprijs":4195,"munt":"EUR","verkoper":"particulier","servicegeschiedenis":"onbekend"}
```

### T02 run 1

```json
{"merk":"Omega","model":"Seamaster Dynamic","referentienummer":"onbekend","bouwjaar":"onbekend","staat":"gedragen","doos_papieren":"onbekend","vraagprijs":650,"munt":"EUR","verkoper":"particulier","servicegeschiedenis":"onbekend"}
```

### T02 run 2

```json
{"merk":"Omega","model":"Seamaster Dynamic","referentienummer":"onbekend","bouwjaar":"onbekend","staat":"gedragen","doos_papieren":"onbekend","vraagprijs":650,"munt":"EUR","verkoper":"particulier","servicegeschiedenis":"onbekend"}
```

### T03 run 1

```json
{"merk":"Rolex","model":"Datejust 41","referentienummer":"onbekend","bouwjaar":2025,"staat":"zeer goed","doos_papieren":"enkel doos","vraagprijs":10500,"munt":"EUR","verkoper":"handelaar","servicegeschiedenis":"onbekend"}
```

### T03 run 2

```json
{"merk":"Rolex","model":"Datejust 41","referentienummer":"onbekend","bouwjaar":2025,"staat":"zeer goed","doos_papieren":"enkel doos","vraagprijs":10500,"munt":"EUR","verkoper":"handelaar","servicegeschiedenis":"onbekend"}
```

### T04 run 1

```json
{"merk":"Audemars Piguet","model":"Royal Oak Offshore","referentienummer":"26020ST.OO.D091CR.01","bouwjaar":2012,"staat":"zeer goed","doos_papieren":"full set","vraagprijs":16995,"munt":"EUR","verkoper":"handelaar","servicegeschiedenis":"Interne revisie op 8 mei 2026"}
```

### T04 run 2

```json
{"merk":"Audemars Piguet","model":"Royal Oak Offshore","referentienummer":"26020ST.OO.D091CR.01","bouwjaar":2012,"staat":"zeer goed","doos_papieren":"full set","vraagprijs":16995,"munt":"EUR","verkoper":"handelaar","servicegeschiedenis":"Interne revisie op 8 mei 2026"}
```

### T05 run 1

```json
{"merk":"Tudor","model":"Black Bay Chrono","referentienummer":"onbekend","bouwjaar":"onbekend","staat":"zeer goed","doos_papieren":"onbekend","vraagprijs":3999,"munt":"EUR","verkoper":"particulier","servicegeschiedenis":"onbekend"}
```

### T05 run 2

```json
{"merk":"Tudor","model":"Black Bay Chrono","referentienummer":"onbekend","bouwjaar":"onbekend","staat":"zeer goed","doos_papieren":"onbekend","vraagprijs":3999,"munt":"EUR","verkoper":"particulier","servicegeschiedenis":"onbekend"}
```
