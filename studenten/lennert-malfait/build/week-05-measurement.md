# Week 5 — meting op set v2 (30 inputs)

De menselijke antwoorden zijn vooraf vastgelegd. De oude T01–T10 bleven inhoudelijk ongewijzigd. T11–T30 zijn gebaseerd op de gecontroleerde Outlook-onderwerpen en geanonimiseerde snippets. Daarna is één run van v3 op alle 30 uitgevoerd.

| ID | Mens | Classifier v3 | Match |
| --- | --- | --- | --- |
| T01 | lezen | lezen | ja |
| T02 | herhaling | herhaling | ja |
| T03 | doen | doen | ja |
| T04 | negeren | negeren | ja |
| T05 | lezen | lezen | ja |
| T06 | doen | doen | ja |
| T07 | lezen | lezen | ja |
| T08 | negeren | lezen | nee |
| T09 | negeren | lezen | nee |
| T10 | herhaling | herhaling | ja |
| T11 | doen | doen | ja |
| T12 | lezen | doen | nee |
| T13 | herhaling | herhaling | ja |
| T14 | doen | lezen | nee |
| T15 | lezen | lezen | ja |
| T16 | lezen | lezen | ja |
| T17 | doen | lezen | nee |
| T18 | negeren | lezen | nee |
| T19 | lezen | lezen | ja |
| T20 | doen | doen | ja |
| T21 | lezen | negeren | nee |
| T22 | doen | lezen | nee |
| T23 | negeren | lezen | nee |
| T24 | lezen | negeren | nee |
| T25 | lezen | lezen | ja |
| T26 | negeren | lezen | nee |
| T27 | negeren | negeren | ja |
| T28 | lezen | lezen | ja |
| T29 | negeren | negeren | ja |
| T30 | negeren | negeren | ja |

**Resultaat: 19/30 = 63.3% (set v2, 1 run).**

De nieuwe inputs maken de contextafhankelijkheid zichtbaar: de classifier kiest bij meerdere berichten `lezen`, terwijl mijn persoonlijke context bepaalt dat ik moet handelen of de mail kan negeren.
