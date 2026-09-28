# WF2-099 - Legal validation

**Stato: `draft_for_legal_validation`. Il caso non e `pilot_ready`.**

Questo file distingue tre cose che non vanno confuse: il self-check meccanico, che
e stato eseguito; la validazione giuridica professionale, che non lo e; la
calibrazione con judge reali, che non lo e.

## Domande per il sign-off

1. L'issue I-04 sposta la definizione di completamento sulla certificazione provinciale. Confermate che sia l'atto cui ancorare il completamento e la conformità al progetto, e confermate che il deliverable non debba attribuirle effetti ulteriori rispetto allo svincolo delle garanzie?

2. L'issue I-09 fa salvi gli obblighi e la facoltà che la legge riconosce al proprietario non responsabile. Confermate che gli obblighi si limitino alla comunicazione e alle misure di prevenzione e che la facoltà di intervento volontario non possa essere rinunciata per contratto?

3. L'issue I-12 fa salvo il diritto di rivalsa della proprietaria per il caso in cui provveda essa alla bonifica. Confermate che una rinuncia contrattuale a ogni pretesa presente e futura non possa comunque comprendere quel diritto, o preferite che il deliverable si limiti a chiedere l'esclusione espressa?

4. L'issue I-14 tratta il ritardo nell'avvio dei lavori come inadempimento verso l'autorità che riguarda il sito. Confermate l'impostazione e confermate che il deliverable non debba qualificarne le conseguenze, che il reference pack non consente di verificare?

5. Il gold non chiede penali per il ritardo del proponente e si limita al recepimento del termine del decreto e al rendiconto. Confermate la scelta, o volete che il caso richieda anche una penale?

6. Il gold indica come posizione minima sulla rinuncia il differimento al rilascio della certificazione, anche senza la delimitazione per matrici e aree. Confermate che sia la posizione minima corretta?

## Punti che le fonti consultate non risolvono

Nessuno di questi e stato trasformato in criterio.

- Le norme civilistiche sull'accordo transattivo, sulla rinuncia e sui suoi limiti non sono state verificate su fonte primaria: non figurano nel reference pack e nessun criterio dipende da esse. Il caso è costruito sul solo profilo ambientale e sulla lettura del testo contrattuale.
- Le norme sanzionatorie applicabili al ritardo nell'esecuzione degli interventi approvati non sono state verificate: nessun criterio richiede di qualificare le conseguenze del mancato avvio dei lavori entro il termine del decreto.
- Le disposizioni sull'iscrizione all'Albo nazionale dei gestori ambientali per l'attività di bonifica dei siti non figurano nel reference pack di questo caso: il criterio sul controlled non-issue relativo all'appaltatore si fonda sul contenuto della bozza e non su una disposizione di legge.
- Nessun prezzario regionale è stato verificato: i prezzi unitari e le quantità del computo metrico sono materiale sintetico e nessun criterio richiede di verificarne la congruità. È verificata la sola somma delle voci.
- Nessuna disciplina regionale in materia di bonifiche è stata verificata: il decreto riprodotto nel fascicolo segue la struttura di un provvedimento reale ma non è ancorato ad alcuna disposizione regionale determinata.
- Nessuna pronuncia è stata verificata o citata, in particolare sulla posizione del proprietario non responsabile, sui limiti di una rinuncia preventiva e sull'efficacia liberatoria della certificazione di avvenuta bonifica.

## Effetto di una correzione

Una correzione che incida su una conclusione richiede l'aggiornamento coordinato di
challenge map, rubrica in prosa, criteri atomizzati, `rubric.json`,
`runtime_routing.json`, gold e distrattore: sono emessi da un'unica fonte
(`source/authoring/casi/wf2_099.py`), quindi si corregge la fonte e si riesegue
`source/gen/assembla_casi.py`.
