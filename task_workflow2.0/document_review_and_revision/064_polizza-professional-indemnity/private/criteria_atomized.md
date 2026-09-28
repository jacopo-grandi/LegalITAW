# WF2-064 - Criteri atomizzati

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

## B.1 - il deliverable afferma che la data 2026 crea un vuoto rispetto alla continuita' dal 2019.
`issue: I-01 - tipo: valore - gravita: alta - judge: no`
Pass se: nel deliverable compare «la data 2026 crea un vuoto rispetto alla continuita' dal 2019»
Fail se: FAIL se manca «la data 2026 crea un vuoto rispetto alla continuita' dal 2019», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 01 e doc. 02

## B.2 - il deliverable afferma che la notifica non aggancia le richieste future.
`issue: I-02 - tipo: presenza - gravita: alta - judge: si`
Pass se: la proposizione compare in una frase autonoma: la notifica non aggancia le richieste future; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: la notifica non aggancia le richieste future
Fail se: FAIL se la proposizione «la notifica non aggancia le richieste future» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 01 art. 3

## B.3 - il deliverable afferma che il reclamo scritto e' almeno circostanza specifica.
`issue: I-03 - tipo: presenza - gravita: alta - judge: si`
Pass se: la proposizione compare in una frase autonoma: il reclamo scritto e' almeno circostanza specifica; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: il reclamo scritto e' almeno circostanza specifica
Fail se: FAIL se la proposizione «il reclamo scritto e' almeno circostanza specifica» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 03

## B.4 - il deliverable afferma che manca una pretesa o minaccia identificata.
`issue: I-04 - tipo: presenza - gravita: alta - judge: si`
Pass se: la proposizione compare in una frase autonoma: manca una pretesa o minaccia identificata; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: manca una pretesa o minaccia identificata
Fail se: FAIL se la proposizione «manca una pretesa o minaccia identificata» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 03

## B.5 - il deliverable afferma che la formula espelle anche errori professionali con componente informatica.
`issue: I-05 - tipo: presenza - gravita: alta - judge: si`
Pass se: la proposizione compare in una frase autonoma: la formula espelle anche errori professionali con componente informatica; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: la formula espelle anche errori professionali con componente informatica
Fail se: FAIL se la proposizione «la formula espelle anche errori professionali con componente informatica» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 01

## B.6 - il deliverable afferma che manca la responsabilita' che esisterebbe anche senza contratto.
`issue: I-06 - tipo: presenza - gravita: alta - judge: si`
Pass se: la proposizione compare in una frase autonoma: manca la responsabilita' che esisterebbe anche senza contratto; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: manca la responsabilita' che esisterebbe anche senza contratto
Fail se: FAIL se la proposizione «manca la responsabilita' che esisterebbe anche senza contratto» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 01

## B.7 - il deliverable afferma che l'esclusione comprende chi opera sotto direzione.
`issue: I-07 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: l'esclusione comprende chi opera sotto direzione; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: l'esclusione comprende chi opera sotto direzione
Fail se: FAIL se la proposizione «l'esclusione comprende chi opera sotto direzione» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 01 e doc. 05

## B.8 - il deliverable afferma che una mera contestazione espelle la copertura.
`issue: I-08 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: una mera contestazione espelle la copertura; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: una mera contestazione espelle la copertura
Fail se: FAIL se la proposizione «una mera contestazione espelle la copertura» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 01

## B.9 - il deliverable afferma che l'assicurato non partecipa a scelta e strategia.
`issue: I-09 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: l'assicurato non partecipa a scelta e strategia; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: l'assicurato non partecipa a scelta e strategia
Fail se: FAIL se la proposizione «l'assicurato non partecipa a scelta e strategia» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 01 art. 7

## B.10 - il deliverable afferma che l'assicuratore puo' imporre ammissioni.
`issue: I-10 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: l'assicuratore puo' imporre ammissioni; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: l'assicuratore puo' imporre ammissioni
Fail se: FAIL se la proposizione «l'assicuratore puo' imporre ammissioni» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 01 art. 7

## B.11 - il deliverable afferma che la bozza riduce il capitale disponibile.
`issue: I-11 - tipo: valore - gravita: media - judge: no`
Pass se: nel deliverable compare «la bozza riduce il capitale disponibile»
Fail se: FAIL se manca «la bozza riduce il capitale disponibile», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 01, doc. 02 e doc. 04

