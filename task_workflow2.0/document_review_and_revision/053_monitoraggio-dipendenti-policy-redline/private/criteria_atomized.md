# WF2-053 - Criteri atomizzati

Forma a campi. Ciò che sta sotto la riga non passa al judge.


## A. Forma dell'output (interamente verifica meccanica)

### A.1 [tipo: valore]

- **Verifica** sono prodotti entrambi i file richiesti, `policy_redline.docx` e `note.md`.
- **Pass se** i due file consegnati hanno nome `policy_redline.docx` e `note.md`.
- **Fail se** manca uno dei due file, oppure un file ha nome o estensione diversi.
- **Indifferente** la presenza di file aggiuntivi.
- *non passa al judge:* Fonte task_spec.json, campo deliverable - Gravita media - judge no

### A.2 [tipo: struttura]

- **Verifica** il file `policy_redline.docx` contiene revisioni tracciate.
- **Pass se** il documento contiene almeno una cancellazione e almeno una inserzione tracciate.
- **Fail se** il documento non contiene revisioni tracciate, oppure le modifiche sono rese con marcatori nel testo.
- **Indifferente** il numero delle revisioni.
- *non passa al judge:* Fonte task_spec.json, campo deliverable - Gravita media - judge no

### A.3 [tipo: struttura]

- **Verifica** il file `note.md` contiene, nell'ordine, le cinque sezioni obbligatorie del template.
- **Pass se** le cinque intestazioni di sezione compaiono nell'ordine indicato dal template.
- **Fail se** manca almeno una sezione o l'ordine è diverso.
- **Indifferente** la numerazione delle sottosezioni.
- *non passa al judge:* Fonte public/response_template.md - Gravita media - judge no

### A.4 [tipo: valore]

- **Verifica** il file `note.md` non supera il limite di 1600 parole.
- **Pass se** il conteggio delle parole del corpo di `note.md` non supera 1600.
- **Fail se** il corpo di `note.md` supera 1600 parole.
- **Indifferente** la lunghezza delle singole sezioni.
- *non passa al judge:* Fonte task_spec.json, campo limite_parole - Gravita media - judge no

### A.5 [tipo: struttura]

- **Verifica** ogni rilievo della nota porta il riferimento all'articolo della bozza su cui incide.
- **Pass se** accanto a ciascun rilievo compare il numero dell'articolo della bozza.
- **Fail se** almeno un rilievo non porta il riferimento all'articolo.
- **Indifferente** la forma del riferimento.
- *non passa al judge:* Fonte public/01_task.md, richiesta sulla fonte - Gravita media - judge no

### A.6 [tipo: presenza]

- **Verifica** la nota distingue i rilievi che incidono da quelli che non incidono.
- **Pass se** compare una separazione fra i rilievi che richiedono modifica e gli elementi che non la richiedono.
- **Fail se** la nota presenta un elenco indistinto di osservazioni.
- **Indifferente** le etichette usate per la separazione.
- *non passa al judge:* Fonte public/response_template.md - Gravita media - judge no

### A.7 [tipo: assenza]

- **Verifica** la nota non richiama fonti normative estranee all'elenco chiuso del reference pack.
- **Fail se** compare un riferimento normativo che non figura in `private/fonti_chiuse.json`.
- **Indifferente** il richiamo agli articoli della bozza e ai paragrafi della scheda tecnica.
- *non passa al judge:* Fonte private/fonti_chiuse.json - Gravita media - judge no


## B. Merito

Il fascicolo è esaminato al 17 febbraio 2031: la bozza non è adottata, l'incontro sindacale si è chiuso senza accordo, l'informativa in vigore non copre i metadati e la valutazione preliminare esclude il monitoraggio sistematico. Il prompt chiede la bozza con revisioni tracciate e una nota che, per ciascun rilievo, indichi l'articolo su cui incide e il documento che lo fonda, la separazione fra rilievi che impongono modifica e rilievi che non la impongono, gli adempimenti anteriori all'entrata in vigore, e la valutazione della lettura del responsabile dei Sistemi Informativi.

### B.1 [issue: I-01] [tipo: qualificazione]

