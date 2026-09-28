# WF2-054 - Criteri atomizzati

Forma a campi. Ciò che sta sotto la riga non passa al judge.


## A. Forma dell'output (interamente verifica meccanica)

### A.1 [tipo: valore]

- **Verifica** sono prodotti entrambi i file richiesti, `agreement_redline.docx` e `risk_note.md`.
- **Pass se** i due file consegnati hanno nome `agreement_redline.docx` e `risk_note.md`.
- **Fail se** manca uno dei due file, oppure un file ha nome o estensione diversi.
- **Indifferente** la presenza di file aggiuntivi.
- *non passa al judge:* Fonte task_spec.json, campo deliverable - Gravita media - judge no

### A.2 [tipo: struttura]

- **Verifica** il file `agreement_redline.docx` contiene revisioni tracciate.
- **Pass se** il documento contiene almeno una cancellazione e almeno una inserzione tracciate.
- **Fail se** il documento non contiene revisioni tracciate, oppure le modifiche sono rese con marcatori nel testo.
- **Indifferente** il numero delle revisioni.
- *non passa al judge:* Fonte task_spec.json, campo deliverable - Gravita media - judge no

### A.3 [tipo: struttura]

- **Verifica** il file `risk_note.md` contiene, nell'ordine, le sei sezioni obbligatorie del template.
- **Pass se** le sei intestazioni di sezione compaiono nell'ordine indicato dal template.
- **Fail se** manca almeno una sezione o l'ordine è diverso.
- **Indifferente** la numerazione delle sottosezioni.
- *non passa al judge:* Fonte public/response_template.md - Gravita media - judge no

### A.4 [tipo: valore]

- **Verifica** il file `risk_note.md` non supera il limite di 2200 parole.
- **Pass se** il conteggio delle parole del corpo di `risk_note.md` non supera 2200.
- **Fail se** il corpo di `risk_note.md` supera 2200 parole.
- **Indifferente** la lunghezza delle singole sezioni.
- *non passa al judge:* Fonte task_spec.json, campo limite_parole - Gravita media - judge no

### A.5 [tipo: struttura]

- **Verifica** ogni rilievo della nota porta il riferimento alla clausola della bozza su cui incide e al documento che lo fonda.
- **Pass se** accanto a ciascun rilievo compaiono il numero della clausola e il rinvio a un allegato.
- **Fail se** almeno un rilievo omette il riferimento alla clausola o il rinvio all'allegato.
- **Indifferente** la forma del riferimento.
- *non passa al judge:* Fonte public/01_task.md, richiesta sulla fonte - Gravita media - judge no

### A.6 [tipo: struttura]

- **Verifica** per ciascun rilievo di livello la nota indica il valore previsto dalla bozza e quello ammesso dalla policy interna.
- **Pass se** per ciascun rilievo di livello compaiono i due valori.
- **Fail se** almeno un rilievo di livello omette uno dei due valori.
- **Indifferente** l'ordine in cui i due valori sono esposti.
- *non passa al judge:* Fonte public/01_task.md, richiesta sui livelli - Gravita media - judge no

### A.7 [tipo: presenza]

- **Verifica** la nota distingue i rilievi che impongono una modifica da quelli che non la impongono.
- **Pass se** compare una separazione fra i rilievi che impongono modifica e gli elementi che non la impongono.
- **Fail se** la nota presenta un elenco indistinto di osservazioni.
- **Indifferente** le etichette usate per la separazione.
- *non passa al judge:* Fonte public/response_template.md - Gravita media - judge no

### A.8 [tipo: assenza]

- **Verifica** la nota non richiama fonti normative estranee all'elenco chiuso del reference pack.
- **Fail se** compare un riferimento normativo che non figura in `private/fonti_chiuse.json`.
- **Indifferente** il richiamo alle clausole dell'accordo, ai paragrafi della policy e alle sezioni del questionario, che non sono fonti normative.
- *non passa al judge:* Fonte private/fonti_chiuse.json - Gravita media - judge no


## B. Merito

Il fascicolo è esaminato al 22 luglio 2031: la bozza non è sottoscritta, la decorrenza prevista è il 1 settembre 2031, il rapporto è classificato a rischio elevato e l'istruttoria non è chiusa. Il prompt chiede la bozza con revisioni tracciate e una nota che, per ciascun rilievo, indichi la clausola su cui incide, il documento che lo fonda e, per i rilievi di livello, i due valori a confronto; chiede inoltre le discrepanze fra questionario e dichiarazioni dell'accordo, i soggetti da approfondire, la separazione fra rilievi che impongono modifica e rilievi che non la impongono, la conclusione sull'apertura e la valutazione della lettura del responsabile dell'unità commerciale.

### B.1 [issue: I-01] [tipo: qualificazione]

- **Verifica** la nota qualifica le clausole 6.1 e 6.2 come traslazione sulla controparte di obblighi che restano in capo alla Banca.
- **Pass se** compare, riferita a quelle clausole, una fra: «traslazione di obblighi non trasferibili», «gli obblighi restano in capo alla Banca», «non delegabili alla controparte».
- **Fail se** le clausole sono presentate come ammissibili, oppure la qualificazione non compare.
- **Indifferente** il richiamo al numero del paragrafo della policy.
- *non passa al judge:* Fonte clausole 6.1 e 6.2 della bozza; paragrafo 2.1 della policy - Gravita alta - judge si

### B.2 [issue: I-01] [tipo: presenza]

