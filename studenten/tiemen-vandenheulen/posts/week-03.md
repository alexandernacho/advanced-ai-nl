# Week 3 — Van fout naar betere prompt

Ik testte hoe AI bezoekersreviews van evenementen kan ordenen in vaste categorieën. Een review over beveiliging of een onveilige situatie hoort bijvoorbeeld bij de categorie `veiligheid`.

Bij een Engelse review over sfeer en geluidskwaliteit gaf mijn eerste prompt zowel `sfeer` als `andere` terug. Dat was niet correct: de review hoorde bij `sfeer`; geluid heeft gewoon geen aparte categorie in mijn tool.

Daarom maakte ik een tweede versie van mijn prompt. Ik voegde expliciet toe dat `andere` nooit samen met een ander label mag voorkomen. Daarna testte ik dezelfde review opnieuw. De tool gaf toen alleen `sfeer` terug, zoals verwacht.
