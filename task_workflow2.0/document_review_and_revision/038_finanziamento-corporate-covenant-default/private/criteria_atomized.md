# WF2-038 — Criteri atomizzati

> È ciò che viene somministrato al judge e alla verifica meccanica. Forma a campi, convenzione atomo v1.
>
> `required` = gravità alta; media e bassa = `optional`. Il campo `issue` porta l'identificativo della rubrica in prosa (`evaluation_criteria.md`). Ciò che segue la riga di separazione non passa al judge.
>
> **Inquadramento.** Il deliverable è la nota di rilievi resa nell'interesse di Mareggia Estrusi S.p.A., società finanziata, alla data di riferimento di giovedì 15 aprile 2032. Il contratto di finanziamento è in essere; l'ultimo certificato di conformità è stato consegnato il 26 marzo 2032; nessuna dichiarazione di decadenza, risoluzione o recesso è stata ricevuta; l'operazione societaria descritta nel term sheet non è perfezionata.

---


## A. FORMA DELL'OUTPUT

**A.1 sezioni obbligatorie**
`issue: - · tipo: valore · gravità: alta · judge: no · fonte: response_template.md`
Verifica: Il deliverable è un solo file markdown denominato review_memo.md, non superiore a 2.600 parole, e contiene una sintesi, una tabella dei rilievi in ordine di priorità, una sezione sulla posizione alla data di riferimento, una sezione su indici importi e scadenze con il calcolo, una sezione su ciò che non è un rilievo, una sezione su ciò che manca dal fascicolo e la risposta al consiglio.
Pass se: tutte e sette le parti sono presenti e distinte e il conteggio delle parole non supera 2.600.
Fail se: manca una delle sette parti, oppure due di esse non sono distinte, oppure il conteggio delle parole supera 2.600.

**A.2 tabella dei rilievi**
`issue: - · tipo: struttura · gravità: alta · judge: no · fonte: response_template.md`
Verifica: I rilievi sono resi in forma di tabella e ciascuna riga indica il rilievo, la clausola o il documento da cui deriva, la qualificazione, il termine e l'azione.
Pass se: la tabella è presente e ogni riga porta i cinque dati.
Fail se: i rilievi non sono in forma di tabella, oppure almeno una riga è priva di uno dei cinque dati.

**A.3 qualificazione di ciascun rilievo**
`issue: - · tipo: presenza · gravità: alta · judge: no · fonte: response_template.md`
Verifica: Ogni riga della tabella dei rilievi porta una fra queste quattro qualificazioni: violazione di un impegno, evento di default, conseguenza potenziale, adempimento in scadenza.
Pass se: ogni riga porta una delle quattro qualificazioni.
Fail se: almeno una riga è priva della qualificazione, oppure si usa una scala che non distingue la violazione dall'evento di default.

**A.4 nessuna riscrittura di clausole**
`issue: - · tipo: assenza · gravità: alta · judge: no · fonte: prompt`
Verifica: Il deliverable non contiene testo redatto in forma di clausola contrattuale, di bozza di lettera o di bozza di atto modificativo.
Pass se: non compare testo in forma di clausola o di atto da sottoscrivere.
Fail se: il deliverable contiene una clausola riscritta, una bozza di lettera o una bozza di atto.

**A.5 fonti nell'elenco chiuso**
`issue: - · tipo: assenza · gravità: alta · judge: no · fonte: public/02_reference_pack.md`
Verifica: Il deliverable non contiene riferimenti normativi estranei all'elenco chiuso delle fonti del reference pack.
Pass se: ogni riferimento normativo citato appartiene all'elenco.
Fail se: compare almeno un riferimento normativo fuori elenco.


## B. MERITO

**B.1 limite applicabile alla Data di Verifica**
`issue: I-01 · tipo: valore · gravità: alta · judge: no · fonte: Atto Modificativo n. 1, art. 3.1`
Verifica: Il deliverable indica 3,90x come limite di Leva Finanziaria applicabile alla Data di Verifica del 31 dicembre 2031.
Pass se: compare 3,90x, o 3,9x, riferito al limite di quella Data di Verifica.
Fail se: compare un limite diverso da 3,90x riferito a quella Data di Verifica, oppure il limite non compare.

**B.2 fonte del limite applicabile**
`issue: I-01 · tipo: attribuzione · gravità: alta · judge: sì · fonte: Atto Modificativo n. 1, art. 3.1`
Verifica: Il deliverable riconduce il limite di 3,90x all'atto modificativo del 12 marzo 2031 e non al contratto originario.
Pass se: il limite di 3,90x è ricondotto all'atto modificativo, all'atto modificativo n. 1 o alla modifica del marzo 2031.
Fail se: il limite di 3,90x è ricondotto al contratto originario, oppure non è ricondotto ad alcuna fonte.
Indifferente: la citazione del numero di articolo.

