# WF2-065 - Criteri atomizzati

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

## B.1 - il deliverable afferma che il preavviso invoca revoca d'interesse pubblico ma descrive decadenza per condizioni.
`issue: I-01 - tipo: presenza - gravita: alta - judge: si`
Pass se: la proposizione compare in una frase autonoma: il preavviso invoca revoca d'interesse pubblico ma descrive decadenza per condizioni; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: il preavviso invoca revoca d'interesse pubblico ma descrive decadenza per condizioni
Fail se: FAIL se la proposizione «il preavviso invoca revoca d'interesse pubblico ma descrive decadenza per condizioni» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 05

## B.2 - il deliverable afferma che l'autorizzazione sposta due assunzioni al 30 settembre.
`issue: I-02 - tipo: presenza - gravita: alta - judge: si`
Pass se: la proposizione compare in una frase autonoma: l'autorizzazione sposta due assunzioni al 30 settembre; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: l'autorizzazione sposta due assunzioni al 30 settembre
Fail se: FAIL se la proposizione «l'autorizzazione sposta due assunzioni al 30 settembre» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 01, doc. 03 e doc. 06

## B.3 - il deliverable afferma che EUR 220.000 non provengono da risorse libere.
`issue: I-03 - tipo: valore - gravita: alta - judge: no`
Pass se: nel deliverable compare «EUR 220.000 non provengono da risorse libere»
Fail se: FAIL se manca «EUR 220.000 non provengono da risorse libere», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 02 e doc. 03

## B.4 - il deliverable afferma che il finanziamento agevolato non prova da solo doppio finanziamento dei medesimi costi.
`issue: I-04 - tipo: presenza - gravita: alta - judge: si`
Pass se: la proposizione compare in una frase autonoma: il finanziamento agevolato non prova da solo doppio finanziamento dei medesimi costi; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: il finanziamento agevolato non prova da solo doppio finanziamento dei medesimi costi
Fail se: FAIL se la proposizione «il finanziamento agevolato non prova da solo doppio finanziamento dei medesimi costi» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 02 e doc. 03

## B.5 - il deliverable afferma che EUR 2.630.000 di costi non sono contestati.
`issue: I-05 - tipo: valore - gravita: alta - judge: no`
Pass se: nel deliverable compare «EUR 2.630.000 di costi non sono contestati»
Fail se: FAIL se manca «EUR 2.630.000 di costi non sono contestati», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 03 e doc. 04

## B.6 - il deliverable afferma che il 40% di EUR 2.630.000 e' EUR 1.052.000.
`issue: I-06 - tipo: valore - gravita: alta - judge: no`
Pass se: nel deliverable compare «il 40% di EUR 2.630.000 e' EUR 1.052.000»
Fail se: FAIL se manca «il 40% di EUR 2.630.000 e' EUR 1.052.000», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 01 e doc. 04

## B.7 - il deliverable afferma che il termine assegnato scade il 22 gennaio 2029.
`issue: I-07 - tipo: valore - gravita: media - judge: no`
Pass se: nel deliverable compare «il termine assegnato scade il 22 gennaio 2029»
Fail se: FAIL se manca «il termine assegnato scade il 22 gennaio 2029», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 05

## B.8 - il deliverable afferma che la beneficiaria ha pianificato assunzioni sullo slittamento scritto.
`issue: I-08 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: la beneficiaria ha pianificato assunzioni sullo slittamento scritto; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: la beneficiaria ha pianificato assunzioni sullo slittamento scritto
Fail se: FAIL se la proposizione «la beneficiaria ha pianificato assunzioni sullo slittamento scritto» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 06

## B.9 - il deliverable afferma che il preavviso e' firmato dal responsabile controllo e non indica delega al recupero.
`issue: I-09 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: il preavviso e' firmato dal responsabile controllo e non indica delega al recupero; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: il preavviso e' firmato dal responsabile controllo e non indica delega al recupero
Fail se: FAIL se la proposizione «il preavviso e' firmato dal responsabile controllo e non indica delega al recupero» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 05

## B.10 - il deliverable afferma che mancano tasso, decorrenza e base.
`issue: I-10 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: mancano tasso, decorrenza e base; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: mancano tasso, decorrenza e base
Fail se: FAIL se la proposizione «mancano tasso, decorrenza e base» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 05

## B.11 - il deliverable afferma che la dichiarazione era vera secondo la classificazione interna ma non e' supportata da parere.
`issue: I-11 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: la dichiarazione era vera secondo la classificazione interna ma non e' supportata da parere; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: la dichiarazione era vera secondo la classificazione interna ma non e' supportata da parere
Fail se: FAIL se la proposizione «la dichiarazione era vera secondo la classificazione interna ma non e' supportata da parere» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 02

