# Testset

Juiste antwoord = label (`GO` / `NO-GO` / `ONZEKER`) en bij `NO-GO` de risico's (A, B, C, D). Ingevuld vóór de eerste run.

**Wanneer is een antwoord juist?**
- Het label moet kloppen.
- Bij `NO-GO` moeten alle verwachte risico's erbij staan. Een gemist risico is een fout (F3), ook als het label klopt. Want als ik één probleem oplos, wil ik weten dat er nog een tweede is.
- Een extra risico telt niet als fout, zolang het citaat echt op de pagina staat. Ik noteer het wel als opvallend.
- Staat een citaat niet op de pagina, dan is het altijd een fout (F2), ook als het label klopt.

| ID | Input | Juiste antwoord | Waarom | Run 1 | Run 2 |
|---|---|---|---|---|---|
| T01 | Tote bag — zie T01 hieronder | GO | Het is een gewone katoenen tas zonder merknaam, geen elektronica, licht en niet breekbaar, dus geen van de vier risico's. "Patronen: Cartoon" is op zich geen probleem, maar het is goed als de tool het aankaart. | GO | GO |
| T02 | Hoesje voor AirPods Pro — zie T02 hieronder | GO | Het is een siliconen hoesje dat het merk alleen noemt om te zeggen waarvoor het past, geen namaak. Geen elektronica, licht en niet breekbaar. | GO | GO |
| T03 | USB-oplader 20W — zie T03 hieronder | GO | Het is een oplader met CE-markering, zonder merknaam van een ander merk, klein en niet breekbaar. | GO | GO |
| T04 | Glazen parfumflesjes — zie T04 hieronder | NO-GO (C) | De flesjes zijn van glas en dus breekbaar, wat verzending duurder maakt en tot meer retours door breuk leidt. | NO-GO (C) | NO-GO (C) |
| T05 | Vage titel + foto — zie T05 hieronder | ONZEKER | De titel is een reeks zoekwoorden en de specificaties zijn bijna leeg, dus uit de tekst weet je niet wat het product is of waaruit het bestaat. | ONZEKER | ONZEKER |
| T06 | Mini handventilator — zie T06 hieronder | GO | Het is elektronica met CE-certificaat, eigen merk XIQI, licht en van plastic. De lithiumbatterij is ingebouwd en niet los, dus dat telt niet als risico C. Lastig punt: de tool kan de batterij toch als verzendrisico zien. Tweede valkuil: de tool kan door de disclaimer denken dat CE niet zeker is. Maar de disclaimer is een standaardtekst van Alibaba die niets over dit product zegt, en CE staat er gewoon bij. | | |
| T07 | Collageen gummies — zie T07 hieronder | NO-GO (D) | Het is een voedingssupplement, en dat is beperkt op bol.com. De titel zegt zelf "Gezondheidssupplementen". Lastig punt: bij de specificaties staat "Gummy Candy" en "Snoepgoed", dus de tool kan denken dat het gewoon snoep is en GO zeggen. | | |
| T08 | Pluche Monster Energy-pop — zie T08 hieronder | NO-GO (A, B) | A: de knuffel gebruikt de naam en de look van Monster Energy, een merk van iemand anders. B: het is speelgoed en er staat geen CE. Lastige punten: de merknaam is XINLI, dus de tool kan denken dat er geen merkprobleem is. Er staat "14 Jaar & up", dus de tool kan denken dat het geen speelgoed is. En "Verantwoordelijke EU-persoon" klinkt als in orde, maar het is geen CE. | | |
| T09 | LED-bureaulamp, pagina in het Frans — zie T09 hieronder | NO-GO (B) | Het is een lamp op netstroom, dus elektronica, en er staat nergens CE. Lastige punten: de pagina is in het Frans, dus de tool moet letterlijk in het Frans citeren en niet vertalen. In de titel staat "norme américaine", dat is geen CE. En "Prise: US/EU/UK" klinkt alsof het voor Europa in orde is, maar een EU-stekker is geen CE. | | |
| T10 | Metalen sleutelhanger, korte input — zie T10 hieronder | GO | Het is een metalen sleutelhanger zonder merk van iemand anders, geen elektronica, niet breekbaar en niet verboden. Lastig punt: er staat weinig tekst, dus de tool kan ONZEKER zeggen. Maar het is wel duidelijk wat het product is en van welk materiaal, dus ONZEKER is hier fout. | | |

