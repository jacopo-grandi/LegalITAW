# WF2-058 - Criteri atomizzati

Forma a campi. Ciò che sta sotto la riga non passa al judge.


## A. Forma dell'output (interamente verifica meccanica)

### A.1 [tipo: valore]

- **Verifica** il deliverable è prodotto come file `procedure_timeline.md`.
- **Pass se** il file consegnato ha nome `procedure_timeline.md`.
- **Fail se** il file ha un altro nome o un'altra estensione.
- **Indifferente** la presenza di intestazioni aggiuntive.
- *non passa al judge:* Fonte task_spec.json, campo deliverable - Gravita media - judge no

### A.2 [tipo: struttura]

- **Verifica** il deliverable contiene, nell'ordine, le sei sezioni obbligatorie del template.
- **Pass se** le sei intestazioni di sezione compaiono nell'ordine indicato dal template.
- **Fail se** manca almeno una sezione o l'ordine è diverso.
- **Indifferente** la numerazione delle sottosezioni.
- *non passa al judge:* Fonte public/response_template.md - Gravita media - judge no

### A.3 [tipo: valore]

- **Verifica** il deliverable non supera il limite di 2400 parole.
- **Pass se** il conteggio delle parole del corpo del deliverable non supera 2400.
- **Fail se** il corpo del deliverable supera 2400 parole.
- **Indifferente** la lunghezza delle singole sezioni.
- *non passa al judge:* Fonte task_spec.json, campo limite_parole - Gravita media - judge no

### A.4 [tipo: struttura]

- **Verifica** la sezione delle scadenze riporta per ciascuna voce data, adempimento, soggetto onerato e conseguenza dell'inosservanza.
- **Pass se** ciascuna voce della sezione delle scadenze porta i quattro elementi.
- **Fail se** almeno una voce omette uno dei quattro elementi.
- **Indifferente** l'ordine delle colonne.
- *non passa al judge:* Fonte public/response_template.md - Gravita media - judge no

### A.5 [tipo: struttura]

- **Verifica** ogni data indicata porta il riferimento al documento del fascicolo da cui è ricavata.
- **Pass se** accanto a ciascuna data compare il rinvio a uno dei cinque allegati.
- **Fail se** almeno una data non porta alcun rinvio a un allegato.
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
- **Indifferente** il richiamo ai protocolli e ai codici pratica del fascicolo.
- *non passa al judge:* Fonte private/fonti_chiuse.json - Gravita media - judge no


## B. Merito

Il fascicolo è esaminato al 15 aprile 2031: l'istanza e l'accettazione sono pubblicate dall'8 aprile, il termine per il ricorso è scaduto il 9 aprile, quello per l'iscrizione del numero di ruolo scade il 28 aprile e nessun provvedimento del tribunale risulta dagli atti. Il prompt chiede da quando opera la protezione, le scadenze con soggetto onerato e conseguenza dell'inosservanza, il calcolo seguito, la fonte di ciascuna data, il perimetro degli effetti, la valutazione della lettera della banca, i difetti del materiale depositato, la distinzione fra profili che incidono e profili che non incidono, e la valutazione della lettura del consulente.

### B.1 [issue: I-01] [tipo: valore]

- **Verifica** il deliverable indica l'8 aprile 2031 come giorno da cui le misure protettive producono effetto.
- **Pass se** compare «8 aprile 2031» come giorno di decorrenza degli effetti delle misure. compare «08/04/2031» come giorno di decorrenza degli effetti delle misure.
- **Fail se** è indicato un altro giorno, oppure la decorrenza degli effetti non è indicata.
- **Indifferente** l'indicazione dell'ora di estrazione della visura.
- *non passa al judge:* Fonte iscrizione prot. 2031/0455; date_verificate.md - Gravita alta - judge no

### B.2 [issue: I-01] [tipo: attribuzione]

- **Verifica** il deliverable riconduce la decorrenza degli effetti alla pubblicazione dell'istanza nel Registro delle Imprese.
- **Pass se** la decorrenza è ricondotta a una fra: «pubblicazione nel Registro delle Imprese», «iscrizione dell'istanza di misure protettive», «pubblicita legale dell'istanza».
- **Fail se** la decorrenza è ricondotta al decreto di conferma, alla nomina dell'esperto o alla trasmissione dell'istanza, oppure l'atto di decorrenza non è indicato.
- **Indifferente** il richiamo al numero di protocollo dell'iscrizione.
- *non passa al judge:* Fonte visura dell'8 aprile 2031 - Gravita alta - judge si

