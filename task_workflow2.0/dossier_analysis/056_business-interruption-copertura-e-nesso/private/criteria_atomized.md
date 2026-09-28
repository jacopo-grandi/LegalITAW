# WF2-056 - Criteri atomizzati

Forma a campi. Ciò che sta sotto la riga non passa al judge.


## A. Forma dell'output (interamente verifica meccanica)

### A.1 [tipo: valore]

- **Verifica** il deliverable è prodotto come file `coverage_opinion.md`.
- **Pass se** il file consegnato ha nome `coverage_opinion.md`.
- **Fail se** il file ha un altro nome o un'altra estensione.
- **Indifferente** la presenza di intestazioni aggiuntive.
- *non passa al judge:* Fonte task_spec.json, campo deliverable - Gravita media - judge no

### A.2 [tipo: struttura]

- **Verifica** il deliverable contiene, nell'ordine, le sette sezioni obbligatorie del template.
- **Pass se** le sette intestazioni di sezione compaiono nell'ordine indicato dal template.
- **Fail se** manca almeno una sezione o l'ordine è diverso.
- **Indifferente** la numerazione delle sottosezioni.
- *non passa al judge:* Fonte public/response_template.md - Gravita media - judge no

### A.3 [tipo: valore]

- **Verifica** il deliverable non supera il limite di 2800 parole.
- **Pass se** il conteggio delle parole del corpo del deliverable non supera 2800.
- **Fail se** il corpo del deliverable supera 2800 parole.
- **Indifferente** la lunghezza delle singole sezioni.
- *non passa al judge:* Fonte task_spec.json, campo limite_parole - Gravita media - judge no

### A.4 [tipo: struttura]

- **Verifica** la quantificazione è esposta per passaggi successivi, ciascuno con il proprio importo.
- **Pass se** nella sezione della quantificazione ogni passaggio porta il proprio importo.
- **Fail se** la quantificazione è esposta con il solo importo finale, oppure almeno un passaggio non porta l'importo.
- **Indifferente** la forma tabellare o discorsiva della quantificazione.
- *non passa al judge:* Fonte public/01_task.md, richiesta sul percorso - Gravita media - judge no

### A.5 [tipo: struttura]

- **Verifica** ogni dato numerico utilizzato nella quantificazione porta il riferimento al documento da cui è ricavato.
- **Pass se** accanto a ciascun dato numerico compare il rinvio a uno degli allegati.
- **Fail se** almeno un dato numerico non porta alcun rinvio a un allegato.
- **Indifferente** la forma del rinvio.
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
- **Indifferente** il richiamo alle clausole di polizza e alle voci del conto economico, che non sono fonti normative.
- *non passa al judge:* Fonte private/fonti_chiuse.json - Gravita media - judge no


## B. Merito

Il fascicolo è esaminato al 30 settembre 2031: il periodo di indennizzo è ancora aperto, l'attività è ripresa a regime dal 18 agosto 2031, la perizia di parte è stata trasmessa e l'assicuratore ha messo tutto in riserva senza corrispondere acconti. Il prompt chiede il parere di copertura, la quantificazione esposta passaggio per passaggio con l'importo e il documento di ciascun dato, la valutazione una per una delle sette posizioni della lettera di riserva, la valutazione della perizia di parte, la distinzione fra profili che incidono e profili che non incidono, l'elenco di ciò che manca per chiudere il conteggio e la valutazione della lettura del perito sullo scostamento del margine dichiarato.

### B.1 [issue: I-01] [tipo: presenza]

- **Verifica** il deliverable afferma che la garanzia della sezione B opera.
- **Pass se** compare, riferita alla sezione B, una fra: «la garanzia opera», «la copertura è operante», «il sinistro è in garanzia».
- **Fail se** la garanzia è presentata come non operante, oppure l'operatività non è affermata.
- **Indifferente** il richiamo al numero della clausola.
- *non passa al judge:* Fonte clausola 1.2 delle condizioni particolari - Gravita alta - judge si

### B.2 [issue: I-01] [tipo: attribuzione]

- **Verifica** il deliverable fonda l'operatività sull'indennizzabilità del danno materiale ai sensi della sezione A, indipendentemente dall'importo liquidato.
- **Pass se** l'operatività è ricondotta all'indennizzabilità del danno materiale in sezione A, con l'indicazione che l'importo liquidato è irrilevante.
- **Fail se** l'operatività è fondata sull'importo liquidato in sezione A, oppure il presupposto non è indicato.
- **Indifferente** il richiamo al numero della clausola.
- *non passa al judge:* Fonte clausola 1.2 delle condizioni particolari - Gravita alta - judge si

### B.3 [issue: I-01] [tipo: presenza]

- **Verifica** il deliverable afferma che la macchina continua è ricompresa nella partita macchinario, attrezzature e impianti della sezione A.
- **Pass se** compare l'indicazione che il bene danneggiato è ricompreso nella partita macchinario, attrezzature e impianti.
- **Fail se** l'affermazione non compare, oppure il bene è presentato come non assicurato.
- **Indifferente** l'indicazione della somma assicurata della partita.
- *non passa al judge:* Fonte sezione A della scheda di polizza - Gravita alta - judge si

### B.4 [issue: I-02] [tipo: presenza]

