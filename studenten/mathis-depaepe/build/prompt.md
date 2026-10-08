# v1 — prompt

Plak dit in een nieuw gesprek. Vervang de advertentie onderaan.

```text
Je haalt gegevens uit één advertentie van een tweedehands luxehorloge. De advertentie kan in het Nederlands, Frans, Duits of Engels zijn. Geef precies één JSON-object terug, en verder niets.

Velden:
- "merk": het merk, bv. "Rolex".
- "model": de modelnaam, bv. "Submariner Date".
- "referentienummer": het referentienummer zoals het in de advertentie staat, bv. "126610LN".
- "bouwjaar": het jaar als getal, bv. 2019.
- "staat": precies één van "nieuw", "zeer goed", "gedragen", "beschadigd".
  - "nieuw": nooit gedragen, ongedragen, stickers nog aanwezig.
  - "zeer goed": gedragen, maar nauwelijks gebruikssporen.
  - "gedragen": duidelijke gebruikssporen, krassen.
  - "beschadigd": defect, kapot onderdeel, werkt niet goed.
- "doos_papieren": precies één van "full set", "enkel doos", "enkel papieren", "geen", "onbekend".
  - "onbekend": de advertentie zegt niets over doos of papieren.
  - "papieren" betekent garantiekaart of certificaat. Een factuur alleen telt niet als papieren.
  - Een algemene vermelding van "papieren" (bv. "Papiere", "papiers", "Unterlagen"), ook in de titel, volstaat niet. Alleen een expliciet genoemde garantiekaart of certificaat telt als papieren.
- "vraagprijs": het bedrag als getal, zonder punten of munt, bv. 12500.
- "munt": de munt, bv. "EUR", "CHF", "USD".
- "verkoper": precies één van "particulier", "handelaar".
- "servicegeschiedenis": een korte zin met wat er staat over service of revisie, bv. "revisie bij Rolex in 2022".

Regels:
- Gebruik alleen wat letterlijk in de advertentie staat.
- Staat iets er niet, of is het niet duidelijk? Vul "onbekend" in.
- Vul nooit iets aan uit eigen kennis. Leid bv. het merk niet af uit het referentienummer, en het bouwjaar niet uit het model.
- Kies "onbekend" liever dan te gokken.

Formaat:
{"merk": "...", "model": "...", "referentienummer": "...", "bouwjaar": ..., "staat": "...", "doos_papieren": "...", "vraagprijs": ..., "munt": "...", "verkoper": "...", "servicegeschiedenis": "..."}

ADVERTENTIE
Titel: [plak de titel]
Tekst: [plak de tekst]
Verkoper: [plak wat er over de verkoper staat, of laat leeg]
```
