Convenzione atomo v1. required = gravità alta; media e bassa = optional.
Inquadramento: WF2-026; fascicolo fotografato al 2031-03-06.
La base normativa è congelata al 25 agosto 2026 e coincide con il reference pack chiuso.

A. FORMA DELL'OUTPUT

A.1 sezioni obbligatorie del memo
issue: — · tipo: valore · gravità: alta · judge: no · fonte: response_template.md
Verifica: Il deliverable contiene una sintesi per la decisione, una sezione di rilievi bloccanti, una sezione di rilievi non bloccanti, una sezione su ciò che non è un rilievo, una sezione con date e numeri e una sezione su ciò che manca dal pacchetto.
Pass se: tutte e sei le sezioni sono presenti e distinte.
Fail se: manca una delle sei sezioni, oppure due di esse non sono distinte.

A.2 qualificazione bloccante o non bloccante
issue: — · tipo: presenza · gravità: alta · judge: no · fonte: prompt
Verifica: Ogni rilievo è qualificato come bloccante o non bloccante rispetto alla data di avvio prevista.
Pass se: ogni rilievo porta una delle due qualificazioni.
Fail se: almeno un rilievo è privo della qualificazione.

A.3 azione e responsabile per ciascun rilievo
issue: — · tipo: struttura · gravità: alta · judge: no · fonte: response_template.md
Verifica: Ogni rilievo indica l'azione richiesta e il soggetto che la deve compiere.
Pass se: ogni rilievo porta azione e soggetto.
Fail se: almeno un rilievo è privo dell'azione o del soggetto.

A.4 ancoraggio documentale
issue: — · tipo: struttura · gravità: alta · judge: no · fonte: response_template.md
Verifica: Ogni rilievo indica il documento del pacchetto da cui deriva.
Pass se: ogni rilievo contiene il nome di un documento del pacchetto o il riferimento a una sua sezione.
Fail se: almeno un rilievo è privo di riferimento documentale.

A.5 nessuna riscrittura di documenti
issue: — · tipo: assenza · gravità: alta · judge: no · fonte: prompt
Verifica: Il deliverable non contiene clausole riscritte, bozze di documenti da firmare o una valutazione d'impatto riscritta.
Pass se: non compare testo redatto in forma di clausola, di informativa o di valutazione d'impatto.
Fail se: il deliverable contiene una clausola riscritta, una bozza di informativa o una valutazione d'impatto riscritta.

A.6 fonti nell'elenco chiuso
issue: — · tipo: assenza · gravità: alta · judge: no · fonte: reference pack
Verifica: Il deliverable non contiene riferimenti normativi estranei all'elenco chiuso delle fonti del reference pack.
Pass se: ogni riferimento normativo citato appartiene all'elenco.
Fail se: compare almeno un riferimento normativo fuori elenco.


B. MERITO

B. MERITO

B.1 finalità non valutata
issue: I-01 · tipo: presenza · gravità: alta · judge: sì · fonte: DPIA § 2.1; specifica funzionale § 1.3
Verifica: Il deliverable afferma che la valutazione d'impatto non copre la finalità di punteggio di propensione all'abbandono prevista dalla specifica funzionale.
Pass se: compare l'affermazione che quella finalità non è valutata, o che l'ambito della valutazione è più stretto del trattamento.
Fail se: l'affermazione non compare, oppure si afferma che la valutazione copre tutte le finalità.

B.2 identità del modello fra le finalità
issue: I-01 · tipo: presenza · gravità: media · judge: sì · fonte: specifica funzionale § 1.3
Verifica: Il deliverable afferma che il punteggio di propensione è calcolato dal medesimo modello e con le medesime variabili del punteggio di rischio.
Pass se: compare quell'affermazione.
Fail se: l'affermazione non compare.

B.3 categoria di dati aggiunta dopo l'approvazione
issue: I-02 · tipo: presenza · gravità: alta · judge: sì · fonte: specifica funzionale § 2 e cronologia delle versioni; DPIA § 2.3
Verifica: Il deliverable afferma che la specifica funzionale ha aggiunto, dopo l'approvazione della valutazione, gli indicatori di comportamento di pagamento acquisiti da una fonte esterna.
Pass se: compare l'affermazione che quella categoria di dati è stata aggiunta dopo l'approvazione della valutazione.
Fail se: l'affermazione non compare.

