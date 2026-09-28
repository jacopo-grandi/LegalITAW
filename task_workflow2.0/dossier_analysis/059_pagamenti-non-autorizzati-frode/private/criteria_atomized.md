# WF2-059 - Criteri atomizzati

Forma a campi. Ciò che sta sotto la riga non passa al judge.


## A. Forma dell'output (interamente verifica meccanica)

### A.1 [tipo: valore]

- **Verifica** il deliverable è prodotto come file `evidence_and_liability_memo.md`.
- **Pass se** il file consegnato ha nome `evidence_and_liability_memo.md`.
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

- **Verifica** il deliverable non supera il limite di 2000 parole.
- **Pass se** il conteggio delle parole del corpo del deliverable non supera 2000.
- **Fail se** il corpo del deliverable supera 2000 parole.
- **Indifferente** la lunghezza delle singole sezioni.
- *non passa al judge:* Fonte task_spec.json, campo limite_parole - Gravita media - judge no

### A.4 [tipo: struttura]

- **Verifica** la matrice delle evidenze riporta una riga per ciascuna delle sei operazioni disconosciute.
- **Pass se** nella sezione della matrice compaiono sei righe, una per ciascuna operazione.
- **Fail se** le righe sono meno di sei, oppure le operazioni sono trattate in forma discorsiva senza matrice.
- **Indifferente** l'ordine delle colonne.
- *non passa al judge:* Fonte public/response_template.md - Gravita media - judge no

### A.5 [tipo: struttura]

- **Verifica** ogni riga della matrice delle evidenze porta il riferimento al documento da cui il dato è ricavato.
- **Pass se** accanto a ciascuna riga compare il rinvio a uno degli allegati.
- **Fail se** almeno una riga della matrice non porta alcun rinvio a un allegato.
- **Indifferente** la forma del rinvio, numero di documento o titolo.
- *non passa al judge:* Fonte public/01_task.md, richiesta sulla fonte - Gravita media - judge no

### A.6 [tipo: presenza]

- **Verifica** il deliverable distingue i fatti provati dagli atti, le inferenze e i dati mancanti.
- **Pass se** compaiono, riferite a contenuti diversi, le tre distinzioni fra fatto documentato, inferenza e dato mancante.
- **Fail se** il deliverable presenta un solo piano indistinto di affermazioni.
- **Indifferente** le etichette usate per la distinzione.
- *non passa al judge:* Fonte public/response_template.md - Gravita media - judge no

### A.7 [tipo: assenza]

- **Verifica** il deliverable non richiama fonti normative estranee all'elenco chiuso del reference pack.
- **Fail se** compare un riferimento normativo che non figura in `private/fonti_chiuse.json`.
- **Indifferente** il richiamo alle clausole del contratto di conto, che non sono fonti normative.
- *non passa al judge:* Fonte private/fonti_chiuse.json - Gravita media - judge no


## B. Merito

Il fascicolo è esaminato al 27 marzo 2031: le sei operazioni sono state disconosciute il 12 marzo, le credenziali sono bloccate, il reclamo è stato rigettato il 20 marzo e la documentazione tecnica non è stata trasmessa. Il prompt chiede la matrice operazione per operazione con la fonte di ciascun dato, l'allocazione della responsabilità e dell'onere della prova, la valutazione una per una delle tesi della banca, la distinzione fra profili che incidono e profili che non incidono, e la valutazione della lettura del consulente.

### B.1 [issue: I-01] [tipo: qualificazione]

- **Verifica** il deliverable qualifica il cliente come utente che non è consumatore e che non ha i requisiti dimensionali della microimpresa.
- **Pass se** compare, riferita al cliente, una fra: «non è microimpresa», «non rientra nella nozione di microimpresa», «supera i requisiti dimensionali della microimpresa».
- **Fail se** il cliente è qualificato come microimpresa o come consumatore, oppure la qualificazione non compare.
- **Indifferente** il richiamo alla fonte che definisce i requisiti dimensionali.
- *non passa al judge:* Fonte sezione II delle condizioni di conto - Gravita alta - judge si

### B.2 [issue: I-01] [tipo: attribuzione]

- **Verifica** il deliverable fonda la qualificazione del cliente sui dati dimensionali della scheda anagrafica.
- **Pass se** la qualificazione è ricondotta a una fra: «34 dipendenti», «fatturato di euro 9.840.000,00», «sezione II delle condizioni di conto».
- **Fail se** la qualificazione è affermata senza indicare i dati da cui è ricavata.
- **Indifferente** l'indicazione del totale dell'attivo.
- *non passa al judge:* Fonte sezione II delle condizioni di conto - Gravita alta - judge si

