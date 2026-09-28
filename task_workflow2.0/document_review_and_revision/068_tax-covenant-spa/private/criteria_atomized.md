# WF2-068 - Criteri atomizzati

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

## B.1 - il deliverable afferma che la bozza copre anche periodi post-closing.
`issue: I-01 - tipo: presenza - gravita: alta - judge: si`
Pass se: la proposizione compare in una frase autonoma: la bozza copre anche periodi post-closing; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: la bozza copre anche periodi post-closing
Fail se: FAIL se la proposizione «la bozza copre anche periodi post-closing» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 01 clausola 1

## B.2 - il deliverable afferma che manca criterio per il periodo gennaio-marzo 2030.
`issue: I-02 - tipo: presenza - gravita: alta - judge: si`
Pass se: la proposizione compare in una frase autonoma: manca criterio per il periodo gennaio-marzo 2030; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: manca criterio per il periodo gennaio-marzo 2030
Fail se: FAIL se la proposizione «manca criterio per il periodo gennaio-marzo 2030» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 02 e doc. 06

## B.3 - il deliverable afferma che l'atto e' deciso prima del closing.
`issue: I-03 - tipo: presenza - gravita: alta - judge: si`
Pass se: la proposizione compare in una frase autonoma: l'atto e' deciso prima del closing; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: l'atto e' deciso prima del closing
Fail se: FAIL se la proposizione «l'atto e' deciso prima del closing» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 06

## B.4 - il deliverable afferma che i venditori pagano senza partecipare.
`issue: I-04 - tipo: presenza - gravita: alta - judge: si`
Pass se: la proposizione compare in una frase autonoma: i venditori pagano senza partecipare; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: i venditori pagano senza partecipare
Fail se: FAIL se la proposizione «i venditori pagano senza partecipare» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 01 clausola 2

## B.5 - il deliverable afferma che l'acquirente puo' definire creando obblighi per i venditori.
`issue: I-05 - tipo: presenza - gravita: alta - judge: si`
Pass se: la proposizione compare in una frase autonoma: l'acquirente puo' definire creando obblighi per i venditori; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: l'acquirente puo' definire creando obblighi per i venditori
Fail se: FAIL se la proposizione «l'acquirente puo' definire creando obblighi per i venditori» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 01 clausola 2

## B.6 - il deliverable afferma che la bozza PVC richiede reazione anche prima di un atto definitivo.
`issue: I-06 - tipo: presenza - gravita: alta - judge: si`
Pass se: la proposizione compare in una frase autonoma: la bozza PVC richiede reazione anche prima di un atto definitivo; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: la bozza PVC richiede reazione anche prima di un atto definitivo
Fail se: FAIL se la proposizione «la bozza PVC richiede reazione anche prima di un atto definitivo» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 03 e doc. 04

## B.7 - il deliverable afferma che si deducono benefici mai realizzati.
`issue: I-07 - tipo: valore - gravita: alta - judge: no`
Pass se: nel deliverable compare «si deducono benefici mai realizzati»
Fail se: FAIL se manca «si deducono benefici mai realizzati», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 01 clausola 3

## B.8 - il deliverable afferma che il pagamento potrebbe essere imponibile.
`issue: I-08 - tipo: presenza - gravita: alta - judge: si`
Pass se: la proposizione compare in una frase autonoma: il pagamento potrebbe essere imponibile; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: il pagamento potrebbe essere imponibile
Fail se: FAIL se la proposizione «il pagamento potrebbe essere imponibile» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 01

## B.9 - il deliverable afferma che gli interessi sono da determinare ma la definizione non li include.
`issue: I-09 - tipo: valore - gravita: alta - judge: no`
Pass se: nel deliverable compare «gli interessi sono da determinare ma la definizione non li include»
Fail se: FAIL se manca «gli interessi sono da determinare ma la definizione non li include», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 04

## B.10 - il deliverable afferma che EUR 1.000.000 assorbirebbe la ripresa IVA.
`issue: I-10 - tipo: valore - gravita: media - judge: no`
Pass se: nel deliverable compare «EUR 1.000.000 assorbirebbe la ripresa IVA»
Fail se: FAIL se manca «EUR 1.000.000 assorbirebbe la ripresa IVA», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 01 e doc. 02

## B.11 - il deliverable afferma che EUR 100.000 frammenta pretese omogenee.
`issue: I-11 - tipo: valore - gravita: media - judge: no`
Pass se: nel deliverable compare «EUR 100.000 frammenta pretese omogenee»
Fail se: FAIL se manca «EUR 100.000 frammenta pretese omogenee», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 01

