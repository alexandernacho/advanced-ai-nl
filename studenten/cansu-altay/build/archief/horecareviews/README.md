# Klachten in horecareviews sorteren — v1

Deze eerste versie werkt met een prompt: instructies die je aan een taalmodel geeft. Je gebruikt hem in ChatGPT of Claude.

## Bestanden

- `taak.md`: wat de tool moet doen.
- `prompt.md`: de eerste instructies voor het model. Lees en controleer deze zelf.
- `log.md`: wat je hebt gedaan, wat eruit kwam en wat je verandert.

## Eén review verwerken

1. Open `prompt.md` en lees het hele bestand.
2. Kopieer de tekst naar een nieuw tijdelijk gesprek in ChatGPT of een incognitogesprek in Claude, zonder web search.
3. Vervang de tekst tussen `<review>` en `</review>` door één publieke horecareview. Verwijder eerst de namen.
4. Verstuur de prompt. Het model hoort één regel met labels terug te geven.
5. Vergelijk het antwoord met de labels die jij vooraf zelf hebt gekozen. Noteer het resultaat in je testset en logboek.

Begin voor elke review een nieuw gesprek. Stuur de juiste antwoorden en de volledige testset niet mee naar het model.

## Eerst zelf controleren

Dit is een eerste voorstel. Controleer vooral de grenzen tussen de categorieën en wanneer `onzeker` moet worden gebruikt. De regels voor klachten buiten de categorieën en voor een combinatie van duidelijke en onduidelijke klachten zijn voorlopige keuzes.

Doe daarna de audit uit week 3: wijs elke regel toe aan een van de zes bouwstenen. Voeg zelf drie tot vijf voorbeelden met jouw juiste labels toe vóór het gedeelte met de review. Herschrijf ook zelf één regel met een **want**.

Er zijn nog geen reviews getest en er is nog geen succespercentage. De echte testinputs, juiste antwoorden en reflecties komen van jou.
