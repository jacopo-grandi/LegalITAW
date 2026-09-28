# WF2-056 - Date e valori verificati

Prodotti da `_build/verifica_termini.py`, non a mano.
Data di riferimento: 2031-09-30.

## Date

| Milestone | Data | Giorno | Calcolo | Fonte |
|---|---|---|---|---|
| data del sinistro | 2031-01-11 | sabato | denuncia e verbale dei vigili del fuoco | doc. 03 |
| ripresa parziale della produzione | 2031-03-24 | lunedi | relazione di stabilimento | doc. 06 |
| ripresa a regime | 2031-08-18 | lunedi | relazione di stabilimento | doc. 06 |
| scadenza del periodo di indennizzo (12 mesi) | 2032-01-11 | domenica | sinistro + 12 mesi come da scheda di polizza; termine convenzionale di durata della copertura, non termine per l'adempimento: cade di domenica e non si proroga (art. 2963 c.c. non si applica alle date pattuite) | art. 3 delle condizioni particolari |
| data di riferimento | 2031-09-30 | martedi | fissata dall'incarico | prompt |

## Valori controllati

| Grandezza | Valore | Fonte |
|---|---|---|
| somma assicurata per i danni indiretti | euro 6.000.000,00 | scheda di polizza |
| margine di contribuzione assicurato dichiarato | euro 5.400.000,00 | scheda di polizza |
| margine di contribuzione dell'esercizio 2030 | euro 6.750.000,00 | conto economico 2030 |
| grado di sottoassicurazione | 20,00 per cento | 1 meno 5.400.000 diviso 6.750.000 |
| quota indennizzabile per effetto della regola proporzionale | 80,00 per cento | 5.400.000 diviso 6.750.000 |
| base di computo del margine giornaliero | 360 giorni | condizioni particolari, art. 4 |
| margine giornaliero | euro 18.750,00 | 6.750.000 diviso 360 |
| giorni di fermo totale | 72 | 11 gennaio 2031 - 23 marzo 2031, inclusi |
| giorni di capacita ridotta | 147 | 24 marzo 2031 - 17 agosto 2031, inclusi |
| capacita residua nel periodo di ripresa parziale | 55 per cento | relazione di stabilimento |
| perdita di margine nel periodo di fermo totale | euro 1.350.000,00 | 72 giorni per 18.750,00 |
| perdita di margine nel periodo di capacita ridotta | euro 1.240.312,50 | 147 giorni per il 45 per cento di 18.750,00 |
| perdita di margine lorda | euro 2.590.312,50 | somma dei due periodi |
| franchigia in giorni | 10 giorni | scheda di polizza |
| importo della franchigia | euro 187.500,00 | 10 giorni per 18.750,00 |
| perdita al netto della franchigia | euro 2.402.812,50 | perdita lorda meno franchigia |
| rettifica per l'andamento dell'attivita | meno 6 per cento | relazione di stabilimento, andamento del portafoglio ordini |
| perdita rettificata per l'andamento | euro 2.258.643,75 | perdita al netto della franchigia meno il 6 per cento |
| indennizzo sulla perdita di margine | euro 1.806.915,00 | perdita rettificata per l'80 per cento |
| maggiori costi di esercizio richiesti | euro 340.000,00 | perizia di parte |
| sublimite per i maggiori costi di esercizio | euro 200.000,00 | scheda di polizza |
| maggiori costi di esercizio indennizzabili | euro 160.000,00 | sublimite per l'80 per cento |
| indennizzo complessivo | euro 1.966.915,00 | indennizzo sul margine piu' maggiori costi indennizzabili |
| quantificazione della perizia di parte | euro 2.838.925,00 | perdita al netto della franchigia con trend in aumento del 4 per cento, senza regola proporzionale, piu' l'intero importo dei maggiori costi |
| scostamento fra perizia di parte e indennizzo verificato | euro 872.010,00 | differenza fra i due importi |
| periodo di indennizzo | 12 mesi | scheda di polizza |

## Codici a struttura calcolata

Generati con l'algoritmo ufficiale da `_build/anagrafica.py` e verificati
con il carattere di controllo.

| Soggetto | Codice |
|---|---|
| Cartiera Valmoranda S.p.A. | P.IVA 73000010964 |
| Cartiera Valmoranda S.p.A. | IBAN IT57Q0189413372400000007928 |
| Assicurazioni Portomanno S.p.A. | P.IVA 74000035878 |
| Assicurazioni Portomanno S.p.A. | IBAN IT09T0291413065500000013141 |
| Perizie Industriali Vaglianico S.r.l. | P.IVA 74000037981 |
| Perizie Industriali Vaglianico S.r.l. | IBAN IT69J0810615522500000013914 |
| Renzo Torlasco | C.F. TRLRNZ68T05F205O |
