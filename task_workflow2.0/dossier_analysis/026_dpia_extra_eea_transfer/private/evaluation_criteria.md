# WF2-026 — Criteri di valutazione (rubrica in prosa, a livello di issue)

> Contenuto della colonna `Criteri di valutazione` del board. È la rubrica che l'avvocato legge, discute e firma: la sede della validazione professionale. La versione somministrata al judge è la rubrica atomizzata (`04_criteri_atomizzati.md`); il raccordo è l'identificativo dell'issue.

## A. Forma dell'output — interamente verifica meccanica, non passa al judge

- Un solo file di testo, con sintesi per la decisione, rilievi bloccanti, rilievi non bloccanti, sezione su ciò che non è un rilievo, date e numeri con il calcolo, sezione su ciò che manca dal pacchetto.
- I rilievi sono presentati in ordine di gravità.
- Ogni rilievo indica il documento da cui deriva, l'azione richiesta e chi la deve compiere.
- Ogni rilievo è qualificato come bloccante o non bloccante rispetto alla data di avvio prevista.
- Nessuna riscrittura di clausole, nessuna bozza di documento, nessuna valutazione d'impatto riscritta: produrle è deviazione di formato.
- Nessun riferimento normativo estraneo all'elenco chiuso delle fonti del reference pack.

## B. Merito

Il memo è reso nell'interesse di **Vernazzano Energia S.p.A.**, titolare del trattamento, alla data di riferimento del **6 marzo 2031**. Il trattamento non è ancora avviato e l'avvio in produzione è previsto per il 1° aprile 2031. Per ogni issue la fonte indica il documento.

**I-01. L'ambito della valutazione d'impatto è più stretto del trattamento** — la valutazione copre la prevenzione delle frodi e il rischio di credito; la specifica funzionale prevede una terza finalità, il punteggio di propensione all'abbandono per le campagne di retention, calcolato dallo stesso modello e con le stesse variabili, che la valutazione non menziona. La valutazione non copre il trattamento che sarà svolto (DPIA § 2.1; specifica funzionale § 1.3; messaggio del DPO; nota del responsabile di progetto § 1).

**I-02. La valutazione precede una modifica sostanziale e non è stata riesaminata** — la specifica funzionale 2.1 del 16 gennaio 2031, cinquantasei giorni dopo l'approvazione della valutazione, aggiunge una settima categoria di dati, gli indicatori di comportamento di pagamento acquisiti da una fonte esterna, ed estende la finestra di addestramento da trentasei a sessanta mesi; non risulta alcun riesame (specifica funzionale § 2 e cronologia delle versioni; DPIA § 2.3; art. 35, par. 11).

**I-03. Necessità e proporzionalità sono affermate e non valutate** — la sezione della valutazione è composta da affermazioni conclusive, non considera alternative meno intrusive e non collega le singole categorie di dati alle finalità; il contenuto minimo richiede una valutazione della necessità e proporzionalità dei trattamenti in relazione alle finalità (DPIA § 4; art. 35, par. 7, lett. b).

**I-04. Il riesame umano non assicura l'intervento umano che la valutazione gli attribuisce** — la procedura prevede quattro ore lavorative per punteggio, ma i dati del collaudo registrano 12.126 conferme su 12.450 punteggi, il 97,4%, con tempo medio di quarantuno secondi; l'operatore non ha accesso alla logica del punteggio e non può chiedere il ricalcolo. Su questa base la valutazione esclude che si tratti di una decisione basata unicamente sul trattamento automatizzato: l'esclusione non è sostenuta, e vanno predisposte le garanzie proprie di quel tipo di decisione (procedura di riesame §§ 3, 4 e 5; DPIA § 5; art. 22).

**I-05. Il rischio residuo dichiarato non è sostenuto dal registro** — il registro censisce sei rischi, di cui tre di livello alto, tutti con misura non attuata e data obiettivo successiva al 1° aprile 2031, e calcola come livello residuo atteso più elevato «alto»; la valutazione dichiara un rischio residuo complessivo «medio» (registro dei rischi, righe R2, R4 e R6 e riepilogo; DPIA § 7).

