# Taak — velden uit het KID van een ETF halen

## De vijf regels

1. **De taak:** uit het KID (essentiële-informatiedocument) van een ETF acht vaste velden halen, met de bron erbij.
2. **Wat erin gaat:** één KID van één ETF, als tekst of PDF. De testset bestaat uit tien KID's, waarvan minstens drie lastig zijn (andere taal, oudere opmaak, een risico-indicator die een plaatje is).
3. **Wat eruit komt:** acht velden, elk met de zin of tabelregel uit het KID waar het vandaan komt:
   - risico-indicator (1 tot 7)
   - aanbevolen bewaartermijn
   - lopende kosten per jaar (%)
   - instapkosten (%)
   - uitstapkosten (%)
   - gevolgde index (alleen de naam)
   - uitkerend of accumulerend
   - ongunstig scenario na de aanbevolen bewaartermijn (bedrag in euro en gemiddeld rendement per jaar in %)

   **Uitweg:** staat een veld er niet in, of kan de tool het niet met zekerheid lezen, dan zegt hij "niet vermeld". Hij gokt niet.
4. **De soort AI:** een taalmodel, want het is tekst in en gestructureerde velden uit. Filteren en rangschikken van ETF's op mijn eigen criteria is rekenwerk op de velden, geen AI, en komt later.
5. **Hoe check ik of een antwoord juist is:** ik lees het veld zelf in het KID en schrijf het juiste antwoord op vóór de tool draait. Een beleggingsplatform of nieuwsartikel is hooguit een wegwijzer, nooit de bron.

## Einddoel
Een tool voor mezelf: ik geef mijn filters (kosten, risico, bewaartermijn) en krijg de ETF's die er het dichtst bij liggen. Geen aanbeveling, ik beslis zelf. Sector komt later, want die staat niet als vast veld in het KID. De Build is stap 1: als de velden niet kloppen, klopt het filteren ook niet.

## Waarom ik van taak veranderd ben
Eerst wilde ik velden uit persberichten van Amerikaanse bedrijven halen (omzet, nettowinst, vrije kasstroom, schulden, rentelasten). De persberichten zoeken en de 25 juiste antwoorden opschrijven kostte te veel tijd. Het KID is compact en heeft altijd dezelfde indeling. Om het niet te makkelijk te maken, kies ik meer en lastigere velden en drie lastige KID's.

## Vijf inputideeën
Echte KID's, zelf te zoeken. Het juiste antwoord schrijf ik zelf in `build/test-set.md`.

1.
2.
3.
4.
5.
