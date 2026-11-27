# Live Query week 6 (ruwe notities)

**Vraag (letterlijk):** Hoe vraag ik compensatie voor een vertraagde trein in België?

| | Claude run 1 | Claude run 2 | Google AI-modus |
|---|---|---|---|
| Zoekopdrachten van de AI | niet genoteerd | niet genoteerd | niet zichtbaar |
| Pagina's die de AI las | NMBS eigen site (3×: voorwaarden, berekenen, uitbetaling) · pers (VRT NWS, staking maart 2026) · juridische site (Securex Lex4You) | NMBS eigen site (3×, dezelfde pagina's) · pers (VRT NWS, zelfde artikel) · Eurostar eigen site | NMBS eigen site (2×: compensatie, compensatie berekenen) |
| Genoemde organisaties | NMBS | NMBS (Eurostar alleen als "andere regels") | NMBS (alleen links, geen uitleg) |
| Zou een kenner dezelfde noemen? | | | |
| Wie had er moeten staan? | Ombudsman voor de treinreizigers | Ombudsman voor de treinreizigers | Ombudsman voor de treinreizigers |

Run 2 en Google: dezelfde organisaties? Ja, alle drie alleen de NMBS.

## Opvallend
- Run 2: bijna hetzelfde als run 1. Securex valt weg, Eurostar komt erbij. Weer alleen de NMBS als plek om hulp te vragen.
- Google AI-modus: alleen 2 links naar de NMBS-site, geen derden, geen uitleg.
- Run 1: het antwoord verwijst alleen naar de NMBS zelf. Derden (VRT, Securex) worden gebruikt als bron, maar niet als plek om hulp te vragen.

## Waarom die wel, en die niet?
Bewijs: bij het zelf opzoeken werd de Ombudsdienst nergens vermeld, alleen als je er expliciet naar zocht.

De NMBS wordt wel genoemd omdat ze overal staat, ook in de pers. De Ombudsman voor de treinreizigers niet, omdat hij bijna nergens vermeld wordt en je hem alleen vindt als je er expliciet naar zoekt.

# GEO-audit: Ombudsdienst voor de treinreizigers (ombudsrail.be)

| Criterium | Score en bewijs |
|---|---|
| 1 · Gestructureerde data | 0 · https://www.ombudsrail.be/nl/klacht-indienen toont in validator.schema.org "Geen items gedetecteerd" |
| 2 · Leesbaar voor AI | 1 · klachtenpagina zonder duidelijke kopjes en zonder antwoord in één zin bovenaan; basisfeiten (termijn, wat meesturen, eerst bij de spoorwegonderneming klagen) staan deels in het formulier; "kosteloos" alleen op de homepage; de woorden "compensatie" en "vertraging" staan niet op de pagina |
| 3 · Vermeldingen door anderen | 0 · bijna nergens in de pers; Google Nieuws "ombudsrail": 5 artikels, allemaal van Ombudsrail zelf |
| 4 · Echt genoemd in AI-antwoorden | 0 · Live Query: in geen van de 3 runs genoemd (Claude 2×, Google AI-modus 1×: alleen de NMBS) |
| 5 · Autoriteit | 3 · ombudsmannen benoemd bij Koninklijk Besluit; lid van het netwerk van Belgische ombudsdiensten (ombudsman.be); jaarverslag op de site |
| 6 · Zoeken op de merknaam | 2 · gevonden en juist, maar alleen met de exacte naam |

**Totaal: 6/18 → onzichtbaar (0–6).**

Tactiek: De Ombudsdienst zou eerst en vooral gelinkt moeten worden op de site van de NMBS, op de plek waar klanten lezen wat ze kunnen doen als ze het niet eens zijn met de reactie en die willen aanvechten.