B.4 obbligo di riesame
issue: I-02 · tipo: qualificazione · gravità: alta · judge: sì · fonte: art. 35, par. 11
Verifica: Il deliverable afferma che la valutazione d'impatto va riesaminata perché sono insorte variazioni del rischio.
Pass se: compare l'indicazione di riesaminare la valutazione a fronte della modifica.
Fail se: l'indicazione non compare.

B.5 necessità e proporzionalità non valutate
issue: I-03 · tipo: presenza · gravità: alta · judge: sì · fonte: DPIA § 4; art. 35, par. 7, lett. b)
Verifica: Il deliverable afferma che la sezione della valutazione su necessità e proporzionalità contiene affermazioni conclusive e non una valutazione, e che non considera alternative meno intrusive.
Pass se: compaiono entrambi gli elementi, il carattere conclusivo della sezione e l'assenza di alternative considerate.
Fail se: manca uno dei due elementi, oppure la sezione è presentata come conforme.

B.6 dati del collaudo sul riesame
issue: I-04 · tipo: presenza · gravità: alta · judge: sì · fonte: procedura di riesame § 5
Verifica: Il deliverable riporta i dati del collaudo sul riesame manuale, indicando la quota di conferme e il tempo medio.
Pass se: compaiono entrambi i dati, la quota di conferme e il tempo medio.
Fail se: manca uno dei due dati.

B.7 il riesame non assicura l'intervento umano
issue: I-04 · tipo: qualificazione · gravità: alta · judge: sì · fonte: procedura di riesame §§ 4 e 5; DPIA § 5; art. 22
Verifica: Il deliverable afferma che il riesame, per come è organizzato e per come ha funzionato nel collaudo, non assicura l'intervento umano e non consente di escludere che la decisione sia basata unicamente sul trattamento automatizzato.
Pass se: compare l'affermazione che l'esclusione operata dalla valutazione non è sostenuta, o che il riesame non integra l'intervento umano.
Fail se: l'affermazione non compare, oppure si afferma che la presenza del riesame esclude la disciplina delle decisioni automatizzate.

B.8 limiti dell'operatore
issue: I-04 · tipo: presenza · gravità: media · judge: sì · fonte: procedura di riesame § 4.3
Verifica: Il deliverable afferma che l'operatore non ha accesso alla logica di formazione del punteggio e non può chiederne il ricalcolo.
Pass se: compare almeno uno dei due limiti.
Fail se: nessuno dei due limiti compare.

B.9 garanzie richieste per la decisione automatizzata
issue: I-04 · tipo: presenza · gravità: alta · judge: sì · fonte: art. 22, parr. 2 e 3
Verifica: Il deliverable indica che vanno individuati la base che consente la decisione e le garanzie a tutela dell'interessato, fra cui il diritto di ottenere l'intervento umano, di esprimere la propria opinione e di contestare la decisione.
Pass se: compaiono la base che consente la decisione e almeno una delle tre garanzie.
Fail se: l'indicazione non compare.

B.10 rischi alti con misura non attuata
issue: I-05 · tipo: presenza · gravità: alta · judge: sì · fonte: registro dei rischi, righe R2, R4 e R6
Verifica: Il deliverable afferma che il registro dei rischi contiene rischi di livello alto la cui misura non è attuata, con data obiettivo successiva alla data di avvio prevista.
Pass se: compaiono entrambi gli elementi, i rischi alti con misura non attuata e la collocazione delle date obiettivo dopo l'avvio.
Fail se: manca uno dei due elementi.

B.11 contraddizione sul rischio residuo
issue: I-05 · tipo: presenza · gravità: alta · judge: sì · fonte: registro dei rischi, riepilogo; DPIA § 7
Verifica: Il deliverable afferma che il rischio residuo dichiarato dalla valutazione non corrisponde a quello che il registro dei rischi calcola.
Pass se: compare l'affermazione che il residuo dichiarato non è sostenuto dal registro, o che i due documenti dicono cose diverse.
Fail se: l'affermazione non compare, oppure il residuo dichiarato è presentato come sostenuto.

