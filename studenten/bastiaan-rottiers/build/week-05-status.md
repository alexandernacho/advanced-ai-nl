# Week 5: stand van zaken

**Afronding week 5:** set v2 (T01–T20) is eenmaal uitgevoerd met v7, GPT-6.1 Sol medium: **10 op 20 (set v2, 1 run; n = 20)**. De correcties van T08 en T11 staan openlijk in `build/log.md`. De post telt 474 woorden exclusief citaten en bevat zes koppen, de score en Bastiaans reflectie op T19. Commit `cda1d1c` staat op `origin/week-05`; bestaande PR #122 is bijgewerkt en staat open. De publieke branchdashboardlink is gecontroleerd: HTTP 200, set-v2-kaart en score 10/20 zichtbaar. Canvas-indiening van de PR-link is nog niet bevestigd.

## Klaar

- Week 4 ingediend via pull request #121; automatische check geslaagd.
- Lesmateriaal opgehaald en branch week-05 gemaakt.
- Bestaande week-4-prompt, testset en kosten behouden.
- Foutmargetest: 30 afzonderlijke antwoorden, Sol medium, T06–T10, drie rondes per versie. v6 is gereconstrueerd; de beperking staat bij de scores.
- Eigen controle van T07 en T10 genoteerd; daarna is alleen het aantoonbaar foutieve T08-antwoord openlijk gecorrigeerd en gelogd.
- Modeltest: vijftien nieuwe antwoorden; Sol 4/5, Luna 2/5, Astra 4/5. Gok vooraf vastgelegd. Eigen keuze achteraf: Sol medium.
- Nieuwe tokenmeting en API-equivalente kosten, met behoud van de oude raming. Haiku-correctie niet van toepassing.
- Waardeketen met herstelduur, scorebereik en gevoeligheid voor de handwerktijd. €20 eigen tijdwaarde en een apart hypothetisch werkgeversscenario van €30.
- De branchdashboardlink in de post is opgehaald zonder login (HTTP 200); set-v2-kaart en score 10/20 zijn zichtbaar.
- Post bijgewerkt: zes koppen, vijf letterlijke citaten met feitelijke herschrijvingen en een reflectie op T19; 481 woorden exclusief citaten.
- Tijdschattingen per stap verwerkt: lezen 5–10 min, begrijpen/zoeken 20–25 min, plannen minstens 5 min; met 5 min plannen is de rekenmiddenwaarde 35 min. De tooltijd vóór herstel is nu 5 min verwerken + 3 min nakijken = 8 min.
- Publieke dashboardlink zelf in een privévenster geopend: na de tussenpagina opent het dashboard zonder inloggen.

## Indiening

- Week 5 is ingediend en bijgewerkt via [pull request #122: week-05 — Bastiaan Rottiers](https://github.com/alexandernacho/advanced-ai-nl/pull/122); de branch staat op commit `cda1d1c`.
- De automatische controle is te volgen op het tabblad Checks van de pull request. De docent beoordeelt en merget de indiening.

## Meetbeperkingen voor de verdere Build

- T08 heeft een tegenstrijdigheid tussen input en verwacht antwoord. Alleen vóór een volgende reeks corrigeren en vastleggen; oude runs niet herlabelen.
- De tijden per werkstap zijn nu geschat, maar nog niet met een chronometer gemeten. De werkelijke herstelduur is nog niet gemeten.
- De huidige meting bevestigt geen prestaties op nieuwe taken rond financieel plan en marktonderzoek. Daarvoor zijn nieuwe eigen praktijkinputs en vooraf vastgelegde antwoorden nodig.
- Voor de eventuele blinde klasgenotencontrole is nog geen resultaat beschikbaar.
