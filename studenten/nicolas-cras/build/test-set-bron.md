# Testset bron (B01–B05)

**Bron:** `build/bronnen/weekschemas-hybride-atleet.md`
**Prompt:** `build/prompt-bron.md` (v8)

Het juiste antwoord, en waar het in het document staat, schrijf je vóór de eerste run.
B01–B04: het document geeft het antwoord. B05: het document geeft het antwoord níet.

Regel voor het verwachte nummer: laatst gebruikt in die categorie + 1. Na week 50 weer 01.

| ID | Vraag | Juiste antwoord | Waar in het document | Run 1 | Juist? |
|---|---|---|---|---|---|
| B01 | zie hieronder | Categorie 1, week 08 | `CATEGORIE 1 • Week 08` | 1 Herstelweek, Cat 1 week 08 (Belasting zwaar, Herstel onvoldoende). Bron: CATEGORIE 1 • Week 08. Volledig: `runs/bron-run1.md` | juist |
| B02 | zie hieronder | Categorie 2, week 12 | `CATEGORIE 2 • Week 12` | 2 Consolidatieweek, Cat 2 week 12 (Belasting zwaar, Herstel voldoende). Bron: CATEGORIE 2 • Week 12. Volledig: `runs/bron-run1.md` | juist |
| B03 | zie hieronder | Categorie 3, week 05 | `CATEGORIE 3 • Week 05` | 3 Progressieweek, Cat 3 week 05 (Belasting normaal, Herstel voldoende). Bron: CATEGORIE 3 • Week 05. Volledig: `runs/bron-run1.md` | juist |
| B04 | zie hieronder | Categorie 3, week 01 | `CATEGORIE 3 • Week 01` | 3 Progressieweek, Cat 3 week 01 (Belasting normaal, Herstel voldoende). Bron: CATEGORIE 3 • Week 01. Volledig: `runs/bron-run1.md` | juist |
| B05 | zie hieronder | `staat niet in het document` | — | Staat niet in het document. Noemt alleen de algemene regel over voeding. Volledig: `runs/bron-run1.md` | juist |

Resultaat: **5 op 5 juist** (n = 5, 1 run, model: Claude Sonnet 5.5 (`claude-sonnet-5-5`), prompt-bron v8, elke run een nieuwe sessie)

---

## De invoer per geval

Elke invoer heeft drie regels voor de tool: Doel, Notities en Laatst gebruikt.
Notities komen uit `build/inputs/tNN.txt`. Kopieer de tekst hieronder.

Tip om een geval te kiezen (uit je week-5 testset, `test-set.md`):
- Herstel onvoldoende: T06, T07
- Zwaar + voldoende: T01, T09
- Normaal + voldoende: T03

### B01 — onvoldoende herstel, Herstelweek (categorie 1)
- Gekozen input: T06
- Doel: spiermassa opbouwen
- Notities:
  ```
  maandag: zware upperbody, dinsdag: lower body, woensdag: rustdag, donderdag: fullbody, vrijdag: fietstraining geschrapt, te veel spierpijn in de benen, zaterdag: korte loop, zondag: zware fullbody
  ```
- Laatst gebruikt: Cat 1 week 07, Cat 2 week 10, Cat 3 week 3
- Verwacht: Categorie 1, week 08

### B02 — zwaar + voldoende, Consolidatieweek (categorie 2)
- Gekozen input: T01
- Doel: aerobe basis
- Notities:
  ```
  Doel: Aerobe basis en duurvermogen opbouwen, terwijl spiermassa behouden blijft.
  Maandag – Zwemmen: Rustige techniektraining met veel aandacht voor efficiënte ademhaling. Voelde gecontroleerd, maar niet bijzonder sterk.
  Dinsdag – Kracht: Full-body krachttraining met squats, pull-ups en presses. Goede training, voelde sterk en energiek.
  Woensdag – Fietsen: Lange zone-2 rit. Eerste helft soepel, laatste uur zwaar maar goed volgehouden.
  Donderdag – Hardlopen: Korte rustige run. Benen waren vermoeid van de fiets, dus tempo bewust laag gehouden.
  Vrijdag – Rust: Volledige rustdag om vermoeidheid weg te werken.
  Zaterdag – Fietsen + lopen: Lange bike gevolgd door korte brick run. Zwaar, maar sterke overgang naar het lopen.
  Zondag – Zwemmen: Lange rustige sessie met constante tempo's. Technisch een van de betere trainingen van de week.
  ```