- **Verifica** il deliverable afferma che la tesi del punto 1 della lettera di riserva non regge.
- **Pass se** compare, riferita al punto 1 della lettera di riserva, una fra: «non regge», «non è fondata», «non è sostenibile».
- **Fail se** la tesi è presentata come fondata, oppure non è valutata.
- **Indifferente** il tono con cui la valutazione è espressa.
- *non passa al judge:* Fonte punto 1 della lettera di riserva - Gravita alta - judge si

### B.5 [issue: I-02] [tipo: attribuzione]

- **Verifica** il deliverable fonda quella valutazione sulla circostanza che la scheda assicura per partite e non elenca i singoli beni.
- **Pass se** la valutazione è ricondotta alla struttura per partite della sezione A della scheda.
- **Fail se** la valutazione è affermata senza indicare il dato della scheda su cui si fonda.
- **Indifferente** l'indicazione del numero delle partite.
- *non passa al judge:* Fonte sezione A della scheda di polizza - Gravita alta - judge si

### B.6 [issue: I-03] [tipo: presenza]

- **Verifica** il deliverable afferma che la tesi del punto 7 della lettera di riserva non regge.
- **Pass se** compare, riferita al punto 7 della lettera di riserva, una fra: «non regge», «non è fondata», «non è sostenibile».
- **Fail se** la tesi è presentata come fondata, oppure non è valutata.
- **Indifferente** il tono con cui la valutazione è espressa.
- *non passa al judge:* Fonte punto 7 della lettera di riserva - Gravita alta - judge si

### B.7 [issue: I-03] [tipo: attribuzione]

- **Verifica** il deliverable fonda quella valutazione sul rapporto dei vigili del fuoco, che riferisce l'interdizione all'area del reparto e non all'attività dello stabilimento.
- **Pass se** la valutazione è ricondotta al paragrafo del rapporto dei vigili del fuoco sui provvedimenti.
- **Fail se** la valutazione è affermata senza il riscontro nel rapporto dei vigili del fuoco.
- **Indifferente** l'indicazione del numero del paragrafo.
- *non passa al judge:* Fonte paragrafo 6 del rapporto dei vigili del fuoco - Gravita alta - judge si

### B.8 [issue: I-03] [tipo: presenza]

- **Verifica** il deliverable afferma che l'esclusione riguarda i provvedimenti dell'autorità non connessi al danno materiale.
- **Pass se** compare l'indicazione che l'esclusione riguarda i provvedimenti non connessi al danno materiale.
- **Fail se** l'affermazione non compare, oppure l'esclusione è presentata come riferita a ogni provvedimento dell'autorità.
- **Indifferente** il richiamo alla lettera della clausola.
- *non passa al judge:* Fonte clausola 12.1, lettera a), delle condizioni particolari - Gravita alta - judge si

### B.9 [issue: I-04] [tipo: valore]

- **Verifica** il deliverable indica l'11 gennaio 2031 come giorno di decorrenza del periodo di indennizzo.
- **Pass se** compare «11 gennaio 2031» come giorno di decorrenza del periodo di indennizzo. compare «11/01/2031» come giorno di decorrenza del periodo di indennizzo.
- **Fail se** è indicato un giorno di decorrenza diverso, oppure la decorrenza non è indicata.
- **Indifferente** l'indicazione dell'ora del sinistro.
- *non passa al judge:* Fonte clausola 3.1 delle condizioni particolari; date_verificate.md - Gravita alta - judge no

### B.10 [issue: I-04] [tipo: valore]

- **Verifica** il deliverable indica l'11 gennaio 2032 come scadenza del periodo di indennizzo.
- **Pass se** compare «11 gennaio 2032» come scadenza del periodo di indennizzo. compare «11/01/2032» come scadenza del periodo di indennizzo.
- **Fail se** è indicata una scadenza diversa, oppure la scadenza non è indicata.
- **Indifferente** l'indicazione del numero di mesi.
- *non passa al judge:* Fonte periodo indicato nella scheda di polizza; date_verificate.md - Gravita alta - judge no

### B.11 [issue: I-05] [tipo: presenza]

- **Verifica** il deliverable afferma che la scadenza del periodo di indennizzo non si proroga pur cadendo in giorno festivo.
- **Pass se** compare l'indicazione che la scadenza non si proroga perché è un termine convenzionale di durata e non un termine per l'adempimento.
- **Fail se** l'affermazione non compare, oppure la scadenza è presentata come prorogabile.
- **Indifferente** il richiamo al numero della clausola.
- *non passa al judge:* Fonte clausola 3.3 delle condizioni particolari - Gravita alta - judge si

### B.12 [issue: I-05] [tipo: assenza]

- **Verifica** il deliverable non indica il 12 gennaio 2032 come scadenza del periodo di indennizzo.
- **Fail se** il 12 gennaio 2032 è indicato come scadenza del periodo di indennizzo.
- **Indifferente** la menzione del giorno della settimana in cui la scadenza cade.
- *non passa al judge:* Fonte clausola 3.3 delle condizioni particolari - Gravita alta - judge si

### B.13 [issue: I-06] [tipo: presenza]

- **Verifica** il deliverable afferma che al 30 settembre 2031 il periodo di indennizzo è ancora aperto.
- **Pass se** compare, riferita alla data di riferimento, una fra: «il periodo di indennizzo è ancora aperto», «il periodo non è scaduto», «la garanzia è ancora in corso».
- **Fail se** il periodo è presentato come chiuso, oppure lo stato del periodo non è affermato.
- **Indifferente** l'indicazione dei giorni residui.
- *non passa al judge:* Fonte data di riferimento; scadenza calcolata - Gravita alta - judge si

