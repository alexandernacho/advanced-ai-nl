# Week 7: mijn eerste skill, en wat "kopen" kost

## Mijn skill
Ik verkoop op Vinted. Kopers vragen vaak dezelfde dingen. Ik schreef elke keer opnieuw hetzelfde antwoord. Nu heb ik een skill gemaakt: `klantbericht`. Hij schrijft een kort antwoord in het Nederlands op de vraag van een koper.

Ik heb hem 3 keer getest. Elke test liep in een eigen sub-agent.

- **Test 1:** nieuw met label, 25 cm. Goed. Hij gebruikte alleen mijn info.
- **Test 2:** een bod van 8 euro, zonder info. Goed. Hij verzon niets en liet de beslissing open.
- **Test 3:** verzenden vandaag, zonder info. Goed, maar één zin was te lang.

Dus 3 van de 3 was goed. Na test 3 heb ik de regel "max 20 woorden per zin" toegevoegd. Die heb ik nog niet opnieuw getest. Dat doe ik de volgende keer.

## Mijn connector
Ik heb Gmail gekoppeld in Claude op claude.ai. Ik vroeg naar mijn laatste Vinted-mails. Gmail vond vooral zendingsmeldingen van een eigen aankoop, geen verkopen.

Ik heb ook CoinGecko gekoppeld in Claude Code. Ik vroeg: wat kost bitcoin nu in euro? Het antwoord was €53.521, en de prijs is in 24 uur met 2,07% gedaald (25 november, rond 11:31 UTC). Zonder de koppeling kon Claude geen actuele prijs geven. Dat is het verschil.

## Build, Connect, Buy
Voor mijn capstone: een boekhoudprogramma voor mijn webshop en Vinted-verkoop.

|  | Voor mijn boekhouding | Wat zit er vast? |
|---|---|---|
| **Build** | Een Excel-blad met mijn verkopen. Claude maakt er een factuur van. | Ik moet het zelf bijhouden. En ik moet de btw-regels zelf kennen. |
| **Connect** | Claude leest mijn Vinted-mails in Gmail en zet de verkopen in een Google Sheet. | Het werkt alleen zolang de connector werkt. En de mails moeten alle info hebben. |
| **Buy** | 3 programma's: Billit, Yuki en Accountable. Prijs per maand, excl. btw: Billit €7,50 (maandelijks), Yuki €23,50 nu of €24 vanaf 2027, Accountable €19,90 (jaarabonnement). Opgehaald op 25-11-2026, bronnen in build/buy.md. | Mijn facturen en btw staan in hun systeem. Kan ik ze exporteren? Nog niet gecontroleerd. |

Wat ik nog niet zeker weet:
- Billit: ik weet niet of €7,50 excl. of incl. btw is.
- Yuki: de prijs is €23,50 of €24. Dat moet ik bij Yuki nagaan.

**Mijn advies:** Build. Excel is gratis. Met ± 35 verkopen heb ik nog geen programma nodig. Ik ken Excel al.
**Wat me van mening doet veranderen:** Als ik veel meer ga verkopen en de btw te ingewikkeld wordt, dan neem ik Billit.