## B.12 - il deliverable afferma che 20% del prezzo non riflette passivita' fiscali storiche.
`issue: I-12 - tipo: valore - gravita: media - judge: no`
Pass se: nel deliverable compare «20% del prezzo non riflette passivita' fiscali storiche»
Fail se: FAIL se manca «20% del prezzo non riflette passivita' fiscali storiche», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 02

## B.13 - il deliverable afferma che puo' scadere prima del potere di accertamento.
`issue: I-13 - tipo: valore - gravita: media - judge: no`
Pass se: nel deliverable compare «puo' scadere prima del potere di accertamento»
Fail se: FAIL se manca «puo' scadere prima del potere di accertamento», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 01

## B.14 - il deliverable afferma che l'acquirente trattiene doppio beneficio.
`issue: I-14 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: l'acquirente trattiene doppio beneficio; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: l'acquirente trattiene doppio beneficio
Fail se: FAIL se la proposizione «l'acquirente trattiene doppio beneficio» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 01 clausola 5

## B.15 - il deliverable afferma che il rischio IVA noto e' escluso.
`issue: I-15 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: il rischio IVA noto e' escluso; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: il rischio IVA noto e' escluso
Fail se: FAIL se la proposizione «il rischio IVA noto e' escluso» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 05

## B.16 - il deliverable afferma che prezzo, polizza e indennizzo possono sovrapporsi.
`issue: I-16 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: prezzo, polizza e indennizzo possono sovrapporsi; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: prezzo, polizza e indennizzo possono sovrapporsi
Fail se: FAIL se la proposizione «prezzo, polizza e indennizzo possono sovrapporsi» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 02 e doc. 05

## B.17 - il deliverable afferma che i venditori rispondono di atti volontari dell'acquirente.
`issue: I-17 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: i venditori rispondono di atti volontari dell'acquirente; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: i venditori rispondono di atti volontari dell'acquirente
Fail se: FAIL se la proposizione «i venditori rispondono di atti volontari dell'acquirente» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 01 clausola 6

## B.18 - il deliverable afferma che il fascicolo non contiene accordo di consolidato e riparto.
`issue: I-18 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: il fascicolo non contiene accordo di consolidato e riparto; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: il fascicolo non contiene accordo di consolidato e riparto
Fail se: FAIL se la proposizione «il fascicolo non contiene accordo di consolidato e riparto» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 03

## B.19 - il deliverable riconduce perimetro temporale illimitato a doc. 01 clausola 1.
`issue: I-01 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01 clausola 1; un richiamo immediatamente adiacente collega il punto a doc. 01 clausola 1
Fail se: FAIL se doc. 01 clausola 1 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01 clausola 1

## B.20 - il deliverable riconduce allocazione straddle a doc. 02 e doc. 06.
`issue: I-02 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 02 e doc. 06; un richiamo immediatamente adiacente collega il punto a doc. 02 e doc. 06
Fail se: FAIL se doc. 02 e doc. 06 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 02 e doc. 06

## B.21 - il deliverable riconduce plusvalenza disposta dal venditore a doc. 06.
`issue: I-03 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 06; un richiamo immediatamente adiacente collega il punto a doc. 06
Fail se: FAIL se doc. 06 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 06

## B.22 - il deliverable riconduce controllo esclusivo acquirente a doc. 01 clausola 2.
`issue: I-04 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01 clausola 2; un richiamo immediatamente adiacente collega il punto a doc. 01 clausola 2
Fail se: FAIL se doc. 01 clausola 2 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01 clausola 2

## B.23 - il deliverable riconduce consenso alle transazioni a doc. 01 clausola 2.
`issue: I-05 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01 clausola 2; un richiamo immediatamente adiacente collega il punto a doc. 01 clausola 2
Fail se: FAIL se doc. 01 clausola 2 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01 clausola 2

## B.24 - il deliverable riconduce urgenze procedurali a doc. 03 e doc. 04.
`issue: I-06 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 03 e doc. 04; un richiamo immediatamente adiacente collega il punto a doc. 03 e doc. 04
Fail se: FAIL se doc. 03 e doc. 04 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 03 e doc. 04

## B.25 - il deliverable riconduce benefici potenziali a doc. 01 clausola 3.
`issue: I-07 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01 clausola 3; un richiamo immediatamente adiacente collega il punto a doc. 01 clausola 3
Fail se: FAIL se doc. 01 clausola 3 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01 clausola 3

