# Buurtest

Lees eerst alleen de prompt. Lees daarna elk bedrijf en kies: **ja**, **nee** of **onzeker**. En: welk e-mailadres staat er, of geen?

## De prompt
```text
Je beoordeelt één bedrijf als mogelijke klant voor DBA Hardwoods, een houthandel die nu vooral rubberwood verkoopt aan bedrijven die in massief hout werken. Geef precies één JSON-object terug, en verder niets.

Stap 1: kies "doelgroep":
- "ja": het bedrijf maakt zelf iets in massief hout waar rubberwood in past: trappen, meubels, keukens, kasten, werkbladen, tafels.
- "nee": het bedrijf maakt zelf niets in massief hout, bijvoorbeeld een plaatser van PVC- of aluminium ramen, een meubelwinkel of een handelaar.
- Verkoopt of plaatst het bedrijf alleen producten die ergens anders gemaakt worden? Dan "nee", want het koopt zelf geen hout.
- "onzeker": de tekst geeft te weinig informatie om te kiezen.

Stap 2: haal de contactgegevens uit de tekst:
bedrijfsnaam, email, telefoon, adres, gemeente, btw, website.

Regels:
- Neem alleen over wat letterlijk in de tekst staat. Verzin niets.
- Staat een veld niet in de tekst, vul dan "onbekend" in.
- Raad nooit een e-mailadres, ook niet info@ of contact@, want een geraden adres bestaat misschien niet.
- Staat er geen e-mailadres in de tekst, zet dan "lead" op "geen e-mail".
- "lead" is "ja" alleen als doelgroep "ja" is en er een e-mailadres in de tekst staat. Anders "nee" of "geen e-mail".
- Geef in "reden" één korte zin: waarom deze doelgroep.

Formaat:
{"doelgroep": "ja|nee|onzeker", "lead": "ja|nee|geen e-mail", "bedrijfsnaam": "...", "email": "...", "telefoon": "...", "adres": "...", "gemeente": "...", "btw": "...", "website": "...", "reden": "..."}

```

## Bedrijf A

Antwoord: doelgroep ____  ·  e-mail ____________

```text
 DL Interieur | Luxe binnenschrijnwerk en maatwerk regio Gent 
 Onze werkwijze
 Expertise
 Inspiratie
 Contact
 Vakmanschap | Kwaliteit | Duurzaamheid
 Welkom bij DL Interieur . 
 DL Interieur staat voor meer dan 20 jaar vakmanschap. De zaakvoerder Andy De Landtsheer realiseert uw interieur op maat in hoogwaardige en duurzame materialen met oog voor detail en comfort. We streven steeds naar een goede klantenservice met stipte opvolging en communicatie waarbij de klant centraal staat.
 Bekijk realisaties
 Neem contact op
 Interieur op maat
 Onze Werkwijze Persoonlijk advies, nauwkeurige plaatsing . 
 Bent u benieuwd hoe we te werk gaan? Ons proces bestaat uit drie duidelijke stappen:
 01 
 Een gesprek
 Elk project start met luisteren naar elkaar. We nemen de tijd om uw wensen, noden en ideeën goed te begrijpen — zonder haast. Zo leggen we een stevige basis voor de samenwerking die volgt.
 02 
 Ontwerp en offerte
 We vertalen uw wensen naar een concreet ontwerp dat past bij uw woning, smaak en budget. U ontvangt een uitgebreide offerte met transparante prijzen — geen verborgen kosten, geen verrassingen.
 03 
 Planning en uitvoering
 In gezamenlijk overleg bepalen we wanneer alles praktisch ingepland kan worden. We starten met de voorbereidende werken in ons eigen atelier, waarna we het maatwerk installeren zoals afgesproken. Ook tijdens de uitvoering blijven we open voor suggesties en ideeën.
 Onze belofte: we luisteren, we maken heldere afspraken en volgen op tot het definitieve eindresultaat.
 01 Eigen atelier
 Alle maatwerk wordt gecreëerd in ons eigen atelier. Bezoek ons
 02 Flexibel
 We zijn zeer flexibel en altijd snel te bereiken voor overleg. Bel of mail ons gerust, we reageren snel en denken meteen met je mee! 
 03 Goede na-service
 Ook na de oplevering staan we voor je klaar. Heb je nog vragen of loop je ergens tegenaan? Eén mailtje en we lossen het samen op! 
 Ons Aanbod Van idee tot realisatie, groot en klein
 Grootschalige renovatie of een kleine aanpassing in uw interieur? Dat doen we volledig op jouw manier. Samen met een vast team van interieurarchitecten en vakmensen, of gewoon rechtstreeks met jou.
 Keukens op Maat
 De keuken is het warme centrum van uw woning. Wij ontwerpen een keuken op maat in uw stijl, met focus op comfort en gebruiksgemak.
 Klassiek, landelijk, modern of tijdloos
 Keuze uit MDF lak, laminaat, fineer of massief hout
 Wandopstelling, kookeiland of keuken met eettafel
 Van ontwerp tot plaatsing met vaste partners
 Bespreek uw project -&gt;
 Dressings
 Een inloopkast of dressing op maat: creëer de ultieme, overzichtelijke ruimte voor al uw kleding, schoenen en accessoires.
 Van eenvoudige inloopkasten tot luxe dressingruimtes
 Op maat ingericht met kledingroedes, ladesystemen en schoenrekken
 Geïntegreerde ledverlichting en handige accessoires mogelijk
 Inbouwkasten
 Maatwerk inbouwkasten voor elke ruimte: van vloer tot plafond benutten we elke vierkante meter optimaal en stijlvol.
 Ingemaakte kasten voor slaapkamers, inkomhallen, bergingen, woonkamer, ...
 Perfecte integratie onder schuine wanden, trappen of in nissen
 Afwerking met greeploze fronten, schuifdeuren of draaideuren
 Flexibele indeling met legplanken en functionele opbergsystemen
 Badkamers
 Een badkamer op maat die rust en functionaliteit combineert, van meubel tot totale renovatie.
 Vrijheid in ontwerp en materiaalkeuze
 Hoogwaardige, vochtbestendige materialen voor een duurzaam meubel
 Van ontwerp tot realisatie
 Complete renovatie is mogelijk
 Haardwanden
 Het interieur rond de haard is minstens even belangrijk als de haard zelf. Wij zorgen voor een totaaloplossing op maat.
 Optie tot ontwerp en uitvoering in samenwerking met interieurarchitect
 Perfecte afstemming met uw haardleverancier voor een veilige installatie
 Gebruik van hittebestendige en brandveilige materialen
 Verfijnde afwerking met hoogwaardige lakken, fineer of natuursteenlook
 Burelen & Thuiskantoren
 Een ergonomische en inspirerende werkplek op maat, naadloos geïntegreerd in uw interieur of kantoor.
 Maatwerk bureaus, archiefkasten en slimme opbergruimte
 Naadloze integratie van alle bekabeling, stopcontacten en ledverlichting
 Functionele en creatieve ontwerpen
 Hoogwaardige afwerking in fineer, laminaat of lakwerk naar keuze
 01 Vakmanschap
 Elk project wordt in eigen atelier voorbereid en met zorg afgewerkt bij u thuis.
 02 Kwaliteit
```

