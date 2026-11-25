# Test prompt op Vinted (1 run, 13 inputs)

Datum: 2026-11-25
Prompt: `build/prompt.md` (risico D verwijst naar `build/bronnen/vinted-catalogusregels.md`)
Model: `claude-haiku-5-5` via `claude -p --tools ""`, elke input in een nieuwe sessie, in een lege map zonder CLAUDE.md.
Juiste antwoorden: `build/test-set.md`, ongewijzigd.

## Score: 12 op 13 juist

| ID | Juist | Model | Oordeel |
|---|---|---|---|
| T01 | GO | GO | juist |
| T02 | GO | GO | juist |
| T03 | GO | GO | juist |
| T04 | NO-GO (C) | NO-GO (C) | juist |
| T05 | ONZEKER | NO-GO (B) | **fout, F1** (verkeerd label) |
| T06 | GO | GO | juist, maar de uitvoer staat in een codeblok |
| T07 | NO-GO (D) | NO-GO (D) | juist |
| T08 | NO-GO (A, B) | NO-GO (A, B) | juist |
| T09 | NO-GO (B) | NO-GO (B) | juist |
| T10 | GO | GO | juist |
| T11 | NO-GO (A) | NO-GO (A) | juist |
| T12 | NO-GO (B) | NO-GO (A, B) | juist. Extra risico A ("Niuniu Energy Drink"), opvallend, geen fout |
| T13 | NO-GO (B) | NO-GO (B) | juist |

## Fouten

- **T05 (F1):** de pagina is vaag. De titel bestaat uit zoekwoorden en de specificaties zijn bijna leeg, dus het juiste label is ONZEKER. Het model zegt NO-GO (B) op basis van "Promotionele Elektronische Producten" en het ontbreken van CE. Dit is dezelfde fout als in week 5.

## T07: risico D

Juist. De citaten staan letterlijk in de bronnen:
- Pagina: "Gezondheidssupplementen" (titel)
- Document (deel 1, niet-pro): "vitamines, voedingssupplementen en andere gezondheidsgerelateerde producten."

Het model gebruikt het document van Vinted, niet bol.com. Het noemt ook de tegenstrijdige omschrijving "snoepgoed" en kiest de riskantste (beslisregel 4).

## Opvallend (geen fout)

- **T12:** extra risico A door "Niuniu Energy Drink". Het citaat staat op de pagina.
- **T01:** de uitleg noemt MOQ 200 en het Vinted-verbod op commerciële inventaris. Dat is geen risico-regel en telt niet als D. De prompt dekt dit verbod nog niet af (zie het voorstel over risico D).
- **Opmaak:** T06 en T08 staan in een codeblok, terwijl de prompt "exact deze vorm" vraagt. De inhoud klopt. Dit telt niet als fout volgens de testset.

## Vergelijking met week 5

Week 5 (bol.com-versie, `claude -p`, Haiku): 24 op 26 juist. Fouten: T05 (2×).
Nu (Vinted-versie, 1 run): 12 op 13 juist. Fout: T05 (1×). T07 blijft juist.

## Ruwe uitvoer

Antwoorden van het model (ingekort: de RISICO'S-regels en het oordeel, de UITLEG-regels zijn weggelaten behalve bij T01):

```
T01: OORDEEL: GO / RISICO'S: geen / UITLEG: Geen merk van iemand anders, geen elektronica of batterij, geen speelgoed, niet breekbaar en 0,3 kg; let wel op MOQ 200 stuks, want het doorverkopen van bulkinkoop van een leverancier valt onder het Vinted-verbod op commerciële inventaris.
T02: OORDEEL: GO / RISICO'S: geen
T03: OORDEEL: GO / RISICO'S: geen
T04: OORDEEL: NO-GO / RISICO'S: - C: "Glass" (Basismateriaal)
T05: OORDEEL: NO-GO / RISICO'S: - B: "Promotionele Elektronische Producten"
T06: OORDEEL: GO / RISICO'S: geen (in codeblok)
T07: OORDEEL: NO-GO / RISICO'S: - D: "Gezondheidssupplementen" — document (deel 1, niet-pro): "vitamines, voedingssupplementen en andere gezondheidsgerelateerde producten."
T08: OORDEEL: NO-GO / RISICO'S: - A: "Monsters Energy Shape: Authentiek ontwerp geeft de iconische energiedranklook weer." - B: "type: drinkend speelgoed" (in codeblok)
T09: OORDEEL: NO-GO / RISICO'S: - B: "Nom de l'article : Lampe de bureau LED avec protection des yeux, grande horloge et calendrier, veilleuse"
T10: OORDEEL: GO / RISICO'S: geen
T11: OORDEEL: NO-GO / RISICO'S: - A: "Designer Frans geïnspireerde schoudertas"
T12: OORDEEL: NO-GO / RISICO'S: - A: "Nieuwe rode Niuniu Energy Drink blik pluche pop" - B: "blik pluche pop"
T13: OORDEEL: NO-GO / RISICO'S: - B: "Donker konijnenknuffel"
```

Alle citaten van de pagina zijn gecontroleerd: ze staan letterlijk in de testpagina's.
