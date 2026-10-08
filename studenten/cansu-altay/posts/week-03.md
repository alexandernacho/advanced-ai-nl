# Week 3 — Waarom één goed AI-antwoord niet genoeg is

## Wat ontbrak er in mijn context?

Mijn Build zet korte trainingsnotities om naar een tabel met de oefening, het gewicht, het aantal sets en de herhalingen. Ik wil hiermee mijn vorige trainingsgewicht kunnen terugvinden.

Tijdens de controle van de zes bouwstenen ontdekte ik dat voorbeelden ontbraken in mijn prompt. Er stonden wel instructies, maar geen voorbeelden die toonden hoe ik het antwoord wilde zien. Ook ontbrak bij mijn regels een uitleg waarom ze belangrijk zijn.

Bij de notitie over face pulls schreef de AI alleen ‘onbekend’ bij de herhalingen. De informatie dat de laatste set tot failure ging, verdween. Ik wil die informatie behouden, omdat ‘onbekend’ en ‘tot failure’ verschillende betekenissen hebben. ‘Onbekend’ betekent dat het aantal herhalingen niet is vastgelegd. ‘Tot failure’ betekent dat ik doorging tot ik geen herhaling meer kon uitvoeren.

De buurtest heb ik nog niet uitgevoerd. Ik was niet meer in de les toen ik aan die stap kwam.

## Mijn eerste cijfer

Met prompt v3 testte ik tien verschillende trainingsnotities, elk twee keer. Het resultaat was 17 op 20 juist: 85% (n = 10, 2 runs). Eén antwoord had een F4-fout: de inhoud klopte, maar de uitvoervorm volgde onze afspraak niet. Twee antwoorden hadden een F3-fout: informatie over failure ontbrak.

Bij de pullovernotitie zag ik ook F6: dezelfde input gaf twee verschillende antwoorden, waarvan één niet aan de afspraak voldeed. Daarom vertrouw ik niet meteen op één goed antwoord. AI kan fouten maken en ik moet de antwoorden blijven controleren.

## Eén wijziging

In v4 voegde ik drie voorbeelden en een regel met een ‘want’ toe. Omdat ik daarmee meerdere dingen tegelijk veranderde, maakte ik daarna een aparte testversie op basis van v3 met alleen de drie voorbeelden. Voorbeelden geven de AI een duidelijke richting en tonen hoe ik de tabel wil zien.

Met die aparte versie testte ik de twee eerder problematische notities opnieuw, elk twee keer. Op dezelfde selectie ging het resultaat van 1 op 4 juist met v3 naar 4 op 4 met alleen de voorbeelden erbij. De verwachte antwoorden bleven gelijk. Zo onderzocht ik één wijziging aan mijn context. De eerdere versies en fouten bleven bewaard.

Dit is nog geen overtuigend bewijs van betrouwbaarheid. De hertest moet uitgebreider zijn: meer verschillende notities en meer herhalingen per input. Vier goede antwoorden betekenen niet dat de AI altijd goed werkt.
