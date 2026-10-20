# Reflectie 1

## 1. Wat kan mijn tool nu?
Mijn tool leest de kop en de eerste alinea van een nieuwsbericht en geeft één label voor de vraag naar defensiebedrijven, met een korte reden. Hij herkent goed wanneer een bericht niet over defensie gaat, ook als het er op lijkt (zoals een oorlogsgame), en wanneer een land extra wapens koopt. Hij geeft bij dezelfde input meestal twee keer hetzelfde antwoord.

## 2. Wat kan hij niet?
Hij kan niet oordelen als de belangrijke info pas in de tweede alinea staat (T01). Hij twijfelt bij vredesgesprekken zonder akkoord (T08): zelfs met een extra regel gaf hij één keer negatief en één keer onzeker. En hij weet niet wat ik weet: de NAVO-top ging over hogere budgetten, maar dat staat niet in zijn input.

## 3. Welk cijfer bewijst dat?
Met de nieuwe prompt had de tool 8 van de 10 antwoorden juist (80%), op n = 5 inputs (T06 tot T10) die elk twee keer gedraaid zijn. Dat is weinig, dus het echte cijfer kan lager liggen: T01 gaf vandaag met dezelfde prompt ook een fout. Eén run kost ongeveer €0,0008 met Haiku 5.5 (gemeten met /cost, n = 1).
