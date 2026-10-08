# Testset

Input = de tekst van de homepage, opgehaald op 8 oktober 2026. Volledige tekst per test in `inputs/T0X.txt`.
Juiste antwoord ingevuld **voor** de tool draait. Elke input twee keer, telkens in een nieuw gesprek.

| ID | Input | Juiste antwoord | Waarom | Run 1 | Run 2 |
|---|---|---|---|---|---|
| T01 | Stebaro, Lochristi — stebaro.be | doelgroep `ja`, lead `ja`. E-mail info@stebaro.be, tel 09 345 93 99, Groenstraat 2, 9185 Lochristi, btw BE0451427211 | Trappenmakerij, houten trappen op maat. E-mail staat letterlijk op de site. | ja · ja · info@stebaro.be ✅ | ja · ja · info@stebaro.be ✅ |
| T02 | Trappen Smet, Zulte — trappensmet.be | doelgroep `ja`, lead `geen e-mail`. Tel +32 (0)56 61 34 39, Staatsbaan 289, 9870 Zulte, btw BE 0441.080.477 | Maakt houten trappen. Het e-mailadres is verborgen: in de tekst staat alleen "[email protected]". Raden (info@trappensmet.be) = verzonnen. | ja · geen e-mail · onbekend ✅ | ja · geen e-mail · onbekend ✅ |
| T03 | Deram Systems, Temse — deramsystems.be | doelgroep `nee`, lead `nee` | Plaatst PVC- en aluminium ramen (Deceuninck, Aliplast). Werkt niet zelf met hout. E-mail info@deramsystems.be staat er wel. | nee · nee ✅ | nee · nee ✅ (adres zonder postcode, F6 klein) |
| T04 | Menuiserie Richard, Jodoigne — menuiserie-richard.be (Frans) | doelgroep `ja`, lead `geen e-mail`. Tel 0495 63 79 03, 1370 Jodoigne, btw BE 0571 897 449 | Maakt houten trappen en schrijnwerk. Alleen een knop "Envoyer un e-mail", geen adres in de tekst. | ja · geen e-mail · onbekend ✅ | ja · geen e-mail · onbekend ✅ |
| T05 | DL Interieur, Destelbergen — dl-interieur.be | doelgroep `ja`, lead `ja`. E-mail info@dl-interieur.be, tel +32 479 63 21 74, Burgstraat 78/C003, 9070 Destelbergen | Binnenschrijnwerk: keukens en kasten in MDF, laminaat, fineer **of** massief hout. Maakt keukens en kasten, ook in massief hout: rubberwood past erin. Was een twijfelgeval; beslist op 8 oktober. | ja · ja · info@dl-interieur.be ✅ | ja · ja · info@dl-interieur.be ✅ |

Run: 8 oktober 2026, Claude Sonnet 5.5 via `claude -p`, elke run een nieuw gesprek zonder tools. Formaat Run-kolom: doelgroep · lead · e-mail.
Inputs gezocht door Claude op mijn vraag; de juiste antwoorden heb ik zelf goedgekeurd voor de runs.

**Resultaat v1:** 10/10 juist op doelgroep, lead en e-mail (n = 5, elk 2×). Geen verzonnen e-mail, ook niet bij T02 ("[email protected]").
Te makkelijk? Waarschijnlijk. Week 3: lastigere inputs (site die rubberwood/hevea vermeldt, handelaar die hout doorverkoopt, meerdere e-mailadressen, Engelstalige site).
