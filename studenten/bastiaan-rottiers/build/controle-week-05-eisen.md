# Controle tegen de uitgebreide Canvas-opdracht van week 5

De uitgebreide Canvas-instructie vraagt een uitbreiding naar set v2 en zes postkoppen. Voor T11–T20 wordt de uitzondering van tien nieuwe inputs gebruikt; de reden moet in één zin worden vastgelegd. De eerdere controle tegen alleen de les-README was daardoor onvolledig. Een geslaagde GitHub-check controleert bestandsregels en de titel, niet of er twintig inhoudelijk goede testgevallen zijn.

| Onderdeel | Controle |
|---|---|
| Oude tien inputs | T01–T10 zijn behouden tegenover week-4-commit dd435d2, met één openlijk gelogde correctie van het aantoonbaar foutieve verwachte antwoord bij T08. De oorspronkelijke momentopname staat in test-set-v1.md. |
| Tien nieuwe inputs en antwoorden vooraf | T11–T20 zijn met Bastiaans’ goedkeuring vooraf vastgelegd. De logboekcontrole gebruikt alleen Bastiaans eigen tabblad en behandelt een ontbrekende registratie als onzekerheid, niet als bewijs van afwezigheid. |
| Uitzondering op twintig inputs | Gekozen voor tien. Eigen reden: grote, complexe bestanden vragen per input meer dan vijftien minuten voorbereiding. |
| Opzettelijke selectie | T11–T20 moeten bewust gekozen worden uit eigen werkdocumenten en relevante rand- of onzekerheidsgevallen; elke input krijgt een bron en een controleerbaar verwacht antwoord. |
| Uitgangspunt voor fouten | Niet ongevraagd invullen en niets verzinnen. |
| Set v2, versie bovenaan | Set v2: T01–T20, 27 oktober; antwoorden vooraf vastgelegd en reden voor de uitzondering vermeld. |
| Eén run op alle twintig | Voltooid met v7, GPT-6.1 Sol medium; alle twintig hebben één geldige output. T17 gaf eerst een tijdelijke capaciteitsfout en is daarna eenmaal succesvol uitgevoerd. Score: 10 op 20 (set v2, 1 run; n = 20). T08 is na open correctie van het vooraf foutieve antwoord beoordeeld; correctie staat in build/log.md. |
| Prompt niet afstemmen op T11–T20 | v7 blijft voor de controlerun bevroren. Geen fout op de nieuwe controle-inputs gebruiken om de prompt bij te sturen. |
| Foutmargetest | Aanwezig: twee versies, drie rondes, n = 5, model en effort, min–max, overlappende bereiken. v6 is gereconstrueerd; die beperking is vermeld. |
| Modeltest | Aanwezig: gok vooraf, Sol medium 4/5, Luna low 2/5, Astra medium 4/5. Keuze: Sol medium. |
| Ruwe runs | 45 lokale runbestanden, alle met exitcode 0; dit zijn geen 45 verschillende testinputs. |
| Kosten | Sol en Luna correct geprijsd; geen Haiku gebruikt. Oude raming behouden, gecorrigeerd in week 5; rekenkoers en cache-aanname benoemd. |
| Waardeketen | Opnieuw berekend op de eigen tijdschattingen per stap; foutenherstel, werkgeversscenario, scorebereik en zwakste cijfer aanwezig. |
| Publieke dashboardlink | De branchlink in de post geeft HTTP 200 zonder login; de opgehaalde versie bevat de set-v2-kaart en score 10/20. |
| Huidige post | Zes koppen, score 10 op 20 (set v2, 1 run; n = 20), Bastiaans reflectie op T19 en 481 woorden exclusief citaten. Binnen de eis van 300–500 woorden. |
| GitHub | Pull request #122 is open en bijgewerkt; de head commit is cda1d1c. De eerdere technische check slaagde op commit 440ed5b; een nieuwe check op de bijgewerkte commit volgt via GitHub. |
| Canvas | De PR-link moet vóór de deadline op Canvas zijn ingediend. Dat is niet door een gekoppelde Canvas-tool bevestigd. |

De oude scorevergelijkingen zijn op set v1 uitgevoerd. Ze blijven bewaard en worden niet vergeleken alsof set v1 en set v2 dezelfde inputs bevatten.

Bronnen: de door mij aangeleverde Canvas-opdracht; cursus/beoordeling/build-brief.md; cursus/week-05/README.md; de eigen post, meetbestanden en Git-historiek. De actuele OpenAI-prijzen zijn opnieuw gecontroleerd via https://developers.openai.com/api/docs/pricing.