## B.26 - il deliverable riconduce gross-up assente a doc. 01.
`issue: I-08 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01; un richiamo immediatamente adiacente collega il punto a doc. 01
Fail se: FAIL se doc. 01 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01

## B.27 - il deliverable riconduce interessi omessi a doc. 04.
`issue: I-09 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 04; un richiamo immediatamente adiacente collega il punto a doc. 04
Fail se: FAIL se doc. 04 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 04

## B.28 - il deliverable riconduce basket generale a doc. 01 e doc. 02.
`issue: I-10 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01 e doc. 02; un richiamo immediatamente adiacente collega il punto a doc. 01 e doc. 02
Fail se: FAIL se doc. 01 e doc. 02 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01 e doc. 02

## B.29 - il deliverable riconduce de minimis elevato a doc. 01.
`issue: I-11 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01; un richiamo immediatamente adiacente collega il punto a doc. 01
Fail se: FAIL se doc. 01 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01

## B.30 - il deliverable riconduce cap insufficiente a doc. 02.
`issue: I-12 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 02; un richiamo immediatamente adiacente collega il punto a doc. 02
Fail se: FAIL se doc. 02 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 02

## B.31 - il deliverable riconduce termine di 18 mesi a doc. 01.
`issue: I-13 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01; un richiamo immediatamente adiacente collega il punto a doc. 01
Fail se: FAIL se doc. 01 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01

## B.32 - il deliverable riconduce recuperi da terzi a doc. 01 clausola 5.
`issue: I-14 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01 clausola 5; un richiamo immediatamente adiacente collega il punto a doc. 01 clausola 5
Fail se: FAIL se doc. 01 clausola 5 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01 clausola 5

## B.33 - il deliverable riconduce polizza W&I a doc. 05.
`issue: I-15 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 05; un richiamo immediatamente adiacente collega il punto a doc. 05
Fail se: FAIL se doc. 05 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 05

## B.34 - il deliverable riconduce divieto di doppio recupero a doc. 02 e doc. 05.
`issue: I-16 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 02 e doc. 05; un richiamo immediatamente adiacente collega il punto a doc. 02 e doc. 05
Fail se: FAIL se doc. 02 e doc. 05 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 02 e doc. 05

## B.35 - il deliverable riconduce condotta post-closing a doc. 01 clausola 6.
`issue: I-17 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01 clausola 6; un richiamo immediatamente adiacente collega il punto a doc. 01 clausola 6
Fail se: FAIL se doc. 01 clausola 6 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01 clausola 6

## B.36 - il deliverable riconduce consolidato fiscale a doc. 03.
`issue: I-18 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 03; un richiamo immediatamente adiacente collega il punto a doc. 03
Fail se: FAIL se doc. 03 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 03

## B.37 - il deliverable richiede limitare a pre-closing e straddle.
`issue: I-01 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «limitare a pre-closing e straddle» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «limitare a pre-closing e straddle» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01 clausola 1

## B.38 - il deliverable richiede usare chiusura contabile al closing con regole per componenti puntuali.
`issue: I-02 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «usare chiusura contabile al closing con regole per componenti puntuali» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «usare chiusura contabile al closing con regole per componenti puntuali» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 02 e doc. 06

## B.39 - il deliverable richiede attribuirne imposte ai venditori.
`issue: I-03 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «attribuirne imposte ai venditori» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «attribuirne imposte ai venditori» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 06

## B.40 - il deliverable richiede attribuire informazione e partecipazione.
`issue: I-04 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «attribuire informazione e partecipazione» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «attribuire informazione e partecipazione» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01 clausola 2

## B.41 - il deliverable richiede richiedere consenso non irragionevole.
`issue: I-05 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «richiedere consenso non irragionevole» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «richiedere consenso non irragionevole» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01 clausola 2

## B.42 - il deliverable richiede prevedere avviso rapido e difese conservative.
`issue: I-06 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «prevedere avviso rapido e difese conservative» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «prevedere avviso rapido e difese conservative» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 03 e doc. 04

## B.43 - il deliverable richiede dedurre solo benefici effettivi e connessi.
`issue: I-07 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «dedurre solo benefici effettivi e connessi» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «dedurre solo benefici effettivi e connessi» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01 clausola 3

## B.44 - il deliverable richiede inserire gross-up e meccanismo di rimborso.
`issue: I-08 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «inserire gross-up e meccanismo di rimborso» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «inserire gross-up e meccanismo di rimborso» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01

## B.45 - il deliverable richiede aggiungere interessi e costi ragionevoli.
`issue: I-09 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «aggiungere interessi e costi ragionevoli» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «aggiungere interessi e costi ragionevoli» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 04

