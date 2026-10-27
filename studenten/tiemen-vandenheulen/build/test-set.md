# Testset — Review-sorteerder voor evenementen

**Set v2: T01–T30, 27 oktober 2026.** T01–T10 zijn ongewijzigd gebleven. T11–T30 zijn vooraf van een verwacht antwoord voorzien, vóór ze op de tool draaien.

Schrijf het juiste antwoord en waarom **vóór** je de tool test. De antwoorden zijn van de student, niet van de AI.

| Nr. | Review | Juiste labels | Waarom? | Run 1 | Foutklasse | Run 2 | Foutklasse |
|---|---|---|---|---|---|---|---|
| 1 | Leuke sfeer en alles was goed geregeld. We hebben ons de hele avond prima vermaakt. | organisatie, sfeer | De review zegt dat alles goed geregeld was en benoemt expliciet de leuke sfeer. | organisatie, sfeer — juist |  |  |  |
| 2 | Fijn evenement met een goede mix van activiteiten. De wachtrij bij de ingang duurde wel even. | organisatie, wachttijden | Organisatie omdat er een goede mix was van activiteiten, en wachttijden omdat de wachtrij aan de ingang even duurde. | organisatie, wachttijden — juist |  |  |  |
| 3 | Gezellige dag gehad! Vooral de optredens maakten het voor mij de moeite waard. | sfeer | De bezoeker zegt dat het gezellig was. |  |  |  |  |
| 4 | Goed georganiseerd en vriendelijk personeel. Ik kom volgend jaar graag weer. | organisatie | De review zegt dat het goed georganiseerd is en noemt het personeel. |  |  |  |  |
| 5 | Leuke locatie en genoeg te doen. Het was op sommige momenten wel erg druk. | locatie | De bezoeker noemt de locatie expliciet leuk. Drukte krijgt in deze v1 geen apart label. |  |  |  |  |
| 6 | Het was… anders dan verwacht. | andere | De review is te vaag: ik weet niet waarom het anders was dan verwacht of wat de verwachtingen waren. |  |  |  |  |
| 7 | Top. | andere | Het is niet duidelijk wat de bezoeker precies goed vond. |  |  |  |  |
| 8 | Really nice atmosphere, but the sound could have been better. | sfeer | “Nice atmosphere” wijst op sfeer. Geluid heeft in deze v1 geen aparte categorie. | sfeer, andere — fout | `andere` onterecht toegevoegd | sfeer — juist |  |
| 9 | De stoelen waren blauw. | andere | Het is geen echte beoordeling en noemt geen thema uit de categorieën. |  |  |  |  |
| 10 | Tijdens het evenement bedacht ik dat ik thuis nog de was in de machine had zitten. | andere | Het is geen beoordeling en noemt geen categorie uit de tool. |  |  |  |  |  |