B.12 presupposto della consultazione preventiva
issue: I-06 · tipo: qualificazione · gravità: alta · judge: sì · fonte: art. 36, par. 1
Verifica: Il deliverable afferma che il titolare deve consultare l'autorità di controllo prima di procedere se la valutazione indica un rischio elevato in assenza di misure di attenuazione.
Pass se: compare l'affermazione del presupposto della consultazione preventiva.
Fail se: l'affermazione non compare.

B.13 ordine fra correzione e consultazione
issue: I-06 · tipo: presenza · gravità: alta · judge: sì · fonte: DPIA § 7; art. 36
Verifica: Il deliverable indica che la valutazione va prima riesaminata e integrata, e che la consultazione dell'autorità va valutata sull'esito del riesame.
Pass se: compare quella sequenza.
Fail se: la sequenza non compare, oppure la consultazione è indicata come alternativa alla correzione.

B.14 uso dei dati per i modelli del fornitore
issue: I-07 · tipo: presenza · gravità: alta · judge: sì · fonte: accordo sul trattamento, allegato tecnico § 4
Verifica: Il deliverable afferma che l'allegato tecnico consente al fornitore di utilizzare i dati per addestrare e migliorare i propri modelli, messi a disposizione anche di altri clienti.
Pass se: compare quell'affermazione.
Fail se: l'affermazione non compare.

B.15 qualificazione del fornitore per quell'attività
issue: I-07 · tipo: qualificazione · gravità: alta · judge: sì · fonte: art. 28, par. 10; accordo sul trattamento, allegato tecnico § 4
Verifica: Il deliverable afferma che per quell'attività il fornitore determina finalità e mezzi ed è perciò considerato titolare del trattamento, e che il modulo di clausole adottato non la copre.
Pass se: compaiono entrambi gli elementi, la qualificazione come titolare per quell'attività e l'inadeguatezza del modulo adottato.
Fail se: manca uno dei due elementi.

B.16 azione richiesta sul perimetro d'uso
issue: I-07 · tipo: presenza · gravità: alta · judge: sì · fonte: accordo sul trattamento, allegato tecnico § 4
Verifica: Il deliverable indica come azione l'esclusione di quell'uso dalle istruzioni al fornitore, oppure la sua copertura con lo strumento previsto per il trasferimento fra titolari.
Pass se: compare almeno una delle due azioni.
Fail se: nessuna delle due azioni compare.

B.17 sub-responsabile in un paese terzo ulteriore
issue: I-08 · tipo: presenza · gravità: alta · judge: sì · fonte: accordo sul trattamento, appendice D; specifica funzionale § 3.2
Verifica: Il deliverable afferma che un sub-responsabile stabilito in un paese terzo diverso da quello dell'importatore accede agli ambienti di produzione.
Pass se: compare quell'affermazione, con l'indicazione del paese.
Fail se: l'affermazione non compare.

B.18 il trasferimento successivo non è coperto
issue: I-08 · tipo: presenza · gravità: alta · judge: sì · fonte: accordo di trasferimento, appendici B e D; art. 44
Verifica: Il deliverable afferma che le appendici dell'accordo di trasferimento descrivono il solo trasferimento verso il paese dell'importatore e dichiarano l'assenza di sub-responsabili, e che il trasferimento successivo non è quindi coperto.
Pass se: compaiono entrambi gli elementi, il contenuto delle appendici e la conseguente mancanza di copertura.
Fail se: manca uno dei due elementi, oppure il trasferimento successivo è presentato come coperto.

B.19 la disciplina si applica ai trasferimenti successivi
issue: I-08 · tipo: qualificazione · gravità: media · judge: sì · fonte: art. 44
Verifica: Il deliverable afferma che la disciplina dei trasferimenti si applica anche ai trasferimenti successivi da un paese terzo verso un altro paese terzo.
Pass se: compare quell'affermazione.
Fail se: l'affermazione non compare.

