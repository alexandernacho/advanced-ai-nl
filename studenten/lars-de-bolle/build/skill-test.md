# Skilltest week 7: /offerteposten

De skill `.claude/skills/offerteposten/` is prompt v4 (`prompt.md`) als skill.
Drie inputs uit `test-set.md`, elk in een eigen sub-agent: leeg contextvenster,
alleen de skillmap, geen web.

Geschreven door Claude Code op vraag van Lars, op 25 november 2026, vóór de
eerste run. Lars kijkt na.

## De drie inputs

| ID | Waarom deze |
|---|---|
| T02 | Echt voorbeeld uit `taak.md`, en de bekende val: een post voor "de belichting" die er niet mag zijn. In week 3 maakte v2 die post twee keer (F2); v3 loste het op. |
| T11 | Echte opname, badkamer: zeven posten, een verspreking, een open product en een ontbrekende maat. |
| T12 | Echte opname, living: een transcriptiefout, en geen sloopwerk dus geen container. |

Gecorrigeerd op 26 november 2026: bij T02 stond eerst dat gpt-4o die post
maakte. Het was v2, op Claude, in week 3 (`log.md`).

## Regel om na te kijken, vastgelegd vóór de run

1. **Posten** volgen het antwoord uit `test-set.md`: dezelfde posten, aantallen,
   eenheden, prijzen en bronlabels, en geen post meer. Een geschatte of open post
   mag anders verwoord zijn.
2. **Correcties** gevuld of leeg zoals in `test-set.md`.
3. **Btw.** Geen van de drie zegt hoe oud de woning is. Volgens v4 is dan
   `tarief` null, noemt `deel` "Ouderdom van de woning", en staat er een vraag
   naar de ouderdom.
4. **Vragen** maximaal 3. Een extra vraag over een echte onbekende is juist, een
   vraag over iets dat in de opname staat is fout (regel uit `log.md`).

Een run is juist als alle vier kloppen.

## Verwacht

| ID | Posten | Correcties | Vragen |
|---|---|---|---|
| T02 | Schilderwerk 2 lagen (m2, 0, 16,50, eigen). Geen post voor de belichting. | leeg | hoeveel m2, wat er met de belichting moet, hoe oud de woning is |
| T11 | Sloopwerk badkamer (uur 13,5, eigen), Container 10 m3 puin (stuk 1, eigen), Afvoer puin en afval (forfait 1, eigen), Chape gieten 5 cm (m2 13,5, eigen), Vloertegels leggen (m2 13,5, eigen), Wandtegels leggen (m2 0, eigen), kraan (stuk 1, 0, open) | gevuld: 3 op 4 werd 3 op 4,5 | hoeveel m2 wand, hoe oud de woning is |
| T12 | Wanden bezetten (m2 30, 30, geschat), Schilderwerk 2 lagen (m2 30, eigen), Plinten plaatsen (m 22, eigen). Geen container, geen afvoer. | gevuld: gescheurd werd bezet | hoe oud de woning is |

## Runs

Model: Claude Opus 5.5, in Claude Code, in deze map. Afwijking van de werkwijze
in `README.md`: niet in een leeg venster buiten de repo, maar in een sub-agent
die alleen de skillmap mocht lezen.

| ID | Uitvoer | Juist? |
|---|---|---|
| T02 | 1 post: Schilderwerk 2 lagen (m2, 0, 16,50, eigen). Geen post voor de belichting. Btw null, `deel` "Voorwaarden > Ouderdom van de woning", citaat letterlijk uit de bron. Correcties leeg. 3 vragen: ouderdom, wat de belichting is (punt, armatuur of kring), hoeveel m2. | JUIST. Het lichtpunt van 415 euro dat v2 in week 3 twee keer verzon, komt niet. |
| T11 | 7 posten: Sloopwerk badkamer (uur 13,5, eigen), Container 10 m3 puin (stuk 1, eigen), Afvoer puin en afval (forfait 1, eigen), Chape gieten 5 cm (m2 13,5, eigen), Vloertegels leggen (m2 13,5, eigen), Wandtegels leggen (m2 0, eigen), nieuwe kraan (stuk 1, 0, open). Btw null, "Voorwaarden > Ouderdom van de woning". Correctie: 3 op 4 werd 3 op 4,5. 3 vragen: ouderdom, m2 wand, budget voor de kraan. | JUIST. De kraanvraag is een echte onbekende: de klant koos nog niet. |
| T12 | 3 posten: Wanden bezetten, 1 laag (m2 30, 30, geschat), Schilderwerk 2 lagen (m2 30, 16,50, eigen), Plinten plaatsen (m 22, 12,00, eigen). Geen container, geen afvoer. Btw null, "Voorwaarden > Ouderdom van de woning". Correctie: eerst gescheurd, daarna bezet. 2 vragen: één of twee lagen bezetten, ouderdom. | JUIST. De vraag over de lagen is een echte onbekende, dezelfde als in week 3. |

Resultaat: **3 op 3 juist** (n = 3, 1 run per input, Claude Opus 5.5, 25 november 2026).

