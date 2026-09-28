# WF2-051 - Criteri atomizzati

Forma a campi. Ciò che sta sotto la riga non passa al judge.


## A. Forma dell'output (interamente verifica meccanica)

### A.1 [tipo: valore]

- **Verifica** il deliverable è prodotto come file `contract_deadline_audit.md`.
- **Pass se** il file consegnato ha nome `contract_deadline_audit.md`.
- **Fail se** il file ha un altro nome o un'altra estensione.
- **Indifferente** la presenza di intestazioni aggiuntive.
- *non passa al judge:* Fonte task_spec.json, campo deliverable - Gravita media - judge no

### A.2 [tipo: struttura]

- **Verifica** il deliverable contiene, nell'ordine, le cinque sezioni obbligatorie del template.
- **Pass se** le cinque intestazioni di sezione compaiono nell'ordine indicato dal template.
- **Fail se** manca almeno una sezione o l'ordine è diverso.
- **Indifferente** la numerazione delle sottosezioni.
- *non passa al judge:* Fonte public/response_template.md - Gravita media - judge no

### A.3 [tipo: valore]

- **Verifica** il deliverable non supera il limite di 1800 parole.
- **Pass se** il conteggio delle parole del corpo del deliverable non supera 1800.
- **Fail se** il corpo del deliverable supera 1800 parole.
- **Indifferente** la lunghezza delle singole sezioni.
- *non passa al judge:* Fonte task_spec.json, campo limite_parole - Gravita media - judge no

### A.4 [tipo: struttura]

- **Verifica** ogni data indicata nella sezione della cronologia porta il riferimento al documento del fascicolo da cui è ricavata.
- **Pass se** accanto a ciascuna data compare il rinvio a uno dei tre allegati.
- **Fail se** almeno una data della cronologia non porta alcun rinvio a un allegato.
- **Indifferente** la forma del rinvio, numero di documento o titolo.
- *non passa al judge:* Fonte public/01_task.md, richiesta sulla fonte - Gravita media - judge no

### A.5 [tipo: presenza]

- **Verifica** il deliverable distingue i fatti provati dagli atti del fascicolo, le inferenze e i dati mancanti.
- **Pass se** compaiono, riferite a contenuti diversi, le tre distinzioni fra fatto documentato, inferenza e dato mancante.
- **Fail se** il deliverable presenta un solo piano indistinto di affermazioni.
- **Indifferente** le etichette usate per la distinzione.
- *non passa al judge:* Fonte public/response_template.md - Gravita media - judge no

### A.6 [tipo: assenza]

- **Verifica** il deliverable non richiama fonti normative estranee all'elenco chiuso del reference pack.
- **Fail se** compare un riferimento normativo che non figura in `private/fonti_chiuse.json`.
- **Indifferente** il richiamo alle clausole del contratto, che non sono fonti normative.
- *non passa al judge:* Fonte private/fonti_chiuse.json - Gravita media - judge no


## B. Merito

Il fascicolo è esaminato al 14 marzo 2031: la contestazione è stata ricevuta il 3 marzo, il termine di rimedio della clausola 14.2 è scaduto il 13 marzo, il termine di quindici giorni scade il 18 marzo e nel fascicolo non vi è alcun atto posteriore al 3 marzo. Il prompt chiede lo stato dei termini, il calcolo seguito, la fonte di ciascuna decorrenza, i passaggi residui, la distinzione fra profili che incidono e profili che non incidono, e la valutazione della lettura dell'amministratore delegato.

### B.1 [issue: I-01] [tipo: valore]

- **Verifica** il deliverable indica il 13 marzo 2031 come scadenza del termine di dieci giorni della clausola 14.2.
- **Pass se** compare «13 marzo 2031» come scadenza del termine della clausola 14.2. compare «13/03/2031» come scadenza del termine della clausola 14.2.
- **Fail se** è indicata una data diversa, oppure la scadenza del termine della clausola 14.2 non è indicata.
- **Indifferente** l'indicazione dell'ora.
- *non passa al judge:* Fonte clausola 14.2; date_verificate.md - Gravita alta - judge no

