# Week 6 — Waar haalt mijn tool zijn antwoord vandaan?

## Mijn live query

Ik koos Outlook-gebruikers die inkomende mail automatisch op prioriteit willen ordenen en actiemails willen herkennen. In twee aparte ChatGPT-zoekopdrachten kwam Copilot als directe match naar voren. Fyxer had erbij mogen staan als Outlook-alternatief: de productpagina beschrijft automatische prioritering. Google AI Mode noemde alleen Copilot; de bedrijven uit run 2 en Google waren dus niet dezelfde. De tabel met zichtbare pagina's staat in [de Live Query-log](../build/week-06-live-query.md). Mijn verklaring is een aanwijzing, geen bewezen oorzaak: Copilot is ingebouwd in Outlook en de zichtbare Google-bronnen kwamen vooral van Microsoft.

## Kan AI dit bedrijf vinden?

Ik onderzocht Fyxers Outlook-assistent. De audit komt uit op **15/18**. De productpagina is duidelijk en bevat JSON-LD voor onder meer FAQPage en SoftwareApplication; ik controleerde dat handmatig in de HTML. Onafhankelijke vergelijkingspagina's noemen Fyxer ook. In de AI-antwoorden bleef de zichtbaarheid beperkt, vooral tegenover Microsoft Copilot. Mijn eerste tactiek is een onafhankelijke, citeerbare vergelijking met concrete Outlook-use-cases en beperkingen. Bewijs en scores staan in [de GEO-audit](../build/week-06-geo-audit.md).

## Mijn tool leest een bron

Ik gebruikte het officiële [Arteveldehogeschool onderwijs- en examenreglement 2026–2027](../build/bronnen/artevelde-onderwijs-en-examenreglement-2026-2027.pdf), omdat de tool algemene schoolregels en exameninformatie nodig kan hebben. Vooraf legde ik vier vragen vast waarvan het antwoord in het reglement staat en één vraag over een persoonlijke examendatum die de bron niet bevat. In vijf afzonderlijke verse sessies waren **5/5 antwoorden correct**. Er ging dus geen antwoord fout; ik kan geen foutgeval als testresultaat aanwijzen. B05 was het lastigste geval: de tool gaf geen persoonlijke datum en verwees naar Mijn Dinar of de opleiding. Dat was correct omdat het reglement die persoonlijke planning niet bevat. De vooraf vastgelegde vragen en uitkomsten staan in [de brontest](../build/test-set-bron.md); de broninstructies staan in [broninstructies](../build/bron-instructies-week-06.md).

**Dashboard van een klasgenoot:** In [Mohameds dashboard](https://raw.githack.com/alexandernacho/advanced-ai-nl/main/studenten/mohamed-camara/build/dashboard.html) trekken de twee grote kaarten bovenaan meteen de aandacht naar de foutmarge van 3–3/5 en de netto jaarwaarde van €210,61, waarna de tabellen de onderbouwing geven.
