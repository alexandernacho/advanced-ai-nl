# Week 6: Kwartaalcijfers van NVIDIA terugvinden

## Mijn live query

> Vat de belangrijkste cijfers uit het meest recente kwartaalrapport van NVDA samen. Vergelijk de omzet, nettowinst en winst per aandeel met de eerdere kwartalen waarvoor je cijfers hebt gevonden. Vermeld per vergelijking de periode en het verschil in bedrag en procent, waar dat zinvol is. Geef aan welke kwartaalcijfers ontbreken en vermeld je bronnen.

| Run | Zichtbare zoekopdrachten | Bronnen in het antwoord | Gevonden kwartalen |
|---|---|---|---|
| 1 · ChatGPT | Twee zoekopdrachten op NVIDIA Newsroom naar Q3 en naar Q1–Q2 FY2027. | Twee officiële NVIDIA-publicaties, voor Q3 en Q1 FY2027, met cijfers uit eerdere kwartalen. | 5 · Q3 FY2026 t/m Q3 FY2027 |
| 2 · Codex | Zocht op NVIDIA Newsroom naar Q3 FY2027 en op SEC EDGAR naar de 10-Q voor 25 oktober 2026. | NVIDIA Investor Relations en NVIDIA Newsroom, met directe links naar publicaties voor Q4 FY2026 en Q1–Q3 FY2027. | 5 · Q3 FY2026 t/m Q3 FY2027 |
| 3 · Google AI-modus | De zoekopdrachten waren niet zichtbaar in het gedeelde antwoord. | Zeven officiële NVIDIA-publicaties, vermeld met titel en datum. | 7 · Q1 FY2026 t/m Q3 FY2027 |

Alle drie de runs noemden NVIDIA en kwamen na afronding overeen over de omzet, nettowinst en verwaterde winst per aandeel voor de vijf gedeelde kwartalen. Google nam ook Q1 en Q2 FY2026 op. Ik vond het antwoord van Codex makkelijker te controleren omdat het korter was en rechtstreeks naar de kwartaalpublicaties linkte.

Een kenner zou bij de ticker NVDA ook NVIDIA verwachten. De vraag legde het bedrijf vooraf vast, dus ik kon hiermee niet testen welk ander bedrijf een AI spontaan zou noemen of missen. Google vermeldde twee oudere kwartaalpublicaties in zijn antwoord, maar ik kon niet zien waarom het die wel opnam.

[NVIDIA Q3 FY2027](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-third-quarter-fiscal-2027) · [NVIDIA Q1 FY2027](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2027)

## Kan AI dit bedrijf vinden?

**NVIDIA scoort 14 op 18** en valt daarmee in de categorie *aanwezig*.

| Criterium | Score | Bewijs |
|---|---:|---|
| Gestructureerde data | 1/3 | De HTML van de geteste Q3-publicatie bevat Open Graph-markering met `og:type=article`. In de opgehaalde HTML werd geen Schema.org-type in JSON-LD of microdata gevonden. [Geteste Q3-pagina](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-third-quarter-fiscal-2027) |
| Leesbaar voor AI | 3/3 | De kwartaalperiode, omzet en omzetgroei staan bovenaan. De GAAP-tabel laat het vorige kwartaal en hetzelfde kwartaal een jaar eerder zien. [Q3-publicatie](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-third-quarter-fiscal-2027) |
| Vermeldingen door anderen | 2/3 | Reuters en The File berichtten over de kwartaalcijfers. De score steunt op deze twee voorbeelden. [Reuters via Investing.com](https://www.investing.com/news/stock-market-news/nvidia-forecasts-quarterly-revenue-above-estimates-in-first-report-since-huangs-exit-as-ceo-5034097) · [The File](https://thefile.news/story/nvidia-q3-fiscal-2027-results-nov17) |
| Genoemd in AI-antwoorden | 2/3 | Alle drie de runs noemden NVIDIA. De ticker stond al in mijn vraag, waardoor spontane vindbaarheid ongetest blijft. |
| Autoriteit | 3/3 | NVIDIA publiceert gedetailleerde financiële cijfers en diende de kwartaalpublicatie als bijlage bij een Form 8-K in bij de SEC. [SEC-dossier](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000088/nvda-20261117.htm) |
| Zoeken op merknaam | 3/3 | Bij een webzoekopdracht met `NVIDIA NVDA` verscheen de officiële aandelenpagina met de ticker. [NVIDIA Investor Relations](https://investor.nvidia.com/stock-info/stock-quote-and-chart/default.aspx) |

Mijn voorgestelde tactiek is om `NewsArticle`-markering in JSON-LD toe te voegen aan de kwartaalpublicaties. Zo kunnen zoekmachines de titel, publicatiedatum en uitgever rechtstreeks uit de pagina halen.

## Mijn tool leest een bron

Ik gebruikte de officiële kwartaalpublicatie van NVIDIA voor Q3 FY2027 om te testen of mijn tool cijfers uit een rapport haalt en ze met eerdere kwartalen vergelijkt. Ik beoordeelde **5 van de 5 antwoorden als juist**. Bij B01 gebruikte de tool ook de officiële Q2-publicatie om de omzetgroei van 20,4% te berekenen. De Q3-publicatie geeft die groei afgerond weer als 20%. Bij B05 maakte de tool correct het onderscheid tussen de omzetprognose en de gerealiseerde omzet. De antwoorden vermeldden geen secties of paginanummers.

[Testset en antwoorden](../build/test-set-bron.md) · [NVIDIA Q3 FY2027](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-third-quarter-fiscal-2027) · [NVIDIA Q2 FY2027](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027/)
