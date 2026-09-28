# WF2-059 - Date e valori verificati

Prodotti da `_build/verifica_termini.py`, non a mano.
Data di riferimento: 2031-03-27.

## Date

| Milestone | Data | Giorno | Calcolo | Fonte |
|---|---|---|---|---|
| comunicazione scritta di variazione del numero di telefono censito | 2031-02-04 | martedi | raccomandata del cliente alla filiale | doc. 03 |
| episodio di comunicazione delle credenziali a terzi | 2031-02-27 | giovedi | dichiarazione del cliente | doc. 03 |
| blocco delle credenziali su richiesta del cliente | 2031-03-12 | mercoledi | registro tecnico, riga del 12 marzo | doc. 02 |
| lettera di rigetto dell'Ufficio Reclami | 2031-03-20 | giovedi | protocollo RC/2031/00814 | doc. 04 |
| prima operazione contestata | 2031-03-05 | mercoledi | lista movimenti | doc. 02 |
| ultima operazione contestata | 2031-03-07 | venerdi | lista movimenti | doc. 02 |
| disconoscimento inviato alla banca | 2031-03-12 | mercoledi | PEC | doc. 03 |
| data di riferimento | 2031-03-27 | giovedi | fissata dall'incarico | prompt |

## Valori controllati

| Grandezza | Valore | Fonte |
|---|---|---|
| totale delle operazioni contestate | euro 148.500,00 | somma dei sei bonifici |
| soglia di autorizzazione a doppia firma prevista dal mandato | euro 25.000,00 | mandato di conto |
| importo del singolo bonifico piu' elevato | euro 39.000,00 | lista movimenti |
| giorni fra la prima operazione e il disconoscimento | 7 | 5 marzo -> 12 marzo |
| giorni fra l'ultima operazione e il disconoscimento | 5 | 7 marzo -> 12 marzo |

## Codici a struttura calcolata

Generati con l'algoritmo ufficiale da `_build/anagrafica.py` e verificati
con il carattere di controllo.

| Soggetto | Codice |
|---|---|
| Officine Pratosolco S.r.l. | P.IVA 73000015070 |
| Officine Pratosolco S.r.l. | IBAN IT16R0912112467400000010901 |
| Chiara Sinibaldeschi | C.F. SNBCHR88A48D612G |
