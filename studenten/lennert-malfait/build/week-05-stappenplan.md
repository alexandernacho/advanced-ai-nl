# Week 5 — 20 mails stap voor stap

Gebruik dit document terwijl Outlook openstaat. Je hoeft geen volledige mails te
kopiëren. Noteer alleen onderwerp, datum, geanonimiseerde afzender/type, één
zin samenvatting, verwacht label en reden.

## Eerst instellen

1. Open Outlook en zoek de eerste mail met de zoekterm uit de tabel.
2. Open de mail en lees onderwerp plus volledige tekst.
3. Vervang namen door `[naam]`, datums door `[datum]` en links door `[link]`.
4. Schrijf de voorgestelde zin over en pas alleen details aan die echt in de
   mail staan.
5. Kies het verwachte label vóór je de mail door de classifier haalt.
6. Bewaar daarna pas de classificatie van de tool. Dat is het meetresultaat.

## De 20 inputs

| ID | Zoekterm in Outlook | Schrijf bij de mail | Verwacht label |
| --- | --- | --- | --- |
| W5-01 | `opdrachtgever` | “Een externe opdrachtgever vraagt extra informatie en noemt [datum] als deadline.” | `doen` |
| W5-02 | `copywriting` | “De copywriting-opdracht moet vóór [datum] ingediend worden.” | `doen` |
| W5-03 | `copywriting` | “Dit bericht herhaalt dezelfde copywriting-opdracht en deadline als W5-02.” Gebruik dit alleen als het echt dezelfde mailinhoud is. | `herhaling` |
| W5-04 | `Canva` | “Ik krijg een uitnodiging voor een Canva-groep van [opleidingsonderdeel].” | `doen` |
| W5-05 | `deadline gemist` | “De deadline is gemist en de mail legt mogelijke gevolgen voor het eindcijfer uit.” | `doen` |
| W5-06 | `masterclass` | “Na een online masterclass ontvang ik materiaal en wordt om feedback gevraagd.” | `doen` |
| W5-07 | `feedback coaching planning` | “De mail bevat feedback, coaching en planning voor een groepsopdracht.” | `lezen` |
| W5-08 | `examen groep 1` | “De mail bevat exameninformatie en een case voor groep 1.” | `lezen` |
| W5-09 | `examen groep 2` | “De mail bevat exameninformatie en een case voor groep 2.” | `lezen` |
| W5-10 | `studiegeld` | “De mail meldt dat een betaling ontbreekt en vraagt mij om opvolging.” | `doen` |
| W5-11 | `Canvas gewijzigde datum` | “Canvas meldt dat de inleverdatum van een opdracht veranderd is naar [datum].” | `lezen` |
| W5-12 | `Franse conversatietafels` | “Dit is een vrijwillige uitnodiging voor Franse conversatietafels.” | `negeren` |
| W5-13 | `werkboek fout` | “De mail legt een fout in een digitaal werkboek uit en vermeldt een mogelijke oplossing.” | `lezen` |
| W5-14 | `TrainTool` | “De mail legt uit hoe ik TrainTool installeer, open of een module start.” | `doen` |
| W5-15 | `inschrijving AI-masterclass` | “Mijn inschrijving voor de AI-masterclass op [datum] wordt bevestigd.” | `lezen` |
| W5-16 | `praktische instructie` | “De mail bevat één korte praktische instructie die ik moet uitvoeren.” | `doen` |
| W5-17 | `deadline` | “De mail verwijst naar een deadline, maar de datum ontbreekt of is onduidelijk.” | `lezen` |
| W5-18 | `moet ik` | “Het is niet duidelijk of ik zelf actie moet ondernemen.” | `lezen` |
| W5-19 | `tegenstrijdig opdracht` | “De mail bevat twee verschillende instructies of deadlines voor dezelfde opdracht.” | `doen` |
| W5-20 | `onduidelijk` | “De afzender of bedoeling is onvoldoende duidelijk om betrouwbare actie af te leiden.” | `negeren` |

## Wat je per mail invult

Gebruik exact dit blok voor elke input:

```text
ID: W5-01
Onderwerp: [zonder naam of persoonlijk nummer]
Datum: [datum of maand]
Type: [school / werk / administratie / uitnodiging]
Samenvatting: [één zin volgens de tabel]
Verwacht label: [doen / lezen / negeren / herhaling]
Reden: [één korte reden]
Tooluitkomst: nog niet gemeten
Juist?: nog niet gemeten
```

## Daarna meten

Pas wanneer alle twintig blokken ingevuld zijn, voer je de samenvattingen één
voor één in bij v3. Gebruik telkens dezelfde prompt en een nieuwe chat of verse
run. Noteer alleen het JSON-label van de tool bij `Tooluitkomst`. Vergelijk het
met `Verwacht label` en zet bij `Juist?` `ja` of `nee`.

Score: tel het aantal `ja` en schrijf bijvoorbeeld `16/20`. Noteer daarnaast
welke ID's fout waren en waarom jouw verwachte label achteraf misschien te
streng of te onzeker was.