## Inputs

Plak per ID de tekst van de pagina (titel, beschrijving, specificaties). Vervang echte namen van personen. Zet de link erbij.

### T01
Link: https://www.alibaba.com/product-detail/Big-Tote-Bag-Small-Canvas-Tote_1601157795419.html

```
Titel: cotton tote bag

Maatwerkopties(1)

Logo/grafisch ontwerp
Min. order: 100 stukken
+ vanaf € 1,79/stuk
Maatwerkmogelijkheden van leverancier

Maatwerk voor ontwerpen
Maatwerk voor voorbeelden
Volledig maatwerk
Belangrijkste kenmerken
Materiaal

Katoen, niet geweven stof

Maat

(30cm<Max Length<50cm), (20cm<Max Length<30cm), Grote( max. lengte> 50cm)

Toepassing

Adverteren, Reizen, Supermarkt, Buiten, Dagelijks, Geschenk

Patronen

Cartoon

Land van herkomst

Guangdong, China

Merknaam

OEM

In één oogopslag

Katoenen doekmateriaal: Het gebruik van 100-230 g/m² katoen en 230-600 g/m² doek zorgt ervoor dat de tas zowel duurzaam als milieuvriendelijk is, waardoor deze geschikt is voor herhaald gebruik in verschillende omstandigheden.

Gepersonaliseerde zijdscreenprint: Zijdscreenprint stelt heldere en langdurige aangepaste logo's mogelijk, verhoogt de merkzichtbaarheid en maakt de tassen ideaal voor promotie- of bedrijfsevenementen.

Shipping
$ 50 korting op de eerste verzendbestelling
Ocean freight via  Maersk
Verzendkosten:vanaf € 0,43/kg (min. 50 kg)
Transittijd: Naar verwachting 24-31 dagen
Offerte aanvragen
Of chat met de leverancier van het product voor meer verzendopties.
Orderbescherming van Alibaba.com

Veilige betalingen

Elke betaling die u op Alibaba.com doet, is beveiligd met strikte SSL-codering en PCI DSS-gegevensbeschermingsprotocollen


Geldteruggarantie
Vraag een restitutie aan als uw bestelling niet is verzonden, zoekraakt of met productproblemen aankomt


Vraag verzenden

Nu chatten
Alleen bestellingen die via Alibaba.com zijn geplaatst en betaald, worden gratis beschermd door
Betaling & financiering
Krijg 30 dagen om renteloos te betalen met  
Andere aanbevelingen voor uw bedrijf

Belangrijkste kenmerken
Toepassing
Adverteren, Reizen, Supermarkt, Buiten, Dagelijks, Geschenk
Materiaal
Katoen, niet geweven stof
Maat
(30cm<Max Length<50cm), (20cm<Max Length<30cm), Grote( max. lengte> 50cm)
Meer weergeven
Patronen
Cartoon
Afdichtingen
Shoulder
Stijl
Behandeld, afgehandeld
Verpakking
PP tas
Land van herkomst
Guangdong, China
Merknaam
OEM
Productnaam
Aangepaste katoenen draagtas
Functie
Promotietas, cadeautas, boodschappentas, Recyclebaar, milieuvriendelijk, herbruikbaar, duurzaam
Meer weergeven
Gebruik
Promotie, gift, dagelijks, reizen, winkelen
Logo
Accepteer aangepast logo
Maat
35*40*10cm of aangepast
Kleur
Aangepaste kleur
Materiaal katoen
100-230gsm/canvas: 230-600gsm
Afdrukken
Aangepast logo door zeefdruk/warmteoverdracht afdrukken enz.
Meer weergeven
Moq
200pcs
Verpakking en levering
Selling Eenheden
Enkel item
enkele pakket maat
15X15X5 cm
enkele brutogewicht
0.3 kg
Doorlooptijd
Maatwerkopties
Logo/grafisch ontwerp(+ vanaf +€ 1,79/stuk/Min. bestelling: 100 stukken)
Details weergeven

Nu chatten
Certificaten


RoHS(2)
Conform RoHS

Beschrijving:
In één oogopslag

Katoenen doekmateriaal: Het gebruik van 100-230 g/m² katoen en 230-600 g/m² doek zorgt ervoor dat de tas zowel duurzaam als milieuvriendelijk is, waardoor deze geschikt is voor herhaald gebruik in verschillende omstandigheden.

Gepersonaliseerde zijdscreenprint: Zijdscreenprint stelt heldere en langdurige aangepaste logo's mogelijk, verhoogt de merkzichtbaarheid en maakt de tassen ideaal voor promotie- of bedrijfsevenementen.
```

