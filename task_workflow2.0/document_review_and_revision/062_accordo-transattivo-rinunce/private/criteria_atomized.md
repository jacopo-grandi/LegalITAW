# WF2-062 - Criteri atomizzati

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

## B.1 - il deliverable afferma che la formula include fatti ignoti e futuri senza delimitazione.
`issue: I-01 - tipo: presenza - gravita: alta - judge: si`
Pass se: la proposizione compare in una frase autonoma: la formula include fatti ignoti e futuri senza delimitazione; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: la formula include fatti ignoti e futuri senza delimitazione
Fail se: FAIL se la proposizione «la formula include fatti ignoti e futuri senza delimitazione» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 01 art. 3

## B.2 - il deliverable afferma che la rinuncia opera prima del pagamento.
`issue: I-02 - tipo: presenza - gravita: alta - judge: si`
Pass se: la proposizione compare in una frase autonoma: la rinuncia opera prima del pagamento; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: la rinuncia opera prima del pagamento
Fail se: FAIL se la proposizione «la rinuncia opera prima del pagamento» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 01 art. 3 e doc. 03

## B.3 - il deliverable afferma che il debitore trasferisce sulla creditrice il rischio di funding.
`issue: I-03 - tipo: presenza - gravita: alta - judge: si`
Pass se: la proposizione compare in una frase autonoma: il debitore trasferisce sulla creditrice il rischio di funding; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: il debitore trasferisce sulla creditrice il rischio di funding
Fail se: FAIL se la proposizione «il debitore trasferisce sulla creditrice il rischio di funding» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 01 art. 2 e doc. 04

## B.4 - il deliverable afferma che trenta giorni sostituiscono i cinque lavorativi negoziati.
`issue: I-04 - tipo: valore - gravita: alta - judge: no`
Pass se: nel deliverable compare «trenta giorni sostituiscono i cinque lavorativi negoziati»
Fail se: FAIL se manca «trenta giorni sostituiscono i cinque lavorativi negoziati», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 01 e doc. 03

## B.5 - il deliverable afferma che la bozza non contiene la garanzia a prima richiesta.
`issue: I-05 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: la bozza non contiene la garanzia a prima richiesta; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: la bozza non contiene la garanzia a prima richiesta
Fail se: FAIL se la proposizione «la bozza non contiene la garanzia a prima richiesta» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 03

## B.6 - il deliverable afferma che la rinuncia agli atti precede l'incasso.
`issue: I-06 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: la rinuncia agli atti precede l'incasso; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: la rinuncia agli atti precede l'incasso
Fail se: FAIL se la proposizione «la rinuncia agli atti precede l'incasso» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 01 art. 4 e doc. 02

## B.7 - il deliverable afferma che il term sheet prevede EUR 18.000 ma la bozza tace.
`issue: I-07 - tipo: valore - gravita: media - judge: no`
Pass se: nel deliverable compare «il term sheet prevede EUR 18.000 ma la bozza tace»
Fail se: FAIL se manca «il term sheet prevede EUR 18.000 ma la bozza tace», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 03

## B.8 - il deliverable afferma che mancano eccezioni per obblighi e consulenti.
`issue: I-08 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: mancano eccezioni per obblighi e consulenti; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: mancano eccezioni per obblighi e consulenti
Fail se: FAIL se la proposizione «mancano eccezioni per obblighi e consulenti» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 01 art. 5

## B.9 - il deliverable afferma che l'interesse legale lascia ferme rinunce non pagate.
`issue: I-09 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: l'interesse legale lascia ferme rinunce non pagate; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: l'interesse legale lascia ferme rinunce non pagate
Fail se: FAIL se la proposizione «l'interesse legale lascia ferme rinunce non pagate» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 01 art. 6

## B.10 - il deliverable riconduce rinuncia troppo ampia a doc. 01 art. 3.
`issue: I-01 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01 art. 3; un richiamo immediatamente adiacente collega il punto a doc. 01 art. 3
Fail se: FAIL se doc. 01 art. 3 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01 art. 3

## B.11 - il deliverable riconduce efficacia anticipata delle rinunce a doc. 01 art. 3 e doc. 03.
`issue: I-02 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01 art. 3 e doc. 03; un richiamo immediatamente adiacente collega il punto a doc. 01 art. 3 e doc. 03
Fail se: FAIL se doc. 01 art. 3 e doc. 03 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01 art. 3 e doc. 03