- **Verifica** il redline sostituisce la clausola 6.2 sull'affidamento integrale alle verifiche della controparte.
- **Pass se** nel documento con revisioni tracciate la clausola 6.2 risulta cancellata o sostituita.
- **Fail se** la clausola 6.2 resta invariata nel documento con revisioni tracciate.
- **Indifferente** la formulazione sostitutiva proposta.
- *non passa al judge:* Fonte clausola 6.2 della bozza - Gravita alta - judge si

### B.3 [issue: I-01] [tipo: assenza]

- **Verifica** la nota non afferma che la Banca deve ripetere la verifica su tutti i clienti della controparte.
- **Fail se** compare l'affermazione che la Banca deve svolgere la verifica su tutti i clienti della controparte.
- **Indifferente** l'indicazione dei casi in cui la verifica sui clienti della controparte è dovuta.
- *non passa al judge:* Fonte paragrafo 2.3 della policy interna - Gravita alta - judge si

### B.4 [issue: I-02] [tipo: qualificazione]

- **Verifica** la nota individua nella banca rispondente il cliente della Banca ai fini della verifica.
- **Pass se** compare, riferita alla controparte, una fra: «è il cliente della Banca», «la verifica della Banca ha per oggetto la banca rispondente», «cliente ai fini della verifica».
- **Fail se** il cliente è individuato nella clientela della controparte, oppure è affermato che la Banca non ha alcun cliente da verificare, oppure l'individuazione non compare.
- **Indifferente** il richiamo al numero del paragrafo della policy.
- *non passa al judge:* Fonte paragrafo 2.2 della policy interna - Gravita alta - judge si

### B.5 [issue: I-03] [tipo: presenza]

- **Verifica** la nota rileva che la clausola 7.2 esclude i filtri autonomi della Banca sulle operazioni.
- **Pass se** compare l'indicazione che la clausola 7.2 esclude i filtri autonomi della Banca.
- **Fail se** il rilievo non compare, oppure la clausola è presentata come ammissibile.
- **Indifferente** il richiamo al numero della clausola.
- *non passa al judge:* Fonte clausola 7.2 della bozza - Gravita alta - judge si

### B.6 [issue: I-03] [tipo: presenza]

- **Verifica** la nota afferma che la policy interna impone i filtri autonomi su tutte le operazioni indipendentemente dai controlli della controparte.
- **Pass se** compare l'indicazione che i filtri autonomi sono imposti su tutte le operazioni.
- **Fail se** l'affermazione non compare, oppure i filtri sono presentati come facoltativi.
- **Indifferente** il richiamo al numero del paragrafo.
- *non passa al judge:* Fonte paragrafo 7.1 della policy interna - Gravita alta - judge si

### B.7 [issue: I-03] [tipo: presenza]

- **Verifica** il redline sostituisce la clausola 7.2.
- **Pass se** nel documento con revisioni tracciate la clausola 7.2 risulta cancellata o sostituita.
- **Fail se** la clausola 7.2 resta invariata nel documento con revisioni tracciate.
- **Indifferente** la formulazione sostitutiva proposta.
- *non passa al judge:* Fonte clausola 7.2 della bozza - Gravita alta - judge si

### B.8 [issue: I-03] [tipo: assenza]

- **Verifica** la nota non afferma che l'esclusione dei filtri autonomi è giustificata dall'esigenza di non duplicare i controlli o di non introdurre ritardi.
- **Fail se** compare l'affermazione che l'esclusione è giustificata da una di quelle due esigenze.
- **Indifferente** la menzione di quelle esigenze come motivazione addotta dalla bozza.
- *non passa al judge:* Fonte clausola 7.2 della bozza - Gravita alta - judge si

### B.9 [issue: I-04] [tipo: presenza]

- **Verifica** la nota rileva che la clausola 3.2 consente ai clienti della controparte di operare direttamente sul conto senza preventiva comunicazione.
- **Pass se** compare l'indicazione che la clausola 3.2 ammette l'utilizzo diretto del conto da parte di terzi senza preventiva comunicazione.
- **Fail se** il rilievo non compare, oppure la clausola è presentata come ammissibile.
- **Indifferente** il richiamo al numero della clausola.
- *non passa al judge:* Fonte clausola 3.2 della bozza - Gravita alta - judge si

### B.10 [issue: I-04] [tipo: presenza]

- **Verifica** la nota indica le tre condizioni che la policy interna pone all'utilizzo diretto del conto: autorizzazione espressa, identificazione preventiva dei soggetti abilitati e monitoraggio dedicato.
- **Pass se** compaiono le tre condizioni previste dalla policy.
- **Fail se** sono indicate meno di tre condizioni, oppure le condizioni non sono indicate.
- **Indifferente** l'ordine in cui le condizioni sono elencate.
- *non passa al judge:* Fonte paragrafo 5.2 della policy interna - Gravita alta - judge si

### B.11 [issue: I-04] [tipo: presenza]

- **Verifica** il redline sostituisce la clausola 3.2.
- **Pass se** nel documento con revisioni tracciate la clausola 3.2 risulta cancellata o sostituita.
- **Fail se** la clausola 3.2 resta invariata nel documento con revisioni tracciate.
- **Indifferente** la formulazione sostitutiva proposta.
- *non passa al judge:* Fonte clausola 3.2 della bozza - Gravita alta - judge si

### B.12 [issue: I-04] [tipo: assenza]

- **Verifica** la nota non afferma che l'utilizzo diretto del conto è ammissibile in quanto condizione della trattativa posta dalla controparte.
- **Fail se** compare l'affermazione che l'utilizzo diretto è ammissibile perché richiesto dalla controparte come condizione della trattativa.
- **Indifferente** la menzione della richiesta della controparte come circostanza di fatto.
- *non passa al judge:* Fonte nota dell'unità Pagamenti esteri; clausola 3.2 della bozza - Gravita alta - judge si