## Bedrijf B

Antwoord: doelgroep ____  ·  e-mail ____________

```text
 BAUTIER
 Browse
 Close menu 
 Cart ( 0 )
 Close
 Bautier
 Main Menu
 -->
 Furniture
 Accessoires
 Books
 Café
 Apartments
 About
 Journal
 Cart
 ( 0 )
 New in
 Shop New Arrivals
 Shop New Arrivals 
 Bautier Journal
 Brussels by Locals: Christoph Nagel
 Aube runs on good bread, a lot of people, and a certain tolerance for chaos. For Christoph Nagel, that’s part of what makes the place work. In this Journal post, the co-founder of the Forest bakery talks about building a business without being a baker, learning the parts of entrepreneurship that don’t come naturally, and why bringing the right people together can be as important as knowing how to do the job yourself. There’s also the question of what comes next — and whether one good place might be enough.
 View full feature
 Shop Bautier Furniture
 Bautier furniture is produced in the northwest corner of Germany by talented craftsmen, trained in making solid and refined products. Bautier not only aspires to create durable objects, durability is fundamental and included in every reflection made regarding choice of materials, manufacturing, suppliers and collaborators.
 Shop now 
 Shop Bautier Accessoires
 A range of homeware goods by Bautier and a selection amongst distinct brands and craftsmen. Common for them all is the wish to create alluring everyday objects. Bautier pays careful attention to how and where the pieces are made, ensuring a warranty of high-quality manufacturing.
 Shop now
 Shop Bautier Books
 A curated selection of Bautier's favourite books, covering the fields of architecture, design, cooking and photography.
 About Bautier
 Belgian brand Bautier offers essential products for the home. Founded in 2013 by designer Marina Bautier, it aims to create functional, durable, and well-made pieces, designed to be used and loved for a lifetime.
 Serene, qualitative and simple is the best way to describe the brand. Bautier is not about making standout objects. Its designs are pure and modest, reduced to its bare essentials. Through a collection of well-crafted items, the company has established an enduring and seasonless style with the flexibility to refine over time.
 At Bautier, the starting point for creating new products is quality, relying on efficient assembly techniques and intelligent use of honest materials. Since sustainability is also a part of the brand's philosophy, it has been naturally incorporated into all processes: from carefully choosing local suppliers, manufacturers, and materials, to informing customers about the care of products to prolong their lifespan.
 After ten years of working in the furniture industry, Marina Bautier's ambition to set up her own brand alongside her design practice grew stronger. What started with a unique assortment of solid wooden furniture has now developed into a full home collection, including small must-have accessories and classic homeware. Personally sourced and curated by Bautier, the range is complemented with qualitative objects from other local brands.
 The Bautier studio, workshop, and store are based in Brussels, Belgium. All items are sold exclusively at the Bautier shop and website.
 Instagram
 How to order
 Bautier products are exclusively available from this website and our store in Brussels.
 Brussels store
 Our store at 314 Chaussée de Forest, 1190 Brussels is open Wednesday to Saturday from 10am to 6pm. Most items are on display and directly available. For large furniture pieces, a delivery might have to be organised.
 Order Furniture online
 We deliver most items worldwide. Please fill in the quote request available on the product pages on this website. We will then get back to you with a shipping quote and estimated delivery date. Your order will be confirmed once we receive your payment, which can be done by bank transfer or credit card.
 Order Accessoires online
 Accessoires can be ordered directly from this website by adding the items to the cart and proceed to checkout.
 Leadtimes
 Most items are held on stock (unless indicated otherwise on product page) and can be delivered without delay. Upholstery is made to order on a 4 weeks lead time.
 Trade enquiries
 Special prices apply for professionals, please contact us
 for a quote.
 Press
 Please contact us on press@bautier.com
 to enquire for press material. Or give us a call on +32 2 520 03 19.
 Bautier Store.
 +32 2 520 03 19
 314 chaussée de Forest, 1190 Brussels
 info@bautier.com, www.bautier.com
 Opening hours
 Wednesday-Saturday: 10-18.00
 Sign up for our newsletter
 Subscribe 
 SHOP
 Gift cards
 ABOUT
 About us
 CUSTOMER CARE
 Shipping & Returns
 Privacy Policy
```

