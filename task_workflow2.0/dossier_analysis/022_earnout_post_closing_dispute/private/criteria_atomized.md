Convenzione atomo v1. required = gravità alta; media e bassa = optional.
Inquadramento: WF2-022; fascicolo fotografato al 2029-07-09.
La base normativa è congelata al 25 agosto 2026 e coincide con il reference pack chiuso.

A. FORMA DELL'OUTPUT

A.1 sezioni obbligatorie del memo
issue: — · tipo: valore · gravità: alta · judge: no · fonte: response_template.md
Verifica: Il deliverable contiene una sezione con la conclusione sull'importo dovuto, una sezione di rilievi, una sezione su scadenze e importi, una sezione su ciò che manca dal fascicolo e una sezione sulle azioni possibili.
Pass se: tutte e cinque le sezioni sono presenti e distinte.
Fail se: manca una delle cinque sezioni, oppure due di esse non sono distinte.

A.2 rilievi in sequenza ordinata
issue: — · tipo: struttura · gravità: media · judge: no · fonte: prompt
Verifica: I rilievi sono presentati in sequenza ordinata.
Pass se: i rilievi sono numerati o elencati in sequenza.
Fail se: i rilievi non sono numerati né elencati in sequenza.

A.3 calcolo esposto per ogni importo e scadenza
issue: — · tipo: presenza · gravità: alta · judge: no · fonte: prompt
Verifica: Per ciascun importo e ciascuna data della sezione su scadenze e importi è riportato il calcolo seguito.
Pass se: ogni voce di quella sezione riporta il valore e il calcolo.
Fail se: una o più voci riportano il valore senza il calcolo.

A.4 ancoraggio al documento
issue: — · tipo: struttura · gravità: alta · judge: no · fonte: response_template.md
Verifica: Ogni affermazione del memo riporta il documento del fascicolo o la clausola da cui deriva.
Pass se: ogni voce contiene un riferimento a un documento del fascicolo o a un articolo del contratto.
Fail se: almeno una voce è priva di riferimento.

A.5 fonti nell'elenco chiuso
issue: — · tipo: assenza · gravità: alta · judge: no · fonte: reference pack
Verifica: Il deliverable non contiene riferimenti normativi estranei all'elenco chiuso delle fonti del reference pack.
Pass se: ogni riferimento normativo citato appartiene all'elenco.
Fail se: compare almeno un riferimento normativo fuori elenco.


B. MERITO

B. MERITO

B.1 costruzione dell'EBITDA
issue: I-01 · tipo: presenza · gravità: alta · judge: sì · fonte: contratto art. 1.2; bilancio, conto economico
Verifica: Il deliverable afferma che l'EBITDA si ottiene aggiungendo alla differenza fra valore e costi della produzione gli ammortamenti e le svalutazioni della voce 10 e gli accantonamenti delle voci 12 e 13.
Pass se: compare l'indicazione che alla differenza fra valore e costi della produzione si aggiungono gli ammortamenti e gli accantonamenti, oppure che l'EBITDA si ricostruisce sommando alla voce A-B la voce 10 e le voci 12 e 13.
Fail se: l'EBITDA è presentato come una voce leggibile dal bilancio, oppure il passaggio non compare.
Indifferente: l'ordine in cui i tre addendi sono presentati.

B.2 esclusione degli oneri di integrazione
issue: I-02 · tipo: presenza · gravità: alta · judge: sì · fonte: contratto art. 1.2, lett. (a) e (b); prospetto riga B.3; bilancio, nota integrativa alla voce B.7
Verifica: Il deliverable afferma che gli oneri connessi all'integrazione della società nel gruppo dell'acquirente vanno esclusi dal calcolo del parametro.
Pass se: compare l'affermazione che quegli oneri vanno esclusi, o riaggiunti, o non lasciati a conto economico, in forza della lettera (b), oppure in forza della lettera (a), oppure in forza della definizione contrattuale di EBITDA Rettificato
Fail se: l'affermazione non compare, oppure gli oneri sono lasciati nel calcolo
Indifferente: la lettera della definizione su cui l'esclusione è fondata