- **Verifica** la nota qualifica il consenso del lavoratore dell'articolo 3.1 come base giuridica non utilizzabile per questo trattamento.
- **Pass se** compare, riferita all'articolo 3.1, una fra: «base giuridica non utilizzabile», «il consenso non è la base giuridica applicabile», «il consenso non è liberamente prestato».
- **Fail se** il consenso è presentato come base giuridica utilizzabile, oppure la qualificazione non compare.
- **Indifferente** il richiamo all'articolo che elenca le basi giuridiche.
- *non passa al judge:* Fonte articoli 3.1 e 3.2 della bozza - Gravita alta - judge si

### B.2 [issue: I-01] [tipo: presenza]

- **Verifica** la nota rileva che la clausola 3.2, che subordina l'assegnazione degli strumenti al consenso, incide sulla libera prestazione del consenso stesso.
- **Pass se** compare l'indicazione che il condizionamento dell'assegnazione degli strumenti incide sulla libera prestazione del consenso.
- **Fail se** il rilievo non compare, oppure la clausola 3.2 è presentata come neutra.
- **Indifferente** la proposta di riformulazione della clausola.
- *non passa al judge:* Fonte articolo 3.2 della bozza - Gravita alta - judge si

### B.3 [issue: I-01] [tipo: presenza]

- **Verifica** la nota indica per ciascuna finalità dell'articolo 2.2 la base giuridica da sostituire al consenso.
- **Pass se** compare, per le finalità dell'articolo 2.2, l'indicazione di una base giuridica diversa dal consenso.
- **Fail se** la sostituzione non è indicata, oppure è indicata in modo indifferenziato per tutte le finalità.
- **Indifferente** l'ordine in cui le finalità sono trattate.
- *non passa al judge:* Fonte articoli 2.2 e 3.1 della bozza - Gravita alta - judge si

### B.4 [issue: I-01] [tipo: assenza]

- **Verifica** la nota non afferma che il trattamento dei dati generati dagli strumenti informatici è privo di base giuridica.
- **Fail se** compare l'affermazione che il trattamento non ha alcuna base giuridica utilizzabile.
- **Indifferente** l'indicazione che la base giuridica va individuata per ciascuna finalità.
- *non passa al judge:* Fonte articolo 3.1 della bozza - Gravita media - judge si

### B.5 [issue: I-02] [tipo: qualificazione]

- **Verifica** la nota qualifica la finalità della lettera c) dell'articolo 2.2 come controllo a distanza dell'attività lavorativa.
- **Pass se** compare, riferita a quella finalità, una fra: «controllo a distanza dell'attivita lavorativa», «controllo dell'attivita dei lavoratori», «finalita di controllo a distanza».
- **Fail se** la finalità è presentata come trattamento connesso all'uso dello strumento di lavoro, oppure la qualificazione non compare.
- **Indifferente** il richiamo al comma della norma lavoristica.
- *non passa al judge:* Fonte articolo 2.2, lettera c), della bozza - Gravita alta - judge si

### B.6 [issue: I-02] [tipo: presenza]

- **Verifica** la nota afferma che il regime degli strumenti utilizzati per rendere la prestazione non copre quella finalità.
- **Pass se** compare l'indicazione che l'esenzione prevista per gli strumenti di lavoro non si estende alla finalità della lettera c).
- **Fail se** l'esenzione è presentata come applicabile, oppure la questione non è trattata.
- **Indifferente** il richiamo al comma della norma lavoristica.
- *non passa al judge:* Fonte articolo 2.2, lettera c), della bozza - Gravita alta - judge si

### B.7 [issue: I-02] [tipo: presenza]

- **Verifica** il redline sopprime o riformula la finalità della lettera c) dell'articolo 2.2.
- **Pass se** nel documento con revisioni tracciate la lettera c) risulta cancellata o sostituita.
- **Fail se** la lettera c) resta invariata nel documento con revisioni tracciate.
- **Indifferente** la formulazione sostitutiva proposta.
- *non passa al judge:* Fonte articolo 2.2, lettera c), della bozza - Gravita alta - judge si

### B.8 [issue: I-03] [tipo: presenza]

