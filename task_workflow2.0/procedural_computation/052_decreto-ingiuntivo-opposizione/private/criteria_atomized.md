# WF2-052 - Criteri atomizzati

Forma a campi. Ciò che sta sotto la riga non passa al judge.


## A. Forma dell'output (interamente verifica meccanica)

### A.1 [tipo: valore]

- **Verifica** il deliverable è prodotto come file `procedural_map.md`.
- **Pass se** il file consegnato ha nome `procedural_map.md`.
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

- **Verifica** il deliverable non supera il limite di 2600 parole.
- **Pass se** il conteggio delle parole del corpo del deliverable non supera 2600.
- **Fail se** il corpo del deliverable supera 2600 parole.
- **Indifferente** la lunghezza delle singole sezioni.
- *non passa al judge:* Fonte task_spec.json, campo limite_parole - Gravita media - judge no

### A.4 [tipo: struttura]

- **Verifica** la sezione delle scadenze riporta per ciascuna voce data, adempimento, soggetto onerato e conseguenza dell'inosservanza.
- **Pass se** ciascuna voce della sezione delle scadenze porta i quattro elementi.
- **Fail se** almeno una voce omette uno dei quattro elementi.
- **Indifferente** l'ordine delle colonne.
- *non passa al judge:* Fonte public/response_template.md - Gravita media - judge no

### A.5 [tipo: struttura]

- **Verifica** ogni data indicata porta il riferimento al documento del fascicolo o al calcolo da cui è ricavata.
- **Pass se** accanto a ciascuna data compare il rinvio a un allegato o l'indicazione del calcolo.
- **Fail se** almeno una data non porta alcun rinvio.
- **Indifferente** la forma del rinvio.
- *non passa al judge:* Fonte public/01_task.md, richiesta sulla fonte - Gravita media - judge no

### A.6 [tipo: struttura]

- **Verifica** per ciascuna scadenza calcolata il deliverable espone il giorno di decorrenza, la durata e il risultato come passaggi distinti.
- **Pass se** per ciascuna scadenza calcolata compaiono i tre passaggi.
- **Fail se** almeno una scadenza calcolata è indicata senza esporre i passaggi.
- **Indifferente** la forma tabellare o discorsiva del computo.
- *non passa al judge:* Fonte public/01_task.md, richiesta sul percorso - Gravita media - judge no

### A.7 [tipo: presenza]

- **Verifica** il deliverable distingue i fatti provati dagli atti, le inferenze, le questioni controverse e i dati mancanti.
- **Pass se** compaiono, riferite a contenuti diversi, le quattro distinzioni.
- **Fail se** il deliverable presenta un solo piano indistinto di affermazioni.
- **Indifferente** le etichette usate per la distinzione.
- *non passa al judge:* Fonte public/response_template.md - Gravita media - judge no

### A.8 [tipo: assenza]

- **Verifica** il deliverable non richiama fonti normative estranee all'elenco chiuso del reference pack.
- **Fail se** compare un riferimento normativo che non figura in `private/fonti_chiuse.json`.
- **Indifferente** il richiamo alle clausole del contratto e ai numeri di documento del fascicolo.
- *non passa al judge:* Fonte private/fonti_chiuse.json - Gravita media - judge no


## B. Merito

Il fascicolo è esaminato al 18 giugno 2031: il decreto è stato notificato il 20 maggio, non è provvisoriamente esecutivo, l'opposizione non è stata proposta e il termine scade il 30 giugno. La bozza di citazione porta un calendario internamente insufficiente e una nota interna che applica una regola abrogata. Il prompt chiede la mappa del procedimento con soggetto onerato e conseguenza dell'inosservanza, il calcolo esposto passaggio per passaggio, la fonte di ciascuna decorrenza, la revisione della bozza, il perimetro del contestabile, l'indicazione delle questioni controverse invece della loro soluzione, la mappa degli scenari con titolo, importo eseguibile e prossima istanza, la distinzione fra profili che incidono e profili che non incidono, e la valutazione della nota interna dello studio.

### B.1 [issue: I-01] [tipo: valore]

- **Verifica** il deliverable indica in quaranta giorni la durata del termine per proporre opposizione.
- **Pass se** compare «quaranta giorni» come durata del termine di opposizione. compare «40 giorni» come durata del termine di opposizione.
- **Fail se** è indicata una durata diversa, oppure la durata non è indicata.
- **Indifferente** il richiamo all'articolo che fissa il termine.
- *non passa al judge:* Fonte avvertimento del decreto ingiuntivo - Gravita alta - judge no

### B.2 [issue: I-01] [tipo: valore]

- **Verifica** il deliverable indica il 20 maggio 2031 come giorno da cui decorre il termine di opposizione.
- **Pass se** compare «20 maggio 2031» come giorno di decorrenza. compare «20/05/2031» come giorno di decorrenza.
- **Fail se** è indicato un giorno di decorrenza diverso, oppure la decorrenza non è indicata.
- **Indifferente** l'indicazione dell'ora della consegna.
- *non passa al judge:* Fonte relata di notificazione; date_verificate.md - Gravita alta - judge no

