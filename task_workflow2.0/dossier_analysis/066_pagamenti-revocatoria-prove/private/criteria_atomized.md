# WF2-066 - Criteri atomizzati

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

## B.1 - il deliverable afferma che il bonifico 30 novembre cade nei sei mesi anteriori alla domanda del 14 dicembre.
`issue: I-01 - tipo: valore - gravita: alta - judge: no`
Pass se: nel deliverable compare «il bonifico 30 novembre cade nei sei mesi anteriori alla domanda del 14 dicembre»
Fail se: FAIL se manca «il bonifico 30 novembre cade nei sei mesi anteriori alla domanda del 14 dicembre», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 01 e doc. 02

## B.2 - il deliverable afferma che il bonifico usa denaro per debiti scaduti.
`issue: I-02 - tipo: presenza - gravita: alta - judge: si`
Pass se: la proposizione compare in una frase autonoma: il bonifico usa denaro per debiti scaduti; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: il bonifico usa denaro per debiti scaduti
Fail se: FAIL se la proposizione «il bonifico usa denaro per debiti scaduti» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 02 e doc. 06

## B.3 - il deliverable afferma che ritardo stipendi e minaccia di sospensione precedono il bonifico.
`issue: I-03 - tipo: presenza - gravita: alta - judge: si`
Pass se: la proposizione compare in una frase autonoma: ritardo stipendi e minaccia di sospensione precedono il bonifico; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: ritardo stipendi e minaccia di sospensione precedono il bonifico
Fail se: FAIL se la proposizione «ritardo stipendi e minaccia di sospensione precedono il bonifico» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 03

## B.4 - il deliverable afferma che il macchinario sostituisce denaro per debito scaduto.
`issue: I-04 - tipo: valore - gravita: alta - judge: no`
Pass se: nel deliverable compare «il macchinario sostituisce denaro per debito scaduto»
Fail se: FAIL se manca «il macchinario sostituisce denaro per debito scaduto», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 02 e doc. 06

## B.5 - il deliverable afferma che manca perizia indipendente sul valore EUR 260.000.
`issue: I-05 - tipo: valore - gravita: alta - judge: no`
Pass se: nel deliverable compare «manca perizia indipendente sul valore EUR 260.000»
Fail se: FAIL se manca «manca perizia indipendente sul valore EUR 260.000», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 02

## B.6 - il deliverable afferma che la garanzia del 10 ottobre assiste debito del 2027.
`issue: I-06 - tipo: valore - gravita: alta - judge: no`
Pass se: nel deliverable compare «la garanzia del 10 ottobre assiste debito del 2027»
Fail se: FAIL se manca «la garanzia del 10 ottobre assiste debito del 2027», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 05

## B.7 - il deliverable afferma che bonifico e cessione non sono individuati dal piano.
`issue: I-07 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: bonifico e cessione non sono individuati dal piano; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: bonifico e cessione non sono individuati dal piano
Fail se: FAIL se la proposizione «bonifico e cessione non sono individuati dal piano» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 04

## B.8 - il deliverable afferma che i pagamenti mensili sono nominati e seguono termini d'uso.
`issue: I-08 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: i pagamenti mensili sono nominati e seguono termini d'uso; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: i pagamenti mensili sono nominati e seguono termini d'uso
Fail se: FAIL se la proposizione «i pagamenti mensili sono nominati e seguono termini d'uso» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 04 e doc. 06

## B.9 - il deliverable afferma che il pagamento e' previsto e la merce arriva per valore equivalente.
`issue: I-09 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: il pagamento e' previsto e la merce arriva per valore equivalente; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: il pagamento e' previsto e la merce arriva per valore equivalente
Fail se: FAIL se la proposizione «il pagamento e' previsto e la merce arriva per valore equivalente» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 04 e doc. 06

## B.10 - il deliverable afferma che 14 dicembre 2028 e 20 febbraio 2029 svolgono funzioni diverse.
`issue: I-10 - tipo: valore - gravita: media - judge: no`
Pass se: nel deliverable compare «14 dicembre 2028 e 20 febbraio 2029 svolgono funzioni diverse»
Fail se: FAIL se manca «14 dicembre 2028 e 20 febbraio 2029 svolgono funzioni diverse», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 01

## B.11 - il deliverable afferma che il massimo teorico e' EUR 440.000 ma dipende da due azioni distinte.
`issue: I-11 - tipo: valore - gravita: media - judge: no`
Pass se: nel deliverable compare «il massimo teorico e' EUR 440.000 ma dipende da due azioni distinte»
Fail se: FAIL se manca «il massimo teorico e' EUR 440.000 ma dipende da due azioni distinte», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 02

## B.12 - il deliverable afferma che mancano causali estese e contabile completa.
`issue: I-12 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: mancano causali estese e contabile completa; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: mancano causali estese e contabile completa
Fail se: FAIL se la proposizione «mancano causali estese e contabile completa» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 02