### B.13 [issue: I-05] [tipo: attribuzione]

- **Verifica** la nota fonda il rilievo sull'utilizzo diretto del conto anche sulla sezione 5 del questionario compilato dalla controparte.
- **Pass se** il rilievo è ricondotto alla sezione del questionario che dichiara l'utilizzo diretto e l'assenza di identificazione preventiva.
- **Fail se** il rilievo è fondato soltanto sulla clausola dell'accordo, senza il riscontro nel questionario.
- **Indifferente** il richiamo al numero della sezione.
- *non passa al judge:* Fonte sezione 5 del questionario di due diligence - Gravita alta - judge si

### B.14 [issue: I-06] [tipo: presenza]

- **Verifica** la nota rileva che il questionario indica quattro dipendenti nella giurisdizione di costituzione, uffici di rappresentanza in due giurisdizioni e un consiglio che si riunisce a distanza.
- **Pass se** compaiono almeno due dei tre elementi sulla struttura della controparte nella giurisdizione di costituzione.
- **Fail se** il rilievo non compare, oppure è indicato un solo elemento.
- **Indifferente** l'ordine in cui gli elementi sono esposti.
- *non passa al judge:* Fonte sezione 1 del questionario - Gravita alta - judge si

### B.15 [issue: I-06] [tipo: qualificazione]

- **Verifica** la nota qualifica la dichiarazione della clausola 5.1 come non documentata da evidenze indipendenti sulla presenza fisica.
- **Pass se** compare, riferita a quella dichiarazione, una fra: «non documentata da evidenze indipendenti», «da verificare con evidenze indipendenti», «la dichiarazione non esaurisce la verifica».
- **Fail se** la dichiarazione è presentata come bastevole, oppure la qualificazione non compare.
- **Indifferente** il richiamo al numero del paragrafo della policy.
- *non passa al judge:* Fonte clausola 5.1 della bozza; paragrafo 4.3 della policy interna - Gravita alta - judge si

### B.16 [issue: I-06] [tipo: assenza]

- **Verifica** la nota non afferma che la controparte è priva di presenza fisica nella giurisdizione di costituzione.
- **Fail se** compare l'affermazione che la controparte è priva di presenza fisica o che integra il divieto per assenza di presenza fisica.
- **Indifferente** l'indicazione che la presenza fisica va accertata con evidenze indipendenti.
- *non passa al judge:* Fonte sezione 1 del questionario; paragrafo 4.1 della policy - Gravita alta - judge si

### B.17 [issue: I-06] [tipo: presenza]

- **Verifica** la nota indica come azione l'acquisizione di evidenze indipendenti sulla presenza fisica e sulla sede di direzione effettiva.
- **Pass se** compare l'indicazione di acquisire evidenze indipendenti sulla presenza fisica.
- **Fail se** l'azione non compare.
- **Indifferente** il tipo di evidenze proposte.
- *non passa al judge:* Fonte paragrafo 4.3 della policy interna - Gravita alta - judge si

### B.18 [issue: I-07] [tipo: presenza]

- **Verifica** la nota rileva che fra la clientela della controparte figurano società di cambio valuta non sottoposte a vigilanza prudenziale.
- **Pass se** compare l'indicazione che la clientela della controparte comprende enti privi di licenza o società di cambio valuta non vigilate.
- **Fail se** il rilievo non compare, oppure la clientela è presentata come composta di soli soggetti vigilati.
- **Indifferente** il richiamo al numero della sezione.
- *non passa al judge:* Fonte sezione 4 del questionario - Gravita alta - judge si

### B.19 [issue: I-07] [tipo: presenza]

- **Verifica** la nota rileva che la controparte rende servizi a banche terze.
- **Pass se** compare l'indicazione che la controparte rende servizi a banche terze.
- **Fail se** il rilievo non compare, oppure è affermato che la controparte non serve banche terze.
- **Indifferente** il richiamo alla percentuale di clientela non residente.
- *non passa al judge:* Fonte sezione 4 del questionario - Gravita alta - judge si

### B.20 [issue: I-08] [tipo: presenza]

- **Verifica** la nota rileva che la clausola 4.2 rende le dichiarazioni della controparte rese una sola volta e confermate per tutta la durata.
- **Pass se** compare l'indicazione che la clausola 4.2 prevede una conferma implicita delle dichiarazioni per tutta la durata.
- **Fail se** il rilievo non compare, oppure la clausola è presentata come ammissibile.
- **Indifferente** il richiamo al numero della clausola.
- *non passa al judge:* Fonte clausola 4.2 della bozza - Gravita alta - judge si

### B.21 [issue: I-08] [tipo: presenza]

- **Verifica** il redline sostituisce la clausola 4.2 con l'obbligo di rinnovare le dichiarazioni e di comunicare senza indugio le variazioni.
- **Pass se** nel documento con revisioni tracciate la clausola 4.2 risulta sostituita con un obbligo di rinnovo e di comunicazione senza indugio.
- **Fail se** la clausola 4.2 resta invariata nel documento con revisioni tracciate.
- **Indifferente** la periodicità proposta per il rinnovo.
- *non passa al judge:* Fonte clausola 4.2 della bozza; paragrafo 6.5 della policy - Gravita alta - judge si

### B.22 [issue: I-09] [tipo: presenza]