## B.12 - il deliverable afferma che le due richieste 2027 consumano un unico aggregato ma il fascicolo non prova il criterio di collegamento.
`issue: I-12 - tipo: valore - gravita: media - judge: no`
Pass se: nel deliverable compare «le due richieste 2027 consumano un unico aggregato ma il fascicolo non prova il criterio di collegamento»
Fail se: FAIL se manca «le due richieste 2027 consumano un unico aggregato ma il fascicolo non prova il criterio di collegamento», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 06

## B.13 - il deliverable afferma che la cessazione lascia senza finestra di denuncia.
`issue: I-13 - tipo: valore - gravita: media - judge: no`
Pass se: nel deliverable compare «la cessazione lascia senza finestra di denuncia»
Fail se: FAIL se manca «la cessazione lascia senza finestra di denuncia», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 01

## B.14 - il deliverable riconduce retroattivita' accorciata a doc. 01 e doc. 02.
`issue: I-01 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01 e doc. 02; un richiamo immediatamente adiacente collega il punto a doc. 01 e doc. 02
Fail se: FAIL se doc. 01 e doc. 02 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01 e doc. 02

## B.15 - il deliverable riconduce circostanze senza deeming a doc. 01 art. 3.
`issue: I-02 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01 art. 3; un richiamo immediatamente adiacente collega il punto a doc. 01 art. 3
Fail se: FAIL se doc. 01 art. 3 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01 art. 3

## B.16 - il deliverable riconduce reclamo Celsa da notificare a doc. 03.
`issue: I-03 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 03; un richiamo immediatamente adiacente collega il punto a doc. 03
Fail se: FAIL se doc. 03 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 03

## B.17 - il deliverable riconduce ritardo Ansedonia da qualificare a doc. 03.
`issue: I-04 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 03; un richiamo immediatamente adiacente collega il punto a doc. 03
Fail se: FAIL se doc. 03 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 03

## B.18 - il deliverable riconduce esclusione cyber eccessiva a doc. 01.
`issue: I-05 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01; un richiamo immediatamente adiacente collega il punto a doc. 01
Fail se: FAIL se doc. 01 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01

## B.19 - il deliverable riconduce esclusione contrattuale senza carve-back a doc. 01.
`issue: I-06 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01; un richiamo immediatamente adiacente collega il punto a doc. 01
Fail se: FAIL se doc. 01 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01

## B.20 - il deliverable riconduce consulenti esterni esclusi a doc. 01 e doc. 05.
`issue: I-07 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01 e doc. 05; un richiamo immediatamente adiacente collega il punto a doc. 01 e doc. 05
Fail se: FAIL se doc. 01 e doc. 05 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01 e doc. 05

## B.21 - il deliverable riconduce disonesta' non accertata a doc. 01.
`issue: I-08 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01; un richiamo immediatamente adiacente collega il punto a doc. 01
Fail se: FAIL se doc. 01 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01

## B.22 - il deliverable riconduce controllo della difesa a doc. 01 art. 7.
`issue: I-09 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01 art. 7; un richiamo immediatamente adiacente collega il punto a doc. 01 art. 7
Fail se: FAIL se doc. 01 art. 7 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01 art. 7

## B.23 - il deliverable riconduce transazione senza consenso a doc. 01 art. 7.
`issue: I-10 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01 art. 7; un richiamo immediatamente adiacente collega il punto a doc. 01 art. 7
Fail se: FAIL se doc. 01 art. 7 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01 art. 7

## B.24 - il deliverable riconduce costi entro massimale a doc. 01, doc. 02 e doc. 04.
`issue: I-11 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01, doc. 02 e doc. 04; un richiamo immediatamente adiacente collega il punto a doc. 01, doc. 02 e doc. 04
Fail se: FAIL se doc. 01, doc. 02 e doc. 04 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01, doc. 02 e doc. 04

## B.25 - il deliverable riconduce aggregazione richieste a doc. 06.
`issue: I-12 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 06; un richiamo immediatamente adiacente collega il punto a doc. 06
Fail se: FAIL se doc. 06 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 06

