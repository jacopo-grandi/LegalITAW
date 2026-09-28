# WF2-061 - Criteri atomizzati

Forma a campi somministrata al judge e alla verifica meccanica. Sorgente canonica: `rubric.json`.

## A.1 - esistono tutti i file di consegna nominati nel template.
`issue: A - tipo: struttura - gravita: alta - judge: no`
Pass se: ogni file atteso esiste con il nome indicato
Fail se: manca almeno un file atteso; non esistono esiti intermedi.
Fonte: response_template.md

## A.2 - il file Markdown principale non supera 3.200 parole.
`issue: A - tipo: valore - gravita: media - judge: no`
Pass se: il conteggio e' al massimo 3.200
Fail se: il conteggio supera 3.200; non esistono esiti intermedi.
Fonte: response_template.md

## A.3 - le sezioni obbligatorie compaiono nell'ordine del template.
`issue: A - tipo: struttura - gravita: media - judge: no`
Pass se: tutte le sezioni compaiono nell'ordine
Fail se: manca una sezione oppure l'ordine cambia; non esistono esiti intermedi.
Fonte: response_template.md

## A.4 - ogni allegato pubblico elencato nell'incarico e' richiamato almeno una volta nel deliverable.
`issue: A - tipo: struttura - gravita: media - judge: no`
Pass se: tutti gli allegati sono richiamati
Fail se: almeno un allegato non e' richiamato; non esistono esiti intermedi.
Fonte: 01_task.md

## A.5 - il deliverable non cita fonti esterne all'elenco chiuso.
`issue: A - tipo: assenza - gravita: alta - judge: no`
Pass se: ogni fonte citata compare in 03_legal_sources.md
Fail se: FAIL se compare almeno una fonte non inclusa nell'elenco chiuso; PASS negli altri casi.
Fonte: 03_legal_sources.md

## A.6 - fatti, inferenze e dati mancanti hanno etichette distinguibili.
`issue: A - tipo: struttura - gravita: media - judge: no`
Pass se: le tre categorie sono distinguibili
Fail se: almeno due categorie sono fuse; non esistono esiti intermedi.
Fonte: response_template.md

## B.1 - il deliverable afferma che Veltragno resta responsabile verso Arcomera anche quando la causa si colloca a valle.
`issue: I-01 - tipo: presenza - gravita: alta - judge: si`
Pass se: la proposizione compare in una frase autonoma: Veltragno resta responsabile verso Arcomera anche quando la causa si colloca a valle; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: Veltragno resta responsabile verso Arcomera anche quando la causa si colloca a valle
Fail se: FAIL se la proposizione «Veltragno resta responsabile verso Arcomera anche quando la causa si colloca a valle» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 01 clausola 12 e doc. 03

## B.2 - il deliverable afferma che la soglia 99,50% e il ripristino a 240 minuti non coprono gli impegni 99,95% e 120 minuti.
`issue: I-02 - tipo: valore - gravita: alta - judge: no`
Pass se: nel deliverable compare «la soglia 99,50% e il ripristino a 240 minuti non coprono gli impegni 99,95% e 120 minuti»
Fail se: FAIL se manca «la soglia 99,50% e il ripristino a 240 minuti non coprono gli impegni 99,95% e 120 minuti», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 02 e doc. 03

## B.3 - il deliverable afferma che Quadir non assume tempi di ripristino ne' exit assistance.
`issue: I-03 - tipo: presenza - gravita: alta - judge: si`
Pass se: la proposizione compare in una frase autonoma: Quadir non assume tempi di ripristino ne' exit assistance; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: Quadir non assume tempi di ripristino ne' exit assistance
Fail se: FAIL se la proposizione «Quadir non assume tempi di ripristino ne' exit assistance» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 03 e doc. 04

## B.4 - il deliverable afferma che il preavviso di un giorno non soddisfa la finestra di cinque giorni.
`issue: I-04 - tipo: valore - gravita: alta - judge: no`
Pass se: nel deliverable compare «il preavviso di un giorno non soddisfa la finestra di cinque giorni»
Fail se: FAIL se manca «il preavviso di un giorno non soddisfa la finestra di cinque giorni», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 02 e doc. 05

## B.5 - il deliverable afferma che l'esclusivita' pattuita a valle non limita i rimedi di Arcomera.
`issue: I-05 - tipo: presenza - gravita: alta - judge: si`
Pass se: la proposizione compare in una frase autonoma: l'esclusivita' pattuita a valle non limita i rimedi di Arcomera; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: l'esclusivita' pattuita a valle non limita i rimedi di Arcomera
Fail se: FAIL se la proposizione «l'esclusivita' pattuita a valle non limita i rimedi di Arcomera» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 01 e doc. 03

