# Dashboard — week 5

Zelfstandig cursusbestand: `build/dashboard.html`. Alle stijlen en interactieve logica staan in dit ene bestand; geen externe scripts of lettertypes.

## Online versie

- URL: https://kwartaalopvolging-week-vijf.socialmorel1025.chatgpt.site
- Gepubliceerd op 23 oktober 2026 met de Sites-plugin.
- Toegang: **openbaar**, op 23 oktober 2026 ingesteld nadat de student het dashboard bekeken had en vroeg verder te gaan. Iedereen met de URL kan de pagina bekijken.
- Site-ID: `appgprj_6adb79d49c30819199b01af54aa3f836`.
- Versie-ID: `appgprj_6adb79d49c30819199b01af54aa3f836~appgver_ade2495e8d208191a53103b9ba11bf1a`.
- Eerste privédeployment: `appgdep_6adb7db05c2c8191b7e07ccf3179d24b`, status `succeeded`.
- Publieke deployment van dezelfde opgeslagen versie: `appgdep_6adb7e64aee08191a8137583cfc1f43f`, status `succeeded`.
- Broncommit in de afzonderlijke Sites-repo: `3ff24ef088f0b3cb30ca45f91858ded1457b1692`.
- Lokale hostingbron: `build/site-dashboard/`, met Site-identiteit in `.openai/hosting.json`. Deze aparte repo en het pakket zijn uitgesloten van de cursusgit; het zelfstandige dashboard blijft in de studentenmap beschikbaar voor indiening.

## Controle

- Lokale browserpreview: eerste desktopweergave en kernbedragen visueel gecontroleerd.
- Schuifregelaars: berekeningen voor 40 en 20 updates, nul updates en herstel van de standaardwaarden met JavaScript gecontroleerd.
- Geen externe scripts/stijlen; hostingversie en cursusbestand inhoudelijk gelijk bij publicatie.
- Mobiele indeling is met CSS ingericht; geen afzonderlijke visuele controle op een mobiel scherm uitgevoerd.
- Cijfers komen uit `foutmarge.md`, `modellen.md`, `kosten.md`, `waarde.md` en de vastgelegde studentkeuzes. De scenario-schuifregelaars wijzigen de opgeslagen meetresultaten niet.
- Publieke toegang bevestigd op 23 oktober 2026: na publicatie van dezelfde versie voor de openbare doelgroep is de pagina zonder cookies, bearer-token of login via curl opgehaald. De ontvangen HTML bevat de dashboardtitel en kerncijfers. De eerdere toegangsrespons vóór deze publicatie is daarmee opgelost. Een privévenster is geopend, maar de UI-controle is niet afgerond doordat de actieve Safari-weergave wijzigde; de geslaagde anonieme HTTP-opvraag is het bewijs voor toegang zonder login.

De URL hierboven is klaar om in `posts/week-05.md` te gebruiken. Het zelfstandige `dashboard.html` moet ook met de week-05-indiening mee. Er is met deze publicatie niets naar de cursusfork gepusht.