**B.3 limite originario non applicabile a quella data**
`issue: I-01 · tipo: assenza · gravità: alta · judge: sì · fonte: contratto, art. 13.5, lett. A`
Verifica: Il deliverable non indica 3,50x come limite di Leva Finanziaria applicabile alla Data di Verifica del 31 dicembre 2031.
Pass se: 3,50x non compare come limite di quella Data di Verifica.
Fail se: 3,50x è indicato come limite applicabile alla Data di Verifica del 31 dicembre 2031.
Indifferente: la menzione di 3,50x come limite che tornerà applicabile dal 30 giugno 2032.

**B.4 finanziamento soci non postergato**
`issue: I-02 · tipo: presenza · gravità: alta · judge: sì · fonte: Atto di Postergazione, artt. 2 e 6 e Allegato A`
Verifica: Il deliverable afferma che il finanziamento soci del 26 novembre 2031, di 7.830.000 euro, non è postergato ai sensi dell'atto di postergazione.
Pass se: compare l'affermazione che quel finanziamento non è postergato, non è coperto dall'atto di postergazione o non rientra fra i crediti postergati.
Fail se: il finanziamento è trattato come postergato, oppure l'affermazione non compare.

**B.5 ragione della mancata postergazione**
`issue: I-02 · tipo: attribuzione · gravità: alta · judge: sì · fonte: Atto di Postergazione, art. 6`
Verifica: Il deliverable riconduce la mancata postergazione all'assenza dell'atto di adesione previsto per i crediti sorti dopo l'atto di postergazione.
Pass se: compare il riferimento all'atto di adesione mancante, alla mancata estensione della postergazione ai crediti successivi o al fatto che il credito non figura nell'elenco allegato.
Fail se: la mancata postergazione è ricondotta ad altra ragione, oppure non è motivata.

**B.6 inclusione nell'Indebitamento Finanziario Netto**
`issue: I-02 · tipo: presenza · gravità: alta · judge: sì · fonte: contratto, def. Indebitamento Finanziario Netto, lett. e`
Verifica: Il deliverable afferma che quel finanziamento soci rientra nell'Indebitamento Finanziario Netto ai fini del calcolo dell'indice.
Pass se: compare l'affermazione che l'importo va incluso, computato o aggiunto nell'Indebitamento Finanziario Netto.
Fail se: l'importo resta escluso dall'Indebitamento Finanziario Netto, oppure l'affermazione non compare.

**B.7 Indebitamento Finanziario Netto ricalcolato**
`issue: I-03 · tipo: valore · gravità: alta · judge: no · fonte: prospetto covenant; contratto, def. Indebitamento Finanziario Netto`
Verifica: Il deliverable indica 57.420.000 euro come Indebitamento Finanziario Netto al 31 dicembre 2031.
Pass se: compare l'importo di 57.420.000 euro.
Fail se: compare un importo diverso, oppure l'importo non compare.

**B.8 Leva Finanziaria ricalcolata**
`issue: I-03 · tipo: valore · gravità: alta · judge: no · fonte: 57.420.000 / 14.500.000`
Verifica: Il deliverable indica 3,96x come Leva Finanziaria al 31 dicembre 2031.
Pass se: compare 3,96x o 3,96.
Fail se: compare un valore diverso, oppure il valore non compare.

**B.9 qualificazione del superamento**
`issue: I-03 · tipo: qualificazione · gravità: alta · judge: sì · fonte: contratto, art. 13.5, lett. A`
Verifica: Il deliverable qualifica il superamento del limite di Leva Finanziaria come violazione di un impegno finanziario del contratto.
Pass se: compare, riferita a quel superamento, una fra: «violazione dell'impegno finanziario», «violazione del covenant», «mancato rispetto dell'impegno finanziario», «inadempimento dell'impegno finanziario».
Fail se: il superamento non è qualificato, oppure è qualificato direttamente come evento di default.

**B.10 assenza di evento di default alla data di riferimento**
`issue: I-04 · tipo: presenza · gravità: alta · judge: sì · fonte: contratto, art. 14.2, lett. D, come sostituito`
Verifica: Il deliverable afferma che alla data di riferimento la violazione dell'impegno sulla Leva Finanziaria non integra ancora un evento di default.
Pass se: compare l'affermazione che l'evento di default non si è ancora verificato, non è ancora maturato o non sussiste alla data di riferimento.
Fail se: l'affermazione non compare, oppure si afferma che l'evento di default sussiste già.

**B.11 scadenza del termine di rimedio**
`issue: I-04 · tipo: valore · gravità: alta · judge: no · fonte: 20 Giorni Lavorativi dal 26 marzo 2032; art. 13.10, lett. b`
Verifica: Il deliverable indica il 26 aprile 2032 come data di scadenza del termine entro il quale la violazione può essere rimediata.
Pass se: compare la data del 26 aprile 2032.
Fail se: compare una data diversa, oppure la data non compare.

