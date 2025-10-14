# Python och Maskininlärning

-----------------

### Uppgift:
Maskininlärningsprojekt från Data till Web-API
Denna uppgift syftar till att testa din förmåga att självständigt genomföra ett komplett maskininlärningsprojekt, från dataanalys och modellträning till driftsättning via ett webb-API. Du ska demonstrera färdigheter i Python, datahantering, modellering och grundläggande webbtjänstutveckling.

---

#### Mitt arbete handlar om Pingviner där jag skapat en modell som räknar ut art beroende på näbb längd, fen längd och kroppsvikt.

| COMMAND | OPERATION | ENDPOINT |
|---|---|---|
| POST | Skapa en pingvin och får tillbaka svar om art | /penguins |

````json
{
    "bill_length_mm": 46,
    "flipper_length_mm": 190,
    "body_mass_g": 4000

}