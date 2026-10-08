# Kwartaalrapporten vergelijken

Deze tool helpt mij als beginnende belegger die aan stockpicking doet om twee kwartaalrapporten overzichtelijk te vergelijken. De uitvoer bevat FCF, totale rentedragende schuld, omzetgroei en expliciet genoemde risico’s, met bronverwijzingen. Ik beoordeel de gegevens zelf.

## Bestanden

- `taak.md`: mijn taak en oorspronkelijke inputideeën.
- `prompt-v1.md`: oorspronkelijke prompt.
- `prompt-v2.md`: huidige werkversie, met de auditlabels B1–B6. De omzetgroei- en vormregels zijn getest met T06–T10; de gewijzigde FCF-perioderegel is in één gerichte keuzevraagtest geslaagd (geen volledige financiële vergelijking).
- `test-set.md`: tien testinputs (T01–T10), verwachte antwoorden, ontvangen runs en resterende controles.
- `log.md`: wijzigingen, teststatus en volgende stappen.

## Gebruik

1. Open per test een nieuw tijdelijk gesprek zonder geheugen en zonder web search.
2. Kopieer uit `prompt-v2.md` alles vanaf “Instructies om te kopiëren”, inclusief de voorbeelden.
3. Voeg bij het inputonderdeel de twee rapporten als bestanden of volledige tekst toe. Geef `test-set.md` niet mee, want daarin staan de verwachte antwoorden.
4. De tool gebruikt bij voorkeur FCF over hetzelfde kwartaal. Lukt dat niet, dan toont hij beschikbare gemeenschappelijke perioden en wacht hij op mijn keuze. Noteer die keuze bij de run.
5. Controleer de uitvoer zelf aan de hand van de rapporten en mijn vooraf vastgelegde verwachtingen. Leg de uitvoer, fouten en gebruikte promptversie vast in `test-set.md` en `log.md`.

## Nog te doen voor week 3

- Tien inputs zijn aanwezig. Controleer of minstens drie als lastig geval zijn onderbouwd en of alle vooraf vastgelegde verwachtingen en beoordelingen compleet zijn.
- Buurtest uitvoeren met drie inputs en alleen de prompt als instructie.
- Resterende bronclaims controleren en fouten classificeren met F1–F6.
- T06–T10 zijn afgerond: 10/10 geslaagde omzetgroeiruns (n = 5 inputs, elk 2 runs). Controleer T01–T05 en hun testcondities voordat een totaalscore voor alle tien inputs wordt vastgesteld.
- Gekozen FCF-perioderegel: oude v2 kiest automatisch halfjaar, huidige v2 toont keuzes en wacht; één gerichte gedragstest geslaagd. Vermeld dat ook andere promptonderdelen gewijzigd zijn en dat één test geen algemeen bewijs vormt.
- Mijn eigen post schrijven in `posts/week-03.md` en indienen vóór dinsdag 13 oktober 2026, 23:59.