### B.14 [issue: I-06] [tipo: assenza]

- **Verifica** il deliverable non afferma che il periodo di indennizzo si è chiuso con la ripresa a regime del 18 agosto 2031.
- **Fail se** compare l'affermazione che il periodo di indennizzo si è chiuso con la ripresa a regime.
- **Indifferente** l'indicazione che dopo la ripresa a regime non risulta ulteriore perdita.
- *non passa al judge:* Fonte clausola 3.2 delle condizioni particolari - Gravita alta - judge si

### B.15 [issue: I-07] [tipo: valore]

- **Verifica** il deliverable indica in euro 6.750.000,00 il margine di contribuzione dell'esercizio anteriore al sinistro.
- **Pass se** compare «euro 6.750.000,00» come margine di contribuzione dell'esercizio 2030. compare «6.750.000,00» come margine di contribuzione dell'esercizio 2030.
- **Fail se** è indicato un margine diverso, oppure il margine di riferimento non è indicato.
- **Indifferente** l'indicazione del valore della produzione e dei costi variabili.
- *non passa al judge:* Fonte conto economico 2030 - Gravita alta - judge no

### B.16 [issue: I-07] [tipo: attribuzione]

- **Verifica** il deliverable ricava il margine di contribuzione dal conto economico 2030 come differenza fra valore della produzione e costi variabili di produzione.
- **Pass se** il margine è ricondotto alla differenza fra le due voci del conto economico 2030.
- **Fail se** il margine è affermato senza indicare le voci da cui è ricavato.
- **Indifferente** l'indicazione degli importi delle singole voci variabili.
- *non passa al judge:* Fonte conto economico 2030; clausola 2.1 delle condizioni particolari - Gravita alta - judge si

### B.17 [issue: I-07] [tipo: assenza]

- **Verifica** il deliverable non usa il margine dichiarato in polizza come margine di riferimento per il calcolo della perdita.
- **Fail se** il margine di euro 5.400.000,00 è usato come base per il calcolo del margine giornaliero o della perdita.
- **Indifferente** l'uso del margine dichiarato come parametro della regola proporzionale.
- *non passa al judge:* Fonte clausole 2.1 e 4.1 delle condizioni particolari - Gravita alta - judge si

### B.18 [issue: I-08] [tipo: valore]

- **Verifica** il deliverable indica in euro 18.750,00 il margine giornaliero.
- **Pass se** compare «euro 18.750,00» come margine giornaliero. compare «18.750,00» come margine giornaliero.
- **Fail se** è indicato un margine giornaliero diverso, oppure il margine giornaliero non è calcolato.
- **Indifferente** l'arrotondamento dei decimali.
- *non passa al judge:* Fonte computo verificato; clausola 4.1 delle condizioni particolari - Gravita alta - judge no

### B.19 [issue: I-08] [tipo: valore]

- **Verifica** il deliverable indica in trecentosessanta giorni la base convenzionale di computo del margine giornaliero.
- **Pass se** compare «trecentosessanta» come base di computo. compare «360 giorni» come base di computo.
- **Fail se** è indicata una base diversa, oppure la base non è indicata.
- **Indifferente** il richiamo al numero della clausola.
- *non passa al judge:* Fonte clausola 4.1 delle condizioni particolari - Gravita alta - judge no

### B.20 [issue: I-09] [tipo: valore]

- **Verifica** il deliverable indica in settantadue i giorni di fermo totale e in centoquarantasette i giorni di capacità ridotta.
- **Pass se** compaiono «72» e «147» come giorni dei due periodi. compaiono «settantadue» e «centoquarantasette» come giorni dei due periodi.
- **Fail se** è indicato un numero diverso per uno dei due periodi, oppure uno dei due periodi non è quantificato.
- **Indifferente** l'ordine in cui i due periodi sono esposti.
- *non passa al judge:* Fonte relazione di stabilimento; date_verificate.md - Gravita alta - judge no

### B.21 [issue: I-09] [tipo: valore]

- **Verifica** il deliverable indica il 24 marzo 2031 come inizio della ripresa parziale e il 18 agosto 2031 come ripresa a regime.
- **Pass se** compaiono «24 marzo 2031» e «18 agosto 2031» come date delle due riprese.
- **Fail se** è indicata una data diversa per una delle due riprese, oppure una delle due date non compare.
- **Indifferente** l'ordine in cui le due date sono esposte.
- *non passa al judge:* Fonte cronologia della relazione di stabilimento; date_verificate.md - Gravita alta - judge no

### B.22 [issue: I-10] [tipo: presenza]

- **Verifica** il deliverable afferma che nel periodo di capacità ridotta la perdita si determina applicando al margine giornaliero la percentuale di riduzione della capacità.
- **Pass se** compare l'indicazione che nel periodo di capacità ridotta si applica al margine giornaliero la percentuale di riduzione della capacità.
- **Fail se** l'affermazione non compare, oppure è applicato l'intero margine giornaliero.
- **Indifferente** il richiamo al numero della clausola.
- *non passa al judge:* Fonte clausola 4.2 delle condizioni particolari - Gravita alta - judge si

### B.23 [issue: I-10] [tipo: valore]