**B.12 momento in cui l'evento di default si produce**
`issue: I-04 · tipo: presenza · gravità: alta · judge: sì · fonte: contratto, art. 14.2, lett. D`
Verifica: Il deliverable afferma che l'evento di default si produrrà alla scadenza del termine di rimedio se il rimedio non interviene.
Pass se: compare l'affermazione che l'evento di default matura, sorge o si verifica alla scadenza di quel termine.
Fail se: l'affermazione non compare, oppure l'evento di default è collocato alla Data di Verifica o alla data di consegna del certificato.

**B.13 divieto di anticipare l'evento di default**
`issue: I-04 · tipo: assenza · gravità: alta · judge: sì · fonte: contratto, art. 14.2`
Verifica: Il deliverable non afferma che la società si trovi già in evento di default alla data di riferimento.
Pass se: non compare l'affermazione che la società è in default, in evento di default o in inadempimento risolutivo alla data di riferimento.
Fail se: compare l'affermazione che la società si trova già in evento di default.

**B.14 rimedio non esercitabile**
`issue: I-05 · tipo: presenza · gravità: alta · judge: sì · fonte: art. 13.10, lett. c`
Verifica: Il deliverable afferma che il rimedio in conto capitale non può essere esercitato per la Data di Verifica del 31 dicembre 2031.
Pass se: compare l'affermazione che il rimedio non è esercitabile, non è disponibile o è precluso per quella Data di Verifica.
Fail se: l'affermazione non compare, oppure il rimedio è presentato come esercitabile.

**B.15 ragione della preclusione**
`issue: I-05 · tipo: attribuzione · gravità: alta · judge: sì · fonte: art. 13.10, lett. c`
Verifica: Il deliverable riconduce la preclusione al divieto di esercitare il rimedio a due Date di Verifica consecutive.
Pass se: compare il riferimento al divieto di esercizio a due Date di Verifica consecutive o a due verifiche successive.
Fail se: la preclusione è ricondotta ad altra ragione, oppure non è motivata.

**B.16 esercizio precedente del rimedio**
`issue: I-05 · tipo: presenza · gravità: alta · judge: sì · fonte: lettera dell'Agente, punto 2; verbale del consiglio, terzo punto`
Verifica: Il deliverable afferma che il rimedio è già stato esercitato con riferimento alla Data di Verifica del 30 giugno 2031.
Pass se: compare l'affermazione che il rimedio è stato usato, esercitato o attivato per la Data di Verifica del 30 giugno 2031.
Fail se: l'affermazione non compare, oppure l'esercizio precedente è collocato a una diversa Data di Verifica.

**B.17 rimedio non proposto come azione**
`issue: I-05 · tipo: assenza · gravità: alta · judge: sì · fonte: art. 13.10, lett. c`
Verifica: Il deliverable non indica l'esercizio del rimedio in conto capitale fra le azioni che la società può compiere per evitare l'evento di default.
Pass se: il rimedio in conto capitale, il versamento in conto capitale o l'aumento di capitale a titolo di rimedio non compaiono fra le azioni proposte.
Fail se: il rimedio in conto capitale è indicato fra le azioni che la società può compiere.
Indifferente: la menzione del rimedio nella descrizione della clausola o della storia del rapporto.

**B.18 dichiarazione dell'Agente necessaria**
`issue: I-06 · tipo: presenza · gravità: alta · judge: sì · fonte: contratto, artt. 14.1 lett. B, 14.2 e 14.4`
Verifica: Il deliverable afferma che la decadenza dal beneficio del termine, la risoluzione e il recesso richiedono una dichiarazione dell'agente.
Pass se: compare l'affermazione che occorre una dichiarazione, una comunicazione o una lettera dell'agente perché la conseguenza si produca.
Fail se: l'affermazione non compare.

**B.19 istruzione della maggioranza**
`issue: I-06 · tipo: presenza · gravità: alta · judge: sì · fonte: contratto, artt. 14.2 e 18.2`
Verifica: Il deliverable afferma che l'agente agisce su istruzione della maggioranza delle banche finanziatrici.
Pass se: compare il riferimento all'istruzione della maggioranza delle banche, della maggioranza delle parti finanziatrici o della maggioranza del pool.
Fail se: l'affermazione non compare, oppure si afferma che l'agente può agire da solo o che una singola banca può attivare la conseguenza.

**B.20 momento di efficacia della dichiarazione**
`issue: I-06 · tipo: valore · gravità: media · judge: no · fonte: contratto, art. 14.1, lett. B`
Verifica: Il deliverable indica il quindicesimo Giorno Lavorativo successivo al ricevimento come momento dal quale la dichiarazione produce effetto.
Pass se: compare l'espressione «quindicesimo Giorno Lavorativo» oppure «15 Giorni Lavorativi» riferita all'efficacia della dichiarazione.
Fail se: compare un termine diverso, oppure il termine non compare.

**B.21 divieto di automatismo**
`issue: I-06 · tipo: assenza · gravità: alta · judge: sì · fonte: contratto, artt. 14.1 lett. B e 14.2`
Verifica: Il deliverable non afferma che la decadenza dal beneficio del termine o la risoluzione operino automaticamente o di diritto senza una dichiarazione dell'agente.
Pass se: non compare l'affermazione che la conseguenza si produce automaticamente, di diritto o senza necessità di comunicazione.
Fail se: compare l'affermazione che la decadenza o la risoluzione operano senza dichiarazione.