### B.2 [issue: I-01] [tipo: attribuzione]

- **Verifica** il deliverable fa decorrere il termine della clausola 14.2 dalla ricezione della PEC del 3 marzo 2031.
- **Pass se** la decorrenza è ricondotta a una fra: «ricezione della PEC», «ricevuta di avvenuta consegna», «consegna della comunicazione del 3 marzo 2031».
- **Fail se** la decorrenza è ricondotta al collaudo del 24 febbraio 2031, alla data di invio del messaggio, oppure l'atto di decorrenza non è indicato.
- **Indifferente** il richiamo alla clausola 16 sul momento di ricezione.
- *non passa al judge:* Fonte clausole 14.2 e 16; ricevuta di consegna - Gravita alta - judge si

### B.3 [issue: I-01] [tipo: presenza]

- **Verifica** il deliverable afferma che il giorno di ricezione della contestazione non si computa nel termine.
- **Pass se** compare l'affermazione che il giorno iniziale non si computa. compare l'affermazione che il termine decorre dal giorno successivo alla ricezione.
- **Fail se** il termine è computato includendo il 3 marzo 2031, oppure la regola di computo non compare.
- **Indifferente** la citazione della norma sul computo dei termini.
- *non passa al judge:* Fonte art. 2963, co. 2 c.c. - Gravita media - judge si

### B.4 [issue: I-02] [tipo: valore]

- **Verifica** il deliverable indica il 18 marzo 2031 come scadenza del termine di quindici giorni assegnato al punto 4 della PEC.
- **Pass se** compare «18 marzo 2031» come scadenza del termine di quindici giorni. compare «18/03/2031» come scadenza del termine di quindici giorni.
- **Fail se** è indicata una data diversa, oppure la scadenza del termine di quindici giorni non è indicata.
- **Indifferente** l'indicazione dell'ora.
- *non passa al judge:* Fonte punto 4 della PEC; date_verificate.md - Gravita alta - judge no

### B.5 [issue: I-02] [tipo: assenza]

- **Verifica** il deliverable non presenta il 13 marzo 2031 come scadenza del termine della diffida.
- **Fail se** il 13 marzo 2031 è indicato come termine entro cui il Fornitore deve adempiere a seguito della diffida.
- **Indifferente** la menzione del 13 marzo 2031 come scadenza del termine della clausola 14.2.
- *non passa al judge:* Fonte punti 3 e 4 della PEC - Gravita alta - judge si

### B.6 [issue: I-03] [tipo: presenza]

- **Verifica** il deliverable espone come due sequenze distinte il termine di rimedio della clausola 14.2 e il termine della diffida.
- **Pass se** le due scadenze compaiono come voci separate della cronologia, ciascuna con la propria fonte.
- **Fail se** le due scadenze sono presentate come un unico termine, oppure una sola delle due compare.
- **Indifferente** l'ordine in cui le due sequenze sono esposte.
- *non passa al judge:* Fonte punti 3 e 4 della PEC; clausole 14.2 e 14.4 - Gravita alta - judge si

### B.7 [issue: I-03] [tipo: qualificazione]

- **Verifica** il deliverable qualifica come diversi gli effetti che il decorso di ciascuno dei due termini può produrre.
- **Pass se** compare l'indicazione che il decorso del termine della clausola 14.2 apre la facoltà di dichiarazione, mentre il decorso del termine di quindici giorni riguarda l'intimazione ad adempiere.
- **Fail se** ai due termini è attribuito il medesimo effetto, oppure gli effetti non sono distinti.
- **Indifferente** l'ordine di trattazione dei due effetti.
- *non passa al judge:* Fonte clausole 14.4 e 14.5; art. 1454 c.c. - Gravita alta - judge si