- **Verifica** la nota rileva che nel verbale del 5 febbraio 2031 le rappresentanze dichiarano di non sottoscrivere alcun accordo.
- **Pass se** compare l'indicazione che le rappresentanze hanno dichiarato di non sottoscrivere alcun accordo.
- **Fail se** il rilievo non compare, oppure il verbale è presentato come contenente un accordo.
- **Indifferente** l'indicazione dei nominativi dei presenti.
- *non passa al judge:* Fonte punti 3 e 4 del verbale del 5 febbraio 2031 - Gravita alta - judge si

### B.9 [issue: I-03] [tipo: qualificazione]

- **Verifica** la nota qualifica come non integrato il presupposto procedurale richiesto per il controllo a distanza.
- **Pass se** compare, riferita al presupposto, una fra: «non integrato», «non sussistente», «manca il presupposto richiesto».
- **Fail se** il presupposto è presentato come integrato, oppure la qualificazione non compare.
- **Indifferente** l'indicazione della via alternativa all'accordo.
- *non passa al judge:* Fonte verbale del 5 febbraio 2031 - Gravita alta - judge si

### B.10 [issue: I-03] [tipo: assenza]

- **Verifica** la nota non afferma che l'illustrazione alle rappresentanze sindacali integra l'accordo richiesto.
- **Fail se** compare l'affermazione che l'informativa o l'illustrazione alle rappresentanze equivale all'accordo.
- **Indifferente** l'indicazione che l'incontro è stato una illustrazione.
- *non passa al judge:* Fonte punti 1 e 4 del verbale del 5 febbraio 2031 - Gravita alta - judge si

### B.11 [issue: I-04] [tipo: valore]

- **Verifica** la nota indica in 21 giorni il termine orientativo per la conservazione dei metadati indicato dall'autorità di controllo.
- **Pass se** compare «21 giorni» come termine orientativo indicato dall'autorità di controllo. compare «ventuno giorni» come termine orientativo indicato dall'autorità di controllo.
- **Fail se** è indicato un termine diverso, oppure il termine orientativo non è indicato.
- **Indifferente** il richiamo al numero del documento dell'autorità.
- *non passa al judge:* Fonte documento di indirizzo dell'autorità di controllo - Gravita alta - judge no

### B.12 [issue: I-04] [tipo: valore]

- **Verifica** la nota indica in 180 giorni il periodo di conservazione previsto dall'articolo 7.2 della bozza.
- **Pass se** compare «180 giorni» come periodo previsto dalla bozza. compare «centottanta giorni» come periodo previsto dalla bozza.
- **Fail se** è indicato un periodo diverso, oppure il periodo della bozza non è rilevato.
- **Indifferente** il richiamo al numero dell'articolo.
- *non passa al judge:* Fonte articolo 7.2 della bozza - Gravita alta - judge no

### B.13 [issue: I-04] [tipo: presenza]

- **Verifica** la nota afferma che la bozza non documenta condizioni particolari che rendano necessaria l'estensione del periodo.
- **Pass se** compare l'indicazione che la bozza non documenta condizioni che giustifichino l'estensione.
- **Fail se** il rilievo non compare, oppure la bozza è presentata come motivata sul punto.
- **Indifferente** l'indicazione delle condizioni che potrebbero giustificare l'estensione.
- *non passa al judge:* Fonte articolo 7 della bozza - Gravita alta - judge si

### B.14 [issue: I-04] [tipo: presenza]

- **Verifica** il redline riduce il periodo di conservazione dei metadati dell'articolo 7.2.
- **Pass se** nel documento con revisioni tracciate il periodo di 180 giorni risulta sostituito da un periodo più breve.
- **Fail se** il periodo di 180 giorni resta invariato nel documento con revisioni tracciate.
- **Indifferente** il valore esatto proposto in sostituzione, purché inferiore.
- *non passa al judge:* Fonte articolo 7.2 della bozza - Gravita alta - judge si

### B.15 [issue: I-05] [tipo: presenza]

- **Verifica** la nota rileva che l'affermazione dell'articolo 7.3 è contraddetta dalla scheda tecnica.
- **Pass se** compare l'indicazione che l'affermazione dell'articolo 7.3 è contraddetta dalla scheda tecnica del fornitore.
- **Fail se** il rilievo non compare, oppure l'affermazione della bozza è presentata come esatta.
- **Indifferente** il richiamo al numero del paragrafo della scheda.
- *non passa al judge:* Fonte articolo 7.3 della bozza; paragrafi 3.1 e 3.2 della scheda tecnica - Gravita alta - judge si

