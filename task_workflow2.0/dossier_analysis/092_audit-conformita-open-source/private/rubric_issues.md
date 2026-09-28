# WF2-092 - Rubrica in prosa, a livello di issue

Questa e la rubrica che l'avvocato legge, discute e firma: dice che cosa il caso
misura. La forma eseguibile, atomizzata e tipizzata, e in `criteria_atomized.md`;
il raccordo fra le due e l'`issue_id`.

**Lato assistito:** Solmarino Software S.r.l., che fornisce il prodotto come apparecchiatura installata presso il cliente e come servizio erogato in cloud  
**Data di riferimento:** 2026-11-05  
**Stato del fascicolo:** audit in corso; versione 5.1.4 in esercizio, versione 5.2 pianificata per il 26 novembre 2026; parere legale e atto di cessione non acquisiti

## Issue di merito

**I-01. pianificatore AGPL modificato e raggiungibile dalla rete** (gravita alta) - il pianificatore corvenza-scheduler 4.2.1 è distribuito con licenza AGPL-3.0-only, è stato modificato localmente ed è eseguito nel servizio in cloud, dove gli utenti del cliente lo raggiungono attraverso il portale e attraverso l'interfaccia programmatica: la versione modificata deve offrire agli utenti che vi interagiscono a distanza la possibilità di ricevere il codice sorgente corrispondente *(fonte: 02_inventario_dipendenze.csv, riga di corvenza-scheduler; 03_notice_e_intestazioni.md; 01_scheda_prodotto_e_fornitura.md, punti 2.2 e 5; 08_email_responsabile_sviluppo.md; atomi: B.1, B.2, B.3, B.4)*

**I-02. menzione delle modifiche sui file Apache** (gravita alta) - tre file del pacchetto algen-crypto sono stati modificati e le loro intestazioni riportano soltanto l'avviso di licenza originale: va apposto su ciascun file modificato un avviso in evidenza che dichiari la modifica *(fonte: 03_notice_e_intestazioni.md, parte seconda, tre file di algen-crypto; 02_inventario_dipendenze.csv; 08_email_responsabile_sviluppo.md, paragrafo sulla cifratura; atomi: B.5, B.6)*

**I-03. avvisi di attribuzione non riprodotti** (gravita alta) - il pacchetto belfonte-parser include un proprio file NOTICE con avvisi di attribuzione che il NOTICE distribuito con la piattaforma non riproduce: il contenuto va riprodotto in una delle collocazioni ammesse *(fonte: 03_notice_e_intestazioni.md, parte prima e contenuto del NOTICE di belfonte-parser; 02_inventario_dipendenze.csv; atomi: B.7, B.8)*

**I-04. combinazione fra Apache-2.0 e GPL-2.0-only** (gravita alta) - meridolo-compress è distribuito con licenza GPL-2.0-only ed è collegato staticamente, nello stesso modulo consegnato al cliente, con algen-crypto distribuito con licenza Apache-2.0: la combinazione va rilevata come incompatibile e risolta prima della distribuzione *(fonte: 02_inventario_dipendenze.csv, righe di meridolo-compress e algen-crypto; atomi: B.9, B.10, B.11)*

**I-05. richiesta scritta del codice sorgente corrispondente** (gravita alta) - la richiesta del cliente del 21 ottobre 2026 riguarda i componenti installati sull'apparecchiatura di sua proprietà e va evasa comprendendo gli script necessari alla generazione, all'installazione e all'esecuzione del codice oggetto; se la consegna avviene mediante archivio in rete, va dichiarato per quanto tempo l'archivio resta disponibile *(fonte: 06_richiesta_codice_sorgente.md; 01_scheda_prodotto_e_fornitura.md, punto 2.1; 02_inventario_dipendenze.csv, canale di distribuzione; atomi: B.12, B.13, B.14, C.5)*

**I-06. componente GPL-3.0 modificato e distribuito sull'appliance** (gravita alta) - quadrelli-render 2.2.0 è distribuito con licenza GPL-3.0-only, è stato modificato ed è collegato staticamente nel modulo solmarino-report installato sull'apparecchiatura: va verificato il perimetro dell'opera così come distribuita, perché la licenza si applica all'insieme e non alla sola porzione modificata *(fonte: 02_inventario_dipendenze.csv, riga di quadrelli-render; 03_notice_e_intestazioni.md; 01_scheda_prodotto_e_fornitura.md, punto 2.1; atomi: B.15, B.16, B.17)*

**I-07. componente EUPL esposto agli utenti del portale** (gravita alta) - aurendo-forms 6.3.0 è distribuito con licenza EUPL-1.2, non è stato modificato ed espone agli utenti del portale la funzione di compilazione guidata: la messa a disposizione online dell'accesso alle funzionalità essenziali rientra nella nozione di distribuzione o comunicazione della licenza, e l'obbligo non dipende dalla modifica *(fonte: 02_inventario_dipendenze.csv, riga di aurendo-forms; 04_verbale_comitato_tecnico.md, punto 2; 08_email_responsabile_sviluppo.md, paragrafo sul portale; atomi: B.18, B.19)*

