# Week 3 — Zelf kiezen welke periode ik vergelijk

## Wat ontbrak er in mijn context?

Ik bouw een tool om financiële rapporten van twee bedrijven te vergelijken. Ik ben een beginnende belegger en doe aan stockpicking. Een duidelijke tabel met de belangrijkste informatie en de onderbouwing eronder maakt die vergelijking voor mij makkelijker.

Bij Netflix en Uber merkte ik dat de beschikbare FCF-cijfers over verschillende perioden gingen. Netflix had kwartaalcijfers, terwijl de gevonden Uber-cijfers het halfjaar betroffen. In mijn oudere prompt schakelde de tool dan automatisch voor beide bedrijven over naar halfjaarcijfers. Dat wilde ik veranderen. Hij moet liefst kwartaalperioden gebruiken en anders de mogelijkheden tonen en mij vragen welke periode ik wil.

Ik wil zelf kiezen, omdat kwartalen soms wat afwijken en ik als mens kan beslissen of de vergelijking bruikbaar is. Bij PepsiCo en Coca-Cola, en bij Rheinmetall en Lockheed Martin, accepteerde ik verschillende kwartaalgrenzen voor de omzetgroei. Het verschil moest wel duidelijk vermeld blijven.

De buurtest heb ik nog niet uitgevoerd. Ik werk thuis en kan niet naar de les komen, omdat die samenvalt met mijn bachelorproef. Mijn eigen controles vervangen die buurtest niet.

## Mijn eerste cijfer

Voor de vijf omzetgroei-inputs T06–T10 beoordeelde ik tien runs als geslaagd: 10 op 10, dus 100% (n = 5 inputs, 2 runs per input). Dat cijfer geldt alleen voor de gecontroleerde omzetgroei, niet voor alle onderdelen van mijn tool.

Er waren ook fouten bij eerdere tests. Bij NVIDIA en AMD miste Run 1 het gerapporteerde AMD-percentage: F3, gemist. Run 2 vond het wel: F6, wisselend. Bij Amazon en Alphabet wisselde het onzekerheidslabel bij dezelfde schuldinformatie, ook F6. Die twee runs vond ik bruikbaar, maar niet volledig geslaagd.

Ik was verrast hoe de twee tests zo goed als altijd overeenkwamen. De tabellen werden ook steeds duidelijker na aanpassingen aan de instructies.

## Eén wijziging

Mijn gekozen wijziging is de periodevraag: beschikbare perioden tonen en wachten op mijn keuze. In één gerichte Netflix/Uber-test deed de tool dat. Ik beoordeelde die keuzevraagtest als geslaagd: 1 op 1 (n = 1 input, 1 run).

Dat bewijst nog niet dat het altijd werkt. Ook andere promptonderdelen zijn gewijzigd. Bovendien geef ik bij twee runs dezelfde informatie. Het is dus niet onlogisch dat dezelfde uitvoer terugkomt, en de tool kan twee keer dezelfde fout maken.
