# WF2-036 — Criteri di valutazione (rubrica in prosa, a livello di issue)

Questa è la forma che l'avvocato legge, discute e firma. La forma atomizzata somministrata al
judge è in `private/criteria_atomized.md` e in `private/rubric.json`; il raccordo fra le due è
l'`issue_id`.

**Stato del fascicolo alla data di riferimento (lunedì 16 ottobre 2028).**

La bozza versione 2.0 è stata trasmessa il 5 ottobre 2028 e nulla è stato sottoscritto: il
contratto del 10 febbraio 2026 è quello che regola il rapporto. Il Software è in esercizio nella
versione 3.4, il corrispettivo di sviluppo è stato integralmente pagato, il codice sorgente è in
deposito presso un notaio e l'ultimo aggiornamento del deposito risale al 16 febbraio 2027. Il
fascicolo è *ex ante*: i criteri riguardano ciò che va chiesto prima di firmare, non l'esito di
una contestazione.

**Che cosa il prompt chiede.**

Un redline con revisioni tracciate, circoscritto a titolarità dei Risultati, componenti di terze
parti, deposito del codice sorgente, verifica dell'uso e responsabilità per pretese di terzi; una
nota delle modifiche con, per ciascuna, l'articolo o la definizione e la ragione; la verifica
delle affermazioni del referente commerciale; una risposta sul rischio attuale in materia di
software a codice aperto. Il prompt esclude espressamente corrispettivi, collaudo, massimale
dell'articolo 12, riservatezza, durata, dati personali e foro. La rubrica non verifica passaggi
che il prompt non chiede di esplicitare.

---

## Issue di merito

**I-01. La titolarità dei Risultati non è trasferita** — l'art. 6 non trasferisce al Cliente i
diritti di utilizzazione economica sui Risultati: gli concede una licenza non esclusiva, non
trasferibile e per uso interno sul codice sorgente, riservando al Fornitore ogni altro diritto. Il
redline deve sostituire la licenza con il trasferimento in via esclusiva dei diritti di
utilizzazione economica, senza limiti di tempo e di territorio, con facoltà di modifica,
elaborazione e trasferimento a terzi (documento 01, art. 6, commi 1 e 3)

**I-02. Il modulo di riconciliazione non è un Componente Preesistente** — l'Allegato B qualifica
il modulo motore-di-riconciliazione come Componente Preesistente del Fornitore sviluppato
anteriormente all'avvio del Progetto, ma il contratto d'opera con lo sviluppatore autonomo che lo
ha realizzato è del 4 maggio 2026, posteriore alla Data di Inizio del Progetto del 9 marzo 2026:
il modulo rientra nei Risultati. Il redline deve escluderlo dai Componenti Preesistenti oppure
ancorare la definizione dell'art. 1 alla Data di Inizio con onere della prova a carico del
Fornitore (documento 01, premesse e art. 1; documento 03, Allegato B; documento 05, data e
oggetto)

**I-03. Prova scritta della trasmissione dai collaboratori non dipendenti** — il Fornitore non è
tenuto a dimostrare di avere acquisito per iscritto i diritti dai collaboratori che non sono suoi
dipendenti. Il redline deve introdurre una dichiarazione e garanzia sull'acquisizione di quei
diritti e l'obbligo di consegnare copia degli atti scritti di trasmissione (documento 01, art. 6 e
art. 10; documento 05, art. 8; artt. 12-bis e 110 l. 633/1941)

**I-04. Cessione gratuita dei Miglioramenti del Cliente** — l'art. 6, comma 5, attribuisce al
Fornitore in via esclusiva e a titolo gratuito i diritti su ogni miglioramento, suggerimento,
segnalazione e specifica proveniente dal Cliente. Il redline deve circoscrivere la clausola alle
segnalazioni e ai suggerimenti in senso proprio, escludendo le informazioni riservate del Cliente
e la sua proprietà intellettuale preesistente (documento 01, art. 6, comma 5)