### T02
Link: https://www.alibaba.com/product-detail/Silicone-Cover-2-3-Cases-Custom_1600860972880.html

```
Titel: Siliconen hoesje 2 3 hoesjes op maat gemaakte hoes, voor Airpods Pro hoesje volledig beschermende mal 3e generatie siliconen

Belangrijkste kenmerken
Type

Case

Gebruik

Airpods beschermen

Merknaam

Neutral

Land van herkomst

Guangdong, China

Materiaal

Siliconen

kenmerk

Milieuvriendelijk

Belangrijkste kenmerken
Type
Case
Gebruik
Airpods beschermen
Materiaal
Siliconen
Functie
Airpods beschermen
Prive-schimmel
NEE
Merknaam
Neutral
kenmerk
Milieuvriendelijk
Land van herkomst
Guangdong, China
Modelnummer
Silicone Airpods Case
Materiaal
Siliconen
Kleuren
Veelkleurig
OEM/ODM-fabrikant
Accepteer OEM/ODM-bestellingen
Pakket
Tas/doos
Functie
Milieuvriendelijk materiaal
Logo
Aangepast logo
Functionaliteit
Airpods beschermen
Ontwerp
Minimalistisch
Stijl
Trendy
Trefwoorden
Voor Apple Airpods/Airpods pro
Verpakking en levering
Packaging Details
Tas/doos
Selling Eenheden
Enkel item
enkele pakket maat
4.9X6.3X2.8 cm
enkele brutogewicht
0.030 kg
Doorlooptijd
Maatwerkopties
Aangepast logo(+ vanaf /Min. bestelling: 50 stukken)
Aangepaste verpakking(+ vanaf /Min. bestelling: 500 stukken)
Grafisch maatwerk(+ vanaf /Min. bestelling: 300 stukken)

Beschrijving: in foto verwerkt (niet als tekst beschikbaar)
```

### T03
Link: https://www.alibaba.com/product-detail/Schitec-Wholesales-20W-Type-c-Charger_1601612265995.html

