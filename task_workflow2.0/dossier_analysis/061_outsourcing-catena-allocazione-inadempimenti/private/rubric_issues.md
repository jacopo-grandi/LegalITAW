# WF2-061 - Rubrica narrativa

Rubrica in prosa a livello di issue: e' il documento che passa dalla validazione
professionale. Ogni voce riporta gli identificativi degli atomi che la attuano; la loro
forma a campi sta in `criteria_atomized.md` e in `rubric.json`, con gli stessi ID.

## A - Forma dell'output

Controlli interamente meccanici sul formato del deliverable.

| ID | Tipo | Proposizione |
|---|---|---|
| A.1 | struttura | esistono tutti i file di consegna nominati nel template. |
| A.2 | valore | il file Markdown principale non supera 3.200 parole. |
| A.3 | struttura | le sezioni obbligatorie compaiono nell'ordine del template. |
| A.4 | struttura | ogni allegato pubblico elencato nell'incarico e' richiamato almeno una volta nel deliverable. |
| A.5 | assenza | il deliverable non cita fonti esterne all'elenco chiuso. |
| A.6 | struttura | fatti, inferenze e dati mancanti hanno etichette distinguibili. |

## B - Merito

Stato del fascicolo alla data di riferimento: in corso, dopo due disservizi e prima del rinnovo.

### I-01 - responsabilita' del contraente principale

Il deliverable deve affermare che Veltragno resta responsabile verso Arcomera anche quando la causa si colloca a valle (fonte: doc. 01 clausola 12 e doc. 03). Azione attesa: rifiutare ogni rinvio diretto del reclamo a Nembrosa. Conseguenza: la catena contrattuale non spezza il rapporto principale. Non deve affermare: che il punto sia provato oltre quanto consentono gli allegati. Gravita': alta.

| ID | Tipo | Proposizione |
|---|---|---|
| B.1 | presenza | il deliverable afferma che Veltragno resta responsabile verso Arcomera anche quando la causa si colloca a valle. |
| B.13 | attribuzione | il deliverable riconduce responsabilita' del contraente principale a doc. 01 clausola 12 e doc. 03. |
| B.25 | presenza | il deliverable richiede rifiutare ogni rinvio diretto del reclamo a Nembrosa. |
| B.37 | presenza | il deliverable indica come conseguenza di responsabilita' del contraente principale che la catena contrattuale non spezza il rapporto principale. |

### I-02 - SLA non trasferiti al primo subfornitore

Il deliverable deve affermare che la soglia 99,50% e il ripristino a 240 minuti non coprono gli impegni 99,95% e 120 minuti (fonte: doc. 02 e doc. 03). Azione attesa: imporre flow-down integrale o buffer misurabile. Conseguenza: Veltragno sopporta uno scoperto prestazionale. Non deve affermare: che il punto sia provato oltre quanto consentono gli allegati. Gravita': alta.

| ID | Tipo | Proposizione |
|---|---|---|
| B.2 | valore | il deliverable afferma che la soglia 99,50% e il ripristino a 240 minuti non coprono gli impegni 99,95% e 120 minuti. |
| B.14 | attribuzione | il deliverable riconduce SLA non trasferiti al primo subfornitore a doc. 02 e doc. 03. |
| B.26 | presenza | il deliverable richiede imporre flow-down integrale o buffer misurabile. |

### I-03 - secondo livello privo di flow-down

Il deliverable deve affermare che Quadir non assume tempi di ripristino ne' exit assistance (fonte: doc. 03 e doc. 04). Azione attesa: estendere SLA, audit e uscita a Quadir. Conseguenza: un guasto del data center resta senza rimedio back-to-back. Non deve affermare: che il punto sia provato oltre quanto consentono gli allegati. Gravita': alta.

| ID | Tipo | Proposizione |
|---|---|---|
| B.3 | presenza | il deliverable afferma che Quadir non assume tempi di ripristino ne' exit assistance. |
| B.15 | attribuzione | il deliverable riconduce secondo livello privo di flow-down a doc. 03 e doc. 04. |
| B.27 | presenza | il deliverable richiede estendere SLA, audit e uscita a Quadir. |

### I-04 - manutenzione non programmata

Il deliverable deve affermare che il preavviso di un giorno non soddisfa la finestra di cinque giorni (fonte: doc. 02 e doc. 05). Azione attesa: conteggiare i 94 minuti nella disponibilita' di febbraio. Conseguenza: l'esclusione SLA non opera. Non deve affermare: che il punto sia provato oltre quanto consentono gli allegati. Gravita': alta.

