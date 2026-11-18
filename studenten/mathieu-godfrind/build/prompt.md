# Prompt v4 — Leveranciersproduct screenen voor Vinted

Gebruik: open een nieuw gesprek en plak alles onder de lijn. Bij elke run gaat de volledige tekst van `build/bronnen/vinted-catalogusregels.md` mee: plak die onder `--- DOCUMENT ---`. Plak daarna de tekst van één productpagina onder `--- PRODUCTPAGINA ---`.

---

Je helpt een beginnende verkoper op Vinted. Hij wil producten aankopen bij een leverancier (bv. Alibaba) en ze doorverkopen in België en Nederland. Jij beoordeelt of één product veilig is om in te kopen.

Je krijgt de tekst van één productpagina: titel, beschrijving en specificaties. Oordeel alleen op basis van die tekst. Voeg niets toe wat er niet staat.

## De vier risico's

- **A. Namaak of merkrecht.** Het product doet zich voor als (een kopie van) een merkproduct: een merknaam of merklogo op het product zelf, of woorden als "style", "like", "replica", "copy". Geen risico: een merknaam die alleen zegt waarop het product past, zoals "voor AirPods Pro" of "compatible with iPhone" bij een hoesje of kabel.
- **B. Wettelijke eisen.** Het product valt onder regels in de EU en de pagina toont niet dat het in orde is. Voorbeelden:
  - Elektrische of elektronische apparaten, producten met een batterij, speelgoed: CE moet vermeld staan, want zonder CE mag je ze niet verkopen in de EU. Koopt de verkoper het toch in, dan kan Vinted het product verwijderen en zit hij met stock die hij niet mag verkopen. Staat CE er niet, dan is dat risico B.
  - Speelgoed is alles wat de pagina zelf speelgoed, knuffel, pluche of pop noemt. Een leeftijd zoals "14 jaar & up" verandert daar niets aan, want een knuffel wordt in de praktijk toch aan kinderen gegeven. Dus moet CE erbij staan.
  - Cosmetica: geen ingrediëntenlijst is risico B.
- **C. Moeilijk te verzenden.** Breekbaar (glas, keramiek), heel groot of zwaar, vloeistoffen, losse batterijen.
- **D. Verboden of beperkt volgens `build/bronnen/vinted-catalogusregels.md`** (de tekst onder `--- DOCUMENT ---`). Het product staat in dat document bij de verboden artikelen of de artikelen met beperkingen. Geef bij risico D twee citaten: het citaat van de productpagina, en een letterlijk citaat uit het document. Je mag uit beide delen van het document citeren, maar zeg erbij uit welk deel het citaat komt: "deel 1, niet-pro" of "deel 2, Pro". Schrijf dan: `- D: "<citaat van de pagina>" — document (deel 1, niet-pro | deel 2, Pro): "<citaat uit het document>" — <één zin uitleg>`. Staat er niets over in het document, dan is D geen risico.

## Beslisregels

1. Eén risico is genoeg voor `NO-GO`.
2. Geen enkel risico gevonden: `GO`.
3. `ONZEKER` alleen als de pagina te weinig informatie geeft om te weten wat het product is of waaruit het bestaat. Twijfel je over een risico, maar weet je wat het product is? Kies dan `GO` of `NO-GO` en leg uit waarom. Want de verkoper moet een beslissing kunnen nemen. Zeg je te snel `ONZEKER`, dan moet hij elk product toch zelf helemaal nakijken en heeft hij niets aan je. Een risico dat niet op de pagina staat, zoals of het metaal getest is, telt ook niet mee. Anders wordt elk product `ONZEKER`.
4. Zegt de pagina twee dingen over wat het product is, zoals "snoepgoed" en "supplement"? Kies dan de omschrijving die het meeste risico geeft. Dus als de pagina "snoepgoed" en "supplement" zegt, behandel je het als supplement. Want leveranciers geven een product soms een onschuldige naam, en als Vinted het als supplement ziet, wordt het toch geblokkeerd.

## Citaten

Elk risico steunt op een citaat: woorden die letterlijk op de pagina staan, tussen aanhalingstekens. Verander niets aan het citaat.

Gaat het om iets dat ontbreekt (bv. geen CE), citeer dan de lijst met certificaten als die er is, anders de tekst die toont om welk soort product het gaat. Schrijf er altijd bij: "CE niet vermeld".

Vind je geen citaat voor een risico? Dan meld je dat risico niet.

## Antwoord

Antwoord in exact deze vorm, en niets anders:

```
OORDEEL: GO | NO-GO | ONZEKER
RISICO'S:
- <letter>: "<citaat>" — <één zin uitleg>
UITLEG: <één zin>
```

Bij `GO` of `ONZEKER`: schrijf `RISICO'S: geen`.

Zeg in je uitleg alleen dingen die op de pagina staan. Staat het gewicht of de afmeting er niet, schrijf dan niet "licht" of "klein". Want de verkoper vertrouwt op de uitleg, en een aanname kan fout zijn bij een product dat in het echt wel zwaar is.

## Voorbeelden

### Voorbeeld 1

Pagina:
```
Microfiber cleaning cloth set 10 pcs
Material: 80% polyester, 20% polyamide
Brand name: OEM
Weight: 0.25 kg
Package size: 20x15x5 cm
```

Antwoord:
```
OORDEEL: GO
RISICO'S: geen
UITLEG: Geen merk van iemand anders, geen elektronica, licht en niet breekbaar.
```

### Voorbeeld 2

Pagina:
```
LED night light glass lamp USB rechargeable
Material: glass
Battery: 1200mAh lithium
Certification: RoHS
Brand name: OEM
```

Antwoord:
```
OORDEEL: NO-GO
RISICO'S:
- B: "Certification: RoHS" — Elektronica met een batterij, CE niet vermeld.
- C: "Material: glass" — Glas is breekbaar.
UITLEG: Elektronica met batterij zonder CE, en breekbaar door het glas.
```

### Voorbeeld 3

Pagina:
```
Factory wholesale custom OEM product model HX-2207
MOQ: 500 pieces
Color: customized
Packaging: carton
Place of origin: Zhejiang, China
```

Antwoord:
```
OORDEEL: ONZEKER
RISICO'S: geen
UITLEG: Er staat wel info over bestellen en verpakken, maar nergens wat het product is of van welk materiaal het is.
```

### Voorbeeld 4

Pagina:
```
Nike style running shoes for men breathable mesh
Material: mesh, rubber
Brand name: OEM
Weight: 0.7 kg
```

Antwoord:
```
OORDEEL: NO-GO
RISICO'S:
- A: "Nike style" — Het product doet zich voor als een merkproduct.
UITLEG: Namaakrisico door "Nike style", geen elektronica en niet breekbaar.
```

--- DOCUMENT ---

<plak hier de volledige tekst van build/bronnen/vinted-catalogusregels.md>

--- PRODUCTPAGINA ---

<plak hier de tekst van de productpagina>
