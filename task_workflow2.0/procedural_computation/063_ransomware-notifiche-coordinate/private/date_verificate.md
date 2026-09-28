# WF2-063 - Date e valori verificati

Tabella prodotta da `source/verifica_date_valori.py` (festivita' nazionali incluse).
Data di riferimento del caso: 16 febbraio 2027.

| Milestone | Data o valore | Calcolo | Fonte | Nota |
|---|---|---|---|---|
| conoscenza qualificata del titolare | 16 febbraio 2027 08:20 (martedi) | dato di fascicolo: report SOC del 16 febbraio 2027, ore 08:20 | doc. 01 | - |
| pre-notifica al soggetto NIS (24 ore) | 17 febbraio 2027 08:20 (mercoledi) | conoscenza + 24 ore | doc. 04 | - |
| avviso al cliente (24 ore contrattuali) | 17 febbraio 2027 08:20 (mercoledi) | conoscenza + 24 ore | doc. 06 | - |
| avviso all'assicuratore (48 ore di polizza) | 18 febbraio 2027 08:20 (giovedi) | conoscenza + 48 ore | doc. 05 | - |
| notifica NIS (72 ore) | 19 febbraio 2027 08:20 (venerdi) | conoscenza + 72 ore | doc. 04 | - |
| notifica all'autorita' di protezione dei dati (72 ore) | 19 febbraio 2027 08:20 (venerdi) | conoscenza + 72 ore | 02_reference_pack.md | - |
| relazione finale NIS (un mese dalla notifica) | 19 marzo 2027 08:20 (venerdi) | notifica + un mese di calendario | doc. 04 | - |
| termini in ore e fine settimana | nessuno slittamento | i termini espressi in ore non si prorogano: 16-19 febbraio 2027 sono martedi'-venerdi' | N-04 | - |

## Calcoli dichiarati nella challenge map

- `24h: 16/02/2027 08:20 + 24h = 17/02/2027 08:20`
- `48h: 18/02/2027 08:20`
- `72h: 19/02/2027 08:20`
- `un mese dalla notifica completa: 19/03/2027 08:20`

