# v3 — prompt

Plak dit in een nieuw gesprek. Vul onderaan de datum, de renner en de berichten in. Eén bundel per gesprek.

```text
Je helpt iemand die wielerwedstrijden voorspelt. Vóór de start van een grote koers wil die per renner weten in welke fysieke toestand hij of zij is, op basis van recente nieuwsberichten en niet op basis van geruchten of oude uitslagen, voor nu focus je enkel op nieuwsberichten later wanneer ik een duidelijk signaal geef in verband met uitslagen zullen we dit er nog extra in verwerken. Jouw taak: je leest een bundel nieuwsberichten over één wielrenner en bepaalt in welke fysieke toestand die renner nu is. Geef precies één JSON-object terug, en verder niets, want het antwoord wordt naast andere renners in een overzicht gezet.

Kies precies één label:
- "uitgeschakeld": de renner kan op dit moment niet fietsen of koersen door een blessure, ziekte of operatie.
- "in herstel": de renner had een blessure of ziekte en traint opnieuw, maar rijdt nog geen wedstrijden.
- "vermoeid": de renner koerst, maar de berichten wijzen op vermoeidheid of minder vorm, bijvoorbeeld na een zware ronde.
- "goed": de renner koerst en de berichten wijzen op goede vorm, zonder blessure of vermoeidheid. Uitspraken van de renner of de ploeg over zich sterk voelen, alles kunnen geven of een sterk seizoen tellen ook als goede vorm.
- "geen info": de berichten zeggen niets over de fysieke toestand, of ze spreken elkaar tegen zonder duidelijke winnaar.

Regels:
- Gebruik alleen wat in de berichten staat, niet wat je zelf over de renner weet, want je kennis kan verouderd zijn en de vorm van een renner verandert snel.
- Een uitslag, klassement of resultaat alleen zegt niets over de fysieke toestand, want een slechte uitslag kan ook komen door een val, ploegtactiek of een parcours dat niet past. Kijk alleen naar wat er gezegd wordt over blessures, ziekte, vermoeidheid of vorm.
- Het meest recente bericht weegt het zwaarst, want een blessure van drie weken geleden kan vandaag al voorbij zijn. Spreken berichten van dezelfde datum elkaar tegen, kies dan "geen info".
- Kies "geen info" liever dan te gokken, want een fout label kan tot een verkeerde voorspelling leiden, terwijl "geen info" eerlijk zegt dat er meer informatie nodig is.
- Verzin geen feiten die niet in de berichten staan, want de gebruiker moet je reden kunnen controleren in de berichten zelf.
- Geef in "reden" één korte zin: waarom dit label, met verwijzing naar het bericht waarop je je baseert.
- Zegt een bericht zowel iets positiefs als iets negatiefs over de vorm, zoals “ik voelde me goed, maar had niet de benen”, en zegt geen recenter bericht duidelijk iets over het lichaam, kies dan “geen info”, want één positieve uitspraak is niet genoeg om van goede vorm te spreken, en een fout label leidt tot een verkeerde voorspelling.

Voorbeelden (verzonnen renners, alleen om te tonen hoe je beslist):

Voorbeeld 1
BERICHT 1 (3 mei): Renner A brak zijn pols bij een val in de Ronde van Romandië.
BERICHT 2 (20 mei): Renner A traint opnieuw op de weg, maar zijn ploeg zegt dat hij de Giro niet rijdt.
{"label": "in herstel", "reden": "Het recentste bericht zegt dat hij opnieuw traint maar nog geen wedstrijden rijdt."}

Voorbeeld 2
BERICHT 1 (10 juli): "Ik heb nog nooit zulke goede benen gehad", zegt renster B na haar training in de bergen.
BERICHT 2 (12 juli): Renster B zegt dat ze zich klaar voelt om voluit te gaan in de Tour.
{"label": "goed", "reden": "Ze zegt zelf dat ze goede benen heeft en zich klaar voelt om voluit te gaan."}

Voorbeeld 3
BERICHT 1 (1 september): Renner C eindigde als 45e in de tijdrit.
BERICHT 2 (2 september): Renner C tekent een contract bij een nieuwe ploeg.
{"label": "geen info", "reden": "De berichten gaan over een uitslag en een transfer, niet over zijn fysieke toestand."}

Voorbeeld 4
BERICHT 1 (14 september): Renner D zegt na drie weken koers dat hij "volledig leeg" is.
{"label": "vermoeid", "reden": "Hij zegt zelf dat hij volledig leeg is na drie weken koers."}

Nu de echte input:

DATUM VAN VANDAAG: [datum]
RENNER: [naam]

BERICHT 1 ([datum]):
[plak de tekst]

BERICHT 2 ([datum]):
[plak de tekst]

BERICHT 3 ([datum], optioneel):
[plak de tekst]

BERICHT 4 ([datum], optioneel):
[plak de tekst]
```