| ID | Tipo | Proposizione |
|---|---|---|
| B.4 | valore | il deliverable afferma che il preavviso di un giorno non soddisfa la finestra di cinque giorni. |
| B.16 | attribuzione | il deliverable riconduce manutenzione non programmata a doc. 02 e doc. 05. |
| B.28 | presenza | il deliverable richiede conteggiare i 94 minuti nella disponibilita' di febbraio. |

### I-05 - service credit non esclusivi nel contratto principale

Il deliverable deve affermare che l'esclusivita' pattuita a valle non limita i rimedi di Arcomera (fonte: doc. 01 e doc. 03). Azione attesa: preservare risarcimento e rimedi contrattuali principali. Conseguenza: Veltragno non puo' trasferire a monte il limite di Nembrosa. Non deve affermare: che il punto sia provato oltre quanto consentono gli allegati. Gravita': alta.

| ID | Tipo | Proposizione |
|---|---|---|
| B.5 | presenza | il deliverable afferma che l'esclusivita' pattuita a valle non limita i rimedi di Arcomera. |
| B.17 | attribuzione | il deliverable riconduce service credit non esclusivi nel contratto principale a doc. 01 e doc. 03. |
| B.29 | presenza | il deliverable richiede preservare risarcimento e rimedi contrattuali principali. |

### I-06 - audit interrotto nella catena

Il deliverable deve affermare che Arcomera non puo' verificare direttamente i log dei soggetti a valle (fonte: doc. 01, doc. 03 e doc. 06). Azione attesa: introdurre accesso per Arcomera o audit indipendente su Nembrosa e Quadir. Conseguenza: manca la prova tecnica per allocare i due incidenti. Non deve affermare: che il punto sia provato oltre quanto consentono gli allegati. Gravita': alta.

| ID | Tipo | Proposizione |
|---|---|---|
| B.6 | presenza | il deliverable afferma che Arcomera non puo' verificare direttamente i log dei soggetti a valle. |
| B.18 | attribuzione | il deliverable riconduce audit interrotto nella catena a doc. 01, doc. 03 e doc. 06. |
| B.30 | presenza | il deliverable richiede introdurre accesso per Arcomera o audit indipendente su Nembrosa e Quadir. |

### I-07 - cambio di localizzazione

Il deliverable deve affermare che la comunicazione successiva sul data center non consente controllo preventivo (fonte: doc. 04). Azione attesa: richiedere autorizzazione preventiva per trasferimenti fuori dal perimetro concordato. Conseguenza: la governance dei dati dipende da una notifica tardiva. Non deve affermare: che il punto sia provato oltre quanto consentono gli allegati. Gravita': media.

| ID | Tipo | Proposizione |
|---|---|---|
| B.7 | presenza | il deliverable afferma che la comunicazione successiva sul data center non consente controllo preventivo. |
| B.19 | attribuzione | il deliverable riconduce cambio di localizzazione a doc. 04. |
| B.31 | presenza | il deliverable richiede richiedere autorizzazione preventiva per trasferimenti fuori dal perimetro concordato. |

### I-08 - sub-responsabile non autorizzato

Il deliverable deve affermare che il fascicolo non prova l'autorizzazione specifica o generale a Quadir (fonte: doc. 01 e doc. 04). Azione attesa: acquisire la catena di nomina e il registro delle opposizioni. Conseguenza: non e' dimostrata la regolarita' del sub-processing. Non deve affermare: che il punto sia provato oltre quanto consentono gli allegati. Gravita': media.

| ID | Tipo | Proposizione |
|---|---|---|
| B.8 | presenza | il deliverable afferma che il fascicolo non prova l'autorizzazione specifica o generale a Quadir. |
| B.20 | attribuzione | il deliverable riconduce sub-responsabile non autorizzato a doc. 01 e doc. 04. |
| B.32 | presenza | il deliverable richiede acquisire la catena di nomina e il registro delle opposizioni. |

### I-09 - exit assistance assente a valle

Il deliverable deve affermare che Veltragno promette novanta giorni di assistenza ma Quadir non e' vincolata (fonte: doc. 01 e doc. 04). Azione attesa: replicare durata, formati e cooperazione nel contratto Quadir. Conseguenza: la migrazione puo' bloccarsi all'ultimo livello. Non deve affermare: che il punto sia provato oltre quanto consentono gli allegati. Gravita': media.

| ID | Tipo | Proposizione |
|---|---|---|
| B.9 | presenza | il deliverable afferma che Veltragno promette novanta giorni di assistenza ma Quadir non e' vincolata. |
| B.21 | attribuzione | il deliverable riconduce exit assistance assente a valle a doc. 01 e doc. 04. |
| B.33 | presenza | il deliverable richiede replicare durata, formati e cooperazione nel contratto Quadir. |