## B.13 - il deliverable riconduce periodo di sei mesi a doc. 01 e doc. 02.
`issue: I-01 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01 e doc. 02; un richiamo immediatamente adiacente collega il punto a doc. 01 e doc. 02
Fail se: FAIL se doc. 01 e doc. 02 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01 e doc. 02

## B.14 - il deliverable riconduce pagamento normale a doc. 02 e doc. 06.
`issue: I-02 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 02 e doc. 06; un richiamo immediatamente adiacente collega il punto a doc. 02 e doc. 06
Fail se: FAIL se doc. 02 e doc. 06 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 02 e doc. 06

## B.15 - il deliverable riconduce indizi di conoscenza a doc. 03.
`issue: I-03 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 03; un richiamo immediatamente adiacente collega il punto a doc. 03
Fail se: FAIL se doc. 03 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 03

## B.16 - il deliverable riconduce cessione in pagamento a doc. 02 e doc. 06.
`issue: I-04 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 02 e doc. 06; un richiamo immediatamente adiacente collega il punto a doc. 02 e doc. 06
Fail se: FAIL se doc. 02 e doc. 06 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 02 e doc. 06

## B.17 - il deliverable riconduce valore del macchinario a doc. 02.
`issue: I-05 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 02; un richiamo immediatamente adiacente collega il punto a doc. 02
Fail se: FAIL se doc. 02 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 02

## B.18 - il deliverable riconduce pegno per debito preesistente a doc. 05.
`issue: I-06 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 05; un richiamo immediatamente adiacente collega il punto a doc. 05
Fail se: FAIL se doc. 05 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 05

## B.19 - il deliverable riconduce piano attestato non copre Grisolara a doc. 04.
`issue: I-07 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 04; un richiamo immediatamente adiacente collega il punto a doc. 04
Fail se: FAIL se doc. 04 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 04

## B.20 - il deliverable riconduce utenze previste dal piano a doc. 04 e doc. 06.
`issue: I-08 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 04 e doc. 06; un richiamo immediatamente adiacente collega il punto a doc. 04 e doc. 06
Fail se: FAIL se doc. 04 e doc. 06 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 04 e doc. 06

## B.21 - il deliverable riconduce fornitura anticipata con nuova utilita' a doc. 04 e doc. 06.
`issue: I-09 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 04 e doc. 06; un richiamo immediatamente adiacente collega il punto a doc. 04 e doc. 06
Fail se: FAIL se doc. 04 e doc. 06 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 04 e doc. 06

## B.22 - il deliverable riconduce domanda e apertura distinte a doc. 01.
`issue: I-10 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01; un richiamo immediatamente adiacente collega il punto a doc. 01
Fail se: FAIL se doc. 01 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01

## B.23 - il deliverable riconduce quantificazione della pretesa a doc. 02.
`issue: I-11 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 02; un richiamo immediatamente adiacente collega il punto a doc. 02
Fail se: FAIL se doc. 02 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 02

## B.24 - il deliverable riconduce prova bancaria mancante a doc. 02.
`issue: I-12 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 02; un richiamo immediatamente adiacente collega il punto a doc. 02
Fail se: FAIL se doc. 02 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 02

## B.25 - il deliverable richiede valutarlo nel regime con prova della conoscenza a carico del curatore.
`issue: I-01 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «valutarlo nel regime con prova della conoscenza a carico del curatore» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «valutarlo nel regime con prova della conoscenza a carico del curatore» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01 e doc. 02

## B.26 - il deliverable richiede non applicare la categoria dei mezzi anormali.
`issue: I-02 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «non applicare la categoria dei mezzi anormali» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «non applicare la categoria dei mezzi anormali» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 02 e doc. 06

## B.27 - il deliverable richiede usare la mail come indizio e cercare ulteriori riscontri.
`issue: I-03 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «usare la mail come indizio e cercare ulteriori riscontri» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «usare la mail come indizio e cercare ulteriori riscontri» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 03

## B.28 - il deliverable richiede qualificare mezzo anormale e verificare il periodo annuale.
`issue: I-04 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «qualificare mezzo anormale e verificare il periodo annuale» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «qualificare mezzo anormale e verificare il periodo annuale» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 02 e doc. 06

