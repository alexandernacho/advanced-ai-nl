# Testset bron (B01–B05)

**Bron:** `build/bronnen/vinted-catalogusregels.md`

Het juiste antwoord, en waar het in het document staat, schrijf je vóór de eerste run.
B01–B04: het document geeft het antwoord. B05: het document geeft het antwoord níet.

| ID | Vraag | Juiste antwoord | Waar in het document | Run 1 | Juist? |
|---|---|---|---|---|---|
| B01 | Mag je als gewone verkoper (niet-Pro) speelgoed verkopen op Vinted? | Ja, maar wie regelmatig inkoopt en verkoopt heeft een ondernemingsnummer en Vinted Pro nodig. | Deel 1, niet-pro: regel 18 (toegestane artikelen: "Kinderspeelgoed"), regels 266–268 (4. Beleid voor commerciële verkoop) | Ja, kinderspeelgoed mag. Bron: deel 1, toegestane artikelen. Zegt niets over inkopen of Vinted Pro. | deels |
| B02 | Mag je voedingssupplementen verkopen op Vinted? | Nee. | Deel 1, niet-pro: regel 63 (verboden artikelen > artikelen met beperkingen). Ook deel 2, Pro: regel 353 | Nee. Bron: deel 1, verboden artikelen > artikelen met beperkingen; geldt ook voor Pro. | juist |
| B03 | Mag je namaak verkopen op Vinted, bv. nep-merkknuffels? | Nee, ook niet als je het vermeldt. | Deel 1, niet-pro: regel 39 (illegale artikelen: "Namaakartikelen"), regels 257–258 (3. Intellectuele Eigendom-beleid, geen disclaimer). Ook deel 2, Pro: regel 332 | Nee, ook nep-merkknuffels niet. Bron: illegale artikelen en 3. Intellectuele Eigendom-beleid. Zegt niets over vermelden. | juist |
| B04 | Mag je als gewone verkoper spullen verkopen die je inkocht om door te verkopen? | Nee, daarvoor heb je een ondernemingsnummer en Vinted Pro nodig. | Deel 1, niet-pro: regels 266–268 (4. Beleid voor commerciële verkoop) | Nee. Bron: 4. Beleid voor commerciële verkoop. Ook niet met een geregistreerd bedrijf; daarvoor is Vinted Pro nodig. | juist |
| B05 | Hoeveel kost verzending met Vinted Go? | `staat niet in het document` (mijn eigen gok: ± 2,70 euro, betaald door de koper) | — | Het document beantwoordt dit niet; geen info over verzendkosten of Vinted Go. | juist |

Resultaat: **4 op 5 juist** (n = 5, 1 run, model: claude-haiku-5-5)

Run 1: elke vraag in een nieuw proces (`claude -p --model claude-haiku-5-5`, zonder tools), met de volledige tekst van het document en de instructie: "Beantwoord de vraag alleen op basis van het document hieronder. Zeg uit welk deel van het document je antwoord komt. Staat het antwoord niet in het document, zeg dat eerlijk. Antwoord kort."