| 11 | De ingang ging open zoals aangekondigd en de vrijwilligers wezen ons meteen naar de juiste camping. | organisatie | De opening en de hulp van vrijwilligers gaan over de organisatie van het evenement. |  |  |  |  |
| 12 | Voor een kleine friet betaalde ik bijna evenveel als voor mijn lunch buiten het terrein. | prijs, catering | De review beoordeelt zowel de prijs als eten; eten hoort bij catering. |  |  |  |  |
| 13 | Het festivalterrein lag mooi tussen de bomen, maar was vanaf het station lastig te voet te bereiken. | locatie | De bereikbaarheid vanaf het station en de ligging gaan over de locatie. |  |  |  |  |
| 14 | De vegetarische curry was lekker en er was ook genoeg keuze zonder vlees. | catering | Het gaat over het eten en het aanbod. |  |  |  |  |
| 15 | Toen de band begon te spelen, zong het hele plein mee. Dat maakte de avond bijzonder gezellig. | sfeer | De gedeelde beleving en gezelligheid wijzen op sfeer. |  |  |  |  |
| 16 | Voor een drankje moesten we ruim twintig minuten aanschuiven aan de bar. | wachttijden | De review noemt een lange wachttijd aan de bar. |  |  |  |  |
| 17 | Bij de uitgang hielp de beveiliging iedereen rustig naar buiten toen het terrein vol liep. | veiligheid | De beveiliging regelde een veilige uitstroom. |  |  |  |  |
| 18 | Het optreden begon een uur te laat omdat het programma niet goed op elkaar was afgestemd. | organisatie | Een slecht afgestemd programma is een organisatieprobleem. |  |  |  |  |
| 19 | De broodjes waren vers, maar tegen de avond was de vegetarische optie al op. | catering | De review gaat over eten en de beschikbaarheid van het aanbod. |  |  |  |  |
| 20 | De tickets waren betaalbaar, maar voor een kluisje moest je nog flink bijbetalen. | prijs | Zowel tickets als het kluisje gaan over kosten. |  |  |  |  |
| 21 | De artiesten zorgden voor een geweldige sfeer, maar bij de toiletten stond een lange rij. | sfeer, wachttijden | De review noemt zowel sfeer als een wachtrij. |  |  |  |  |
| 22 | Het eten was goed; alleen het bestellen en afhalen duurde erg lang. | catering, wachttijden | Het gaat over eten en een lange wachttijd bij bestelling en afhaling. |  |  |  |  |
| 23 | De parkeerplaats was slecht aangegeven, waardoor we eerst aan de verkeerde kant van het terrein aankwamen. | locatie | De wegwijzing naar de parkeerplaats hoort bij de bereikbaarheid van de locatie. |  |  |  |  |
| 24 | De rij aan de ingang was lang, maar de beveiligers controleerden iedereen rustig en zorgvuldig. | wachttijden, veiligheid | De review noemt zowel een wachtrij als de veiligheidscontrole. |  |  |  |  |
| 25 | Het kluisje werkte prima, maar twintig euro vond ik te duur voor één dag. | prijs | De review beoordeelt de prijs van het kluisje. |  |  |  |  |
| 26 | Een nooduitgang was geblokkeerd; een medewerker maakte die meteen vrij en waarschuwde de beveiliging. | organisatie, veiligheid | De nooduitgang en beveiliging gaan over veiligheid; de medewerker hoort bij organisatie. |  |  |  |  |
| 27 | Het was nogal wat. | andere | De review is te vaag om een thema te kiezen. |  |  |  |  |
| 28 | Dat liep anders dan gedacht. | andere | De review is te vaag om een thema te kiezen. |  |  |  |  |
| 29 | Ik weet nog steeds niet goed wat ik ervan moet vinden. | andere | De review is te vaag om een thema te kiezen. |  |  |  |  |
| 30 | Er was iets met dat ene onderdeel, maar goed. | andere | De review is te vaag om een thema te kiezen. |  |  |  |  |

**Bron T11–T20:** eigen ervaringen op de festivals Modul'air, Sweet Seduction en Bambata.

## Resultaat

_Getest: review 2 was juist in v1. Review 8 was fout in v1 en juist na de aanpassing in v2._

## V2-test — 20 oktober 2026

| Nr. | Uitkomst v2 | Beoordeling | Foutklasse |
|---|---|---|---|
| 1 | `organisatie, sfeer` | juist | |
| 2 | `organisatie, sfeer, wachttijden` | fout: extra `sfeer` | F1 |
| 3 | `sfeer` | juist | |
| 4 | `organisatie` | juist | |
| 5 | `organisatie, locatie` | fout: extra `organisatie` | F1 |
| 6 | `andere` | juist | |
| 7 | `andere` | juist | |
| 8 | `sfeer` | juist | |
| 9 | `andere` | juist | |
| 10 | `andere` | juist | |

**Resultaat v2: 8 op 10 juist (n = 10, 1 run).** De twee F1-fouten zijn extra labels bij dubbelzinnige reviews.

## Set v2 — run 1, 27 oktober 2026

- **Model:** GPT-6.1 Sol via `codex exec`, hoog redeneerniveau.
- **Oorspronkelijke beoordeling:** 25 op 30 juist. T12 en T26 zijn daarna openlijk gecorrigeerd in het log, omdat hun vooraf gekozen antwoorden niet volledig waren.
- **Score na die inhoudelijke correcties:** **27 op 30 juist (set v2, n = 30, 1 run).**
- **Fouten:** drie F1-fouten: het model voegde één extra label toe bij T05 (`organisatie`), T16 (`catering`) en T25 (`locatie`).

| Nr. | Verwacht | Gekregen | Beoordeling |
|---:|---|---|---|
| 5 | `locatie` | `locatie, organisatie` | fout: extra `organisatie` (F1) |
| 16 | `wachttijden` | `wachttijden, catering` | fout: extra `catering` (F1) |
| 25 | `prijs` | `prijs, locatie` | fout: extra `locatie` (F1) |