B.20 la valutazione sul trasferimento poggia su una dichiarazione
issue: I-09 · tipo: presenza · gravità: alta · judge: sì · fonte: valutazione sul trasferimento § 3
Verifica: Il deliverable afferma che l'unico elemento su cui la valutazione sul trasferimento si fonda è una dichiarazione del fornitore.
Pass se: compare quell'affermazione.
Fail se: l'affermazione non compare, oppure la valutazione è presentata come fondata su elementi indipendenti.

B.21 assenza dell'esame del quadro normativo
issue: I-09 · tipo: presenza · gravità: alta · judge: sì · fonte: valutazione sul trasferimento §§ 3 e 4
Verifica: Il deliverable afferma che la valutazione sul trasferimento non contiene l'esame del quadro normativo del paese di destinazione e non valuta misure supplementari.
Pass se: compaiono entrambe le mancanze.
Fail se: manca una delle due.

B.22 la certificazione non è uno strumento di trasferimento
issue: I-09 · tipo: qualificazione · gravità: media · judge: sì · fonte: valutazione sul trasferimento § 4
Verifica: Il deliverable afferma che la certificazione di sicurezza del fornitore non è uno strumento che fonda il trasferimento.
Pass se: compare quell'affermazione.
Fail se: l'affermazione non compare, oppure la certificazione è presentata come strumento o garanzia del trasferimento.

B.23 la valutazione non copre il secondo paese
issue: I-09 · tipo: presenza · gravità: alta · judge: sì · fonte: valutazione sul trasferimento; accordo sul trattamento, appendice D
Verifica: Il deliverable afferma che la valutazione sul trasferimento non riguarda il paese del sub-responsabile.
Pass se: compare quell'affermazione.
Fail se: l'affermazione non compare.

B.24 il registro non copre il nuovo trattamento
issue: I-10 · tipo: presenza · gravità: alta · judge: sì · fonte: scheda del trattamento; art. 30, par. 1
Verifica: Il deliverable afferma che la scheda del registro delle attività di trattamento non riporta il nuovo trattamento e dichiara l'assenza di trasferimenti verso paesi terzi.
Pass se: compaiono entrambi gli elementi.
Fail se: manca uno dei due elementi.

B.25 l'informativa non copre il punteggio né il trasferimento
issue: I-10 · tipo: presenza · gravità: alta · judge: sì · fonte: informativa §§ 5 e 9; artt. 13 e 22
Verifica: Il deliverable afferma che l'informativa in uso non contiene la finalità di punteggio né il trasferimento verso paesi terzi, e che dichiara il contrario di quanto il progetto prevede.
Pass se: compaiono entrambi gli elementi, le mancanze e la presenza di dichiarazioni contrarie.
Fail se: manca uno dei due elementi.

B.26 incoerenza fra conservazione e addestramento
issue: I-11 · tipo: presenza · gravità: alta · judge: sì · fonte: DPIA § 3; specifica funzionale §§ 4.1 e 4.2
Verifica: Il deliverable afferma che la finestra di addestramento del modello eccede il termine di conservazione dichiarato dalla valutazione.
Pass se: compare quell'affermazione.
Fail se: l'affermazione non compare.

B.27 conferma dell'incoerenza nel registro dei rischi
issue: I-11 · tipo: attribuzione · gravità: media · judge: sì · fonte: registro dei rischi, riga R6
Verifica: Il deliverable collega l'incoerenza sulla conservazione al rischio censito nel registro sulla conservazione oltre il termine negli ambienti di addestramento.
Pass se: compare il collegamento fra l'incoerenza e quella riga del registro.
Fail se: il collegamento non compare.

B.28 il responsabile della protezione dei dati non è stato consultato
issue: I-12 · tipo: presenza · gravità: alta · judge: sì · fonte: DPIA, frontespizio; messaggio del DPO; art. 35, par. 2
Verifica: Il deliverable afferma che il responsabile della protezione dei dati non è stato consultato durante lo svolgimento della valutazione e che il suo parere non risulta.
Pass se: compaiono entrambi gli elementi.
Fail se: manca uno dei due elementi, oppure la consultazione è presentata come avvenuta.