```
Titel: Schitec Groothandel 20W Type-C opladerset, snellaad wandstekker USB-oplader met 60W USB-C kabel voor het opladen van mobiele apparaten

Maatwerkopties
Logo/grafisch ontwerp+€ 0,18/stuk (Min. order: 1.000 stukken)
Maatwerkmogelijkheden van leverancier

Klein maatwerk
Maatwerk voor ontwerpen
Maatwerk voor voorbeelden
Volledig maatwerk
Belangrijkste kenmerken
poort

Type-C

Uitgang

12 V/1.25A, 9V/2A, 5 V/3A, 5 V/4A, 12 V/1.5A

Ingang

100-240 V/0.4A, 100-240 V/0.8A, 100-240 V/0.6A

Functie

QC3.0, PD, snelle oplader

Uitgangsvermogen

18W, 20W

Materiaal

ABS, PC (glanzend)

Belangrijkste kenmerken
Type
Elektrische, Usb wall charger, Voeding Adapter, Universele Adapter, Fast charger
Meer weergeven
Uitgangsvermogen
18W, 20W
Uitgang
12 V/1.25A, 9V/2A, 5 V/3A, 5 V/4A, 12 V/1.5A
Ingang
100-240 V/0.4A, 100-240 V/0.8A, 100-240 V/0.6A
Functie
QC3.0, PD, snelle oplader
poort
Type-C
Bescherming
Kortsluiting Bescherming, Over-opladen, Overcurrent, Overvoltage
Meer weergeven
gebruik
Mobiele telefoon, Laptop, Game Player, Camera, Oortelefoon, MP3 / MP4 Player, Tablet, Slim horloge, mobiele telefoon of tablet, snellader voor mobiele telefoons
Meer weergeven
Materiaal
ABS, PC (glanzend)
Merknaam
SChitec/OEM
Modelnummer
TC178
Land van herkomst
Guangdong, China
Productnaam
PD 20W USB-oplader met 60W USB-kabel
USB-poort
Type C (enkel/dubbel/drie/1*c/1*c+1*A)
Invoer
100V-240V
Uitgang
3,1A/QC3.0/QC3.0+2A/PD/PD+2A
Kleur
Zwart, wit, aangepast
Stekker
VS/EU/VK/AU
Pakket
PP-zak / geschenkdoos
OEM/ODM
Ondersteuning op maat
Verpakking en levering
Selling Eenheden
Enkel item
Doorlooptijd
Maatwerkopties
Logo/grafisch ontwerp(+ vanaf +€ 0,18/stuk/Min. bestelling: 1.000 stukken)
Details weergeven

Nu chatten
Certificaten


Declaration of Conformity
CE-gecertificeerd

CE
Voldoet aan de EU-normen

UKCA(2)
UK-naleving gecertificeerd

Beschrijving:
In één oogopslag

PD20W-uitvoer: Zorgt voor snelle en efficiënte oplading van compatibele apparaten, waardoor de oplaadtijd wordt verkleind.

ABS-materiaal: Biedt een duurzame en hittebestendige behuizing, waardoor langdurig gebruik en veiligheid worden gegarandeerd.

Overstroombeveiliging: Bescherm het apparaat en de lader tegen schade door overbelasting, waardoor de veiligheid tijdens gebruik wordt verbeterd.
```

### T04
Link: https://www.alibaba.com/product-detail/botella-de-perfume-Glass-perfume-rectangular_1601469297755.html

```
Titel: Botella De Parfum Glas Parfum Rechthoekige Fles 50 Ml Lege Fles Parfum Fles 100Ml Met Boxset

Belangrijkste kenmerken
Type afdichting

Schroefdop

Vorm

Polish and paint

Drukafwerking

Etiketten, Goudfolie, Decorbrand, Matten, Spuiten, Thermische overdracht druk, ZIJDEN SCHERM AFDRUKKEN

Inclusief geurstokjes of niet

Nee

Merknaam

YB

Land van herkomst

Guangxi, China

Belangrijkste kenmerken
Industrieel gebruik
Parfum
Vorm
Polish and paint
Type afdichting
Schroefdop
Inclusief geurstokjes of niet
Nee
Oppervlaktebehandeling
Foliedruk
Drukafwerking
Etiketten, Goudfolie, Decorbrand, Matten, Spuiten, Thermische overdracht druk, ZIJDEN SCHERM AFDRUKKEN
Meer weergeven
Modelnummer
YB
Land van herkomst
Guangxi, China
Merknaam
YB
Basismateriaal
Glass
Materiaal behuizing
Glass
Kraagmateriaal
Glass
Verpakking en levering
Selling Eenheden
Enkel item
Doorlooptijd
Certificaten


FDA CPG
FDA-compatibel

AOAC
Analytische uitmuntendheid

Beschrijving:
Productbeschrijving
Productnaam
Parfumflesje, rechthoekige glazen parfumfles 50 ml, lege parfumfles 100 ml met doos.
Gebruik
Geur
Volume
A. 100 ml 150 ml 200 ml 
B. Volgens het specifieke verzoek van klanten.
Afdichtingstype
Kurk, kroonkurk, schroefdop, swingtop of per klantverzoek
Voorbeeld
A. Monster op voorraad is 1-2 dagen
B. Maak monsters op maat, slechts 7-15 dagen
MOQ
A. Als we voorraad hebben, kleinere MOQ.
B. Indien niet op voorraad, is de MOQ 5000-30000 stuks.
Oppervlaktebehandeling
Decal, Embossing, Zeefdruk, Spuitlakken, Frosten, Goudstempelen, Verzilveren, enz.
Materiaal
Kristalwit, Zwart, Super Flint, Extra Flint, enz. Breed assortiment voor uw selectie.
Verpakking
Karton, pallet, eisen van de klant.
Kleur
A.Transparant/gekleurd
B. Klantkleur en drukontwerpen
Levering
A. Op voorraad: binnen 7 dagen na ontvangst van betaling.
B. Niet op voorraad: 20-25 dagen na ontvangst van de betaling.
Extra diensten
1. ACL-printen, zijdeprinten en frostprinten.
2. Accessoires voor capsules, zoals plastic, aluminium en metalen sluitingen en houten inzetstoppers, zijn ook verkrijgbaar bij YB.
```

