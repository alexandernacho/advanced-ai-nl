# Week 6: de AI noemt vooral wie de Belgische vraag beantwoordt

## Mijn live query

**Vraag (letterlijk):** Welke ETF is beste voor beginners in België?

| | Run 1: eigen AI | Run 2: eigen AI | Run 3: Google AI-modus |
|---|---|---|---|
| Tool | Claude (Sonnet 5.5) | Claude (nieuwe sessie) | Google AI-modus |
| Zoekopdrachten van de AI | `beste ETF beginners België 2026 TOB` en `meerwaardebelasting België 2026 ETF vrijstelling 10.000 euro` (achteraf aan Claude gevraagd) | niet genoteerd | niet genoteerd |
| Pagina's die de AI las | 36 zoekresultaten, alleen snippets. 13 aanbieders met eigen belang (Curvo 11, Easyvest 2), 5 banken, 4 advies, 10 Test-Aankoop, 3 vakmedia, 1 Morningstar. Geen reviews, geen forums | 36 zoekresultaten: 26 Curvo, 4 Test-Aankoop, 2 Easyvest, 1 freenance.io, 1 Reddit-spiegel, 2 docs.google.com | andere bronnen dan Claude, wel nog Curvo, plus KBC en Ewoud Bogaert. Geen justETF |
| Genoemde ETF's | IWDA, VWCE | IWDA, VWCE, SPDR ACWI IMI, EMIM (als combinatie) | SWRD, IWDA, WEBN, IMIE. VWCE alleen als slecht voorbeeld (TOB 1,32%) |

**Zou een kenner van deze markt dezelfde noemen?** Hoogstwaarschijnlijk niet, omdat ik zelf MWEQ zou aanraden: daar krijgt elk bedrijf hetzelfde gewicht in de ETF. De AI noemt in alle runs gewone MSCI World- en All-World-ETF's, waar grote bedrijven zwaarder tellen, en MWEQ staat in geen enkele run.

**Wie had er moeten staan?** justETF. Hij staat in geen enkele run, ook niet bij Google.

**Run 2 en Google: dezelfde bedrijven?** Alleen IWDA staat in alle drie de runs. Curvo is als bron in alle drie aanwezig.

**Waarom die wel, en die niet?**
Curvo staat er waarschijnlijk wel in omdat Curvo artikels heeft die precies de Belgische vraag beantwoorden. Het justETF-artikel dat ik las heeft geen België, geen TOB en noemt IWDA of VWCE niet.

| | Curvo | justETF |
|---|---|---|
| Reviews | 18, 4 op 5 | 53, 4,5 op 5 |
| Pers / vergelijkingssites | geen, alleen eigen artikels | geen, alleen eigen artikels |
| Artikel "beste ETF beginner België" | ja, met België, TOB, ISIN en TER | artikel zonder België, TOB, IWDA of VWCE |

## Kan AI dit bedrijf vinden?
**Bedrijf:** justETF (vergelijkingssite voor ETF's). Het ontbrak in al mijn drie runs.

| Criterium | Score en bewijs |
|---|---|
| 1 · Gestructureerde data | 3 · `https://www.justetf.com/nl/etf-profile.html?isin=IE00B4L5Y983` toont `BreadcrumbList / FAQPage`. De FAQ heeft 6 vragen met antwoord (naam, ticker, ISIN, kosten 0,20%, accumulerend, fondsgrootte). Zwak: de FAQ staat in het Engels op een `/nl/`-pagina, en er is geen vraag over België of de beurstaks. |
| 2 · Leesbaar voor AI | 3 · Een hoofdkop met de naam van de ETF en twaalf tussenkoppen (o.a. Kosten, Risico, Veelgestelde vragen). Bovenaan één zin: "The iShares Core MSCI World UCITS ETF USD (Acc) seeks to track the MSCI World index. The MSCI World index tracks stocks from 23 developed countries worldwide." ISIN en TER (0,20%) staan op de pagina. Zwak: die zin is Engels op een `/nl/`-pagina. |
| 3 · Vermeldingen door anderen | 3 · 53 reviews, gemiddeld 4,5 op 5. Pers: De Standaard noemt justETF (https://www.standaard.be/economie/geld/ontdek-twee-goudmijnen-vol-info-voor-hangmatbeleggers/99370182.html). Forumvermeldingen op Reddit (`r/beleggen` en `r/ETFs_Europe`, o.a. https://www.reddit.com/r/ETFs_Europe/comments/1qzhiby/doubt_regarding_the_returns_presented_in_justetf/). Geen vergelijkingssite gevonden. Zoeken op `justetf` geeft alleen eigen artikels: de vermeldingen vind je pas als je `reddit` toevoegt. |
| 4 · Echt genoemd in AI-antwoorden | 0 · justETF kwam in geen van mijn drie runs voor (Claude 2×, Google AI-modus 1×), niet in de antwoorden en niet in de lijsten met zoekresultaten. |
| 5 · Autoriteit | 3 · Opgericht in 2011 door Dominique en Petra Riedl, sinds 2021 deel van de Scalable Group (zelf een broker, dus met een eigen belang). Eigen onderzoek (justETF Research). Genoemd in De Standaard. |
| 6 · Zoeken op de merknaam | 3 · Google op `justetf`: de officiële site staat bovenaan. Claude op "Wat is justETF?": de AI kent het, legt het juist uit (ETF-portaal, geen broker) en noemt de Belgische versie `justetf.com/nl-be`, die bestaat (gecontroleerd). Hij zegt zelf dat justETF niets zegt over de Belgische belasting (TOB). |

**Totaal:** 15 op 18 (aanwezig)
**Tactiek:** justETF moet als eerste een Nederlandstalige pagina maken voor Belgische beginners ("Beste ETF voor beginners in België"), met een antwoord in de eerste zin en een tabel met ISIN, TER en beurstaks (TOB), omdat Curvo precies zo'n pagina heeft en justETF niet. Nu staat justETF in geen enkele AI-run, ook al vindt de AI het bedrijf wel op de naam.

## Mijn tool leest een bron
**Document:** het KID van Invesco MSCI World Equal Weight (NL), `build/bronnen/invesco-kid.md`. Ik koos het toevallig, maar het is een goed document voor mijn tool omdat ik dit KID zelf las toen ik deze ETF kocht.

**Score: 4 op 5.** Ik schreef de antwoorden zelf, vóór de run, en keek elk antwoord zelf na (n = 5, 1 run, elk in een nieuwe sessie).

**Hoe weet ik dat het uit het document komt?** Bij B01 gaf de tool als bron de regel `Stress  Er is geen minimaal gegarandeerd rendement ... 4.280 USD`, met de rommelige opmaak uit de pdf. Die regel staat letterlijk in het document (regel 123).

**Waar het fout ging: B05** (het TOB-tarief voor een Belgische belegger, dat niet in het document staat). De tool zei dat hij het antwoord niet wist, maar zette er een bron bij: de zin over "persoonlijke fiscale situatie". Mijn prompt eiste bij elk antwoord een bron. Er was geen plek voor "geen bron", dus de tool pakte de zin die het dichtst bij de vraag lag. Aanpassing: bij een antwoord dat niet in het document staat schrijft de tool "geen bron, want het staat niet in het document". Een nieuwe run van B05 was daarna juist. Dat is één run, na het zien van de fout, dus het bewijst niet dat het altijd werkt.
