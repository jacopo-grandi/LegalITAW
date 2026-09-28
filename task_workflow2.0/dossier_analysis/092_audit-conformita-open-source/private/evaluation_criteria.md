# WF2-092 - Scheda di valutazione

Questa scheda è un indice operativo. La motivazione giuridica resta in
`rubric_issues.md`; le condizioni binarie complete restano in
`criteria_atomized.md` e `rubric.json`.

## Quadro di routing

- Verifica meccanica: 13 criteri (A.1, A.2, A.3, A.4, A.5, A.6, A.7, A.8, A.9, C.1, C.2, C.4, C.5).
- Judge: 41 criteri (B.1, B.2, B.3, B.4, B.5, B.6, B.7, B.8, B.9, B.10, B.11, B.12, B.13, B.14, B.15, B.16, B.17, B.18, B.19, B.20, B.21, B.22, B.23, B.24, B.25, B.26, B.27, B.28, B.29, B.30, B.31, B.32, B.33, B.34, B.35, B.36, B.37, B.38, B.39, C.3, C.6).

## Issue di merito

| Issue | Gravità | Criteri | Evidenza da consultare |
|---|---:|---|---|
| I-01 - pianificatore AGPL modificato e raggiungibile dalla rete | alta | B.1, B.2, B.3, B.4 | 02_inventario_dipendenze.csv, riga di corvenza-scheduler; 03_notice_e_intestazioni.md; 01_scheda_prodotto_e_fornitura.md, punti 2.2 e 5; 08_email_responsabile_sviluppo.md |
| I-02 - menzione delle modifiche sui file Apache | alta | B.5, B.6 | 03_notice_e_intestazioni.md, parte seconda, tre file di algen-crypto; 02_inventario_dipendenze.csv; 08_email_responsabile_sviluppo.md, paragrafo sulla cifratura |
| I-03 - avvisi di attribuzione non riprodotti | alta | B.7, B.8 | 03_notice_e_intestazioni.md, parte prima e contenuto del NOTICE di belfonte-parser; 02_inventario_dipendenze.csv |
| I-04 - combinazione fra Apache-2.0 e GPL-2.0-only | alta | B.9, B.10, B.11 | 02_inventario_dipendenze.csv, righe di meridolo-compress e algen-crypto |
| I-05 - richiesta scritta del codice sorgente corrispondente | alta | B.12, B.13, B.14, C.5 | 06_richiesta_codice_sorgente.md; 01_scheda_prodotto_e_fornitura.md, punto 2.1; 02_inventario_dipendenze.csv, canale di distribuzione |
| I-06 - componente GPL-3.0 modificato e distribuito sull'appliance | alta | B.15, B.16, B.17 | 02_inventario_dipendenze.csv, riga di quadrelli-render; 03_notice_e_intestazioni.md; 01_scheda_prodotto_e_fornitura.md, punto 2.1 |
| I-07 - componente EUPL esposto agli utenti del portale | alta | B.18, B.19 | 02_inventario_dipendenze.csv, riga di aurendo-forms; 04_verbale_comitato_tecnico.md, punto 2; 08_email_responsabile_sviluppo.md, paragrafo sul portale |
| I-08 - componenti senza licenza dichiarata | alta | B.20, B.21, B.22, C.1, C.2, C.3, C.6 | 02_inventario_dipendenze.csv, righe con il campo della licenza vuoto e relativi canali di distribuzione |
| I-09 - titolo sul codec scritto da un collaboratore esterno | alta | B.23, B.24, B.25 | 02_inventario_dipendenze.csv, riga di ferlaino-codec; 03_notice_e_intestazioni.md, ultima intestazione; 04_verbale_comitato_tecnico.md, punto 3 |
| I-10 - dichiarazione contrattuale smentita dall'inventario | alta | B.26, B.27 | 05_contratto_fornitura.md, articolo 4.2; 02_inventario_dipendenze.csv |
| I-11 - delibera condizionata a un parere mai acquisito | media | B.28, B.29 | 04_verbale_comitato_tecnico.md, punto 1; 07_piano_di_rilascio.md, punto 5.1 |
| I-12 - rilascio non condizionato ai rimedi | alta | B.30, B.31, B.32, C.4 | 07_piano_di_rilascio.md, punti 2, 3, 4, 5 e 6 |

## Controlled non-issue

| Non-issue | Criteri di assenza | Ragione del controllo |
|---|---|---|
| N-01 - componente AGPL non modificato nel servizio in cloud | B.33 | il pacchetto tessitura-queue 1.9.0 è distribuito con licenza AGPL-3.0-only ma è usato senza modifiche: l'obbligo della sezione 13 è formulato in termini di modifica del programma e sul testo della licenza non scatta |
| N-02 - componente GPL-2.0-or-later nella stessa combinazione | B.34 | vestrigo-imaging 5.0.2 è distribuito con licenza GPL-2.0-or-later ed è collegato staticamente insieme allo stesso componente Apache-2.0: l'opzione della versione successiva consente di collocare la combinazione sotto la versione 3 della GPL, che la Free Software Foundation dichiara compatibile con la Apache-2.0 |
| N-03 - componente GPL-3.0 modificato per il solo uso interno | B.35 | nabissa-loader 1.0.4 è modificato ma resta sui sistemi interni di Solmarino e non è consegnato ad alcun destinatario: la licenza consente di realizzare e usare una versione modificata senza distribuirla, e in tal caso non impone il rilascio del sorgente |
| N-04 - componenti Apache-2.0 eseguiti nel servizio in cloud | B.36 | la Apache License 2.0 non contiene disposizioni relative all'uso in rete: l'esecuzione di un componente Apache nel servizio in cloud non fa nascere alcun obbligo di divulgazione del codice sorgente |
| N-05 - categoria di opera derivata attribuita alla GPL-3.0 | B.37 | il testo della GPL-3.0 non usa la categoria dell'opera derivata: parla di opera basata sul programma, di versione modificata e di opera coperta. La nozione di opera derivata appartiene al diritto d'autore applicabile, non alla licenza |

## Regola di chiusura

La valutazione è completa solo dopo l'esito di tutti i criteri elencati sopra;
nessun issue o controlled non-issue può essere deciso per analogia con un altro.
