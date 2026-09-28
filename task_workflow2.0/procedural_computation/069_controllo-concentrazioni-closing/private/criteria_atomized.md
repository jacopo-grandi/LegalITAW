# WF2-069 - Criteri atomizzati

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

## B.1 - il deliverable afferma che EUR 613 milioni supera EUR 595 milioni.
`issue: I-01 - tipo: valore - gravita: alta - judge: no`
Pass se: nel deliverable compare «EUR 613 milioni supera EUR 595 milioni»
Fail se: FAIL se manca «EUR 613 milioni supera EUR 595 milioni», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 02 e AGCM

## B.2 - il deliverable afferma che almeno due imprese superano EUR 36 milioni.
`issue: I-02 - tipo: valore - gravita: alta - judge: no`
Pass se: nel deliverable compare «almeno due imprese superano EUR 36 milioni»
Fail se: FAIL se manca «almeno due imprese superano EUR 36 milioni», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 02

## B.3 - il deliverable afferma che l'acquisto del 100% conferisce controllo esclusivo.
`issue: I-03 - tipo: presenza - gravita: alta - judge: si`
Pass se: la proposizione compare in una frase autonoma: l'acquisto del 100% conferisce controllo esclusivo; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: l'acquisto del 100% conferisce controllo esclusivo
Fail se: FAIL se la proposizione «l'acquisto del 100% conferisce controllo esclusivo» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 03

## B.4 - il deliverable afferma che il fatturato mondiale di EUR 1,4 miliardi non raggiunge le soglie UE indicate nel pack.
`issue: I-04 - tipo: valore - gravita: alta - judge: no`
Pass se: nel deliverable compare «il fatturato mondiale di EUR 1,4 miliardi non raggiunge le soglie UE indicate nel pack»
Fail se: FAIL se manca «il fatturato mondiale di EUR 1,4 miliardi non raggiunge le soglie UE indicate nel pack», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 02 e doc. 03

## B.5 - il deliverable afferma che il deposito deve precedere la realizzazione.
`issue: I-05 - tipo: presenza - gravita: alta - judge: si`
Pass se: la proposizione compare in una frase autonoma: il deposito deve precedere la realizzazione; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: il deposito deve precedere la realizzazione
Fail se: FAIL se la proposizione «il deposito deve precedere la realizzazione» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 01 e fonti

## B.6 - il deliverable afferma che lo SPA richiede non avvio, non il solo deposito.
`issue: I-06 - tipo: presenza - gravita: alta - judge: si`
Pass se: la proposizione compare in una frase autonoma: lo SPA richiede non avvio, non il solo deposito; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: lo SPA richiede non avvio, non il solo deposito
Fail se: FAIL se la proposizione «lo SPA richiede non avvio, non il solo deposito» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 01

## B.7 - il deliverable afferma che il fascicolo non deve trasformare la condizione contrattuale in una regola legale generale non presente nell'elenco.
`issue: I-07 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: il fascicolo non deve trasformare la condizione contrattuale in una regola legale generale non presente nell'elenco; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: il fascicolo non deve trasformare la condizione contrattuale in una regola legale generale non presente nell'elenco
Fail se: FAIL se la proposizione «il fascicolo non deve trasformare la condizione contrattuale in una regola legale generale non presente nell'elenco» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: fonti congelate

## B.8 - il deliverable afferma che le quote di mercato arrivano il 4 ottobre.
`issue: I-08 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: le quote di mercato arrivano il 4 ottobre; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: le quote di mercato arrivano il 4 ottobre
Fail se: FAIL se la proposizione «le quote di mercato arrivano il 4 ottobre» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 04

## B.9 - il deliverable afferma che il presidio iniziale decorre dal ricevimento della notifica.
`issue: I-09 - tipo: valore - gravita: media - judge: no`
Pass se: nel deliverable compare «il presidio iniziale decorre dal ricevimento della notifica»
Fail se: FAIL se manca «il presidio iniziale decorre dal ricevimento della notifica», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: legge n. 287/1990 art. 16

## B.10 - il deliverable afferma che una richiesta puo' rendere necessario integrare il fascicolo.
`issue: I-10 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: una richiesta puo' rendere necessario integrare il fascicolo; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: una richiesta puo' rendere necessario integrare il fascicolo
Fail se: FAIL se la proposizione «una richiesta puo' rendere necessario integrare il fascicolo» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 04 e fonti

## B.11 - il deliverable afferma che il 15 dicembre lascia margine ma dipende dalla data di deposito e da un eventuale approfondimento.
`issue: I-11 - tipo: valore - gravita: media - judge: no`
Pass se: nel deliverable compare «il 15 dicembre lascia margine ma dipende dalla data di deposito e da un eventuale approfondimento»
Fail se: FAIL se manca «il 15 dicembre lascia margine ma dipende dalla data di deposito e da un eventuale approfondimento», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 01

## B.12 - il deliverable afferma che il team vuole anticipare integrazione operativa.
`issue: I-12 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: il team vuole anticipare integrazione operativa; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: il team vuole anticipare integrazione operativa
Fail se: FAIL se la proposizione «il team vuole anticipare integrazione operativa» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 01 e doc. 04

