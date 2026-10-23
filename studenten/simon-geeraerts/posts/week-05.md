# Post week 5

## Mijn foutmarge

Ik dacht eerst dat mijn nieuwe prompt beter was, maar extra testen toonden bijna geen verschil. Met meer verschillende vragen krijg je een beter beeld; met maar enkele vragen kan een juiste score toeval zijn.

- Model: `gpt-6-luna`
- Vorige prompt: 13/13, 12/13, 13/13 → bereik 12–13/13
- Huidige prompt: 12/13, 13/13, 13/13 → bereik 12–13/13
- n = 13, drie nieuwe runs per promptversie
- Conclusie: de verbetering van de huidige prompt is niet bewezen; de claim is ingetrokken.

## Model en effort

Mijn gok klopte: je hebt geen heel zwaar model nodig voor deze taak. Luna haalde 12 of 13 op 13 en kost bijna niets. De andere modellen scoorden hetzelfde en waren ongeveer twintig keer duurder, dus ik kies Luna.

- Luna, Terra en Sol scoorden elk 12/13, dus binnen de foutmarge.
- Luna kost €0,0000514 per run en €0,0185 per jaar bij 360 vragen.

## Mijn value chain, met de foutmarge erin

Uit mijn berekening blijkt dat de tool ongeveer 9 minuten per vraag kan besparen. Op een jaar zou dat zo'n 56 tot 57 uur en €2.225 tot €2.280 kunnen opleveren. Die 30 vragen per maand heb ik geschat op basis van mijn eigen ervaringen bij Ford Geeraerts, omdat ik daar niet echt een exact cijfer over kan bekomen.

- Netto per jaar: €2.224,60–€2.279,98.
- Zwakste cijfer: 30 vragen per maand; dit is een eigen inschatting.

## Mijn dashboard

https://raw.githack.com/SimonGeeraerts/advanced-ai-nl/week-05/studenten/simon-geeraerts/build/dashboard.html

Ik wil dat je meteen ziet hoeveel tijd en geld de tool kan besparen en hoe goed hij scoorde bij de testen.

## Mijn AI-ismen

> Week 1: “Dit kan helpen in het productieproces.”

Tijdens mijn etiketten-test onderscheidde de AI waterflessen met een recht etiket van flessen met een scheef etiket.

> Week 4: “Zo werd de tool stap voor stap duidelijker en betrouwbaarder.”

De huidige prompt scoorde 12/13, 13/13 en 13/13, maar was door de overlappende foutmarge niet aantoonbaar beter dan de vorige prompt.

> Week 4: “Wat mij vooral verraste is dat de kost per vraag echt heel laag is.”

Ik was verbaasd dat één vraag maar €0,0000514 kost en dat dit bij 360 vragen per jaar ongeveer €0,0185 is.

> Week 4: “Als het goedkopere model doet wat het moet doen, is dat voorlopig goed genoeg.”

Luna, Terra en Sol scoorden elk 12/13, binnen mijn foutmarge van 12–13; ik kies Luna omdat die €0,0000514 per run kost.

> Week 4: “Ik zou de tool nu al aanraden om verder te gebruiken bij Ford Geeraerts, omdat de laatste testen allemaal juist waren en hij veel tijd kan besparen.”

In mijn test runs scoorde de tool 12 of 13 op 13, maar omdat ik alleen fictieve gegevens gebruikte, moet ik eerst met echte gegevens controleren of dat resultaat overeind blijft.

## Mijn testset groeit

Ik voegde 20 nieuwe vragen toe: gewone klantvragen, korte en anderstalige vragen en vragen met ontbrekende info. Zo test ik of de assistent eerlijk zegt dat hij iets niet weet. T15 verraste mij het meest: hij gaf de huidige datum, maar zei niet dat hij niet kan weten of die veranderd is. Op set v2 scoorde de laatste prompt 26 op 30 (n = 30, 1 run, `gpt-6-luna`).
