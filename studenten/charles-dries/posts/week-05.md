# Week 5: mijn tool is goedkoper dan ik dacht

## Mijn foutmarge

Ik testte twee promptversies elk drie keer op dezelfde tien reacties met GPT-6 Luna. De verwachte labels stonden vooraf in mijn testset en ik heb ze niet aangepast. Versie 1 haalde drie keer 9/10, dus 90%–90%. Versie 2 haalde 8/10, 9/10 en 9/10, dus 80%–90%. Mijn oorspronkelijke claim was dat versie 2 beter zou zijn omdat die meerdere labels kan geven. Die claim trek ik in: beide bereiken overlappen op 90%. Versie 1 is voor mij de beste keuze, want mijn tool moet juist één label teruggeven en die versie was drie keer even stabiel.

## Model en effort

Voor de modeltest gokte ik dat GPT-6.1 Sol met high effort zou winnen. Dat gebeurde niet. GPT-6 Luna met high en medium effort en GPT-6.1 Sol met high effort haalden alle drie 9/10 op dezelfde tien inputs. Dat verschil valt dus binnen mijn foutmarge. Luna medium gebruikte gemiddeld 28,4 outputtokens per reactie; Luna high gebruikte 58,9 en Sol high 116,7. Ik kies daarom Luna medium. Met een geschatte 480 inputtokens kost die run ongeveer €0,000056. Bij 500 reacties per jaar is dat afgerond €0,03.

## Mijn value chain, met de foutmarge erin

Ik schat dat één reactie met de hand 35 seconden vraagt: 20 seconden lezen, 10 seconden een label kiezen en 5 seconden het resultaat noteren. Met de tool reken ik 3 seconden draaien en 10 seconden nakijken. Bij een score van 90% moet ik gemiddeld 10% herstellen: 10% van 35 seconden is 3,5 seconden. De tool vraagt dan 16,5 seconden en wint 18,5 seconden per reactie.

Bij 500 reacties per jaar is dat 2,57 uur. Ik neem €20 bruto per uur als aanname voor iemand die eventfeedback verwerkt; volgens de vuistregel uit de cursus is de kost voor de werkgever ongeveer €30 per uur. De bruto tijdwinst is dan €77,08. Min €0,03 toolkost blijft **€77,05 netto per jaar**. Bij de gemeten ondergrens van 80% score is de netto tijdwinst €62,47; het bereik is dus €62,47–€77,05. Mijn zwakste cijfer is de 35 seconden handwerk, want ik schatte die tijd. Als het handwerk maar 17,5 seconden duurt, blijft ongeveer €4,14 netto over. Dat beweegt veel meer dan mijn foutmarge.

## Mijn dashboard

Mijn publieke dashboard staat op https://event-feedback-overview-2026.braveswan3.chatgpt.site. Een lezer ziet daar eerst de score, de foutmarge en waarom ik Luna medium kies.

## Mijn AI-ismen

- Week 1: “De resultaten hielpen mij en zorgden ervoor dat ik meer tijd had voor andere dingen.” Herschreven: “Ik gebruikte Claude en ChatGPT voor planningen en taakverdelingen bij de scouts.”
- Week 2: “Een taalmodel past bij deze taak omdat bezoekers hun mening in vrije en soms rommelig geschreven tekst geven.” Herschreven: “Mijn tien testreacties bevatten Nederlands, Engels, korte zinnen en spelfouten.”
- Week 2: “Zo kan een eventorganisator achteraf zien welke verbeterpunten het vaakst terugkomen.” Herschreven: “Na 500 labels kan de organisator tellen hoeveel reacties over prijs, programma of bereikbaarheid gaan.”
- Week 3: “Ik merkte dat duidelijke afspraken vooraf heel belangrijk zijn.” Herschreven: “T07 kreeg in alle zes foutmargeruns een ander label dan het vooraf gekozen antwoord.”
- Week 3: “AI werkt beter als je een taak klein en concreet maakt.” Herschreven: “Mijn prompt met acht labels haalde 9/10 in drie runs.”