- **Verifica** la nota rileva che la clausola 10.1 àncora la comunicazione delle variazioni al riesame anziché richiederla senza indugio.
- **Pass se** compare l'indicazione che la clausola 10.1 collega la comunicazione delle variazioni al riesame.
- **Fail se** il rilievo non compare, oppure la clausola è presentata come ammissibile.
- **Indifferente** il richiamo al numero della clausola.
- *non passa al judge:* Fonte clausola 10.1 della bozza; paragrafo 6.5 della policy - Gravita alta - judge si

### B.23 [issue: I-09] [tipo: presenza]

- **Verifica** il redline sostituisce la clausola 10.1 con l'obbligo di comunicazione senza indugio.
- **Pass se** nel documento con revisioni tracciate la clausola 10.1 risulta sostituita con un obbligo di comunicazione senza indugio.
- **Fail se** la clausola 10.1 resta invariata nel documento con revisioni tracciate.
- **Indifferente** la formulazione sostitutiva proposta.
- *non passa al judge:* Fonte clausola 10.1 della bozza - Gravita alta - judge si

### B.24 [issue: I-10] [tipo: valore]

- **Verifica** la nota indica in 36 mesi la periodicità del riesame prevista dalla bozza e in 12 mesi quella ammessa dalla policy per i rapporti a rischio elevato.
- **Pass se** compaiono «36 mesi» e «12 mesi» come periodicità prevista e periodicità ammessa. compaiono «trentasei mesi» e «dodici mesi» come periodicità prevista e periodicità ammessa.
- **Fail se** è indicata una periodicità diversa per uno dei due valori, oppure uno dei due valori non compare.
- **Indifferente** l'ordine in cui i due valori sono esposti.
- *non passa al judge:* Fonte clausola 9.2 della bozza; paragrafo 6.4 della policy - Gravita alta - judge no

### B.25 [issue: I-10] [tipo: attribuzione]

- **Verifica** la nota collega la periodicità di dodici mesi alla classe di rischio elevata attribuita dalla scheda paese.
- **Pass se** il collegamento è fatto alla classe di rischio elevata attribuita dalla scheda di valutazione del rischio paese.
- **Fail se** la periodicità è indicata senza il collegamento alla classificazione del rischio.
- **Indifferente** il richiamo al protocollo della scheda.
- *non passa al judge:* Fonte scheda rischio paese; paragrafo 6.4 della policy - Gravita alta - judge si

### B.26 [issue: I-10] [tipo: presenza]

- **Verifica** il redline riduce la periodicità del riesame prevista dalla clausola 9.2.
- **Pass se** nel documento con revisioni tracciate la periodicità di 36 mesi risulta sostituita da una periodicità più breve.
- **Fail se** la periodicità di 36 mesi resta invariata nel documento con revisioni tracciate.
- **Indifferente** il valore esatto proposto, purché non superiore a dodici mesi.
- *non passa al judge:* Fonte clausola 9.2 della bozza - Gravita alta - judge si

### B.27 [issue: I-11] [tipo: valore]

- **Verifica** la nota indica in euro 1.000.000,00 la soglia di escalation prevista dalla bozza e in euro 250.000,00 quella prevista dalla policy.
- **Pass se** compaiono «euro 1.000.000,00» ed «euro 250.000,00» come soglia prevista e soglia ammessa. compaiono «1.000.000,00» e «250.000,00» come soglia prevista e soglia ammessa.
- **Fail se** è indicata una soglia diversa per uno dei due valori, oppure uno dei due valori non compare.
- **Indifferente** l'ordine in cui i due valori sono esposti.
- *non passa al judge:* Fonte clausola 12.2 della bozza; paragrafo 7.2 della policy - Gravita alta - judge no

### B.28 [issue: I-11] [tipo: presenza]

- **Verifica** la nota afferma che la policy impone l'approfondimento anche per le operazioni con indicatori di anomalia indipendentemente dall'importo.
- **Pass se** compare l'indicazione che l'approfondimento è dovuto anche a prescindere dall'importo, in presenza di indicatori di anomalia.
- **Fail se** l'affermazione non compare, oppure l'approfondimento è presentato come legato al solo importo.
- **Indifferente** il richiamo al numero del paragrafo.
- *non passa al judge:* Fonte paragrafo 7.2 della policy interna - Gravita alta - judge si

### B.29 [issue: I-11] [tipo: presenza]

- **Verifica** il redline riduce la soglia di escalation prevista dalla clausola 12.2.
- **Pass se** nel documento con revisioni tracciate la soglia di euro 1.000.000,00 risulta sostituita da una soglia inferiore.
- **Fail se** la soglia di euro 1.000.000,00 resta invariata nel documento con revisioni tracciate.
- **Indifferente** il valore esatto proposto, purché non superiore a euro 250.000,00.
- *non passa al judge:* Fonte clausola 12.2 della bozza - Gravita alta - judge si

### B.30 [issue: I-12] [tipo: presenza]

- **Verifica** la nota rileva che la clausola 12.3 indirizza l'informativa alla sola funzione pagamenti esteri.
- **Pass se** compare l'indicazione che l'informativa è indirizzata alla sola funzione pagamenti esteri.
- **Fail se** il rilievo non compare, oppure l'indirizzamento è presentato come completo.
- **Indifferente** il richiamo al numero della clausola.
- *non passa al judge:* Fonte clausola 12.3 della bozza - Gravita media - judge si

### B.31 [issue: I-13] [tipo: valore]