### B.3 [issue: I-01] [tipo: assenza]

- **Verifica** il deliverable non afferma che le misure protettive producono effetto dal decreto di conferma del tribunale.
- **Fail se** compare l'affermazione che le misure operano dalla conferma o dal provvedimento del tribunale.
- **Indifferente** l'indicazione che il decreto conferma, modifica o revoca misure già operanti.
- *non passa al judge:* Fonte disciplina delle misure protettive - Gravita alta - judge si

### B.4 [issue: I-01] [tipo: assenza]

- **Verifica** il deliverable non indica il 27 marzo 2031 come giorno da cui le misure producono effetto.
- **Fail se** il 27 marzo 2031 è indicato come giorno di decorrenza degli effetti delle misure.
- **Indifferente** la menzione del 27 marzo 2031 come data di trasmissione dell'istanza.
- *non passa al judge:* Fonte visura dell'8 aprile 2031 - Gravita media - judge si

### B.5 [issue: I-02] [tipo: valore]

- **Verifica** il deliverable indica il 9 aprile 2031 come termine per il deposito del ricorso al tribunale.
- **Pass se** compare «9 aprile 2031» come termine per il ricorso. compare «09/04/2031» come termine per il ricorso.
- **Fail se** è indicata una data diversa, oppure il termine per il ricorso non è indicato.
- **Indifferente** l'indicazione dell'orario di deposito.
- *non passa al judge:* Fonte computo dalla pubblicazione; date_verificate.md - Gravita alta - judge no

### B.6 [issue: I-02] [tipo: presenza]

- **Verifica** il deliverable afferma che l'omissione del ricorso nel termine fa cessare gli effetti delle misure protettive.
- **Pass se** compare l'indicazione che, in mancanza del ricorso nel termine, le misure cessano di produrre effetto.
- **Fail se** la conseguenza dell'omissione non è indicata, oppure è indicata una conseguenza diversa.
- **Indifferente** il richiamo all'articolo che disciplina il procedimento.
- *non passa al judge:* Fonte disciplina del procedimento sulle misure protettive - Gravita alta - judge si

### B.7 [issue: I-03] [tipo: valore]

- **Verifica** il deliverable indica il 28 aprile 2031 come termine per l'iscrizione del numero di ruolo nel Registro delle Imprese.
- **Pass se** compare «28 aprile 2031» come termine per l'iscrizione del numero di ruolo. compare «28/04/2031» come termine per l'iscrizione del numero di ruolo.
- **Fail se** è indicata una data diversa, oppure il termine non è indicato.
- **Indifferente** l'indicazione del soggetto che cura materialmente l'iscrizione.
- *non passa al judge:* Fonte computo dalla pubblicazione; date_verificate.md - Gravita alta - judge no

### B.8 [issue: I-03] [tipo: qualificazione]

- **Verifica** il deliverable qualifica l'inosservanza del termine di venti giorni come causa di inefficacia delle misure protettive.
- **Pass se** compare, riferita a quell'inosservanza, una fra: «inefficacia delle misure», «le misure divengono inefficaci», «perdita di efficacia».
- **Fail se** l'inosservanza è presentata come priva di conseguenze, oppure la conseguenza indicata è diversa dall'inefficacia, oppure la qualificazione non compare.
- **Indifferente** il richiamo all'articolo che disciplina il procedimento.
- *non passa al judge:* Fonte disciplina del procedimento sulle misure protettive - Gravita alta - judge si

### B.9 [issue: I-04] [tipo: valore]

- **Verifica** il deliverable indica in dieci giorni dal deposito del ricorso il termine entro cui il tribunale fissa l'udienza.
- **Pass se** compare «dieci giorni» come termine per la fissazione dell'udienza. compare «10 giorni» come termine per la fissazione dell'udienza.
- **Fail se** è indicato un termine diverso, oppure il termine non è indicato.
- **Indifferente** l'indicazione della modalità di svolgimento dell'udienza.
- *non passa al judge:* Fonte disciplina del procedimento sulle misure protettive - Gravita alta - judge no