B.3 qualificazione come ricorrenti non recepita
issue: I-02 · tipo: assenza · gravità: alta · judge: sì · fonte: prospetto riga B.3; contratto art. 1.2, lett. (a) e (b)
Verifica: Il deliverable non recepisce la qualificazione degli oneri come costi ordinari e ricorrenti quale ragione per non applicare la rettifica.
Pass se: non compare l'affermazione che la rettifica non è dovuta, o non è applicabile, perché gli oneri sono costi di gestione ordinari e ricorrenti
Fail se: la riga B.3 del prospetto è confermata, oppure si afferma che la natura ricorrente degli oneri esclude la rettifica
Indifferente: il richiamo della lettera (a), della lettera (b) o di entrambe come fondamento dell'esclusione

B.4 ancoraggio degli oneri alla nota integrativa
issue: I-02 · tipo: attribuzione · gravità: alta · judge: sì · fonte: bilancio, nota integrativa alla voce B.7
Verifica: Il deliverable riconduce la descrizione degli oneri come connessi all'integrazione nel gruppo alla nota integrativa del bilancio.
Pass se: il rilievo è ancorato alla nota integrativa, o alla voce B.7 del bilancio, o ai costi per servizi del bilancio.
Fail se: il rilievo non è ancorato ad alcun documento, oppure è ancorato al solo prospetto dell'acquirente.

B.5 valorizzazione delle commesse ai prezzi verso terzi
issue: I-03 · tipo: presenza · gravità: alta · judge: sì · fonte: contratto art. 1.2, lett. (d)
Verifica: Il deliverable afferma che i ricavi delle commesse eseguite per società del gruppo dell'acquirente vanno valorizzati ai prezzi praticati a terzi indipendenti.
Pass se: compare l'affermazione che quelle commesse vanno valorizzate ai prezzi praticati a terzi indipendenti, oppure ai prezzi di listino, in luogo dei corrispettivi applicati.
Fail se: l'affermazione non compare.

B.6 ancoraggio dei due valori delle commesse
issue: I-03 · tipo: attribuzione · gravità: alta · judge: sì · fonte: verbale del consiglio, punto 2; bilancio, nota integrativa
Verifica: Il deliverable riconduce il valore a listino delle commesse al verbale del consiglio di amministrazione e il ricavo contabilizzato alla nota integrativa del bilancio.
Pass se: compaiono entrambi gli ancoraggi, anche in forma sintetica.
Fail se: manca uno dei due ancoraggi, oppure entrambi i valori sono attribuiti allo stesso documento.

B.7 l'accordo infragruppo non esclude la rettifica
issue: I-03 · tipo: assenza · gravità: alta · judge: sì · fonte: contratto art. 1.2, lett. (d); prospetto riga B.5
Verifica: Il deliverable non afferma che l'esistenza dell'accordo infragruppo di fornitura escluda la rettifica.
Pass se: quell'affermazione non compare.
Fail se: si afferma che, essendo le lavorazioni fatturate secondo l'accordo infragruppo, la rettifica non è dovuta.

B.8 corrispettivo dovuto nell'importo massimo
issue: I-04 · tipo: presenza · gravità: alta · judge: sì · fonte: contratto artt. 4.1 e 4.2
Verifica: Il deliverable afferma che il parametro supera la soglia superiore e che il corrispettivo variabile è dovuto nell'importo massimo, senza applicazione della formula proporzionale.
Pass se: compare l'affermazione che il parametro è pari o superiore alla soglia superiore e che spetta l'importo massimo.
Fail se: il corrispettivo è calcolato con la formula proporzionale, oppure l'affermazione non compare.