### B.3 [issue: I-01] [tipo: attribuzione]

- **Verifica** il deliverable riconduce la decorrenza alla notificazione del decreto risultante dalla ricevuta di avvenuta consegna.
- **Pass se** la decorrenza è ricondotta a una fra: «notificazione del decreto», «ricevuta di avvenuta consegna», «relata di notificazione».
- **Fail se** la decorrenza è ricondotta all'emissione del decreto, al deposito del ricorso, oppure l'atto di decorrenza non è indicato.
- **Indifferente** la menzione del gestore del servizio.
- *non passa al judge:* Fonte relata di notificazione - Gravita alta - judge si

### B.4 [issue: I-01] [tipo: assenza]

- **Verifica** il deliverable non indica il 12 maggio 2031 come giorno da cui decorre il termine di opposizione.
- **Fail se** il 12 maggio 2031 è indicato come giorno di decorrenza del termine.
- **Indifferente** la menzione del 12 maggio 2031 come data di emissione del decreto.
- *non passa al judge:* Fonte decreto ingiuntivo - Gravita alta - judge si

### B.5 [issue: I-02] [tipo: valore]

- **Verifica** il deliverable indica il 30 giugno 2031 come scadenza del termine per proporre opposizione.
- **Pass se** compare «30 giugno 2031» come scadenza del termine di opposizione. compare «30/06/2031» come scadenza del termine di opposizione.
- **Fail se** è indicata una scadenza diversa, oppure la scadenza non è indicata.
- **Indifferente** l'indicazione dell'ora entro cui notificare.
- *non passa al judge:* Fonte computo verificato; date_verificate.md - Gravita alta - judge no

### B.6 [issue: I-02] [tipo: presenza]

- **Verifica** il deliverable afferma che il quarantesimo giorno cade in giorno festivo e che il termine è prorogato al primo giorno successivo non festivo.
- **Pass se** compare l'indicazione che la scadenza nominale cade di domenica e che opera la proroga al giorno non festivo successivo.
- **Fail se** la proroga non è affermata, oppure è affermata senza indicare il fatto che la determina.
- **Indifferente** la citazione della norma sulla proroga.
- *non passa al judge:* Fonte calendario 2031; disciplina sulla proroga dei termini - Gravita alta - judge si

### B.7 [issue: I-02] [tipo: assenza]

- **Verifica** il deliverable non indica il 29 giugno 2031 come scadenza del termine per proporre opposizione.
- **Fail se** il 29 giugno 2031 è indicato come data entro cui l'opposizione va notificata.
- **Indifferente** la menzione del 29 giugno 2031 come quarantesimo giorno nominale.
- *non passa al judge:* Fonte computo verificato - Gravita alta - judge si

### B.8 [issue: I-03] [tipo: valore]

- **Verifica** il deliverable indica in dodici il numero dei giorni che residuano alla data di riferimento.
- **Pass se** compare «dodici giorni» come tempo residuo. compare «12 giorni» come tempo residuo.
- **Fail se** è indicato un numero diverso, oppure il tempo residuo non è indicato.
- **Indifferente** l'indicazione dei giorni lavorativi residui.
- *non passa al judge:* Fonte data di riferimento e scadenza calcolata - Gravita alta - judge no

### B.9 [issue: I-04] [tipo: presenza]

- **Verifica** il deliverable afferma che la riduzione a metà dei termini di comparizione nell'opposizione a decreto ingiuntivo non è più prevista.
- **Pass se** compare l'indicazione che la riduzione a metà dei termini di comparizione è stata soppressa e non si applica.
- **Fail se** l'affermazione non compare, oppure la riduzione è presentata come applicabile.
- **Indifferente** l'indicazione dell'anno in cui la riduzione è stata soppressa.
- *non passa al judge:* Fonte disciplina dell'opposizione a decreto ingiuntivo - Gravita alta - judge si

### B.10 [issue: I-04] [tipo: presenza]

- **Verifica** il deliverable rileva che la nota interna della bozza applica la riduzione a metà dei termini.
- **Pass se** compare l'indicazione che la nota interna della bozza si fonda sulla riduzione a metà dei termini.
- **Fail se** il rilievo non compare, oppure la nota interna è presentata come esatta.
- **Indifferente** il giudizio sull'opportunità di inserire note interne nell'atto.
- *non passa al judge:* Fonte nota interna della bozza di citazione - Gravita alta - judge si

### B.11 [issue: I-04] [tipo: assenza]

- **Verifica** il deliverable non applica la riduzione a metà ad alcuno dei termini della procedura.
- **Fail se** un termine della procedura è calcolato nella misura ridotta della metà.
- **Indifferente** la menzione della riduzione come regola non più vigente.
- *non passa al judge:* Fonte disciplina dell'opposizione a decreto ingiuntivo - Gravita alta - judge si

### B.12 [issue: I-05] [tipo: valore]