## B.6 - il deliverable afferma che Arcomera non puo' verificare direttamente i log dei soggetti a valle.
`issue: I-06 - tipo: presenza - gravita: alta - judge: si`
Pass se: la proposizione compare in una frase autonoma: Arcomera non puo' verificare direttamente i log dei soggetti a valle; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: Arcomera non puo' verificare direttamente i log dei soggetti a valle
Fail se: FAIL se la proposizione «Arcomera non puo' verificare direttamente i log dei soggetti a valle» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 01, doc. 03 e doc. 06

## B.7 - il deliverable afferma che la comunicazione successiva sul data center non consente controllo preventivo.
`issue: I-07 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: la comunicazione successiva sul data center non consente controllo preventivo; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: la comunicazione successiva sul data center non consente controllo preventivo
Fail se: FAIL se la proposizione «la comunicazione successiva sul data center non consente controllo preventivo» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 04

## B.8 - il deliverable afferma che il fascicolo non prova l'autorizzazione specifica o generale a Quadir.
`issue: I-08 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: il fascicolo non prova l'autorizzazione specifica o generale a Quadir; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: il fascicolo non prova l'autorizzazione specifica o generale a Quadir
Fail se: FAIL se la proposizione «il fascicolo non prova l'autorizzazione specifica o generale a Quadir» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 01 e doc. 04

## B.9 - il deliverable afferma che Veltragno promette novanta giorni di assistenza ma Quadir non e' vincolata.
`issue: I-09 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: Veltragno promette novanta giorni di assistenza ma Quadir non e' vincolata; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: Veltragno promette novanta giorni di assistenza ma Quadir non e' vincolata
Fail se: FAIL se la proposizione «Veltragno promette novanta giorni di assistenza ma Quadir non e' vincolata» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 01 e doc. 04

## B.10 - il deliverable afferma che il massimale Nembrosa di EUR 300.000 e' inferiore a quello assunto da Veltragno.
`issue: I-10 - tipo: valore - gravita: media - judge: no`
Pass se: nel deliverable compare «il massimale Nembrosa di EUR 300.000 e' inferiore a quello assunto da Veltragno»
Fail se: FAIL se manca «il massimale Nembrosa di EUR 300.000 e' inferiore a quello assunto da Veltragno», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 01 e doc. 03

## B.11 - il deliverable afferma che il rinnovo proposto non disciplina preavviso e opposizione alla sostituzione.
`issue: I-11 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: il rinnovo proposto non disciplina preavviso e opposizione alla sostituzione; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: il rinnovo proposto non disciplina preavviso e opposizione alla sostituzione
Fail se: FAIL se la proposizione «il rinnovo proposto non disciplina preavviso e opposizione alla sostituzione» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 01 e doc. 06

## B.12 - il deliverable afferma che i log Quadir non sono nel fascicolo.
`issue: I-12 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: i log Quadir non sono nel fascicolo; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: i log Quadir non sono nel fascicolo
Fail se: FAIL se la proposizione «i log Quadir non sono nel fascicolo» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 05 e doc. 06

## B.13 - il deliverable riconduce responsabilita' del contraente principale a doc. 01 clausola 12 e doc. 03.
`issue: I-01 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01 clausola 12 e doc. 03; un richiamo immediatamente adiacente collega il punto a doc. 01 clausola 12 e doc. 03
Fail se: FAIL se doc. 01 clausola 12 e doc. 03 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01 clausola 12 e doc. 03

## B.14 - il deliverable riconduce SLA non trasferiti al primo subfornitore a doc. 02 e doc. 03.
`issue: I-02 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 02 e doc. 03; un richiamo immediatamente adiacente collega il punto a doc. 02 e doc. 03
Fail se: FAIL se doc. 02 e doc. 03 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 02 e doc. 03

## B.15 - il deliverable riconduce secondo livello privo di flow-down a doc. 03 e doc. 04.
`issue: I-03 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 03 e doc. 04; un richiamo immediatamente adiacente collega il punto a doc. 03 e doc. 04
Fail se: FAIL se doc. 03 e doc. 04 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 03 e doc. 04

