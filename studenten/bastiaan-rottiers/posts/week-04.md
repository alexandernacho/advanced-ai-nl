# Week 4 — Van veel documenten en opdrachten tot overzichtelijk werken

## Mijn tool in cijfers

Mijn tool maakt van een Canvas-opdracht en de bijhorende documenten een voorbereidingskaart. Die kaart zet samen wat we moeten opleveren, de concrete stappen, deadline, inleverwijze, beoordelingscriteria en een agenda-voorstel. Bij documenten zoals ons businessplan of Sustainable Business Model Canvas kan de tool ook tonen wat al ingevuld is en wat de volgende stap is.

Ik testte tien inputs: gewone Canvas-opdrachten, onvolledige informatie en twee documenten waarin WATTZAK al informatie had ingevuld. Over alle beoordeelde runs was het resultaat **10 op 14 juist (n = 10 inputs, 14 runs)**. De eerste fouten waren nuttig. Drie keer gaf de tool een F1-fout: een overtuigend maar verkeerd antwoord, bijvoorbeeld een verkeerde status. Twee keer was er een F2-fout: informatie die niet in de bron stond. Dat is het gevaarlijkste type fout, omdat het antwoord dan geloofwaardig lijkt.

Na elke fout heb ik de prompt gerichter gemaakt. Ik voegde regels toe voor concrete deadlines, ontbrekende inleverwijzen, aantallen zoals “ieder groepslid” en de status van een opdracht. Bij de laatste test van het Sustainable Business Model Canvas gaf de tool correct per bouwsteen aan wat al ingevuld was, wat nog ontbrak en wat de volgende stap is. De tool is dus niet foutloos, maar de testset toont wel dat ik fouten kan vinden, een oorzaak kan benoemen en daarna gericht kan verbeteren.

## Wat kost één run?

Voor de kostenmeting gebruikte ik GPT-6.1 Sol in een nieuwe Codex-sessie met T01. Na de run stond `/status` op 25.800 tokens. De tool toont geen aparte input- en outputtokens, daarom is mijn verdeling een aanname: 98% input en 2% output. Met de prijzen uit het lesmateriaal ($2 per miljoen inputtokens en $10 per miljoen outputtokens) kost deze run ongeveer **$0,056**.

De ECB noteerde op 20 oktober 2026 $1,1215 voor €1. Dat betekent dat $1 ongeveer €0,892 waard was. [ECB-wisselkoers van 20 oktober 2026](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.eu.html) De kost is dus afgerond **€0,05 per run**. Ik was verrast dat een taak die voor een mens veel zoeken en nadenken vraagt, via AI zo goedkoop kan zijn.

Voor WATTZAK schat ik acht runs per maand: minstens zes belangrijke documenten en één à twee opdrachten. Dat komt neer op ongeveer **€0,40 per maand**, **€4 bij tien keer dit volume** en ongeveer **€400 bij duizend keer dit volume**. Met GPT-6 Luna uit de prijstabel zou dezelfde run ongeveer twintig keer goedkoper zijn, maar dat model moet eerst nog op dezelfde testset bewijzen dat de kwaliteit voldoende blijft. Bij ons huidige volume is de kost bijna verwaarloosbaar; pas op grote schaal wordt ze een echte beslissing.

## Met de hand of met de tool?

Zonder de tool kost een belangrijk document of een opdracht lezen, begrijpen en in onze agenda zetten volgens mijn inschatting minstens dertig minuten. Voor ons businessplan moeten we informatie uit veel verschillende documenten samenbrengen en telkens opnieuw zoeken waar iets staat. Met de tool reken ik maximaal vier minuten: de run laten uitvoeren en daarna de uitvoer nakijken. Nakijken blijft nodig, omdat de testset toonde dat een AI soms iets verkeerd interpreteert of verzint.

De winst is dus 30 min min 4 min = **26 minuten per taak**. Bij acht taken per maand bespaart dat 208 minuten of ongeveer 3,47 uur per maand. Verdeeld over twintig werkdagen is dat ongeveer tien minuten per dag; per week zijn het twee taken en 52 minuten. Op jaarbasis gaat het om 96 taken of **41,6 uur**. Ik reken met €20 per uur als voorzichtige tijdwaarde voor één WATTZAK-teamlid. Dit is een aanname, geen werkelijk loon. De brutowaarde is dan 41,6 uur maal €20 = **€832 per jaar**. Na aftrek van ongeveer €4,80 toolkost blijft een netto waarde van ongeveer **€827 per jaar**.

Ik ga de tool zeker gebruiken voor mijn bachelorproef. Hij helpt mij niet alleen tijd winnen, maar geeft ook het team eenzelfde overzicht van wat we al hebben en wat er nog ontbreekt. Dat is bij een groepswerk minstens even waardevol als de minuten die we besparen.

## Mijn zwakste cijfer

Mijn zwakste cijfer is de geschatte dertig minuten handmatig werk. Ik heb dit niet met een chronometer gemeten; het is mijn inschatting op basis van het zoeken in Canvas, lesnotities en andere documenten. Als die tijd in werkelijkheid maar vijftien minuten is, blijft er per taak nog elf minuten winst over. Dat geeft 17,6 uur per jaar. Aan €20 per uur en na de toolkost blijft dan ongeveer **€347 netto per jaar** over. Zelfs in dat voorzichtige scenario blijft de tool dus nuttig, maar de echte waarde moet ik later nog toetsen tijdens het verdere werk aan WATTZAK.
