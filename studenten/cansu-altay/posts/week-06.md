# Week 6 — Welke fitnessapps vindt AI?

## Mijn Live Query

Ik stelde in alle drie de rondes dezelfde vraag: “Welke apps kan ik gebruiken om tijdens het fitnessen snel te zien hoeveel gewicht, sets en herhalingen ik de vorige keer deed per oefening?”

| Run | Zichtbare zoekactiviteit | Brondomeinen die ik noteerde | Genoemde apps |
|---|---|---|---|
| ChatGPT 1 | Niet genoteerd | www.hevyapp.com, help.fitbod.me, help.hevyapp.com, assets-global.website-files.com, fitbod.me, s3.amazonaws.com, play.google.com, greypatterson.me, recipp.ipp.pt, riunet.upv.es, www.reddit.com, www.thenerdystudent.com | Hevy, Strong, Fitbod |
| ChatGPT 2 | “Vergelijken van workouttrackers en trainingsgeschiedenis” | www.hevyapp.com, help.hevyapp.com, www.strong.app, help.strongapp.io, www.fitnotesapp.com | Hevy, Strong, FitNotes |
| Google AI-modus | Niet genoteerd | Niet genoteerd | Hevy, Strong, FitNotes, StrengthLog, JEFIT |

Voor de twee ChatGPT-runs heb ik de domeinen uit het bronnenpaneel bewaard. De links naar de specifieke bronpagina’s heb ik niet genoteerd.

- **Zou een kenner dezelfde apps noemen?** Hevy zou ik zelf gebruiken. Ik heb de app opgezocht en zag dat die veel reviews en gebruikers heeft. Over de andere apps kan ik moeilijk oordelen, omdat ik ze niet heb gebruikt of opgezocht.
- **Wie ontbreekt?** GymRun. Ik vond dat de app eerdere trainingsgegevens automatisch kan invullen op Android.
- **Dezelfde apps in run 2 en Google?** Google noemde dezelfde drie apps en voegde StrengthLog en JEFIT toe.

Hevy werd mogelijk wel genoemd omdat de app meer reviews heeft, op de eigen website duidelijk uitlegt hoe je vorige trainingsgegevens terugvindt en in app-overzichten zoals BarBend en TechRadar voorkomt, terwijl ik voor GymRun minder zichtbare vermeldingen vond.

## Kan AI GymRun vinden?

| Criterium | Score | Mijn bewijs |
|---|---:|---|
| Gestructureerde data | 1/3 | Op `https://www.gymrun.app/startpage` vond de Schema Markup Validator het type `WebPage` met de naam GymRun Tour en één fout bij `imageUrl`. |
| Leesbaar voor AI | 1/3 | De intro noemt de app een trainingsdagboek. De eerste uitleg over het gebruik staat vooral in afbeeldingen. |
| Vermeldingen door anderen | 1/3 | Ik zag ongeveer 17.300 reviews op Google Play. Andere kanalen heb ik voor dit criterium niet apart gecontroleerd. |
| Genoemd in AI-antwoorden | 0/3 | GymRun verscheen in geen van mijn drie zoekrondes. |
| Autoriteit | 2/3 | Google Play vermeldt GymRun Team als ontwikkelaar, meer dan 1 miljoen downloads en een score van 4,5/5. |
| Zoeken op de merknaam | 3/3 | Bij mijn zoekopdracht naar GymRun stond GymRun Tour bovenaan. De FAQ van dezelfde site stond op de derde plaats. |

**Totaal: 8/18.** Ik zou bovenaan GymRun Tour een korte inleiding in tekst zetten. Daarin zou ik meteen uitleggen dat je met de app per oefening je vorige gewicht, sets en herhalingen kunt terugvinden.

## Mijn tool leest een bron

Ik koos de [Fitnessgids Oefeningen en Techniek](../build/bronnen/Fitnessgids_Oefeningen_en_Techniek.txt), omdat die uitleg geeft over oefeningen en techniek. Ik beoordeelde vijf vragen en gaf **5 op 5**. Bij B05 gaf de tool aan dat de gids geen exacte rusttijd per oefening vermeldt. Bij B02 noemde de tool de bovenkant van de borst als bestemming van de stang. Ik vond dat voldoende voor de vraag, ook al liet de tool de extra techniekdetails uit mijn verwachte antwoord weg. [Mijn brontest](../build/test-set-bron.md)