B.9 decorrenza del termine dal ricevimento
issue: I-05 · tipo: presenza · gravità: alta · judge: sì · fonte: contratto art. 4.4; PEC del 21 maggio 2029
Verifica: Il deliverable afferma che il termine di trenta giorni per la contestazione decorre dal ricevimento del prospetto e non dalla data del documento.
Pass se: compare l'affermazione che il termine decorre dal ricevimento, o dalla data della ricevuta di avvenuta consegna.
Fail se: il termine è fatto decorrere dalla data del prospetto, oppure la decorrenza non è indicata.

B.10 tempestività della contestazione
issue: I-05 · tipo: presenza · gravità: alta · judge: sì · fonte: contratto art. 4.4; PEC del 19 giugno 2029
Verifica: Il deliverable afferma che la contestazione è stata inviata nel termine.
Pass se: compare l'affermazione che la contestazione è tempestiva, o nel termine, o non tardiva.
Fail se: la contestazione è presentata come tardiva, oppure il venditore è dichiarato decaduto.

B.11 nomina unilaterale dell'esperto
issue: I-06 · tipo: presenza · gravità: alta · judge: sì · fonte: contratto art. 4.5; lettera di incarico del 2 luglio 2029
Verifica: Il deliverable afferma che l'esperto è stato nominato dal solo acquirente, mentre il contratto richiede la scelta congiunta o la designazione da parte del Presidente dell'Ordine.
Pass se: compare l'affermazione che la nomina è unilaterale e non conforme alla procedura dell'art. 4.5.
Fail se: l'affermazione non compare, oppure la nomina è presentata come conforme al contratto.

B.12 incarico anteriore alla finestra di trattativa
issue: I-06 · tipo: presenza · gravità: media · judge: sì · fonte: contratto art. 4.5; lettera di incarico del 2 luglio 2029
Verifica: Il deliverable afferma che l'incarico è stato conferito prima della scadenza del termine di trenta giorni entro il quale le parti dovevano tentare l'accordo.
Pass se: compare l'affermazione che l'incarico è anteriore alla scadenza di quel termine, o che è stato conferito prima che la finestra di trattativa fosse esaurita.
Fail se: l'affermazione non compare.

B.13 l'esperto è il revisore del gruppo
issue: I-06 · tipo: presenza · gravità: alta · judge: sì · fonte: lettera di incarico del 2 luglio 2029
Verifica: Il deliverable afferma che l'esperto incaricato è il revisore del bilancio consolidato del gruppo dell'acquirente.
Pass se: compare l'affermazione che l'incaricato ha svolto o svolge la revisione per il gruppo dell'acquirente, oppure che non è indipendente rispetto all'acquirente.
Fail se: l'affermazione non compare.

B.14 la determinazione non vincola il venditore
issue: I-06 · tipo: assenza · gravità: alta · judge: sì · fonte: contratto art. 4.5
Verifica: Il deliverable non afferma che la determinazione dell'esperto così nominato sia vincolante per il venditore.
Pass se: quell'affermazione non compare.
Fail se: si afferma che il venditore è vincolato alla determinazione dell'esperto nominato dall'acquirente.

B.15 natura della determinazione
issue: I-07 · tipo: qualificazione · gravità: media · judge: sì · fonte: contratto art. 4.5; art. 1349 c.c.
Verifica: Il deliverable qualifica la determinazione affidata al terzo come determinazione con equo apprezzamento e non rimessa al mero arbitrio.
Pass se: compare, riferita a quella determinazione, l'espressione «equo apprezzamento», oppure «arbitraggio», oppure l'affermazione che non è rimessa al mero arbitrio del terzo.
Fail se: la determinazione è qualificata come rimessa al mero arbitrio, oppure la qualificazione non compare.

B.16 impugnabilità della determinazione
issue: I-07 · tipo: assenza · gravità: media · judge: sì · fonte: art. 1349 c.c.
Verifica: Il deliverable non afferma che la determinazione del terzo sia impugnabile soltanto provando la mala fede del terzo.
Pass se: quell'affermazione non compare.
Fail se: si afferma che la determinazione è impugnabile solo provando la mala fede del terzo.