### B.3 [issue: I-01] [tipo: presenza]

- **Verifica** il deliverable afferma che la deroga della clausola 18.2 è ammessa per questo rapporto.
- **Pass se** compare, riferita alla clausola 18.2, una fra: «la deroga è ammessa», «la deroga è efficace», «le parti potevano derogare».
- **Fail se** la deroga è presentata come inefficace o nulla, oppure l'ammissibilità non è affermata.
- **Indifferente** il richiamo alla norma che consente la deroga.
- *non passa al judge:* Fonte clausole 18.1 e 18.2 - Gravita alta - judge si

### B.4 [issue: I-02] [tipo: presenza]

- **Verifica** il deliverable afferma che la deroga non si estende all'obbligo di rimborso del prestatore di servizi di pagamento.
- **Pass se** compare l'indicazione che l'obbligo di rimborso resta fuori dal perimetro della deroga.
- **Fail se** l'obbligo di rimborso è presentato come derogato, oppure la questione del perimetro non è trattata.
- **Indifferente** il richiamo all'articolo che disciplina il rimborso.
- *non passa al judge:* Fonte clausole 18.2 e 18.4 - Gravita alta - judge si

### B.5 [issue: I-02] [tipo: presenza]

- **Verifica** il deliverable afferma che la deroga non si estende al termine massimo per la comunicazione dell'operazione non autorizzata.
- **Pass se** compare l'indicazione che il termine di comunicazione resta fuori dal perimetro della deroga.
- **Fail se** il termine di comunicazione è presentato come derogato, oppure la questione non è trattata.
- **Indifferente** l'indicazione della durata del termine.
- *non passa al judge:* Fonte clausole 18.2 e 18.4 - Gravita alta - judge si

### B.6 [issue: I-02] [tipo: presenza]

- **Verifica** il deliverable afferma che la deroga ha spostato sul cliente l'onere di provare la mancata autorizzazione.
- **Pass se** compare l'indicazione che l'onere della prova della mancata autorizzazione grava sul cliente.
- **Fail se** l'onere è collocato sulla Banca nonostante la deroga, oppure la questione non è trattata.
- **Indifferente** il giudizio sulla convenienza della clausola per il cliente.
- *non passa al judge:* Fonte clausole 18.2 e 18.3 - Gravita media - judge si

### B.7 [issue: I-03] [tipo: qualificazione]

- **Verifica** il deliverable qualifica come eccedente il contenuto della deroga l'affermazione della Banca secondo cui nessun obbligo di rimborso le grava.
- **Pass se** compare, riferita al punto 1 della lettera del 20 marzo 2031, una fra: «eccede il contenuto della deroga», «non è sostenuta dalla clausola 18.2», «va oltre ciò che le parti hanno derogato».
- **Fail se** l'affermazione della Banca è presentata come fondata, oppure non è valutata.
- **Indifferente** il tono con cui la valutazione è espressa.
- *non passa al judge:* Fonte punto 1 della lettera del 20 marzo 2031 - Gravita alta - judge si

### B.8 [issue: I-04] [tipo: valore]

- **Verifica** il deliverable indica come operazioni eccedenti la soglia di doppia firma quella di euro 39.000,00 e quella di euro 29.000,00.
- **Pass se** compaiono «euro 39.000,00» ed «euro 29.000,00» come le operazioni oltre soglia. compaiono «39.000,00» e «29.000,00» come le operazioni oltre soglia.
- **Fail se** sono indicate operazioni diverse, oppure le operazioni oltre soglia non sono identificate.
- **Indifferente** l'ordine in cui le due operazioni sono elencate.
- *non passa al judge:* Fonte clausola 5.3; estratto conto - Gravita alta - judge no

### B.9 [issue: I-04] [tipo: presenza]

- **Verifica** il deliverable afferma che le due operazioni oltre soglia risultano disposte con una sola firma.
- **Pass se** compare l'indicazione che per quelle due operazioni la colonna del numero di firme riporta una firma sola.
- **Fail se** le due operazioni sono presentate come disposte con due firme, oppure il numero di firme non è rilevato.
- **Indifferente** il richiamo alla clausola 5.4.
- *non passa al judge:* Fonte colonna numero_firme dell'estratto conto - Gravita alta - judge si

### B.10 [issue: I-04] [tipo: qualificazione]