### B.8 [issue: I-04] [tipo: presenza]

- **Verifica** il deliverable afferma che la clausola risolutiva espressa richiede una dichiarazione del Committente successiva all'inadempimento.
- **Pass se** compare l'affermazione che occorre una dichiarazione di volersi avvalere della clausola risolutiva.
- **Fail se** la necessità della dichiarazione non è affermata, oppure è presentata come facoltativa ai fini della risoluzione.
- **Indifferente** il richiamo alla clausola 14.5.
- *non passa al judge:* Fonte clausole 14.4 e 14.5; art. 1456 c.c. - Gravita alta - judge si

### B.9 [issue: I-04] [tipo: assenza]

- **Verifica** il deliverable non afferma che il contratto si risolve di diritto alla scadenza del termine di dieci giorni.
- **Fail se** compare l'affermazione che alla scadenza del termine della clausola 14.2 il contratto è risolto di diritto o automaticamente.
- **Indifferente** la riproduzione, come citazione del punto 5 della PEC, della frase del Committente.
- *non passa al judge:* Fonte clausola 14.5 - Gravita alta - judge si

### B.10 [issue: I-05] [tipo: qualificazione]

- **Verifica** il deliverable qualifica l'avvertimento del punto 5 della PEC come annuncio anteriore all'inadempimento del termine e non come dichiarazione ai sensi della clausola 14.4.
- **Pass se** compare, riferita a quel punto, una fra: «non integra la dichiarazione», «non vale come dichiarazione di avvalersi della clausola risolutiva», «annuncio preventivo».
- **Fail se** l'avvertimento è qualificato come dichiarazione di avvalersi della clausola risolutiva, oppure la qualificazione non compare.
- **Indifferente** il giudizio sull'opportunità della formulazione usata dal Committente.
- *non passa al judge:* Fonte punto 5 della PEC; clausola 14.4 - Gravita alta - judge si

### B.11 [issue: I-05] [tipo: presenza]

- **Verifica** il deliverable rileva che il fascicolo non contiene comunicazioni posteriori al 3 marzo 2031.
- **Pass se** compare l'indicazione che dopo il 3 marzo 2031 il fascicolo non contiene atti.
- **Fail se** il rilievo non compare, oppure sono dati per esistenti atti successivi.
- **Indifferente** l'elenco dei documenti che il Committente dovrebbe reperire.
- *non passa al judge:* Fonte composizione del fascicolo - Gravita alta - judge si

### B.12 [issue: I-05] [tipo: presenza]

- **Verifica** il deliverable indica come azione la predisposizione della dichiarazione ai sensi della clausola 14.4 da valutare dopo la scadenza dei termini.
- **Pass se** compare l'indicazione di predisporre una dichiarazione di avvalersi della clausola risolutiva.
- **Fail se** l'azione non compare.
- **Indifferente** la forma proposta per la dichiarazione.
- *non passa al judge:* Fonte clausola 14.4 - Gravita media - judge si

### B.13 [issue: I-06] [tipo: qualificazione]

- **Verifica** il deliverable qualifica il termine di dieci giorni della clausola 14.2 come termine di rimedio pattuito e non come termine dell'intimazione ad adempiere.
- **Pass se** compare, riferita al termine di dieci giorni, una fra: «termine di rimedio contrattuale», «cure period contrattuale», «termine pattuito dalle parti».
- **Fail se** il termine di dieci giorni è qualificato come diffida ad adempiere, oppure la qualificazione non compare.
- **Indifferente** il richiamo alla clausola 14.3.
- *non passa al judge:* Fonte clausola 14.2; art. 1454 c.c. - Gravita alta - judge si

### B.14 [issue: I-06] [tipo: presenza]

