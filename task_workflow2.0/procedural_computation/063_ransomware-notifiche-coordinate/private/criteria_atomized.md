# WF2-063 - Criteri atomizzati

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

## B.1 - il deliverable afferma che il dies a quo di Saliceto e' il 16 febbraio alle 08:20, non il primo alert delle 06:42.
`issue: I-01 - tipo: valore - gravita: alta - judge: no`
Pass se: nel deliverable compare «il dies a quo di Saliceto e' il 16 febbraio alle 08:20, non il primo alert delle 06:42»
Fail se: FAIL se manca «il dies a quo di Saliceto e' il 16 febbraio alle 08:20, non il primo alert delle 06:42», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 01

## B.2 - il deliverable afferma che Kairone doveva informare senza ritardo e comunque entro il limite contrattuale.
`issue: I-02 - tipo: presenza - gravita: alta - judge: si`
Pass se: la proposizione compare in una frase autonoma: Kairone doveva informare senza ritardo e comunque entro il limite contrattuale; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: Kairone doveva informare senza ritardo e comunque entro il limite contrattuale
Fail se: FAIL se la proposizione «Kairone doveva informare senza ritardo e comunque entro il limite contrattuale» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 02

## B.3 - il deliverable afferma che la scadenza e' 17 febbraio 2027 alle 08:20.
`issue: I-03 - tipo: valore - gravita: alta - judge: no`
Pass se: nel deliverable compare «la scadenza e' 17 febbraio 2027 alle 08:20»
Fail se: FAIL se manca «la scadenza e' 17 febbraio 2027 alle 08:20», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 01 e doc. 04

## B.4 - il deliverable afferma che la scadenza e' 19 febbraio 2027 alle 08:20.
`issue: I-04 - tipo: valore - gravita: alta - judge: no`
Pass se: nel deliverable compare «la scadenza e' 19 febbraio 2027 alle 08:20»
Fail se: FAIL se manca «la scadenza e' 19 febbraio 2027 alle 08:20», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 01 e fonti

## B.5 - il deliverable afferma che la relazione finale va calendarizzata a un mese dalla notifica completa, con aggiornamenti se l'incidente perdura.
`issue: I-05 - tipo: valore - gravita: alta - judge: no`
Pass se: nel deliverable compare «la relazione finale va calendarizzata a un mese dalla notifica completa, con aggiornamenti se l'incidente perdura»
Fail se: FAIL se manca «la relazione finale va calendarizzata a un mese dalla notifica completa, con aggiornamenti se l'incidente perdura», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: fonti e registro evento

## B.6 - il deliverable afferma che la scadenza e' 19 febbraio 2027 alle 08:20 e il rischio non e' improbabile.
`issue: I-06 - tipo: valore - gravita: alta - judge: no`
Pass se: nel deliverable compare «la scadenza e' 19 febbraio 2027 alle 08:20 e il rischio non e' improbabile»
Fail se: FAIL se manca «la scadenza e' 19 febbraio 2027 alle 08:20 e il rischio non e' improbabile», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 01, doc. 03 e GDPR

## B.7 - il deliverable afferma che dati sanitari ed esfiltrazione sostengono un rischio elevato.
`issue: I-07 - tipo: presenza - gravita: alta - judge: si`
Pass se: la proposizione compare in una frase autonoma: dati sanitari ed esfiltrazione sostengono un rischio elevato; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: dati sanitari ed esfiltrazione sostengono un rischio elevato
Fail se: FAIL se la proposizione «dati sanitari ed esfiltrazione sostengono un rischio elevato» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 03, doc. 08 e doc. 09

## B.8 - il deliverable afferma che le 48 ore scadono il 18 febbraio 2027 alle 08:20.
`issue: I-08 - tipo: valore - gravita: alta - judge: no`
Pass se: nel deliverable compare «le 48 ore scadono il 18 febbraio 2027 alle 08:20»
Fail se: FAIL se manca «le 48 ore scadono il 18 febbraio 2027 alle 08:20», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 05

## B.9 - il deliverable afferma che le 24 ore scadono il 17 febbraio 2027 alle 08:20.
`issue: I-09 - tipo: valore - gravita: media - judge: no`
Pass se: nel deliverable compare «le 24 ore scadono il 17 febbraio 2027 alle 08:20»
Fail se: FAIL se manca «le 24 ore scadono il 17 febbraio 2027 alle 08:20», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 06

