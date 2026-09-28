# WF2-069 - Date e valori verificati

Tabella prodotta da `source/verifica_date_valori.py` (festivita' nazionali incluse).
Data di riferimento del caso: 20 settembre 2027.

| Milestone | Data o valore | Calcolo | Fonte | Nota |
|---|---|---|---|---|
| fatturato Italia complessivo | EUR 613 milioni | 420 + 92 + 101 | doc. 02 | - |
| soglia complessiva superata | si | EUR 613 milioni contro EUR 595 milioni | 02_reference_pack.md | - |
| soglia individuale superata da almeno due imprese | si | Orizzonte EUR 420 milioni e Biancospino EUR 92 milioni, entrambe oltre EUR 36 milioni | doc. 02 | - |
| signing | 15 settembre 2027 (mercoledi) | dato di fascicolo | doc. 01 | - |
| completezza del filing | 4 ottobre 2027 (lunedi) | dato di fascicolo: quote di mercato disponibili | doc. 04 | - |
| presidio iniziale di trenta giorni | non calcolabile alla data del fascicolo | il termine decorre dal ricevimento della notifica; la ricevuta AGCM non esiste perche' il filing non e' stato depositato | 02_reference_pack.md e doc. 04 | - |
| long-stop date | 15 dicembre 2027 (mercoledi) | dato di fascicolo | doc. 04 | - |

## Calcoli dichiarati nella challenge map

- `EUR 420m + 92m + 101m = EUR 613m`
- `EUR 613m > EUR 595m`
- `Orizzonte e Biancospino > EUR 36m`