### B.16 [issue: I-05] [tipo: valore]

- **Verifica** la nota indica l'intervallo da 7 a 365 giorni come intervallo di configurabilità del periodo di conservazione secondo la scheda tecnica.
- **Pass se** compare «da 7 a 365 giorni» come intervallo configurabile. compaiono «7» e «365» come estremi dell'intervallo configurabile.
- **Fail se** è indicato un intervallo diverso, oppure la configurabilità non è quantificata.
- **Indifferente** l'indicazione del valore preimpostato di fabbrica.
- *non passa al judge:* Fonte paragrafo 3.1 della scheda tecnica - Gravita alta - judge no

### B.17 [issue: I-05] [tipo: presenza]

- **Verifica** il redline sopprime o riformula l'articolo 7.3.
- **Pass se** nel documento con revisioni tracciate l'articolo 7.3 risulta cancellato o sostituito.
- **Fail se** l'articolo 7.3 resta invariato nel documento con revisioni tracciate.
- **Indifferente** la formulazione sostitutiva proposta.
- *non passa al judge:* Fonte articolo 7.3 della bozza - Gravita alta - judge si

### B.18 [issue: I-06] [tipo: valore]

- **Verifica** la nota indica in 12 mesi il periodo di conservazione dei log di navigazione previsto dall'articolo 8.1.
- **Pass se** compare «12 mesi» come periodo previsto dalla bozza per i log di navigazione. compare «dodici mesi» come periodo previsto dalla bozza per i log di navigazione.
- **Fail se** è indicato un periodo diverso, oppure il periodo non è rilevato.
- **Indifferente** il richiamo al numero dell'articolo.
- *non passa al judge:* Fonte articolo 8.1 della bozza - Gravita alta - judge no

### B.19 [issue: I-06] [tipo: presenza]

- **Verifica** la nota rileva che il periodo dei log di navigazione non è correlato ad alcuna finalità determinata nell'articolo 2.
- **Pass se** compare l'indicazione che il periodo non è collegato a una finalità determinata.
- **Fail se** il rilievo non compare, oppure il periodo è presentato come motivato.
- **Indifferente** il valore proposto in sostituzione.
- *non passa al judge:* Fonte articoli 2 e 8.1 della bozza - Gravita alta - judge si

### B.20 [issue: I-07] [tipo: qualificazione]

- **Verifica** la nota qualifica il fornitore della piattaforma come responsabile del trattamento.
- **Pass se** compare, riferita al fornitore, una fra: «responsabile del trattamento», «tratta su istruzione del titolare», «non è titolare autonomo».
- **Fail se** il fornitore resta qualificato come titolare autonomo, oppure la qualificazione non compare.
- **Indifferente** il richiamo all'articolo che disciplina il rapporto con il responsabile.
- *non passa al judge:* Fonte articolo 4.3 della bozza; paragrafi 1, 4 e 6 della scheda tecnica - Gravita alta - judge si

### B.21 [issue: I-07] [tipo: presenza]

- **Verifica** il redline sostituisce la qualificazione dell'articolo 4.3.
- **Pass se** nel documento con revisioni tracciate la qualificazione di titolare autonomo risulta sostituita.
- **Fail se** la qualificazione dell'articolo 4.3 resta invariata nel documento con revisioni tracciate.
- **Indifferente** la formulazione sostitutiva proposta.
- *non passa al judge:* Fonte articolo 4.3 della bozza - Gravita alta - judge si

### B.22 [issue: I-07] [tipo: presenza]

- **Verifica** la nota indica come azione la stipulazione o la verifica dell'atto che disciplina il trattamento da parte del fornitore.
- **Pass se** compare l'indicazione di stipulare o verificare l'atto che disciplina il trattamento da parte del fornitore.
- **Fail se** l'azione non compare.
- **Indifferente** la denominazione usata per l'atto.
- *non passa al judge:* Fonte articolo 4.3 della bozza - Gravita media - judge si

### B.23 [issue: I-08] [tipo: presenza]