- **Verifica** il deliverable indica in centoventi giorni liberi il termine minimo che deve intercorrere fra notificazione e udienza per notificazione in Italia.
- **Pass se** compare «centoventi giorni» come termine minimo a comparire. compare «120 giorni» come termine minimo a comparire.
- **Fail se** è indicato un termine minimo diverso, oppure il termine minimo non è indicato.
- **Indifferente** l'indicazione del termine per la notificazione all'estero.
- *non passa al judge:* Fonte disciplina dei termini a comparire - Gravita alta - judge no

### B.13 [issue: I-05] [tipo: presenza]

- **Verifica** il deliverable afferma che il termine minimo a comparire si computa in giorni liberi.
- **Pass se** compare l'indicazione che i giorni si computano come giorni liberi, esclusi il giorno della notificazione e quello dell'udienza.
- **Fail se** il computo in giorni liberi non è affermato, oppure il termine è presentato come computabile includendo gli estremi.
- **Indifferente** la citazione della norma sul computo.
- *non passa al judge:* Fonte disciplina dei termini a comparire - Gravita media - judge si

### B.14 [issue: I-06] [tipo: valore]

- **Verifica** il deliverable indica in centosedici il numero dei giorni liberi fra la notificazione programmata dalla bozza e l'udienza da essa indicata.
- **Pass se** compare «centosedici giorni» come intervallo fra notificazione programmata e udienza. compare «116 giorni» come intervallo fra notificazione programmata e udienza.
- **Fail se** è indicato un numero diverso, oppure l'intervallo non è calcolato.
- **Indifferente** l'indicazione dei giorni non liberi.
- *non passa al judge:* Fonte date della bozza; date_verificate.md - Gravita alta - judge no

### B.15 [issue: I-06] [tipo: qualificazione]

- **Verifica** il deliverable qualifica il calendario della bozza come inferiore al termine minimo a comparire.
- **Pass se** compare, riferito al calendario della bozza, una fra: «inferiore al termine minimo», «non rispetta il termine minimo a comparire», «insufficiente rispetto ai centoventi giorni liberi».
- **Fail se** il calendario è presentato come rispettoso del minimo, oppure la qualificazione non compare.
- **Indifferente** il numero di giorni di scostamento indicato.
- *non passa al judge:* Fonte date della bozza; termine minimo a comparire - Gravita alta - judge si

### B.16 [issue: I-07] [tipo: presenza]

- **Verifica** il deliverable indica come azione lo spostamento dell'udienza a una data che rispetti il termine minimo, prima della notificazione.
- **Pass se** compare l'indicazione di spostare l'udienza a una data compatibile con il termine minimo, prima di notificare l'atto.
- **Fail se** l'azione non compare, oppure la correzione è collocata dopo la notificazione.
- **Indifferente** la data proposta per l'udienza.
- *non passa al judge:* Fonte date della bozza; termine minimo a comparire - Gravita alta - judge si

### B.17 [issue: I-07] [tipo: assenza]

- **Verifica** il deliverable non afferma che l'insufficienza del termine a comparire è sanabile con una istanza al giudice dopo la notificazione.
- **Fail se** compare l'affermazione che l'insufficienza si sana con una istanza successiva alla notificazione.
- **Indifferente** l'indicazione dei rimedi che il giudice può adottare in caso di vizio.
- *non passa al judge:* Fonte disciplina dei termini a comparire - Gravita alta - judge si

### B.18 [issue: I-08] [tipo: valore]

- **Verifica** il deliverable indica in dieci giorni dalla notificazione il termine per la costituzione dell'opponente.
- **Pass se** compare «dieci giorni» come termine per la costituzione dell'opponente. compare «10 giorni» come termine per la costituzione dell'opponente.
- **Fail se** è indicato un termine diverso, oppure il termine non è indicato.
- **Indifferente** il richiamo all'articolo che lo fissa.
- *non passa al judge:* Fonte disciplina della costituzione dell'attore - Gravita alta - judge no

### B.19 [issue: I-08] [tipo: qualificazione]

- **Verifica** il deliverable qualifica l'opponente come parte che assume la veste di attore nel giudizio di opposizione.
- **Pass se** compare, riferita all'opponente, una fra: «assume la veste di attore», «è attore in senso formale», «sta in giudizio come attore».
- **Fail se** l'opponente è qualificato come convenuto, oppure la qualificazione non compare.
- **Indifferente** il richiamo alla posizione sostanziale delle parti.
- *non passa al judge:* Fonte disciplina dell'opposizione a decreto ingiuntivo - Gravita alta - judge si

### B.20 [issue: I-08] [tipo: presenza]

- **Verifica** il deliverable indica quali atti l'opponente deposita al momento della costituzione.
- **Pass se** compare l'indicazione di almeno tre elementi fra originale dell'atto notificato, procura, documenti e nota di iscrizione a ruolo.
- **Fail se** l'indicazione non compare, oppure sono indicati meno di tre elementi.
- **Indifferente** l'ordine in cui gli atti sono elencati.
- *non passa al judge:* Fonte disciplina della costituzione dell'attore - Gravita media - judge si

