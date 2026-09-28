# WF2-100 - Legal validation

**Stato: `draft_for_legal_validation`. Il caso non e `pilot_ready`.**

Questo file distingue tre cose che non vanno confuse: il self-check meccanico, che
e stato eseguito; la validazione giuridica professionale, che non lo e; la
calibrazione con judge reali, che non lo e.

## Domande per il sign-off

1. L'issue I-04 tratta il termine di quarantotto ore come non in gioco perché il superamento è accertato. Confermate che l'autocertificazione di ripristino operi soltanto nell'ipotesi di soglie non superate e che la sua scadenza non produca conseguenze nel caso?

2. L'issue I-05 àncora il dies a quo dei trenta giorni alla notizia del superamento. Confermate che la notizia data sulla base di uno screening di campo, e non del rapporto di prova, sia il fatto da cui il termine decorre, o preferite ancorare il caso al rapporto di prova?

3. L'issue I-12 e l'issue I-13 tengono distinte la cedevolezza delle soglie rispetto ai valori di fondo e la procedura per determinarli. Confermate che il gold non debba affermare che il superamento viene meno, ma soltanto che il confronto con il valore tabellare non è definitivo?

4. L'issue I-16 attribuisce alla provincia l'ordinanza-diffida. Confermate, e confermate che il deliverable non debba qualificare le conseguenze sanzionatorie del ritardo, che il reference pack non consente di verificare?

5. Il gold consiglia di presentare il piano di caratterizzazione immediatamente e di trasmettere contestualmente il rapporto di prova del 1 ottobre 2026, mai comunicato. Confermate che sia la scelta che consigliereste?

6. Il gold espone la catena dei termini successivi come calcolo condizionato all'ipotesi di presentazione del piano alla data di riferimento. Confermate che sia il modo corretto di rispondere alla domanda del consiglio, o preferite che il gold si limiti alle sole decorrenze?

## Punti che le fonti consultate non risolvono

Nessuno di questi e stato trasformato in criterio.

- L'Allegato 5 al Titolo V della Parte quarta non figura nel reference pack di questo caso: i valori tabellari di 500 e di 1.000 milligrammi per chilogrammo compaiono nel rapporto di prova come limiti di riferimento indicati dal committente, e i criteri sul superamento poggiano sul giudizio di conformità che il rapporto esprime, non su un confronto con l'allegato. Prima della validazione professionale i due valori vanno riletti sull'allegato, che su Normattiva è disponibile soltanto in formato grafico.
- L'Allegato 2 alla Parte quarta, che individua i requisiti di contenuto del piano di caratterizzazione, non è stato esaminato: nessun criterio richiede di indicare il contenuto del piano, e la lacuna è dichiarata nella challenge map.
- L'Allegato 1 alla Parte quarta, che contiene i criteri dell'analisi di rischio, non è stato esaminato: nessun criterio richiede di indicare come l'analisi di rischio si svolge.
- Le norme sanzionatorie applicabili al ritardo nella presentazione del piano di caratterizzazione non sono state verificate: nessun criterio richiede di qualificare le conseguenze del ritardo, e il gold si limita alla conseguenza procedimentale prevista dall'art. 244.
- Nessuna disciplina regionale è stata verificata: le amministrazioni e i provvedimenti che compaiono nel fascicolo seguono la struttura di atti reali ma non sono ancorati ad alcuna disposizione regionale determinata.
- Nessuna pronuncia è stata verificata o citata, in particolare sull'individuazione del responsabile e sull'ambito dell'ordinanza-diffida provinciale.
- I metodi analitici e i valori di incertezza che compaiono nel rapporto di prova sono materiale sintetico coerente con la struttura di un rapporto reale; nessun criterio richiede di verificarne la correttezza metrologica.

## Effetto di una correzione

Una correzione che incida su una conclusione richiede l'aggiornamento coordinato di
challenge map, rubrica in prosa, criteri atomizzati, `rubric.json`,
`runtime_routing.json`, gold e distrattore: sono emessi da un'unica fonte
(`source/authoring/casi/wf2_100.py`), quindi si corregge la fonte e si riesegue
`source/gen/assembla_casi.py`.