## B.26 - il deliverable riconduce periodo di osservazione assente a doc. 01.
`issue: I-13 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01; un richiamo immediatamente adiacente collega il punto a doc. 01
Fail se: FAIL se doc. 01 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01

## B.27 - il deliverable richiede ripristinare 1 ottobre 2019 o retroattivita' illimitata.
`issue: I-01 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «ripristinare 1 ottobre 2019 o retroattivita' illimitata» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «ripristinare 1 ottobre 2019 o retroattivita' illimitata» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01 e doc. 02

## B.28 - il deliverable richiede introdurre clausola di collegamento alla data della circostanza.
`issue: I-02 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «introdurre clausola di collegamento alla data della circostanza» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «introdurre clausola di collegamento alla data della circostanza» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01 art. 3

## B.29 - il deliverable richiede notificarlo prima della scadenza.
`issue: I-03 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «notificarlo prima della scadenza» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «notificarlo prima della scadenza» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 03

## B.30 - il deliverable richiede acquisire corrispondenza prima di dichiararlo sinistro.
`issue: I-04 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «acquisire corrispondenza prima di dichiararlo sinistro» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «acquisire corrispondenza prima di dichiararlo sinistro» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 03

## B.31 - il deliverable richiede limitare l'esclusione al rischio cyber autonomo.
`issue: I-05 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «limitare l'esclusione al rischio cyber autonomo» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «limitare l'esclusione al rischio cyber autonomo» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01

## B.32 - il deliverable richiede aggiungere carve-back.
`issue: I-06 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «aggiungere carve-back» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «aggiungere carve-back» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01

## B.33 - il deliverable richiede coprire collaboratori nominati e sotto controllo.
`issue: I-07 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «coprire collaboratori nominati e sotto controllo» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «coprire collaboratori nominati e sotto controllo» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01 e doc. 05

## B.34 - il deliverable richiede richiedere accertamento definitivo e separabilita'.
`issue: I-08 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «richiedere accertamento definitivo e separabilita'» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «richiedere accertamento definitivo e separabilita'» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01

## B.35 - il deliverable richiede prevedere consultazione e scelta concordata.
`issue: I-09 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «prevedere consultazione e scelta concordata» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «prevedere consultazione e scelta concordata» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01 art. 7

## B.36 - il deliverable non segnala come rischio, criticita' o inadempimento assenza di domanda giudiziale (doc. 03).
`issue: N-01 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - assenza di domanda giudiziale non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - assenza di domanda giudiziale e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 03

## B.37 - il deliverable non segnala come rischio, criticita' o inadempimento continuita' dei premi (doc. 02); elemento tracciato: 1 ottobre 2019.
`issue: N-02 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - continuita' dei premi non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - continuita' dei premi e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 02

## B.38 - il deliverable non segnala come rischio, criticita' o inadempimento due sinistri collegati (doc. 06); elemento tracciato: EUR 2.360.000.
`issue: N-03 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - due sinistri collegati non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - due sinistri collegati e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 06

## B.39 - il deliverable non segnala come rischio, criticita' o inadempimento attivita' del collaboratore BIM (doc. 05).
`issue: N-04 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - attivita' del collaboratore BIM non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - attivita' del collaboratore BIM e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 05

## B.40 - il deliverable applica lo stesso test alle due circostanze note (reclamo Celsa e ritardo Ansedonia): qualificazione, obbligo di notifica e conseguenza sulla copertura.
`issue: CHIUSURA - tipo: presenza - gravita: media - judge: si`
Pass se: per ciascuna delle voci indicate nell'oggetto del criterio il deliverable riporta tutti gli elementi richiesti, applicando a ogni voce lo stesso test
Fail se: almeno una delle voci non e' esaminata, oppure per almeno una voce manca uno degli elementi richiesti, oppure le voci sono esaminate con criteri diversi senza che la differenza sia motivata
Indifferente: l'ordine delle voci, la forma (tabella o testo) e la scelta lessicale, purche' ogni elemento sia riconoscibile per ciascuna voce
Fonte: doc. 03 e doc. 04

## B.41 - il deliverable non afferma che l'assicuratore accettera' la denuncia delle due circostanze note.
`issue: CHIUSURA - tipo: assenza - gravita: alta - judge: si`
Pass se: presunzione dell'esito non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se presunzione dell'esito e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 04