B.17 violazione del divieto di atti riduttivi
issue: I-08 · tipo: presenza · gravità: alta · judge: sì · fonte: contratto art. 5.2; verbale del consiglio, punto 2
Verifica: Il deliverable afferma che la delibera del 14 settembre 2028 viola il divieto contrattuale di trasferire commesse a società del gruppo a condizioni diverse da quelle praticate a terzi indipendenti.
Pass se: compare l'affermazione che quella delibera integra la condotta vietata dall'art. 5.2, o che costituisce inadempimento dell'acquirente.
Fail se: l'affermazione non compare.

B.18 il rilievo si aggiunge alla rettifica
issue: I-08 · tipo: assenza · gravità: media · judge: sì · fonte: contratto artt. 1.2, lett. (d), e 5.2
Verifica: Il deliverable non presenta il rilievo sull'inadempimento come alternativo alla rettifica della lettera (d).
Pass se: non compare l'affermazione che si debba scegliere fra la rettifica e la pretesa risarcitoria.
Fail se: si afferma che il venditore deve scegliere fra la rettifica del parametro e la pretesa per inadempimento, o che la seconda assorbe la prima.

B.19 accesso ai dati senza risposta
issue: I-09 · tipo: presenza · gravità: media · judge: sì · fonte: contratto art. 4.3; PEC del 19 giugno 2029
Verifica: Il deliverable afferma che la richiesta di accesso ai dati contabili non ha avuto risposta agli atti e che il termine di quindici giorni è decorso.
Pass se: compare l'affermazione che non risulta alcuna risposta alla richiesta di dati e che il termine è scaduto.
Fail se: l'affermazione non compare, oppure si afferma che i dati sono stati trasmessi.

B.20 dettaglio degli oneri di integrazione da acquisire
issue: I-09 · tipo: presenza · gravità: media · judge: sì · fonte: contratto art. 4.3
Verifica: Il deliverable indica fra gli elementi da acquisire il dettaglio degli oneri di integrazione.
Pass se: compare l'indicazione del dettaglio, della documentazione o dei giustificativi degli oneri di integrazione fra gli elementi da chiedere all'acquirente.
Fail se: l'indicazione non compare.

B.21 listini praticati a terzi da acquisire
issue: I-09 · tipo: presenza · gravità: media · judge: sì · fonte: contratto art. 4.3
Verifica: Il deliverable indica fra gli elementi da acquisire i listini o i prezzi praticati dalla società a terzi indipendenti nel periodo di riferimento.
Pass se: compare l'indicazione dei listini, dei prezzi praticati a terzi o della documentazione dei prezzi verso terzi fra gli elementi da chiedere.
Fail se: l'indicazione non compare.

B.22 esigibilità del corrispettivo
issue: I-10 · tipo: presenza · gravità: media · judge: sì · fonte: contratto art. 4.6
Verifica: Il deliverable afferma che il corrispettivo variabile è esigibile entro trenta giorni dalla determinazione definitiva del parametro.
Pass se: compare l'indicazione del termine di trenta giorni dalla determinazione definitiva.
Fail se: il termine di pagamento non è indicato, oppure è ancorato a un evento diverso dalla determinazione definitiva.

B.23 decorrenza degli interessi
issue: I-10 · tipo: assenza · gravità: media · judge: sì · fonte: art. 1224 c.c.; contratto art. 4.6
Verifica: Il deliverable non indica gli interessi come decorrenti dalla chiusura dell'esercizio.
Pass se: non compare l'affermazione che gli interessi decorrono dal 31 dicembre 2028.
Fail se: gli interessi sono indicati come decorrenti dalla chiusura dell'esercizio o dalla data del prospetto.