## B.10 - il deliverable afferma che la regola unica delle 72 ore omette NIS 24h, polizza 48h e cliente 24h.
`issue: I-10 - tipo: valore - gravita: media - judge: no`
Pass se: nel deliverable compare «la regola unica delle 72 ore omette NIS 24h, polizza 48h e cliente 24h»
Fail se: FAIL se manca «la regola unica delle 72 ore omette NIS 24h, polizza 48h e cliente 24h», se un valore o una data differiscono, oppure se il rapporto logico e' invertito. Una formulazione più vaga o parziale, o che cambia anche uno solo fra soggetti, valori, date e rapporto logico, conta come mancante.
Indifferente la scelta delle parole, purché resti la stessa proposizione, con gli stessi soggetti, valori, date e rapporto logico; maiuscole, apostrofi tipografici e punteggiatura finale.
Fonte: doc. 07

## B.11 - il deliverable afferma che il punto di contatto NIS e' direzione sicurezza, non DPO.
`issue: I-11 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: il punto di contatto NIS e' direzione sicurezza, non DPO; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: il punto di contatto NIS e' direzione sicurezza, non DPO
Fail se: FAIL se la proposizione «il punto di contatto NIS e' direzione sicurezza, non DPO» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 04 e doc. 07

## B.12 - il deliverable afferma che la bozza omette l'esfiltrazione e il recapito.
`issue: I-12 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: la bozza omette l'esfiltrazione e il recapito; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: la bozza omette l'esfiltrazione e il recapito
Fail se: FAIL se la proposizione «la bozza omette l'esfiltrazione e il recapito» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 09

## B.13 - il deliverable afferma che l'incertezza sulla composizione dei 62 GB non giustifica attendere.
`issue: I-13 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: l'incertezza sulla composizione dei 62 GB non giustifica attendere; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: l'incertezza sulla composizione dei 62 GB non giustifica attendere
Fail se: FAIL se la proposizione «l'incertezza sulla composizione dei 62 GB non giustifica attendere» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 08 e GDPR

## B.14 - il deliverable afferma che immagini, log e indicatori devono restare integri mentre si ripristina.
`issue: I-14 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: immagini, log e indicatori devono restare integri mentre si ripristina; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: immagini, log e indicatori devono restare integri mentre si ripristina
Fail se: FAIL se la proposizione «immagini, log e indicatori devono restare integri mentre si ripristina» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 08 e doc. 10

## B.15 - il deliverable afferma che la scadenza imposta dall'attaccante non sospende notifiche.
`issue: I-15 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: la scadenza imposta dall'attaccante non sospende notifiche; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: la scadenza imposta dall'attaccante non sospende notifiche
Fail se: FAIL se la proposizione «la scadenza imposta dall'attaccante non sospende notifiche» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 10

## B.16 - il deliverable afferma che i medesimi fatti alimentano cinque flussi ma i test giuridici non coincidono.
`issue: I-16 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: i medesimi fatti alimentano cinque flussi ma i test giuridici non coincidono; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: i medesimi fatti alimentano cinque flussi ma i test giuridici non coincidono
Fail se: FAIL se la proposizione «i medesimi fatti alimentano cinque flussi ma i test giuridici non coincidono» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: tutti i documenti

## B.17 - il deliverable afferma che non e' noto quali record compongano tutti i 62 GB.
`issue: I-17 - tipo: presenza - gravita: media - judge: si`
Pass se: la proposizione compare in una frase autonoma: non e' noto quali record compongano tutti i 62 GB; la proposizione compare in una riga di tabella con tutti i soggetti, valori e rapporti logici: non e' noto quali record compongano tutti i 62 GB
Fail se: FAIL se la proposizione «non e' noto quali record compongano tutti i 62 GB» manca, e' negata o cambia soggetto, valore o rapporto logico; PASS solo in uno dei due casi elencati.
Indifferente: forma in prosa o tabella e ordine delle parole.
Fonte: doc. 08

## B.18 - il deliverable riconduce momento di conoscenza del titolare a doc. 01.
`issue: I-01 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01; un richiamo immediatamente adiacente collega il punto a doc. 01
Fail se: FAIL se doc. 01 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01

## B.19 - il deliverable riconduce obbligo del responsabile a doc. 02.
`issue: I-02 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 02; un richiamo immediatamente adiacente collega il punto a doc. 02
Fail se: FAIL se doc. 02 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 02