### B.21 [issue: I-08] [tipo: assenza]

- **Verifica** il deliverable non indica in cinque giorni il termine per la costituzione dell'opponente.
- **Fail se** il termine per la costituzione dell'opponente è indicato in cinque giorni.
- **Indifferente** la menzione della riduzione a metà come regola non più vigente.
- *non passa al judge:* Fonte disciplina della costituzione dell'attore - Gravita alta - judge si

### B.22 [issue: I-09] [tipo: valore]

- **Verifica** il deliverable indica in settanta giorni prima dell'udienza il termine per la costituzione dell'opposto.
- **Pass se** compare «settanta giorni» come termine per la costituzione dell'opposto. compare «70 giorni» come termine per la costituzione dell'opposto.
- **Fail se** è indicato un termine diverso, oppure il termine non è indicato.
- **Indifferente** il richiamo all'articolo che lo fissa.
- *non passa al judge:* Fonte disciplina della costituzione del convenuto - Gravita alta - judge no

### B.23 [issue: I-09] [tipo: assenza]

- **Verifica** il deliverable non indica in venti giorni prima dell'udienza il termine per la costituzione dell'opposto.
- **Fail se** il termine per la costituzione dell'opposto è indicato in venti giorni prima dell'udienza.
- **Indifferente** la menzione del termine previgente con la qualificazione di regola non più vigente.
- *non passa al judge:* Fonte disciplina della costituzione del convenuto - Gravita alta - judge si

### B.24 [issue: I-10] [tipo: valore]

- **Verifica** il deliverable indica in quaranta, venti e dieci giorni prima dell'udienza i termini delle tre memorie integrative.
- **Pass se** compaiono «quaranta», «venti» e «dieci» giorni come termini delle tre memorie. compaiono «40», «20» e «10» giorni come termini delle tre memorie.
- **Fail se** è indicato un termine diverso per una delle memorie, oppure il numero delle memorie è diverso da tre.
- **Indifferente** l'ordine in cui le tre memorie sono elencate.
- *non passa al judge:* Fonte disciplina delle memorie integrative - Gravita alta - judge no

### B.25 [issue: I-10] [tipo: presenza]

- **Verifica** il deliverable indica per ciascuna delle tre memorie integrative il contenuto proprio.
- **Pass se** per ciascuna delle tre memorie compare l'indicazione del contenuto ammesso.
- **Fail se** il contenuto non è differenziato fra le tre memorie, oppure è indicato per meno di tre memorie.
- **Indifferente** il grado di dettaglio del contenuto indicato.
- *non passa al judge:* Fonte disciplina delle memorie integrative - Gravita alta - judge si

### B.26 [issue: I-11] [tipo: presenza]

- **Verifica** il deliverable afferma che il decreto non è dichiarato provvisoriamente esecutivo.
- **Pass se** compare l'indicazione che il decreto non è provvisoriamente esecutivo.
- **Fail se** il decreto è presentato come esecutivo, oppure lo stato del titolo non è affermato.
- **Indifferente** il richiamo al dispositivo del decreto.
- *non passa al judge:* Fonte dispositivo del decreto ingiuntivo - Gravita alta - judge si

### B.27 [issue: I-11] [tipo: presenza]

- **Verifica** il deliverable afferma che alla data di riferimento non esiste alcun titolo esecutivo azionabile.
- **Pass se** compare l'indicazione che alla data di riferimento non esiste titolo esecutivo.
- **Fail se** l'affermazione non compare, oppure è indicata l'esistenza di un titolo azionabile.
- **Indifferente** l'indicazione che il titolo potrebbe formarsi in seguito.
- *non passa al judge:* Fonte dispositivo del decreto; determinazione dell'amministratore unico - Gravita alta - judge si

### B.28 [issue: I-11] [tipo: assenza]

- **Verifica** il deliverable non afferma che l'opposta può procedere a pignoramento alla data di riferimento.
- **Fail se** compare l'affermazione che l'opposta può iniziare l'esecuzione forzata alla data di riferimento.
- **Indifferente** l'indicazione delle condizioni al verificarsi delle quali l'esecuzione diverrebbe possibile.
- *non passa al judge:* Fonte dispositivo del decreto ingiuntivo - Gravita alta - judge si

### B.29 [issue: I-12] [tipo: presenza]

- **Verifica** il deliverable rileva che la domanda di sospensione contenuta nella bozza presuppone la concessione o l'inizio dell'esecuzione provvisoria.
- **Pass se** compare l'indicazione che la domanda di sospensione presuppone l'esecuzione provvisoria concessa o iniziata.
- **Fail se** il rilievo non compare, oppure la domanda è presentata come autonomamente proponibile allo stato.
- **Indifferente** il richiamo all'articolo che disciplina la sospensione.
- *non passa al judge:* Fonte conclusione sub b) della bozza; dispositivo del decreto - Gravita alta - judge si