### B.10 [issue: I-05] [tipo: valore]

- **Verifica** il deliverable indica in trenta giorni il limite minimo e in centoventi giorni il limite massimo della durata che il tribunale può assegnare alle misure.
- **Pass se** compaiono «trenta giorni» e «centoventi giorni» come limiti della durata iniziale. compaiono «30 giorni» e «120 giorni» come limiti della durata iniziale.
- **Fail se** sono indicati limiti diversi, oppure i limiti della durata iniziale non sono indicati.
- **Indifferente** l'indicazione della durata che il tribunale potrebbe scegliere nel caso concreto.
- *non passa al judge:* Fonte disciplina delle misure protettive - Gravita alta - judge no

### B.11 [issue: I-06] [tipo: valore]

- **Verifica** il deliverable indica in duecentoquaranta giorni la durata massima complessiva delle misure comprese le proroghe.
- **Pass se** compare «duecentoquaranta giorni» come durata massima complessiva. compare «240 giorni» come durata massima complessiva.
- **Fail se** è indicata una durata massima diversa, oppure il limite complessivo non è indicato.
- **Indifferente** l'indicazione del numero di proroghe.
- *non passa al judge:* Fonte disciplina delle misure protettive - Gravita alta - judge no

### B.12 [issue: I-06] [tipo: assenza]

- **Verifica** il deliverable non afferma che le misure protettive possono durare per l'intera durata della composizione negoziata.
- **Fail se** compare l'affermazione che le misure durano quanto la composizione negoziata o che seguono la durata delle trattative.
- **Indifferente** l'indicazione che la composizione negoziata ha una propria durata distinta.
- *non passa al judge:* Fonte disciplina delle misure protettive - Gravita media - judge si

### B.13 [issue: I-07] [tipo: valore]

- **Verifica** il deliverable indica il 31 gennaio 2031 come data di aggiornamento della situazione patrimoniale depositata.
- **Pass se** compare «31 gennaio 2031» come data della situazione patrimoniale. compare «31/01/2031» come data della situazione patrimoniale.
- **Fail se** è indicata una data diversa, oppure la data del documento non è rilevata.
- **Indifferente** l'indicazione delle voci contenute nel documento.
- *non passa al judge:* Fonte punto 4, numero 3, dell'istanza; date_verificate.md - Gravita alta - judge no

### B.14 [issue: I-07] [tipo: presenza]

- **Verifica** il deliverable rileva che alla data di pubblicazione la situazione patrimoniale depositata ha un'anzianità superiore al limite di sessanta giorni.
- **Pass se** compare l'indicazione che il documento supera il limite di anzianità di sessanta giorni alla data rilevante.
- **Fail se** il rilievo non compare, oppure il documento è presentato come conforme al requisito di aggiornamento.
- **Indifferente** il numero esatto di giorni di anzianità indicato.
- *non passa al judge:* Fonte punto 4 dell'istanza; visura dell'8 aprile 2031 - Gravita alta - judge si

### B.15 [issue: I-07] [tipo: presenza]

- **Verifica** il deliverable indica come azione l'aggiornamento e il deposito di una nuova situazione patrimoniale.
- **Pass se** compare l'indicazione di aggiornare e depositare la situazione patrimoniale.
- **Fail se** l'azione non compare.
- **Indifferente** la data alla quale la nuova situazione dovrebbe essere aggiornata.
- *non passa al judge:* Fonte punto 4 dell'istanza - Gravita media - judge si

### B.16 [issue: I-08] [tipo: presenza]

- **Verifica** il deliverable afferma che i crediti dei lavoratori sono esclusi dalle misure protettive.
- **Pass se** compare l'indicazione che i crediti dei lavoratori restano fuori dall'ambito delle misure protettive.
- **Fail se** i crediti dei lavoratori sono presentati come coperti dalle misure, oppure l'esclusione non è affermata.
- **Indifferente** il richiamo all'articolo che dispone l'esclusione.
- *non passa al judge:* Fonte disciplina delle misure protettive - Gravita alta - judge si

### B.17 [issue: I-08] [tipo: valore]

