# Week 6: Waarom AI DB Hardwoods niet vindt

DB Hardwoods is het bedrijf van mijn vader en ik help er mee. Daarom ken ik de markt, maar ik heb de audit gedaan zoals een buitenstaander: alleen met wat online te vinden is.

## Mijn live query

**Vraag (letterlijk):** "Waar kan ik massief rubberwood kopen voor trappen in België?"

| Run | Zoekopdrachten van de AI | Pagina's die de AI las | Genoemde bedrijven |
|---|---|---|---|
| Eigen AI 1 | <nog in te vullen> | Vooral bedrijfssites met productpagina's en prijzen. Bobex (vergelijkingssite). | Hanssens Hout, BCFV, Gamma, Brico, NewStairs, Bobex |
| Eigen AI 2 | <nog in te vullen> | Vooral bedrijfssites. Bobex (vergelijkingssite). | Hanssens Hout, BCFV, Martens Hout, NewStairs, Bobex |
| Google AI-modus | <nog in te vullen> | 13 bronnen, meeste bedrijfssites, waaronder de rubberwood-pagina van DB Hardwoods. | Martens Hout, Ecohout, BCFV, Cras Woodshops, Hanssens Hout, Eurabo, Borra Trappen, Qualitrap, Trappen Verschaeve, TrapDirect |

Reviews, fora en persartikels werden in geen enkele run gelezen.

- **Zou een kenner van die markt dezelfde noemen?** <jouw antwoord>
- **Wie had er moeten staan?** DB Hardwoods. Het stond in geen enkele run.
- **Run 2 en Google: dezelfde bedrijven?** Alleen Hanssens Hout, BCFV en Martens Hout kwamen in allebei voor.

**Waarom staat het ene bedrijf wel, en het andere niet?** <één zin, zelf geschreven>

## GEO-audit: DB Hardwoods

| # | Criterium | Score | Bewijs |
|---|---|---|---|
| 1 | Gestructureerde data | 0 | In de broncode van de rubberwood-pagina staat geen ld+json of schema.org, en ook geen meta-description. De pagina is gemaakt met Microsoft Office (codes zoals "MsoNormal") en gebruikt nog de oude codering windows-1252. |
| 2 | Leesbaar voor AI | 1 | De maten en diktes staan in een grote tabel, maar er staat geen prijs op de pagina. Er is ook geen korte zin die zegt wat DB Hardwoods verkoopt en aan wie. De voorraad spreekt zichzelf tegen: eerst "meer dan 5000 m³", verderop "3500 m³". |
| 3 | Vermeldingen door anderen | 1 | 17 Google-reviews, tegenover 474 bij Hanssens Hout. Wel vermeld op bsearch.be onder "trap rubberwood", niet op Bobex. Geen persartikels gevonden. |
| 4 | Echt genoemd in AI-antwoorden | 0 | In geen van de drie runs genoemd. Google AI-modus las de rubberwood-pagina wel als bron, maar noemde DB Hardwoods niet bij de houthandels. |
| 5 | Autoriteit | 2 | Importeert rubberwood sinds 1995 en heeft sinds 2001 een eigen productie in Zuidoost-Azië. In 2013 slaagde een brandtest bij Warrington Fire in Gent, waardoor de panelen gebruikt mogen worden voor DF 30-deuren van De Coene Products en Theuma. Geen 3, omdat die erkenning alleen op de eigen site staat. |
| 6 | Zoeken op de merknaam | 2 | Wie "DB Hardwoods" typt in Google, krijgt een juiste AI-samenvatting, met rubberwood panelen erbij. Claude (incognito) kent het bedrijf alleen via bedrijfsdatabanken, vindt de eigen site niet, noemt geen rubberwood en vraagt of ik een Amerikaans bedrijf met dezelfde naam bedoel. |

**Totaal: 6 op 18, onzichtbaar.**

Google kent DB Hardwoods wel als je de naam typt, maar raadt het niet aan als je gewoon vraagt waar je rubberwood koopt.

**Tactiek:** Zet bovenaan de rubberwood-pagina één duidelijke zin, zoals "DB Hardwoods verkoopt verlijmde rubberwood panelen voor trappen en meubels, uit voorraad in Rollegem-Kapelle." Voeg een richtprijs per m² toe en houd één voorraadcijfer over. Google las de pagina al, maar zag DB Hardwoods niet als verkoper. Deze zin lost dat het snelst op.

## Mijn tool leest een bron
**Document:** build/bronnen/db-hardwoods-rubberwood_advanced_ai_opdracht.md, een kopie van de rubberwood-pagina van DB Hardwoods (https://www.dbhardwoods.com/rubberwoodNL.htm). Ik koos die omdat ik help bij de houthandel van mijn vader en klanten vaak vragen stellen over diktes, maten en trappen. Die antwoorden staan allemaal op deze pagina.

**Score:** 5 op 5.

**Wat opviel:** Bij B05 vroeg ik wat een paneel van 40 mm per m² kost. De tool zei dat de prijs niet in de bron staat en verzon geen bedrag. Dat was de vraag waar ik het meest schrik voor had, want in week 1 verzon Claude nog e-mailadressen. Wel zag ik dat de bron zelf twee verschillende voorraadcijfers geeft (meer dan 5000 m³ en 3500 m³). Een vraag over de voorraad zou de tool dus niet juist kunnen beantwoorden, omdat het document zichzelf tegenspreekt.
