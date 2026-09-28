# WF2-067 - Criteri atomizzati

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

## B.1 - il deliverable afferma che dal 6 novembre decorrono dieci giorni lavorativi escludendo il dies a quo.
`issue: I-01 - tipo: valore - gravita: alta - judge: no`
Pass se: nel deliverable compare «dal 6 novembre decorrono dieci giorni lavorativi escludendo il dies a quo»
Fail se: FAIL se manca «dal 6 novembre decorrono dieci giorni lavorativi escludendo il dies a quo», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 01

## B.2 - il deliverable afferma che la diffida non contiene dichiarazione di accelerazione.
`issue: I-02 - tipo: presenza - gravita: alta - judge: si`
Pass se: la proposizione compare in una frase autonoma: la diffida non contiene dichiarazione di accelerazione; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: la diffida non contiene dichiarazione di accelerazione
Fail se: FAIL se la proposizione «la diffida non contiene dichiarazione di accelerazione» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 01

## B.3 - il deliverable afferma che la richiesta e' valida solo dopo accelerazione.
`issue: I-03 - tipo: valore - gravita: alta - judge: no`
Pass se: nel deliverable compare «la richiesta e' valida solo dopo accelerazione»
Fail se: FAIL se manca «la richiesta e' valida solo dopo accelerazione», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 02

## B.4 - il deliverable afferma che servono accelerazione, preavviso e valutazione.
`issue: I-04 - tipo: valore - gravita: alta - judge: no`
Pass se: nel deliverable compare «servono accelerazione, preavviso e valutazione»
Fail se: FAIL se manca «servono accelerazione, preavviso e valutazione», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 03

## B.5 - il deliverable afferma che l'Evento di Escussione coincide con accelerazione valida.
`issue: I-05 - tipo: presenza - gravita: alta - judge: si`
Pass se: la proposizione compare in una frase autonoma: l'Evento di Escussione coincide con accelerazione valida; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: l'Evento di Escussione coincide con accelerazione valida
Fail se: FAIL se la proposizione «l'Evento di Escussione coincide con accelerazione valida» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 04

## B.6 - il deliverable afferma che il titolo esecutivo non elimina precetto e termine.
`issue: I-06 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: il titolo esecutivo non elimina precetto e termine; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: il titolo esecutivo non elimina precetto e termine
Fail se: FAIL se la proposizione «il titolo esecutivo non elimina precetto e termine» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 05

## B.7 - il deliverable afferma che i proventi seguono ordine contrattuale.
`issue: I-07 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: i proventi seguono ordine contrattuale; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: i proventi seguono ordine contrattuale
Fail se: FAIL se la proposizione «i proventi seguono ordine contrattuale» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 06

## B.8 - il deliverable afferma che manca la perizia sulle quote.
`issue: I-08 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: manca la perizia sulle quote; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: manca la perizia sulle quote
Fail se: FAIL se la proposizione «manca la perizia sulle quote» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 03

## B.9 - il deliverable afferma che 11, 12, 18 e 19 novembre non contano.
`issue: I-09 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: 11, 12, 18 e 19 novembre non contano; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: 11, 12, 18 e 19 novembre non contano
Fail se: FAIL se la proposizione «11, 12, 18 e 19 novembre non contano» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: calendario

## B.10 - il deliverable afferma che debito EUR 4.480.000 e conto EUR 620.000.
`issue: I-10 - tipo: valore - gravita: media - judge: no`
Pass se: nel deliverable compare «debito EUR 4.480.000 e conto EUR 620.000»
Fail se: FAIL se manca «debito EUR 4.480.000 e conto EUR 620.000», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 01 e doc. 04

## B.11 - il deliverable riconduce cure period a doc. 01.
`issue: I-01 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01; un richiamo immediatamente adiacente collega il punto a doc. 01
Fail se: FAIL se doc. 01 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01

## B.12 - il deliverable riconduce accelerazione separata a doc. 01.
`issue: I-02 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01; un richiamo immediatamente adiacente collega il punto a doc. 01
Fail se: FAIL se doc. 01 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01

## B.13 - il deliverable riconduce fideiussione subordinata a doc. 02.
`issue: I-03 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 02; un richiamo immediatamente adiacente collega il punto a doc. 02
Fail se: FAIL se doc. 02 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 02

## B.14 - il deliverable riconduce pegno quote a doc. 03.
`issue: I-04 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 03; un richiamo immediatamente adiacente collega il punto a doc. 03
Fail se: FAIL se doc. 03 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 03

