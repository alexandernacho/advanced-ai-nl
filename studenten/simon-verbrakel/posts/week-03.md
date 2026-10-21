# Week 3 — Voorbeelden, grijze zones en een regel die half werkt

## Wat ontbrak er in mijn context?
In mijn context ontbraken voorbeelden. Het model kreeg wel vijf labels met uitleg, maar zag nooit hoe een bericht met het juiste label eruitziet. Daarnaast ontbraken regels voor de grijze zones. Bij de buurtest twijfelde de buur bij T05 (extra defensiegeld, betaald met besparingen elders) en bij T09 (een defensiebedrijf dat een fabriek bouwt), omdat mijn prompt daar niets over zei. Bij T05 kozen de buur en het model allebei positief, en ik moest toegeven dat mijn eigen antwoord fout was. Een zwakte van mijn buurtest is wel dat de buur Claude was in een apart gesprek, geen mens. Een echte klasgenoot had misschien op andere dingen gelet.

## Mijn eerste cijfer
Met de nieuwe prompt had het model 8 op 10 antwoorden juist (80%). Dat zijn wel 5 inputs (T06 tot T10) die elk twee keer gedraaid zijn, dus geen 10 verschillende metingen. Er was één fout: T08, in beide runs F1 (fout). Het model was zeker van "negatief", terwijl het juiste antwoord "onzeker" was. Dit cijfer zegt dat de prompt goed werkt op deze vijf berichten en dat het model consistent is. Het zegt niet hoe goed de tool in het algemeen is: vijf inputs is weinig, en T01 tot T05 heb ik nog niet met de nieuwe prompt gedraaid.

## Eén wijziging
Mijn wijziging was één nieuwe regel: "Gaat het bericht over gesprekken of onderhandelingen zonder akkoord, kies dan onzeker, want pas een getekend akkoord verandert de vraag naar defensie." Daarna draaide ik T08 opnieuw: Run 1 gaf negatief, Run 2 gaf onzeker. De fout ging dus van F1 (zeker fout) naar F6 (wisselend). De regel helpt een beetje, maar niet altijd. Het woord "productieve" trekt het model nog richting negatief. Omdat het maar één input is en ik de regel precies op deze fout schreef, bewijst dit weinig. Of de regel echt werkt, test ik volgende week op andere berichten.
