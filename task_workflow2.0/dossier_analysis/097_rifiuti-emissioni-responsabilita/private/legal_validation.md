# WF2-097 - Legal validation

**Stato: `draft_for_legal_validation`. Il caso non e `pilot_ready`.**

Questo file distingue tre cose che non vanno confuse: il self-check meccanico, che
e stato eseguito; la validazione giuridica professionale, che non lo e; la
calibrazione con judge reali, che non lo e.

## Domande per il sign-off

1. L'issue I-11 si limita ad affermare che il deposito non è più coperto dalla previsione che lo esonera dall'autorizzazione, senza qualificare la fattispecie sanzionatoria, perché il reference pack non contiene le norme sanzionatorie in materia di rifiuti. Confermate questa delimitazione, o volete che il caso arrivi alla qualificazione sanzionatoria, con l'integrazione delle fonti che ne consegue?

2. L'issue I-05 tratta l'esposizione dell'ente come dipendente esclusivamente dall'ipotesi aggravata. Confermate che la violazione del comma 2 semplice non sia reato presupposto e che il memo debba dirlo?

3. L'issue I-04 qualifica il mancato autocontrollo semestrale come violazione di prescrizione dell'autorizzazione. Confermate che la periodicità del monitoraggio, fissata nell'allegato tecnico, sia una prescrizione ai fini della sanzione amministrativa?

4. Il caso non risolve la questione se il direttore dello stabilimento sia il gestore. Confermate l'impostazione, e confermate che il memo debba indicare la deliberazione consiliare e i dati sui poteri di spesa fra gli elementi da acquisire?

5. Il gold indica fra le azioni la presentazione immediata della domanda di rinnovo, senza affermare che la domanda tardiva consenta la prosecuzione dell'esercizio dopo la scadenza. Confermate questa cautela?

6. Il gold non consiglia di comunicare spontaneamente all'autorità l'esito del rapporto di prova del 3 agosto 2026 e si limita a rilevare che nessuna comunicazione risulta. Confermate, o volete che il caso richieda una valutazione su quel punto?

## Punti che le fonti consultate non risolvono

Nessuno di questi e stato trasformato in criterio.

- Il testo integrale del comma 7 dell'articolo 269 non è stato letto su fonte primaria in questa sessione: fra il periodo sulla domanda di rinnovo e il periodo sul rinnovo imposto dall'autorità il testo contiene un ulteriore periodo che non è stato verificato. Nessun criterio dipende da esso e il gold non afferma né nega che la domanda tardiva consenta la prosecuzione dell'esercizio dopo la scadenza. Prima della validazione professionale il comma va riletto integralmente su Normattiva.
- Le norme sanzionatorie in materia di rifiuti non sono state verificate e non figurano nel reference pack: nessun criterio richiede di qualificare sotto il profilo sanzionatorio il superamento del sotto-limite del deposito temporaneo, l'annotazione tardiva sul registro o la mancata restituzione della copia del formulario.
- Il testo del decreto ministeriale 4 aprile 2023, n. 59, non è stato letto: i modelli di registro e di formulario riprodotti nei documenti seguono i modelli pubblicati dal Registro elettronico nazionale, e nessun criterio richiede di citarne un articolo.
- Nessun codice dell'elenco europeo dei rifiuti è stato verificato sull'allegato D: i codici che compaiono nei documenti sono materiale sintetico e nessun criterio dipende dalla loro correttezza.
- Gli allegati alla parte quinta non sono stati esaminati e nessun valore limite di emissione di fonte legislativa è verificato: i valori limite che compaiono nei documenti sono quelli fissati dall'autorizzazione sintetica e nessun criterio richiede di confrontarli con i valori minimi di legge.
- Gli effetti di una delega interna o di una procura sull'imputazione degli obblighi ambientali sono materia di elaborazione giurisprudenziale: nessuna pronuncia è stata verificata né citata, e nessun criterio richiede di risolvere la questione.
- La natura non impugnabile del verbale di prescrizioni è affermata dalle linee guida del sistema nazionale per la protezione dell'ambiente e non dal testo di legge: la questione non figura fra i criteri.
- Nessuna disposizione regionale è stata verificata: l'individuazione dell'autorità competente al rilascio dell'autorizzazione alle emissioni è rimessa dalla legge alla regione, e il caso non attribuisce ad alcuna regione una disciplina determinata.

## Effetto di una correzione

Una correzione che incida su una conclusione richiede l'aggiornamento coordinato di
challenge map, rubrica in prosa, criteri atomizzati, `rubric.json`,
`runtime_routing.json`, gold e distrattore: sono emessi da un'unica fonte
(`source/authoring/casi/wf2_097.py`), quindi si corregge la fonte e si riesegue
`source/gen/assembla_casi.py`.