## B.20 - il deliverable riconduce pre-notifica NIS entro 24 ore a doc. 01 e doc. 04.
`issue: I-03 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01 e doc. 04; un richiamo immediatamente adiacente collega il punto a doc. 01 e doc. 04
Fail se: FAIL se doc. 01 e doc. 04 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01 e doc. 04

## B.21 - il deliverable riconduce notifica NIS entro 72 ore a doc. 01 e fonti.
`issue: I-04 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01 e fonti; un richiamo immediatamente adiacente collega il punto a doc. 01 e fonti
Fail se: FAIL se doc. 01 e fonti non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01 e fonti

## B.22 - il deliverable riconduce relazione finale NIS a fonti e registro evento.
`issue: I-05 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a fonti e registro evento; un richiamo immediatamente adiacente collega il punto a fonti e registro evento
Fail se: FAIL se fonti e registro evento non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: fonti e registro evento

## B.23 - il deliverable riconduce notifica GDPR entro 72 ore a doc. 01, doc. 03 e GDPR.
`issue: I-06 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 01, doc. 03 e GDPR; un richiamo immediatamente adiacente collega il punto a doc. 01, doc. 03 e GDPR
Fail se: FAIL se doc. 01, doc. 03 e GDPR non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 01, doc. 03 e GDPR

## B.24 - il deliverable riconduce comunicazione agli interessati a doc. 03, doc. 08 e doc. 09.
`issue: I-07 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 03, doc. 08 e doc. 09; un richiamo immediatamente adiacente collega il punto a doc. 03, doc. 08 e doc. 09
Fail se: FAIL se doc. 03, doc. 08 e doc. 09 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 03, doc. 08 e doc. 09

## B.25 - il deliverable riconduce avviso all'assicuratore a doc. 05.
`issue: I-08 - tipo: attribuzione - gravita: alta - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 05; un richiamo immediatamente adiacente collega il punto a doc. 05
Fail se: FAIL se doc. 05 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 05

## B.26 - il deliverable riconduce avviso al cliente Cerasia a doc. 06.
`issue: I-09 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 06; un richiamo immediatamente adiacente collega il punto a doc. 06
Fail se: FAIL se doc. 06 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 06

## B.27 - il deliverable riconduce runbook con termini fusi a doc. 07.
`issue: I-10 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 07; un richiamo immediatamente adiacente collega il punto a doc. 07
Fail se: FAIL se doc. 07 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 07

## B.28 - il deliverable riconduce owner NIS errato a doc. 04 e doc. 07.
`issue: I-11 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 04 e doc. 07; un richiamo immediatamente adiacente collega il punto a doc. 04 e doc. 07
Fail se: FAIL se doc. 04 e doc. 07 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 04 e doc. 07

## B.29 - il deliverable riconduce bozza interessati incompleta a doc. 09.
`issue: I-12 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 09; un richiamo immediatamente adiacente collega il punto a doc. 09
Fail se: FAIL se doc. 09 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 09

## B.30 - il deliverable riconduce notifica per fasi a doc. 08 e GDPR.
`issue: I-13 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 08 e GDPR; un richiamo immediatamente adiacente collega il punto a doc. 08 e GDPR
Fail se: FAIL se doc. 08 e GDPR non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 08 e GDPR

## B.31 - il deliverable riconduce conservazione probatoria a doc. 08 e doc. 10.
`issue: I-14 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 08 e doc. 10; un richiamo immediatamente adiacente collega il punto a doc. 08 e doc. 10
Fail se: FAIL se doc. 08 e doc. 10 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 08 e doc. 10

## B.32 - il deliverable riconduce riscatto non sospensivo a doc. 10.
`issue: I-15 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 10; un richiamo immediatamente adiacente collega il punto a doc. 10
Fail se: FAIL se doc. 10 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 10

## B.33 - il deliverable riconduce registro unico dei fatti, decisioni separate a tutti i documenti.
`issue: I-16 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a tutti i documenti; un richiamo immediatamente adiacente collega il punto a tutti i documenti
Fail se: FAIL se tutti i documenti non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: tutti i documenti

## B.34 - il deliverable riconduce lacuna sull'estensione a doc. 08.
`issue: I-17 - tipo: attribuzione - gravita: media - judge: si`
Pass se: la stessa frase, riga di tabella o nota collega il punto a doc. 08; un richiamo immediatamente adiacente collega il punto a doc. 08
Fail se: FAIL se doc. 08 non e' collegata al punto, se e' collegata a un punto diverso o se e' sostituita da una fonte non ammessa; PASS solo in uno dei due casi elencati.
Indifferente: forma del richiamo: doc., documento, clausola, riga o nota.
Fonte: doc. 08

