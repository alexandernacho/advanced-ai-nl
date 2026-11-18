# Week 6: Mijn tool vond een regel die ik zelf niet kende

## Mijn live query

| | Eigen AI 1 | Eigen AI 2 | Google AI-modus |
|---|---|---|---|
| De vraag | "Waar koop ik goedkope knuffels in bulk om door te verkopen in België?" | "Waar koop ik goedkope knuffels in bulk om door te verkopen in België?" | "Waar koop ik goedkope knuffels in bulk om door te verkopen in België?" |
| Zoekopdrachten van de AI | "knuffels groothandel België bulk inkopen wederverkoop", "plush toys wholesale supplier EU low MOQ" | "knuffels groothandel België B2B", "plush toys wholesale Europe supplier EU warehouse dropshipping" | niet zichtbaar |
| Pagina's die de AI las | alibaba.com (3x), faire.com, action.com | qogita.com, faire.com, merkandi.us, bigbuy.eu, hackceleration.com, droppery.io, hertwill.com | megamaga.be, plushtrading.be, piasofttoys.com, afhaalgroothandel.be, e-stocklots.be, merkandi.be, orderchamp.com, bellustoys.com, meekestrade.com, vandermeulen.com |
| Type pagina's | vooral vergelijkingssite (platforms met veel leveranciers) | vooral vergelijkingssite (platforms met veel leveranciers) | vooral eigen site (groothandels zelf) |
| Genoemde bedrijven | Alibaba, Global Sources, Faire, Action | Alibaba, AliExpress, Qogita, Faire, Merkandi, BigBuy, Droppery, Hertwill | Plush Trading Company, Megamaga, PIA International, Afhaalgroothandel.be, e-Stocklots, Merkandi, Gompies, Orderchamp, Bellus Toys, Meekes, Van der Meulen, Otto Simon |
| **Zou een kenner van die markt dezelfde noemen?** | Ja. Als je goedkoop wil inkopen, kom je bij China uit. Belgisch inkopen is duurder voor dezelfde kwaliteit. | | |
| **Wie had er moeten staan?** | Megamaga. Belgisch, lage minimale afname. Google noemt het, Claude niet. | | |
| **Run 2 en Google: dezelfde bedrijven?** | Nee. Run 1 en 2 hebben alleen Alibaba en Faire gemeen. Run 2 en Google alleen Merkandi. | | |

Claude las bij beide runs eerst mijn memory. Een extra run met Research-modus (36 zoekopdrachten) vond wel Bellus Toys en megamaga.be.

### Waarom die wel, en die niet?
Merkandi toont prijzen en lange productteksten aan iedereen, bij Megamaga moet je inloggen voor prijzen en staan er vooral foto's met korte teksten, dus een AI vindt daar weinig om te lezen.

## Kan AI dit bedrijf vinden?

Megamaga (megamaga.be, Kruisem)

| Criterium | Score | Bewijs |
|---|---|---|
| 1 · Gestructureerde data | 2/3 | validator.schema.org op https://www.megamaga.be/nl/beer-grijs-pluche-15cm.html toont Organization / BreadcrumbList / WebSite / Product. Prijs voor mensen alleen na login, maar in de code staat ecomm_totalvalue 5.45. |
| 2 · Leesbaar voor AI | 1/3 | Prijzen achter login, korte afgekapte teksten, sjabloontekst "Button text" en "Custom price filter title". |
| 3 · Vermeldingen door anderen | 1/3 | Alleen in bedrijfsregisters (companyweb.be, creditsafe), geen reviews, fora of pers gevonden. |
| 4 · Echt genoemd in AI-antwoorden | 1/3 | Claude 0 keer in 2 runs, Google AI-modus en een Research-run wel. |
| 5 · Autoriteit | 1/3 | Over ons toont alleen adres en btw (Mega Import BV), geen jaartal, cijfers of erkenning. |
| 6 · Zoeken op merknaam | 1/3 | Op "megamaga" alleen komen games, met "megamaga groothandel" wel de site. |

**Totaal: 7 op 18, marginaal (net).**

**Tactiek:** echte productteksten op elke productpagina zetten (wat het is, maat, materiaal, minimale afname) en de sjabloontekst weghalen, zodat een AI iets kan lezen, ook zonder prijs.

## Mijn tool leest een bron

Ik koos de catalogusregels van Vinted als document. Mijn risico D ging nog over bol.com, maar ik verkoop op Vinted, dus dat klopte niet meer. Ik schreef 5 vragen met mijn antwoord eerst en liet ze draaien met Haiku 5.5. Score: 4 op 5.

Let op: de vragen liepen niet via mijn prompt v4, die is gemaakt voor productpagina's, maar via een korte instructie met het document erbij. Ik testte dus vooral of het model het document goed leest.

B01 was maar half juist. De tool zei dat speelgoed mag, maar zei niets over Vinted Pro of regelmatig verkopen. Ik denk dat hij gewoon de eerste regel pakte die paste en niet verder zocht in het document.

Het grootste wat ik leerde: Vinted verbiedt het doorverkopen van nieuwe spullen die je in bulk of bij een leverancier koopt, ook met Vinted Pro. Dat is net wat ik doe met mijn knuffels. Dat wist ik niet. Ik moet dus nadenken of Vinted wel de juiste plek is.

Nadeel: het document is lang (8.798 woorden), dus elke run kost meer dan vroeger.
