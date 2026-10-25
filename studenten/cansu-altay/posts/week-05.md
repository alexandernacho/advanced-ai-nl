# Week 5: Van schattingen naar tests in mijn AI-trainingslog

<!-- Door Cansu als geheel nagelezen en goedgekeurd. -->

## Mijn foutmarge

Ik verwachtte dat v5 beter zou scoren doordat de tool bij onduidelijke sets ‘onbekend’ schrijft. Codex testte v4 en v5 elk driemaal met dezelfde tien notities op GPT-5.6 Terra, effort high. V4 scoorde 9/10, 8/10 en 9/10; v5 8/10, 9/10 en 8/10 (n = 10, 3 runs). Beide bereiken zijn 8–9/10. Ik trek mijn algemene verbeterclaim in: v5 verwerkt de onduidelijke sets beter, maar de globale nauwkeurigheid lijkt vergelijkbaar. Eén notitie is ook een promptvoorbeeld. Ik controleerde twee antwoorden; bij één accepteerde ik een compactere uitvoer dan vooraf afgesproken. Dat verschil is bewaard, zonder de score achteraf te wijzigen.

## Model en effort

Ik verwachtte meer fouten bij een kleiner model op rommelige notities. Met dezelfde v5-prompt scoorde GPT-5.6 Terra 9/10, Luna 10/10 en Sol 8/10, allemaal effort high (n = 10, 1 run). Terra en Sol vielen binnen het eerdere Terra-bereik; Luna erboven. De geraamde kosten per notitie zijn respectievelijk $0,001946, $0,0003344 en $0,004010. Ik kies voorlopig Luna vanwege de score en kosten, maar wil extra onduidelijke notities testen. Eén ronde bewijst geen foutloze werking; Luna heeft nog geen eigen foutmarge.

## Mijn value chain, met de foutmarge erin

Ik schat drie minuten uitproberen zonder overzicht, tegenover twee keer dertig seconden terugzoeken met overzicht. Typen, wachten en nakijken passen volgens mijn inschatting binnen gewone rust. Correcties kosten gemiddeld 45 seconden, waarvan slechts een deel extra trainingstijd is.

Met 5–6 notities per training en 10–20% fouten als gevoeligheidsscenario kost volledig extra herstelwerk 22,5–54 seconden. Dat laat 66–97,5 seconden winst per training over: 2,86–4,225 uur bij drie trainingen per week en 52 weken. Passen correcties volledig binnen rust, dan resteert 5,2 uur.

Mijn persoonlijke uurwaarde van €15–€17 geeft na circa €0,23–€0,28 Luna-modelkosten een vergelijkingswaarde van €42,62–€71,59 zonder overlap, of €77,72–€88,17 bij volledige overlap. Dit zijn geen inkomsten of werkgeversloonkosten. Het foutenbereik komt van Terra, niet Luna. Alle tijden zijn schattingen; het overzicht is nog niet gebouwd. Bij halvering van de uitprobeertijd kan tijdverlies ontstaan. Ik wil de terugzoektijd eerst meten zodra het overzicht bestaat.

## Mijn dashboard

[Mijn publieke dashboard](https://raw.githack.com/C6nsuuu/advanced-ai-nl/week-05/studenten/cansu-altay/build/dashboard.html). De lezer moet eerst zien dat de verbetering van v5 niet bewezen is.

## Mijn AI-ismen

Week 4:
> Deze berekening heeft mijn visie uitgebreid.

Ik was verrast dat de geraamde kosten van ongeveer €0,11–€0,13 per maand voor mezelf bij duizend keer zoveel gebruik stegen tot €106–€127 per maand (Sol-raming week 4).

Week 3:
> AI kan fouten maken en ik moet de antwoorden blijven controleren.

Als ik een verkeerd gewicht, aantal sets of aantal herhalingen bewaar, kan ik bij mijn volgende training verkeerde gegevens volgen en opnieuw tijd verliezen met uitzoeken wat ik echt deed.

Week 3:
> Voorbeelden geven de AI een duidelijke richting en tonen hoe ik de tabel wil zien.

Mijn voorbeelden laten zien dat de tabel ‘tot failure’ moet behouden als ik doorging tot ik geen herhaling meer kon uitvoeren, ook wanneer mijn herhalingsaantal onbekend is.

Week 4:
> Dit toont dat mijn huidige berekening nog niet helemaal betrouwbaar is, omdat ze op schattingen gebaseerd is.

Zodra het overzicht gebouwd is, wil ik eerst de geschatte 30 seconden terugzoeken per oefening meten, omdat meerdere zoekmomenten samen de terugzoektijd per training bepalen.

Week 3:
> Vier goede antwoorden betekenen niet dat de AI altijd goed werkt.

Ook na Luna's 10/10 op tien notities wil ik extra onduidelijke of rommelige trainingsnotities testen voordat ik op de betrouwbaarheid vertrouw.