## B.35 - il deliverable richiede ancorare tutti i termini del titolare alle 08:20.
`issue: I-01 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «ancorare tutti i termini del titolare alle 08:20» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «ancorare tutti i termini del titolare alle 08:20» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01

## B.36 - il deliverable richiede registrare 05:55 e 07:48 come eventi distinti.
`issue: I-02 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «registrare 05:55 e 07:48 come eventi distinti» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «registrare 05:55 e 07:48 come eventi distinti» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 02

## B.37 - il deliverable richiede inviare pre-notifica ACN con natura dolosa e possibile impatto.
`issue: I-03 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «inviare pre-notifica ACN con natura dolosa e possibile impatto» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «inviare pre-notifica ACN con natura dolosa e possibile impatto» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01 e doc. 04

## B.38 - il deliverable richiede trasmettere valutazione iniziale, gravita' e indicatori disponibili.
`issue: I-04 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «trasmettere valutazione iniziale, gravita' e indicatori disponibili» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «trasmettere valutazione iniziale, gravita' e indicatori disponibili» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01 e fonti

## B.39 - il deliverable richiede fissare presidio al 19 marzo 2027 e verificare lo stato.
`issue: I-05 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «fissare presidio al 19 marzo 2027 e verificare lo stato» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «fissare presidio al 19 marzo 2027 e verificare lo stato» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: fonti e registro evento

## B.40 - il deliverable richiede notificare il Garante anche per fasi se mancano dettagli.
`issue: I-06 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «notificare il Garante anche per fasi se mancano dettagli» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «notificare il Garante anche per fasi se mancano dettagli» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 01, doc. 03 e GDPR

## B.41 - il deliverable richiede comunicare senza ingiustificato ritardo con natura, conseguenze, misure e contatto.
`issue: I-07 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «comunicare senza ingiustificato ritardo con natura, conseguenze, misure e contatto» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «comunicare senza ingiustificato ritardo con natura, conseguenze, misure e contatto» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 03, doc. 08 e doc. 09

## B.42 - il deliverable richiede inviare avviso cautelativo e chiedere consenso alle spese non urgenti.
`issue: I-08 - tipo: presenza - gravita: alta - judge: si`
Pass se: il deliverable chiede l'azione «inviare avviso cautelativo e chiedere consenso alle spese non urgenti» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «inviare avviso cautelativo e chiedere consenso alle spese non urgenti» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 05

## B.43 - il deliverable richiede inviare avviso contrattuale e aggiornamenti giornalieri.
`issue: I-09 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «inviare avviso contrattuale e aggiornamenti giornalieri» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «inviare avviso contrattuale e aggiornamenti giornalieri» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 06

## B.44 - il deliverable richiede sostituire la riga unica con scadenze e owner separati.
`issue: I-10 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «sostituire la riga unica con scadenze e owner separati» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «sostituire la riga unica con scadenze e owner separati» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 07

## B.45 - il deliverable richiede assegnare approvazione aziendale e invio al punto registrato.
`issue: I-11 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «assegnare approvazione aziendale e invio al punto registrato» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «assegnare approvazione aziendale e invio al punto registrato» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 04 e doc. 07

## B.46 - il deliverable richiede correggere contenuto prima dell'invio.
`issue: I-12 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «correggere contenuto prima dell'invio» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «correggere contenuto prima dell'invio» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 09

## B.47 - il deliverable richiede inviare dati disponibili e integrare senza ritardo.
`issue: I-13 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «inviare dati disponibili e integrare senza ritardo» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «inviare dati disponibili e integrare senza ritardo» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 08 e GDPR

## B.48 - il deliverable richiede preservare copie, catena di custodia e decision log.
`issue: I-14 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «preservare copie, catena di custodia e decision log» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «preservare copie, catena di custodia e decision log» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 08 e doc. 10

## B.49 - il deliverable richiede procedere con gli adempimenti senza attendere il 18 febbraio.
`issue: I-15 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «procedere con gli adempimenti senza attendere il 18 febbraio» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «procedere con gli adempimenti senza attendere il 18 febbraio» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 10