## B.16 - il deliverable riconduce manutenzione non programmata a doc. 02 e doc. 05.
`issue: I-04 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 02 e doc. 05; un richiamo immediatamente adiacente collega il punto a doc. 02 e doc. 05
Fail se: FAIL se doc. 02 e doc. 05 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 02 e doc. 05

## B.17 - il deliverable riconduce service credit non esclusivi nel contratto principale a doc. 01 e doc. 03.
`issue: I-05 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01 e doc. 03; un richiamo immediatamente adiacente collega il punto a doc. 01 e doc. 03
Fail se: FAIL se doc. 01 e doc. 03 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01 e doc. 03

## B.18 - il deliverable riconduce audit interrotto nella catena a doc. 01, doc. 03 e doc. 06.
`issue: I-06 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01, doc. 03 e doc. 06; un richiamo immediatamente adiacente collega il punto a doc. 01, doc. 03 e doc. 06
Fail se: FAIL se doc. 01, doc. 03 e doc. 06 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01, doc. 03 e doc. 06

## B.19 - il deliverable riconduce cambio di localizzazione a doc. 04.
`issue: I-07 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 04; un richiamo immediatamente adiacente collega il punto a doc. 04
Fail se: FAIL se doc. 04 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 04

## B.20 - il deliverable riconduce sub-responsabile non autorizzato a doc. 01 e doc. 04.
`issue: I-08 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01 e doc. 04; un richiamo immediatamente adiacente collega il punto a doc. 01 e doc. 04
Fail se: FAIL se doc. 01 e doc. 04 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01 e doc. 04

## B.21 - il deliverable riconduce exit assistance assente a valle a doc. 01 e doc. 04.
`issue: I-09 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01 e doc. 04; un richiamo immediatamente adiacente collega il punto a doc. 01 e doc. 04
Fail se: FAIL se doc. 01 e doc. 04 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01 e doc. 04

## B.22 - il deliverable riconduce massimali disallineati a doc. 01 e doc. 03.
`issue: I-10 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01 e doc. 03; un richiamo immediatamente adiacente collega il punto a doc. 01 e doc. 03
Fail se: FAIL se doc. 01 e doc. 03 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01 e doc. 03

## B.23 - il deliverable riconduce sostituzione del subfornitore a doc. 01 e doc. 06.
`issue: I-11 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01 e doc. 06; un richiamo immediatamente adiacente collega il punto a doc. 01 e doc. 06
Fail se: FAIL se doc. 01 e doc. 06 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01 e doc. 06

## B.24 - il deliverable riconduce causalita' ancora incompleta a doc. 05 e doc. 06.
`issue: I-12 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 05 e doc. 06; un richiamo immediatamente adiacente collega il punto a doc. 05 e doc. 06
Fail se: FAIL se doc. 05 e doc. 06 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 05 e doc. 06

## B.25 - il deliverable richiede rifiutare ogni rinvio diretto del reclamo a Nembrosa.
`issue: I-01 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «rifiutare ogni rinvio diretto del reclamo a Nembrosa» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «rifiutare ogni rinvio diretto del reclamo a Nembrosa» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01 clausola 12 e doc. 03

## B.26 - il deliverable richiede imporre flow-down integrale o buffer misurabile.
`issue: I-02 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «imporre flow-down integrale o buffer misurabile» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «imporre flow-down integrale o buffer misurabile» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 02 e doc. 03

## B.27 - il deliverable richiede estendere SLA, audit e uscita a Quadir.
`issue: I-03 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «estendere SLA, audit e uscita a Quadir» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «estendere SLA, audit e uscita a Quadir» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 03 e doc. 04

## B.28 - il deliverable richiede conteggiare i 94 minuti nella disponibilita' di febbraio.
`issue: I-04 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «conteggiare i 94 minuti nella disponibilita' di febbraio» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «conteggiare i 94 minuti nella disponibilita' di febbraio» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 02 e doc. 05

## B.29 - il deliverable richiede preservare risarcimento e rimedi contrattuali principali.
`issue: I-05 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «preservare risarcimento e rimedi contrattuali principali» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «preservare risarcimento e rimedi contrattuali principali» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01 e doc. 03

## B.30 - il deliverable richiede introdurre accesso per Arcomera o audit indipendente su Nembrosa e Quadir.
`issue: I-06 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «introdurre accesso per Arcomera o audit indipendente su Nembrosa e Quadir» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «introdurre accesso per Arcomera o audit indipendente su Nembrosa e Quadir» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01, doc. 03 e doc. 06

## B.31 - il deliverable richiede richiedere autorizzazione preventiva per trasferimenti fuori dal perimetro concordato.
`issue: I-07 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «richiedere autorizzazione preventiva per trasferimenti fuori dal perimetro concordato» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «richiedere autorizzazione preventiva per trasferimenti fuori dal perimetro concordato» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 04

