# WF2-066 - Date e valori verificati

Tabella prodotta da `source/verifica_date_valori.py` (festivita' nazionali incluse).
Data di riferimento del caso: 12 aprile 2029.

| Milestone | Data o valore | Calcolo | Fonte | Nota |
|---|---|---|---|---|
| domanda di apertura | 14 dicembre 2028 (giovedi) | dato di fascicolo | doc. 01 | - |
| apertura della liquidazione giudiziale | 20 febbraio 2029 (martedi) | dato di fascicolo | doc. 01 | - |
| distanza bonifico-domanda | 14 giorni | 14 dicembre 2028 - 30 novembre 2028 | doc. 01 e doc. 02 | - |
| bonifico nel semestre anteriore | si | finestra dal 15 giugno 2028 al 14 dicembre 2028 | doc. 02 | - |
| cessione nel semestre anteriore | no | 18 aprile 2028 precede il 15 giugno 2028 | doc. 02 | - |
| cessione nell'anno anteriore | si | finestra dal 14 dicembre 2027 al 14 dicembre 2028 | doc. 02 | - |
| pegno nel semestre anteriore | si | 10 ottobre 2028 dentro la finestra semestrale | doc. 05 | - |
| massimo teorico della pretesa | EUR 440.000 | EUR 180.000 + EUR 260.000 | doc. 02 | - |

## Calcoli dichiarati nella challenge map

- `30/11/2028 e' 14 giorni prima della domanda`
- `18/04/2028 e' entro l'anno anteriore alla domanda`
- `pretesa massima senza duplicazioni: EUR 180.000 + EUR 260.000 = EUR 440.000`