## B.15 - il deliverable riconduce conto come garanzia finanziaria a doc. 04.
`issue: I-05 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 04; un richiamo immediatamente adiacente collega il punto a doc. 04
Fail se: FAIL se doc. 04 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 04

## B.16 - il deliverable riconduce ipoteca a doc. 05.
`issue: I-06 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 05; un richiamo immediatamente adiacente collega il punto a doc. 05
Fail se: FAIL se doc. 05 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 05

## B.17 - il deliverable riconduce waterfall a doc. 06.
`issue: I-07 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 06; un richiamo immediatamente adiacente collega il punto a doc. 06
Fail se: FAIL se doc. 06 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 06

## B.18 - il deliverable riconduce valutazione indipendente a doc. 03.
`issue: I-08 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 03; un richiamo immediatamente adiacente collega il punto a doc. 03
Fail se: FAIL se doc. 03 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 03

## B.19 - il deliverable riconduce giorni non lavorativi a calendario.
`issue: I-09 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a calendario; un richiamo immediatamente adiacente collega il punto a calendario
Fail se: FAIL se calendario non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: calendario

## B.20 - il deliverable riconduce saldo iniziale a doc. 01 e doc. 04.
`issue: I-10 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01 e doc. 04; un richiamo immediatamente adiacente collega il punto a doc. 01 e doc. 04
Fail se: FAIL se doc. 01 e doc. 04 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01 e doc. 04

## B.21 - il deliverable richiede fissare scadenza al 20 novembre 2028.
`issue: I-01 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «fissare scadenza al 20 novembre 2028» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «fissare scadenza al 20 novembre 2028» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01

## B.22 - il deliverable richiede inviare atto successivo dopo il 20 novembre.
`issue: I-02 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «inviare atto successivo dopo il 20 novembre» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «inviare atto successivo dopo il 20 novembre» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01

## B.23 - il deliverable richiede calendarizzare domanda e tre giorni lavorativi.
`issue: I-03 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «calendarizzare domanda e tre giorni lavorativi» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «calendarizzare domanda e tre giorni lavorativi» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 02

## B.24 - il deliverable non segnala come rischio, criticita' o inadempimento covenant sanato a settembre (doc. 01).
`issue: N-01 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - covenant sanato a settembre non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - covenant sanato a settembre e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 01

## B.25 - il deliverable non segnala come rischio, criticita' o inadempimento bozza di richiesta al garante (fascicolo email).
`issue: N-02 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - bozza di richiesta al garante non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - bozza di richiesta al garante e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: fascicolo email

## B.26 - il deliverable non segnala come rischio, criticita' o inadempimento ipoteca di primo grado (doc. 05).
`issue: N-03 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - ipoteca di primo grado non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - ipoteca di primo grado e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 05

## B.27 - il deliverable non segnala come rischio, criticita' o inadempimento conto capiente solo in parte (doc. 04); elemento tracciato: EUR 620.000.
`issue: N-04 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - conto capiente solo in parte non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - conto capiente solo in parte e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 04

## B.28 - il deliverable indica per ciascuna delle quattro garanzie (fideiussione, pegno di quote, garanzia finanziaria sul conto, ipoteca) il presupposto di escussione, il preavviso richiesto e gli atti preliminari necessari.
`issue: CHIUSURA - tipo: presenza - gravita: media - judge: si`
Pass se: per ciascuna delle voci indicate nell'oggetto del criterio il deliverable riporta tutti gli elementi richiesti, applicando a ogni voce lo stesso test
Fail se: almeno una delle voci non e' esaminata, oppure per almeno una voce manca uno degli elementi richiesti, oppure le voci sono esaminate con criteri diversi senza che la differenza sia motivata
Indifferente: l'ordine delle voci, la forma (tabella o testo) e la scelta lessicale, purche' ogni elemento sia riconoscibile per ciascuna voce
Fonte: doc. 02, doc. 03, doc. 04 e doc. 05

## B.29 - il deliverable non afferma che l'escussione delle garanzie coprira' integralmente il credito.
`issue: CHIUSURA - tipo: assenza - gravita: alta - judge: si`
Pass se: presunzione dell'esito non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se presunzione dell'esito e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 06