## B.32 - il deliverable richiede acquisire la catena di nomina e il registro delle opposizioni.
`issue: I-08 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «acquisire la catena di nomina e il registro delle opposizioni» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «acquisire la catena di nomina e il registro delle opposizioni» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01 e doc. 04

## B.33 - il deliverable richiede replicare durata, formati e cooperazione nel contratto Quadir.
`issue: I-09 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «replicare durata, formati e cooperazione nel contratto Quadir» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «replicare durata, formati e cooperazione nel contratto Quadir» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01 e doc. 04

## B.34 - il deliverable richiede negoziare massimale e copertura assicurativa coerenti con l'esposizione.
`issue: I-10 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «negoziare massimale e copertura assicurativa coerenti con l'esposizione» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «negoziare massimale e copertura assicurativa coerenti con l'esposizione» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01 e doc. 03

## B.35 - il deliverable richiede inserire notifica preventiva e diritto di opposizione motivata.
`issue: I-11 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «inserire notifica preventiva e diritto di opposizione motivata» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «inserire notifica preventiva e diritto di opposizione motivata» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01 e doc. 06

## B.36 - il deliverable richiede sospendere l'attribuzione definitiva del primo incidente e acquisire i log.
`issue: I-12 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «sospendere l'attribuzione definitiva del primo incidente e acquisire i log» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «sospendere l'attribuzione definitiva del primo incidente e acquisire i log» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 05 e doc. 06

## B.37 - il deliverable indica come conseguenza di responsabilita' del contraente principale che la catena contrattuale non spezza il rapporto principale.
`issue: I-01 - tipo: presenza - gravita: alta - judge: si`
Pass se: la conseguenza e' espressa nel testo: la catena contrattuale non spezza il rapporto principale; la conseguenza compare in una cella dedicata della matrice: la catena contrattuale non spezza il rapporto principale
Fail se: FAIL se manca «la catena contrattuale non spezza il rapporto principale» o compare una conseguenza incompatibile; PASS solo in uno dei due casi elencati.
Indifferente: collocazione in prosa o tabella.
Fonte: doc. 01 clausola 12 e doc. 03

## B.38 - il deliverable non segnala come rischio, criticita' o inadempimento cifratura a riposo (doc. 04).
`issue: N-01 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - cifratura a riposo non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - cifratura a riposo e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 04

## B.39 - il deliverable non segnala come rischio, criticita' o inadempimento primo evento unico (doc. 05); elemento tracciato: segnalazioni filiali.
`issue: N-02 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - primo evento unico non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - primo evento unico e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 05

## B.40 - il deliverable non segnala come rischio, criticita' o inadempimento hosting iniziale a Milano (doc. 04).
`issue: N-03 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - hosting iniziale a Milano non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - hosting iniziale a Milano e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 04

## B.41 - il deliverable non segnala come rischio, criticita' o inadempimento rinnovo ancora non firmato (doc. 06); elemento tracciato: rinnovo automatico.
`issue: N-04 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - rinnovo ancora non firmato non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - rinnovo ancora non firmato e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 06

## B.42 - il deliverable esamina i tre livelli della catena (contratto Arcomera-Veltragno, subcontratto Veltragno-Nembrosa, ordine Nembrosa-Quadir) con lo stesso test su SLA, audit e responsabilita'.
`issue: CHIUSURA - tipo: presenza - gravita: media - judge: si`
Pass se: per ciascuna delle voci indicate nell'oggetto del criterio il deliverable riporta tutti gli elementi richiesti, applicando a ogni voce lo stesso test
Fail se: almeno una delle voci non e' esaminata, oppure per almeno una voce manca uno degli elementi richiesti, oppure le voci sono esaminate con criteri diversi senza che la differenza sia motivata
Indifferente: l'ordine delle voci, la forma (tabella o testo) e la scelta lessicale, purche' ogni elemento sia riconoscibile per ciascuna voce
Fonte: doc. 01, doc. 03 e doc. 04

## B.43 - il deliverable non afferma che una pretesa di Arcomera verso Veltragno sara' accolta.
`issue: CHIUSURA - tipo: assenza - gravita: alta - judge: si`
Pass se: presunzione dell'esito non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se presunzione dell'esito e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: 01_task.md