- **Verifica** la nota indica in 15 giorni lavorativi il termine di riscontro previsto dalla bozza e in 5 giorni lavorativi quello atteso dalla policy.
- **Pass se** compaiono «15 giorni lavorativi» e «5 giorni lavorativi» come termine previsto e termine atteso. compaiono «quindici giorni lavorativi» e «cinque giorni lavorativi» come termine previsto e termine atteso.
- **Fail se** è indicato un termine diverso per uno dei due valori, oppure uno dei due valori non compare.
- **Indifferente** l'ordine in cui i due valori sono esposti.
- *non passa al judge:* Fonte clausola 11.4 della bozza; paragrafo 7.5 della policy - Gravita alta - judge no

### B.32 [issue: I-13] [tipo: presenza]

- **Verifica** la nota afferma che il mancato riscontro nel termine costituisce fattore di rischio che attiva la valutazione della chiusura.
- **Pass se** compare l'indicazione che il mancato riscontro nel termine attiva la valutazione della chiusura.
- **Fail se** l'affermazione non compare, oppure al mancato riscontro non è collegata alcuna conseguenza.
- **Indifferente** il richiamo al numero del paragrafo.
- *non passa al judge:* Fonte paragrafi 7.5 e 8.2 della policy interna - Gravita alta - judge si

### B.33 [issue: I-13] [tipo: presenza]

- **Verifica** il redline riduce il termine di riscontro previsto dalla clausola 11.4.
- **Pass se** nel documento con revisioni tracciate il termine di 15 giorni lavorativi risulta sostituito da un termine più breve.
- **Fail se** il termine di 15 giorni lavorativi resta invariato nel documento con revisioni tracciate.
- **Indifferente** il valore esatto proposto, purché non superiore a cinque giorni lavorativi.
- *non passa al judge:* Fonte clausola 11.4 della bozza - Gravita alta - judge si

### B.34 [issue: I-14] [tipo: presenza]

- **Verifica** la nota rileva che la clausola 11.3 subordina il riscontro ai limiti della riservatezza bancaria della giurisdizione della controparte.
- **Pass se** compare l'indicazione che la clausola 11.3 subordina il riscontro ai limiti della riservatezza della giurisdizione della controparte.
- **Fail se** il rilievo non compare, oppure la clausola è presentata come ammissibile.
- **Indifferente** il richiamo al numero della clausola.
- *non passa al judge:* Fonte clausola 11.3 della bozza - Gravita alta - judge si

### B.35 [issue: I-14] [tipo: attribuzione]

- **Verifica** la nota collega quel rilievo alla dichiarazione del questionario secondo cui la trasmissione richiede l'autorizzazione dell'autorità di vigilanza locale.
- **Pass se** il rilievo è ricondotto alla sezione del questionario sulla riservatezza e la cooperazione.
- **Fail se** il rilievo è fondato soltanto sulla clausola dell'accordo, senza il riscontro nel questionario.
- **Indifferente** il richiamo alla riga della scheda paese sul segreto bancario.
- *non passa al judge:* Fonte sezione 7 del questionario - Gravita alta - judge si

### B.36 [issue: I-14] [tipo: qualificazione]

- **Verifica** la nota qualifica il diritto di informazione della Banca come inattuabile nei termini della bozza.
- **Pass se** compare, riferita al diritto di informazione, una fra: «inattuabile», «privo di effettivita», «non esercitabile nei termini della bozza».
- **Fail se** il diritto è presentato come esercitabile, oppure la qualificazione non compare.
- **Indifferente** la formulazione sostitutiva proposta.
- *non passa al judge:* Fonte clausola 11.3 della bozza; sezione 7 del questionario - Gravita alta - judge si

### B.37 [issue: I-14] [tipo: assenza]

- **Verifica** la nota non afferma che il limite di riservatezza si supera con la sola motivazione della richiesta.
- **Fail se** compare l'affermazione che la formulazione motivata della richiesta supera il limite di riservatezza opposto dalla controparte.
- **Indifferente** l'indicazione che la richiesta va comunque motivata.
- *non passa al judge:* Fonte clausole 11.2 e 11.3 della bozza - Gravita alta - judge si

### B.38 [issue: I-15] [tipo: presenza]

- **Verifica** la nota rileva che la clausola 13.1 esclude il diritto della Banca di svolgere verifiche presso la controparte.
- **Pass se** compare l'indicazione che la clausola 13.1 esclude il diritto di verifica.
- **Fail se** il rilievo non compare, oppure la clausola è presentata come ammissibile.
- **Indifferente** il richiamo al numero della clausola.
- *non passa al judge:* Fonte clausola 13.1 della bozza - Gravita alta - judge si

### B.39 [issue: I-15] [tipo: presenza]

- **Verifica** la nota afferma che la dichiarazione annuale di conformità non sostituisce il diritto di verifica.
- **Pass se** compare l'indicazione che la dichiarazione annuale non sostituisce il diritto di verifica.
- **Fail se** l'affermazione non compare, oppure la dichiarazione è presentata come equivalente.
- **Indifferente** il richiamo al numero del paragrafo.
- *non passa al judge:* Fonte clausola 13.2 della bozza; paragrafo 10.2 della policy - Gravita alta - judge si

### B.40 [issue: I-15] [tipo: presenza]

- **Verifica** il redline sostituisce la clausola 13.1 introducendo il diritto di verifica presso la controparte.
- **Pass se** nel documento con revisioni tracciate la clausola 13.1 risulta sostituita con il diritto di svolgere verifiche presso la controparte.
- **Fail se** la clausola 13.1 resta invariata nel documento con revisioni tracciate.
- **Indifferente** il preavviso proposto per le verifiche.
- *non passa al judge:* Fonte clausola 13.1 della bozza; paragrafo 10.1 della policy - Gravita alta - judge si