**I-05. La garanzia no-copyleft è tarata sulla sola distribuzione** — l'art. 7, comma 3,
garantisce che nessun componente imponga, in caso di distribuzione a terzi del Software, la messa
a disposizione del codice sorgente. Il componente melograno-reportd è rilasciato sotto AGPL-3.0,
è stato modificato ed è incluso nel Software consegnato, e il Software è esposto ai clienti del
Cliente attraverso il portale: l'obbligo della sezione 13 di quella licenza si attiva per effetto
dell'interazione remota attraverso una rete, non della distribuzione. Il redline deve estendere la
garanzia agli obblighi che si attivano per effetto dell'uso, dell'accesso o dell'interazione via
rete (documento 01, art. 7, comma 3; documento 03, riga melograno-reportd; documento 02, funzione
del portale; AGPL-3.0, sezione 13)

**I-06. Garanzia specifica e rimedio sul componente AGPL** — il redline deve introdurre una
dichiarazione e garanzia specifica sul componente melograno-reportd e l'obbligo del Fornitore di
sostituirlo o di rimuoverlo a proprie spese qualora l'obbligo di messa a disposizione del codice
sorgente risulti attivato (documento 03; documento 01, art. 7)

**I-07. L'Allegato B non è vincolante per il Fornitore** — l'art. 7, comma 4, consente al
Fornitore di modificare l'elenco dei componenti di terze parti anche senza preventiva
comunicazione al Cliente. Il redline deve subordinare l'inserimento di nuovi componenti e il
mutamento della licenza applicabile alla preventiva approvazione scritta del Cliente (documento
01, art. 7, comma 4)

**I-08. Gli eventi di rilascio del deposito non comprendono l'inadempimento** — l'art. 8 rinvia
all'Accordo di deposito per gli eventi che consentono il rilascio del Materiale Depositato;
l'Accordo li limita alla liquidazione giudiziale e alla cessazione dell'attività del Fornitore.
Il redline deve elencare nel contratto gli eventi di rilascio, comprendendovi l'inadempimento
grave e non sanato degli obblighi di manutenzione e correzione, e obbligare il Fornitore a far
modificare conformemente l'Accordo (documento 01, art. 8, comma 2; documento 04, art. 7)

**I-09. Il rilascio richiede la richiesta congiunta delle Parti** — l'Accordo di deposito prevede
che il depositario consegni il Materiale Depositato su richiesta congiunta delle Parti ovvero su
ordine dell'autorità giudiziaria: è il difetto che rende il deposito inutilizzabile, perché il
rilascio finisce per dipendere dal consenso del Fornitore inadempiente. Il redline deve prevedere
il rilascio su richiesta del solo Cliente, con facoltà del Fornitore di opporsi davanti a un
terzo entro un termine breve (documento 04, art. 8)

**I-10. Periodicità e perimetro del deposito** — l'obbligo di aggiornamento del deposito è
annuale, l'ultimo deposito risale al 16 febbraio 2027 e in produzione gira la versione 3.4
rilasciata il 5 settembre 2028: il Materiale Depositato è inservibile, e non comprende gli script
di compilazione e distribuzione, la documentazione tecnica e l'elenco delle dipendenze. Il redline
deve legare il deposito a ogni rilascio in produzione entro un termine breve, estendere il
perimetro del Materiale Depositato e prevedere una verifica periodica a spese del Fornitore
(documento 01, art. 8; documento 04, artt. 4 e 5; documento 07, versione in produzione)

**I-11. La verifica dell'uso è senza limiti** — l'art. 9 consente al Fornitore di verificare
l'uso del Software senza preavviso, per mezzo di un soggetto da lui designato e senza alcun
vincolo di riservatezza a carico del verificatore, con accesso ai sistemi del Cliente. Il redline
deve introdurre preavviso scritto, svolgimento in orario di lavoro, limite di frequenza,
verificatore indipendente vincolato alla riservatezza e non concorrente del Cliente, e perimetro
circoscritto ai dati di utilizzo del Software, con esclusione dell'accesso al codice e ai dati del
Cliente (documento 01, art. 9, commi 1 e 2)