**B.22 partecipazione indiretta risultante**
`issue: I-07 · tipo: valore · gravità: alta · judge: no · fonte: 55% x 78%; contratto, def. Cambio di Controllo, lett. a`
Verifica: Il deliverable indica 42,9% come partecipazione indiretta che la controllante deterrebbe nella società all'esito dell'operazione.
Pass se: compare il valore 42,9% o 42,90%.
Fail se: compare un valore diverso, oppure il valore non compare.

**B.23 l'operazione integra un Cambio di Controllo**
`issue: I-07 · tipo: qualificazione · gravità: alta · judge: sì · fonte: contratto, def. Cambio di Controllo, lett. a; term sheet, punti 2.2 e 3.2`
Verifica: Il deliverable qualifica l'operazione descritta nel term sheet come cambio di controllo ai sensi della definizione contrattuale.
Pass se: compare, riferita a quell'operazione, una fra: «cambio di controllo», «change of control», «ricorre la fattispecie del cambio di controllo».
Fail se: l'operazione non è qualificata, oppure è qualificata come non integrante un cambio di controllo.

**B.24 il permanere del controllo non esclude la fattispecie**
`issue: I-07 · tipo: assenza · gravità: alta · judge: sì · fonte: contratto, def. Cambio di Controllo, lett. a`
Verifica: Il deliverable non afferma che il cambio di controllo non ricorre perché la controllante continua a controllare la società di nuova costituzione.
Pass se: non compare l'affermazione che il mantenimento del controllo sulla catena societaria esclude il cambio di controllo.
Fail se: compare l'affermazione che il cambio di controllo non ricorre in quanto la controllante mantiene il controllo.

**B.25 carve-out non applicabile**
`issue: I-08 · tipo: presenza · gravità: alta · judge: sì · fonte: contratto, def. Riorganizzazione Consentita, lett. i; term sheet, punto 3.2`
Verifica: Il deliverable afferma che l'esenzione prevista per le riorganizzazioni consentite non si applica perché la società di nuova costituzione non è interamente controllata dalla controllante.
Pass se: compare l'affermazione che il requisito della società interamente controllata non è soddisfatto, o che il cessionario non è interamente controllato.
Fail se: l'affermazione non compare, oppure l'operazione è ricondotta all'esenzione.

**B.26 preavviso richiesto dal carve-out**
`issue: I-08 · tipo: valore · gravità: media · judge: no · fonte: contratto, def. Riorganizzazione Consentita, lett. ii`
Verifica: Il deliverable indica 20 Giorni Lavorativi come preavviso che l'esenzione richiede di dare all'agente prima del perfezionamento.
Pass se: compare «20 Giorni Lavorativi» o «venti Giorni Lavorativi» riferito al preavviso.
Fail se: compare un termine diverso, oppure il termine non compare.

**B.27 conseguenza del Cambio di Controllo**
`issue: I-09 · tipo: qualificazione · gravità: alta · judge: sì · fonte: contratto, art. 9.2, lett. A`
Verifica: Il deliverable qualifica la conseguenza del cambio di controllo come diritto di ciascuna banca, esercitabile individualmente, di ottenere il rimborso della propria quota.
Pass se: compare l'affermazione che il diritto spetta a ciascuna banca singolarmente, individualmente o pro quota.
Fail se: la conseguenza è presentata come rimborso automatico dell'intero finanziamento, oppure come decisione collettiva del pool, oppure non è qualificata.

**B.28 il Cambio di Controllo non è evento di default**
`issue: I-09 · tipo: assenza · gravità: alta · judge: sì · fonte: contratto, artt. 9.2 e 14`
Verifica: Il deliverable non qualifica il cambio di controllo come evento di default o come causa di risoluzione del contratto.
Pass se: il cambio di controllo non compare fra gli eventi di default o fra le cause di risoluzione.
Fail se: il cambio di controllo è qualificato come evento di default, come causa di risoluzione o come causa di recesso.

**B.29 termine per la comunicazione del Cambio di Controllo**
`issue: I-09 · tipo: valore · gravità: media · judge: no · fonte: contratto, art. 9.2, lett. B`
Verifica: Il deliverable indica 5 Giorni Lavorativi dal perfezionamento dell'operazione come termine entro cui la società deve comunicare il cambio di controllo all'agente.
Pass se: compare «5 Giorni Lavorativi» o «cinque Giorni Lavorativi» riferito a quella comunicazione.
Fail se: compare un termine diverso, oppure il termine non compare.

**B.30 termine scaduto per la comunicazione della dismissione**
`issue: I-10 · tipo: valore · gravità: alta · judge: no · fonte: 10 Giorni Lavorativi dal 5 febbraio 2032; contratto, art. 9.1, lett. B`
Verifica: Il deliverable indica il 19 febbraio 2032 come data entro cui la cessione dell'immobile andava comunicata all'agente.
Pass se: compare la data del 19 febbraio 2032.
Fail se: compare una data diversa, oppure la data non compare.