- **Verifica** la nota rileva che la richiesta del responsabile di funzione prevista dall'articolo 6.1 non basta come presupposto dell'accesso.
- **Pass se** compare l'indicazione che la sola richiesta del responsabile di funzione non basta come presupposto dell'accesso.
- **Fail se** il rilievo non compare, oppure la previsione è presentata come bastevole.
- **Indifferente** il numero dei livelli di autorizzazione proposti.
- *non passa al judge:* Fonte articolo 6.1 della bozza - Gravita alta - judge si

### B.24 [issue: I-08] [tipo: presenza]

- **Verifica** il redline introduce nell'articolo 6 la registrazione dell'accesso e l'autorizzazione a più di una persona.
- **Pass se** nel documento con revisioni tracciate l'articolo 6 risulta integrato con la registrazione dell'accesso e con un'autorizzazione a più di una persona.
- **Fail se** l'articolo 6 resta invariato, oppure è integrato con uno solo dei due elementi.
- **Indifferente** l'ordine in cui i due elementi sono introdotti.
- *non passa al judge:* Fonte articolo 6.1 della bozza; paragrafi 4.3 e 4.4 della scheda tecnica - Gravita alta - judge si

### B.25 [issue: I-08] [tipo: attribuzione]

- **Verifica** la nota fonda la praticabilità di quelle misure sui paragrafi 4.3 e 4.4 della scheda tecnica.
- **Pass se** il rilievo è ricondotto ai paragrafi della scheda che prevedono il giornale di accesso non modificabile e l'autorizzazione a due persone.
- **Fail se** le misure sono proposte senza indicare che la piattaforma le rende disponibili.
- **Indifferente** l'ordine in cui i due paragrafi sono citati.
- *non passa al judge:* Fonte paragrafi 4.3 e 4.4 della scheda tecnica - Gravita media - judge si

### B.26 [issue: I-08] [tipo: assenza]

- **Verifica** la nota non afferma che l'accesso al contenuto delle caselle individuali è in ogni caso vietato.
- **Fail se** compare l'affermazione che l'accesso al contenuto delle caselle non è consentito in alcun caso.
- **Indifferente** l'indicazione che l'accesso richiede presupposti e garanzie.
- *non passa al judge:* Fonte articolo 6 della bozza - Gravita alta - judge si

### B.27 [issue: I-09] [tipo: presenza]

- **Verifica** la nota rileva che l'informativa vigente non contempla i metadati né i controlli.
- **Pass se** compare l'indicazione che l'informativa vigente non copre i metadati e i controlli.
- **Fail se** il rilievo non compare, oppure l'informativa è presentata come bastevole.
- **Indifferente** il richiamo ai paragrafi dell'informativa.
- *non passa al judge:* Fonte paragrafi 3, 4 e 7 dell'informativa vigente - Gravita alta - judge si

### B.28 [issue: I-09] [tipo: presenza]

- **Verifica** il redline sostituisce il rinvio generico dell'articolo 10.1 con l'obbligo di rendere un'informativa specifica sui metadati e sui controlli.
- **Pass se** nel documento con revisioni tracciate l'articolo 10.1 risulta integrato o sostituito con la previsione di un'informativa specifica.
- **Fail se** l'articolo 10.1 resta invariato nel documento con revisioni tracciate.
- **Indifferente** la formulazione sostitutiva proposta.
- *non passa al judge:* Fonte articolo 10.1 della bozza - Gravita alta - judge si

### B.29 [issue: I-09] [tipo: presenza]

- **Verifica** la nota indica come azione l'aggiornamento dell'informativa al personale prima dell'entrata in vigore della policy.
- **Pass se** compare l'indicazione di aggiornare l'informativa prima dell'entrata in vigore.
- **Fail se** l'azione non compare, oppure l'aggiornamento è collocato dopo l'avvio del trattamento.
- **Indifferente** la forma di comunicazione proposta.
- *non passa al judge:* Fonte articoli 10.1 e 13.1 della bozza - Gravita media - judge si

### B.30 [issue: I-10] [tipo: presenza]

- **Verifica** la nota afferma che in assenza dell'informazione sulle modalità d'uso degli strumenti e sulle modalità di effettuazione dei controlli i dati raccolti non sono utilizzabili a tutti i fini connessi al rapporto di lavoro.
- **Pass se** compare l'indicazione che l'utilizzabilità dei dati a tutti i fini connessi al rapporto presuppone quell'informazione.
- **Fail se** l'utilizzabilità è presentata come dipendente dalla sola base giuridica, oppure la questione non è trattata.
- **Indifferente** il richiamo al comma della norma lavoristica.
- *non passa al judge:* Fonte articolo 10.1 della bozza; disciplina lavoristica dei controlli - Gravita alta - judge si