## Bedrijf C

Antwoord: doelgroep ____  ·  e-mail ____________

```text
 -->
 Aannemer voor renovatie en verbouwingen Oost-Vlaanderen 
 top of page 
 VOLKAN.ER@ICLOUD.COM 
 0472 240 543 
 INFO@ER-BOUW.BE 
 HOME 
 ALGEMENE VERBOUWINGEN 
 TOTAALRENOVATIE 
 REALISATIES 
 CONTACT 
 ALGEMENE VERBOUWINGEN EN RENOVATIES 
 Neem contact op 
 SPECIALIST IN VERBOUWINGEN EN RENOVATIES
 Vroeg of laat dient iedere woon- of werkruimte aan een verbouwing of renovatie onderworpen te worden. Vaak zijn renovatiewerken noodzakelijk om vochtophoping, lekkages, geluidshinder en andere ongewenste problemen te vermijden of te verhelpen. Naast het wegnemen van deze ongemakken geven verbouwingswerken ook een frisse look aan uw pand en leiden ze tot een stijging van de marktwaarde. 
 Verbouwingen van specifieke ruimte
 Wenst u een bepaalde ruimte van uw woning of bedrijfspand te vernieuwen? Bel ons voor de professionele verbouwing van onder andere de volgende ruimtes:
 Badkamerrenovatie: tegelen van de vloer en/of muren, plaatsen van badkamermeubels, installeren van allerlei soorten baden en douches
 Kantoorruimtes: plaatsen en activeren van verlichting, vloer- en tegelwerken
 Keukenrenovatie: uitbreken en aanleggen van vloeren en muren, plaatsen van meubilair en installatie van elektrische installaties
 Zolderrenovatie
 Specifieke renovatieklussen
 Bent u niet van plan om een volledige ruimte te laten verbouwen, maar zijn er wel enkele elementen die u dient te vernieuwen? Contacteer onze onderneming voor de volgende renovatiewerkzaamheden:
 Chapewerken
 Dakwerken: dakrenovatie, isolatie, dakgoten plaatsen, daken ontmossen
 Elektriciteitswerken: plaatsen en/of herstellen van zekeringskasten, installeren van verlichting, plaatsen van stopcontacten en (hoofd)schakelaars
 Gyprocwerken: plaatsen van Gyprocwanden als voorzetwand of tussenwand in diverse groottes, kleuren en afwerkingen
 Metselwerken: brievenbussen, tuinmuurtjes, bijgebouwen
 Pleisterwerken
 Sanitaire werkzaamheden: inloopdouche installeren, afvoerbuizen plaatsen, toiletten installeren, badkuipen plaatsen
 Verf- en schilderwerken: vloeren, muren, ramen en deuren
 Plaatsen van vloer- en wandtegels 
 Leggen van parket 
 Leggen van laminaat 
 Uitstekende resultaten 
 Tijdbesparend 
 Waarom uw renovatiewerken toevertrouwen aan ER-Bouw?
 Snelle en stipte service 
 BEKIJK ONZE REALISATIES 
 ER-Bouw
 press to zoom 
 1/1
 KIJKT U UIT NAAR EEN ALLROUND AANNEMER VOOR UW ALGEMENE VERBOUWINGEN EN RENOVATIES IN OOST-VLAANDEREN? 
 Laat u verrassen door de sublieme service en resultaten van ER-Bouw!
 NEEM CONTACT OP 
 Adres 
 Zeeschipstraat 82
 9000 Gent
 Telefoon 
 0472 240 543
 E-mail 
 info@er-bouw.be 
 TVA 
 BE 0668 731 658
 volkan.er@icloud.com
 © 2026
 FCR Media Belgium
 - Sitemap
 - Privacy Policy
 bottom of page 
```
