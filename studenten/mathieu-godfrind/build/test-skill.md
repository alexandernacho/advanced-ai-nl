# Test skill: klantbericht (3 tests, elk in eigen sub-agent)

Skill: `.claude/skills/klantbericht/SKILL.md`

## Test 1: nieuw met label, 25 cm

**Koper:** "Hallo, is de knuffel nog nieuw? En hoe groot is hij?"
**Info verkoper:** nieuw met label, 25 cm

**Antwoord:**
> Hallo, ja, de knuffel is nieuw en heeft nog zijn label. Hij is 25 cm groot.

**Check:** 2 zinnen (plus groet), niets beloofd, geen [INVULLEN] nodig. ✅

## Test 2: prijsonderhandeling, geen info

**Koper:** "Wil je hem voor 8 euro verkopen i.p.v. 12?"
**Info verkoper:** geen

**Antwoord:**
> Hallo, bedankt voor je bericht. Over de prijs: [INVULLEN: wel of niet akkoord met het bod van 8 euro]. Laat gerust weten wat je beslist.

**Check:** 3 zinnen, niets beloofd, geen akkoord of weigering verzonnen, [INVULLEN] op de plek van de beslissing. ✅

## Test 3: verzenden vandaag, geen info

**Koper:** "Kan je vandaag nog verzenden? Mijn dochter verjaart zaterdag."
**Info verkoper:** geen

**Antwoord:**
> Hallo, bedankt voor je vraag en ik begrijp dat je het graag op tijd wil hebben voor de verjaardag van je dochter. [INVULLEN: of en wanneer je vandaag nog kan verzenden]. [INVULLEN: verwachte verzend- en leveringstermijn, zodat het pakje op tijd voor zaterdag kan aankomen]. Laat maar weten als je nog vragen hebt.

**Check:** 4 zinnen (de telling is met de hand gedaan), niets beloofd over verzending of levering, twee [INVULLEN]-plekken voor wat ontbreekt. Let op: de zin "ik begrijp dat..." is wel erg lang. ⚠️

## Samenvatting

| Test | Koper | Zinnen | Niets beloofd | [INVULLEN] waar nodig | Resultaat |
|---|---|---|---|---|---|
| 1 | Nieuw? Hoe groot? (info gegeven) | 2 | ✅ | n.v.t. (info was er) | ✅ |
| 2 | Bod 8 euro | 3 | ✅ | ✅ | ✅ |
| 3 | Verzenden vandaag | 4 | ✅ | ✅ | ✅ (lange zin) |

## Opmerkingen

- De skill werkte bij alle drie: geen beloftes, geen verzonnen info, [INVULLEN] waar info ontbrak.
- Test 3 zit op het maximum van 4 zinnen. Een kortere formulering zou beter zijn.
- Test 1 gebruikt de info uit de context. Test 2 en 3 zonder info laten zien dat de skill niets verzint.