**B.31 comunicazione non effettuata**
`issue: I-10 · tipo: presenza · gravità: alta · judge: sì · fonte: verbale del consiglio, secondo punto; assenza di riscontro nel fascicolo`
Verifica: Il deliverable afferma che nel fascicolo non risulta la comunicazione della cessione dell'immobile all'agente.
Pass se: compare l'affermazione che la comunicazione non risulta, non è documentata o non è stata effettuata.
Fail se: l'affermazione non compare, oppure si afferma che la comunicazione è stata effettuata.

**B.32 qualificazione dell'omessa comunicazione**
`issue: I-10 · tipo: qualificazione · gravità: media · judge: sì · fonte: contratto, artt. 9.1 lett. B, 13.6 e 14.2 lett. C`
Verifica: Il deliverable qualifica l'omessa comunicazione come inadempimento di un obbligo del contratto.
Pass se: compare, riferita all'omissione, una fra: «inadempimento», «violazione di un impegno», «violazione di un obbligo informativo».
Fail se: l'omissione non è qualificata, oppure è presentata come irregolarità priva di conseguenze.

**B.33 termine per il reinvestimento**
`issue: I-11 · tipo: valore · gravità: media · judge: no · fonte: 12 mesi dal 5 febbraio 2032; contratto, art. 9.1, lett. C`
Verifica: Il deliverable indica il 5 febbraio 2033 come termine entro cui il corrispettivo della cessione deve essere reinvestito.
Pass se: compare la data del 5 febbraio 2033.
Fail se: compare una data diversa, oppure la data non compare.

**B.34 condizione per evitare il rimborso anticipato**
`issue: I-11 · tipo: presenza · gravità: alta · judge: sì · fonte: contratto, art. 9.1, lett. C`
Verifica: Il deliverable afferma che l'obbligo di rimborso anticipato è escluso soltanto se il corrispettivo è reinvestito nel termine e il reinvestimento è dimostrato all'agente.
Pass se: compare l'affermazione che serve il reinvestimento nel termine e la sua dimostrazione documentale all'agente.
Fail se: l'affermazione non compare, oppure la delibera del consiglio che destina il ricavato agli investimenti è presentata come atto che di per sé esclude l'obbligo.

**B.35 importo massimo garantito richiesto**
`issue: I-12 · tipo: valore · gravità: alta · judge: no · fonte: 50% di 60.000.000; contratto, art. 5.3; Atto Modificativo n. 1, art. 2.2`
Verifica: Il deliverable indica 30.000.000 euro come importo massimo garantito che la fideiussione deve avere dopo l'aumento dell'importo totale.
Pass se: compare l'importo di 30.000.000 euro.
Fail se: compare un importo diverso, oppure l'importo non compare.

**B.36 misura della scopertura**
`issue: I-12 · tipo: valore · gravità: alta · judge: no · fonte: 30.000.000 - 25.000.000`
Verifica: Il deliverable indica 5.000.000 euro come differenza fra l'importo massimo garantito richiesto e quello della fideiussione in essere.
Pass se: compare l'importo di 5.000.000 euro.
Fail se: compare un importo diverso, oppure l'importo non compare.

**B.37 qualificazione della scopertura**
`issue: I-12 · tipo: qualificazione · gravità: alta · judge: sì · fonte: contratto, artt. 5.3 e 13.9`
Verifica: Il deliverable qualifica la scopertura della fideiussione come inadempimento dell'impegno di mantenimento delle garanzie.
Pass se: compare, riferita alla scopertura, una fra: «inadempimento dell'impegno», «violazione dell'impegno di mantenimento delle garanzie», «violazione dell'obbligo di mantenere la garanzia al livello previsto».
Fail se: la scopertura non è qualificata, oppure è presentata come questione da negoziare senza indicare che il contratto è già violato.

**B.38 termine per prorogare o sostituire la garanzia**
`issue: I-13 · tipo: valore · gravità: media · judge: no · fonte: 90 giorni prima del 31 dicembre 2034; contratto, art. 13.9`
Verifica: Il deliverable indica il 2 ottobre 2034 come termine entro cui la fideiussione deve essere prorogata o sostituita.
Pass se: compare la data del 2 ottobre 2034.
Fail se: compare una data diversa, oppure la data non compare.

**B.39 scopertura temporale della garanzia**
`issue: I-13 · tipo: presenza · gravità: media · judge: sì · fonte: fideiussione, art. 6.1; contratto, art. 4.1`
Verifica: Il deliverable afferma che la fideiussione cessa di essere efficace prima della scadenza finale del finanziamento.
Pass se: compare l'affermazione che la garanzia scade prima del finanziamento, che copre solo una parte della durata o che resta un periodo scoperto.
Fail se: l'affermazione non compare, oppure si afferma che la garanzia copre l'intera durata.