- **Verifica** il deliverable afferma che il termine dell'intimazione ad adempiere non può essere inferiore a quindici giorni.
- **Pass se** compare l'indicazione del limite minimo di quindici giorni per l'intimazione ad adempiere.
- **Fail se** il limite minimo non compare, oppure è indicato in una misura diversa.
- **Indifferente** il richiamo alle eccezioni al limite minimo.
- *non passa al judge:* Fonte art. 1454, co. 2 c.c. - Gravita alta - judge si

### B.15 [issue: I-07] [tipo: presenza]

- **Verifica** il deliverable afferma che al 14 marzo 2031 il contratto non risulta risolto.
- **Pass se** compare, riferita alla data di riferimento, una fra: «il contratto non risulta risolto», «il rapporto è ancora in essere», «la risoluzione non si è prodotta».
- **Fail se** il contratto è presentato come risolto, oppure lo stato del rapporto alla data di riferimento non è affermato.
- **Indifferente** l'indicazione delle condizioni al verificarsi delle quali la risoluzione potrebbe prodursi.
- *non passa al judge:* Fonte cronologia; clausole 14.4 e 14.5 - Gravita alta - judge si

### B.16 [issue: I-07] [tipo: assenza]

- **Verifica** il deliverable non presenta come già opponibile al Fornitore una risoluzione del contratto.
- **Fail se** compare l'affermazione che la risoluzione è opponibile o efficace nei confronti del Fornitore alla data di riferimento.
- **Indifferente** la descrizione degli effetti che la risoluzione produrrebbe una volta perfezionata.
- *non passa al judge:* Fonte clausola 14.4 - Gravita alta - judge si

### B.17 [issue: I-08] [tipo: presenza]

- **Verifica** il deliverable afferma che il fascicolo non consente di stabilire se l'inadempimento sia stato rimosso entro il 13 marzo 2031.
- **Pass se** compare, riferita all'esito del termine di rimedio, una fra: «non risulta dagli atti», «il fascicolo non lo documenta», «non determinabile con i documenti disponibili».
- **Fail se** l'esito del termine di rimedio è dato per accertato in un senso o nell'altro, oppure la lacuna non è dichiarata.
- **Indifferente** il numero di documenti indicati come necessari.
- *non passa al judge:* Fonte composizione del fascicolo - Gravita alta - judge si

### B.18 [issue: I-08] [tipo: presenza]

- **Verifica** il deliverable indica quali documenti occorrono per accertare l'esito del termine di rimedio.
- **Pass se** compare l'indicazione di almeno un documento da acquisire, fra verbale di nuova prova di resa, rapporto di intervento e corrispondenza successiva al 3 marzo 2031.
- **Fail se** la lacuna è dichiarata senza indicare che cosa serve per colmarla.
- **Indifferente** il numero di documenti elencati.
- *non passa al judge:* Fonte public/01_task.md, richiesta sui dati mancanti - Gravita alta - judge si

### B.19 [issue: I-09] [tipo: qualificazione]

- **Verifica** il deliverable qualifica l'installazione del ricambio entro il 7 marzo 2031 come dichiarazione del Fornitore a verbale e non come fatto accaduto.
- **Pass se** compare, riferita a quell'installazione, una fra: «dichiarazione di intenti», «impegno assunto a verbale», «annunciata e non documentata».
- **Fail se** l'installazione del ricambio è presentata come avvenuta, oppure la qualificazione non compare.
- **Indifferente** la menzione della causa tecnica indicata dal Fornitore.
- *non passa al judge:* Fonte paragrafo 6 del verbale di collaudo - Gravita media - judge si

### B.20 [issue: I-09] [tipo: assenza]

- **Verifica** il deliverable non afferma che la resa contrattuale è stata ripristinata.
- **Fail se** compare l'affermazione che la linea ha raggiunto la resa della clausola 5.1 dopo il collaudo.
- **Indifferente** l'ipotesi, dichiarata come tale, che il ricambio possa aver risolto l'anomalia.
- *non passa al judge:* Fonte assenza di una seconda prova di resa nel fascicolo - Gravita media - judge si