- **Verifica** il deliverable indica in euro 410.000,00 l'ammontare dei crediti dei lavoratori esclusi dalle misure.
- **Pass se** compare «euro 410.000,00» come ammontare dei crediti dei lavoratori. compare «410.000,00» come ammontare dei crediti dei lavoratori.
- **Fail se** è indicato un ammontare diverso, oppure l'ammontare non è isolato.
- **Indifferente** l'indicazione del fondo per il trattamento di fine rapporto, che è voce distinta.
- *non passa al judge:* Fonte situazione patrimoniale; elenco delle categorie di creditori nell'istanza - Gravita media - judge no

### B.18 [issue: I-09] [tipo: qualificazione]

- **Verifica** il deliverable qualifica la sospensione delle linee comunicata dalla banca come consentita nella finestra che va dalla pubblicazione alla conferma delle misure.
- **Pass se** compare, riferita alla sospensione, una fra: «consentita fino alla conferma», «ammessa nella fase anteriore alla conferma», «legittima solo fino al provvedimento di conferma».
- **Fail se** la sospensione è presentata come in ogni caso illegittima, oppure come consentita senza limite temporale, oppure la qualificazione non compare.
- **Indifferente** il richiamo alla disciplina prudenziale.
- *non passa al judge:* Fonte punto 1 della lettera del 10 aprile 2031 - Gravita alta - judge si

### B.19 [issue: I-09] [tipo: presenza]

- **Verifica** il deliverable indica come azione la contestazione della prosecuzione della sospensione dopo la conferma delle misure.
- **Pass se** compare l'indicazione di contestare la sospensione se prosegue dopo la conferma.
- **Fail se** l'azione non compare.
- **Indifferente** la forma proposta per la contestazione.
- *non passa al judge:* Fonte punto 1 della lettera del 10 aprile 2031 - Gravita media - judge si

### B.20 [issue: I-10] [tipo: qualificazione]

- **Verifica** il deliverable qualifica come vietata la revoca degli affidamenti annunciata dalla banca, in quanto motivata con il mancato pagamento di debiti anteriori.
- **Pass se** compare, riferita a quella revoca, una fra: «ricade nel divieto», «non è consentita perché fondata sui soli debiti pregressi», «vietata in quanto motivata dal mancato pagamento anteriore».
- **Fail se** la revoca è presentata come consentita, oppure la qualificazione non compare.
- **Indifferente** il giudizio sulla motivazione alternativa addotta al punto 3 della lettera.
- *non passa al judge:* Fonte punto 2 della lettera del 10 aprile 2031 - Gravita alta - judge si

### B.21 [issue: I-10] [tipo: attribuzione]

- **Verifica** il deliverable fonda quella qualificazione sulle rate scadute il 31 gennaio e il 28 febbraio 2031 nominate dalla banca.
- **Pass se** la qualificazione è ricondotta a una fra: «rate scadute il 31 gennaio e il 28 febbraio 2031», «rate anteriori alla pubblicazione», «punto 2 della lettera».
- **Fail se** la qualificazione è affermata senza indicare la motivazione addotta dalla banca.
- **Indifferente** l'indicazione dell'importo delle rate.
- *non passa al judge:* Fonte punto 2 della lettera del 10 aprile 2031 - Gravita alta - judge si

### B.22 [issue: I-11] [tipo: presenza]

- **Verifica** il deliverable afferma che il decreto ingiuntivo notificato il 10 marzo 2031 resta valido.
- **Pass se** compare, riferita al decreto ingiuntivo, una fra: «resta valido», «conserva efficacia come titolo», «non è travolto dalle misure».
- **Fail se** il decreto è presentato come inefficace o nullo, oppure la sua sorte non è trattata.
- **Indifferente** l'indicazione dello stato del termine per l'opposizione.
- *non passa al judge:* Fonte punto 6 dell'istanza - Gravita alta - judge si

### B.23 [issue: I-11] [tipo: qualificazione]

- **Verifica** il deliverable qualifica l'effetto delle misure sul decreto come limitato all'inizio o alla prosecuzione delle azioni esecutive e cautelari.
- **Pass se** compare l'indicazione che le misure impediscono di iniziare o proseguire azioni esecutive e cautelari sul patrimonio.
- **Fail se** alle misure è attribuito l'effetto di annullare il titolo, oppure l'effetto non è precisato.
- **Indifferente** il richiamo all'articolo che disciplina gli effetti.
- *non passa al judge:* Fonte disciplina delle misure protettive - Gravita alta - judge si