**B.40 assenza di cross-default alla data di riferimento**
`issue: I-14 · tipo: presenza · gravità: alta · judge: sì · fonte: contratto, art. 14.3, lett. A; diffida, punti 2 e 3`
Verifica: Il deliverable afferma che alla data di riferimento la posizione verso il locatore finanziario non integra il presupposto del recesso per inadempimento verso altri finanziatori.
Pass se: compare l'affermazione che il cross-default non è maturato, non si è verificato o non sussiste alla data di riferimento.
Fail se: l'affermazione non compare, oppure si afferma che il cross-default è già maturato.

**B.41 scadenza del termine della diffida**
`issue: I-14 · tipo: valore · gravità: alta · judge: no · fonte: 15 giorni dal 1 aprile 2032; diffida, punto 3`
Verifica: Il deliverable indica il 16 aprile 2032 come data di scadenza del termine assegnato dalla diffida del locatore.
Pass se: compare la data del 16 aprile 2032.
Fail se: compare una data diversa, oppure la data non compare.

**B.42 conseguenza della risoluzione del leasing**
`issue: I-14 · tipo: presenza · gravità: alta · judge: sì · fonte: diffida, punto 4; contratto, art. 14.3, lett. A`
Verifica: Il deliverable afferma che la risoluzione del contratto di locazione finanziaria renderebbe esigibile un importo superiore alla soglia di rilevanza prevista dal contratto di finanziamento.
Pass se: compare l'affermazione che, risolto il leasing, l'importo esigibile supera la soglia oltre la quale scatta il presupposto del recesso.
Fail se: l'affermazione non compare, oppure si afferma che l'importo resterebbe sotto la soglia.

**B.43 priorità dell'adempimento più ravvicinato**
`issue: I-14 · tipo: presenza · gravità: alta · judge: sì · fonte: diffida, punto 3`
Verifica: Il deliverable colloca il pagamento dell'insoluto verso il locatore fra le azioni con la scadenza più ravvicinata rispetto alla data di riferimento.
Pass se: il pagamento dell'insoluto compare fra le azioni da compiere e il relativo termine è indicato come il primo a scadere.
Fail se: l'azione non compare, oppure è collocata dopo adempimenti con scadenza successiva.
Indifferente: la posizione della riga nella tabella, purché il termine sia indicato come il primo a scadere.

**B.44 la lettera dell'Agente riserva i diritti**
`issue: I-15 · tipo: presenza · gravità: media · judge: sì · fonte: lettera dell'Agente, punto 5; contratto, art. 14.5`
Verifica: Il deliverable afferma che la lettera dell'agente non contiene alcuna rinuncia e riserva espressamente i diritti delle banche.
Pass se: compare l'affermazione che la lettera riserva i diritti, non costituisce rinuncia o non produce effetti di tolleranza.
Fail se: l'affermazione non compare.

**B.45 divieto di leggere la lettera come rinuncia**
`issue: I-15 · tipo: assenza · gravità: alta · judge: sì · fonte: lettera dell'Agente, punto 5`
Verifica: Il deliverable non presenta la lettera dell'agente come rinuncia, consenso, tolleranza o accettazione della posizione della società.
Pass se: non compare l'affermazione che l'agente ha rinunciato, ha acconsentito, ha tollerato o ha accettato.
Fail se: compare l'affermazione che la lettera vale come rinuncia, consenso o tolleranza.

**B.46 atto di adesione mancante**
`issue: I-16 · tipo: presenza · gravità: alta · judge: sì · fonte: Atto di Postergazione, art. 6 e Allegato B`
Verifica: Il deliverable indica fra gli elementi mancanti l'atto di adesione con cui il socio avrebbe potuto sottoporre alla postergazione il finanziamento del 26 novembre 2031.
Pass se: compare l'indicazione che quell'atto di adesione manca o non risulta nel fascicolo.
Fail se: l'indicazione non compare.

**B.47 relazione di revisione mancante**
`issue: I-16 · tipo: presenza · gravità: media · judge: sì · fonte: verbale del consiglio, primo punto; lettera dell'Agente, punto 4`
Verifica: Il deliverable indica fra gli elementi mancanti la relazione del soggetto incaricato della revisione legale sul bilancio consolidato al 31 dicembre 2031.
Pass se: compare l'indicazione che la relazione di revisione manca, non è ancora emessa o non è nel fascicolo.
Fail se: l'indicazione non compare.

**B.48 contratto di leasing mancante**
`issue: I-16 · tipo: presenza · gravità: media · judge: sì · fonte: diffida, punti 1 e 4`
Verifica: Il deliverable indica fra gli elementi mancanti il contratto di locazione finanziaria con il locatore che ha inviato la diffida.
Pass se: compare l'indicazione che il contratto di locazione finanziaria non è nel fascicolo.
Fail se: l'indicazione non compare.