**I-06. La consultazione preventiva non è affrontata** — il titolare consulta l'autorità di controllo prima di procedere qualora la valutazione indichi che il trattamento presenterebbe un rischio elevato in assenza di misure di attenuazione; la valutazione non affronta la questione. La sequenza corretta è correggere la valutazione e poi, se il rischio residuo resta elevato, consultare l'autorità prima dell'avvio (DPIA § 7; registro dei rischi; art. 36, par. 1).

**I-07. Il modulo di clausole adottato non copre una parte del trattamento** — le parti hanno adottato il modulo dal titolare al responsabile; l'allegato tecnico dell'accordo sul trattamento dichiara che il fornitore utilizza i dati in forma aggregata per addestrare e migliorare i propri modelli, messi a disposizione anche di altri clienti, e che determina autonomamente tecniche, periodi e finalità di quello sviluppo. Per quella attività il fornitore determina finalità e mezzi ed è considerato titolare: quell'uso va escluso dalle istruzioni oppure coperto con lo strumento corretto (accordo di trasferimento, art. 1.2 e appendice A; accordo sul trattamento, allegato tecnico § 4; art. 28, parr. 3, lett. a, e 10).

**I-08. Il trasferimento successivo verso il paese terzo ulteriore non è coperto** — l'appendice D dell'accordo sul trattamento, aggiornata al 22 gennaio 2031, autorizza un sub-responsabile stabilito nelle Filippine con accesso agli ambienti di produzione; l'appendice B dell'accordo di trasferimento descrive il solo trasferimento verso Singapore e l'appendice D di quell'accordo dichiara l'assenza di sub-responsabili. La disciplina dei trasferimenti si applica anche ai trasferimenti successivi da un paese terzo verso un altro paese terzo (accordo sul trattamento, appendice D; accordo di trasferimento, appendici B e D; specifica funzionale § 3.2; art. 44).

**I-09. La valutazione sul trasferimento si regge su una dichiarazione del fornitore** — l'unico elemento riportato è la dichiarazione del fornitore di non avere mai ricevuto richieste di accesso da autorità pubbliche; non c'è esame del quadro normativo del paese di destinazione, non è valutata alcuna misura supplementare oltre alla cifratura con chiavi detenute dal fornitore e alla certificazione di sicurezza, e la valutazione non menziona le Filippine. La certificazione di sicurezza non è uno strumento di trasferimento (valutazione sul trasferimento §§ 3 e 4; accordo di trasferimento, appendice C).

**I-10. Il registro dei trattamenti e l'informativa non coprono il nuovo trattamento** — la scheda del registro è aggiornata al 28 novembre 2030, descrive la fatturazione, dichiara l'assenza di trasferimenti verso paesi terzi e non riporta la finalità di scoring, le categorie di dati aggiunte, i destinatari né i termini di conservazione del nuovo trattamento; l'informativa in uso è del 4 aprile 2029, dichiara che i dati non sono trasferiti fuori dallo Spazio economico europeo e che il titolare non adotta processi decisionali interamente automatizzati, e non contiene la finalità di punteggio né la logica utilizzata (scheda del trattamento; informativa §§ 5 e 9; artt. 13, 22 e 30, par. 1).

**I-11. Conservazione e finestra di addestramento sono incoerenti** — la valutazione dichiara ventiquattro mesi; la specifica prevede l'addestramento su sessanta mesi di storico e la conservazione delle basi di addestramento per l'intera finestra, trentasei mesi oltre il termine dichiarato; il registro dei rischi censisce il punto alla riga R6 con misura «non avviata» (DPIA § 3; specifica funzionale §§ 4.1 e 4.2; accordo sul trattamento, allegato tecnico § 3; registro dei rischi, riga R6).

**I-12. Il responsabile della protezione dei dati è stato sentito dopo l'approvazione** — il titolare si consulta con il responsabile della protezione dei dati quando svolge la valutazione; il frontespizio riporta il parere come «in attesa», e il messaggio del 25 novembre 2030, quattro giorni dopo l'approvazione, dichiara di non avere ricevuto il documento né di essere stata coinvolta (DPIA, frontespizio; messaggio del DPO; art. 35, par. 2).