## B.50 - il deliverable richiede mantenere fonte fattuale unica con decisioni e versioni per destinatario.
`issue: I-16 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «mantenere fonte fattuale unica con decisioni e versioni per destinatario» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «mantenere fonte fattuale unica con decisioni e versioni per destinatario» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: tutti i documenti

## B.51 - il deliverable richiede aprire workstream forense con checkpoint alle 18:00.
`issue: I-17 - tipo: presenza - gravita: media - judge: si`
Pass se: il deliverable chiede l'azione «aprire workstream forense con checkpoint alle 18:00» come passo da compiere, e non come semplice possibilità, oppure la esegue direttamente (per esempio nel testo rivisto, nella tabella o nella cronologia).
Fail se: l'azione manca; oppure è solo eventuale, facoltativa o rinviata a una valutazione successiva («valutare se», «eventualmente», «si potrebbe»); oppure è indicata in modo così generico che «aprire workstream forense con checkpoint alle 18:00» non è riconoscibile; oppure è sostituita da un'azione incompatibile.
Indifferente chi deve compiere l'azione e con quale priorità; la forma (richiesta, raccomandazione vincolante o modifica già apportata).
Fonte: doc. 08

## B.52 - il deliverable indica come conseguenza di momento di conoscenza del titolare che il dies a quo dei termini di notifica e' il 16 febbraio 2027 alle 08:20.
`issue: I-01 - tipo: presenza - gravita: alta - judge: si`
Pass se: la conseguenza e' espressa nel testo: il dies a quo dei termini di notifica e' il 16 febbraio 2027 alle 08:20; la conseguenza compare in una cella dedicata della matrice: il dies a quo dei termini di notifica e' il 16 febbraio 2027 alle 08:20
Fail se: FAIL se manca «il dies a quo dei termini di notifica e' il 16 febbraio 2027 alle 08:20» o compare una conseguenza incompatibile; PASS solo in uno dei due casi elencati.
Indifferente: collocazione in prosa o tabella.
Fonte: doc. 01

## B.53 - il deliverable indica come conseguenza di obbligo del responsabile che il termine del responsabile non sostituisce quello del titolare.
`issue: I-02 - tipo: presenza - gravita: alta - judge: si`
Pass se: la conseguenza e' espressa nel testo: il termine del responsabile non sostituisce quello del titolare; la conseguenza compare in una cella dedicata della matrice: il termine del responsabile non sostituisce quello del titolare
Fail se: FAIL se manca «il termine del responsabile non sostituisce quello del titolare» o compare una conseguenza incompatibile; PASS solo in uno dei due casi elencati.
Indifferente: collocazione in prosa o tabella.
Fonte: doc. 02

## B.54 - il deliverable indica come conseguenza di pre-notifica NIS entro 24 ore che il primo adempimento NIS precede la notifica completa.
`issue: I-03 - tipo: presenza - gravita: alta - judge: si`
Pass se: la conseguenza e' espressa nel testo: il primo adempimento NIS precede la notifica completa; la conseguenza compare in una cella dedicata della matrice: il primo adempimento NIS precede la notifica completa
Fail se: FAIL se manca «il primo adempimento NIS precede la notifica completa» o compare una conseguenza incompatibile; PASS solo in uno dei due casi elencati.
Indifferente: collocazione in prosa o tabella.
Fonte: doc. 01 e doc. 04

## B.55 - il deliverable indica come conseguenza di notifica NIS entro 72 ore che il secondo adempimento resta distinto dalla pre-notifica.
`issue: I-04 - tipo: presenza - gravita: alta - judge: si`
Pass se: la conseguenza e' espressa nel testo: il secondo adempimento resta distinto dalla pre-notifica; la conseguenza compare in una cella dedicata della matrice: il secondo adempimento resta distinto dalla pre-notifica
Fail se: FAIL se manca «il secondo adempimento resta distinto dalla pre-notifica» o compare una conseguenza incompatibile; PASS solo in uno dei due casi elencati.
Indifferente: collocazione in prosa o tabella.
Fonte: doc. 01 e fonti

## B.56 - il deliverable indica come conseguenza di relazione finale NIS che la chiusura tecnica non cancella l'obbligo.
`issue: I-05 - tipo: presenza - gravita: alta - judge: si`
Pass se: la conseguenza e' espressa nel testo: la chiusura tecnica non cancella l'obbligo; la conseguenza compare in una cella dedicata della matrice: la chiusura tecnica non cancella l'obbligo
Fail se: FAIL se manca «la chiusura tecnica non cancella l'obbligo» o compare una conseguenza incompatibile; PASS solo in uno dei due casi elencati.
Indifferente: collocazione in prosa o tabella.
Fonte: fonti e registro evento

## B.57 - il deliverable indica come conseguenza di notifica GDPR entro 72 ore che la notifica privacy ha destinatario e test diversi dalla NIS.
`issue: I-06 - tipo: presenza - gravita: alta - judge: si`
Pass se: la conseguenza e' espressa nel testo: la notifica privacy ha destinatario e test diversi dalla NIS; la conseguenza compare in una cella dedicata della matrice: la notifica privacy ha destinatario e test diversi dalla NIS
Fail se: FAIL se manca «la notifica privacy ha destinatario e test diversi dalla NIS» o compare una conseguenza incompatibile; PASS solo in uno dei due casi elencati.
Indifferente: collocazione in prosa o tabella.
Fonte: doc. 01, doc. 03 e GDPR

## B.58 - il deliverable indica come conseguenza di comunicazione agli interessati che non esiste un termine fisso di 72 ore per l'art. 34.
`issue: I-07 - tipo: presenza - gravita: alta - judge: si`
Pass se: la conseguenza e' espressa nel testo: non esiste un termine fisso di 72 ore per l'art. 34; la conseguenza compare in una cella dedicata della matrice: non esiste un termine fisso di 72 ore per l'art. 34
Fail se: FAIL se manca «non esiste un termine fisso di 72 ore per l'art. 34» o compare una conseguenza incompatibile; PASS solo in uno dei due casi elencati.
Indifferente: collocazione in prosa o tabella.
Fonte: doc. 03, doc. 08 e doc. 09

## B.59 - il deliverable non segnala come rischio, criticita' o inadempimento primo alert non qualificato (doc. 01).
`issue: N-01 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - primo alert non qualificato non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - primo alert non qualificato e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 01