### B.30 [issue: I-12] [tipo: presenza]

- **Verifica** il deliverable indica come azione la riformulazione della domanda di sospensione in via subordinata all'eventuale concessione dell'esecuzione provvisoria.
- **Pass se** compare l'indicazione di formulare la domanda di sospensione in via subordinata.
- **Fail se** l'azione non compare, oppure è indicata la semplice soppressione della domanda.
- **Indifferente** la formulazione proposta.
- *non passa al judge:* Fonte conclusione sub b) della bozza - Gravita alta - judge si

### B.31 [issue: I-13] [tipo: presenza]

- **Verifica** il deliverable afferma che l'opposto può chiedere nel giudizio di opposizione la provvisoria esecuzione del decreto.
- **Pass se** compare l'indicazione che l'opposto può chiedere la provvisoria esecuzione nel giudizio di opposizione.
- **Fail se** l'affermazione non compare, oppure la richiesta è presentata come non proponibile.
- **Indifferente** il richiamo all'articolo che la disciplina.
- *non passa al judge:* Fonte disciplina della provvisoria esecuzione nel giudizio di opposizione - Gravita alta - judge si

### B.32 [issue: I-13] [tipo: assenza]

- **Verifica** il deliverable non afferma che la provvisoria esecuzione sarà concessa per l'intero importo ingiunto.
- **Fail se** compare l'affermazione che la provvisoria esecuzione sarà concessa, o che lo sarà per l'intero importo.
- **Indifferente** l'indicazione degli importi per i quali la concessione è più probabile.
- *non passa al judge:* Fonte composizione documentale del credito - Gravita alta - judge si

### B.33 [issue: I-13] [tipo: presenza]

- **Verifica** il deliverable indica come azione la predisposizione dell'opposizione all'istanza di provvisoria esecuzione, con la prova documentale delle voci contestate.
- **Pass se** compare l'indicazione di predisporre l'opposizione all'istanza con la relativa prova documentale.
- **Fail se** l'azione non compare.
- **Indifferente** l'elenco dei documenti proposti.
- *non passa al judge:* Fonte composizione documentale del credito - Gravita alta - judge si

### B.34 [issue: I-14] [tipo: presenza]

- **Verifica** il deliverable rileva che la bozza chiede la revoca integrale del decreto sviluppando motivi per un importo inferiore.
- **Pass se** compare l'indicazione che conclusioni e motivi della bozza non sono allineati quanto all'importo.
- **Fail se** il rilievo non compare, oppure conclusioni e motivi sono presentati come allineati.
- **Indifferente** la formulazione proposta per le conclusioni.
- *non passa al judge:* Fonte punto 6 e conclusione sub a) della bozza - Gravita alta - judge si

### B.35 [issue: I-14] [tipo: valore]

- **Verifica** il deliverable indica in euro 126.000,00 l'importo per il quale la bozza sviluppa motivi.
- **Pass se** compare «euro 126.000,00» come importo contestato dalla bozza. compare «126.000,00» come importo contestato dalla bozza.
- **Fail se** è indicato un importo diverso, oppure l'importo contestato dalla bozza non è isolato.
- **Indifferente** la scomposizione dell'importo fra note di credito e penale.
- *non passa al judge:* Fonte punto 6 della bozza; date_verificate.md - Gravita alta - judge no

### B.36 [issue: I-14] [tipo: presenza]

- **Verifica** il deliverable indica come azione l'allineamento delle conclusioni ai motivi, in via principale e in via gradata.
- **Pass se** compare l'indicazione di articolare le conclusioni in via principale e in via gradata in coerenza con i motivi.
- **Fail se** l'azione non compare.
- **Indifferente** la formulazione proposta.
- *non passa al judge:* Fonte conclusione sub a) della bozza - Gravita alta - judge si

### B.37 [issue: I-15] [tipo: valore]

- **Verifica** il deliverable indica in euro 60.000,00 l'ammontare complessivo degli acconti versati e non imputati a riduzione del credito.
- **Pass se** compare «euro 60.000,00» come ammontare degli acconti non imputati. compare «60.000,00» come ammontare degli acconti non imputati.
- **Fail se** è indicato un ammontare diverso, oppure gli acconti non sono isolati.
- **Indifferente** l'indicazione delle due date di versamento.
- *non passa al judge:* Fonte righe degli incassi dell'estratto delle partite; date_verificate.md - Gravita alta - judge no

### B.38 [issue: I-15] [tipo: presenza]

- **Verifica** il deliverable rileva che la bozza non contesta gli acconti non imputati.
- **Pass se** compare l'indicazione che gli acconti non imputati non figurano fra i motivi della bozza.
- **Fail se** il rilievo non compare, oppure gli acconti sono presentati come contestati dalla bozza.
- **Indifferente** il richiamo alla determinazione dell'amministratore unico.
- *non passa al judge:* Fonte punto 6 della bozza; estratto delle partite - Gravita alta - judge si

### B.39 [issue: I-15] [tipo: attribuzione]