### B.24 [issue: I-11] [tipo: assenza]

- **Verifica** il deliverable non afferma che il decreto ingiuntivo è divenuto inefficace per effetto della pubblicazione dell'istanza.
- **Fail se** compare l'affermazione che il decreto ingiuntivo è inefficace, nullo o travolto per effetto della pubblicazione.
- **Indifferente** l'indicazione che il credito ingiunto resta soggetto alle trattative.
- *non passa al judge:* Fonte punto 6 dell'istanza - Gravita alta - judge si

### B.25 [issue: I-12] [tipo: qualificazione]

- **Verifica** il deliverable qualifica l'inibitoria del ritiro degli impianti come misura cautelare specifica distinta dalle misure protettive.
- **Pass se** compare, riferita all'inibitoria, una fra: «misura cautelare specifica», «provvedimento cautelare distinto», «non rientra nelle misure protettive».
- **Fail se** l'inibitoria è presentata come effetto automatico della pubblicazione, oppure la qualificazione non compare.
- **Indifferente** l'indicazione del valore dei canoni maturati.
- *non passa al judge:* Fonte punto 5 dell'istanza - Gravita media - judge si

### B.26 [issue: I-12] [tipo: presenza]

- **Verifica** il deliverable indica come azione la motivazione specifica dell'inibitoria nel ricorso al tribunale.
- **Pass se** compare l'indicazione di motivare l'inibitoria nel ricorso, distintamente dalla richiesta di conferma delle misure.
- **Fail se** l'azione non compare.
- **Indifferente** il contenuto proposto per la motivazione.
- *non passa al judge:* Fonte punto 5 dell'istanza - Gravita media - judge si

### B.27 [issue: I-13] [tipo: presenza]

- **Verifica** il deliverable afferma che al 15 aprile 2031 il decreto del tribunale non risulta dagli atti.
- **Pass se** compare, riferita al decreto del tribunale, una fra: «non risulta dagli atti», «non è nel fascicolo», «la conferma non risulta intervenuta».
- **Fail se** la conferma è data per intervenuta o per negata, oppure lo stato del procedimento non è affermato.
- **Indifferente** l'indicazione della data entro cui il decreto dovrebbe intervenire.
- *non passa al judge:* Fonte visura dell'8 aprile 2031; composizione del fascicolo - Gravita alta - judge si

### B.28 [issue: I-13] [tipo: presenza]

- **Verifica** il deliverable afferma che l'iscrizione del numero di ruolo non risulta dalla visura.
- **Pass se** compare l'indicazione che nella visura non compare l'iscrizione del numero di ruolo.
- **Fail se** l'iscrizione è data per avvenuta, oppure la verifica non compare.
- **Indifferente** il rilievo che la visura è estratta l'8 aprile 2031.
- *non passa al judge:* Fonte visura dell'8 aprile 2031 - Gravita alta - judge si

### B.29 [issue: I-13] [tipo: presenza]

- **Verifica** il deliverable indica quali documenti occorrono per accertare lo stato del procedimento davanti al tribunale.
- **Pass se** compare l'indicazione di almeno un documento fra ricevuta di deposito del ricorso, decreto di fissazione dell'udienza e visura aggiornata.
- **Fail se** la lacuna è dichiarata senza indicare che cosa serve per colmarla.
- **Indifferente** il numero di documenti elencati.
- *non passa al judge:* Fonte public/01_task.md, richiesta sui dati mancanti - Gravita media - judge si

### B.30 [issue: I-14] [tipo: presenza]

- **Verifica** il deliverable afferma che il tribunale può revocare o abbreviare le misure in ogni momento.
- **Pass se** compare l'indicazione che la revoca o l'abbreviazione delle misure è possibile in ogni momento del procedimento.
- **Fail se** le misure confermate sono presentate come intangibili fino alla scadenza, oppure la questione non è trattata.
- **Indifferente** l'indicazione dei presupposti della revoca.
- *non passa al judge:* Fonte disciplina del procedimento sulle misure protettive - Gravita media - judge si


## C. Date, valori calcolati e chiusura

### C.1 [issue: I-02] [tipo: assenza]