**B.49 divieto di prudenza paralizzante**
`issue: I-16 · tipo: assenza · gravità: alta · judge: sì · fonte: prospetto covenant; Atto di Postergazione`
Verifica: Il deliverable non afferma che la posizione sugli impegni finanziari non sia determinabile sulla base del fascicolo.
Pass se: non compare l'affermazione che l'indice non è determinabile, che occorre attendere il bilancio certificato per pronunciarsi o che non è possibile concludere.
Fail se: compare l'affermazione che la posizione sugli impegni finanziari non è determinabile.

**B.50 facoltà di sostituire la banca non è un rischio**
`issue: N-06 · tipo: assenza · gravità: media · judge: sì · fonte: contratto, art. 20.4`
Verifica: Il deliverable non presenta come rischio per la società la facoltà di designare un istituto sostitutivo della banca non consenziente o inadempiente.
Pass se: quella facoltà non compare fra i rilievi o fra i rischi.
Fail se: la facoltà è presentata come rischio, come clausola sfavorevole o come criticità.

**B.51 l'aumento del margine è pattuito**
`issue: N-05 · tipo: assenza · gravità: media · judge: sì · fonte: Atto Modificativo n. 1, art. 6.1; contratto, art. 19.2`
Verifica: Il deliverable non presenta l'aumento del margine da 215 a 260 punti base come modifica imposta unilateralmente dalle banche.
Pass se: l'aumento del margine non è descritto come unilaterale, imposto o non concordato.
Fail se: l'aumento del margine è presentato come modifica unilaterale o come imposizione.

**B.52 il DSCR non è violato**
`issue: N-01 · tipo: assenza · gravità: alta · judge: sì · fonte: prospetto covenant; contratto, art. 13.5, lett. B`
Verifica: Il deliverable non afferma che l'impegno sul DSCR alla Data di Verifica del 31 dicembre 2031 sia violato.
Pass se: non compare l'affermazione che il DSCR è al di sotto del limite o che l'impegno sul DSCR non è rispettato.
Fail se: compare l'affermazione che il DSCR viola il limite contrattuale.

**B.53 la fideiussione non è invalida**
`issue: N-02 · tipo: assenza · gravità: alta · judge: sì · fonte: fideiussione, art. 2.1`
Verifica: Il deliverable non afferma che la fideiussione sia nulla o invalida per mancata indicazione dell'importo massimo garantito.
Pass se: non compare l'affermazione di nullità o invalidità della fideiussione.
Fail se: compare l'affermazione che la fideiussione è nulla, invalida o inefficace per quel motivo.

**B.54 nessun rischio di decadenza del creditore**
`issue: N-03 · tipo: assenza · gravità: media · judge: sì · fonte: fideiussione, art. 5.1`
Verifica: Il deliverable non segnala come rischio la decadenza del creditore per mancato esercizio delle istanze contro il debitore nel termine di legge.
Pass se: quel rischio non compare fra i rilievi.
Fail se: il rischio di decadenza per mancato esercizio delle istanze è segnalato come rilievo.

**B.55 l'insoluto non è cross-default**
`issue: N-04 · tipo: assenza · gravità: alta · judge: sì · fonte: diffida, punto 2; contratto, art. 14.3, lett. A`
Verifica: Il deliverable non afferma che i canoni scaduti verso il locatore, per il loro ammontare, integrino il presupposto del recesso per inadempimento verso altri finanziatori.
Pass se: non compare l'affermazione che l'importo dei canoni scaduti supera la soglia di rilevanza.
Fail se: compare l'affermazione che i canoni scaduti superano la soglia o integrano il cross-default.

**B.56 la sostituzione del consigliere non è un rilievo**
`issue: N-09 · tipo: assenza · gravità: media · judge: sì · fonte: verbale del consiglio, quinto punto`
Verifica: Il deliverable non presenta la sostituzione del consigliere deliberata dal consiglio come rilievo o come evento da comunicare alle banche.
Pass se: la sostituzione del consigliere non compare fra i rilievi.
Fail se: la sostituzione del consigliere è presentata come rilievo, come rischio o come evento da comunicare.

**B.57 il rimborso anticipato volontario non è un onere**
`issue: N-07 · tipo: assenza · gravità: bassa · judge: sì · fonte: contratto, art. 8.1`
Verifica: Il deliverable non presenta come onere per la società il compenso per rimborso anticipato volontario.
Pass se: il compenso per rimborso anticipato volontario non compare fra i rilievi o fra i costi da sostenere.
Fail se: il compenso è presentato come onere attuale o come rischio.

**B.58 l'approvazione specifica è presente**
`issue: N-08 · tipo: assenza · gravità: bassa · judge: sì · fonte: contratto, blocco di approvazione in calce`
Verifica: Il deliverable non segnala come mancante o irregolare l'approvazione specifica per iscritto delle clausole in calce al contratto.
Pass se: non compare un rilievo sulla mancanza o sull'irregolarità dell'approvazione specifica.
Fail se: compare un rilievo che indica l'approvazione specifica come mancante o irregolare.