### B.31 [issue: I-11] [tipo: presenza]

- **Verifica** la nota rileva che la conclusione della valutazione preliminare è contraddetta dalla finalità della lettera c) dell'articolo 2.2 e dal periodo di conservazione.
- **Pass se** compare l'indicazione che la valutazione preliminare è contraddetta dal contenuto della bozza.
- **Fail se** il rilievo non compare, oppure la valutazione preliminare è presentata come coerente con la bozza.
- **Indifferente** il richiamo al riferimento del documento.
- *non passa al judge:* Fonte riga del monitoraggio sistematico della valutazione preliminare; articoli 2.2 e 7.2 della bozza - Gravita alta - judge si

### B.32 [issue: I-11] [tipo: presenza]

- **Verifica** la nota indica come azione il riesame della valutazione preliminare.
- **Pass se** compare l'indicazione di riesaminare la valutazione preliminare.
- **Fail se** l'azione non compare.
- **Indifferente** l'esito che il riesame potrebbe avere.
- *non passa al judge:* Fonte paragrafo 4 della valutazione preliminare - Gravita alta - judge si

### B.33 [issue: I-11] [tipo: assenza]

- **Verifica** la nota non afferma che una valutazione d'impatto sulla protezione dei dati è necessaria.
- **Fail se** compare l'affermazione che la valutazione d'impatto è necessaria o dovuta.
- **Indifferente** l'indicazione che l'esito del riesame potrebbe richiederla.
- *non passa al judge:* Fonte valutazione preliminare; articoli 2.2 e 7.2 della bozza - Gravita alta - judge si

### B.34 [issue: I-12] [tipo: presenza]

- **Verifica** la nota rileva che la bozza non disciplina la sorte della casella alla cessazione del rapporto.
- **Pass se** compare l'indicazione che la cessazione del rapporto non è disciplinata quanto alla casella di posta elettronica.
- **Fail se** il rilievo non compare, oppure la bozza è presentata come completa sul punto.
- **Indifferente** l'elenco delle misure proposte per la cessazione.
- *non passa al judge:* Fonte articolo 9.1 della bozza - Gravita alta - judge si

### B.35 [issue: I-12] [tipo: presenza]

- **Verifica** il redline introduce nella bozza la disciplina della disattivazione e della cancellazione della casella alla cessazione del rapporto.
- **Pass se** nel documento con revisioni tracciate compare una previsione sulla disattivazione o sulla cancellazione della casella alla cessazione.
- **Fail se** il documento con revisioni tracciate non contiene alcuna previsione sulla cessazione.
- **Indifferente** la durata proposta per l'eventuale periodo transitorio.
- *non passa al judge:* Fonte articolo 9 della bozza - Gravita alta - judge si

### B.36 [issue: I-13] [tipo: presenza]

- **Verifica** la nota rileva che la scheda tecnica consente di disattivare la raccolta del campo oggetto e in blocco quella dei record.
- **Pass se** compare l'indicazione che la raccolta è disattivabile secondo la scheda tecnica.
- **Fail se** il rilievo non compare, oppure la raccolta è presentata come necessaria.
- **Indifferente** il richiamo ai numeri dei paragrafi.
- *non passa al judge:* Fonte paragrafi 2.2 e 2.3 della scheda tecnica - Gravita media - judge si

### B.37 [issue: I-13] [tipo: presenza]

- **Verifica** la nota indica come azione la documentazione della scelta di raccogliere i metadati.
- **Pass se** compare l'indicazione di documentare e motivare la scelta di raccogliere i metadati.
- **Fail se** l'azione non compare.
- **Indifferente** la sede in cui la scelta va documentata.
- *non passa al judge:* Fonte paragrafi 2.2 e 2.3 della scheda tecnica - Gravita media - judge si

### B.38 [issue: I-14] [tipo: presenza]