- **Verifica** il deliverable qualifica l'esecuzione delle due operazioni oltre soglia come difforme dal mandato.
- **Pass se** compare, riferita a quelle due operazioni, una fra: «difformita dal mandato», «violazione della clausola 5.3», «eseguita in difformita dai poteri di firma».
- **Fail se** l'esecuzione è presentata come conforme al mandato, oppure la qualificazione non compare.
- **Indifferente** il richiamo alla clausola 5.4.
- *non passa al judge:* Fonte clausole 5.3 e 5.4 - Gravita alta - judge si

### B.11 [issue: I-05] [tipo: valore]

- **Verifica** il deliverable indica in quattro il numero delle operazioni disconosciute di importo inferiore alla soglia di doppia firma.
- **Pass se** compare l'indicazione di «quattro» operazioni sotto soglia. compare l'indicazione di «4» operazioni sotto soglia.
- **Fail se** è indicato un numero diverso, oppure la distinzione fra operazioni sopra e sotto soglia non è fatta.
- **Indifferente** l'ordine in cui le quattro operazioni sono elencate.
- *non passa al judge:* Fonte clausola 5.2; estratto conto - Gravita alta - judge no

### B.12 [issue: I-05] [tipo: assenza]

- **Verifica** il deliverable non afferma che l'esecuzione a firma singola delle operazioni di euro 24.500,00, 18.000,00, 22.000,00 e 16.000,00 viola il mandato.
- **Fail se** l'esecuzione a firma singola di una di quelle quattro operazioni è presentata come violazione del mandato o della soglia di doppia firma.
- **Indifferente** il rilievo che quelle operazioni presentano un vizio diverso.
- *non passa al judge:* Fonte clausola 5.2 - Gravita alta - judge si

### B.13 [issue: I-06] [tipo: valore]

- **Verifica** il deliverable indica in quattro il numero delle operazioni disconosciute eseguite senza autenticazione forte.
- **Pass se** compare l'indicazione di «quattro» operazioni senza autenticazione forte. compare l'indicazione di «4» operazioni senza autenticazione forte.
- **Fail se** è indicato un numero diverso, oppure la questione dell'autenticazione forte non è trattata.
- **Indifferente** l'ordine in cui le operazioni sono elencate.
- *non passa al judge:* Fonte colonna autenticazione_forte dell'estratto conto - Gravita alta - judge no

### B.14 [issue: I-06] [tipo: attribuzione]

- **Verifica** il deliverable collega le quattro operazioni senza autenticazione forte all'utenza vertegno.a e al dispositivo non censito.
- **Pass se** il collegamento è fatto a una fra: «utenza vertegno.a», «DEV-019», «dispositivo non censito».
- **Fail se** le quattro operazioni sono attribuite a un'altra utenza o a un dispositivo censito, oppure il collegamento non è fatto.
- **Indifferente** l'indicazione dell'ora delle disposizioni.
- *non passa al judge:* Fonte colonne utenza_disponente e dispositivo dell'estratto conto - Gravita alta - judge si

### B.15 [issue: I-07] [tipo: presenza]

- **Verifica** il deliverable afferma che la registrazione dell'uso dello strumento di pagamento non dimostra da sé che l'operazione sia stata autorizzata.
- **Pass se** compare, riferita al punto 2 della lettera del 20 marzo 2031, una fra: «la registrazione non prova l'autorizzazione», «la regolarita formale non dimostra l'autorizzazione», «la contabilizzazione non equivale ad autorizzazione».
- **Fail se** la tesi del punto 2 della lettera è presentata come fondata, oppure la questione non è trattata.
- **Indifferente** il richiamo alla giurisprudenza in materia.
- *non passa al judge:* Fonte punto 2 della lettera del 20 marzo 2031 - Gravita alta - judge si

### B.16 [issue: I-08] [tipo: presenza]

- **Verifica** il deliverable rileva che l'avviso via SMS previsto dal contratto non è stato ricevuto per le operazioni disconosciute.
- **Pass se** compare l'indicazione che l'avviso previsto dalla clausola 8.1 non è stato ricevuto.
- **Fail se** il rilievo non compare, oppure l'avviso è dato per ricevuto.
- **Indifferente** l'indicazione della soglia di importo che attiva l'avviso.
- *non passa al judge:* Fonte clausola 8.1, lettera a); PEC del 12 marzo 2031 - Gravita alta - judge si

### B.17 [issue: I-08] [tipo: valore]

- **Verifica** il deliverable indica il 4 febbraio 2031 come data della comunicazione scritta di variazione del numero di telefono censito.
- **Pass se** compare «4 febbraio 2031» come data della comunicazione di variazione. compare «04/02/2031» come data della comunicazione di variazione.
- **Fail se** è indicata una data diversa, oppure la comunicazione di variazione non è collocata nel tempo.
- **Indifferente** l'indicazione del mezzo con cui la comunicazione è stata inviata.
- *non passa al judge:* Fonte PEC del 12 marzo 2031 - Gravita alta - judge no