B.29 divieto di ritenere sanata la consultazione
issue: I-12 · tipo: assenza · gravità: media · judge: sì · fonte: nota del responsabile di progetto § 5
Verifica: Il deliverable non afferma che la messa a disposizione del documento sul repository condiviso equivale alla consultazione del responsabile della protezione dei dati.
Pass se: quell'affermazione non compare.
Fail se: si afferma che la messa a disposizione del documento ha assolto l'obbligo di consultazione.

B.30 correzione: ambito della valutazione
issue: I-13 · tipo: presenza · gravità: alta · judge: sì · fonte: nota del responsabile di progetto § 1
Verifica: Il deliverable afferma che l'affermazione della nota secondo cui la valutazione d'impatto copre l'intero progetto è errata.
Pass se: compare l'indicazione che quell'affermazione è errata o da correggere.
Fail se: l'indicazione non compare, oppure l'affermazione è confermata.

B.31 correzione: effetto della revisione umana
issue: I-13 · tipo: presenza · gravità: alta · judge: sì · fonte: nota del responsabile di progetto § 2
Verifica: Il deliverable afferma che l'affermazione della nota secondo cui la presenza della revisione umana esclude la disciplina delle decisioni automatizzate è errata.
Pass se: compare l'indicazione che quell'affermazione è errata o da correggere.
Fail se: l'indicazione non compare, oppure l'affermazione è confermata.

B.32 correzione: copertura dei trasferimenti
issue: I-13 · tipo: presenza · gravità: alta · judge: sì · fonte: nota del responsabile di progetto § 3
Verifica: Il deliverable afferma che l'affermazione della nota secondo cui le clausole firmate coprono tutti i trasferimenti è errata.
Pass se: compare l'indicazione che quell'affermazione è errata o da correggere.
Fail se: l'indicazione non compare, oppure l'affermazione è confermata.

B.33 correzione: termine di opposizione
issue: I-13 · tipo: presenza · gravità: alta · judge: sì · fonte: nota del responsabile di progetto § 4; accordo sul trattamento, art. 5.2
Verifica: Il deliverable afferma che l'affermazione della nota secondo cui il termine per opporsi al sub-responsabile non è ancora decorso è errata.
Pass se: compare l'indicazione che quell'affermazione è errata, o che il termine è scaduto.
Fail se: l'indicazione non compare, oppure l'affermazione è confermata.

B.34 simmetria: preavviso rispettato
issue: I-13 · tipo: assenza · gravità: media · judge: sì · fonte: accordo sul trattamento, art. 5.2; nota del responsabile di progetto § 4
Verifica: Il deliverable non contesta l'affermazione secondo cui la comunicazione del sub-responsabile ha rispettato il preavviso di trenta giorni.
Pass se: quell'affermazione non è presentata come errata.
Fail se: si afferma che il preavviso non è stato rispettato.

B.35 elementi mancanti: parere e logica del punteggio
issue: I-16 · tipo: presenza · gravità: alta · judge: sì · fonte: messaggio del DPO; specifica funzionale § 2
Verifica: Il deliverable indica fra gli elementi mancanti il parere del responsabile della protezione dei dati e la descrizione della logica di formazione del punteggio.
Pass se: compaiono entrambe le voci fra gli elementi mancanti.
Fail se: manca una delle due voci.

B.36 elementi mancanti: fonte esterna e quadro normativo
issue: I-16 · tipo: presenza · gravità: media · judge: sì · fonte: specifica funzionale § 2; valutazione sul trasferimento § 3
Verifica: Il deliverable indica fra gli elementi mancanti il contratto con la fonte esterna degli indicatori e la documentazione del quadro normativo dei paesi di destinazione.
Pass se: compaiono entrambe le voci fra gli elementi mancanti.
Fail se: manca una delle due voci.

B.37 simmetria: fornitore non stabilito nell'Unione
issue: I-14 · tipo: assenza · gravità: media · judge: sì · fonte: accordo di trasferimento, appendice A
Verifica: Il deliverable non presenta come rilievo il fatto che il fornitore non sia stabilito nell'Unione europea.
Pass se: quel fatto non è presentato come rilievo.
Fail se: si afferma che la mancanza di stabilimento nell'Unione è un difetto del pacchetto.