### B.41 [issue: I-16] [tipo: presenza]

- **Verifica** la nota rileva che la clausola 15.2 subordina al consenso della controparte la comunicazione di informazioni alle autorità.
- **Pass se** compare l'indicazione che la clausola 15.2 subordina al consenso della controparte le comunicazioni alle autorità.
- **Fail se** il rilievo non compare, oppure la clausola è presentata come ammissibile.
- **Indifferente** il richiamo al numero della clausola.
- *non passa al judge:* Fonte clausola 15.2 della bozza - Gravita alta - judge si

### B.42 [issue: I-16] [tipo: presenza]

- **Verifica** il redline sopprime la subordinazione al consenso contenuta nella clausola 15.2.
- **Pass se** nel documento con revisioni tracciate la clausola 15.2 risulta cancellata o sostituita.
- **Fail se** la clausola 15.2 resta invariata nel documento con revisioni tracciate.
- **Indifferente** la formulazione sostitutiva proposta.
- *non passa al judge:* Fonte clausola 15.2 della bozza - Gravita alta - judge si

### B.43 [issue: I-16] [tipo: assenza]

- **Verifica** la nota non afferma che la clausola 15.2 è sanabile con l'aggiunta di una riserva generica per gli obblighi di legge.
- **Fail se** compare l'affermazione che una riserva generica per gli obblighi di legge rende la clausola 15.2 ammissibile.
- **Indifferente** l'indicazione che la clausola va soppressa nella parte che subordina le comunicazioni.
- *non passa al judge:* Fonte paragrafo 9.2 della policy interna - Gravita alta - judge si

### B.44 [issue: I-17] [tipo: valore]

- **Verifica** la nota indica in 90 giorni il preavviso di chiusura per motivi di rischio previsto dalla bozza e in 5 giorni lavorativi quello ammesso dalla policy.
- **Pass se** compaiono «90 giorni» e «5 giorni lavorativi» come preavviso previsto e preavviso ammesso. compaiono «novanta giorni» e «cinque giorni lavorativi» come preavviso previsto e preavviso ammesso.
- **Fail se** è indicato un preavviso diverso per uno dei due valori, oppure uno dei due valori non compare.
- **Indifferente** l'ordine in cui i due valori sono esposti.
- *non passa al judge:* Fonte clausola 14.3 della bozza; paragrafo 8.3 della policy - Gravita alta - judge no

### B.45 [issue: I-17] [tipo: presenza]

- **Verifica** il redline riduce il preavviso di chiusura per motivi di rischio previsto dalla clausola 14.3.
- **Pass se** nel documento con revisioni tracciate il preavviso di 90 giorni risulta sostituito da un preavviso più breve.
- **Fail se** il preavviso di 90 giorni resta invariato nel documento con revisioni tracciate.
- **Indifferente** il valore esatto proposto, purché non superiore a cinque giorni lavorativi.
- *non passa al judge:* Fonte clausola 14.3 della bozza - Gravita alta - judge si

### B.46 [issue: I-18] [tipo: presenza]

- **Verifica** la nota rileva che il questionario non indica disponente e beneficiari di Sarvenko Trust, socio al ventiquattro per cento.
- **Pass se** compare l'indicazione che disponente e beneficiari del socio costituito in trust non sono indicati.
- **Fail se** il rilievo non compare, oppure l'assetto è dato per ricostruito.
- **Indifferente** il richiamo al numero della sezione.
- *non passa al judge:* Fonte sezione 3 del questionario - Gravita alta - judge si

### B.47 [issue: I-18] [tipo: attribuzione]

- **Verifica** la nota collega quel rilievo all'esito non eseguibile dello screening su Sarvenko Trust.
- **Pass se** il rilievo è ricondotto alla riga dello screening relativa a Sarvenko Trust, con esito non eseguibile.
- **Fail se** il rilievo è formulato senza il collegamento all'esito dello screening.
- **Indifferente** il richiamo alla percentuale della quota.
- *non passa al judge:* Fonte riga di Sarvenko Trust nell'esito dello screening - Gravita alta - judge si

### B.48 [issue: I-18] [tipo: assenza]

- **Verifica** la nota non afferma che la quota inferiore a un quarto rende irrilevante l'identificazione dei titolari effettivi del trust.
- **Fail se** compare l'affermazione che la misura della quota rende irrilevante l'identificazione dei titolari effettivi del trust.
- **Indifferente** l'indicazione della misura della quota come dato di fatto.
- *non passa al judge:* Fonte sezione 3 del questionario - Gravita alta - judge si

### B.49 [issue: I-19] [tipo: presenza]

- **Verifica** la nota riporta il riscontro su lista di persone politicamente esposte relativo a Nadir Kolstemp, titolare effettivo dichiarato.
- **Pass se** compare l'indicazione del riscontro su persona politicamente esposta riferito a Nadir Kolstemp.
- **Fail se** il riscontro non è riportato, oppure è attribuito a un altro soggetto.
- **Indifferente** l'indicazione dell'incarico e dell'anno di cessazione.
- *non passa al judge:* Fonte riga di Nadir Kolstemp nell'esito dello screening - Gravita alta - judge si

### B.50 [issue: I-19] [tipo: attribuzione]

