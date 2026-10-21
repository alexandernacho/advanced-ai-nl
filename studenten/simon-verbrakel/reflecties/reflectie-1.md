# Reflectie 1

## 1. Wat kan mijn tool nu?
Mijn tool leest de kop en de eerste alinea van een nieuwsbericht en geeft één label voor de vraag naar defensiebedrijven, met een korte reden. Hij herkent goed wanneer een bericht niet over defensie gaat, ook als het er op lijkt (zoals een oorlogsgame), en wanneer een land extra wapens koopt. Hij geeft bij dezelfde input meestal twee keer hetzelfde antwoord.

## 2. Wat kan hij niet?
Hij kan niet oordelen als de belangrijke info pas in de tweede alinea staat (T01). Hij twijfelt bij vredesgesprekken zonder akkoord (T08): zelfs met een extra regel gaf hij één keer negatief en één keer onzeker. En hij weet niet wat ik weet: de NAVO-top ging over hogere budgetten, maar dat staat niet in zijn input.

## 3. Welk cijfer bewijst dat?
Met de huidige prompt had de tool 19 van de 20 antwoorden juist (95%), op n = 10 inputs die elk twee keer gedraaid zijn. Vóór ik achteraf het juiste antwoord van T01 aanpaste, was het 17 op 20 (85%). Dat is weinig. T06, T07, T09 en T10 draaiden met de prompt van net vóór de laatste regel. Eén run kost ongeveer €0,0008 met Haiku 5.5 (gemeten met /cost, n = 1).
