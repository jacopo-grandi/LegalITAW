# WF2-067 - Date e valori verificati

Tabella prodotta da `source/verifica_date_valori.py` (festivita' nazionali incluse).
Data di riferimento del caso: 7 novembre 2028.

| Milestone | Data o valore | Calcolo | Fonte | Nota |
|---|---|---|---|---|
| rata non pagata | 4 novembre 2028 (sabato) | dato di fascicolo | doc. 01 | - |
| diffida ricevuta | 6 novembre 2028 (lunedi) | dato di fascicolo | doc. 01 | - |
| giorni del cure period | 7, 8, 9, 10, 13, 14, 15, 16, 17, 20 novembre 2028 | 10 giorni lavorativi dalla ricezione, dies a quo escluso | doc. 01 | - |
| ultimo giorno del cure period | 20 novembre 2028 (lunedi) | decimo giorno lavorativo | doc. 01 | - |
| giorni non computati | 11, 12, 18, 19 novembre 2028 | sabati e domeniche nella finestra; nessuna festivita' nazionale (1 novembre precede la diffida) | N/A | - |
| residuo dopo compensazione del conto vincolato | EUR 3.860.000 | EUR 4.480.000 - EUR 620.000 | doc. 01 e doc. 04 | - |

## Calcoli dichiarati nella challenge map

- `cure: 7,8,9,10,13,14,15,16,17,20 novembre = 10 giorni lavorativi`
- `EUR 4.480.000 - EUR 620.000 = EUR 3.860.000`

