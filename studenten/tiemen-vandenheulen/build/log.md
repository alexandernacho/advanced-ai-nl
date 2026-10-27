# Logboek

## Nieuwe testrun — 20 oktober 2026

- **Versie:** v2
- **Resultaat:** 8 van 10 juist (n = 10, 1 run)
- **Fouten:** bij reviews 2 en 5 voegde de tool een extra label toe (F1). Beide reviews zijn dubbelzinnig: “fijn evenement” kan als sfeer gelezen worden en “genoeg te doen” als organisatie.
- **Volgende stap:** de huidige fouten zijn voorlopig aanvaardbaar, omdat ik elke uitkomst zelf nakijk voordat ik de labels gebruik.

Elke run, elk resultaat en elke wijziging komt hier. Wis geen fouten.

| Datum | Versie | Wat ik deed | Resultaat | Fout of opvallend | Volgende stap |
|---|---|---|---|---|---|
| 7 oktober 2026 | v1 | Buurtest met reviews 1, 8 en 9 | 2 van 3 labels kwamen volledig overeen | Bij review 1 koos de buur alleen `organisatie`; de testset verwacht `organisatie, sfeer`. | Nagaan waarom `sfeer` werd overgeslagen. |
| 7 oktober 2026 | v1 | Test met review 2 | Labels kwamen volledig overeen | `organisatie, wachttijden` was juist. | Geen wijziging nodig voor deze review. |
| 7 oktober 2026 | v1 | Test met review 8 (Engels) | Niet volledig juist | Tool gaf `sfeer, andere`; verwacht was alleen `sfeer`. | In v2 verduidelijken: gebruik `andere` nooit samen met een ander label. |
| 7 oktober 2026 | v2 | Review 8 opnieuw getest | Labels kwamen volledig overeen | De tool gaf alleen `sfeer`. | V2 werkt voor deze fout. |
| 27 oktober 2026 | set v2 | Eén run op T01–T30 met de huidige prompt | 25 op 30 juist (n = 30, 1 run) | Vijf F1-fouten: telkens een extra label bij T05, T12, T16, T25 of T26. | Niet bijsturen op T11–T30; in week 6 vergelijken met een nieuwe run op dezelfde set. |
| 27 oktober 2026 | set v2 | Openlijke correctie van verwachte antwoorden T12 en T26 | Herbeoordeeld: 27 op 30 juist | T12 was eerst alleen `prijs`; ook `catering` hoort erbij omdat de review eten benoemt. T26 was eerst alleen `veiligheid`; ook `organisatie` hoort erbij omdat personeel onder organisatie valt. | Deze correcties blijven zichtbaar; volgende run gebruikt de volledige antwoorden. |