**I-13. Affermazioni della nota del responsabile di progetto** — sono errate: che la valutazione d'impatto copra l'intero progetto; che la presenza della revisione umana escluda la disciplina delle decisioni automatizzate; che le clausole firmate coprano tutti i trasferimenti; che il termine per opporsi al sub-responsabile non sia ancora decorso, essendo scaduto il 21 febbraio 2031. Sono esatte, e non vanno contraddette: che la comunicazione del sub-responsabile abbia rispettato il preavviso di trenta giorni, e che il fornitore disponga della certificazione di sicurezza dichiarata (nota del responsabile di progetto §§ 1-4; accordo sul trattamento, art. 5.2 e appendice D).

**I-14. Simmetria del controllo** — non va presentato come rilievo un elemento neutro o conforme: la scala qualitativa di valutazione del rischio, la scelta motivata di non raccogliere il parere degli interessati, il fatto che il fornitore non sia stabilito nell'Unione, la certificazione di sicurezza in quanto tale, la comunicazione del sub-responsabile.

**I-15. Divieto di presunzione dell'esito** — non va affermato che l'autorità di controllo vieterebbe il trattamento o irrogherebbe una sanzione, che il fornitore accetterà le modifiche richieste, che i dati sono già stati oggetto di accesso da parte di autorità del paese di destinazione, o che l'avvio in produzione slitterà.

**I-16. Che cosa manca dal pacchetto** — il parere del responsabile della protezione dei dati sul contenuto della valutazione; la descrizione della logica di formazione del punteggio, che serve sia all'informativa sia alla valutazione della proporzionalità; il contratto con la fonte esterna degli indicatori di comportamento di pagamento e la base giuridica della comunicazione; la documentazione del quadro normativo dei due paesi di destinazione (messaggio del DPO; specifica funzionale § 2; valutazione sul trasferimento § 3).

## C. Controlled non-issue — la sovra-segnalazione è penalizzata

**N-01. La certificazione di sicurezza del fornitore non è un difetto** — è una misura tecnica documentata; il rilievo sta nell'uso che ne fa la valutazione sul trasferimento, non nella sua esistenza.

**N-02. La scala qualitativa di valutazione del rischio è ammissibile** — basso, medio e alto con matrice probabilità per gravità è una metodologia corrente: il difetto è l'esito dichiarato, non il metodo.

**N-03. La comunicazione del sub-responsabile è conforme** — preavviso di trenta giorni rispettato e termine di opposizione decorso il 21 febbraio 2031 senza opposizione: il difetto è la copertura del trasferimento, non la comunicazione.

**N-04. I dati di misura oraria non sono una categoria particolare di dati** — non vanno trattati come dati dell'articolo 9.

**N-05. La conclusione sulla necessità di svolgere la valutazione è corretta** — il trattamento rientra fra quelli per cui la valutazione è richiesta: non va rilevato che fosse superflua né che la soglia sia stata valutata male.

**N-06. La scelta di non raccogliere il parere degli interessati è motivata e ammissibile** — il parere si raccoglie ove opportuno e la valutazione dà la ragione della scelta.

**N-07. Che il fornitore non sia stabilito nell'Unione non è di per sé un rilievo** — è il presupposto del trasferimento, non un difetto del pacchetto.

## D. Chiusura obbligatoria

Simmetria (I-14), sovra-segnalazione con un divieto nominato per ciascuno dei controlled non-issue N-01 a N-07, divieto di presunzione dell'esito (I-15).

## E. Punti neutri dichiarati — né premiati né penalizzati (decisione #5)

Le fasce di punteggio della specifica funzionale; la pseudonimizzazione dell'identificativo cliente nei flussi; la conservazione dei registri di accesso per dodici mesi; il rapporto trimestrale di stabilità del modello; la formazione degli operatori del 16 dicembre 2030; il numero di operatori assegnati al riesame; le causali di modifica registrate nel collaudo; la clausola di verifica annuale sul fornitore; il foro italiano dell'accordo di trasferimento.

## F. Date e valori calcolati

Il caso computa. I valori attesi, con il calcolo, sono in `private/date_e_valori_verificati.md`. Le derivazioni sbagliate da escludere sono: due rischi di livello alto in luogo di tre; un rischio residuo del registro pari a «medio»; il 24 marzo 2031 come termine di opposizione al sub-responsabile; sei categorie di dati come perimetro della specifica funzionale 2.1; una percentuale di conferme diversa dal 97,4%.