**I-12. Assenza di un diritto di verifica simmetrico del Cliente** — il contratto non attribuisce
al Cliente alcun diritto di verificare la conformità delle licenze dei componenti di terze parti.
Il redline deve attribuire al Cliente il diritto di ottenere, con periodicità almeno annuale,
l'elenco aggiornato dei componenti con licenza, versione e tipo di collegamento, e un'attestazione
di conformità del Fornitore (documento 01, artt. 7 e 9)

**I-13. L'eccezione per i Componenti di Terze Parti svuota la manleva** — l'art. 11, comma 3,
lettera e), esclude dalla manleva le pretese che derivano dai Componenti di Terze Parti, che sono
però selezionati, integrati e forniti dal Fornitore ed elencati nell'Allegato B: l'eccezione
svuota la manleva proprio dove il rischio è concentrato. Il redline deve sopprimere l'eccezione
almeno per i componenti indicati nell'Allegato B (documento 01, art. 11, comma 3, lettera e);
documento 03)

**I-14. Il rimedio della manleva non garantisce l'equivalenza funzionale** — l'art. 11, comma 4,
consente al Fornitore di scegliere fra modificare e sostituire il Software, senza obbligo di
equivalenza funzionale, e in mancanza di recedere rimborsando i soli canoni del periodo residuo:
il Cliente resterebbe senza software e senza ristoro. Il redline deve imporre l'equivalenza
funzionale, attribuire al Cliente la facoltà di rifiutare una sostituzione non equivalente e
sostituire il rimborso dei canoni residui con un ristoro che comprenda i costi di migrazione
(documento 01, art. 11, comma 4)

**I-15. Controllo esclusivo della difesa e potere di transigere** — l'art. 11, comma 5,
attribuisce al Fornitore il controllo esclusivo della difesa e il potere di definire la pretesa in
via transattiva senza il consenso del Cliente. Il redline deve attribuire al Cliente il diritto di
partecipare alla difesa con propri difensori e vietare transazioni che comportino ammissioni di
responsabilità o obblighi a carico del Cliente senza il suo consenso scritto (documento 01, art.
11, comma 5)

**I-16. Che cosa non è determinabile dal fascicolo** — il fascicolo non contiene la distinta
delle dipendenze transitive né l'architettura di distribuzione degli ambienti: non è possibile
escludere la presenza di ulteriori componenti soggetti a licenze con obblighi di messa a
disposizione del codice sorgente, e non è possibile affermare che un obbligo del genere sia già
stato violato. Occorre acquisire la distinta completa delle dipendenze e la documentazione
dell'architettura di distribuzione (documento 03, che dichiara di riportare le sole dipendenze
dirette; documento 02, punto A.3, che rinvia al manuale tecnico di esercizio)

**I-17. Perimetro dell'intervento** — l'incarico circoscrive l'intervento a titolarità dei
Risultati, componenti di terze parti, deposito del codice sorgente, verifica dell'uso e
responsabilità per pretese di terzi, ed esclude espressamente corrispettivi, collaudo, massimale
dell'articolo 12, riservatezza, durata, dati personali e foro. Il redline non deve contenere
revisioni negli articoli esclusi e la nota non deve proporne la modifica (01_task.md, terzo
capoverso; documento 01, articoli 3, 4, 12, 13, 14, 15 e 16)

---

## Controlled non-issue (da non segnalare)

**N-01. Componente a licenza MIT** — la licenza MIT è permissiva e impone soltanto la
conservazione dell'avviso di copyright e del testo della licenza, obbligo che l'art. 7, comma 2,
della bozza già recepisce. Non produce alcun effetto di contaminazione, quale che sia il tipo di
collegamento. (oggetto: documento 03, riga quadrifoglio-orm; criterio B.30)