B.38 presunzione: esito davanti all'autorità
issue: I-15 · tipo: assenza · gravità: alta · judge: sì · fonte: prompt
Verifica: Il deliverable non afferma che l'autorità di controllo vieterebbe il trattamento o irrogherebbe una sanzione.
Pass se: nessuna delle due affermazioni compare.
Fail se: si afferma che l'autorità vieterebbe il trattamento o irrogherebbe una sanzione.

B.39 presunzione: condotta del fornitore e accessi avvenuti
issue: I-15 · tipo: assenza · gravità: alta · judge: sì · fonte: prompt; valutazione sul trasferimento § 3
Verifica: Il deliverable non afferma che il fornitore accetterà le modifiche richieste né che i dati sono già stati oggetto di accesso da parte di autorità del paese di destinazione.
Pass se: nessuna delle due affermazioni compare.
Fail se: si afferma che il fornitore accetterà le modifiche, o che gli accessi si sono già verificati.

B.40 sovra-segnalazione: certificazione di sicurezza
issue: N-01 · tipo: assenza · gravità: alta · judge: sì · fonte: accordo di trasferimento, appendice C
Verifica: Il deliverable non presenta la certificazione di sicurezza del fornitore come difetto del pacchetto.
Pass se: la certificazione non compare fra i rilievi.
Fail se: la certificazione è presentata come difetto o come elemento insufficiente in se'.

B.41 sovra-segnalazione: scala qualitativa del rischio
issue: N-02 · tipo: assenza · gravità: alta · judge: sì · fonte: registro dei rischi
Verifica: Il deliverable non presenta come rilievo la scala qualitativa di valutazione del rischio adottata dal registro.
Pass se: la metodologia di valutazione non compare fra i rilievi.
Fail se: si rileva che la scala qualitativa è inadatta o che serve una valutazione quantitativa.

B.42 sovra-segnalazione: comunicazione del sub-responsabile
issue: N-03 · tipo: assenza · gravità: alta · judge: sì · fonte: accordo sul trattamento, art. 5.2 e appendice D
Verifica: Il deliverable non presenta come rilievo la comunicazione con cui il fornitore ha aggiunto il sub-responsabile.
Pass se: la comunicazione non compare fra i rilievi.
Fail se: si rileva che la comunicazione era irregolare, tardiva o priva di effetto.

B.43 sovra-segnalazione: dati di misura come categoria particolare
issue: N-04 · tipo: assenza · gravità: alta · judge: sì · fonte: DPIA § 2.4; art. 9
Verifica: Il deliverable non qualifica i dati di misura oraria del consumo come categoria particolare di dati.
Pass se: quella qualificazione non compare.
Fail se: si afferma che i dati di misura oraria sono categorie particolari di dati o rientrano nell'articolo 9.

B.44 sovra-segnalazione: necessità della valutazione
issue: N-05 · tipo: assenza · gravità: alta · judge: sì · fonte: DPIA § 1
Verifica: Il deliverable non afferma che la valutazione d'impatto non fosse dovuta né che la valutazione della soglia sia errata.
Pass se: nessuna delle due affermazioni compare.
Fail se: si afferma che la valutazione d'impatto non era richiesta, o che l'analisi della soglia è sbagliata.

B.45 sovra-segnalazione: parere degli interessati
issue: N-06 · tipo: assenza · gravità: alta · judge: sì · fonte: DPIA § 8; art. 35, par. 9
Verifica: Il deliverable non presenta come rilievo la scelta di non raccogliere il parere degli interessati.
Pass se: quella scelta non compare fra i rilievi.
Fail se: si rileva che il parere degli interessati andava raccolto.

B.46 sovra-segnalazione: stabilimento del fornitore
issue: N-07 · tipo: assenza · gravità: media · judge: sì · fonte: accordo di trasferimento, appendice A
Verifica: Il deliverable non presenta come rilievo autonomo la circostanza che il fornitore sia stabilito in un paese terzo.
Pass se: quella circostanza non compare fra i rilievi.
Fail se: si rileva che il fornitore non poteva essere designato responsabile perché stabilito fuori dall'Unione.


C. DATE E VALORI CALCOLATI

C. DATE E VALORI

