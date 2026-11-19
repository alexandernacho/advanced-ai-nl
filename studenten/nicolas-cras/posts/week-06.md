# Week 6: Live query

## Mijn live query

**De vraag (letterlijk):** Waar vind ik een sportcoach met wekelijkse analyses rond Gent?

| | Eigen AI, run 1 | Eigen AI, run 2 | Google AI-modus |
|---|---|---|---|
| Welke AI / tool | Claude | Claude | Google AI-modus |
| Zoekopdrachten van de AI | Sportcoach Gent persoonlijke coaching wekelijkse opvolging analyse<br>Hyrox running coach Gen training schema wekelijkse feedback<br>Online personal trainer Oost-Vlaanderen wekelijkse check-in analyse feedback | Personal coach Gent wekelijkse opvolging analyse training coaching<br>Hardloopcoach triatloncoach Gent wekelijkse analyse trainingschema | waar vindt ik een sportcoach met wekelijkse analyses rond Gent? |
| Pagina's die de AI las (eigen site · vergelijkingssite · review · forum · pers) | Zoekresultatenlijsten uit 3 screenshots (domeinen):<br>• TrainingPeaks (trainingsplannen en coachprofielen, o.a. Bart De Temmerman, Simon Van Roy, Evert De Jaeghere, Mathias Lefeber)<br>• Marktplaatsen/platformen: Fiverr, Apprentus, TrainHeroic, Fresha, Payhip<br>• Vergelijking/software: Capterra, Virtuagym, myPTHub, Coachway<br>• Eigen sites: Golazo (energyshop.golazo.com), Basic-Fit, 3Lab (Substack), TLW coaching (formulier)<br>• Overig: stad.gent, vdab.be, publicaties.vlaanderen.be, Red Bull, Decathlon, Eventbrite, tally.so, Weight Watchers, fitsociety.nl<br><br>**Echt aangehaald in het antwoord (bronlabels):** TrainingPeaks (Bart De Temmerman en All In Gent), Golazo, Substack (3Lab), Basic-Fit, Intercom (Hyrox-coaching), Decathlon (prijs) | Zoekresultatenlijsten uit 2 screenshots (domeinen):<br>• TrainingPeaks (triatlon-schema's, Bart De Temmerman, Evert De Jaeghere)<br>• Eigen sites: Golazo (energyshop.golazo.com, energy.golazo.com)<br>• Marktplaatsen/platformen: Fiverr, Apprentus, Fresha, Doctena, Bsearch<br>• Overig: stad.gent, vdab.be, vlaanderen.be, tally.so, gortcoaching.nl, learnit.nl, download.boekhuis.nl<br><br>**Echt aangehaald in het antwoord (bronlabels):** TrainingPeaks (All In Gent en Bart De Temmerman), Golazo (2×) | Bronnen in het antwoord (1 screenshot):<br>• All In Gent (+1)<br>• sportartsdegendt.be<br>• deloopcoach.be<br>• Uplevel Performance<br>• Kaart met Sportschuur, Connect Personal Training, sportarts de decker (Google Maps) |
| Genoemde bedrijven | All-in Gent<br>Bart De Temmerman<br>Golazo Energy<br>3Lab<br>Basic-Fit Online coach | All-in Gent<br>Bart De Temmerman<br>Golazo Energy | All-in Gent<br>Sportarts Ruben De Gendt<br>De Loopcoach<br>Uplevel Performance<br>Sportschuur<br>ConnectPT |
| Zou een kenner dezelfde noemen? | ja | ja | ja, maar ze zijn wel heel specifiek |

- **Wie had er moeten staan?** Level-up sportcoaching (ontbrak in alle drie de runs)
- **Run 2 en Google: dezelfde bedrijven?** Niet helemaal: beide noemen All-in Gent. Alleen run 2 noemt Bart De Temmerman en Golazo Energy. Alleen Google noemt Sportarts Ruben De Gendt, De Loopcoach, Uplevel Performance, Sportschuur en ConnectPT.

**Waarom staat het ene bedrijf er wel, en het andere niet?**
Golazo Energy heeft minder en slechtere reviews maar ligt echt in Gent, terwijl Level-up sport coaching veel meer en betere reviews heeft maar verder van Gent ligt dan Golazo Energy, waardoor die niet wordt genoemd door de AI-modellen.

## Kan AI dit bedrijf vinden?

Bedrijf: Level UP Sportcoaching (https://levelupsportcoaching.be)

| # | Criterium | Score | Bewijs |
|---|---|---|---|
| 1 | Gestructureerde data | 1/3 | https://levelupsportcoaching.be/extra-diensten/personal-training: geen gestructureerde data gevonden. De homepage toont alleen `Organization` en `WebSite`. Reviews en openingsuren staan wel zichtbaar of op Google, maar niet als data op de dienstpagina. |
| 2 | Leesbaar voor AI | 2/3 | Diensten en team staan duidelijk op de site, maar er staat geen adres of Gent op de dienstpagina en niets over "wekelijkse analyse". |
| 3 | Vermeldingen door anderen | 1/3 | Het bedrijf wordt niet vermeld door anderen, maar heeft wel veel Google-reviews. |
| 4 | Echt genoemd in AI-antwoorden | 0/3 | Niet genoemd in 0 van 3 runs van mijn live query. |
| 5 | Autoriteit | 1/3 | Teampagina met vier coaches, maar geen diploma's, certificaten of resultaten vermeld. |
| 6 | Zoeken op merknaam | 3/3 | Zoek ik de naam zelf in Google, dan staat Level UP bovenaan. |

**Totaal: 8/18 (marginaal).**

**Eén tactiek:** Gent en het adres op de dienstpagina zetten, zodat AI-systemen het bedrijf sneller koppelen aan de vraag "rond Gent".

## Mijn tool leest een bron

**Document:** 150 weekschema's voor de hybride atleet (`build/bronnen/weekschemas-hybride-atleet.md`). Ik koos dit omdat het praktisch is en er nog iets extra automatiseert: de coach hoeft niet telkens een nieuwe training te verzinnen.

**Wat de tool doet:** hij bekijkt de vorige week, analyseert de belasting en het herstel, en kiest op basis daarvan een categorie van trainingen. Hij zegt erbij uit welk deel van het document het schema komt, en zegt het als het document het antwoord niet bevat.

**Score: 5 op 5** (B01–B05, n = 5, 1 run per geval, elke run een nieuwe sessie, Claude Sonnet 5.5).

**Eerlijk punt:** er ging geen geval fout. De test was waarschijnlijk te makkelijk.

## Wat nog openstond uit week 5

Mijn week-5-post ging alleen over prompt v5 op T01–T10. Daarna heb ik nog extra inputs gemaakt (T11–T40) en de prompt verbeterd tot v6 en v7. Op T11–T30 scoorde v7 20 op 20, maar dat bewijst weinig: ik had de verwachte antwoorden aangepast nadat ik de output had gezien. De eerlijke test is T31–T40, nieuwe inputs (vage weken en weken in het Frans, Spaans, Duits, Italiaans en Portugees) die ik vooraf niet had gezien. Daar scoorde v7 **5–6 op 10** (Opus 5.5, 3 runs, `build/v7-eerlijke-test.md`). De meeste fouten zijn de Belasting die als "onzeker" wordt beoordeeld terwijl ik "zwaar" verwachtte, vooral bij de buitenlandse talen.
