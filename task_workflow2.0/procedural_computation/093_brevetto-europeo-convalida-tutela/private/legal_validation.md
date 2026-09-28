# WF2-093 - Legal validation

**Stato: `draft_for_legal_validation`. Il caso non e `pilot_ready`.**

Questo file distingue tre cose che non vanno confuse: il self-check meccanico, che
e stato eseguito; la validazione giuridica professionale, che non lo e; la
calibrazione con judge reali, che non lo e.

## Domande per il sign-off

1. L'issue I-04 poggia sulla distinzione fra opposizione considerata non proposta e opposizione rigettata per inammissibilità, che le Guidelines tengono separate. Confermate che, sul materiale del fascicolo pubblico, la circostanza sia sollevabile dal titolare e non debba essere rilevata d'ufficio?

2. L'issue I-05 conclude che nessuna disposizione della Convenzione prevede la sospensione automatica. È una conclusione argomentativa dal combinato di più articoli e non una citazione di norma. Confermate la formulazione, e confermate che l'eventuale sospensione discrezionale del giudizio nazionale resti fuori dal perimetro del caso?

3. L'issue I-07 e l'issue I-08 costruiscono l'asimmetria fra contraffazione e nullità. Confermate che l'asimmetria vada rappresentata al cliente in questi termini?

4. L'issue I-09 richiede che la traduzione rettificata sia resa accessibile al pubblico o notificata al presunto contraffattore. Nel caso concreto indichereste la notificazione, che è più rapida, o la messa a disposizione presso l'Ufficio?

5. L'issue I-10 tiene aperta la salvezza del preuso perché il fascicolo non dice da quando il concorrente distribuisce il prodotto. Confermate che questa sia la risposta corretta e non prudenza eccessiva?

6. L'issue I-14 conclude che il termine per l'inizio del giudizio di merito non è determinabile alla data di riferimento. Confermate, e confermate che l'art. 132 nel testo in vigore dal 12 giugno 2026 sia quello applicabile a un provvedimento richiesto dopo tale data?

## Punti che le fonti consultate non risolvono

Nessuno di questi e stato trasformato in criterio.

- L'importo della tassa di opposizione e le disposizioni del regolamento sulle tasse relative alla data in cui il pagamento si considera effettuato non sono stati verificati sul testo del regolamento: il caso poggia sulla nota a stampa dell'estratto di conto, che è un fatto del documento, e sulla regola dell'art. 99(1) della Convenzione.
- L'elenco dei giorni di chiusura degli uffici di deposito dell'Ufficio europeo per il 2026 non è stato verificato: il 28 ottobre 2026 è un mercoledì e non è festività nazionale italiana, ma la proroga prevista dalla Regola 134(1) dipende dal calendario dell'Ufficio. Nessun criterio dipende da quella proroga.
- Le decisioni della Commissione allargata di ricorso richiamate dalle Guidelines non sono state consultate. Nessun criterio poggia su di esse.
- Le norme del codice di procedura civile richiamate dagli artt. 129, 130 e 132 del Codice della proprietà industriale non sono state consultate: i presupposti cautelari non sono oggetto di alcun criterio.
- La sospensione discrezionale del giudizio nazionale in pendenza di opposizione non è stata verificata su alcuna norma processuale e non è oggetto di alcun criterio.
- L'importo del diritto di mora sulle annualità e il decreto ministeriale che lo fissa non sono stati verificati: il caso non richiede alcun calcolo di mora, perché il pagamento è tempestivo.

## Effetto di una correzione

Una correzione che incida su una conclusione richiede l'aggiornamento coordinato di
challenge map, rubrica in prosa, criteri atomizzati, `rubric.json`,
`runtime_routing.json`, gold e distrattore: sono emessi da un'unica fonte
(`source/authoring/casi/wf2_093.py`), quindi si corregge la fonte e si riesegue
`source/gen/assembla_casi.py`.
