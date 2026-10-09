# Leveringsassistent voor een Ford-garage

Deze eerste versie is een lokale website waarop een klant eerst een vraag stelt. De assistent vraagt daarna om het vijfcijferige bestelbonnummer en de naam op de bestelling. De server zoekt de bestelling op en laat een taalmodel alleen met de gevonden gegevens antwoorden.

De drie bestellingen in `orders.mjs` zijn volledig fictief. Ze zijn enkel bedoeld om de werking te tonen. Een echte versie mag pas gegevens uit het Ford-programma gebruiken nadat de garage heeft bevestigd welke geanonimiseerde gegevens beschikbaar zijn en hoe een klant veilig wordt gecontroleerd.

## Starten

1. Start de website:

   ```sh
   npm start
   ```

2. Open `http://localhost:3000` in je browser.

Zonder API-sleutel draait de website in demomodus. Je kunt dan de volledige klantstroom met fictieve bestelgegevens testen, maar het antwoord is nog geen AI-antwoord. Voor de echte AI-versie kopieer je `.env.example` naar `.env` en zet je eigen OpenAI API-sleutel in `OPENAI_API_KEY`.

Test bijvoorbeeld met bestelbonnummer `10481` en naam `Emma Peeters`. Een bestelbonnummer bestaat uit precies vijf cijfers.

## Wekelijkse Excel-update

De garage werkt elke week hetzelfde Excelbestand bij. Plaats dat bestand op de computer of server waar de assistent draait als `build/data/bestellingen.xlsx`. Bij de volgende klantvraag leest de assistent automatisch de nieuwste versie. Er is geen uploadscherm op de website.

De eerste werkbladpagina van het Excelbestand moet deze kolommen bevatten:

| Bestelbonnummer | Naam | Wagen | Status | Verwachte aankomst |
| --- | --- | --- | --- | --- |
| 12345 | Voorbeeld Klant | Ford Puma | Onderweg naar de garage | 18 oktober 2026 |

Een realistisch fictief voorbeeldbestand staat al lokaal in `data/bestellingen.xlsx`. De volledige kolombeschrijving staat in [data/kolommen.md](data/kolommen.md).

Het Excelbestand staat in `.gitignore` en komt dus niet in Git. De assistent blijft met de vorige gegevens werken wanneer het bestand tijdens het opslaan tijdelijk niet leesbaar is.

## Controleren

```sh
npm test
```

De test controleert dat een bestelling alleen wordt gevonden wanneer zowel bestelbonnummer als naam overeenkomen.

## Grenzen van v1

- De verwachte aankomstdatum bij de garage is geen leverings- of afhaaldatum.
- Bij een bekende aankomstdatum vermeldt de assistent dat de verkoper contact opneemt om de levering verder af te spreken. Ombouw, reiniging, nummerplaten en papieren kunnen de planning beïnvloeden.
- Als een datum nog niet bekend is, moet de assistent dat zeggen en geen datum verzinnen.
- Deze demo gebruikt naam en bestelbonnummer als eenvoudige controle. Dat is nog niet genoeg voor echte klantgegevens.
- Iemand die het Excelbestand kan wijzigen, bepaalt de informatie die de assistent toont. De garage moet daarom de map met dit bestand beperken tot bevoegde medewerkers.
- De API-sleutel blijft in `.env`; dit bestand wordt door Git genegeerd.

## Volgende versie

1. Vraag de garage welke gegevens uit het Ford-programma beschikbaar zijn.
2. Maak een geanonimiseerde testset met echte klantvragen en juiste antwoorden die Simon vooraf invult.
3. Test minstens tien vragen twee keer en noteer fouten in `log.md`.
