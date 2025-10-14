# Python och Maskininlärning

### Uppgift:
Maskininlärningsprojekt från Data till Web-API
Denna uppgift syftar till att testa din förmåga att självständigt genomföra ett komplett maskininlärningsprojekt, från dataanalys och modellträning till driftsättning via ett webb-API. Du ska demonstrera färdigheter i Python, datahantering, modellering och grundläggande webbtjänstutveckling.

---
### Projekt
Mitt projekt använder maskininlärning för att förutsäga vilken art en pingvin är baserat på fysiska egenskaper. Genom att träna en model på ett dataset med mätningar hittas mönster som skiljer arterna åt, och som i detta fall är näbblängd, vinglängd och kroppsvikt



### JSON request
````json
{
    "bill_length_mm": 46,
    "flipper_length_mm": 190,
    "body_mass_g": 4000

}
````

| COMMAND | OPERATION | ENDPOINT |
|---|---|---|
| POST | Skapa en pingvin och får tillbaka svar om art | /penguins |

---

### Exempel på pingviner
En lat hund för att lättare testa dom olika pingvinerna

| Art | Näbblängd | Vinglängd | Kroppsvikt |
|---|---|---|---|
| Gentoo | 47 - 52 mm| 205 - 220 mm| 4500 - 5500 g|
| Chinstrap |46 - 50 mm| 180 - 200 mm | 3300 - 4000 g|
| Adelie | 36 - 39 mm| 180 - 200 mm| 3700 - 4500 g|