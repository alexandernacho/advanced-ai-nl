# Foutmarge — week 5

## Voorspelling van Cansu vóór de nieuwe tests

> Ik denk dat v5 beter zal scoren dan v4. In v4 vulde de tool bij een onduidelijk aantal sets soms zelf een aantal in, zoals 3 sets, terwijl dat niet zeker was. Daardoor kon verkeerde informatie in de tabel komen. V5 moet in zo’n situatie “onbekend” zetten in plaats van te gokken. Bij duidelijke notities zal het resultaat waarschijnlijk hetzelfde blijven, maar bij onduidelijke notities verwacht ik minder fouten.

## Voorbereiding

Te vergelijken: `prompt-v4.md` en `prompt-v5.md`, elk drie runs op dezelfde inputs, met hetzelfde model en dezelfde beoordelingsregels.

Bij input 6 veranderde het verwachte aantal sets eerder van `4` naar `onbekend`. Cansu bevestigt vóór de nieuwe tests: voor zowel v4 als v5 is bij deze input alleen `onbekend` bij Sets correct. Een ingevuld totaal, waaronder `3` of `4`, is fout. De overige velden volgen de vooraf vastgelegde v5-uitvoerafspraak: oefening `cable straight arm pull down`, gewicht `20kg`, herhalingen `3 x 12, laatste set: tot failure (aantal onbekend)`. Inhoudelijk gelijkwaardige schrijfwijzen zijn toegestaan, zonder een totaal aantal sets te verzinnen.

Deze gemeenschappelijke regel geldt voor de nieuwe vergelijking. De eerdere resultaten en verwachte antwoorden blijven bewaard in `test-set.md` en worden niet achteraf herbeoordeeld.

## Uitvoering — 24 oktober 2026