**B.59 divieto di presumere la rinuncia**
`issue: I-18 · tipo: assenza · gravità: alta · judge: sì · fonte: -`
Verifica: Il deliverable non afferma che le banche concederanno una rinuncia o che accetteranno di non attivare i rimedi.
Pass se: non compare l'affermazione che la rinuncia sarà concessa o che le banche non agiranno.
Fail se: compare l'affermazione che la rinuncia sarà ottenuta o che le banche non attiveranno i rimedi.
Indifferente: l'indicazione della richiesta di rinuncia fra le azioni da compiere.

**B.60 divieto di presumere il perfezionamento**
`issue: I-18 · tipo: assenza · gravità: media · judge: sì · fonte: term sheet, punto 1 e punto 6`
Verifica: Il deliverable non afferma che l'operazione societaria descritta nel term sheet si perfezionerà.
Pass se: non compare l'affermazione che l'operazione si perfezionerà o che il cambio di controllo si è verificato.
Fail se: compare l'affermazione che l'operazione si perfezionerà o che il cambio di controllo è già avvenuto.

**B.61 simmetria sugli elementi neutri**
`issue: I-17 · tipo: assenza · gravità: media · judge: sì · fonte: verbale del consiglio, secondo punto`
Verifica: Il deliverable non presenta come rischio per la società la destinazione a investimenti del ricavato della cessione deliberata dal consiglio.
Pass se: la destinazione deliberata non compare fra i rischi.
Fail se: la destinazione deliberata è presentata come rischio in sé, indipendentemente dalla dimostrazione del reinvestimento.


## C. INDICI, DATE E VALORI CALCOLATI

**C.1 indice dichiarato nel certificato**
`issue: I-03 · tipo: valore · gravità: media · judge: no · fonte: certificato al 31 dicembre 2031, punto 2`
Verifica: Il deliverable indica 3,42x come Leva Finanziaria dichiarata nel certificato di conformità al 31 dicembre 2031.
Pass se: compare 3,42x o 3,42 riferito al dato dichiarato.
Fail se: compare un valore diverso, oppure il valore dichiarato non è riportato.

**C.2 origine della differenza fra i due indici**
`issue: I-03 · tipo: presenza · gravità: alta · judge: sì · fonte: prospetto covenant, riga 9`
Verifica: Il deliverable afferma che la differenza fra l'indice dichiarato e l'indice ricalcolato dipende dall'inclusione del finanziamento soci non postergato.
Pass se: compare l'affermazione che lo scostamento deriva dall'inclusione di quel finanziamento soci.
Fail se: l'affermazione non compare, oppure lo scostamento è ricondotto ad altra posta.

**C.3 regola applicata al limite**
`issue: I-01 · tipo: presenza · gravità: alta · judge: sì · fonte: Atto Modificativo n. 1, artt. 3.1 e 3.2`
Verifica: Il deliverable afferma che il limite di 3,90x vale per le sole Date di Verifica dell'anno 2031 e che dalla Data di Verifica del 30 giugno 2032 riprende applicazione la scaletta del contratto.
Pass se: compare l'affermazione che la deroga è limitata alle Date di Verifica del 2031 e che il limite contrattuale torna ad applicarsi dalla prima Data di Verifica del 2032.
Fail se: l'affermazione non compare, oppure la deroga è presentata come permanente.

**C.4 derivazione errata dell'indice**
`issue: I-03 · tipo: assenza · gravità: media · judge: sì · fonte: Atto di Postergazione, Allegato A`
Verifica: Il deliverable non presenta 3,96x come risultato di un calcolo che include nell'indebitamento i finanziamenti soci elencati nell'allegato dell'atto di postergazione.
Pass se: non compare l'affermazione che l'indice ricalcolato include anche i finanziamenti soci postergati.
Fail se: compare l'affermazione che l'indice ricalcolato include i finanziamenti soci postergati elencati nell'allegato.

**C.5 derivazione errata del termine di rimedio**
`issue: I-04 · tipo: assenza · gravità: media · judge: sì · fonte: art. 13.10, lett. b`
Verifica: Il deliverable non presenta il 26 aprile 2032 come risultato di un computo in giorni di calendario o come termine decorrente dalla Data di Verifica.
Pass se: non compare l'indicazione che il termine si computa in giorni di calendario o che decorre dal 31 dicembre 2031.
Fail se: il termine è presentato come 20 giorni di calendario, oppure come decorrente dalla Data di Verifica anziché dalla trasmissione del certificato.

**C.6 scostamento dal limite**
`issue: I-03 · tipo: valore · gravità: bassa · judge: no · fonte: 3,96 - 3,90`
Verifica: Il deliverable indica lo scostamento fra la Leva Finanziaria ricalcolata e il limite applicabile.
Pass se: compare il valore 0,06 riferito allo scostamento fra 3,96x e 3,90x.
Fail se: compare un valore diverso, oppure lo scostamento non è indicato.

---

**Conteggi.** 18 issue di merito, 9 controlled non-issue, 72 criteri atomici, di cui 51 al judge e 21 a verifica meccanica.
