# Week 7: Vertuoza maakt offertes uit spraak, maar zegt niet voor hoeveel

## Mijn skill

Elke run met de hand begon met plakken in een nieuw gesprek: de prompt (2.376
woorden), de btw-pagina van FOD Financiën (1.216 woorden) en de werfopname. Nu
is dat één commando: `/offerteposten` met de opname erachter. De skill is prompt
v4, letterlijk overgenomen, met de FOD-bron als bestand ernaast.

Getest op drie inputs uit mijn testset, elk in een eigen sub-agent, antwoord
vooraf: **3 op 3 juist** (n = 3, 1 run, Claude Opus 5.5).

- T02, de fout uit week 3: v2 zette er twee keer een lichtpunt van 415 euro bij.
  In de skill blijft die post weg.
- T11 en T12, de twee opnames die het meest op een echte werf lijken: alles
  klopte.

Daarna typte ik zelf T05 in een nieuwe sessie. Ook juist.

In alle vier de runs vroeg de skill naar de ouderdom van de woning, door de
btw-regel uit week 6. Joeri krijgt die vraag dus bij elke offerte, ook als hij
het antwoord al weet.

3 op 3 zegt weinig: de prompt is op deze inputs geschreven. Wel draaide v4 voor
het eerst op Claude.

[Skilltest](../build/skill-test.md) · [Skill](../.claude/skills/offerteposten/SKILL.md)

## Mijn connector

Firecrawl, in Claude Code. Mijn drie sub-agents voor Buy lazen er de
prijspagina's mee.

Nuttig: het haalde de prijspagina van Trustup Pro op, waar een gewone download
op Cloudflare botste.

Niet nuttig: de prijs van Robaws staat alleen in de HTML, niet in de tekst. Eén
agent vond hem daar, een andere nam van een vergelijkingssite "op aanvraag"
over. Dat is criterium 2 uit mijn GEO-audit van week 6. En Firecrawl rekent
credits aan, terwijl ik daar niet om had gevraagd.

## Build, Connect, Buy

|  | Voor Joeri | Wat zit er vast? |
|---|---|---|
| **Build** | Mijn prompt als skill `/offerteposten`: één map met twee bestanden. | Bijna niets. De map is van mij, en Codex en de Claude-app lezen hetzelfde formaat. |
| **Connect** | De skill maakt de posten, Claude zet ze via de MCP-koppeling van Robaws in zijn pakket. Gratis voor klanten; Robaws Starter kost 29 euro per maand bij jaarbetaling. | MCP is een open standaard, maar de offertes staan dan in Robaws. Of de koppeling een offerte kan aanmaken, staat nergens. |
| **Buy** | Vertuoza, de enige van de drie die offertes uit spraak maakt. Prijs niet publiek (gelezen op 25 november 2026). Bij Robaws en Trustup Pro (39 euro per maand bij jaarbetaling) vond ik geen spraak. | Offertes exporteren kan, het formaat staat er niet bij. Mijn prijslijst exporteren: niet gevonden. |

**Mijn advies:** Build, want het is de enige van de drie met een gemeten score:
3 op 3 op Claude, en 35 op 36 voor v3 op GPT-6 Luna in week 5. Bij de pakketten
met een publieke prijs vond ik geen spraak.

**Wat me van mening doet veranderen:** als een pakket met spraak, zoals
Vertuoza, mijn 12 testopnames minstens even goed omzet en mijn offertes en
prijslijst laat exporteren.

[Prijzen en bronnen](../build/buy-prijzen.md)
