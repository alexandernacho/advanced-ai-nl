# Week 3

## Wat ontbrak er in mijn context?
In mijn prompt ontbraken voorbeelden (bouwsteen 4): ik had alleen een formaat met lege plekken. De uitweg "niet vermeld" stond maar bij twee van de acht velden. Daarnaast botsten twee regels, "reken niets uit" en "geef de lopende kosten per jaar", en mijn regel over "tekens" was niet duidelijk genoeg over notatie.

Door de botsende regels telde de tool de beheer- en transactiekosten niet op bij T02, T03 en T04 in week 2. Door de vage regel over tekens bleef de Engelse notatie staan in T04 (13,600 USD in plaats van 13.600 USD).

Ik voegde twee voorbeelden toe uit KID's die niet in mijn testset zitten, en een uitzondering op "reken niets uit": als de kosten in delen staan, tel ze op. De notatieregel kreeg een "want" erbij, zodat de tool begrijpt waarom. Claude zag daarna dat het voorbeeld in die notatieregel per ongeluk het antwoord van T04 bevatte, waardoor die test minder zegt. Dat voorbeeld is vervangen.

## Mijn eerste cijfer
Met mijn laatste prompt (v1.2) kwam ik op 79 op 80 juist (n = 10, 1 run). Claude draaide die runs voor mij, elk in een schoon gesprek, en ik schreef de juiste antwoorden vooraf zelf op.

Over de vier runs van week 3 kwamen drie klassen voor: F1 drie keer (T04, T05, T06), F4 twee keer (T07, T05) en F6 één keer, want v1.1 gaf bij dezelfde prompt in run 1 en run 2 een andere fout.

Wat me opvalt: elke run haalt 79 op 80, maar de ene fout valt telkens bij een ander KID en in een ander veld. Elke regel die ik toevoeg, lost dus vooral de vorige fout op en niet de onderliggende onzekerheid. Bij dezelfde prompt viel de fout bij een ander KID.

Dit is nog geen bewijs, omdat één run met tien KID's te klein is.

## Eén wijziging
In v1.1 voegde ik één regel toe: de tool moet bij het ongunstige scenario controleren of het rendement bij het juiste bedrag hoort, omdat hij bij T04 het rendement uit een andere rij had genomen. Bij T04 gaf de tool daarna het juiste rendement van 6,3 % in plaats van −33,5 %. De regel bracht wel een nieuwe fout mee: bij T07 en T05 schreef de tool extra tekst bij zijn antwoord, en daarom liet ik hem die controle in v1.2 "in stilte" doen. Toch is dit nog geen bewijs, want ik draaide T04 per versie maar één keer, en mijn eigen runs tonen dat dezelfde prompt de ene keer goed en de andere keer fout kan uitkomen.

Een taalmodel is hiervoor nodig, omdat elk KID een andere layout heeft en Excel met vaste plekken werkt. Zelf een KID lezen en acht velden opschrijven kost mij 7 tot 10 minuten. Met de tool plak ik het KID in een paar seconden en lees ik de acht uitkomsten in maximaal 1 minuut.