### T05
Link: https://www.alibaba.com/product-detail/new-product-ideas-2024-hot-selling_1601044532507.html

```
Titel: Nieuw Product Ideeën 2024 Hot Selling Product Verjaardag Innovatieve Vintage Familie Bruiloft Meisjes Groeiende Print Fotogeschenken Voor vrouwen

Belangrijkste kenmerken
plaats van herkomst

Guangdong, China

Toepassing

Terug Naar School, Chinese Nieuwe Jaar, Kerst, Vaderdag, Afstuderen, Halloween, Moederdag, Nieuwe Jaar, Thanksgiving, Valentijnsdag

Bedrukking

ZIJDEN SCHERM AFDRUKKEN, UV-printen, Digitaal printen, Laser graveren

Product Type

Promotionele Kantoor Producten, Promotionele Huishoudelijke Producten, Promotionele Elektronische Producten, Promotionele Novelty Gifts

modelnummer

18-0218

Stijl

Eenvoudige zakelijke stijl

Belangrijkste kenmerken
Bedrukking
ZIJDEN SCHERM AFDRUKKEN, UV-printen, Digitaal printen, Laser graveren
Toepassing
Terug Naar School, Chinese Nieuwe Jaar, Kerst, Vaderdag, Afstuderen, Halloween, Moederdag, Nieuwe Jaar, Thanksgiving, Valentijnsdag
Product Type
Promotionele Kantoor Producten, Promotionele Huishoudelijke Producten, Promotionele Elektronische Producten, Promotionele Novelty Gifts
Meer weergeven
plaats van herkomst
Guangdong, China
modelnummer
18-0218
Stijl
Eenvoudige zakelijke stijl
Verpakking en levering
Selling Eenheden
Enkel item
enkele pakket maat
33X30X10 cm
enkele brutogewicht
2.0 kg
Doorlooptijd
Maatwerkopties
Aangepast logo(+ vanaf /Min. bestelling: 100 sets)
Aangepaste verpakking(+ vanaf /Min. bestelling: 500 sets)
Afbeeldingen bewerken(+ vanaf /Min. bestelling: 1.000 sets)

Beschrijving: geen
```

### T06
Link: https://www.alibaba.com/product-detail/New-Unique-Desktop-Portable-Hand-Fan_1601270556301.html

De rest van de beschrijving staat in foto's en een video.