## B.29 - il deliverable richiede acquisire stima alla data dell'atto.
`issue: I-05 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «acquisire stima alla data dell'atto» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «acquisire stima alla data dell'atto» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 02

## B.30 - il deliverable richiede trattare separatamente costituzione e pagamento.
`issue: I-06 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «trattare separatamente costituzione e pagamento» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «trattare separatamente costituzione e pagamento» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 05

## B.31 - il deliverable richiede non estendere automaticamente l'esenzione.
`issue: I-07 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «non estendere automaticamente l'esenzione» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «non estendere automaticamente l'esenzione» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 04

## B.32 - il deliverable richiede classificarli come esenti salvo prova contraria specifica.
`issue: I-08 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «classificarli come esenti salvo prova contraria specifica» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «classificarli come esenti salvo prova contraria specifica» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 04 e doc. 06

## B.33 - il deliverable richiede preservare prova di consegna.
`issue: I-09 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «preservare prova di consegna» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «preservare prova di consegna» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 04 e doc. 06

## B.34 - il deliverable richiede riportare entrambe nella timeline.
`issue: I-10 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «riportare entrambe nella timeline» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «riportare entrambe nella timeline» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01

## B.35 - il deliverable richiede separare EUR 180.000 e EUR 260.000.
`issue: I-11 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «separare EUR 180.000 e EUR 260.000» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «separare EUR 180.000 e EUR 260.000» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 02

## B.36 - il deliverable richiede acquisire flussi bancari e beneficiario effettivo.
`issue: I-12 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «acquisire flussi bancari e beneficiario effettivo» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «acquisire flussi bancari e beneficiario effettivo» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 02

## B.37 - il deliverable indica come conseguenza di periodo di sei mesi che la data di apertura non e' l'unico riferimento.
`issue: I-01 - tipo: presenza - gravita: alta - judge: si`
Pass se: la conseguenza e' espressa nel testo: la data di apertura non e' l'unico riferimento; la conseguenza compare in una cella dedicata della matrice: la data di apertura non e' l'unico riferimento
Fail se: FAIL se manca «la data di apertura non e' l'unico riferimento» o compare una conseguenza incompatibile; PASS solo in uno dei due casi elencati.
Indifferente: collocazione in prosa o tabella.
Fonte: doc. 01 e doc. 02

## B.38 - il deliverable non segnala come rischio, criticita' o inadempimento utenze ordinarie (doc. 04 e doc. 06).
`issue: N-01 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - utenze ordinarie non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - utenze ordinarie e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 04 e doc. 06

## B.39 - il deliverable non segnala come rischio, criticita' o inadempimento fornitura anticipata (doc. 06); elemento tracciato: EUR 75.000.
`issue: N-02 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - fornitura anticipata non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - fornitura anticipata e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 06

## B.40 - il deliverable non segnala come rischio, criticita' o inadempimento ritardo stipendi come indizio (doc. 03).
`issue: N-03 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - ritardo stipendi come indizio non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - ritardo stipendi come indizio e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 03

## B.41 - il deliverable non segnala come rischio, criticita' o inadempimento pegno senza pagamento (doc. 05).
`issue: N-04 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - pegno senza pagamento non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - pegno senza pagamento e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 05

## B.42 - il deliverable applica lo stesso test ai quattro atti esaminati (bonifico, cessione del macchinario, pagamento delle utenze, pagamento della fornitura anticipata): collocazione nel periodo, natura dell'atto e prova disponibile.
`issue: CHIUSURA - tipo: presenza - gravita: media - judge: si`
Pass se: per ciascuna delle voci indicate nell'oggetto del criterio il deliverable riporta tutti gli elementi richiesti, applicando a ogni voce lo stesso test
Fail se: almeno una delle voci non e' esaminata, oppure per almeno una voce manca uno degli elementi richiesti, oppure le voci sono esaminate con criteri diversi senza che la differenza sia motivata
Indifferente: l'ordine delle voci, la forma (tabella o testo) e la scelta lessicale, purche' ogni elemento sia riconoscibile per ciascuna voce
Fonte: doc. 02 e doc. 04

## B.43 - il deliverable non afferma che l'azione revocatoria sara' accolta.
`issue: CHIUSURA - tipo: assenza - gravita: alta - judge: si`
Pass se: presunzione dell'esito non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se presunzione dell'esito e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: 01_task.md