- **Verifica** il deliverable ricava la mancata imputazione degli acconti dalla colonna dell'estratto che la registra.
- **Pass se** il rilievo è ricondotto alla colonna dell'estratto relativa all'imputazione a riduzione del credito.
- **Fail se** il rilievo è affermato senza indicare il dato dell'estratto da cui è ricavato.
- **Indifferente** l'indicazione dei numeri di riga.
- *non passa al judge:* Fonte estratto delle partite - Gravita alta - judge si

### B.40 [issue: I-16] [tipo: valore]

- **Verifica** il deliverable indica in euro 210.700,00 l'importo complessivamente contestabile sulla base dei documenti.
- **Pass se** compare «euro 210.700,00» come importo complessivamente contestabile. compare «210.700,00» come importo complessivamente contestabile.
- **Fail se** è indicato un importo diverso, oppure il contestabile non è calcolato.
- **Indifferente** l'ordine in cui le componenti sono elencate.
- *non passa al judge:* Fonte estratto delle partite; date_verificate.md - Gravita alta - judge no

### B.41 [issue: I-16] [tipo: valore]

- **Verifica** il deliverable indica in euro 84.700,00 lo scostamento fra l'importo contestabile e quello contestato dalla bozza.
- **Pass se** compare «euro 84.700,00» come scostamento. compare «84.700,00» come scostamento.
- **Fail se** è indicato uno scostamento diverso, oppure lo scostamento non è quantificato.
- **Indifferente** la scomposizione dello scostamento fra acconti e interessi.
- *non passa al judge:* Fonte estratto delle partite; punto 6 della bozza - Gravita alta - judge no

### B.42 [issue: I-16] [tipo: presenza]

- **Verifica** il deliverable espone la composizione dell'importo contestabile distinguendo capitale, penale e interessi.
- **Pass se** compare la distinzione fra la componente in linea capitale, la penale e gli interessi all'interno dell'importo contestabile.
- **Fail se** la composizione non è esposta, oppure le tre componenti non sono distinte.
- **Indifferente** l'ordine in cui le componenti sono esposte.
- *non passa al judge:* Fonte estratto delle partite - Gravita media - judge si

### B.43 [issue: I-17] [tipo: qualificazione]

- **Verifica** il deliverable qualifica la PEC dell'opposta del 3 aprile 2031 come conferma della ricezione delle note di credito accompagnata da riserva sul loro fondamento.
- **Pass se** compare, riferita a quella comunicazione, una fra: «conferma la ricezione con riserva di verifica», «riserva il fondamento», «non accetta le note di credito».
- **Fail se** la comunicazione è qualificata come accettazione delle note di credito, oppure la qualificazione non compare.
- **Indifferente** l'indicazione dell'ora della consegna.
- *non passa al judge:* Fonte corpo della PEC del 3 aprile 2031 - Gravita alta - judge si

### B.44 [issue: I-17] [tipo: assenza]

- **Verifica** il deliverable non afferma che la PEC del 3 aprile 2031 prova l'accettazione delle note di credito.
- **Fail se** compare l'affermazione che quella comunicazione prova l'accettazione delle note di credito o il riconoscimento del credito dell'opponente.
- **Indifferente** l'indicazione che la comunicazione prova la conoscenza delle note.
- *non passa al judge:* Fonte corpo della PEC del 3 aprile 2031 - Gravita alta - judge si

### B.45 [issue: I-18] [tipo: presenza]

- **Verifica** il deliverable indica come necessaria la produzione della documentazione di reso richiesta dall'opposta.
- **Pass se** compare l'indicazione di produrre la documentazione di reso, con documento di trasporto e indicazione di partita e lotto.
- **Fail se** l'indicazione non compare, oppure la documentazione è data per acquisita.
- **Indifferente** il richiamo alle clausole del contratto.
- *non passa al judge:* Fonte corpo della PEC del 3 aprile 2031; clausola 10.1 del contratto - Gravita alta - judge si

### B.46 [issue: I-18] [tipo: presenza]

- **Verifica** il deliverable indica come necessaria la prova delle contestazioni scritte di qualità nel termine contrattuale.
- **Pass se** compare l'indicazione di provare le contestazioni scritte di qualità nel termine previsto dal contratto.
- **Fail se** l'indicazione non compare, oppure la tempestività è data per provata.
- **Indifferente** l'indicazione della durata del termine contrattuale.
- *non passa al judge:* Fonte clausola 9.1 del contratto; PEC del 3 aprile 2031 - Gravita alta - judge si

### B.47 [issue: I-18] [tipo: assenza]

- **Verifica** il deliverable non afferma che le note di credito provano da sé il minor debito.
- **Fail se** compare l'affermazione che l'emissione delle note di credito è di per sé prova del minor debito.
- **Indifferente** l'indicazione che le note di credito sono il punto di partenza della prova.
- *non passa al judge:* Fonte PEC del 3 aprile 2031 - Gravita alta - judge si

### B.48 [issue: I-19] [tipo: qualificazione]