Wat dit waard is: weinig. Drie inputs, één run, en de prompt is op deze inputs
geschreven. Wel is het de eerste keer dat v4 op Claude draait: eerder liep v4
alleen op GPT-6 Luna, op B01 tot B05. Elke sub-agent deed twee leesacties, wat
past bij de twee bestanden van de skill. Of ze `context.md` meelazen, is niet
nagekeken.

## Controle: draait de skill zelf?

Op 26 november 2026 typte Lars in een nieuwe sessie:
`/offerteposten Tegels leggen 5 op 5 meter.` Dat is T05. Verwacht volgens
`test-set.md`: `posten` leeg, en een vraag of het om vloer of wand gaat. Door
v4 ook `btw` leeg, want er zijn geen posten.

Uitvoer: `posten`, `btw` en `correcties` leeg. Twee vragen: vloer of wand (met
25 m2 juist uitgerekend), en de ouderdom van de woning. **JUIST.** De
ouderdomsvraag is extra, maar gaat over een echte onbekende.

In alle vier de runs (T02, T05, T11, T12) vraagt v4 naar de ouderdom van de
woning.

## Ruwe uitvoer

T02

```json
{
  "posten": [
    {"omschrijving": "Schilderwerk 2 lagen", "eenheid": "m2", "aantal": 0,
     "eenheidsprijs": 16.50, "bron": "eigen"}
  ],
  "btw": {"tarief": null, "deel": "Voorwaarden > Ouderdom van de woning",
          "citaat": "De woning moet ouder zijn dan 10 jaar."},
  "correcties": [],
  "vragen": ["Is de woning ouder dan 10 jaar?",
             "Gaat die belichting over nieuwe lichtpunten, armaturen ophangen of een hele kring?",
             "Hoeveel m2 moet je in die ruimte schilderen?"]
}
```

T11

```json
{
  "posten": [
    {"omschrijving": "Sloopwerk badkamer", "eenheid": "uur", "aantal": 13.5,
     "eenheidsprijs": 62.50, "bron": "eigen"},
    {"omschrijving": "Container 10 m3 puin", "eenheid": "stuk", "aantal": 1,
     "eenheidsprijs": 385.00, "bron": "eigen"},
    {"omschrijving": "Afvoer puin en afval", "eenheid": "forfait", "aantal": 1,
     "eenheidsprijs": 145.00, "bron": "eigen"},
    {"omschrijving": "Chape gieten 5 cm", "eenheid": "m2", "aantal": 13.5,
     "eenheidsprijs": 18.50, "bron": "eigen"},
    {"omschrijving": "Vloertegels leggen", "eenheid": "m2", "aantal": 13.5,
     "eenheidsprijs": 42.00, "bron": "eigen"},
    {"omschrijving": "Wandtegels leggen", "eenheid": "m2", "aantal": 0,
     "eenheidsprijs": 46.00, "bron": "eigen"},
    {"omschrijving": "Nieuwe kraan, model nog te kiezen door klant", "eenheid": "stuk", "aantal": 1,
     "eenheidsprijs": 0, "bron": "open"}
  ],
  "btw": {"tarief": null, "deel": "Voorwaarden > Ouderdom van de woning",
          "citaat": "De woning moet ouder zijn dan 10 jaar."},
  "correcties": ["Je zei eerst 3 op 4 en daarna 3 op 4,5; ik reken met 3 op 4,5, dus 13,5 m2 voor sloop, chape en vloertegels."],
  "vragen": ["Is de woning ouder dan 10 jaar?",
             "Hoeveel m2 wand moet er getegeld worden?",
             "Welk budget reken ik voor de kraan zolang de klant niet gekozen heeft?"]
}
```

T12

```json
{
  "posten": [
    {"omschrijving": "Wanden bezetten, 1 laag", "eenheid": "m2", "aantal": 30,
     "eenheidsprijs": 30, "bron": "geschat"},
    {"omschrijving": "Schilderwerk 2 lagen", "eenheid": "m2", "aantal": 30,
     "eenheidsprijs": 16.50, "bron": "eigen"},
    {"omschrijving": "Plinten plaatsen", "eenheid": "m", "aantal": 22,
     "eenheidsprijs": 12.00, "bron": "eigen"}
  ],
  "btw": {"tarief": null, "deel": "Voorwaarden > Ouderdom van de woning",
          "citaat": "De woning moet ouder zijn dan 10 jaar."},
  "correcties": ["Je zei eerst dat de muren gescheurd moeten worden en daarna bezet; ik reken met bezetten."],
  "vragen": ["Bezet je de muren in één laag of in twee lagen met afwerking?",
             "Is de woning ouder dan 10 jaar?"]
}
```

T05, door Lars in een nieuwe sessie

```json
{
  "posten": [],
  "btw": {"tarief": null, "deel": "", "citaat": ""},
  "correcties": [],
  "vragen": [
    "Zijn die tegels van 5 op 5 meter (25 m2) voor de vloer of voor de wand?",
    "Is de woning ouder dan 10 jaar?"
  ]
}
```
