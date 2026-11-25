# Week 6: Sporza wel, ProCyclingStats niet

## Mijn live query
Mijn vraag: "Wat zijn de beste 12 renners die ik kan samenstellen voor 100 miljoen in de Sporza Wielermanager?"

| | Eigen AI 1 (Claude) | Eigen AI 2 (Claude) | Google AI-modus |
|---|---|---|---|
| Antwoord | Geen ploeg: er loopt geen spel en de prijzen zijn nog niet bekend. Legt de spelvormen uit. | Zelfde weigering, met prijzen en puntenpakkers van 2026. | Geen ploeg, wel een strategie: kopmannen, goedkope renners, parcours. |
| Pagina's die de AI las | alleen sporza.be | alleen sporza.be | wielermanager.sporza.be, sporza.be, pouletips.nl, voorjaarsklassiekers.be, deleadout.com (forum) |
| Genoemde bronnen | Sporza | Sporza | Sporza, Pouletips, Voorjaarsklassiekers.be, De Lead-out |

Een kenner zou ook Sporza noemen, maar ook ProCyclingStats, en dat had er moeten staan. Run 1 en run 2 lazen dezelfde bron en gaven bijna hetzelfde antwoord. Google las vooral tipsites en een forum en gaf een heel ander antwoord. Geen enkele bron ging over de vorm of blessures van renners, en dat is net wat mijn tool doet.

Pouletips werd wel genoemd en ProCyclingStats niet, omdat Pouletips een pagina heeft die bijna letterlijk mijn vraag beantwoordt ("beste renners voor je Sporza Wielermanager-ploeg"), terwijl ProCyclingStats alleen cijfers en tabellen heeft die spelers zelf moeten omzetten.

## Kan AI dit bedrijf vinden?
Ik deed een GEO-audit van ProCyclingStats, de bron die in mijn Live Query ontbrak.

| # | Criterium | Score | Bewijs |
|---|---|---:|---|
| 1 | Gestructureerde data | 0 | https://www.procyclingstats.com/rider/tadej-pogacar op validator.schema.org: geen items gevonden. |
| 2 | Leesbaar voor AI | 1 | Vooral tabellen met uitslagen, ranglijsten en startlijsten, bijna geen antwoorden in gewone zinnen. |
| 3 | Vermeldingen door anderen | 2 | Veel gebruikt door spelers (een Google Sheet op De Lead-out, een scraper op GitHub, een Python-pakket), maar geen recensies of persartikels. |
| 4 | Echt genoemd in AI-antwoorden | 0 | In mijn Live Query las of noemde geen enkele run ProCyclingStats. |
| 5 | Autoriteit | 3 | Databank sinds 2013, met de claim "99,9% juist" voor UCI-uitslagen; volgens Similarweb nummer 2 in de categorie fietsen. |
| 6 | Zoeken op de merknaam | 3 | Wie "ProCyclingStats" zoekt, vindt meteen de site. |
| | **Totaal** | **9 op 18** | **Marginaal** |

ProCyclingStats is sterk op wat het zelf heeft: cijfers, autoriteit en een bekende naam. Het is zwak op hoe een AI het kan lezen en op wat anderen erover schrijven. Mijn tactiek: ProCyclingStats moet naast zijn tabellen korte pagina's in gewone zinnen maken die vragen van spelers beantwoorden, bijvoorbeeld "beste renners voor de Sporza Wielermanager", zodat een AI die pagina's kan lezen en citeren.

## Mijn tool leest een bron
Mijn tool kreeg één bron: een vormoverzicht van tien renners, in mijn eigen woorden, met per renner de datum van het recentste bericht en een link naar de bron (build/bronnen/vormoverzicht.md). Ik koos eigen notities in plaats van volledige artikels, omdat mijn map openbaar is op GitHub. Mijn tool moet bij elk antwoord het kopje en de datum uit het document noemen, en eerlijk zeggen als een renner er niet in staat.

Mijn score: 5 op 5 juist (n = 5, 1 run, Sonnet 5.5). Bij B05 vroeg ik naar Wout van Aert, die niet in het document staat. Het model kent hem zeker, maar zei toch "staat niet in het document". Zo weet ik dat het antwoord uit het document kwam, en niet uit wat het model al wist.

Er ging niets fout. Mijn vijf vragen waren wel eenvoudig. Een lastiger geval is Pogačar: daar zegt de dokter dat hij kan koersen, maar wil de ploeg hem nog niet laten starten. Dat test ik volgende keer.