## B.12 - il deliverable afferma che oggi esiste soltanto preavviso.
`issue: I-12 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: oggi esiste soltanto preavviso; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: oggi esiste soltanto preavviso
Fail se: FAIL se la proposizione «oggi esiste soltanto preavviso» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 05

## B.13 - il deliverable riconduce qualificazione incoerente del potere a doc. 05.
`issue: I-01 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 05; un richiamo immediatamente adiacente collega il punto a doc. 05
Fail se: FAIL se doc. 05 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 05

## B.14 - il deliverable riconduce milestone modificata a doc. 01, doc. 03 e doc. 06.
`issue: I-02 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01, doc. 03 e doc. 06; un richiamo immediatamente adiacente collega il punto a doc. 01, doc. 03 e doc. 06
Fail se: FAIL se doc. 01, doc. 03 e doc. 06 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01, doc. 03 e doc. 06

## B.15 - il deliverable riconduce apporto proprio parzialmente agevolato a doc. 02 e doc. 03.
`issue: I-03 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 02 e doc. 03; un richiamo immediatamente adiacente collega il punto a doc. 02 e doc. 03
Fail se: FAIL se doc. 02 e doc. 03 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 02 e doc. 03

## B.16 - il deliverable riconduce cumulo non dimostrato a doc. 02 e doc. 03.
`issue: I-04 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 02 e doc. 03; un richiamo immediatamente adiacente collega il punto a doc. 02 e doc. 03
Fail se: FAIL se doc. 02 e doc. 03 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 02 e doc. 03

## B.17 - il deliverable riconduce recupero integrale non proporzionato a doc. 03 e doc. 04.
`issue: I-05 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 03 e doc. 04; un richiamo immediatamente adiacente collega il punto a doc. 03 e doc. 04
Fail se: FAIL se doc. 03 e doc. 04 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 03 e doc. 04

## B.18 - il deliverable riconduce tetto del 40% a doc. 01 e doc. 04.
`issue: I-06 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01 e doc. 04; un richiamo immediatamente adiacente collega il punto a doc. 01 e doc. 04
Fail se: FAIL se doc. 01 e doc. 04 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01 e doc. 04

## B.19 - il deliverable riconduce partecipazione procedimentale a doc. 05.
`issue: I-07 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 05; un richiamo immediatamente adiacente collega il punto a doc. 05
Fail se: FAIL se doc. 05 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 05

## B.20 - il deliverable riconduce affidamento sull'autorizzazione a doc. 06.
`issue: I-08 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 06; un richiamo immediatamente adiacente collega il punto a doc. 06
Fail se: FAIL se doc. 06 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 06

## B.21 - il deliverable riconduce competenza del firmatario a doc. 05.
`issue: I-09 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 05; un richiamo immediatamente adiacente collega il punto a doc. 05
Fail se: FAIL se doc. 05 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 05

## B.22 - il deliverable riconduce interessi non calcolabili a doc. 05.
`issue: I-10 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 05; un richiamo immediatamente adiacente collega il punto a doc. 05
Fail se: FAIL se doc. 05 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 05

## B.23 - il deliverable riconduce dichiarazione da contestualizzare a doc. 02.
`issue: I-11 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 02; un richiamo immediatamente adiacente collega il punto a doc. 02
Fail se: FAIL se doc. 02 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 02

## B.24 - il deliverable riconduce tutela dopo il provvedimento a doc. 05.
`issue: I-12 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 05; un richiamo immediatamente adiacente collega il punto a doc. 05
Fail se: FAIL se doc. 05 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 05

## B.25 - il deliverable richiede chiedere individuazione della base e dei presupposti.
`issue: I-01 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «chiedere individuazione della base e dei presupposti» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «chiedere individuazione della base e dei presupposti» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 05

## B.26 - il deliverable richiede opporre il provvedimento autorizzativo al dato del 30 giugno.
`issue: I-02 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «opporre il provvedimento autorizzativo al dato del 30 giugno» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «opporre il provvedimento autorizzativo al dato del 30 giugno» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01, doc. 03 e doc. 06

## B.27 - il deliverable richiede verificare se il bando esclude ogni finanza agevolata e rettificare la dichiarazione.
`issue: I-03 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «verificare se il bando esclude ogni finanza agevolata e rettificare la dichiarazione» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «verificare se il bando esclude ogni finanza agevolata e rettificare la dichiarazione» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 02 e doc. 03