## B.13 - il deliverable riconduce soglia complessiva a doc. 02 e AGCM.
`issue: I-01 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 02 e AGCM; un richiamo immediatamente adiacente collega il punto a doc. 02 e AGCM
Fail se: FAIL se doc. 02 e AGCM non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 02 e AGCM

## B.14 - il deliverable riconduce soglia individuale a doc. 02.
`issue: I-02 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 02; un richiamo immediatamente adiacente collega il punto a doc. 02
Fail se: FAIL se doc. 02 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 02

## B.15 - il deliverable riconduce concentrazione a doc. 03.
`issue: I-03 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 03; un richiamo immediatamente adiacente collega il punto a doc. 03
Fail se: FAIL se doc. 03 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 03

## B.16 - il deliverable riconduce competenza nazionale a doc. 02 e doc. 03.
`issue: I-04 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 02 e doc. 03; un richiamo immediatamente adiacente collega il punto a doc. 02 e doc. 03
Fail se: FAIL se doc. 02 e doc. 03 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 02 e doc. 03

## B.17 - il deliverable riconduce filing preventivo a doc. 01 e fonti.
`issue: I-05 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01 e fonti; un richiamo immediatamente adiacente collega il punto a doc. 01 e fonti
Fail se: FAIL se doc. 01 e fonti non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01 e fonti

## B.18 - il deliverable riconduce closing condition contrattuale a doc. 01.
`issue: I-06 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01; un richiamo immediatamente adiacente collega il punto a doc. 01
Fail se: FAIL se doc. 01 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01

## B.19 - il deliverable riconduce nessun standstill legale presunto a fonti congelate.
`issue: I-07 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a fonti congelate; un richiamo immediatamente adiacente collega il punto a fonti congelate
Fail se: FAIL se fonti congelate non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: fonti congelate

## B.20 - il deliverable riconduce completezza filing a doc. 04.
`issue: I-08 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 04; un richiamo immediatamente adiacente collega il punto a doc. 04
Fail se: FAIL se doc. 04 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 04

## B.21 - il deliverable riconduce termine di trenta giorni a legge n. 287/1990 art. 16.
`issue: I-09 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a legge n. 287/1990 art. 16; un richiamo immediatamente adiacente collega il punto a legge n. 287/1990 art. 16
Fail se: FAIL se legge n. 287/1990 art. 16 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: legge n. 287/1990 art. 16

## B.22 - il deliverable riconduce richieste informative a doc. 04 e fonti.
`issue: I-10 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 04 e fonti; un richiamo immediatamente adiacente collega il punto a doc. 04 e fonti
Fail se: FAIL se doc. 04 e fonti non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 04 e fonti

## B.23 - il deliverable riconduce long-stop a doc. 01.
`issue: I-11 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01; un richiamo immediatamente adiacente collega il punto a doc. 01
Fail se: FAIL se doc. 01 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01

## B.24 - il deliverable non segnala come rischio, criticita' o inadempimento signing del 15 settembre (doc. 01).
`issue: N-01 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - signing del 15 settembre non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - signing del 15 settembre e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 01

## B.25 - il deliverable non segnala come rischio, criticita' o inadempimento rifinanziamento del debito (SPA allegato).
`issue: N-02 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - rifinanziamento del debito non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - rifinanziamento del debito e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: SPA allegato

## B.26 - il deliverable non segnala come rischio, criticita' o inadempimento fatturato mondiale EUR 1,4 miliardi (doc. 03).
`issue: N-03 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - fatturato mondiale EUR 1,4 miliardi non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - fatturato mondiale EUR 1,4 miliardi e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 03

## B.27 - il deliverable non segnala come rischio, criticita' o inadempimento bozza filing del 27 settembre (doc. 04).
`issue: N-04 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - bozza filing del 27 settembre non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - bozza filing del 27 settembre e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 04

## B.28 - il deliverable verifica separatamente la soglia complessiva e la soglia individuale, indicando per ciascuna il dato di fatturato utilizzato e la fonte della soglia.
`issue: CHIUSURA - tipo: presenza - gravita: media - judge: si`
Pass se: per ciascuna delle voci indicate nell'oggetto del criterio il deliverable riporta tutti gli elementi richiesti, applicando a ogni voce lo stesso test
Fail se: almeno una delle voci non e' esaminata, oppure per almeno una voce manca uno degli elementi richiesti, oppure le voci sono esaminate con criteri diversi senza che la differenza sia motivata
Indifferente: l'ordine delle voci, la forma (tabella o testo) e la scelta lessicale, purche' ogni elemento sia riconoscibile per ciascuna voce
Fonte: doc. 02 e 02_reference_pack.md

## B.29 - il deliverable non afferma che l'Autorita' non avviera' l'istruttoria.
`issue: CHIUSURA - tipo: assenza - gravita: alta - judge: si`
Pass se: presunzione dell'esito non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se presunzione dell'esito e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: 02_reference_pack.md