## B.60 - il deliverable non segnala come rischio, criticita' o inadempimento backup clinici integri (doc. 03).
`issue: N-02 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - backup clinici integri non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - backup clinici integri e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 03

## B.61 - il deliverable non segnala come rischio, criticita' o inadempimento scadenza del riscatto (doc. 10); elemento tracciato: 18 febbraio ore 12:00.
`issue: N-03 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - scadenza del riscatto non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - scadenza del riscatto e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 10

## B.62 - il deliverable non segnala come rischio, criticita' o inadempimento festivita' e fine settimana (calendario).
`issue: N-04 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - festivita' e fine settimana non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - festivita' e fine settimana e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: calendario

## B.63 - il deliverable non segnala come rischio, criticita' o inadempimento DPO consultato (doc. 07).
`issue: N-05 - tipo: assenza - gravita: media - judge: si`
Pass se: sovra-segnalazione - DPO consultato non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se sovra-segnalazione - DPO consultato e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: doc. 07

## B.64 - il deliverable indica dies a quo, termine e destinatario per ciascuno dei cinque flussi di comunicazione (pre-notifica e notifica NIS, notifica all'autorita' di protezione dei dati, comunicazione agli interessati, avviso all'assicuratore, avviso al cliente Cerasia).
`issue: CHIUSURA - tipo: presenza - gravita: media - judge: si`
Pass se: per ciascuna delle voci indicate nell'oggetto del criterio il deliverable riporta tutti gli elementi richiesti, applicando a ogni voce lo stesso test
Fail se: almeno una delle voci non e' esaminata, oppure per almeno una voce manca uno degli elementi richiesti, oppure le voci sono esaminate con criteri diversi senza che la differenza sia motivata
Indifferente: l'ordine delle voci, la forma (tabella o testo) e la scelta lessicale, purche' ogni elemento sia riconoscibile per ciascuna voce
Fonte: doc. 04, doc. 05, doc. 06 e doc. 09

## B.65 - il deliverable non afferma che l'autorita' non contestera' l'incidente o le notifiche.
`issue: CHIUSURA - tipo: assenza - gravita: alta - judge: si`
Pass se: presunzione dell'esito non e' presentato come rischio, criticita', inadempimento o conclusione negativa
Fail se: FAIL se presunzione dell'esito e' presentato anche una sola volta come rischio, criticita', inadempimento o conclusione negativa; PASS altrimenti.
Indifferente: la mera menzione fattuale fuori da elenchi o conclusioni negative.
Fonte: 01_task.md