- **Verifica** il deliverable indica nel quarantacinque per cento la percentuale di riduzione della capacità nel periodo di ripresa parziale.
- **Pass se** compare «45 per cento» come percentuale di riduzione della capacità. compare «quarantacinque per cento» come percentuale di riduzione della capacità.
- **Fail se** è indicata una percentuale diversa, oppure la percentuale di riduzione non è indicata.
- **Indifferente** l'indicazione della capacità residua del cinquantacinque per cento.
- *non passa al judge:* Fonte tabella della capacità della relazione di stabilimento - Gravita alta - judge no

### B.24 [issue: I-11] [tipo: valore]

- **Verifica** il deliverable indica in euro 1.350.000,00 la perdita del periodo di fermo totale e in euro 1.240.312,50 quella del periodo di capacità ridotta.
- **Pass se** compaiono «euro 1.350.000,00» ed «euro 1.240.312,50» come perdite dei due periodi. compaiono «1.350.000,00» e «1.240.312,50» come perdite dei due periodi.
- **Fail se** è indicato un importo diverso per uno dei due periodi, oppure uno dei due importi non compare.
- **Indifferente** l'ordine in cui i due importi sono esposti.
- *non passa al judge:* Fonte computo verificato - Gravita alta - judge no

### B.25 [issue: I-11] [tipo: valore]

- **Verifica** il deliverable indica in euro 2.590.312,50 la perdita lorda.
- **Pass se** compare «euro 2.590.312,50» come perdita lorda. compare «2.590.312,50» come perdita lorda.
- **Fail se** è indicata una perdita lorda diversa, oppure la perdita lorda non è calcolata.
- **Indifferente** l'arrotondamento dei decimali.
- *non passa al judge:* Fonte computo verificato - Gravita alta - judge no

### B.26 [issue: I-11] [tipo: assenza]

- **Verifica** il deliverable non determina la perdita lorda sommando i margini mensili risultanti dalla situazione gestionale 2031.
- **Fail se** la perdita lorda è ricavata dai margini mensili della situazione gestionale invece che dal margine giornaliero convenzionale.
- **Indifferente** l'uso della situazione gestionale come riscontro dell'andamento effettivo.
- *non passa al judge:* Fonte clausola 4.1 delle condizioni particolari; situazione gestionale 2031 - Gravita alta - judge si

### B.27 [issue: I-12] [tipo: valore]

- **Verifica** il deliverable indica in euro 187.500,00 l'importo della franchigia.
- **Pass se** compare «euro 187.500,00» come importo della franchigia. compare «187.500,00» come importo della franchigia.
- **Fail se** è indicato un importo diverso, oppure la franchigia non è quantificata in euro.
- **Indifferente** l'indicazione dei dieci giorni.
- *non passa al judge:* Fonte computo verificato; clausola 6.1 delle condizioni particolari - Gravita alta - judge no

### B.28 [issue: I-12] [tipo: presenza]

- **Verifica** il deliverable afferma che la franchigia si detrae moltiplicando i giorni di franchigia per il margine giornaliero.
- **Pass se** compare l'indicazione che la franchigia si ottiene moltiplicando i giorni di franchigia per il margine giornaliero.
- **Fail se** l'affermazione non compare, oppure la franchigia è trattata come importo fisso.
- **Indifferente** il richiamo al numero della clausola.
- *non passa al judge:* Fonte clausola 6.1 delle condizioni particolari - Gravita alta - judge si

### B.29 [issue: I-12] [tipo: valore]

- **Verifica** il deliverable indica in euro 2.402.812,50 la perdita al netto della franchigia.
- **Pass se** compare «euro 2.402.812,50» come perdita al netto della franchigia. compare «2.402.812,50» come perdita al netto della franchigia.
- **Fail se** è indicato un importo diverso, oppure il passaggio non compare.
- **Indifferente** l'arrotondamento dei decimali.
- *non passa al judge:* Fonte computo verificato - Gravita alta - judge no

### B.30 [issue: I-12] [tipo: assenza]

- **Verifica** il deliverable non detrae i giorni di franchigia dai giorni di fermo prima di calcolare la perdita del periodo di capacità ridotta.
- **Fail se** la franchigia è applicata sottraendo dieci giorni dal periodo di fermo totale.
- **Indifferente** la menzione dei giorni di franchigia nella descrizione della cronologia.
- *non passa al judge:* Fonte clausola 6.1 delle condizioni particolari - Gravita media - judge si

### B.31 [issue: I-13] [tipo: qualificazione]

- **Verifica** il deliverable qualifica la rettifica per l'andamento dell'attività come operante in diminuzione.
- **Pass se** compare, riferita alla rettifica, una fra: «in diminuzione», «riduce la perdita», «segno negativo».
- **Fail se** la rettifica è qualificata come operante in aumento, oppure è presentata come non applicabile, oppure la qualificazione non compare.
- **Indifferente** il richiamo al numero della clausola.
- *non passa al judge:* Fonte clausole 5.1 e 5.2 delle condizioni particolari - Gravita alta - judge si

### B.32 [issue: I-13] [tipo: attribuzione]

- **Verifica** il deliverable fonda il segno della rettifica sui dati di portafoglio ordini della relazione di stabilimento.
- **Pass se** il segno della rettifica è ricondotto ai dati di portafoglio ordini o alla stima della relazione di stabilimento.
- **Fail se** il segno è affermato senza indicare i dati su cui si fonda.
- **Indifferente** l'indicazione della variazione percentuale del quarto trimestre.
- *non passa al judge:* Fonte paragrafi 4 e 5 della relazione di stabilimento - Gravita alta - judge si