Model aangevraagd: `gpt-5.6-terra`, effort `high`. Deze technische modelnaam staat in de lokale Codex-modellijst en in de [officiële modeldocumentatie](https://developers.openai.com/api/docs/models/gpt-5.6-terra). Cansu rapporteert de instelling van haar eerdere tests als `GPT 5.6 terra hoog`; van die historische ChatGPT-tests is geen technische model-ID vastgelegd.

Nieuwe vergelijking via `codex exec`: n = 10 oorspronkelijke inputs, 3 runs per versie, 60 afzonderlijke sessies. Elke sessie krijgt één promptversie met één notitie. Verwachte antwoorden, eerdere gesprekken en projectdocumenten worden niet meegestuurd. Sessies draaien in een lege tijdelijke map, met gebruikersconfiguratie en projectdocumenten uitgeschakeld; Codex voegt wel eigen systeeminstructies toe. Shell, webzoeken en apply_patch zijn uitgeschakeld. Eventlogs worden gecontroleerd op toolgebruik. De Codex-omgeving is anders dan de eerdere handmatige ChatGPT-omgeving; de twee nieuwe versies worden onderling in dezelfde omgeving vergeleken.

Input 7 staat met antwoord als voorbeeld in beide prompts. Rapporteer daarom ook de score zonder input 7 (n = 9). De overige inputs en beoordelingsregels volgen `test-set.md`, met de hierboven bevestigde gemeenschappelijke regel voor input 6. Variant 6b telt niet mee.

Script, antwoorden en uitvoerlogs: `week-05-runs/`. Alle 60 aanroepen zijn afgerond. De uitvoerlogs bevatten 60 verschillende sessies en geen toolgebruik. Technisch mislukte aanroepen tellen niet als inhoudelijk fout antwoord.

## Voorlopige beoordeling door Codex

Cansu heeft twee antwoorden zelf nagekeken; zie de zelfcontrole onderaan. Onderstaande scores volgen de vooraf vastgelegde uitvoerregels. Bij één nagekeken antwoord accepteert Cansu een compactere uitvoer dan vooraf afgesproken; dit verschil is afzonderlijk bewaard.

| Versie | Run 1 | Run 2 | Run 3 | Waargenomen bereik (min–max) |
|---|---:|---:|---:|---:|
| v4 | 9/10 | 8/10 | 9/10 | 8–9/10 |
| v5 | 8/10 | 9/10 | 8/10 | 8–9/10 |

Dit is het waargenomen bereik over drie herhalingen, geen statistisch betrouwbaarheidsinterval.

### Beoordeling per input

| Input | v4 run 1 | v4 run 2 | v4 run 3 | v5 run 1 | v5 run 2 | v5 run 3 |
|---|---|---|---|---|---|---|
| 1 | Correct | Correct | Correct | Correct | Correct | Correct |
| 2 | Correct | Correct | Correct | Correct | Correct | Correct |
| 3 | Correct | Correct | Correct | Correct | Correct | Correct |
| 4 | Correct | Correct | Correct | Correct | Correct | Correct |
| 5 | Correct | Correct | Correct | Correct | Correct | Correct |
| 6 | F1 | F1 + F3 | F1 | Correct | Correct | Correct |
| 7 (promptvoorbeeld) | Correct | Correct | Correct | Correct | Correct | Correct |
| 8 | Correct | F4 | Correct | F4 | F4 | F4 |
| 9 | Correct | Correct | Correct | F1 + F3 | Correct | F4 |
| 10 | Correct | Correct | Correct | Correct | Correct | Correct |

Eén antwoord met meerdere foutsoorten telt als één fout antwoord.

- Input 6, v4: alle runs kiezen `3` sets in plaats van `onbekend`. Run 2 laat ook failure weg. V5 zet alle drie keren `onbekend` en behoudt drie keer twaalf en de laatste set tot failure; de uitschrijving `12, 12, 12` is inhoudelijk gelijkwaardig aan `3 x 12` zonder een totaal in Sets vast te leggen.
- Input 8: v4 run 2 en alle v5-runs geven slechts `tot failure (aantal onbekend)` in de cel Herhalingen. De vooraf afgesproken uitvoer specificeert alle drie sets, of vermeldt expliciet dat alle drie tot failure gaan. Daarom voorlopig F4, overeenkomstig de historische beoordeling van een onvoldoende uitgesplitst antwoord. Dit is een belangrijk antwoord voor Cansu om zelf te controleren.
- Input 9, v5 run 1: Sets is `onbekend` in plaats van `4`; de herhalingscel vermeldt alleen failure en laat de verdeling over de vier sets weg. Run 3 heeft wel `4` sets en `laatste set: tot failure (aantal onbekend)`, maar noemt de onbekende herhalingen van de eerste drie sets niet expliciet: voorlopig F4 volgens de afgesproken volledige uitvoer. Ook deze beoordeling moet Cansu nakijken. Als zij de beoordelingsregel wil veranderen, wordt dat een afspraak voor een volgende test, geen stilzwijgende aanpassing van deze ronde.
- Hoofdletters en `face pulls` versus `facepulls` veranderen de inhoud niet en zijn toegestaan volgens eerdere afspraken.

Zonder promptvoorbeeld 7: v4 **8/9, 7/9, 8/9** (bereik 7–8/9); v5 **7/9, 8/9, 7/9** (bereik 7–8/9). Beide versies vertonen wisselende naleving (F6): v4 bij inputs 6 en 8, v5 bij input 9. Alleen verschillen in hoofdletters tellen niet als inhoudelijke wisseling.

## Conclusie volgens de beslisregel

Voorspelling: v5 scoort beter dan v4 doordat de tool bij onduidelijke sets niet gokt.

**Algemene verbetering niet bewezen; de bereiken overlappen.** Volgens de beslisregel van week 5 wordt de algemene claim ingetrokken. De gerichte verbetering bij input 6 is in deze ronde wel zichtbaar (v4 0/3 correct, v5 3/3), maar er zijn ook fouten bij andere inputs. Cansu heeft twee beoordelingen gecontroleerd en haar eigen conclusie hieronder geformuleerd. De voorspelling blijft hierboven ongewijzigd bewaard.

## Zelfcontrole door Cansu — afgerond

1. Open `week-05-runs/v5-run-1-input-08.txt` en vergelijk met de vooraf vastgelegde uitvoer voor input 8.
2. Open `week-05-runs/v5-run-3-input-09.txt` en vergelijk met de vooraf vastgelegde uitvoer voor input 9.

Noteer wat je zelf correct of fout vindt en waarom. Er zijn nog geen verwachte antwoorden aangepast.

### Zelfcontrole 1 — input 8, v5 run 1

Cansu vindt het antwoord goed en licht toe:

> ik vind dit goed aangezien tot failure betekent dat ik moet gaan tot wanneer het niet meer lukt, tot mijn kracht het niet meer aan kan wat betekent dat ik niet heb geteld maar gewoon door ga tot mijn kracht het niet meer aan kan

Er is een verschil tussen de beoordelingen: Codex gaf voorlopig F4 omdat de vooraf afgesproken uitvoer alle drie sets expliciet tot failure laat gaan; Cansu accepteert de compacte vermelding in dit antwoord. Dit verschil wordt zichtbaar bewaard. De verwachte antwoorden en scores van deze ronde worden niet achteraf aangepast. Voor een volgende ronde kan Cansu vooraf verduidelijken of één vermelding van failure bij drie sets voldoende is. De tweede zelfcontrole staat hieronder.

### Zelfcontrole 2 — input 9, v5 run 3

Cansu vindt dat de onbekende herhalingen van de eerste drie sets expliciet moeten worden vermeld:

> de eerste drie moeten ook onbekend vermelden omdat ik tijdens die opdracht ben vergeten te noteren tot hoeveel herhalingen ik ben gegaan, het is dus onbekend

Dit bevestigt de beoordeling F4 voor dit antwoord: de afgesproken uitvoer is onvolledig. Het verwachte antwoord blijft `onbekend, onbekend, onbekend, tot failure (aantal onbekend)` bij Herhalingen, met `4` bij Sets.

Beide zelfcontroles zijn afgerond. Bij één van de twee antwoorden verschillen Cansu en Codex van oordeel; bij het tweede zijn ze het eens. De scores volgens de vooraf vastgelegde uitvoerregels blijven behouden.

## Conclusie van Cansu

> Met deze resultaten kunnen we nog niet concluderen dat v5 duidelijk beter is dan v4. V5 volgt de nieuwe regel rond onduidelijke sets beter, maar omdat beide versies in totaal 8 à 9 op 10 scoren, lijkt de globale nauwkeurigheid voorlopig vergelijkbaar. We zouden moeten bekijken bij welke specifieke notities v5 nog fouten maakt en de instructie daar verder verfijnen.

De algemene claim dat v5 beter scoort is **ingetrokken voor deze vergelijking**, omdat de bereiken overlappen (beide 8–9/10). Dit betekent dat de algemene verbetering niet bewezen is. De gerichte verbetering bij input 6 blijft afzonderlijk zichtbaar. Promptwijzigingen zijn nog niet uitgevoerd; voor de modeltest blijft v5 gelijk, zodat alleen de modelinstelling verandert.
