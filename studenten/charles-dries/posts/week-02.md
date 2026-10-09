# Week 2 — Eventreacties ordenen

## Wat bouw ik?

Ik bouw een tool die één geanonimiseerde bezoekersreactie over een event leest en die in precies één label plaatst: locatie/bereikbaarheid, programma, catering, prijs, personeel, veiligheid, geen verbeterpunt of onzeker/anders. Zo kan een eventorganisator achteraf zien welke verbeterpunten het vaakst terugkomen.

## Waarom een taalmodel?

Een taalmodel past bij deze taak omdat bezoekers hun mening in vrije en soms rommelig geschreven tekst geven. Het kan begrijpen waar een reactie over gaat, ook wanneer iemand het niet met vaste woorden zegt. Bij een onduidelijke reactie of meerdere onderwerpen kiest de tool `onzeker/anders`, zodat ze niet gokt.

## Eén testinput

**Input:** “Bambata Openair: De straten lagen open, dus het was moeilijker bereikbaar. De locatie was niet zo goed aangeduid. Het eten was wel heel lekker.”

**Juiste antwoord:** `locatie/bereikbaarheid`, omdat de verbeterpunten over werken, bereikbaarheid en aanduiding gaan.

**Wat de tool zei:** `{"label":"locatie/bereikbaarheid","reden":"De reactie noemt openliggende straten en gebrekkige aanduiding als verbeterpunten voor de bereikbaarheid en locatie."}`

Ik testte tien reacties twee keer. Beide testruns gaven tien juiste labels op tien.