### B.33 [issue: I-13] [tipo: valore]

- **Verifica** il deliverable indica nel sei per cento la misura della rettifica in diminuzione.
- **Pass se** compare «6 per cento» come misura della rettifica. compare «sei per cento» come misura della rettifica.
- **Fail se** è indicata una misura diversa, oppure la misura non è indicata.
- **Indifferente** il segno con cui la misura è scritta.
- *non passa al judge:* Fonte paragrafo 5 della relazione di stabilimento - Gravita alta - judge no

### B.34 [issue: I-14] [tipo: valore]

- **Verifica** il deliverable indica in euro 2.258.643,75 la perdita rettificata per l'andamento.
- **Pass se** compare «euro 2.258.643,75» come perdita rettificata. compare «2.258.643,75» come perdita rettificata.
- **Fail se** è indicato un importo diverso, oppure il passaggio non compare.
- **Indifferente** l'arrotondamento dei decimali.
- *non passa al judge:* Fonte computo verificato - Gravita alta - judge no

### B.35 [issue: I-14] [tipo: assenza]

- **Verifica** il deliverable non indica euro 2.498.925,00 come perdita rettificata.
- **Fail se** l'importo di euro 2.498.925,00 è indicato come perdita rettificata.
- **Indifferente** la menzione di quell'importo come risultato della perizia di parte.
- *non passa al judge:* Fonte computo verificato; paragrafo 5 della perizia di parte - Gravita alta - judge si

### B.36 [issue: I-15] [tipo: presenza]

- **Verifica** il deliverable rileva che la perizia di parte applica una rettifica in aumento del quattro per cento.
- **Pass se** compare l'indicazione che la perizia di parte applica una rettifica in aumento del quattro per cento.
- **Fail se** il rilievo non compare, oppure la rettifica della perizia è presentata come in diminuzione.
- **Indifferente** il richiamo al numero del paragrafo.
- *non passa al judge:* Fonte paragrafo 5 della perizia di parte - Gravita alta - judge si

### B.37 [issue: I-15] [tipo: presenza]

- **Verifica** il deliverable rileva che la motivazione della perizia contrasta con i dati di portafoglio ordini dell'assicurato.
- **Pass se** compare l'indicazione che la motivazione della perizia contrasta con i dati di portafoglio ordini della relazione di stabilimento.
- **Fail se** il rilievo non compare, oppure la motivazione è presentata come sostenuta dai documenti.
- **Indifferente** l'indicazione della fonte di settore invocata dalla perizia.
- *non passa al judge:* Fonte paragrafo 5 della perizia di parte; paragrafo 4 della relazione di stabilimento - Gravita alta - judge si

### B.38 [issue: I-16] [tipo: valore]

- **Verifica** il deliverable indica in euro 5.400.000,00 il margine dichiarato in polizza e in euro 6.750.000,00 quello effettivo dell'esercizio anteriore.
- **Pass se** compaiono «euro 5.400.000,00» ed «euro 6.750.000,00» come margine dichiarato e margine effettivo.
- **Fail se** è indicato un importo diverso per uno dei due valori, oppure uno dei due valori non compare.
- **Indifferente** l'ordine in cui i due valori sono esposti.
- *non passa al judge:* Fonte scheda di polizza; conto economico 2030 - Gravita alta - judge no

### B.39 [issue: I-16] [tipo: valore]

- **Verifica** il deliverable indica nel venti per cento il grado di sottoassicurazione e nell'ottanta per cento la quota indennizzabile.
- **Pass se** compaiono «20 per cento» e «80 per cento» come grado di sottoassicurazione e quota indennizzabile. compaiono «venti per cento» e «ottanta per cento» come grado di sottoassicurazione e quota indennizzabile.
- **Fail se** è indicata una percentuale diversa per uno dei due valori, oppure uno dei due valori non compare.
- **Indifferente** l'ordine in cui i due valori sono esposti.
- *non passa al judge:* Fonte computo verificato - Gravita alta - judge no

### B.40 [issue: I-16] [tipo: qualificazione]

- **Verifica** il deliverable qualifica la fattispecie come assicurazione parziale con riduzione proporzionale dell'indennizzo.
- **Pass se** compare, riferita alla fattispecie, una fra: «assicurazione parziale», «regola proporzionale», «riduzione proporzionale dell'indennizzo».
- **Fail se** la fattispecie è qualificata diversamente, oppure la qualificazione non compare.
- **Indifferente** il richiamo al numero della clausola o dell'articolo.
- *non passa al judge:* Fonte clausola 8.3 delle condizioni particolari; articolo 8.1 delle condizioni generali - Gravita alta - judge si

### B.41 [issue: I-17] [tipo: presenza]

- **Verifica** il deliverable afferma che l'osservazione del paragrafo 8 della perizia di parte non regge.
- **Pass se** compare, riferita a quell'osservazione, una fra: «non regge», «non è fondata», «non è sostenibile».
- **Fail se** l'osservazione è presentata come fondata, oppure non è valutata.
- **Indifferente** il tono con cui la valutazione è espressa.
- *non passa al judge:* Fonte paragrafo 8 della perizia di parte - Gravita alta - judge si

### B.42 [issue: I-17] [tipo: presenza]

