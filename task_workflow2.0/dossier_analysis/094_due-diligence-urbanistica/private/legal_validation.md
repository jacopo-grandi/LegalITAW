# WF2-094 - Legal validation

**Stato: `draft_for_legal_validation`. Il caso non e `pilot_ready`.**

Questo file distingue tre cose che non vanno confuse: il self-check meccanico, che
e stato eseguito; la validazione giuridica professionale, che non lo e; la
calibrazione con judge reali, che non lo e.

## Domande per il sign-off

1. La qualificazione del soppalco non assentito come parziale difformità, e non come variazione essenziale, dipende dalla legge regionale che il fascicolo non contiene. Il caso chiede di sospendere quella qualificazione e di indicare che cosa manca: confermate l'impostazione, o preferite ancorare il caso a una regione determinata?

2. L'issue I-01 distingue l'obbligo relativo ai terreni da quello relativo al fabbricato. Confermate che, per un compendio composto da fabbricato e terreni pertinenziali sopra i 5.000 metri quadrati, entrambi gli adempimenti siano richiesti?

3. L'issue I-09 chiede di rilevare che il fascicolo non consente di quantificare l'oblazione. Confermate che il criterio corretto sia la commisurazione alle sole opere in difformità?

4. L'issue I-10 tratta la carenza di parcheggio come violazione di prescrizione del titolo e non come scostamento dimensionale. Confermate, e confermate che vada calcolata sulla superficie utile rilevata?

5. L'issue I-13 chiede di rilevare il rinvio alla disposizione abrogata senza dedurne l'inefficacia della segnalazione. Confermate che sia la posizione corretta da rappresentare all'acquirente?

6. L'issue I-15 chiede di collocare ciascun rilievo fra le difformità regolarizzabili e quelle non regolarizzabili ai fini delle condizioni contrattuali. Confermate la collocazione proposta nel gold, in particolare per la carenza di parcheggio?

## Punti che le fonti consultate non risolvono

Nessuno di questi e stato trasformato in criterio.

- Nessuna legge regionale è stata verificata. La determinazione delle variazioni essenziali è rimessa alla legge regionale, e il caso non attribuisce ad alcuna regione una disciplina determinata: la qualificazione resta sospesa e nessun criterio la richiede.
- Nessuno strumento urbanistico o regolamento edilizio comunale è stato verificato: le norme di attuazione allegate al certificato sono materiale sintetico e nessun criterio le presenta come fonte normativa.
- Il coordinamento fra la disposizione del testo unico che ammette l'accertamento di compatibilità paesaggistica anche per lavori che abbiano creato superfici utili e le disposizioni del codice dei beni culturali che lo escludono non è stato risolto: il caso non colloca l'immobile in area vincolata e nessun criterio dipende da quel coordinamento.
- Gli importi comunali del contributo di costruzione e degli oneri di urbanizzazione non sono stati verificati: l'importo che compare nel permesso è sintetico e nessun criterio richiede di quantificare l'oblazione.
- Nessuna pronuncia è stata verificata o citata.

## Effetto di una correzione

Una correzione che incida su una conclusione richiede l'aggiornamento coordinato di
challenge map, rubrica in prosa, criteri atomizzati, `rubric.json`,
`runtime_routing.json`, gold e distrattore: sono emessi da un'unica fonte
(`source/authoring/casi/wf2_094.py`), quindi si corregge la fonte e si riesegue
`source/gen/assembla_casi.py`.
