# Overdracht — Build leveringsassistent

## Doel

Een chatassistent op de website van een Ford-garage beantwoordt vragen over de verwachte aankomst van een bestelde wagen.

## Gespreksverloop

1. De klant stelt een vraag, bijvoorbeeld: “Wanneer komt mijn wagen aan?”
2. De assistent vraagt: “Mag ik uw bestelbonnummer van vijf cijfers, alstublieft?”
3. Daarna vraagt hij naar de naam waarop de wagen besteld is.
4. Bij een overeenkomst in de gegevens geeft de assistent de verwachte aankomstdatum bij de garage.

Een bestelbonnummer bestaat uit precies vijf cijfers.

## Verplichte uitleg bij een bekende aankomstdatum

- Het is een verwachte aankomst bij de garage, geen leverings- of afhaaldatum.
- De verkoper neemt contact op om een datum voor de levering aan de klant vast te leggen.
- De uiteindelijke planning hangt onder meer af van eventuele ombouw, reiniging, nummerplaten en papieren.
- De assistent berekent nooit zelf een afhaaldatum of voorbereidingstijd.

## Gegevens

De assistent leest `build/data/bestellingen.xlsx`. De garage kan later elke week hetzelfde Excelbestand bijwerken; de assistent leest de nieuwste versie bij de volgende klantvraag.

Vereiste Excelkolommen:

- Bestelbonnummer
- Naam
- Wagen
- Status
- Verwachte aankomst

Extra kolommen in de fictieve demo: Ombouw, Opmerking ombouw en Laatst bijgewerkt. De volledige uitleg staat in `build/data/kolommen.md`.

Alle huidige gegevens zijn fictief. Het voorbeeldbestand bevat vijf verzonnen bestellingen.

## Huidige bestanden

- `build/server.mjs` — lokale server en gespreklogica
- `build/public/index.html` — website
- `build/orders.mjs` — bestelling zoeken en vijfcijferige nummers controleren
- `build/notices.mjs` — vaste uitleg na een bekende aankomstdatum
- `build/orders.test.mjs` — automatische controles
- `build/test-set.md` — Simon vult hier vooraf zelf de juiste antwoorden in
- `build/log.md` — versiegeschiedenis
- `build/taak.md` — afbakening van de Build

## Starten en testen

```sh
cd build
npm start
```

Open daarna `http://localhost:3000`.

Zonder API-sleutel draait de website in een duidelijke demomodus met fictieve gegevens. Voor een echte AI-versie is later een `.env`-bestand met API-sleutel nodig. Zet nooit een sleutel in Git.

```sh
npm test
```

De vijf bestaande controles slagen.

## Volgende stappen

1. Simon bepaalt voor de testset vooraf de juiste antwoorden op zijn klantvragen.
2. De klantstroom wordt getest met de fictieve Excelgegevens.
3. Later: een echte AI-API instellen en vervolgens opnieuw meten met minstens tien testgevallen.
4. Voor echt gebruik: veilige klantcontrole en een veilige, actuele gegevensbron uit het Ford-programma uitwerken.