```
Titel: Draagbare mini handventilator met type-C oplaadpoort, voor thuis, auto en buitengebruik, elektrische voeding, plastic, huishoudelijk

Beschrijving:
Waarschuwing/Disclaimer
Dit product heeft de relevante productkwalificatie (en)/licentie (en) van bepaalde toepasselijke landen verworven.
Disclaimer: Alibaba.com geeft geen verklaring of bevestiging dat dit product volledig voldoet aan alle toepasselijke wet- en regelgeving; of dat enige kwalificatie/licentie daarvan echt, nauwkeurig en effectief is; of dat de verworven relevante kwalificatie(s)/licentie(s) voldoende zijn. Kopers wordt geadviseerd om voorafgaand aan de aankoop de relevante informatie in te winnen bij de verkoper om na te gaan of dit product voldoet aan de toepasselijke wet- en regelgeving van hun eigen land.

Specificaties:
Type: Handventilator
Voedingsbron: USB, Elektrisch
Werktijd: 1-2 uur
Batterijcapaciteit (mAh): 800
Windsnelheid: vijf
Materiaal: Kunststof
Besturingsmethode: Knop
installatie: Handheld
Spanning (V): 5
Vermogen (W): 5
Prive-schimmel: JA
Garantie: Geen
Verpakkingssoorten: kleurendoos
Toepassing: Hotel, Auto, Buiten, Garage, Huishouden
Batterijen Inbegrepen: JA
App-gestuurd: NEE
Land van herkomst: Guangdong, China
Merknaam: XIQI
Afmetingen: 16,2*3,6*13,2CM
Modelnummer: 12
Productnaam: Draagbare desktopventilator
Oplaadmodus: Type-C
Batterijtype: 18650 lithiumbatterij
Oplaadtijd: 2 uur
Gebruikstijd: 2-3 uur
Productgewicht: 174 gram
enkele pakket maat: 21.4X8.8X18.4 cm
enkele brutogewicht: 0.4 kg

Certificaten:
Declaration of Conformity - CE-gecertificeerd
CE - Voldoet aan de EU-normen
FCC - Elektromagnetische compatibiliteit
RoHS - Conform RoHS
94/62/EC - EU-conforme verpakking
EMC - Elektromagnetische compatibiliteit
REACH - REACH-gecertificeerd
```

### T07
Link: https://www.alibaba.com/product-detail/Daynee-Collagen-Gummies-Vitamin-Herbal-Label_1600900188417.html

```
Titel: Daynee Collageen Gummies Vitamine Kruiden Labelontwerp Gezondheidssupplementen Snoepjes Gummies Shanghai Flesverpakking cartoon roze

Beschrijving:
Waarschuwing/Disclaimer
Dit product heeft de relevante productkwalificatie (en)/licentie (en) van bepaalde toepasselijke landen verworven.
Beauty Collagen Gummies voor dagelijkse verzorging. Dit collageen gummies-supplement is ontworpen voor dagelijkse schoonheidsverzorging, met de nadruk op huid-, haar- en nagelondersteuning. Het is geschikt voor merken van schoonheidssupplementen, wellnesswinkels, online verkopers en private label gummy-productlijnen.
Schoonheid van Binnen Positionering: Dit product kan gepositioneerd worden als een handige 'schoonheid van binnen' gummy voor consumenten die de voorkeur geven aan een eenvoudige, dagelijkse routine in plaats van tabletten, capsules of poeder.
Huid-, Haar- en Nagelondersteuning. Speciaal ontwikkeld voor mooie nagels en krachtig haar, een gladde huid, gezond gewrichts- en botweefsel, en dagelijkse voeding voor een stralende schoonheid.
Gummies met natuurlijke aardbeiensmaak. De aardbeiensmaak maakt het product leuker dan traditionele tabletten of capsules.
60 veganistische gummies per fles. Elke fles bevat 60 veganistische gummies, geschikt voor detailhandel, monstertesten, cadeausets, schoonheidspakketten en planning van nabestellingen.
2 Gummies Dagelijkse Routine. Aanbevolen portie is 2 gummies per dag.
Ondersteuning voor private label-verpakkingen. Wij ondersteunen private label-aanpassingen, waaronder merklogo, flessenlabel, flesgrootte, dopkleur, smaakrichting, gummykleur, buitendoos.
OEM ODM Bulk Groothandel Levering. Geschikt voor beautymerken, supplementdistributeurs, Amazon-verkopers, TikTok-verkopers, online winkels en B2B-kopers.

Specificaties:
type: Gummy Candy
smaak: Fruitig
Verpakking: Fles
functie: Normaal
vorm: Cartoon
kleur: Roze
type product: Snoepgoed
opslag type: Kamertemperatuur
Specificatie: 3g*60gummies/fles
houdbaarheid: 24 maanden
Fabrikant: Dagnee
Ingrediënten: Natuurlijke aardbeiensmaak
Content: Collageenpeptiden, vitamine C, vitamine E, D-biotine
Gebruiksaanwijzing: Klaar om te eten
plaats van herkomst: Shanghai, China
naam van het merk: Daynee
modelnummer: R22
Productnaam: Collageen gummies
OEM: accepteren
Andere naam: Huidblekende L-Glutathion Gummies
Trefwoord: Collageen gomachtig
enkele pakket maat: 15X5X5 cm
enkele brutogewicht: 0.21 kg
```