- **Verifica** la nota fonda la rilevanza del riscontro sulla coincidenza dell'anagrafica.
- **Pass se** la rilevanza è ricondotta alla colonna dello screening che riporta la coincidenza dell'anagrafica.
- **Fail se** la rilevanza è affermata senza indicare il dato che la sostiene.
- **Indifferente** l'indicazione della fonte del riscontro.
- *non passa al judge:* Fonte riga di Nadir Kolstemp nell'esito dello screening - Gravita alta - judge si

### B.51 [issue: I-19] [tipo: assenza]

- **Verifica** la nota non afferma che il riscontro è irrilevante perché l'incarico è cessato.
- **Fail se** compare l'affermazione che la cessazione dell'incarico rende il riscontro irrilevante o esclude le misure rafforzate.
- **Indifferente** la menzione dell'anno di cessazione dell'incarico.
- *non passa al judge:* Fonte riga di Nadir Kolstemp nell'esito dello screening - Gravita alta - judge si

### B.52 [issue: I-20] [tipo: presenza]

- **Verifica** la nota rileva che il fascicolo non contiene il parere della funzione antiriciclaggio né l'autorizzazione della Direzione generale.
- **Pass se** compare l'indicazione che parere e autorizzazione non risultano dagli atti.
- **Fail se** uno dei due atti è dato per esistente, oppure la lacuna non è dichiarata.
- **Indifferente** il richiamo al numero del paragrafo.
- *non passa al judge:* Fonte paragrafo 3.2 della policy interna; composizione del fascicolo - Gravita alta - judge si

### B.53 [issue: I-20] [tipo: qualificazione]

- **Verifica** la nota qualifica il parere della funzione antiriciclaggio come condizione dell'autorizzazione all'apertura.
- **Pass se** compare l'indicazione che il parere è condizione dell'autorizzazione.
- **Fail se** il parere è presentato come facoltativo, oppure la sua funzione non è indicata.
- **Indifferente** il richiamo al numero del paragrafo.
- *non passa al judge:* Fonte paragrafo 3.2 della policy interna - Gravita alta - judge si

### B.54 [issue: I-20] [tipo: presenza]

- **Verifica** la nota elenca gli elementi dell'istruttoria di apertura che il fascicolo non contiene.
- **Pass se** compaiono almeno due elementi mancanti fra evidenze indipendenti sulla presenza fisica, identificazione dei titolari effettivi del trust, parere della funzione antiriciclaggio e autorizzazione della Direzione generale.
- **Fail se** gli elementi mancanti non sono elencati, oppure ne è indicato uno solo.
- **Indifferente** l'ordine in cui gli elementi sono elencati.
- *non passa al judge:* Fonte paragrafo 3.1 della policy interna; composizione del fascicolo - Gravita alta - judge si

### B.55 [issue: I-21] [tipo: presenza]

- **Verifica** la nota rileva che l'utilizzo diretto del conto, l'esclusione dei filtri autonomi e il preavviso di centottanta giorni sono chiesti dalla nota dell'unità Pagamenti esteri.
- **Pass se** compare l'indicazione che almeno due di quelle tre clausole hanno origine nella richiesta dell'unità Pagamenti esteri.
- **Fail se** il rilievo non compare, oppure è indicata una sola clausola.
- **Indifferente** il richiamo al protocollo della nota.
- *non passa al judge:* Fonte paragrafo 4 della nota del 27 giugno 2031 - Gravita media - judge si

### B.56 [issue: I-21] [tipo: assenza]

- **Verifica** la nota non afferma che la richiesta dell'unità Pagamenti esteri vincola l'esito della revisione.
- **Fail se** compare l'affermazione che la richiesta dell'unità commerciale vincola o determina l'esito della revisione.
- **Indifferente** l'indicazione che la decisione spetta alla Direzione generale su parere della funzione antiriciclaggio.
- *non passa al judge:* Fonte paragrafo 3.2 della policy interna - Gravita media - judge si

### B.57 [issue: I-22] [tipo: presenza]

- **Verifica** la nota afferma che il rapporto non è apribile nei termini della bozza.
- **Pass se** compare, riferita all'apertura, una fra: «non apribile nei termini della bozza», «le modifiche sono condizione dell'apertura», «l'accordo non è sottoscrivibile come è».
- **Fail se** l'affermazione non compare, oppure il rapporto è presentato come apribile senza modifiche.
- **Indifferente** l'ordine in cui le condizioni sono elencate.
- *non passa al judge:* Fonte insieme dei rilievi - Gravita alta - judge si

### B.58 [issue: I-22] [tipo: presenza]

- **Verifica** la nota afferma che resta da valutare se l'assetto dichiarato dalla controparte consenta l'apertura anche con l'accordo modificato.
- **Pass se** compare l'indicazione che, apportate le modifiche all'accordo, resta da valutare l'assetto dichiarato dalla controparte.
- **Fail se** l'affermazione non compare, oppure è affermato che le correzioni contrattuali esauriscono la valutazione.
- **Indifferente** l'indicazione degli elementi dell'assetto che restano da valutare.
- *non passa al judge:* Fonte divieti del paragrafo 4 della policy; sezioni 1, 4 e 5 del questionario - Gravita alta - judge si

### B.59 [issue: I-22] [tipo: assenza]

- **Verifica** la nota non afferma che l'apertura del rapporto è vietata in via definitiva.
- **Fail se** compare l'affermazione che l'apertura è vietata o preclusa in via definitiva.
- **Indifferente** l'indicazione dei divieti che potrebbero risultare integrati a esito delle verifiche.
- *non passa al judge:* Fonte paragrafo 4 della policy interna - Gravita alta - judge si


## C. Date, valori calcolati e chiusura

### C.1 [issue: N-01] [tipo: assenza]