### B.18 [issue: I-08] [tipo: assenza]

- **Verifica** il deliverable non afferma che il cliente ha omesso di comunicare la variazione del numero di telefono censito.
- **Fail se** compare l'affermazione che il cliente non aveva comunicato la variazione del numero.
- **Indifferente** il rilievo che la ricevuta di ritorno della raccomandata non è nel fascicolo.
- *non passa al judge:* Fonte clausola 7.3; PEC del 12 marzo 2031 - Gravita alta - judge si

### B.19 [issue: I-09] [tipo: presenza]

- **Verifica** il deliverable riporta come fatto provato dagli atti la comunicazione a terzi di identificativo, codice segreto e codice temporaneo del 27 febbraio 2031.
- **Pass se** compare l'indicazione della comunicazione delle credenziali a terzi del 27 febbraio 2031.
- **Fail se** il fatto non è riportato, oppure è presentato come non provato.
- **Indifferente** la descrizione tecnica delle modalità con cui l'inganno è avvenuto.
- *non passa al judge:* Fonte PEC del 12 marzo 2031 - Gravita alta - judge si

### B.20 [issue: I-09] [tipo: presenza]

- **Verifica** il deliverable riporta come fatto provato dagli atti che la Banca non è stata informata dell'episodio del 27 febbraio 2031.
- **Pass se** compare l'indicazione che l'episodio non è stato comunicato alla Banca.
- **Fail se** il fatto non è riportato, oppure la Banca è presentata come informata.
- **Indifferente** l'indicazione del soggetto interno che era stato informato.
- *non passa al judge:* Fonte PEC del 12 marzo 2031; clausola 7.2 - Gravita alta - judge si

### B.21 [issue: I-09] [tipo: qualificazione]

- **Verifica** il deliverable qualifica la misura dell'incidenza della condotta del cliente sul danno come non determinabile con i dati del fascicolo.
- **Pass se** compare, riferita alla misura dell'incidenza, una fra: «non determinabile con i dati disponibili», «richiede la documentazione tecnica non trasmessa», «non quantificabile sugli atti».
- **Fail se** la misura è quantificata, oppure la condotta è presentata come irrilevante, oppure la questione non è trattata.
- **Indifferente** il richiamo alla norma sul concorso del creditore.
- *non passa al judge:* Fonte PEC del 12 marzo 2031; punto 5 della lettera del 20 marzo 2031 - Gravita alta - judge si

### B.22 [issue: I-09] [tipo: assenza]

- **Verifica** il deliverable non afferma che la condotta del cliente esclude ogni pretesa nei confronti della Banca.
- **Fail se** compare l'affermazione che la condotta del 27 febbraio 2031 esclude, preclude o estingue ogni pretesa del cliente.
- **Indifferente** l'indicazione che la condotta riduce la pretesa in misura da determinare.
- *non passa al judge:* Fonte punto 3 della lettera del 20 marzo 2031 - Gravita alta - judge si

### B.23 [issue: I-10] [tipo: presenza]

- **Verifica** il deliverable rileva che la Banca non ha trasmesso la documentazione tecnica sull'autenticazione delle singole operazioni.
- **Pass se** compare l'indicazione che la documentazione tecnica non è stata trasmessa.
- **Fail se** il rilievo non compare, oppure la documentazione è data per acquisita.
- **Indifferente** la valutazione della motivazione addotta dalla Banca.
- *non passa al judge:* Fonte punto 5 della lettera del 20 marzo 2031 - Gravita media - judge si

### B.24 [issue: I-11] [tipo: presenza]

- **Verifica** il deliverable afferma che il fascicolo non prova chi abbia materialmente impartito le disposizioni contestate.
- **Pass se** compare, riferita all'autore materiale delle disposizioni, una fra: «non risulta dagli atti», «non provato dal fascicolo», «non determinabile con i documenti disponibili».
- **Fail se** l'autore materiale è indicato come accertato, oppure la lacuna non è dichiarata.
- **Indifferente** le ipotesi sull'autore, se dichiarate come ipotesi.
- *non passa al judge:* Fonte assenza di log di sessione nel fascicolo - Gravita alta - judge si

### B.25 [issue: I-11] [tipo: presenza]