- **Verifica** il deliverable non indica un termine per il ricorso al tribunale decorrente dalla nomina dell'esperto del 2 aprile 2031.
- **Fail se** il termine per il ricorso è fatto decorrere dalla nomina dell'esperto.
- **Indifferente** la menzione del 2 aprile 2031 come data della nomina.
- *non passa al judge:* Fonte computo dalla pubblicazione - Gravita alta - judge si

### C.2 [issue: I-03] [tipo: assenza]

- **Verifica** il deliverable non presenta il termine di venti giorni come decorrente dalla trasmissione dell'istanza del 27 marzo 2031.
- **Fail se** il termine di venti giorni è fatto decorrere dal 27 marzo 2031.
- **Indifferente** la menzione del 27 marzo 2031 nella cronologia.
- *non passa al judge:* Fonte computo dalla pubblicazione - Gravita media - judge si

### C.3 [issue: N-01] [tipo: assenza]

- **Verifica** il deliverable non segnala come criticità l'indipendenza dell'esperto nominato.
- **Fail se** l'indipendenza dell'esperto compare fra i profili di rischio o fra le criticità del procedimento.
- **Indifferente** la menzione della dichiarazione di indipendenza nella cronologia.
- *non passa al judge:* Fonte challenge map, N-01 - Gravita media - judge si

### C.4 [issue: N-02] [tipo: assenza]

- **Verifica** il deliverable non segnala come omissione la mancata richiesta di limitazione della pubblicita dell'istanza.
- **Fail se** la mancata richiesta di limitazione della pubblicita compare fra le omissioni o fra i profili di rischio.
- **Indifferente** la menzione della pubblicita legale come condizione di operatività delle misure.
- *non passa al judge:* Fonte challenge map, N-02 - Gravita media - judge si

### C.5 [issue: N-03] [tipo: assenza]

- **Verifica** il deliverable non segnala come profilo di rischio la disponibilità della banca alla partecipazione agli incontri convocati dall'esperto.
- **Fail se** la disponibilità della banca a partecipare agli incontri compare fra i profili di rischio.
- **Indifferente** la menzione della disponibilità nella descrizione della posizione della banca.
- *non passa al judge:* Fonte challenge map, N-03 - Gravita media - judge si

### C.6 [issue: N-04] [tipo: assenza]

- **Verifica** il deliverable non afferma che la perdita del periodo di gennaio 2031 preclude l'accesso alla composizione negoziata.
- **Fail se** la perdita del periodo è presentata come fatto che preclude l'accesso alla composizione negoziata o che ne impone la chiusura.
- **Indifferente** la menzione della perdita del periodo fra i dati della situazione patrimoniale.
- *non passa al judge:* Fonte challenge map, N-04 - Gravita media - judge si

### C.7 [issue: X-01] [tipo: assenza]

- **Verifica** simmetria del controllo: il deliverable non tratta come provata la conferma delle misure mentre tratta come non provata l'iscrizione del numero di ruolo.
- **Fail se** la conferma delle misure è data per intervenuta e nello stesso deliverable l'iscrizione del numero di ruolo è dichiarata non risultante.
- **Indifferente** l'ordine in cui i due punti sono trattati.
- *non passa al judge:* Fonte visura dell'8 aprile 2031 - Gravita media - judge si

### C.8 [issue: X-02] [tipo: assenza]

- **Verifica** divieto di presunzione dell'esito: il deliverable non afferma che il tribunale confermerà le misure protettive.
- **Fail se** compare l'affermazione che il tribunale confermerà le misure o che la conferma è certa.
- **Indifferente** l'indicazione delle condizioni al verificarsi delle quali la conferma sarebbe probabile.
- *non passa al judge:* Fonte disciplina del procedimento sulle misure protettive - Gravita alta - judge si

### C.9 [issue: X-03] [tipo: assenza]

- **Verifica** sovra-segnalazione: il deliverable non presenta come profilo di rischio il ricorso alla piattaforma telematica per la trasmissione dell'istanza.
- **Fail se** la trasmissione tramite piattaforma telematica compare fra i profili di rischio o fra le irregolarità.
- **Indifferente** la menzione della piattaforma nella descrizione dell'atto di apertura.
- *non passa al judge:* Fonte istanza; visura - Gravita media - judge si
