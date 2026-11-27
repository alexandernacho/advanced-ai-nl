# Week 6: De Ombudsdienst is onzichtbaar voor AI

## Mijn live query

Vraag: "Hoe vraag ik compensatie voor een vertraagde trein in België?"

| | Claude run 1 | Claude run 2 | Google AI-modus |
|---|---|---|---|
| Genoemd | NMBS | NMBS | NMBS |

Alle runs lazen vooral de NMBS-site; Claude ook VRT NWS en Securex.

Zou een kenner dezelfde noemen? Ja, klanten vragen compensatie best aan via de NMBS. Maar zijn ze niet tevreden met de reactie op hun compensatie, dan kunnen ze die aanvechten via de Ombudsdienst. Die wordt echter niet genoemd, niet door de AI en niet door de NMBS.

Wie had er moeten staan? De Ombudsman voor de treinreizigers. Daar kan een klant terecht als hij het niet eens is met het antwoord van de NMBS. Run 2 en Google gaven dezelfde organisatie: alleen de NMBS.

De NMBS wordt wel genoemd omdat ze overal staat, ook in de pers. De Ombudsman voor de treinreizigers niet, omdat hij bijna nergens vermeld wordt en je hem alleen vindt als je er expliciet naar zoekt.

## Kan AI dit bedrijf vinden?

GEO-audit van de Ombudsdienst voor de treinreizigers (ombudsrail.be): **6/18, onzichtbaar.**

| Criterium | Score en bewijs |
|---|---|
| 1 · Gestructureerde data | 0 · https://www.ombudsrail.be/nl/klacht-indienen: "Geen items gedetecteerd" |
| 2 · Leesbaar voor AI | 1 · geen duidelijke kopjes, geen antwoord in één zin bovenaan, basisfeiten deels in het formulier; "compensatie" en "vertraging" staan niet op de pagina |
| 3 · Vermeldingen door anderen | 0 · Google Nieuws: 5 artikels, allemaal van Ombudsrail zelf |
| 4 · Echt genoemd in AI-antwoorden | 0 · in geen van mijn 3 runs |
| 5 · Autoriteit | 3 · benoemd bij Koninklijk Besluit, lid van het netwerk van Belgische ombudsdiensten, jaarverslag op de site |
| 6 · Zoeken op de merknaam | 2 · gevonden, maar alleen met de exacte naam |

Tactiek: de Ombudsdienst zou eerst en vooral gelinkt moeten worden op de site van de NMBS, op de plek waar klanten lezen wat ze kunnen doen als ze het niet eens zijn met de reactie en die willen aanvechten. De AI las de NMBS-site in alle 3 de runs.

## Mijn tool leest een bron

Document: de publieke NMBS-pagina over regularisatie in de trein (`build/bronnen/`).

Voor mijn tool is dit document nuttig, omdat er elke dag klantenreacties binnenstromen over klanten zonder geldig vervoersbewijs, een vergeten abonnement of een boete omdat ze niet binnen de voorziene periode betaalden.

Score: **4 op 5** (n = 5, 1 run, Opus 5.5).

Fout: B04. Een klant kreeg op 3 november een kaartje en vraagt op 18 november of hij nog kan betalen. De tool noemt de termijn van 14 kalenderdagen, maar rekent niet uit dat die tot en met 16 november liep en verstreken is. Ik denk dat het komt door mijn regel "reken de datum niet om". Die regel geldt alleen als de klant woorden als vandaag, gisteren of eergisteren gebruikt, niet voor concrete datums in de reactie. Maar dat heb ik niet expliciet in de prompt gezet. Het is één run, dus een vermoeden, geen bewijs.
