# Week 2 — Een tool die ETF-documenten leest

## Wat bouw ik?
Ik bouw een tool die het KID van één ETF leest en er acht vaste velden uit haalt (risico, bewaartermijn, kosten, index, uitkerend of accumulerend, ongunstig scenario), elk met de zin uit het KID erbij. Later wil ik ETF's daarmee vergelijken op mijn eigen behoeften, zoals kosten en risico, en ook op sector en index. Een aanbeveling geeft de tool niet.

## Waarom een taalmodel?
Een taalmodel helpt me om snel te zien of een ETF iets voor mij is. Het bespaart me tijd, want ik moet geen saaie documenten meer lezen. Ik heb geen programma's gevonden die dit al doen. In mijn test ging het mis bij de lopende kosten: als het KID die opsplitst in beheerskosten en transactiekosten, telde de tool ze niet op. Dat is geen reden om het taalmodel te laten vallen. Ik pas de prompt aan in een volgende versie.

## Eén testinput
Input T04: het KID van L&G Artificial Intelligence, in het Frans. Ik schreef vooraf op dat de lopende kosten 0,53% zijn: 0,49% beheerskosten plus 0,04% transactiekosten. De tool zei in beide runs 0.49% en noemde de 0.04% er alleen naast. De andere zeven velden klopten, met één nuance: bij het ongunstige scenario schreef de tool "13,600 USD" en "6.3%", zoals het KID dat in Engelse notatie doet. Dat is dezelfde waarde als mijn 13.600 USD en 6,3%, maar in het Nederlands lees je "13,600" als dertien komma zes. Wat ik leerde: twee regels in mijn prompt botsten ("reken niets uit" en "geef de lopende kosten per jaar"). De tool koos in alle zes de runs van T02, T03 en T04 dezelfde regel, het was dus geen toeval. In versie 2 zeg ik erbij wat hij moet doen als een KID de kosten opsplitst.