C.1 finalità valutate e finalità previste
issue: I-01 · tipo: valore · gravità: alta · judge: no · fonte: DPIA § 2.1; specifica funzionale § 1
Verifica: Il deliverable indica due come numero delle finalità valutate dalla valutazione d'impatto e tre come numero delle finalità previste dalla specifica funzionale.
Pass se: compaiono entrambi i numeri, due e tre, riferiti rispettivamente alla valutazione e alla specifica.
Fail se: manca uno dei due numeri, oppure sono indicati numeri diversi.

C.2 categorie di dati della specifica funzionale
issue: I-02 · tipo: valore · gravità: alta · judge: no · fonte: specifica funzionale § 2
Verifica: Il deliverable indica sette come numero dei gruppi di variabili in ingresso previsti dalla specifica funzionale 2.1.
Pass se: compare il numero sette riferito ai gruppi di variabili della specifica.
Fail se: compare un numero diverso, oppure il numero non è indicato.

C.3 derivazione errata: sei categorie
issue: I-02 · tipo: assenza · gravità: media · judge: sì · fonte: DPIA § 2.3; specifica funzionale § 2
Verifica: Il deliverable non indica sei come numero dei gruppi di variabili previsti dalla specifica funzionale 2.1.
Pass se: quel numero non compare come perimetro della specifica funzionale 2.1.
Fail se: compare il numero sei come perimetro della specifica funzionale 2.1.
Indifferente: il richiamo di sei categorie come perimetro della valutazione d'impatto.

C.4 giorni fra approvazione e modifica
issue: I-02 · tipo: valore · gravità: media · judge: no · fonte: DPIA, frontespizio; specifica funzionale, cronologia
Verifica: Il deliverable indica cinquantasei come numero di giorni fra l'approvazione della valutazione d'impatto e la specifica funzionale 2.1.
Pass se: compare il numero cinquantasei riferito a quell'intervallo.
Fail se: compare un numero diverso, oppure l'intervallo non è quantificato.
Indifferente: l'espressione dell'intervallo in mesi accanto al numero di giorni.

C.5 quota di conferme del riesame
issue: I-04 · tipo: valore · gravità: alta · judge: no · fonte: procedura di riesame § 5
Verifica: Il deliverable indica 97,4% come quota dei punteggi confermati dall'operatore nel collaudo.
Pass se: compare il valore 97,4% riferito alle conferme.
Fail se: compare un valore diverso, oppure la quota non è indicata.

C.6 passaggio: conferme su punteggi
issue: I-04 · tipo: presenza · gravità: alta · judge: sì · fonte: procedura di riesame § 5
Verifica: Il deliverable espone la quota di conferme come rapporto fra 12.126 conferme e 12.450 punteggi sopra soglia.
Pass se: compaiono entrambi i valori come termini del rapporto.
Fail se: manca uno dei due valori.

C.7 tempo medio di riesame
issue: I-04 · tipo: valore · gravità: alta · judge: no · fonte: procedura di riesame § 5
Verifica: Il deliverable indica quarantuno secondi come tempo medio di riesame rilevato nel collaudo.
Pass se: compare il valore quarantuno secondi riferito al tempo medio.
Fail se: compare un valore diverso, oppure il tempo medio non è indicato.

C.8 confronto fra tempo previsto e tempo rilevato
issue: I-04 · tipo: presenza · gravità: alta · judge: sì · fonte: procedura di riesame §§ 3 e 5
Verifica: Il deliverable confronta il tempo medio rilevato con il termine di quattro ore lavorative previsto dalla procedura.
Pass se: compaiono entrambi i termini del confronto.
Fail se: il confronto non compare.

C.9 rischi di livello alto
issue: I-05 · tipo: valore · gravità: alta · judge: no · fonte: registro dei rischi
Verifica: Il deliverable indica tre come numero dei rischi di livello alto censiti nel registro.
Pass se: compare il numero tre riferito ai rischi di livello alto.
Fail se: compare un numero diverso, oppure il numero non è indicato.

C.10 derivazione errata: due rischi alti
issue: I-05 · tipo: assenza · gravità: media · judge: sì · fonte: registro dei rischi
Verifica: Il deliverable non indica due come numero dei rischi di livello alto.
Pass se: quel numero non compare come numero dei rischi alti.
Fail se: compare il numero due come numero dei rischi di livello alto.

