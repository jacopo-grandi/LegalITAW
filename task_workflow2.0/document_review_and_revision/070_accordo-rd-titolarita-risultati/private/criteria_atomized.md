# WF2-070 - Criteri atomizzati

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

## A.7 - il DOCX di consegna contiene almeno un inserimento tracciato w:ins.
`issue: A - tipo: struttura - gravita: alta - judge: no`
Pass se: e' presente almeno un w:ins
Fail se: non e' presente alcun w:ins; non esistono esiti intermedi.
Fonte: response_template.md

## A.8 - il DOCX di consegna contiene almeno una cancellazione tracciata w:del.
`issue: A - tipo: struttura - gravita: alta - judge: no`
Pass se: e' presente almeno un w:del
Fail se: non e' presente alcun w:del; non esistono esiti intermedi.
Fonte: response_template.md

## B.1 - il deliverable afferma che la comunione automatica trasferisce asset preesistenti.
`issue: I-01 - tipo: presenza - gravita: alta - judge: si`
Pass se: la proposizione compare in una frase autonoma: la comunione automatica trasferisce asset preesistenti; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: la comunione automatica trasferisce asset preesistenti
Fail se: FAIL se la proposizione «la comunione automatica trasferisce asset preesistenti» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 01 art. 4 e doc. 02

## B.2 - il deliverable afferma che manca il codice sorgente e la versione depositata.
`issue: I-02 - tipo: presenza - gravita: alta - judge: si`
Pass se: la proposizione compare in una frase autonoma: manca il codice sorgente e la versione depositata; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: manca il codice sorgente e la versione depositata
Fail se: FAIL se la proposizione «manca il codice sorgente e la versione depositata» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 02

## B.3 - il deliverable afferma che il testo ignora team misti e finanziamento Eterea.
`issue: I-03 - tipo: presenza - gravita: alta - judge: si`
Pass se: la proposizione compare in una frase autonoma: il testo ignora team misti e finanziamento Eterea; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: il testo ignora team misti e finanziamento Eterea
Fail se: FAIL se la proposizione «il testo ignora team misti e finanziamento Eterea» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 01 art. 5 e doc. 03

## B.4 - il deliverable afferma che Eterea non puo' industrializzare o trasferire.
`issue: I-04 - tipo: presenza - gravita: alta - judge: si`
Pass se: la proposizione compare in una frase autonoma: Eterea non puo' industrializzare o trasferire; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: Eterea non puo' industrializzare o trasferire
Fail se: FAIL se la proposizione «Eterea non puo' industrializzare o trasferire» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 01

## B.5 - il deliverable afferma che mancano gestione, costi e licenze reciproche.
`issue: I-05 - tipo: presenza - gravita: alta - judge: si`
Pass se: la proposizione compare in una frase autonoma: mancano gestione, costi e licenze reciproche; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: mancano gestione, costi e licenze reciproche
Fail se: FAIL se la proposizione «mancano gestione, costi e licenze reciproche» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 03

## B.6 - il deliverable afferma che la clausola generica non identifica diritti e risultati.
`issue: I-06 - tipo: presenza - gravita: alta - judge: si`
Pass se: la proposizione compare in una frase autonoma: la clausola generica non identifica diritti e risultati; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: la clausola generica non identifica diritti e risultati
Fail se: FAIL se la proposizione «la clausola generica non identifica diritti e risultati» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 04

## B.7 - il deliverable afferma che nessuna Parte deve esibire gli atti.
`issue: I-07 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: nessuna Parte deve esibire gli atti; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: nessuna Parte deve esibire gli atti
Fail se: FAIL se la proposizione «nessuna Parte deve esibire gli atti» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 01 e doc. 04

## B.8 - il deliverable afferma che Cobalt puo' depositare e abbandonare da sola.
`issue: I-08 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: Cobalt puo' depositare e abbandonare da sola; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: Cobalt puo' depositare e abbandonare da sola
Fail se: FAIL se la proposizione «Cobalt puo' depositare e abbandonare da sola» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 01 e doc. 06

## B.9 - il deliverable afferma che la demo del 20 dicembre puo' anticipare il deposito.
`issue: I-09 - tipo: valore - gravita: media - judge: no`
Pass se: nel deliverable compare «la demo del 20 dicembre puo' anticipare il deposito»
Fail se: FAIL se manca «la demo del 20 dicembre puo' anticipare il deposito», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 06