- **Verifica** il deliverable distingue la somma assicurata, che opera come limite massimo di indennizzo, dal margine dichiarato, che opera come parametro della proporzione.
- **Pass se** compare la distinzione fra la funzione della somma assicurata e quella del margine dichiarato.
- **Fail se** la distinzione non compare, oppure i due parametri sono trattati come equivalenti.
- **Indifferente** il richiamo ai numeri delle clausole.
- *non passa al judge:* Fonte clausole 8.1 e 8.2 delle condizioni particolari - Gravita alta - judge si

### B.43 [issue: I-18] [tipo: valore]

- **Verifica** il deliverable indica in euro 1.806.915,00 l'indennizzo sulla perdita di margine.
- **Pass se** compare «euro 1.806.915,00» come indennizzo sulla perdita di margine. compare «1.806.915,00» come indennizzo sulla perdita di margine.
- **Fail se** è indicato un importo diverso, oppure il passaggio non compare.
- **Indifferente** l'arrotondamento dei decimali.
- *non passa al judge:* Fonte computo verificato - Gravita alta - judge no

### B.44 [issue: I-19] [tipo: valore]

- **Verifica** il deliverable indica in euro 340.000,00 i maggiori costi richiesti e in euro 200.000,00 il sublimite previsto dalla scheda di polizza.
- **Pass se** compaiono «euro 340.000,00» ed «euro 200.000,00» come importo richiesto e sublimite.
- **Fail se** è indicato un importo diverso per uno dei due valori, oppure uno dei due valori non compare.
- **Indifferente** l'ordine in cui i due valori sono esposti.
- *non passa al judge:* Fonte paragrafo 6 della perizia di parte; scheda di polizza - Gravita alta - judge no

### B.45 [issue: I-19] [tipo: valore]

- **Verifica** il deliverable indica in euro 160.000,00 i maggiori costi indennizzabili.
- **Pass se** compare «euro 160.000,00» come maggiori costi indennizzabili. compare «160.000,00» come maggiori costi indennizzabili.
- **Fail se** è indicato un importo diverso, oppure il passaggio non compare.
- **Indifferente** l'ordine dei due passaggi, sublimite e proporzione.
- *non passa al judge:* Fonte computo verificato - Gravita alta - judge no

### B.46 [issue: I-19] [tipo: presenza]

- **Verifica** il deliverable afferma che il sublimite per i maggiori costi è a sua volta soggetto alla riduzione proporzionale.
- **Pass se** compare l'indicazione che la riduzione proporzionale si applica anche ai maggiori costi entro il sublimite.
- **Fail se** l'affermazione non compare, oppure i maggiori costi sono sottratti alla riduzione proporzionale.
- **Indifferente** l'ordine in cui i due passaggi sono esposti.
- *non passa al judge:* Fonte clausola 8.3 delle condizioni particolari; scheda di polizza - Gravita alta - judge si

### B.47 [issue: I-20] [tipo: presenza]

- **Verifica** il deliverable afferma che i maggiori costi sono indennizzabili nella misura in cui hanno evitato una perdita di margine di importo non inferiore.
- **Pass se** compare l'indicazione della condizione di indennizzabilità dei maggiori costi.
- **Fail se** l'affermazione non compare, oppure i maggiori costi sono presentati come indennizzabili senza condizione.
- **Indifferente** il richiamo al numero della clausola.
- *non passa al judge:* Fonte clausola 7.2 delle condizioni particolari - Gravita media - judge si

### B.48 [issue: I-20] [tipo: presenza]

- **Verifica** il deliverable afferma che il fascicolo non contiene il raffronto fra maggiori costi sostenuti e perdita evitata.
- **Pass se** compare, riferita a quel raffronto, una fra: «non risulta dagli atti», «documentazione in corso di raccolta», «non verificabile sui documenti disponibili».
- **Fail se** il raffronto è dato per svolto, oppure la lacuna non è dichiarata.
- **Indifferente** l'indicazione dei documenti necessari.
- *non passa al judge:* Fonte paragrafo 6 della relazione di stabilimento - Gravita media - judge si

### B.49 [issue: I-21] [tipo: valore]

- **Verifica** il deliverable indica in euro 1.966.915,00 l'indennizzo complessivo.
- **Pass se** compare «euro 1.966.915,00» come indennizzo complessivo. compare «1.966.915,00» come indennizzo complessivo.
- **Fail se** è indicato un importo diverso, oppure l'indennizzo complessivo non è calcolato.
- **Indifferente** l'arrotondamento dei decimali.
- *non passa al judge:* Fonte computo verificato - Gravita alta - judge no

### B.50 [issue: I-21] [tipo: presenza]

- **Verifica** il deliverable afferma che l'indennizzo complessivo è contenuto entro la somma assicurata di euro 6.000.000,00.
- **Pass se** compare l'indicazione che l'indennizzo è contenuto entro la somma assicurata.
- **Fail se** l'affermazione non compare, oppure l'indennizzo è presentato come eccedente la somma assicurata.
- **Indifferente** l'indicazione del margine residuo rispetto alla somma assicurata.
- *non passa al judge:* Fonte somma assicurata nella scheda di polizza - Gravita media - judge si

### B.51 [issue: I-22] [tipo: valore]