- **Verifica** la nota non riporta il riscontro su omonimo relativo a Teodor Kolstemp come precedente dell'amministratore della controparte.
- **Fail se** il riscontro relativo a Teodor Kolstemp è attribuito all'amministratore della controparte o compare fra i red flag che lo riguardano.
- **Indifferente** la menzione del riscontro con l'indicazione delle difformità anagrafiche.
- *non passa al judge:* Fonte challenge map, N-01 - Gravita alta - judge si

### C.2 [issue: N-01] [tipo: presenza]

- **Verifica** la nota afferma che il riscontro relativo a Teodor Kolstemp non riguarda il soggetto in perimetro.
- **Pass se** compare, riferita a quel riscontro, una fra: «non riguarda il soggetto in perimetro», «cade su omonimo», «anagrafica difforme».
- **Fail se** il riscontro è attribuito al soggetto in perimetro, oppure l'esito della verifica anagrafica non è affermato.
- **Indifferente** l'indicazione di quale dato anagrafico differisce.
- *non passa al judge:* Fonte riga di Teodor Kolstemp nell'esito dello screening - Gravita alta - judge si

### C.3 [issue: N-02] [tipo: assenza]

- **Verifica** la nota non presenta i volumi attesi dichiarati dall'unità commerciale come clausola da modificare.
- **Fail se** i volumi attesi compaiono fra i rilievi che impongono una modifica dell'accordo.
- **Indifferente** la menzione dei volumi fra gli elementi che concorrono alla classificazione del rischio.
- *non passa al judge:* Fonte challenge map, N-02 - Gravita media - judge si

### C.4 [issue: N-03] [tipo: assenza]

- **Verifica** la nota non segnala come rischio la clausola compromissoria della clausola 16.2.
- **Fail se** la clausola compromissoria compare fra i rilievi che impongono una modifica.
- **Indifferente** la menzione della sede arbitrale nella descrizione dell'accordo.
- *non passa al judge:* Fonte challenge map, N-03 - Gravita media - judge si

### C.5 [issue: N-04] [tipo: assenza]

- **Verifica** la nota non estende al preavviso di recesso ordinario della clausola 14.1 il rilievo formulato sul preavviso di chiusura per motivi di rischio.
- **Fail se** il preavviso di recesso ordinario di centottanta giorni compare fra i rilievi che impongono una modifica.
- **Indifferente** la menzione del preavviso ordinario come termine di confronto.
- *non passa al judge:* Fonte challenge map, N-04 - Gravita alta - judge si

### C.6 [issue: N-05] [tipo: assenza]

- **Verifica** la nota non segnala come profilo di rischio la durata a tempo indeterminato dell'accordo.
- **Fail se** la durata a tempo indeterminato compare fra i rilievi che impongono una modifica.
- **Indifferente** la menzione della durata nella descrizione dell'accordo.
- *non passa al judge:* Fonte challenge map, N-05 - Gravita media - judge si

### C.7 [issue: N-06] [tipo: assenza]

- **Verifica** la nota non segnala come ostacolo alla chiusura il completamento delle operazioni in corso di regolamento previsto dalla clausola 14.4.
- **Fail se** il completamento delle operazioni in corso compare fra i rilievi che impongono una modifica o fra gli ostacoli alla chiusura.
- **Indifferente** la menzione della previsione nella trattazione della chiusura.
- *non passa al judge:* Fonte challenge map, N-06 - Gravita media - judge si

### C.8 [issue: N-07] [tipo: assenza]

- **Verifica** la nota non presenta come red flag l'assenza di quotazione della controparte e la sua non appartenenza a un gruppo bancario.
- **Fail se** l'assenza di quotazione o la non appartenenza a un gruppo compaiono fra i red flag.
- **Indifferente** la menzione di quei dati fra le informazioni anagrafiche della controparte.
- *non passa al judge:* Fonte challenge map, N-07 - Gravita media - judge si

### C.9 [issue: X-01] [tipo: assenza]

- **Verifica** simmetria del controllo: la nota non tratta come provata l'assenza di presenza fisica mentre tratta come da verificare l'assetto proprietario del socio costituito in trust.
- **Fail se** l'assenza di presenza fisica è data per provata e nello stesso documento l'assetto proprietario del trust è dichiarato da verificare.
- **Indifferente** l'ordine in cui i due punti sono trattati.
- *non passa al judge:* Fonte sezioni 1 e 3 del questionario - Gravita alta - judge si

### C.10 [issue: X-02] [tipo: assenza]

- **Verifica** divieto di presunzione dell'esito: la nota non afferma che la controparte è coinvolta in attività di riciclaggio.
- **Fail se** compare l'affermazione che la controparte è coinvolta in attività di riciclaggio o che le operazioni attese sono di provenienza illecita.
- **Indifferente** l'indicazione dei fattori di rischio che richiedono misure rafforzate.
- *non passa al judge:* Fonte composizione del fascicolo - Gravita alta - judge si

### C.11 [issue: X-03] [tipo: assenza]

- **Verifica** sovra-segnalazione: la nota non presenta come red flag la frequenza mensile di aggiornamento delle liste dichiarata dalla controparte, senza collegarla ad alcun rilievo sull'accordo.
- **Fail se** la frequenza di aggiornamento delle liste compare fra i red flag autonomi, non collegata ad alcuna clausola.
- **Indifferente** la menzione della frequenza fra gli elementi che concorrono alla valutazione dei presidi della controparte.
- *non passa al judge:* Fonte sezione 6 del questionario - Gravita media - judge si