B.24 divieto di compensazione
issue: I-11 · tipo: presenza · gravità: media · judge: sì · fonte: contratto art. 8.3
Verifica: Il deliverable afferma che l'acquirente non può compensare pretese indennitarie con il corrispettivo variabile.
Pass se: compare l'affermazione che la compensazione con le pretese indennitarie è esclusa dal contratto.
Fail se: l'affermazione non compare, oppure si afferma che l'acquirente può compensare.

B.25 manipolazione del bilancio non sostenuta
issue: I-12 · tipo: presenza · gravità: media · judge: sì · fonte: PEC del 19 giugno 2029; bilancio, relazione del revisore
Verifica: Il deliverable afferma che l'affermazione secondo cui il bilancio sarebbe stato costruito per comprimere il parametro non trova riscontro nel fascicolo.
Pass se: compare l'affermazione che quel rilievo non è sostenuto dai documenti, o non è provato, o non è sostenibile allo stato degli atti.
Fail se: l'affermazione del cliente è recepita come accertata, oppure non è esaminata.

B.26 assicurazione in trattativa non documentata
issue: I-12 · tipo: presenza · gravità: media · judge: sì · fonte: PEC del 19 giugno 2029
Verifica: Il deliverable afferma che l'assicurazione ricevuta in trattativa sul riconoscimento del corrispettivo non risulta da alcun documento del fascicolo.
Pass se: compare l'affermazione che quella circostanza non è documentata, o non è provata dagli atti.
Fail se: l'affermazione del cliente è recepita come accertata, oppure non è esaminata.

B.27 il trasferimento delle commesse è documentato
issue: I-12 · tipo: assenza · gravità: media · judge: sì · fonte: verbale del consiglio, punto 2
Verifica: Il deliverable non presenta come non documentato il trasferimento delle commesse a Zandobbio Componenti S.r.l.
Pass se: non compare l'affermazione che il trasferimento delle commesse sia privo di riscontro.
Fail se: il trasferimento delle commesse è presentato come circostanza non provata o solo affermata dal cliente.

B.28 richiesta formale dei dati
issue: I-13 · tipo: presenza · gravità: alta · judge: sì · fonte: contratto art. 4.3
Verifica: Fra le azioni indicate compare la richiesta formale all'acquirente dei dati contabili previsti dal contratto.
Pass se: compare l'indicazione di formulare o rinnovare per iscritto la richiesta dei dati.
Fail se: l'azione non compare.

B.29 contestazione della nomina dell'esperto
issue: I-13 · tipo: presenza · gravità: alta · judge: sì · fonte: contratto art. 4.5
Verifica: Fra le azioni indicate compare la contestazione della nomina dell'esperto con richiesta di scelta congiunta o di designazione da parte del Presidente dell'Ordine.
Pass se: compare l'indicazione di contestare la nomina e di chiedere la scelta congiunta oppure la designazione da parte del Presidente dell'Ordine.
Fail se: l'azione non compare.

B.30 domanda giudiziale come strada residua
issue: I-13 · tipo: presenza · gravità: media · judge: sì · fonte: contratto art. 13.1
Verifica: Fra le azioni indicate compare, in difetto di accordo, la domanda giudiziale di accertamento del corrispettivo.
Pass se: compare l'indicazione di agire in giudizio, o davanti al foro convenuto, in mancanza di accordo.
Fail se: l'azione non compare.

B.31 il venditore non deve attendere
issue: I-13 · tipo: assenza · gravità: alta · judge: sì · fonte: contratto art. 4.5
Verifica: Il deliverable non afferma che il venditore debba attendere la determinazione dell'esperto prima di agire.
Pass se: quell'affermazione non compare.
Fail se: si afferma che non vi è nulla da fare fino alla determinazione dell'esperto.

B.32 sovra-segnalazione: plusvalenza
issue: N-01 · tipo: assenza · gravità: alta · judge: sì · fonte: prospetto riga B.1; contratto art. 1.2, lett. (a)
Verifica: Il deliverable non contesta l'esclusione della plusvalenza sulla cessione del fabbricato magazzino.
Pass se: non compare alcun rilievo che chieda di reintegrare quella plusvalenza nel parametro o che qualifichi come errata la riga B.1 del prospetto.
Fail se: l'esclusione della plusvalenza è presentata come errata, oppure si chiede di reintegrarla.