### T08
Link: https://www.alibaba.com/product-detail/Plush-Doll-Monster-Energy-23CM-27CM_1601931802984.html

```
Titel: Pluche Monster Energy pop 23CM-27CM Super Witte Energy Drink Vorm Schattig Kussen Speelgoed Gewassen PP Katoen Gevuld OEM groothandel

Beschrijving:
Verantwoordelijke EU-persoon
Superzacht pluche: biedt ongeëvenaard comfort en gezelligheid.
Monsters Energy Shape: Authentiek ontwerp geeft de iconische energiedranklook weer.
23-27 cm hoogte: perfecte maat voor gemakkelijk dragen en tentoonstellen.
Katoenen vulling: zorgt voor zachtheid en duurzaamheid.
Kleurrijk en schattig: ideaal als cadeau of decoratie.

Specificaties:
Leeftijdscategorie: 14 Jaar & up
Personages: Monster-energie
type: drinkend speelgoed
Hoogte: 23CM-27CM
Hoofdmateriaal: Super zacht pluche
materiaal: korte pluche
Acg Naam: Monster-energie
Vulling: PP-katoen
Geslacht: Unisex
functie: COMFORTER
Technieken: Washed
gelegenheid: Halloween
voering materiaal: Spandex/elastaan
modelnummer: XL-drinking
plaats van herkomst: Anhui, China
Waslabel: Katoen
naam van het merk: XINLI
Productnaam: Pluche pop
Gebruik: Mooi cadeau
Grootte: 23CM-27CM
Kleur: Kleurrijk
Trefwoord: Zacht gevuld plsh-speelgoed
Stijl: Leuk en Speels
Verpakking: OPP-zak
enkele pakket maat: 35X25X2 cm
enkele brutogewicht: 0.150 kg
```

### T09
Link: https://french.alibaba.com/product-detail/LED-Eye-Protection-Desk-Lamp-with-1601696226086.html

```
Titel: Lampe de bureau LED avec protection oculaire, grande horloge, calendrier, veilleuse, norme américaine, avec ports de charge pour la maison, l...

Description du produit
Nom de l'article : Lampe de bureau LED avec protection des yeux, grande horloge et calendrier, veilleuse
Puissance: AC 110v-220v
Prise: US/EU/UK
USB TYPE C: 5V2A
Température de couleur: 3000/4500/6000
Matériau: PP et PC
```

### T10
Link: https://www.alibaba.com/product-detail/Custom-Metal-Keychain-Blank-Heat-Transfer_1601624454473.html

Korte input: alleen de titel en zes regels uit de kenmerken. Een echte korte pagina vond ik niet, want Alibaba-pagina's zijn bijna altijd lang. Ik heb de rest van de pagina zelf weggelaten. Dit is wat een verkoper ziet als hij snel kijkt zonder te scrollen.