## B.12 - il deliverable riconduce condizione legata all'assicuratore a doc. 01 art. 2 e doc. 04.
`issue: I-03 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01 art. 2 e doc. 04; un richiamo immediatamente adiacente collega il punto a doc. 01 art. 2 e doc. 04
Fail se: FAIL se doc. 01 art. 2 e doc. 04 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01 art. 2 e doc. 04

## B.13 - il deliverable riconduce termine di pagamento difforme a doc. 01 e doc. 03.
`issue: I-04 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01 e doc. 03; un richiamo immediatamente adiacente collega il punto a doc. 01 e doc. 03
Fail se: FAIL se doc. 01 e doc. 03 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01 e doc. 03

## B.14 - il deliverable riconduce garanzia mancante a doc. 03.
`issue: I-05 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 03; un richiamo immediatamente adiacente collega il punto a doc. 03
Fail se: FAIL se doc. 03 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 03

## B.15 - il deliverable riconduce chiusura del giudizio prematura a doc. 01 art. 4 e doc. 02.
`issue: I-06 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01 art. 4 e doc. 02; un richiamo immediatamente adiacente collega il punto a doc. 01 art. 4 e doc. 02
Fail se: FAIL se doc. 01 art. 4 e doc. 02 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01 art. 4 e doc. 02

## B.16 - il deliverable riconduce spese legali non regolate a doc. 03.
`issue: I-07 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 03; un richiamo immediatamente adiacente collega il punto a doc. 03
Fail se: FAIL se doc. 03 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 03

## B.17 - il deliverable riconduce riservatezza assoluta a doc. 01 art. 5.
`issue: I-08 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01 art. 5; un richiamo immediatamente adiacente collega il punto a doc. 01 art. 5
Fail se: FAIL se doc. 01 art. 5 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01 art. 5

## B.18 - il deliverable riconduce rimedio insufficiente all'inadempimento a doc. 01 art. 6.
`issue: I-09 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01 art. 6; un richiamo immediatamente adiacente collega il punto a doc. 01 art. 6
Fail se: FAIL se doc. 01 art. 6 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01 art. 6

## B.19 - il deliverable richiede limitare la rinuncia alle domande e ai crediti dell'Allegato A.
`issue: I-01 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «limitare la rinuncia alle domande e ai crediti dell'Allegato A» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «limitare la rinuncia alle domande e ai crediti dell'Allegato A» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01 art. 3

## B.20 - il deliverable richiede subordinarla all'accredito integrale.
`issue: I-02 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «subordinarla all'accredito integrale» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «subordinarla all'accredito integrale» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01 art. 3 e doc. 03

## B.21 - il deliverable richiede rendere il pagamento incondizionato.
`issue: I-03 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «rendere il pagamento incondizionato» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «rendere il pagamento incondizionato» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01 art. 2 e doc. 04

## B.22 - il deliverable richiede ripristinare cinque giorni lavorativi.
`issue: I-04 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «ripristinare cinque giorni lavorativi» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «ripristinare cinque giorni lavorativi» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01 e doc. 03

## B.23 - il deliverable non segnala come rischio, criticita' o inadempimento assenza di ammissione (doc. 01 art. 7).
`issue: N-01 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - assenza di ammissione non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - assenza di ammissione e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 01 art. 7

## B.24 - il deliverable non segnala come rischio, criticita' o inadempimento legge italiana (doc. 01 art. 7).
`issue: N-02 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - legge italiana non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - legge italiana e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 01 art. 7

## B.25 - il deliverable non segnala come rischio, criticita' o inadempimento contributo dell'assicuratore (doc. 04); elemento tracciato: EUR 300.000.
`issue: N-03 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - contributo dell'assicuratore non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - contributo dell'assicuratore e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 04

## B.26 - il deliverable confronta la bozza di accordo (doc. 01) e il term sheet (doc. 03) applicando a entrambi lo stesso test su termine di pagamento, garanzia e spese legali.
`issue: CHIUSURA - tipo: presenza - gravita: media - judge: si`
Pass se: per ciascuna delle voci indicate nell'oggetto del criterio il deliverable riporta tutti gli elementi richiesti, applicando a ogni voce lo stesso test
Fail se: almeno una delle voci non e' esaminata, oppure per almeno una voce manca uno degli elementi richiesti, oppure le voci sono esaminate con criteri diversi senza che la differenza sia motivata
Indifferente: l'ordine delle voci, la forma (tabella o testo) e la scelta lessicale, purche' ogni elemento sia riconoscibile per ciascuna voce
Fonte: doc. 01 e doc. 03

## B.27 - il deliverable non afferma che il giudizio pendente sara' definito in senso favorevole a Frassino.
`issue: CHIUSURA - tipo: assenza - gravita: alta - judge: si`
Pass se: presunzione dell'esito non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se presunzione dell'esito e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 02