B.33 sovra-segnalazione: tempestività del prospetto
issue: N-02 · tipo: assenza · gravità: media · judge: sì · fonte: contratto art. 4.4; bilancio, frontespizio; PEC del 21 maggio 2029
Verifica: Il deliverable non afferma che il prospetto sia stato trasmesso oltre il termine contrattuale.
Pass se: quell'affermazione non compare.
Fail se: il prospetto è presentato come tardivo o inefficace per superamento del termine.

B.34 sovra-segnalazione: variazione dei criteri
issue: N-03 · tipo: assenza · gravità: media · judge: sì · fonte: contratto art. 1.2, lett. (c); bilancio, nota integrativa
Verifica: Il deliverable non applica una rettifica per variazione dei criteri di valutazione.
Pass se: non compare alcuna rettifica riferita alla lettera (c), né l'ipotesi di una variazione dei criteri di valutazione.
Fail se: si applica o si ipotizza una rettifica per variazione dei criteri di valutazione.

B.35 sovra-segnalazione: corrispettivo nell'atto notarile
issue: N-04 · tipo: assenza · gravità: alta · judge: sì · fonte: atto notarile del 1 febbraio 2028, articolo 2
Verifica: Il deliverable non afferma che il corrispettivo variabile non sia dovuto perché non risulta dall'atto notarile.
Pass se: quell'affermazione non compare.
Fail se: si afferma che il corrispettivo variabile non è dovuto, o non è opponibile, perché l'atto notarile indica il solo corrispettivo fisso.

B.36 sovra-segnalazione: discrezionalità gestionale
issue: N-05 · tipo: assenza · gravità: alta · judge: sì · fonte: contratto artt. 5.2 e 5.3
Verifica: Il deliverable non presenta la clausola che nega l'obbligo di massimizzare il parametro come clausola che legittima la compressione del parametro.
Pass se: non compare l'affermazione che l'art. 5.3 consente all'acquirente di ridurre il parametro o priva il venditore di tutela.
Fail se: l'art. 5.3 è presentato come licenza a comprimere il parametro o come clausola che rende inefficace il divieto dell'art. 5.2.

B.37 sovra-segnalazione: accantonamenti
issue: N-06 · tipo: assenza · gravità: media · judge: sì · fonte: contratto art. 1.2; bilancio, voci B.12 e B.13
Verifica: Il deliverable non applica agli accantonamenti delle voci 12 e 13 una rettifica ulteriore rispetto alla loro inclusione nell'EBITDA.
Pass se: non compare alcuna rettifica riferita agli accantonamenti.
Fail se: gli accantonamenti sono sommati o sottratti una seconda volta fra le rettifiche.

B.38 prudenza paralizzante: decadenza
issue: N-07 · tipo: assenza · gravità: alta · judge: sì · fonte: contratto art. 4.4; PEC del 19 giugno 2029
Verifica: Il deliverable non afferma che il venditore sia decaduto, o che la contestazione sia inefficace, per non avere quantificato gli importi contestati.
Pass se: quell'affermazione non compare.
Fail se: si afferma la decadenza del venditore, o l'inefficacia della contestazione, per difetto di quantificazione.

B.39 simmetria: accesso ai dati
issue: I-14 · tipo: assenza · gravità: bassa · judge: sì · fonte: contratto art. 4.3
Verifica: Il deliverable non presenta il diritto di accesso ai dati come una esposizione per il venditore.
Pass se: non compare alcun rilievo che presenti l'art. 4.3 come sfavorevole al venditore.
Fail se: l'art. 4.3 è presentato come clausola sfavorevole o come esposizione.