### I-10 - massimali disallineati

Il deliverable deve affermare che il massimale Nembrosa di EUR 300.000 e' inferiore a quello assunto da Veltragno (fonte: doc. 01 e doc. 03). Azione attesa: negoziare massimale e copertura assicurativa coerenti con l'esposizione. Conseguenza: resta una quota non recuperabile a valle. Non deve affermare: che il punto sia provato oltre quanto consentono gli allegati. Gravita': media.

| ID | Tipo | Proposizione |
|---|---|---|
| B.10 | valore | il deliverable afferma che il massimale Nembrosa di EUR 300.000 e' inferiore a quello assunto da Veltragno. |
| B.22 | attribuzione | il deliverable riconduce massimali disallineati a doc. 01 e doc. 03. |
| B.34 | presenza | il deliverable richiede negoziare massimale e copertura assicurativa coerenti con l'esposizione. |

### I-11 - sostituzione del subfornitore

Il deliverable deve affermare che il rinnovo proposto non disciplina preavviso e opposizione alla sostituzione (fonte: doc. 01 e doc. 06). Azione attesa: inserire notifica preventiva e diritto di opposizione motivata. Conseguenza: Arcomera non governa la composizione della catena. Non deve affermare: che il punto sia provato oltre quanto consentono gli allegati. Gravita': media.

| ID | Tipo | Proposizione |
|---|---|---|
| B.11 | presenza | il deliverable afferma che il rinnovo proposto non disciplina preavviso e opposizione alla sostituzione. |
| B.23 | attribuzione | il deliverable riconduce sostituzione del subfornitore a doc. 01 e doc. 06. |
| B.35 | presenza | il deliverable richiede inserire notifica preventiva e diritto di opposizione motivata. |

### I-12 - causalita' ancora incompleta

Il deliverable deve affermare che i log Quadir non sono nel fascicolo (fonte: doc. 05 e doc. 06). Azione attesa: sospendere l'attribuzione definitiva del primo incidente e acquisire i log. Conseguenza: la responsabilita' contrattuale e la causa tecnica vanno tenute distinte. Non deve affermare: che il punto sia provato oltre quanto consentono gli allegati. Gravita': media.

| ID | Tipo | Proposizione |
|---|---|---|
| B.12 | presenza | il deliverable afferma che i log Quadir non sono nel fascicolo. |
| B.24 | attribuzione | il deliverable riconduce causalita' ancora incompleta a doc. 05 e doc. 06. |
| B.36 | presenza | il deliverable richiede sospendere l'attribuzione definitiva del primo incidente e acquisire i log. |

## Controlled non-issue - divieto nominato di sovra-segnalazione

### N-01 - cifratura a riposo

Non e' un issue: AES-256 e' una misura dichiarata, non il difetto del caso (doc. 04). Segnalarlo come rischio e' errore.

| ID | Tipo | Proposizione |
|---|---|---|
| B.38 | assenza | il deliverable non segnala come rischio, criticita' o inadempimento cifratura a riposo (doc. 04). |

### N-02 - primo evento unico

Non e' un issue: le segnalazioni delle filiali descrivono la stessa indisponibilita' e non tre incidenti (doc. 05). Segnalarlo come rischio e' errore.

| ID | Tipo | Proposizione |
|---|---|---|
| B.39 | assenza | il deliverable non segnala come rischio, criticita' o inadempimento primo evento unico (doc. 05); elemento tracciato: segnalazioni filiali. |

### N-03 - hosting iniziale a Milano

Non e' un issue: la localizzazione iniziale coincide con il perimetro comunicato (doc. 04). Segnalarlo come rischio e' errore.

| ID | Tipo | Proposizione |
|---|---|---|
| B.40 | assenza | il deliverable non segnala come rischio, criticita' o inadempimento hosting iniziale a Milano (doc. 04). |

### N-04 - rinnovo ancora non firmato

Non e' un issue: la proposta non ha ancora modificato il contratto (doc. 06). Segnalarlo come rischio e' errore.

| ID | Tipo | Proposizione |
|---|---|---|
| B.41 | assenza | il deliverable non segnala come rischio, criticita' o inadempimento rinnovo ancora non firmato (doc. 06); elemento tracciato: rinnovo automatico. |

## Chiusura obbligatoria

| ID | Tipo | Proposizione |
|---|---|---|
| B.42 | assenza | il deliverable esamina i tre livelli della catena (contratto Arcomera-Veltragno, subcontratto Veltragno-Nembrosa, ordine Nembrosa-Quadir) con lo stesso test su SLA, audit e responsabilita'. |
| B.43 | assenza | il deliverable non afferma che una pretesa di Arcomera verso Veltragno sara' accolta. |