C.11 livello residuo calcolato dal registro
issue: I-05 · tipo: valore · gravità: alta · judge: no · fonte: registro dei rischi, riepilogo
Verifica: Il deliverable indica «alto» come livello residuo atteso più elevato risultante dal registro dei rischi.
Pass se: compare il livello alto riferito al residuo calcolato dal registro.
Fail se: compare un livello diverso, oppure il livello residuo del registro non è indicato.

C.12 termine di opposizione al sub-responsabile
issue: I-13 · tipo: valore · gravità: alta · judge: no · fonte: accordo sul trattamento, art. 5.2; appendice D
Verifica: Il deliverable indica il 21 febbraio 2031 come termine per l'opposizione al sub-responsabile.
Pass se: compare la data del 21 febbraio 2031 riferita a quel termine.
Fail se: compare una data diversa, oppure il termine non è indicato.

C.13 passaggio: trenta giorni dalla comunicazione
issue: I-13 · tipo: presenza · gravità: alta · judge: sì · fonte: accordo sul trattamento, art. 5.2
Verifica: Il deliverable espone il termine come trenta giorni dalla comunicazione del 22 gennaio 2031.
Pass se: compaiono i trenta giorni e la decorrenza dal 22 gennaio 2031.
Fail se: manca uno dei due elementi.

C.14 conservazione dichiarata e finestra di addestramento
issue: I-11 · tipo: valore · gravità: alta · judge: no · fonte: DPIA § 3; specifica funzionale § 4.1
Verifica: Il deliverable indica ventiquattro mesi come conservazione dichiarata e sessanta mesi come finestra di addestramento.
Pass se: compaiono entrambi i valori, ventiquattro e sessanta mesi, riferiti rispettivamente alla conservazione e all'addestramento.
Fail se: manca uno dei due valori.

C.15 eccedenza in mesi
issue: I-11 · tipo: valore · gravità: media · judge: no · fonte: calcolo
Verifica: Il deliverable indica trentasei come numero di mesi di cui la finestra di addestramento eccede la conservazione dichiarata.
Pass se: compare il numero trentasei riferito a quell'eccedenza.
Fail se: compare un numero diverso, oppure l'eccedenza non è quantificata.

C.16 giorni fra data di riferimento e avvio previsto
issue: I-06 · tipo: valore · gravità: media · judge: no · fonte: prompt; nota del responsabile di progetto
Verifica: Il deliverable indica ventisei come numero di giorni fra la data di riferimento e l'avvio in produzione previsto.
Pass se: compare il numero ventisei riferito a quell'intervallo.
Fail se: compare un numero diverso, oppure l'intervallo non è quantificato.
Indifferente: l'espressione dell'intervallo in settimane accanto al numero di giorni.

C.17 età dell'informativa in uso
issue: I-11 · tipo: valore · gravità: media · judge: no · fonte: informativa
Verifica: Il deliverable indica il 4 aprile 2029 come data della versione di informativa in uso.
Pass se: compare la data del 4 aprile 2029 riferita all'informativa.
Fail se: compare una data diversa, oppure la data non è indicata.

C.18 paesi terzi coinvolti
issue: I-08 · tipo: valore · gravità: alta · judge: no · fonte: accordo di trasferimento, appendice B; accordo sul trattamento, appendice D
Verifica: Il deliverable indica due come numero dei paesi terzi verso cui i dati sono trasferiti o resi accessibili.
Pass se: compare il numero due riferito ai paesi terzi coinvolti.
Fail se: compare un numero diverso, oppure il numero non è indicato.

C.19 assenza di decisione di adeguatezza
issue: I-09 · tipo: presenza · gravità: alta · judge: sì · fonte: valutazione sul trasferimento § 2
Verifica: Il deliverable afferma che nessuno dei due paesi terzi coinvolti è coperto da una decisione di adeguatezza della Commissione europea.
Pass se: compare quell'affermazione riferita a entrambi i paesi.
Fail se: l'affermazione non compare, oppure è riferita a uno solo dei due paesi.