- Laatst gebruikt: Cat 1 week 07, Cat 2 week 11, Cat 3 week 3
- Verwacht: Categorie 2, week 12

### B03 — normaal + voldoende, Progressieweek (categorie 3)
- Gekozen input: T03
- Doel: spiermassa opbouwen
- Notities:
  ```
  Doel: Lean blijven maar extra spiermassa opbouwen, zonder conditie te verliezen.
  Maandag – Kracht: Push-training met borst, schouders en triceps. Zeer sterke sessie met progressie op meerdere oefeningen.
  Dinsdag – Hardlopen: Easy run van ongeveer 40 minuten. Licht en ontspannen, vooral bedoeld om conditie te onderhouden.
  Woensdag – Kracht: Pull-training met rug en biceps. Goede volume-training, spieren waren volledig vermoeid.
  Donderdag – Zwemmen: Technische zwemtraining met korte intervallen. Niet geweldig gevoel, maar wel netjes afgewerkt.
  Vrijdag – Kracht: Benen en core. Zware squats en lunges; laatste sets waren duidelijk pittig.
  Zaterdag – Fietsen: Lange rustige rit. Goed hersteltempo en relatief lage intensiteit.
  Zondag – Rust: Volledige rust en extra aandacht voor voeding en herstel.
  ```
- Laatst gebruikt: Cat 1 week 07, Cat 2 week 11, Cat 3 week 4
- Verwacht: Categorie 3, week 05

### B04 — normaal + voldoende, categorie 3 (wat test dit geval anders dan B03?)
- Gekozen input: T03
- Doel: spiermassa opbouwen
- Notities:
  ```
  Doel: Lean blijven maar extra spiermassa opbouwen, zonder conditie te verliezen.
  Maandag – Kracht: Push-training met borst, schouders en triceps. Zeer sterke sessie met progressie op meerdere oefeningen.
  Dinsdag – Hardlopen: Easy run van ongeveer 40 minuten. Licht en ontspannen, vooral bedoeld om conditie te onderhouden.
  Woensdag – Kracht: Pull-training met rug en biceps. Goede volume-training, spieren waren volledig vermoeid.
  Donderdag – Zwemmen: Technische zwemtraining met korte intervallen. Niet geweldig gevoel, maar wel netjes afgewerkt.
  Vrijdag – Kracht: Benen en core. Zware squats en lunges; laatste sets waren duidelijk pittig.
  Zaterdag – Fietsen: Lange rustige rit. Goed hersteltempo en relatief lage intensiteit.
  Zondag – Rust: Volledige rust en extra aandacht voor voeding en herstel.
  ```
- Laatst gebruikt: Cat 1 week 07, Cat 2 week 11, Cat 3 week 50
- Verwacht: Categorie 3, week 01
- Wat dit test: doorrollen. Cat 3 week 50 was het laatst gebruikt, dus de tool moet weer bij week 01 beginnen.

### B05 — het document geeft geen antwoord
- Vraag aan de tool: Geef mij een voedingsschema voor de komende week.
- Verwacht: `staat niet in het document`
- Waarom staat het er niet in: het document bevat trainingsschema's. Over voeding staat alleen één algemene regel (koolhydraatinname bij sessies langer dan 75–90 minuten) en "oefen drinken/voeding", geen voedingsschema.

---

## Nakijken (invullen na de runs)
Per geval: juist of fout. Komt het schema letterlijk uit het document? Klopt het nummer?