### B.21 [issue: I-10] [tipo: presenza]

- **Verifica** il deliverable afferma che il giudizio sull'importanza dell'inadempimento non è formulabile sui dati del fascicolo.
- **Pass se** compare, riferita all'importanza dell'inadempimento, una fra: «non determinabile con i dati disponibili», «il fascicolo non contiene i dati necessari», «richiede dati di produzione non presenti».
- **Fail se** l'importanza dell'inadempimento è affermata o esclusa sulla base dei soli dati del fascicolo, oppure la questione non è trattata.
- **Indifferente** il richiamo alla norma sull'importanza dell'inadempimento.
- *non passa al judge:* Fonte paragrafo 5 del verbale; art. 1455 c.c. - Gravita media - judge si

### B.22 [issue: I-10] [tipo: presenza]

- **Verifica** il deliverable indica quali dati di produzione occorrono per valutare l'importanza dell'inadempimento.
- **Pass se** compare l'indicazione di almeno un dato fra volumi lavorati, scarti, fermate e ore di indisponibilità della linea dal 24 febbraio 2031.
- **Fail se** la questione è dichiarata indeterminabile senza indicare quali dati servono.
- **Indifferente** il numero di dati elencati.
- *non passa al judge:* Fonte public/01_task.md, richiesta sui dati mancanti - Gravita media - judge si

### B.23 [issue: I-11] [tipo: qualificazione]

- **Verifica** il deliverable qualifica come commisurata alla prestazione inesatta la sospensione del pagamento del saldo.
- **Pass se** compare, riferita alla sospensione del saldo, una fra: «in proporzione», «commisurata», «parziale e proporzionata alla difformita».
- **Fail se** la sospensione integrale del saldo è presentata come dovuta per il solo fatto della contestazione, oppure la questione della misura non è trattata.
- **Indifferente** il richiamo alla norma sull'eccezione di inadempimento.
- *non passa al judge:* Fonte punto 6 della PEC; art. 1460 c.c. - Gravita media - judge si

### B.24 [issue: I-12] [tipo: presenza]

- **Verifica** il deliverable afferma che la ripetizione dell'acconto di euro 180.000,00 presuppone il perfezionamento di un rimedio risolutorio.
- **Pass se** compare l'indicazione che la restituzione dell'acconto dipende dal perfezionamento della risoluzione.
- **Fail se** l'acconto è presentato come ripetibile alla data di riferimento, oppure la condizione non è indicata.
- **Indifferente** il richiamo alla norma sugli effetti della risoluzione.
- *non passa al judge:* Fonte clausola 6.2; art. 1458 c.c. - Gravita bassa - judge si

### B.25 [issue: I-12] [tipo: presenza]

- **Verifica** il deliverable indica come azione l'inventario delle prestazioni ricevute prima di formulare domande restitutorie.
- **Pass se** compare l'indicazione di inventariare le prestazioni ricevute, con menzione dell'impianto installato o della licenza software.
- **Fail se** l'azione non compare.
- **Indifferente** il dettaglio delle voci inventariate.
- *non passa al judge:* Fonte clausole 6.2 e 9.2; art. 1458 c.c. - Gravita bassa - judge si


## C. Date, valori calcolati e chiusura

### C.1 [issue: I-01] [tipo: assenza]

- **Verifica** il deliverable non presenta il 13 marzo 2031 come risultato di un computo decorrente dal collaudo del 24 febbraio 2031.
- **Fail se** il 13 marzo 2031 è ricavato da un termine che decorre dal collaudo.
- **Indifferente** la menzione del collaudo come fatto che ha originato la contestazione.
- *non passa al judge:* Fonte clausola 14.2 - Gravita alta - judge si

### C.2 [issue: I-01] [tipo: assenza]