- **Verifica** il deliverable indica in euro 2.838.925,00 la quantificazione della perizia di parte e in euro 872.010,00 lo scostamento rispetto all'indennizzo verificato.
- **Pass se** compaiono «euro 2.838.925,00» ed «euro 872.010,00» come quantificazione della perizia e scostamento.
- **Fail se** è indicato un importo diverso per uno dei due valori, oppure uno dei due valori non compare.
- **Indifferente** l'ordine in cui i due valori sono esposti.
- *non passa al judge:* Fonte paragrafo 7 della perizia di parte; computo verificato - Gravita alta - judge no

### B.52 [issue: I-22] [tipo: presenza]

- **Verifica** il deliverable riconduce lo scostamento a tre cause: il segno della rettifica, la mancata applicazione della riduzione proporzionale e il superamento del sublimite.
- **Pass se** compaiono le tre cause dello scostamento.
- **Fail se** sono indicate meno di tre cause, oppure lo scostamento è affermato senza indicarne le cause.
- **Indifferente** l'ordine in cui le tre cause sono esposte.
- *non passa al judge:* Fonte computo verificato; perizia di parte - Gravita alta - judge si

### B.53 [issue: I-23] [tipo: qualificazione]

- **Verifica** il deliverable qualifica la perizia come perizia di parte non vincolante per l'assicuratore.
- **Pass se** compare, riferita alla perizia, una fra: «perizia di parte», «non vincolante per l'assicuratore», «predisposta su incarico dell'assicurato».
- **Fail se** la perizia è presentata come vincolante, oppure la qualificazione non compare.
- **Indifferente** il richiamo al numero della clausola.
- *non passa al judge:* Fonte clausola 10.3 delle condizioni particolari; intestazione della perizia - Gravita alta - judge si

### B.54 [issue: I-23] [tipo: assenza]

- **Verifica** il deliverable non afferma che il rifiuto di vincolatività contenuto nel punto 2 della lettera di riserva è infondato.
- **Fail se** compare l'affermazione che l'assicuratore non può rifiutare la vincolatività della perizia di parte.
- **Indifferente** l'indicazione che la posizione dell'assicuratore su quel punto è conforme alle condizioni.
- *non passa al judge:* Fonte punto 2 della lettera di riserva; clausola 10.3 delle condizioni particolari - Gravita alta - judge si

### B.55 [issue: I-24] [tipo: presenza]

- **Verifica** il deliverable afferma che le condizioni particolari prevedono un acconto fino al cinquanta per cento dell'importo non contestato.
- **Pass se** compare l'indicazione dell'acconto fino al cinquanta per cento dell'importo non contestato.
- **Fail se** l'affermazione non compare, oppure l'acconto è presentato come non previsto.
- **Indifferente** il richiamo al numero della clausola.
- *non passa al judge:* Fonte clausola 11.2 delle condizioni particolari - Gravita alta - judge si

### B.56 [issue: I-24] [tipo: presenza]

- **Verifica** il deliverable indica come azione la richiesta dell'acconto sull'importo non contestato.
- **Pass se** compare l'indicazione di chiedere l'acconto sull'importo non contestato.
- **Fail se** l'azione non compare.
- **Indifferente** l'importo proposto per l'acconto.
- *non passa al judge:* Fonte clausola 11.2 delle condizioni particolari; punto 6 della lettera di riserva - Gravita alta - judge si

### B.57 [issue: I-24] [tipo: assenza]

- **Verifica** il deliverable non afferma che l'acconto presuppone la determinazione definitiva del danno.
- **Fail se** compare l'affermazione che l'acconto è dovuto solo dopo la determinazione definitiva dell'ammontare del danno.
- **Indifferente** l'indicazione dei sessanta giorni dalla denuncia.
- *non passa al judge:* Fonte clausola 11.2 delle condizioni particolari - Gravita alta - judge si

### B.58 [issue: I-25] [tipo: presenza]

- **Verifica** il deliverable afferma che la quantificazione non è definitiva.
- **Pass se** compare, riferita alla quantificazione, una fra: «non definitiva», «provvisoria», «da chiudere all'esito dei dati mancanti».
- **Fail se** la quantificazione è presentata come definitiva, oppure lo stato della quantificazione non è affermato.
- **Indifferente** l'indicazione della data entro cui i dati potrebbero essere disponibili.
- *non passa al judge:* Fonte paragrafo 6 della relazione di stabilimento; situazione gestionale 2031 - Gravita alta - judge si

### B.59 [issue: I-25] [tipo: presenza]

- **Verifica** il deliverable elenca i dati mancanti per la chiusura della quantificazione.
- **Pass se** compaiono almeno due elementi fra dati gestionali da settembre a dicembre 2031, rilevazione dei costi variabili non sostenuti e documentazione dei maggiori costi.
- **Fail se** i dati mancanti non sono elencati, oppure ne è indicato uno solo.
- **Indifferente** l'ordine in cui gli elementi sono elencati.
- *non passa al judge:* Fonte paragrafo 6 della relazione di stabilimento - Gravita alta - judge si

### B.60 [issue: I-25] [tipo: assenza]

- **Verifica** il deliverable non afferma che i dati mancanti impediscono ogni quantificazione.
- **Fail se** compare l'affermazione che in assenza dei dati mancanti nessuna quantificazione è possibile.
- **Indifferente** l'indicazione che la quantificazione è provvisoria.
- *non passa al judge:* Fonte paragrafo 6 della relazione di stabilimento - Gravita alta - judge si


## C. Date, valori calcolati e chiusura

### C.1 [issue: N-01] [tipo: assenza]

