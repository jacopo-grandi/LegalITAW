# WF2-096 - Legal validation

**Stato: `draft_for_legal_validation`. Il caso non e `pilot_ready`.**

Questo file distingue tre cose che non vanno confuse: il self-check meccanico, che
e stato eseguito; la validazione giuridica professionale, che non lo e; la
calibrazione con judge reali, che non lo e.

## Domande per il sign-off

1. L'issue I-04 àncora la proroga comunque accordata all'accertamento contenuto nella determinazione di revoca. Confermate che un'ordinanza revocata con accertamento dell'insussistenza della difformità integri l'iniziativa dell'amministrazione rivelatasi poi infondata?

2. L'issue I-10 sospende la qualificazione della variante perché la determinazione delle variazioni essenziali è rimessa alla legge regionale. Confermate l'impostazione, o preferite ancorare il caso a una regione determinata?

3. L'issue I-12 chiede di verificare la necessità di un nuovo assenso paesaggistico prima dell'esecuzione. Confermate che la modifica dei materiali prescritti dall'autorizzazione e l'arretramento della facciata richiedano quella verifica preventiva?

4. L'issue I-14 tratta la conseguenza della scadenza del termine come limitata alla parte non eseguita. Confermate, e confermate che il ricalcolo del contributo vada indicato come eventuale?

5. Il gold indica lo slittamento in quarantasei giorni di calendario. Confermate che sia la misura corretta rispetto a un cronoprogramma espresso in giorni di calendario?

6. Il gold consiglia di presentare l'istanza di proroga adesso, pur essendo il termine lontano, per fissare l'evidenza dell'interruzione. Confermate che sia la scelta che consigliereste?

## Punti che le fonti consultate non risolvono

Nessuno di questi e stato trasformato in criterio.

- Nessuna legge regionale è stata verificata: la determinazione delle variazioni essenziali è rimessa alla legge regionale e il caso non attribuisce ad alcuna regione una disciplina determinata. Nessun criterio richiede la qualificazione della variante.
- Nessun regolamento edilizio o strumento urbanistico comunale è stato verificato: le prescrizioni che compaiono nei documenti sono materiale sintetico.
- Il coordinamento fra la disposizione del testo unico che ammette l'accertamento di compatibilità paesaggistica anche per lavori che abbiano creato superfici utili e le disposizioni del codice dei beni culturali che lo escludono non è stato risolto: nessun criterio dipende da quel coordinamento e il caso chiede l'assenso preventivo.
- Gli importi comunali del contributo di costruzione non sono stati verificati: l'importo che compare nel permesso è sintetico e nessun criterio richiede di quantificare il ricalcolo.
- Nessuna pronuncia è stata verificata o citata. In particolare non è stata verificata alcuna pronuncia sull'ambito della proroga comunque accordata.

## Effetto di una correzione

Una correzione che incida su una conclusione richiede l'aggiornamento coordinato di
challenge map, rubrica in prosa, criteri atomizzati, `rubric.json`,
`runtime_routing.json`, gold e distrattore: sono emessi da un'unica fonte
(`source/authoring/casi/wf2_096.py`), quindi si corregge la fonte e si riesegue
`source/gen/assembla_casi.py`.