## B.10 - il deliverable afferma che quindici giorni non bastano per brevetto e riservatezza.
`issue: I-10 - tipo: valore - gravita: media - judge: no`
Pass se: nel deliverable compare «quindici giorni non bastano per brevetto e riservatezza»
Fail se: FAIL se manca «quindici giorni non bastano per brevetto e riservatezza», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 05

## B.11 - il deliverable afferma che ogni licenza e' ammessa senza registro.
`issue: I-11 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: ogni licenza e' ammessa senza registro; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: ogni licenza e' ammessa senza registro
Fail se: FAIL se la proposizione «ogni licenza e' ammessa senza registro» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 01 e doc. 05

## B.12 - il deliverable afferma che il dataset motori non ha scheda di provenienza.
`issue: I-12 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: il dataset motori non ha scheda di provenienza; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: il dataset motori non ha scheda di provenienza
Fail se: FAIL se la proposizione «il dataset motori non ha scheda di provenienza» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 01 e doc. 02

## B.13 - il deliverable afferma che terminano anche licenze necessarie ai risultati.
`issue: I-13 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: terminano anche licenze necessarie ai risultati; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: terminano anche licenze necessarie ai risultati
Fail se: FAIL se la proposizione «terminano anche licenze necessarie ai risultati» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 01 art. 10

## B.14 - il deliverable riconduce Background assorbito a doc. 01 art. 4 e doc. 02.
`issue: I-01 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01 art. 4 e doc. 02; un richiamo immediatamente adiacente collega il punto a doc. 01 art. 4 e doc. 02
Fail se: FAIL se doc. 01 art. 4 e doc. 02 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01 art. 4 e doc. 02

## B.15 - il deliverable riconduce Background incompleto a doc. 02.
`issue: I-02 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 02; un richiamo immediatamente adiacente collega il punto a doc. 02
Fail se: FAIL se doc. 02 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 02

## B.16 - il deliverable riconduce Foreground tutto a Cobalt a doc. 01 art. 5 e doc. 03.
`issue: I-03 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01 art. 5 e doc. 03; un richiamo immediatamente adiacente collega il punto a doc. 01 art. 5 e doc. 03
Fail se: FAIL se doc. 01 art. 5 e doc. 03 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01 art. 5 e doc. 03

## B.17 - il deliverable riconduce licenza revocabile e interna a doc. 01.
`issue: I-04 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01; un richiamo immediatamente adiacente collega il punto a doc. 01
Fail se: FAIL se doc. 01 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01

## B.18 - il deliverable riconduce regole sui risultati congiunti a doc. 03.
`issue: I-05 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 03; un richiamo immediatamente adiacente collega il punto a doc. 03
Fail se: FAIL se doc. 03 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 03

## B.19 - il deliverable riconduce collaboratrice autonoma a doc. 04.
`issue: I-06 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 04; un richiamo immediatamente adiacente collega il punto a doc. 04
Fail se: FAIL se doc. 04 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 04

## B.20 - il deliverable riconduce evidenza delle cessioni a doc. 01 e doc. 04.
`issue: I-07 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01 e doc. 04; un richiamo immediatamente adiacente collega il punto a doc. 01 e doc. 04
Fail se: FAIL se doc. 01 e doc. 04 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01 e doc. 04

## B.21 - il deliverable riconduce brevetti unilaterali a doc. 01 e doc. 06.
`issue: I-08 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01 e doc. 06; un richiamo immediatamente adiacente collega il punto a doc. 01 e doc. 06
Fail se: FAIL se doc. 01 e doc. 06 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01 e doc. 06

## B.22 - il deliverable riconduce demo prima della tutela a doc. 06.
`issue: I-09 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 06; un richiamo immediatamente adiacente collega il punto a doc. 06
Fail se: FAIL se doc. 06 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 06

## B.23 - il deliverable riconduce preavviso pubblicazione breve a doc. 05.
`issue: I-10 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 05; un richiamo immediatamente adiacente collega il punto a doc. 05
Fail se: FAIL se doc. 05 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 05

## B.24 - il deliverable riconduce open source non governato a doc. 01 e doc. 05.
`issue: I-11 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01 e doc. 05; un richiamo immediatamente adiacente collega il punto a doc. 01 e doc. 05
Fail se: FAIL se doc. 01 e doc. 05 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01 e doc. 05