- **Verifica** il deliverable non presenta la scadenza del termine della clausola 14.2 come risultato di un computo in giorni lavorativi.
- **Fail se** la scadenza è ricavata contando dieci giorni lavorativi.
- **Indifferente** la menzione del giorno della settimana in cui la scadenza cade.
- *non passa al judge:* Fonte clausola 14.2 - Gravita media - judge si

### C.3 [issue: I-02] [tipo: assenza]

- **Verifica** il deliverable non presenta il 18 marzo 2031 come risultato di un termine di quindici giorni decorrente dal collaudo del 24 febbraio 2031.
- **Fail se** il 18 marzo 2031 è ricavato da un termine che decorre dal collaudo.
- **Indifferente** la menzione della data del collaudo nella cronologia.
- *non passa al judge:* Fonte punto 4 della PEC - Gravita media - judge si

### C.4 [issue: N-01] [tipo: assenza]

- **Verifica** il deliverable non segnala come rischio la clausola compromissoria della clausola 15.2, che devolve le controversie ad arbitrato secondo il Regolamento della Camera Arbitrale di Milano.
- **Fail se** la clausola compromissoria della clausola 15.2 compare fra i profili di rischio o fra le clausole da modificare.
- **Indifferente** la menzione della sede arbitrale nella descrizione del contratto.
- *non passa al judge:* Fonte challenge map, N-01 - Gravita media - judge si

### C.5 [issue: N-02] [tipo: assenza]

- **Verifica** il deliverable non segnala come esposizione del Committente la licenza non trasferibile dei moduli software prevista dalla clausola 9.2.
- **Fail se** la licenza non trasferibile della clausola 9.2 compare fra i profili di rischio.
- **Indifferente** la menzione della licenza software nell'inventario delle prestazioni ricevute.
- *non passa al judge:* Fonte challenge map, N-02 - Gravita media - judge si

### C.6 [issue: N-03] [tipo: assenza]

- **Verifica** il deliverable non segnala come irregolarità il computo del termine della clausola 14.2 in giorni di calendario.
- **Fail se** il computo in giorni di calendario compare fra le irregolarità o fra i profili di rischio.
- **Indifferente** la menzione del computo in giorni di calendario nella spiegazione della scadenza.
- *non passa al judge:* Fonte challenge map, N-03 - Gravita media - judge si

### C.7 [issue: X-01] [tipo: assenza]

- **Verifica** simmetria del controllo: il deliverable non tratta come provata l'installazione del ricambio del 7 marzo 2031 mentre tratta come non provato l'esito del termine di rimedio.
- **Fail se** l'installazione del ricambio è data per avvenuta e nello stesso deliverable l'esito del termine di rimedio è dichiarato non documentato.
- **Indifferente** l'ordine in cui i due fatti sono trattati.
- *non passa al judge:* Fonte verbale di collaudo; composizione del fascicolo - Gravita media - judge si

### C.8 [issue: X-02] [tipo: assenza]

- **Verifica** divieto di presunzione dell'esito: il deliverable non afferma che il Fornitore non ha rimosso l'inadempimento entro il 13 marzo 2031.
- **Fail se** compare l'affermazione che l'inadempimento non è stato rimosso entro il termine.
- **Indifferente** l'indicazione della verifica da compiere alla scadenza del termine.
- *non passa al judge:* Fonte composizione del fascicolo - Gravita alta - judge si

### C.9 [issue: X-03] [tipo: assenza]

- **Verifica** sovra-segnalazione: il deliverable non presenta come profilo di rischio la sottoscrizione del verbale di collaudo con riserva.
- **Fail se** la sottoscrizione con riserva compare fra i profili di rischio o fra gli elementi che indeboliscono la posizione del Committente.
- **Indifferente** la menzione della riserva come fatto che conserva le contestazioni.
- *non passa al judge:* Fonte paragrafo 7 del verbale di collaudo - Gravita media - judge si