- **Verifica** il deliverable indica quali elementi occorrono per accertare l'autore materiale delle disposizioni.
- **Pass se** compare l'indicazione di almeno un elemento fra log di sessione, indirizzi di collegamento, identificativo del dispositivo e tracciato dei codici temporanei.
- **Fail se** la lacuna è dichiarata senza indicare che cosa serve per colmarla.
- **Indifferente** il numero di elementi elencati.
- *non passa al judge:* Fonte public/01_task.md, richiesta sui dati mancanti - Gravita alta - judge si

### B.26 [issue: I-12] [tipo: valore]

- **Verifica** il deliverable indica in euro 148.500,00 il totale delle operazioni disconosciute.
- **Pass se** compare «euro 148.500,00» come totale delle operazioni disconosciute. compare «148.500,00» come totale delle operazioni disconosciute.
- **Fail se** è indicato un totale diverso, oppure il totale non compare.
- **Indifferente** l'indicazione del saldo progressivo.
- *non passa al judge:* Fonte PEC del 12 marzo 2031; estratto conto - Gravita media - judge no


## C. Date, valori calcolati e chiusura

### C.1 [issue: N-01] [tipo: assenza]

- **Verifica** il deliverable non presenta come profilo di rischio la tempestivita della comunicazione del disconoscimento del 12 marzo 2031.
- **Fail se** il ritardo o la tardività del disconoscimento compare fra i profili di rischio o fra gli argomenti opponibili al cliente.
- **Indifferente** l'indicazione della data in cui il cliente ha avuto conoscenza delle operazioni.
- *non passa al judge:* Fonte challenge map, N-01 - Gravita alta - judge si

### C.2 [issue: N-01] [tipo: presenza]

- **Verifica** il deliverable afferma che il rilievo della Banca sulla tempestività della comunicazione non è fondato.
- **Pass se** compare, riferita al punto 4 della lettera del 20 marzo 2031, una fra: «il rilievo non è fondato», «la comunicazione è nei termini», «il termine è rispettato».
- **Fail se** il rilievo della Banca è presentato come fondato, oppure non è valutato.
- **Indifferente** l'indicazione del numero di giorni intercorsi.
- *non passa al judge:* Fonte punto 4 della lettera del 20 marzo 2031 - Gravita media - judge si

### C.3 [issue: N-02] [tipo: assenza]

- **Verifica** il deliverable non include il bonifico stipendi di euro 96.420,00 del 3 marzo 2031 fra le operazioni contestate.
- **Fail se** il bonifico stipendi compare fra le operazioni disconosciute o fra quelle disposte in difformità dal mandato.
- **Indifferente** la menzione del bonifico stipendi come termine di confronto sull'autenticazione.
- *non passa al judge:* Fonte challenge map, N-02 - Gravita media - judge si

### C.4 [issue: N-03] [tipo: assenza]

- **Verifica** il deliverable non segnala come irregolarità il termine di risposta al reclamo osservato dalla Banca.
- **Fail se** il tempo impiegato dalla Banca per rispondere al reclamo compare fra le irregolarità o fra i profili di rischio.
- **Indifferente** la menzione della data della risposta nella cronologia.
- *non passa al judge:* Fonte challenge map, N-03 - Gravita media - judge si

### C.5 [issue: X-01] [tipo: assenza]

- **Verifica** simmetria del controllo: il deliverable non tratta come provata l'assenza di autorizzazione mentre tratta come non provato l'autore materiale delle disposizioni.
- **Fail se** l'assenza di autorizzazione è data per provata e nello stesso deliverable l'autore materiale è dichiarato non accertabile.
- **Indifferente** l'ordine in cui i due punti sono trattati.
- *non passa al judge:* Fonte estratto conto; PEC del 12 marzo 2031 - Gravita alta - judge si

### C.6 [issue: X-02] [tipo: assenza]

- **Verifica** divieto di presunzione dell'esito: il deliverable non afferma che la Banca sarà tenuta a rimborsare l'importo delle operazioni contestate.
- **Fail se** compare l'affermazione che il rimborso è dovuto o che la Banca dovrà rimborsare l'importo.
- **Indifferente** l'indicazione delle condizioni al verificarsi delle quali il rimborso sarebbe dovuto.
- *non passa al judge:* Fonte clausole 18.2 e 18.4 - Gravita alta - judge si

### C.7 [issue: X-03] [tipo: assenza]

- **Verifica** sovra-segnalazione: il deliverable non presenta come profilo di rischio la destinazione estera dei conti dei due beneficiari.
- **Fail se** la destinazione estera dei conti compare fra i profili di rischio autonomi o fra le irregolarità imputabili alla Banca.
- **Indifferente** la menzione della destinazione estera nella descrizione delle operazioni.
- *non passa al judge:* Fonte estratto conto - Gravita media - judge si