- **Verifica** il deliverable non segnala una decadenza per tardiva denuncia, ne mette in discussione la tempestivita della denuncia.
- **Fail se** la denuncia è presentata come tardiva o come fonte di decadenza.
- **Indifferente** la menzione della data della denuncia nella cronologia.
- *non passa al judge:* Fonte challenge map, N-01 - Gravita alta - judge si

### C.2 [issue: N-02] [tipo: assenza]

- **Verifica** il deliverable non attribuisce all'ora del sinistro o al fermo programmato di fine settimana effetti sull'operatività della garanzia o sulla decorrenza.
- **Fail se** all'ora del sinistro o al fermo programmato di fine settimana sono attribuiti effetti sull'operatività o sulla decorrenza.
- **Indifferente** la menzione dell'ora nella descrizione dell'evento.
- *non passa al judge:* Fonte challenge map, N-02 - Gravita media - judge si

### C.3 [issue: N-03] [tipo: assenza]

- **Verifica** il deliverable non segnala come ostacolo la procedura di nomina dei periti prevista dalle condizioni particolari.
- **Fail se** la procedura di nomina dei periti compare fra i profili di rischio o fra gli ostacoli.
- **Indifferente** la menzione della procedura nella descrizione dell'accertamento del danno.
- *non passa al judge:* Fonte challenge map, N-03 - Gravita media - judge si

### C.4 [issue: N-04] [tipo: assenza]

- **Verifica** il deliverable non presenta come carenza di copertura la circostanza che le somme assicurate distinte delle due sezioni siano autonome.
- **Fail se** l'autonomia delle somme assicurate delle due sezioni compare fra i profili di sottoassicurazione o di carenza di copertura.
- **Indifferente** la menzione delle somme assicurate della sezione A nella descrizione della polizza.
- *non passa al judge:* Fonte challenge map, N-04 - Gravita media - judge si

### C.5 [issue: N-05] [tipo: assenza]

- **Verifica** il deliverable non presenta come inadempimento dell'assicurato l'affidamento in lavorazione esterna delle commesse.
- **Fail se** l'affidamento in lavorazione esterna compare fra gli inadempimenti o fra le violazioni degli obblighi dell'assicurato.
- **Indifferente** la menzione dell'affidamento come fonte dei maggiori costi.
- *non passa al judge:* Fonte challenge map, N-05 - Gravita media - judge si

### C.6 [issue: N-06] [tipo: assenza]

- **Verifica** il deliverable non applica alla quantificazione dei danni indiretti la franchigia della sezione A.
- **Fail se** una franchigia in euro della sezione A è detratta dalla quantificazione dei danni indiretti.
- **Indifferente** la menzione delle franchigie della sezione A nella descrizione della polizza.
- *non passa al judge:* Fonte challenge map, N-06 - Gravita alta - judge si

### C.7 [issue: N-07] [tipo: assenza]

- **Verifica** il deliverable non esclude dal computo il periodo del fermo programmato di luglio 2031.
- **Fail se** i giorni del fermo programmato di luglio 2031 sono esclusi dal computo dei giorni di capacità ridotta.
- **Indifferente** la menzione del fermo programmato fra gli elementi dell'andamento.
- *non passa al judge:* Fonte challenge map, N-07 - Gravita media - judge si

### C.8 [issue: N-08] [tipo: assenza]

- **Verifica** il deliverable non segnala, a fronte della quietanza del premio in atti, profili di operatività della garanzia legati al pagamento del premio.
- **Fail se** il pagamento del premio compare fra i profili che incidono sull'operatività della garanzia.
- **Indifferente** la menzione della quietanza fra i dati della polizza.
- *non passa al judge:* Fonte challenge map, N-08 - Gravita media - judge si

### C.9 [issue: X-01] [tipo: assenza]

- **Verifica** simmetria del controllo: il deliverable non tratta come provata la perdita del periodo di capacità ridotta mentre tratta come non provato il raffronto sui maggiori costi.
- **Fail se** la perdita del periodo di capacità ridotta è data per provata e nello stesso deliverable il raffronto sui maggiori costi è dichiarato non verificabile, senza distinguere i due piani di prova.
- **Indifferente** l'ordine in cui i due punti sono trattati.
- *non passa al judge:* Fonte relazione di stabilimento; clausola 7.2 delle condizioni particolari - Gravita alta - judge si

### C.10 [issue: X-02] [tipo: assenza]

- **Verifica** divieto di presunzione dell'esito: il deliverable non afferma che l'assicuratore corrisponderà l'indennizzo determinato.
- **Fail se** compare l'affermazione che l'assicuratore pagherà o riconoscerà l'indennizzo determinato.
- **Indifferente** l'indicazione dei passaggi necessari per la determinazione dell'ammontare.
- *non passa al judge:* Fonte clausola 10.2 delle condizioni particolari; lettera di riserva - Gravita alta - judge si

### C.11 [issue: X-03] [tipo: assenza]

- **Verifica** sovra-segnalazione: il deliverable non presenta come profilo di rischio la facoltà di recesso dopo il sinistro prevista dalle condizioni generali.
- **Fail se** la facoltà di recesso dopo il sinistro compare fra i profili di rischio o fra i rilievi sulla polizza.
- **Indifferente** la menzione della facoltà di recesso fra le previsioni contrattuali applicabili.
- *non passa al judge:* Fonte articolo 9.1 delle condizioni generali - Gravita media - judge si