**N-02. Concessione di brevetto della licenza Apache-2.0** — la sezione 3 della licenza Apache-2.0
concede una licenza di brevetto perpetua e irrevocabile a favore di chi riceve l'opera: è una
clausola che avvantaggia il Cliente. Segnalarla fra i rischi è errore di lato. (oggetto:
documento 03, riga tessitura-http; criterio B.31)

**N-03. Componente LGPL-2.1 collegato dinamicamente e non modificato** — il componente non è
stato modificato ed è collegato dinamicamente come libreria condivisa. La sezione 6 della
LGPL-2.1 consente di distribuire l'opera che usa la libreria a condizioni di propria scelta, fermi
gli obblighi di avviso che l'art. 7, comma 2, della bozza già recepisce. Segnalare un rischio di
contaminazione è errore. (oggetto: documento 03, riga vetrata-charts; criterio B.32)

**N-04. Componente GPL-2.0 non incluso nel Software consegnato** — è uno strumento di
compilazione eseguito solo in fase di build e non è incluso nel Software consegnato al Cliente:
non entra nell'opera e non produce alcun effetto sulle sue condizioni di licenza. Segnalare un
rischio di contaminazione è errore. (oggetto: documento 03, riga ferrobatte-build; criterio B.33)

**N-05. Riserva del diritto di essere riconosciuti autori** — la clausola riserva agli autori il
diritto di essere riconosciuti tali. È un diritto morale, inalienabile per legge: la clausola non
sottrae al Cliente nulla che avrebbe potuto acquisire, e la sua soppressione non produrrebbe alcun
effetto. Segnalarla come limite alla titolarità è errore. (oggetto: documento 01, art. 6, comma
6; criterio B.34)

**N-06. Nessun diritto ulteriore sui Componenti di Terze Parti** — la clausola precisa che il
Cliente non acquisisce sui componenti di terze parti diritti diversi da quelli concessi dalle
rispettive licenze. Nessuno può concedere più di quanto la licenza del terzo consenta: la
clausola enuncia un limite che esiste comunque. Segnalarla come difetto è errore. (oggetto:
documento 01, art. 7, comma 1; criterio B.35)

**N-07. Efficacia subordinata all'integrale pagamento** — l'acquisto dei diritti è subordinato
all'integrale pagamento del corrispettivo, ma il medesimo comma concede al Cliente, nelle more, il
diritto di utilizzare il Software in ambiente di produzione. L'allarme riflesso è neutralizzato
dal correttivo di prassi ed è assetto ordinario. Segnalarlo come esposizione è errore. (oggetto:
documento 01, art. 6, comma 4; criterio B.36)

---

## Punti neutri, non valutati

- La clausola compromissoria dell'art. 16, redatta sul modello della clausola tipo della Camera
Arbitrale di Milano: fuori perimetro e non valutata in nessuna direzione.
- L'accettazione tacita del collaudo a quindici giorni dell'art. 4: fuori perimetro. Nessun
criterio la premia; il perimetro è presidiato dai criteri di sovra-intervento.
- La doppia sottoscrizione degli artt. 1341 e 1342 c.c. in chiusura del contratto: presente, e
deliberatamente non valutata. La leva è già impiegata da un caso esistente del benchmark.
- L'obbligo di mantenere il marchio del Fornitore nella schermata informativa del Software:
coincidenza di drafting neutra.
- La scelta fra cessione dei diritti e licenza esclusiva perpetua come tecnica redazionale del
rimedio: entrambe accettabili, purché il redline produca l'effetto richiesto. Nessun criterio
premia l'una o l'altra.

---

## Punti aperti per la validazione professionale

Sono elencati, in ordine di importanza, in `source/authoring/legal_validation.md`.