```
Titel: Gepersonaliseerde metalen sleutelhanger blank voor hittetransferdruk logo sleutelhanger roestvrijstalen sleutelhanger blank

Producttype: Carabiner Keychain
Metaaltype: Roestvrij staal of zinklegering
Bedrukking: UV-printen
vorm: Rond
materiaal: Metaal
plaats van herkomst: Guangdong, China
```

## Antwoorden van de tool (v1, claude.ai)

### T01 run 1
```
OORDEEL: GO
RISICO'S: geen
UITLEG: Het is een katoenen draagtas zonder merknaam of merklogo, zonder elektronica of batterij, klein en licht verpakt ("0.3 kg"), en niet verboden of beperkt op bol.com.
```

### T01 run 2
```
OORDEEL: GO
RISICO'S: geen
UITLEG: Het is een katoenen draagtas zonder merknaam (alleen "OEM"), zonder elektronica, batterij of andere CE-plichtige kenmerken, compact verpakt (15X15X5 cm, 0.3 kg) en niet verboden op bol.com.
```

### T02 run 1
```
OORDEEL: GO
RISICO'S: geen
UITLEG: Het is een siliconen beschermhoesje dat alleen zegt waarop het past ("Voor Apple Airpods/Airpods pro"), zonder merklogo, zonder elektronica of batterij, klein en licht (0.030 kg) en niet verboden.
```

### T02 run 2
```
OORDEEL: GO
RISICO'S: geen
UITLEG: Het is een siliconen hoesje dat alleen vermeldt waarop het past ("Voor Apple Airpods/Airpods pro"), zonder merklogo of woorden als "replica"; het is geen elektrisch apparaat, geen batterij, niet breekbaar (0.030 kg) en niet verboden op bol.com.
```

### T03 run 1
```
OORDEEL: GO
RISICO'S: geen
UITLEG: Het is een elektrische oplader waarvoor "CE-gecertificeerd" en "Declaration of Conformity" op de pagina staan, het is niet breekbaar, zwaar of vloeibaar, en er is geen merknaam van derden of een verboden productcategorie te vinden.
```

### T03 run 2
```
OORDEEL: GO
RISICO'S: geen
UITLEG: Het is een elektrische oplader waarvan de pagina CE-certificering vermeldt ("CE-gecertificeerd"), er staat geen merkkopie of merklogo op het product (alleen de eigen merknaam "SChitec/OEM"), en het is een compact, niet-breekbaar product dat niet onder verboden categorieën valt.
```

### T04 run 1
```
OORDEEL: NO-GO
RISICO'S:
- C: "Parfumflesje, rechthoekige glazen parfumfles 50 ml, lege parfumfles 100 ml met doos." — Het product is een glazen fles, en glas is breekbaar en dus moeilijk veilig te verzenden.
UITLEG: Het is een lege glazen parfumfles, en breekbaar glas is al genoeg voor een NO-GO.
```

### T04 run 2
```
OORDEEL: NO-GO
RISICO'S:

C: "Parfumflesje, rechthoekige glazen parfumfles 50 ml, lege parfumfles 100 ml met doos." — Glas is breekbaar en dus moeilijk veilig te verzenden.
UITLEG: Het product is een lege glazen parfumfles, en breekbaar glas is een verzendrisico.
```

### T05 run 1
```
OORDEEL: ONZEKER
RISICO'S: geen
UITLEG: De pagina zegt niet wat het product precies is (alleen vage termen als "Fotogeschenken" en "Promotionele Novelty Gifts", zonder beschrijving of materiaal), dus de risico's zijn niet te beoordelen.
```

### T05 run 2
```
OORDEEL: ONZEKER
RISICO'S: geen
UITLEG: De pagina toont niet wat het product is of waaruit het bestaat: alleen algemene termen als "Fotogeschenken" en vier uiteenlopende producttypes (kantoor, huishoudelijk, elektronisch, novelty), zonder beschrijving, materiaal of CE-informatie.
```
