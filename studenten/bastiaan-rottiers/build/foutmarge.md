# Foutmarge, 27 oktober 2026

Testset: **set v1**, vaste deelset T06–T10 uit de oorspronkelijke tien. Deze scorevergelijking blijft apart van de eenmalige controlerun op set v2; de sets hebben verschillende inputs en scores zijn niet rechtstreeks vergelijkbaar.

Model: **GPT-6.1 Sol (`gpt-6.1-sol`)**, effort **medium**. n = **5**: T06, T07, T08, T09 en T10. Drie rondes per versie; iedere input in een nieuwe, aparte sessie. Dezelfde inputs en bijlagen voor beide versies. In totaal 30 antwoorden.

| Versie | Run 1 | Run 2 | Run 3 | Foutmarge (min–max) |
|---|---:|---:|---:|---:|
| v6, gereconstrueerd | 2/5 | 2/5 | 3/5 | 2–3/5 |
| v7 | 3/5 | 3/5 | 4/5 | 3–4/5 |

Deze scores zijn beoordeeld met de bestaande testset en de al in week 4 gehanteerde statusregel voor T10. De eigen controle van twee antwoorden staat in `controle-week-05.md`.

## Claim en conclusie

Te toetsen claim uit het logboek van 20 oktober, na de v7-hertest van T10: **“De gerichte statusregel lost de fout op.”** De week-4-post beschrijft gerichte verbeteringen, maar bevat geen zuivere scorevergelijking van v6 en v7 op dezelfde inputs.

**Algemene verbeterclaim: ingetrokken als bewezen verbetering.** De bereiken 2–3 en 3–4 overlappen bij 3/5. De laagste nieuwe score ligt niet hoger dan de hoogste oude score. Deze beperkte test bewijst dus geen hogere totaalkwaliteit.

Bij T10 is de gewenste eindstatus `nog in te plannen` wel vaker aanwezig: v6 1/3, v7 3/3. Dat is een waarneming op één input, geen bewijs dat de statusregel altijd werkt.

## Beoordeling per antwoord

Juist betekent dat het antwoord de vooraf vastgelegde inhoud behoudt, geen onterechte bronfeiten toevoegt en aan de reeds gebruikte statusregel voldoet. Bij T09 en T10 worden de documenten als bron gebruikt; suggesties voor volgende stappen zijn geen reeds ingevulde feiten.

| Input | v6 R1 | v6 R2 | v6 R3 | v7 R1 | v7 R2 | v7 R3 | Reden |
|---|---|---|---|---|---|---|---|
| T06 | juist | juist | juist | juist | juist | juist | Ieder groepslid, minimaal twee events, kostenoverleg, foto met coach-tag, deadline en onzekere inleverwijze behouden. |
| T07 | fout | fout | fout | fout | fout | juist | De eerste vijf antwoorden noemen de deadline onzeker. Het verwachte antwoord legt 5 oktober 2026 vast. v7 R3 neemt die datum correct over en noemt invullen en indienen. |
| T08 | fout | fout | fout | fout | fout | fout | De antwoorden noemen BMC, terwijl het bestaande verwachte antwoord Sustainable Business Canvas vereist. Zie de beperking hieronder; dit is geen zuiver bewijs van een modelfout. Sommige antwoorden leiden ook “opladen” af uit de titel. |
| T09 | juist | juist | juist | juist | juist | juist | Kort overzicht per hoofdstuk met een toegelaten status en volgende stap, gebaseerd op de bijlagen. De eindstatus is bij v6 onzeker en bij v7 nog in te plannen; de vooraf vastgelegde inhoud van T09 schrijft die eindstatus niet afzonderlijk voor. |
| T10 | fout | fout | juist | juist | juist | juist | De onderdelen krijgen een status en volgende stap. v6 R1 mist de eindstatus; v6 R2 eindigt met onzeker. v6 R3 en alle v7-antwoorden eindigen met nog in te plannen. Deze statusvoorwaarde werd in week 4 al gebruikt om T10 v6 fout te rekenen. |

## Grenzen van de meting

- **v6 is gereconstrueerd.** Git bewaart de tussenversie niet afzonderlijk. Uit v7 is uitsluitend de gedocumenteerde extra regel over de eindstatus bij voortgangsvergelijkingen verwijderd; de kop noemt de reconstructie. Zie `prompt-v6-gereconstrueerd.md` en `prompt-v7.md`.
- **T08 is niet eenduidig.** De input spreekt over een Business Model Canvas en noemt een afgekorte bijlagenaam zonder inhoud. Het verwachte antwoord vereist een Sustainable Business Canvas. In week 4 werd “BMC” toch geaccepteerd. Nu is de bestaande antwoordkolom strikt aangehouden. Geen verwacht antwoord, input of historisch oordeel is achteraf gewijzigd. Vóór een toekomstige nieuwe testreeks moet deze tegenstrijdigheid worden opgelost.
- **T10 heeft een extra historisch criterium.** De antwoordkolom noemt alleen de inhoud per bouwsteen; het week-4-logboek en de prompt vereisen ook de eindstatus. Zonder die al bestaande statuscontrole zou v6 3/5, 3/5, 3/5 scoren; v7 blijft 3/5, 3/5, 4/5. De bereiken overlappen ook dan. De conclusie verandert dus niet.
- **De bron van T10 bevat elf blokken:** de negen gewone bouwstenen plus Eco-Social Costs en Eco-Social Benefits. Alle elf worden meegenomen; de testset spreekt nog van negen.
- **Historische effort onbekend.** Week 4 vermeldt Sol, maar bewaart het effortniveau niet. Medium is voor deze nieuwe vergelijking vastgezet.
- Dit min–max-bereik beschrijft drie geobserveerde scores. Het is geen statistisch betrouwbaarheidsinterval en garandeert geen bereik voor volgende runs. Met vijf inputs verandert één oordeel de score al met 20 procentpunten.

## Uitvoering en controleerbaarheid

De sessies krijgen uitsluitend de prompt en één input, inclusief de geëxtraheerde documenttekst bij T09 en T10. De verwachte antwoorden worden niet meegestuurd. Shelltools, apps, multi-agentfunctionaliteit en webzoeken zijn uitgeschakeld; er zijn geen tools aangeroepen. De standaard Codex-systeeminstructies blijven onderdeel van de CLI.

Ruwe uitvoer, aangeleverde input, tokens en tijdsduur staan lokaal in `week-05-lokaal/`, buiten git. `week-05-test.ps1` bevat de reproduceerbare werkwijze. De SHA-256-controle bevestigt dat `test-set.md` tijdens de runs niet is veranderd.

## Zelf nakijken

De eigen controle van T07 v7 R3 en T10 v7 R3 is op 27 oktober genoteerd in `controle-week-05.md`. Bij T07 is de datum praktisch voldoende; de vereiste is een ingevuld Teamcharter. Canvas is als inleverplek bevestigd, maar stond niet expliciet in de oorspronkelijke input. Bij T10 is bevestigd dat “al ingevuld” klopt voor dit oudere document. De volgende stappen zijn niet afzonderlijk nagekeken. Deze feedback wijzigt geen verwacht antwoord of score van de uitgevoerde reeks; ze wordt vóór een toekomstige testreeks verwerkt.