- **Verifica** il deliverable qualifica il deposito di euro 276.000,00 come atto di disponibilità che non costituisce riconoscimento del debito residuo.
- **Pass se** compare, riferito a quel deposito, una fra: «non costituisce riconoscimento», «senza riconoscimento del debito», «atto di disponibilita».
- **Fail se** il deposito è qualificato come riconoscimento del debito o come confessione, oppure la qualificazione non compare.
- **Indifferente** l'indicazione della sede in cui il deposito va fatto constare.
- *non passa al judge:* Fonte punti 1 e 2 della determinazione dell'amministratore unico - Gravita alta - judge si

### B.49 [issue: I-19] [tipo: valore]

- **Verifica** il deliverable indica in euro 276.000,00 l'importo del deposito autorizzato.
- **Pass se** compare «euro 276.000,00» come importo del deposito autorizzato. compare «276.000,00» come importo del deposito autorizzato.
- **Fail se** è indicato un importo diverso, oppure l'importo del deposito non è indicato.
- **Indifferente** l'indicazione del calcolo che porta a quell'importo.
- *non passa al judge:* Fonte punto 1 della determinazione; date_verificate.md - Gravita alta - judge no

### B.50 [issue: I-20] [tipo: qualificazione]

- **Verifica** il deliverable qualifica il rapporto dedotto in giudizio come contratto di somministrazione.
- **Pass se** compare, riferito al rapporto, una fra: «contratto di somministrazione», «somministrazione periodica», «rapporto di somministrazione».
- **Fail se** il rapporto è qualificato diversamente, oppure la qualificazione non compare.
- **Indifferente** il richiamo all'articolo del codice che lo definisce.
- *non passa al judge:* Fonte oggetto del contratto del 9 gennaio 2029 - Gravita alta - judge si

### B.51 [issue: I-20] [tipo: presenza]

- **Verifica** il deliverable afferma che per questa materia il tentativo di mediazione è condizione di procedibilità.
- **Pass se** compare l'indicazione che il tentativo di mediazione è condizione di procedibilità per la materia dedotta in giudizio.
- **Fail se** l'affermazione non compare, oppure la mediazione è presentata come facoltativa.
- **Indifferente** il richiamo all'articolo che la prevede.
- *non passa al judge:* Fonte oggetto del contratto; disciplina della mediazione - Gravita alta - judge si

### B.52 [issue: I-20] [tipo: presenza]

- **Verifica** il deliverable rileva che la bozza non fa alcuna menzione della condizione di procedibilità.
- **Pass se** compare l'indicazione che la bozza non menziona la condizione di procedibilità.
- **Fail se** il rilievo non compare, oppure la bozza è presentata come conforme sul punto.
- **Indifferente** la formulazione proposta per l'atto.
- *non passa al judge:* Fonte bozza di citazione - Gravita alta - judge si

### B.53 [issue: I-20] [tipo: assenza]

- **Verifica** il deliverable non afferma su quale parte gravi l'onere di presentare la domanda di mediazione, presentandolo come punto pacifico.
- **Fail se** compare l'affermazione che l'onere di presentare la domanda di mediazione grava con certezza su una delle due parti, senza dichiarare la questione controversa.
- **Indifferente** l'indicazione della soluzione ritenuta preferibile, purché dichiarata come controversa.
- *non passa al judge:* Fonte disciplina della mediazione nell'opposizione a decreto ingiuntivo - Gravita alta - judge si

### B.54 [issue: I-21] [tipo: presenza]

- **Verifica** il deliverable espone quattro scenari distinti: revoca integrale, accoglimento parziale, rigetto e concessione della provvisoria esecuzione.
- **Pass se** i quattro scenari compaiono come voci separate.
- **Fail se** gli scenari sono meno di quattro, oppure sono trattati in forma indistinta.
- **Indifferente** l'ordine in cui gli scenari sono esposti.
- *non passa al judge:* Fonte public/response_template.md - Gravita alta - judge si

### B.55 [issue: I-21] [tipo: struttura]

- **Verifica** per ciascuno scenario il deliverable indica il titolo che ne deriva, l'importo eseguibile e la prossima istanza utile.
- **Pass se** ciascuno scenario porta i tre elementi.
- **Fail se** almeno uno scenario omette uno dei tre elementi.
- **Indifferente** l'ordine in cui i tre elementi sono esposti.
- *non passa al judge:* Fonte public/response_template.md - Gravita alta - judge si

### B.56 [issue: I-21] [tipo: assenza]

- **Verifica** il deliverable non afferma quale dei quattro scenari si verificherà.
- **Fail se** compare l'affermazione che uno degli scenari si verificherà o è il più probabile in termini di esito.
- **Indifferente** l'indicazione di quali elementi renderebbero uno scenario più probabile.
- *non passa al judge:* Fonte composizione del fascicolo - Gravita alta - judge si


## C. Date, valori calcolati e chiusura

### C.1 [issue: I-06] [tipo: assenza]