- **Verifica** la nota indica come azione il riscontro alle osservazioni sindacali sulla procedura di accesso nella versione rivista della bozza.
- **Pass se** compare l'indicazione di riscontrare le osservazioni sindacali sulla procedura di accesso.
- **Fail se** l'azione non compare.
- **Indifferente** la forma del riscontro.
- *non passa al judge:* Fonte punto 3 del verbale del 5 febbraio 2031 - Gravita media - judge si


## C. Date, valori calcolati e chiusura

### C.1 [issue: N-01] [tipo: assenza]

- **Verifica** la nota non segnala come rischio di trasferimento il ricorso al sub-responsabile con sede in un paese con decisione di adeguatezza.
- **Fail se** il sub-responsabile per l'assistenza di secondo livello compare fra i profili di rischio relativi ai trasferimenti.
- **Indifferente** la menzione del sub-responsabile nell'elenco dei destinatari.
- *non passa al judge:* Fonte challenge map, N-01 - Gravita alta - judge si

### C.2 [issue: N-02] [tipo: assenza]

- **Verifica** la nota non segnala come controllo individuale le statistiche aggregate dell'articolo 5.
- **Fail se** le statistiche aggregate dell'articolo 5 compaiono fra i rilievi da modificare o fra le forme di controllo individuale.
- **Indifferente** la menzione delle statistiche fra i trattamenti descritti.
- *non passa al judge:* Fonte challenge map, N-02 - Gravita alta - judge si

### C.3 [issue: N-03] [tipo: assenza]

- **Verifica** la nota non segnala come mancante la designazione del responsabile della protezione dei dati.
- **Fail se** la designazione del responsabile della protezione dei dati compare fra gli adempimenti mancanti.
- **Indifferente** la menzione della designazione fra gli adempimenti assolti.
- *non passa al judge:* Fonte challenge map, N-03 - Gravita media - judge si

### C.4 [issue: N-04] [tipo: assenza]

- **Verifica** la nota non segnala come eccedente la conservazione del contenuto della casella per la durata del rapporto.
- **Fail se** la conservazione per la durata del rapporto compare fra i rilievi che richiedono riduzione del periodo.
- **Indifferente** la menzione dell'articolo 9.1 nella trattazione della cessazione del rapporto.
- *non passa al judge:* Fonte challenge map, N-04 - Gravita media - judge si

### C.5 [issue: N-05] [tipo: assenza]

- **Verifica** la nota non segnala come profilo di rischio il rinvio al contratto collettivo dell'articolo 12.1.
- **Fail se** il rinvio al contratto collettivo dell'articolo 12.1 compare fra i rilievi da modificare.
- **Indifferente** la menzione dell'articolo 12.1 nella descrizione della bozza.
- *non passa al judge:* Fonte challenge map, N-05 - Gravita media - judge si

### C.6 [issue: X-01] [tipo: assenza]

- **Verifica** simmetria del controllo: la nota non tratta come provata l'inutilizzabilità dei dati già raccolti mentre tratta come da riesaminare la valutazione preliminare.
- **Fail se** l'inutilizzabilità dei dati già raccolti è affermata come accertata e nello stesso documento la valutazione preliminare è rimessa a un riesame.
- **Indifferente** l'ordine in cui i due punti sono trattati.
- *non passa al judge:* Fonte articolo 10.1 della bozza; valutazione preliminare - Gravita alta - judge si

### C.7 [issue: X-02] [tipo: assenza]

- **Verifica** divieto di presunzione dell'esito: la nota non afferma che l'autorità di controllo adotterà un provvedimento nei confronti della Società.
- **Fail se** compare l'affermazione che l'autorità di controllo intervenirà o sanzionerà la Società.
- **Indifferente** l'indicazione dei profili che potrebbero formare oggetto di verifica.
- *non passa al judge:* Fonte composizione del fascicolo - Gravita alta - judge si

### C.8 [issue: X-03] [tipo: assenza]

- **Verifica** sovra-segnalazione: la nota non presenta come profilo di rischio la certificazione del sistema di gestione della sicurezza dichiarata dal fornitore.
- **Fail se** la certificazione dichiarata al paragrafo 7 della scheda tecnica compare fra i profili di rischio.
- **Indifferente** la menzione della certificazione fra le informazioni sul fornitore.
- *non passa al judge:* Fonte paragrafo 7 della scheda tecnica - Gravita media - judge si