## B.28 - il deliverable richiede acquisire contratto e tracciatura per costo.
`issue: I-04 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «acquisire contratto e tracciatura per costo» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «acquisire contratto e tracciatura per costo» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 02 e doc. 03

## B.29 - il deliverable richiede costruire scenario di riduzione proporzionale e motivazione.
`issue: I-05 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «costruire scenario di riduzione proporzionale e motivazione» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «costruire scenario di riduzione proporzionale e motivazione» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 03 e doc. 04

## B.30 - il deliverable richiede confrontare il contributo erogato di EUR 1.050.000.
`issue: I-06 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «confrontare il contributo erogato di EUR 1.050.000» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «confrontare il contributo erogato di EUR 1.050.000» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01 e doc. 04

## B.31 - il deliverable richiede depositare osservazioni e richiesta di accesso entro la data.
`issue: I-07 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «depositare osservazioni e richiesta di accesso entro la data» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «depositare osservazioni e richiesta di accesso entro la data» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 05

## B.32 - il deliverable richiede documentare costi e decisioni conseguenti.
`issue: I-08 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «documentare costi e decisioni conseguenti» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «documentare costi e decisioni conseguenti» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 06

## B.33 - il deliverable richiede acquisire atto organizzativo.
`issue: I-09 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «acquisire atto organizzativo» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «acquisire atto organizzativo» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 05

## B.34 - il deliverable richiede chiedere prospetto di calcolo.
`issue: I-10 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «chiedere prospetto di calcolo» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «chiedere prospetto di calcolo» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 05

## B.35 - il deliverable richiede ricostruire istruttoria e conoscenza.
`issue: I-11 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «ricostruire istruttoria e conoscenza» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «ricostruire istruttoria e conoscenza» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 02

## B.36 - il deliverable richiede preservare motivi e prova senza descrivere come gia' adottato il recupero.
`issue: I-12 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «preservare motivi e prova senza descrivere come gia' adottato il recupero» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «preservare motivi e prova senza descrivere come gia' adottato il recupero» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 05

## B.37 - il deliverable indica come conseguenza di qualificazione incoerente del potere che difesa e conseguenze economiche dipendono dalla qualificazione.
`issue: I-01 - tipo: presenza - gravita: alta - judge: si`
Pass se: la conseguenza e' espressa nel testo: difesa e conseguenze economiche dipendono dalla qualificazione; la conseguenza compare in una cella dedicata della matrice: difesa e conseguenze economiche dipendono dalla qualificazione
Fail se: FAIL se manca «difesa e conseguenze economiche dipendono dalla qualificazione» o compare una conseguenza incompatibile; PASS solo in uno dei due casi elencati.
Indifferente: collocazione in prosa o tabella.
Fonte: doc. 05

## B.38 - il deliverable non segnala come rischio, criticita' o inadempimento cambio di amministratore (visura richiamata nel doc. 03).
`issue: N-01 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - cambio di amministratore non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - cambio di amministratore e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: visura richiamata nel doc. 03

## B.39 - il deliverable non segnala come rischio, criticita' o inadempimento rinomina del progetto (doc. 04).
`issue: N-02 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - rinomina del progetto non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - rinomina del progetto e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 04

## B.40 - il deliverable non segnala come rischio, criticita' o inadempimento scarto di EUR 2.000 (doc. 04).
`issue: N-03 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - scarto di EUR 2.000 non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - scarto di EUR 2.000 e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 04

## B.41 - il deliverable non segnala come rischio, criticita' o inadempimento due assunzioni differite (doc. 06).
`issue: N-04 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - due assunzioni differite non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - due assunzioni differite e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 06

## B.42 - il deliverable applica lo stesso test ai due addebiti del preavviso (milestone occupazionale e fonte dell'apporto proprio): base documentale, qualificazione e conseguenza economica.
`issue: CHIUSURA - tipo: presenza - gravita: media - judge: si`
Pass se: per ciascuna delle voci indicate nell'oggetto del criterio il deliverable riporta tutti gli elementi richiesti, applicando a ogni voce lo stesso test
Fail se: almeno una delle voci non e' esaminata, oppure per almeno una voce manca uno degli elementi richiesti, oppure le voci sono esaminate con criteri diversi senza che la differenza sia motivata
Indifferente: l'ordine delle voci, la forma (tabella o testo) e la scelta lessicale, purche' ogni elemento sia riconoscibile per ciascuna voce
Fonte: doc. 03 e doc. 05

## B.43 - il deliverable non afferma che il procedimento si concludera' senza recupero del contributo.
`issue: CHIUSURA - tipo: assenza - gravita: alta - judge: si`
Pass se: presunzione dell'esito non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se presunzione dell'esito e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 05
