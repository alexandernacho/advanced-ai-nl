# Week 3 — Wat betekent "zelf maken"?

## Wat ontbrak er in mijn context?
Mijn tool leest de homepage van een bedrijf en zegt of het een mogelijke klant is voor DBA Hardwoods, de houthandel van mijn vader. Op dit moment ligt de focus op rubberwood. Een klant is dus een bedrijf dat zelf iets maakt in massief hout: trappen, meubels, keukens. Zonder e-mailadres op de site is het geen lead.

Deze week kwamen er vijf lastige inputs bij: een andere houthandel, een Engelstalige meubelwinkel, een renovatie-aannemer met twee e-mailadressen, een korte Engelse site zonder e-mail en een totaalaannemer. Het juiste antwoord schreef ik vooraf zelf op.

Bij Bautier ging het fout. Hun site zegt dat studio, workshop en winkel in Brussel zitten, maar dat de meubels in Duitsland gemaakt worden. Ik zei `nee`, want ze kopen zelf geen hout. Run 1 zei `ja`, run 2 zei `onzeker`.

Mijn prompt zei niet wat "zelf maken" precies betekent: een bedrijf dat meubels onder eigen naam verkoopt maar ze elders laat produceren, telt niet. Alleen een bedrijf dat zelf het hout verwerkt in een eigen werkplaats telt als ja, ook als de site woorden als "workshop" of "studio" gebruikt.

Bij de audit op de zes bouwstenen ontbraken ook de voorbeelden, en geen enkele regel had een "want". Ik voegde er één toe: "Raad nooit een e-mailadres, want een geraden adres bestaat misschien niet."

Buurtest met mijn papa, alleen met de prompt: drie keer hetzelfde antwoord als ik bij DL Interieur, Bautier en ER-Bouw. Ook hij zei: "workshop" bewijst niet dat ze zelf hout verwerken.

## Mijn eerste cijfer
18 op 20 juist (n = 10 inputs, 2 runs). Beide fouten zitten bij Bautier: één F1 (vol overtuiging `ja`) en één F6 (`onzeker`, een ander antwoord bij dezelfde input). Geen F2: de tool verzon in 20 runs geen enkel e-mailadres.

Ik vertrouw het cijfer maar half: met 10 bedrijven en 2 runs zijn het geen 20 onafhankelijke metingen, en beide fouten komen uit één geval, dus één extra lastig bedrijf kan de score sterk doen zakken. En dat de tool nooit een e-mailadres verzon, zegt weinig, want alleen Trappen Smet, Menuiserie Richard en Woontheater testen dat echt. Dat zijn 6 runs, te weinig om F2 uit te sluiten. Daarvoor heb ik meer testgevallen nodig waar het verleidelijk is om iets te verzinnen.

## Eén wijziging
Ik voegde één regel toe: "Verkoopt of plaatst het bedrijf alleen producten die ergens anders gemaakt worden? Dan nee, want het koopt zelf geen hout." Daarna gaf Bautier twee keer `nee`.

Dat is nog geen bewijs, omdat het niet toonde wat er precies anders ging, enkel dat T07 twee keer juist was. De andere negen bedrijven heb ik nog niet opnieuw gedraaid met de nieuwe regel, dus misschien gaat er nu een ander fout. En bij de eerste versie gaven twee runs al verschillende antwoorden, dus twee keer juist kan ook toeval zijn.
