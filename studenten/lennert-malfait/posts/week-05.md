# Week 5 — Mijn testset groeit

## Mijn foutmarge

Mijn vorige v2- en v3-runs op T01–T10 lagen allebei tussen 7 en 9 op 10. De bereiken overlappen volledig, dus mijn eerdere claim dat v3 bewezen beter was, trek ik in. De claim is ingetrokken. De nieuwe controle is groter: set v2 bevat T01–T30 en v3 scoorde 19 op 30 in één run.

## Model en effort

Mijn gok vooraf was dat lage effort genoeg zou zijn voor deze vier eenvoudige labels. Sonnet, Haiku en Opus kon ik in mijn lokale Codex-runner niet uitvoeren; ik verzin daar geen scores voor. De beschikbare setups met gpt-5.6-luna waren medium 8/10, low 9/10 en high 8/10 op n = 10. Ik zet low effort voorlopig in productie. De prijsaanname blijft ongeveer €0,00080 per run.

## Mijn value chain, met de foutmarge erin

Handmatig schat ik 55 seconden per mail: 40 seconden lezen, 10 seconden beslissen en 5 seconden verplaatsen. Met de tool duurt draaien en nakijken ongeveer 13 seconden. Op basis van de vorige foutmarge van 70–90% juist blijft de totale tijd ongeveer 18,5–29,5 seconden per mail. Dat geeft 25,5–36,5 seconden winst. Bij 100 mails per maand is dat ongeveer 8,5–12,2 uur per jaar. Met €15 per uur is de waarde €127,50–€182,50. Na ongeveer €0,96 toolkost blijft €126,54–€181,54 over. Het zwakste cijfer is mijn handmatige 55 seconden, want die is niet met een chronometer gemeten.

## Mijn dashboard

Het dashboard staat op [de publieke dashboardpagina](https://raw.githack.com/LennertM4/advanced-ai-nl/week-05/studenten/lennert-malfait/build/dashboard.html). Daar staan de vorige foutmarge, set v2, de setups en de kosten samen.

## Mijn AI-ismen

- “Daardoor kan ik de uitkomst ook gemakkelijk controleren.” → “Ik vergelijk het JSON-label met de verwachte labelkolom.”
- “Zo test ik niet alleen makkelijke schoolmails.” → “Ik gebruik ook een Franse correctiemail, een tokenmail en een onduidelijke service-mail.”
- “Dit is een goed teken, maar nog geen bewijs.” → “Een score van 19 op 30 is één run en bewijst geen algemene betrouwbaarheid.”
- “Daarom is dit een transparante schatting, geen factuurbedrag.” → “De prijs is een aanname op basis van de zichtbare tokenmeting.”
- “De beslissing hangt dus meer af van de tijd die controle kost dan van de kleine tokenkost.” → “De controle op foute labels bepaalt de waarde sterker dan €0,96 toolkost.”

## Mijn testset groeit

Ik heb 20 nieuwe inputs uit mijn echte Outlook-inbox gekozen: echte opdrachtmails, een andere taal, een tokenmelding, een nieuwsbrief, automatische digests, exameninformatie en korte of contextafhankelijke berichten. De oude T01–T10 bleven ongewijzigd. Voor T11–T30 schreef ik eerst mijn eigen label en reden op. Daarna draaide ik één run van de laatste prompt op alle 30. De score is **19/30 (set v2, 1 run)**. De nieuwe set verraste mij vooral bij de Canva-groep en de Canvasmelding: mijn persoonlijke context maakte daar het verschil tussen lezen, doen en negeren.