B.40 simmetria: divieto di atti riduttivi
issue: I-14 · tipo: assenza · gravità: bassa · judge: sì · fonte: contratto art. 5.2
Verifica: Il deliverable non presenta il divieto di atti che riducano il parametro come una esposizione per il venditore.
Pass se: non compare alcun rilievo che presenti l'art. 5.2 come sfavorevole al venditore.
Fail se: l'art. 5.2 è presentato come clausola sfavorevole o come esposizione.

B.41 simmetria: divieto di compensazione
issue: I-14 · tipo: assenza · gravità: bassa · judge: sì · fonte: contratto art. 8.3
Verifica: Il deliverable non presenta il divieto di compensazione come una esposizione per il venditore.
Pass se: non compare alcun rilievo che presenti l'art. 8.3 come sfavorevole al venditore.
Fail se: l'art. 8.3 è presentato come clausola sfavorevole o come esposizione.

B.42 presunzione: determinazione dell'esperto
issue: I-15 · tipo: assenza · gravità: media · judge: sì · fonte: lettera di incarico del 2 luglio 2029
Verifica: Il deliverable non afferma che l'esperto abbia reso la determinazione.
Pass se: quell'affermazione non compare.
Fail se: si afferma che l'esperto ha reso, o ha comunicato, la propria determinazione.

B.43 presunzione: dolo dell'acquirente
issue: I-15 · tipo: assenza · gravità: media · judge: sì · fonte: stato del fascicolo
Verifica: Il deliverable non afferma che l'acquirente abbia agito con dolo o che il bilancio sia falso.
Pass se: quelle affermazioni non compaiono.
Fail se: si afferma il dolo dell'acquirente, o la falsità del bilancio, come accertati.


C. DATE E VALORI CALCOLATI

C. DATE E VALORI

C.1 EBITDA di partenza
issue: I-01 · tipo: valore · gravità: alta · judge: no · fonte: contratto art. 1.2; bilancio, conto economico
Verifica: Il deliverable indica 3.740.000 euro come EBITDA del periodo di riferimento.
Pass se: compare l'importo di 3.740.000 euro riferito all'EBITDA.
Fail se: è indicato un importo diverso, oppure l'EBITDA non è quantificato.

C.2 derivazione errata: differenza A-B
issue: I-01 · tipo: assenza · gravità: alta · judge: sì · fonte: bilancio, conto economico
Verifica: Il deliverable non indica 2.150.000 euro come EBITDA.
Pass se: quell'importo non compare come EBITDA.
Fail se: 2.150.000 euro è presentato come EBITDA del periodo di riferimento.

C.3 derivazione errata: accantonamenti omessi
issue: I-01 · tipo: assenza · gravità: media · judge: sì · fonte: bilancio, voci B.12 e B.13
Verifica: Il deliverable non indica 3.660.000 euro come EBITDA.
Pass se: quell'importo non compare come EBITDA.
Fail se: 3.660.000 euro è presentato come EBITDA del periodo di riferimento.

C.4 importo della rettifica sugli oneri di integrazione
issue: I-02 · tipo: valore · gravità: alta · judge: no · fonte: bilancio, nota integrativa alla voce B.7; verbale del consiglio, punto 3
Verifica: Il deliverable indica 420.000 euro come importo della rettifica sugli oneri di integrazione.
Pass se: compare l'importo di 420.000 euro riferito a quella rettifica.
Fail se: è indicato un importo diverso, oppure la rettifica non è quantificata.

C.5 importo della rettifica sulle commesse
issue: I-03 · tipo: valore · gravità: alta · judge: no · fonte: verbale del consiglio, punto 2; bilancio, nota integrativa
Verifica: Il deliverable indica 260.000 euro come importo della rettifica sulle commesse trasferite.
Pass se: compare l'importo di 260.000 euro riferito a quella rettifica.
Fail se: è indicato un importo diverso, oppure la rettifica non è quantificata.