- **Verifica** il deliverable non presenta il calendario della bozza come rispettoso del termine minimo per effetto della riduzione a metà.
- **Fail se** il calendario della bozza è presentato come rispettoso del minimo applicando la riduzione a metà dei termini.
- **Indifferente** la menzione della nota interna come punto da correggere.
- *non passa al judge:* Fonte nota interna della bozza - Gravita alta - judge si

### C.2 [issue: I-02] [tipo: assenza]

- **Verifica** il deliverable non presenta la scadenza del termine di opposizione come risultato di un computo in giorni lavorativi.
- **Fail se** la scadenza è ricavata contando quaranta giorni lavorativi.
- **Indifferente** l'indicazione del giorno della settimana in cui la scadenza cade.
- *non passa al judge:* Fonte computo verificato - Gravita media - judge si

### C.3 [issue: N-01] [tipo: assenza]

- **Verifica** il deliverable non attribuisce all'ora della consegna della notificazione l'effetto di spostare la decorrenza al giorno successivo.
- **Fail se** all'ora della consegna è attribuito l'effetto di spostare il perfezionamento al giorno successivo.
- **Indifferente** la menzione dell'ora nella descrizione della notificazione.
- *non passa al judge:* Fonte challenge map, N-01 - Gravita alta - judge si

### C.4 [issue: N-02] [tipo: assenza]

- **Verifica** il deliverable non applica la sospensione feriale sul termine di opposizione al periodo che va dal 20 maggio al 30 giugno 2031.
- **Fail se** la sospensione feriale è applicata per spostare la scadenza del termine di opposizione oltre il 30 giugno 2031.
- **Indifferente** la menzione della sospensione feriale con l'indicazione che il periodo non la interseca.
- *non passa al judge:* Fonte challenge map, N-02 - Gravita alta - judge si

### C.5 [issue: N-03] [tipo: assenza]

- **Verifica** il deliverable non afferma la nullita della clausola penale del contratto, ne mette in discussione la validita della clausola penale.
- **Fail se** compare l'affermazione che la clausola penale è nulla o invalida.
- **Indifferente** la contestazione del presupposto della penale o della sua misura.
- *non passa al judge:* Fonte challenge map, N-03 - Gravita alta - judge si

### C.6 [issue: N-04] [tipo: assenza]

- **Verifica** il deliverable non segnala come errore il foro indicato nella bozza.
- **Fail se** il foro indicato nella bozza compare fra i profili da correggere.
- **Indifferente** la menzione del foro nella descrizione dell'atto.
- *non passa al judge:* Fonte challenge map, N-04 - Gravita media - judge si

### C.7 [issue: N-05] [tipo: assenza]

- **Verifica** il deliverable non segnala come profilo di rischio la distrazione delle spese in favore del difensore disposta dal decreto.
- **Fail se** la distrazione delle spese compare fra i profili di rischio o fra le irregolarità.
- **Indifferente** la menzione della liquidazione delle spese nella descrizione del decreto.
- *non passa al judge:* Fonte challenge map, N-05 - Gravita media - judge si

### C.8 [issue: N-06] [tipo: assenza]

- **Verifica** il deliverable non segnala come profilo di rischio il rinvio o rinnovo tacito del contratto previsto dalla clausola 2.2.
- **Fail se** il rinnovo tacito del contratto compare fra i profili di rischio o fra i punti controversi.
- **Indifferente** la menzione del rinnovo tacito nella descrizione del rapporto.
- *non passa al judge:* Fonte challenge map, N-06 - Gravita media - judge si

### C.9 [issue: X-01] [tipo: assenza]

- **Verifica** simmetria del controllo: il deliverable non tratta come provati i resi dell'opponente mentre tratta come da provare le contestazioni di qualita.
- **Fail se** i resi sono dati per provati e nello stesso deliverable le contestazioni di qualità sono dichiarate da provare.
- **Indifferente** l'ordine in cui i due punti sono trattati.
- *non passa al judge:* Fonte PEC del 3 aprile 2031; clausole 9.1 e 10.1 del contratto - Gravita alta - judge si

### C.10 [issue: X-02] [tipo: assenza]

- **Verifica** divieto di presunzione dell'esito: il deliverable non afferma che il decreto sarà revocato.
- **Fail se** compare l'affermazione che il decreto sarà revocato, integralmente o in parte.
- **Indifferente** l'indicazione degli importi per i quali la revoca è sostenuta dai documenti.
- *non passa al judge:* Fonte composizione del fascicolo - Gravita alta - judge si

### C.11 [issue: X-03] [tipo: assenza]

- **Verifica** sovra-segnalazione: il deliverable non presenta come profilo di rischio il deposito del ricorso per decreto ingiuntivo del 28 aprile 2031.
- **Fail se** il deposito del ricorso compare fra i profili di rischio o fra le irregolarità della fase monitoria.
- **Indifferente** la menzione del deposito nella cronologia.
- *non passa al judge:* Fonte decreto ingiuntivo - Gravita media - judge si
