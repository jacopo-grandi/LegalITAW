# WF2-032 - Termini, date e importi verificati

Prodotto da `source/authoring/verifica_wf2_032.py`; l'output integrale dell'ultima esecuzione e' in
`source/authoring/_output_verifica.txt`. Festivita' nazionali italiane incluse nel controllo, insieme
alla regola sul sabato per i termini processuali. Nessun valore di questa tabella e' stato calcolato
a mano.

## Cronologia

| Evento | Data | Giorno | Fonte |
|---|---|---|---|
| Comunicazione dello schema di atto | 08/04/2030 (2030-04-08) | lunedi | documento 01 |
| Osservazioni della societa' | 27/05/2030 (2030-05-27) | lunedi | documento 02 |
| Data dell'avviso di accertamento | 17/06/2030 (2030-06-17) | lunedi | documento 03 |
| Ricevuta di accettazione della posta certificata | 20/06/2030 (2030-06-20) | giovedi | documento 04 |
| RICEVUTA DI AVVENUTA CONSEGNA (notificazione) | 20/06/2030 (2030-06-20) | giovedi | documento 04 |
| Istanza di accertamento con adesione | 01/07/2030 (2030-07-01) | lunedi | documento 05 |
| Invito a comparire | 11/07/2030 (2030-07-11) | giovedi | documento 06 |
| Contraddittorio e verbale di mancato accordo | 04/09/2030 (2030-09-04) | mercoledi | documento 06 |
| Nota del consulente fiscale | 15/09/2030 (2030-09-15) | domenica | documento 07 |
| Data di riferimento del fascicolo | 16/09/2030 (2030-09-16) | lunedi | prompt |

## Termini

| Termine | Regola | Scadenza nominale | Scadenza effettiva | Stato al 16/09/2030 |
|---|---|---|---|---|
| Osservazioni allo schema di atto | 60 giorni dalla comunicazione | 07/06/2030 (venerdi) | 07/06/2030 | scaduto, rispettato |
| Istanza di accertamento con adesione | 15 giorni dalla notifica dell'atto preceduto dallo schema | 05/07/2030 (venerdi) | 05/07/2030 | scaduto, rispettato con 4 giorni di margine |
| Invito a comparire dell'Ufficio | 15 giorni dalla ricezione dell'istanza | 16/07/2030 | 16/07/2030 | scaduto, rispettato dall'Ufficio |
| RICORSO | 60 giorni dalla notificazione + 30 di sospensione da adesione + 31 di sospensione feriale | 19/10/2030 (SABATO) | 21/10/2030 (lunedi) | aperto, 35 giorni residui |
| Pagamento in acquiescenza | entro il termine per la proposizione del ricorso | 19/10/2030 | 21/10/2030 | aperto |
| Costituzione in giudizio | 30 giorni dalla proposizione del ricorso | 20/11/2030 | 20/11/2030 (mercoledi) | futuro |

Il computo del termine per il ricorso: giorno iniziale non computato; 60 + 30 + 31 = 121 giorni dal
20 giugno 2030 danno il 19 ottobre 2030; la scadenza cade di sabato ed e' prorogata al primo giorno
seguente non festivo, il 21 ottobre 2030.

## Derivazioni errate presidiate da criteri `assenza`

| Derivazione errata | Risultato | Criterio |
|---|---|---|
| sospensione di 90 giorni invece di 30 | 18/12/2030 | C.9 |
| decorso ripreso dal verbale di mancato accordo | 23/10/2030 | C.10 |
| nessuna sospensione feriale | 18/09/2030 | C.11 |
| nessuna sospensione da adesione | 19/09/2030 | C.12 |
| decorrenza dalla data dell'avviso anziche' dalla notificazione | 16/10/2030 | C.13 |

Verificato con script che nessuna delle cinque derivazioni errate coincide con il termine effettivo.

## Importi

| Voce | Importo (euro) | Calcolo | Fonte |
|---|---:|---|---|
| Ricavi non contabilizzati (rilievo A) | 900.000,00 | - | documento 03 |
| Costi indeducibili (rilievo B) | 350.000,00 | - | documento 03 |
| Maggiore imponibile IRES | 1.250.000,00 | 900.000 + 350.000 | documento 03 |
| Maggiore IRES | 300.000,00 | 24% di 1.250.000,00 | documento 03 |
| Maggiore IVA | 198.000,00 | 22% di 900.000,00 | documento 03 |
| Totale maggiori imposte | 498.000,00 | 300.000 + 198.000 | documento 03 |
| Sanzioni irrogate | 348.600,00 | 70% di 498.000,00 | documento 03 |
| Totale dell'atto | 846.600,00 | 498.000 + 348.600 | documento 03 |
| Iscrizione a titolo provvisorio | 166.000,00 | un terzo di 498.000,00, senza resto | art. 15 d.P.R. 602/1973 |

## Codici a struttura calcolata

| Codice | Valore | Verifica |
|---|---|---|
| P.IVA Ronchivalle Sistemi S.r.l. | 02947180176 | cifra di controllo valida |
| C.F. Ilaria Bencivenni | BNCLRI74P52B157Y | algoritmo ufficiale; Belfiore B157 = Brescia |

## Coerenza relativa dei valori

- Il totale delle maggiori imposte e' **divisibile per tre senza resto**: l'importo iscrivibile a
  titolo provvisorio e' un numero esatto e il criterio di tipo `valore` non dipende
  dall'arrotondamento.
- La scadenza nominale cade **di sabato**: la proroga opera, e la differenza fra chi la applica e chi
  non la applica e' di due giorni, non di uno.
- Il margine dell'istanza di adesione e' di **quattro giorni**: abbastanza stretto da rendere
  significativa la verifica di tempestivita', abbastanza ampio da non renderla opinabile.
- Alla data di riferimento restano **35 giorni**: il caso e' costruito perche' ogni opzione sia
  ancora praticabile e la decisione sia effettivamente da prendere.
