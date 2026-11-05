# Week 5: Hoe mijn foutmarge de nettowinst beïnvloedt

## Mijn foutmarge

Ik draaide v1 en v2 elk 3 keer op dezelfde 10 inputs, met Opus 5.5. v1 haalde 6–7 op 10, v2 drie keer 8 op 10.

Laat ik de twee inputs weg waarvoor ik regels schreef, dan scoort v2 niet beter dan v1: v1 6–7, v2 6–6 (n = 8, 3 runs). Mijn claim "bevestigd" is dus ingetrokken.

T08 verraste me: v1 had hem 2 van de 3 keer juist, v2 3 keer fout. Er passen twee labels in.

Bij v3 verander ik één regel per keer, en test ik op een aparte testset.

## Model en effort

Prompt v2, 1 run op dezelfde 10 inputs: Sonnet 5.5 (effort medium) haalde 7 op 10, Haiku 5.5 en Opus 5.5 elk 8 op 10. Eén input verschil bij 1 run valt binnen mijn foutmarge. Mijn gok schreef ik pas na de resultaten op.

Ik kies Haiku 5.5: even goed als Opus, maar voor het team ± € 495 per jaar in plaats van ± € 10.545.

## Mijn value chain, met de foutmarge erin

| Schakel | Laag (6/10) | Basis (8/10) |
|---|---:|---:|
| Winst bij opzoeken, min draaien en nakijken | 2,4 min | 2,4 min |
| Fouten herstellen (% fout × 3 min) | − 1,2 min | − 0,6 min |
| Winst per reactie | 1,2 min | 1,8 min |
| × € 53,85 per uur (€ 60.000 bruto × 1,5) | € 440.700 | € 661.100 |
| − Haiku 5.5 | − € 495 | − € 495 |
| **Netto per jaar** | **± € 440.000** | **± € 660.600** |

Mijn zwakste cijfer is de opzoekwinst (± 2 tot 5 min per reactie): geschat, nooit geklokt. Is die winst maar de helft, dan zakt het netto naar ± € 43.600 (− 93%). Mijn foutmarge laat het netto maar − 33% dalen. Op het werk klok ik 10 reacties zonder en 10 met de tool.

## Mijn dashboard

https://claude.ai/artifact/WvtreLoSPAyPk439U61Gb9

Wat je eerst moet zien: de score van mijn AI-tool bij de NMBS.

## Mijn AI-ismen

> Week 4: "De tool werkt goed bij duidelijke klantenreacties"
> Herschreven: "De tool had 16 op 20 labels juist (n = 10, 2 runs)."

> Week 3: "Dit is een werkpuntje dat in v3 zeker opgelost moet worden."
> Herschreven: "In v3 zeg ik wanneer een veld `nee` is en wanneer `niet vermeld`."

## Mijn testset groeit

Mijn testset groeide van 10 naar 30 inputs (set v2). Ongeveer 10 komen uit het CRM van de NMBS, met verzonnen namen, datums en trajecten. Omdat niet alle klantenreacties even duidelijk, lang of goed onderbouwd zijn, test ik ook met korte, Franse en onzekere reacties.

T27 verraste me het meest. In deze run gokte de tool één keer, bij T27: `ticket te laat gekocht`, ook al zegt de prompt dat hij niet mag gokken. Normaal houdt hij zich altijd aan de regels.

Op set v2 had de tool 25 op 30 labels juist (n = 30, set v2, 1 run), vroeger 8 op 10. De tool blijft dus ongeveer even accuraat. 4 van de 5 fouten gaan over `ticket te laat gekocht`. Die wil ik in v3 oplossen.
