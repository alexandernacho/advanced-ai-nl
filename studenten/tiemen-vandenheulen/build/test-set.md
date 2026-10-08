# Testset — Review-sorteerder voor evenementen

De juiste antwoorden en redenen zijn vooraf gekozen, vóórdat de tool wordt getest.

| Nr. | Review | Juiste labels | Waarom? | Run 1 | Run 2 |
|---|---|---|---|---|---|
| 1 | Leuke sfeer en alles was goed geregeld. We hebben ons de hele avond prima vermaakt. | organisatie, sfeer | De review zegt dat alles goed geregeld was en benoemt expliciet de leuke sfeer. | organisatie, sfeer — juist | organisatie, sfeer — juist |
| 2 | Fijn evenement met een goede mix van activiteiten. De wachtrij bij de ingang duurde wel even. | organisatie, wachttijden | Organisatie omdat er een goede mix is van activiteiten, en wachttijden omdat de wachtrij aan de ingang even duurde. | organisatie, sfeer, wachttijden — fout: `sfeer` extra | organisatie, wachttijden — juist |
| 3 | Gezellige dag gehad! Vooral de optredens maakten het voor mij de moeite waard. | sfeer | De bezoeker zegt dat het gezellig was. | sfeer — juist | sfeer — juist |
| 4 | Goed georganiseerd en vriendelijk personeel. Ik kom volgend jaar graag weer. | organisatie | De review zegt dat het goed georganiseerd is en noemt het personeel. | organisatie — juist | organisatie — juist |
| 5 | Leuke locatie en genoeg te doen. Het was op sommige momenten wel erg druk. | locatie | De bezoeker noemt de locatie expliciet leuk. Drukte krijgt in deze versie geen apart label. | organisatie, locatie — fout: `organisatie` extra | organisatie, locatie — fout: `organisatie` extra |