## B.25 - il deliverable riconduce dataset di terzi a doc. 01 e doc. 02.
`issue: I-12 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01 e doc. 02; un richiamo immediatamente adiacente collega il punto a doc. 01 e doc. 02
Fail se: FAIL se doc. 01 e doc. 02 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01 e doc. 02

## B.26 - il deliverable riconduce cessazione distruttiva a doc. 01 art. 10.
`issue: I-13 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01 art. 10; un richiamo immediatamente adiacente collega il punto a doc. 01 art. 10
Fail se: FAIL se doc. 01 art. 10 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01 art. 10

## B.27 - il deliverable richiede preservare titolarita' e allegato chiuso.
`issue: I-01 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «preservare titolarita' e allegato chiuso» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «preservare titolarita' e allegato chiuso» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01 art. 4 e doc. 02

## B.28 - il deliverable richiede allegare hash, versione e materiali minimi.
`issue: I-02 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «allegare hash, versione e materiali minimi» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «allegare hash, versione e materiali minimi» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 02

## B.29 - il deliverable richiede attribuire risultati esclusivi e congiunti per contributo.
`issue: I-03 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «attribuire risultati esclusivi e congiunti per contributo» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «attribuire risultati esclusivi e congiunti per contributo» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01 art. 5 e doc. 03

## B.30 - il deliverable richiede rendere licenza perpetua, trasferibile e sublicenziabile nel campo.
`issue: I-04 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «rendere licenza perpetua, trasferibile e sublicenziabile nel campo» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «rendere licenza perpetua, trasferibile e sublicenziabile nel campo» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01

## B.31 - il deliverable richiede introdurre governance paritetica.
`issue: I-05 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «introdurre governance paritetica» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «introdurre governance paritetica» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 03

## B.32 - il deliverable richiede ottenere atto scritto specifico.
`issue: I-06 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «ottenere atto scritto specifico» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «ottenere atto scritto specifico» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 04

## B.33 - il deliverable richiede introdurre obbligo di conservazione ed evidenza.
`issue: I-07 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «introdurre obbligo di conservazione ed evidenza» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «introdurre obbligo di conservazione ed evidenza» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01 e doc. 04

## B.34 - il deliverable richiede usare comitato e diritto di subentro.
`issue: I-08 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «usare comitato e diritto di subentro» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «usare comitato e diritto di subentro» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01 e doc. 06

## B.35 - il deliverable richiede sospendere divulgazione fino alla revisione brevettuale.
`issue: I-09 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «sospendere divulgazione fino alla revisione brevettuale» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «sospendere divulgazione fino alla revisione brevettuale» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 06

## B.36 - il deliverable non segnala come rischio, criticita' o inadempimento riconoscimento inventori (doc. 04).
`issue: N-01 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - riconoscimento inventori non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - riconoscimento inventori e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 04

## B.37 - il deliverable non segnala come rischio, criticita' o inadempimento componenti Apache-2.0 e MIT (doc. 05).
`issue: N-02 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - componenti Apache-2.0 e MIT non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - componenti Apache-2.0 e MIT e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 05

## B.38 - il deliverable non segnala come rischio, criticita' o inadempimento pubblicazione scientifica (doc. 05).
`issue: N-03 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - pubblicazione scientifica non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - pubblicazione scientifica e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 05

## B.39 - il deliverable non segnala come rischio, criticita' o inadempimento budget Eterea (doc. 03); elemento tracciato: EUR 1.800.000.
`issue: N-04 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - budget Eterea non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - budget Eterea e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 03

## B.40 - il deliverable applica lo stesso test al Background e al Foreground: titolarita', evidenza documentale della provenienza e diritti d'uso di Eterea.
`issue: CHIUSURA - tipo: presenza - gravita: media - judge: si`
Pass se: per ciascuna delle voci indicate nell'oggetto del criterio il deliverable riporta tutti gli elementi richiesti, applicando a ogni voce lo stesso test
Fail se: almeno una delle voci non e' esaminata, oppure per almeno una voce manca uno degli elementi richiesti, oppure le voci sono esaminate con criteri diversi senza che la differenza sia motivata
Indifferente: l'ordine delle voci, la forma (tabella o testo) e la scelta lessicale, purche' ogni elemento sia riconoscibile per ciascuna voce
Fonte: doc. 01 e doc. 02

## B.41 - il deliverable non afferma che il brevetto sui risultati del progetto sara' concesso.
`issue: CHIUSURA - tipo: assenza - gravita: alta - judge: si`
Pass se: presunzione dell'esito non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se presunzione dell'esito e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 06