C.6 passaggio: differenza fra i due valori delle commesse
issue: I-03 · tipo: presenza · gravità: alta · judge: sì · fonte: verbale del consiglio, punto 2; bilancio, nota integrativa
Verifica: Il deliverable espone la rettifica sulle commesse come differenza fra il valore a listino di 1.240.000 euro e il ricavo contabilizzato di 980.000 euro.
Pass se: compaiono entrambi gli importi e la loro differenza.
Fail se: il calcolo non è esposto, oppure compare un solo importo.

C.7 EBITDA Rettificato
issue: I-04 · tipo: valore · gravità: alta · judge: no · fonte: contratto art. 1.2
Verifica: Il deliverable indica 4.110.000 euro come EBITDA Rettificato del periodo di riferimento.
Pass se: compare l'importo di 4.110.000 euro riferito all'EBITDA Rettificato.
Fail se: è indicato un importo diverso, oppure l'EBITDA Rettificato non è quantificato.

C.8 corrispettivo variabile dovuto
issue: I-04 · tipo: valore · gravità: alta · judge: no · fonte: contratto artt. 4.1 e 4.2
Verifica: Il deliverable indica 2.000.000 euro come corrispettivo variabile dovuto.
Pass se: compare l'importo di 2.000.000 euro riferito al corrispettivo variabile.
Fail se: è indicato un importo diverso, oppure il corrispettivo non è quantificato.

C.9 derivazione errata: formula proporzionale
issue: I-04 · tipo: assenza · gravità: alta · judge: sì · fonte: contratto art. 4.1, lett. (iii)
Verifica: Il deliverable non indica 750.000 euro come corrispettivo variabile dovuto.
Pass se: quell'importo non compare come corrispettivo dovuto.
Fail se: 750.000 euro è presentato come corrispettivo variabile dovuto.

C.10 derivazione errata: nulla dovuto
issue: I-04 · tipo: assenza · gravità: alta · judge: sì · fonte: prospetto riga C.5
Verifica: Il deliverable non afferma che il corrispettivo variabile non sia dovuto.
Pass se: quell'affermazione non compare come conclusione.
Fail se: la conclusione del deliverable è che nulla è dovuto al venditore.

C.11 termine di decadenza
issue: I-05 · tipo: valore · gravità: alta · judge: no · fonte: contratto art. 4.4; PEC del 21 maggio 2029
Verifica: Il deliverable indica il 20 giugno 2029 come termine finale per la contestazione.
Pass se: compare la data del 20 giugno 2029 riferita al termine di contestazione.
Fail se: è indicata una data diversa, oppure il termine non è indicato.

C.12 derivazione errata: decorrenza dalla data del prospetto
issue: I-05 · tipo: assenza · gravità: alta · judge: sì · fonte: contratto art. 4.4
Verifica: Il deliverable non indica il 14 giugno 2029 come termine finale per la contestazione.
Pass se: quella data non compare come termine di contestazione.
Fail se: il 14 giugno 2029 è presentato come termine finale per la contestazione.

C.13 scadenza della finestra di trattativa
issue: I-06 · tipo: valore · gravità: media · judge: no · fonte: contratto art. 4.5; PEC del 19 giugno 2029
Verifica: Il deliverable indica il 19 luglio 2029 come scadenza del termine entro il quale le parti dovevano tentare l'accordo.
Pass se: compare la data del 19 luglio 2029 riferita a quel termine.
Fail se: è indicata una data diversa, oppure il termine non è indicato.

C.14 rettifica in diminuzione sulla plusvalenza
issue: I-04 · tipo: valore · gravità: alta · judge: no · fonte: contratto art. 1.2, lett. (a); prospetto riga B.1
Verifica: Il deliverable indica 310.000 euro come importo della rettifica in diminuzione sulla plusvalenza.
Pass se: compare l'importo di 310.000 euro riferito a quella rettifica.
Fail se: è indicato un importo diverso, oppure la rettifica in diminuzione non è quantificata.