**I-08. componenti senza licenza dichiarata** (gravita alta) - otto componenti dell'inventario non dichiarano alcuna licenza, e cinque di essi sono distribuiti sull'apparecchiatura: l'assenza di dichiarazione non equivale a una licenza permissiva e la posizione va risolta prima della distribuzione *(fonte: 02_inventario_dipendenze.csv, righe con il campo della licenza vuoto e relativi canali di distribuzione; atomi: B.20, B.21, B.22, C.1, C.2, C.3, C.6)*

**I-09. titolo sul codec scritto da un collaboratore esterno** (gravita alta) - ferlaino-codec 2.8.1 è stato scritto da un collaboratore esterno, non dichiara licenza e non risulta alcun atto di cessione sottoscritto: il titolo di Solmarino non è dimostrato dal fascicolo e non si presume, perché la regola che attribuisce al datore di lavoro i diritti di utilizzazione economica riguarda il lavoratore dipendente *(fonte: 02_inventario_dipendenze.csv, riga di ferlaino-codec; 03_notice_e_intestazioni.md, ultima intestazione; 04_verbale_comitato_tecnico.md, punto 3; atomi: B.23, B.24, B.25)*

**I-10. dichiarazione contrattuale smentita dall'inventario** (gravita alta) - l'articolo 4.2 del contratto contiene la dichiarazione e garanzia che nessun componente di terze parti impone obblighi di divulgazione del codice sorgente, e il confronto con l'inventario la smentisce: la posizione contrattuale va gestita e non lasciata in piedi *(fonte: 05_contratto_fornitura.md, articolo 4.2; 02_inventario_dipendenze.csv; atomi: B.26, B.27)*

**I-11. delibera condizionata a un parere mai acquisito** (gravita media) - il comitato tecnico ha deliberato il 4 giugno 2026 l'adozione del pianificatore subordinatamente all'acquisizione del parere dell'ufficio legale, e il fascicolo non contiene alcun parere: la condizione della delibera non risulta soddisfatta *(fonte: 04_verbale_comitato_tecnico.md, punto 1; 07_piano_di_rilascio.md, punto 5.1; atomi: B.28, B.29)*

**I-12. rilascio non condizionato ai rimedi** (gravita alta) - il piano di rilascio non annovera fra le condizioni di rilascio le attività di conformità ancora aperte, e il rilascio del 26 novembre 2026 aggiorna sia il servizio in cloud sia le apparecchiature installate: i rimedi che incidono sulla distribuzione vanno chiusi prima di quella data *(fonte: 07_piano_di_rilascio.md, punti 2, 3, 4, 5 e 6; atomi: B.30, B.31, B.32, C.4)*

## Controlled non-issue

Elementi che sembrano problematici e non lo sono. Ciascuno ha un criterio di
assenza che lo nomina: senza quel criterio il non-issue non sarebbe misurato.

**N-01. componente AGPL non modificato nel servizio in cloud** - il pacchetto tessitura-queue 1.9.0 è distribuito con licenza AGPL-3.0-only ma è usato senza modifiche: l'obbligo della sezione 13 è formulato in termini di modifica del programma e sul testo della licenza non scatta *(chiave nel criterio: tessitura-queue; atomi: B.33)*

**N-02. componente GPL-2.0-or-later nella stessa combinazione** - vestrigo-imaging 5.0.2 è distribuito con licenza GPL-2.0-or-later ed è collegato staticamente insieme allo stesso componente Apache-2.0: l'opzione della versione successiva consente di collocare la combinazione sotto la versione 3 della GPL, che la Free Software Foundation dichiara compatibile con la Apache-2.0 *(chiave nel criterio: vestrigo-imaging; atomi: B.34)*

**N-03. componente GPL-3.0 modificato per il solo uso interno** - nabissa-loader 1.0.4 è modificato ma resta sui sistemi interni di Solmarino e non è consegnato ad alcun destinatario: la licenza consente di realizzare e usare una versione modificata senza distribuirla, e in tal caso non impone il rilascio del sorgente *(chiave nel criterio: nabissa-loader; atomi: B.35)*

**N-04. componenti Apache-2.0 eseguiti nel servizio in cloud** - la Apache License 2.0 non contiene disposizioni relative all'uso in rete: l'esecuzione di un componente Apache nel servizio in cloud non fa nascere alcun obbligo di divulgazione del codice sorgente *(chiave nel criterio: obbligo di divulgazione del sorgente per i componenti Apache-2.0; atomi: B.36)*

**N-05. categoria di opera derivata attribuita alla GPL-3.0** - il testo della GPL-3.0 non usa la categoria dell'opera derivata: parla di opera basata sul programma, di versione modificata e di opera coperta. La nozione di opera derivata appartiene al diritto d'autore applicabile, non alla licenza *(chiave nel criterio: definizione di opera derivata; atomi: B.37)*

## Chiusura obbligatoria

La rubrica atomizzata si chiude con i criteri di simmetria, sovra-segnalazione e
divieto di presunzione dell'esito, ciascuno con l'oggetto nominato: sono i criteri
che impediscono di premiare la prudenza vuota.