## B.46 - il deliverable richiede escludere tax covenant dal basket generale.
`issue: I-10 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «escludere tax covenant dal basket generale» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «escludere tax covenant dal basket generale» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01 e doc. 02

## B.47 - il deliverable richiede ridurre a EUR 25.000 e aggregare fatti connessi.
`issue: I-11 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «ridurre a EUR 25.000 e aggregare fatti connessi» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «ridurre a EUR 25.000 e aggregare fatti connessi» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01

## B.48 - il deliverable richiede negoziare cap fino al prezzo per imposte pre-closing.
`issue: I-12 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «negoziare cap fino al prezzo per imposte pre-closing» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «negoziare cap fino al prezzo per imposte pre-closing» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 02

## B.49 - il deliverable richiede legare la survival alla decadenza fiscale piu' 60 giorni.
`issue: I-13 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «legare la survival alla decadenza fiscale piu' 60 giorni» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «legare la survival alla decadenza fiscale piu' 60 giorni» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01

## B.50 - il deliverable richiede riversare recuperi netti fino all'indennizzo.
`issue: I-14 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «riversare recuperi netti fino all'indennizzo» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «riversare recuperi netti fino all'indennizzo» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01 clausola 5

## B.51 - il deliverable richiede non trattare la polizza come recupero certo.
`issue: I-15 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «non trattare la polizza come recupero certo» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «non trattare la polizza come recupero certo» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 05

## B.52 - il deliverable richiede inserire ordine di imputazione e rendiconto.
`issue: I-16 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «inserire ordine di imputazione e rendiconto» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «inserire ordine di imputazione e rendiconto» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 02 e doc. 05

## B.53 - il deliverable richiede escludere atti fuori ordinaria gestione non imposti.
`issue: I-17 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «escludere atti fuori ordinaria gestione non imposti» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «escludere atti fuori ordinaria gestione non imposti» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01 clausola 6

## B.54 - il deliverable richiede acquisire accordi 2026-2028.
`issue: I-18 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «acquisire accordi 2026-2028» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «acquisire accordi 2026-2028» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 03

## B.55 - il deliverable non segnala come rischio, criticita' o inadempimento prezzo EUR 48 milioni (doc. 02); elemento tracciato: EUR 48.000.000.
`issue: N-01 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - prezzo EUR 48 milioni non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - prezzo EUR 48 milioni e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 02

## B.56 - il deliverable non segnala come rischio, criticita' o inadempimento bozza PVC non notificata (doc. 04); elemento tracciato: non notificato.
`issue: N-02 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - bozza PVC non notificata non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - bozza PVC non notificata e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 04

## B.57 - il deliverable non segnala come rischio, criticita' o inadempimento credito R&S 2026 (doc. 03).
`issue: N-03 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - credito R&S 2026 non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - credito R&S 2026 e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 03

## B.58 - il deliverable non segnala come rischio, criticita' o inadempimento periodo di locked box (doc. 02).
`issue: N-04 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - periodo di locked box non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - periodo di locked box e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 02

## B.59 - il deliverable non segnala come rischio, criticita' o inadempimento consultazione assicuratore (doc. 05).
`issue: N-05 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - consultazione assicuratore non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - consultazione assicuratore e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 05

## B.60 - il deliverable applica lo stesso test ai quattro limiti dell'indennizzo (basket generale, de minimis, cap e termine di decadenza): livello pattuito, effetto sulla ripresa IVA nota e modifica richiesta.
`issue: CHIUSURA - tipo: presenza - gravita: media - judge: si`
Pass se: per ciascuna delle voci indicate nell'oggetto del criterio il deliverable riporta tutti gli elementi richiesti, applicando a ogni voce lo stesso test
Fail se: almeno una delle voci non e' esaminata, oppure per almeno una voce manca uno degli elementi richiesti, oppure le voci sono esaminate con criteri diversi senza che la differenza sia motivata
Indifferente: l'ordine delle voci, la forma (tabella o testo) e la scelta lessicale, purche' ogni elemento sia riconoscibile per ciascuna voce
Fonte: doc. 01 e doc. 04

## B.61 - il deliverable non afferma che la ripresa IVA descritta nella bozza di PVC diventera' definitiva.
`issue: CHIUSURA - tipo: assenza - gravita: alta - judge: si`
Pass se: presunzione dell'esito non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se presunzione dell'esito e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 04
