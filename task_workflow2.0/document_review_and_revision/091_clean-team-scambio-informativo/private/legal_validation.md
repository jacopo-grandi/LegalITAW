# WF2-091 - Legal validation

**Stato: `draft_for_legal_validation`. Il caso non e `pilot_ready`.**

Questo file distingue tre cose che non vanno confuse: il self-check meccanico, che
e stato eseguito; la validazione giuridica professionale, che non lo e; la
calibrazione con judge reali, che non lo e.

## Domande per il sign-off

1. La qualificazione della proposta di allineamento del calendario promozionale come condotta da interrompere immediatamente, e non come questione di perimetro informativo, è quella che riterreste corretta in uno scenario reale?

2. L'impianto dell'issue I-16 tiene: sui dati dell'Allegato 1 non sorge obbligo di comunicazione preventiva, ma l'operazione ricade fra quelle di cui l'Autorità può richiedere la notifica perché una sola delle due soglie è superata. Confermate la lettura dell'art. 16, comma 1-bis?

3. Il controlled non-issue N-03 poggia sull'assenza, nella legge italiana, di un obbligo generale di sospensione dell'esecuzione: è la stessa asimmetria già registrata fra golden power e antitrust nazionale. Confermate che l'assenza di obbligo di sospensione sia affermabile in questi termini in un deliverable destinato al cliente?

4. La posizione minima proposta sulla clausola 6.2 è la soppressione integrale dell'eccezione. In una trattativa reale accettereste come fallback una restituzione disaggregata al solo consulente indipendente, senza restituzione alle parti?

5. La copia di difesa segregata introdotta nella revisione della clausola 10.1 è affidata ai responsabili affari legali delle parti per cinque anni. Il termine e il soggetto sono quelli che indichereste?

6. Il perimetro della revisione della clausola 3.3 è la soppressione dell'autoqualificazione. Ritenete preferibile sopprimerla o sostituirla con una dichiarazione di intento come quella proposta nel gold?

## Punti che le fonti consultate non risolvono

Nessuno di questi e stato trasformato in criterio.

- Non esiste una fonte ufficiale che elenchi le sezioni tipiche di un clean team protocol pre-closing: la struttura del documento sintetico è stata ricavata dai requisiti funzionali documentati nella decisione della Commissione nel caso M.7993 e dai punti 406-408 delle linee direttrici 2023. Nessun criterio verifica la conformità del documento a un modello ufficiale.
- Non è stato verificato l'atto che ha portato a novanta giorni il termine dell'art. 16, comma 8, della legge n. 287/1990: il termine non è usato in alcun criterio.
- Non sono state cercate rettifiche pubblicate dopo il 21 luglio 2023 alle linee direttrici 2023/C 259/01: i numeri di punto citati sono quelli della versione italiana consultata al freeze.
- Non è stata verificata alcuna pronuncia, italiana o europea, sul trattamento dello scambio informativo pre-closing in operazioni non notificabili. Nessun criterio poggia su giurisprudenza.
- Le linee direttrici non fissano una soglia temporale numerica per qualificare un dato come storico: la convenzione dei dodici mesi del term sheet è una scelta delle parti e nessun criterio la presenta come regola di fonte.

## Effetto di una correzione

Una correzione che incida su una conclusione richiede l'aggiornamento coordinato di
challenge map, rubrica in prosa, criteri atomizzati, `rubric.json`,
`runtime_routing.json`, gold e distrattore: sono emessi da un'unica fonte
(`source/authoring/casi/wf2_091.py`), quindi si corregge la fonte e si riesegue
`source/gen/assembla_casi.py`.
