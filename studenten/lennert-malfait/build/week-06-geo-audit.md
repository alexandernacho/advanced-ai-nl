# Week 6 — GEO-audit

**Bedrijf:** Fyxer
**Geteste URL:** https://www.fyxer.com/ai-email-assistants/outlook

| # | Criterium | Score (0–3) | Bewijs |
|---|---|---:|---|
| 1 | Gestructureerde data (URL en gedetecteerde namen) | 3 | In de HTML van de geteste URL vond ik JSON-LD met de `@type`-namen `FAQPage`, `BreadcrumbList`, `Organization`, `SoftwareApplication` en `Offer`. Handmatig in de broncode gecontroleerd; geen externe validator-run. |
| 2 | Leesbaar voor AI | 3 | De pagina noemt expliciet Outlook, beschrijft inboxorganisatie en e-maildrafts en bevat concrete FAQ-antwoorden. De kop “The AI email assistant for Outlook” maakt het product en platform direct duidelijk. |
| 3 | Vermeldingen door anderen | 3 | Fyxer komt voor in onafhankelijke vergelijkings-/reviewpagina's, waaronder [Command Mail](https://commandmail.app/en/compare/best-ai-email-assistant-outlook), [GetInboxZero](https://www.getinboxzero.com/blog/post/best-ai-email-assistants) en [Pidgy](https://www.pidgy-ai.com/fyxer-ai-review). Pagina's kunnen commerciële belangen hebben. |
| 4 | Genoemd in AI-antwoorden (Live Query) | 1 | In de twee ChatGPT-zoekruns was Fyxer zichtbaar in gevonden vergelijkingsbronnen; het was niet de hoofdconclusie. Google AI Mode noemde Fyxer niet. Zie [Live Query-log](week-06-live-query.md). |
| 5 | Autoriteit | 2 | [OpenAI's Fyxer-klantverhaal](https://openai.com/index/fyxer/) en [Fyxers perspagina](https://www.fyxer.com/press) geven zichtbaarheid en bedrijfsinformatie. De prestatiecijfers op die pagina's zijn deels bedrijfsclaims; dit is geen onafhankelijke productevaluatie. |
| 6 | Zoeken op de merknaam | 3 | Een zoekopdracht op “Fyxer AI” leverde de officiële product- en perspagina's, een OpenAI-klantverhaal en de [Britse bedrijfsregistratie](https://find-and-update.company-information.service.gov.uk/company/15189973) op. |

**Totaal:** 15/18
**Eerste tactiek om de vindbaarheid te verbeteren:** publiceer een onafhankelijke, goed citeerbare vergelijking van Outlook-triage met concrete use-cases en beperkingen. De eigen productpagina en structured data zijn al duidelijk; de zichtbare AI-antwoorden blijven sterk gericht op Microsofts eigen oplossing.
