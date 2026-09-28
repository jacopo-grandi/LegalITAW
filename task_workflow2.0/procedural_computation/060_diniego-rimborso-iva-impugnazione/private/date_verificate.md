# WF2-060 - Date e valori verificati

Prodotti da `_build/verifica_termini.py`, non a mano.
Data di riferimento: 2031-06-30.

## Date

| Milestone | Data | Giorno | Calcolo | Fonte |
|---|---|---|---|---|
| presentazione dell'istanza di rimborso | 2029-11-20 | martedi | ricevuta di protocollo | doc. 02 |
| decorso dei novanta giorni dall'istanza | 2030-02-18 | lunedi | istanza + 90 giorni | art. 21, co. 2 D.Lgs. 546/1992 |
| notifica del provvedimento di diniego | 2031-05-06 | martedi | ricevuta di consegna PEC | doc. 04 |
| scadenza del termine per il ricorso (60 giorni) | 2031-07-07 | lunedi | 6 maggio + 60 giorni, dies a quo escluso; la sospensione feriale dal 1 al 31 agosto non interseca il periodo | art. 21, co. 1 D.Lgs. 546/1992 |
| data di riferimento | 2031-06-30 | lunedi | fissata dall'incarico | prompt |

## Proroghe applicate

- scadenza del termine per il ricorso (60 giorni): scadenza nominale 2031-07-05 (sabato), prorogata al primo giorno non festivo (regime processuale)

## Valori controllati

| Grandezza | Valore | Fonte |
|---|---|---|
| credito IVA chiesto a rimborso | euro 318.400,00 | istanza di rimborso |
| importo riconosciuto dall'ufficio | euro 0,00 | provvedimento di diniego |
| periodo d'imposta | 2028 | istanza di rimborso |

## Codici a struttura calcolata

Generati con l'algoritmo ufficiale da `_build/anagrafica.py` e verificati
con il carattere di controllo.

| Soggetto | Codice |
|---|---|
| Vetreria Sambrenta S.p.A. | P.IVA 73000016441 |
| Vetreria Sambrenta S.p.A. | IBAN IT79Q0238616690400000011892 |
| Emanuele Vallecorsa | C.F. VLLMNL76R19H501L |
