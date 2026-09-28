# WF2-057 - Criteri atomizzati

Forma a campi. Ciò che sta sotto la riga non passa al judge.


## A. Forma dell'output (interamente verifica meccanica)

### A.1 [tipo: valore]

- **Verifica** il deliverable è prodotto come file `tender_review.md`.
- **Pass se** il file consegnato ha nome `tender_review.md`.
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

- **Verifica** il deliverable non supera il limite di 2200 parole.
- **Pass se** il conteggio delle parole del corpo del deliverable non supera 2200.
- **Fail se** il corpo del deliverable supera 2200 parole.
- **Indifferente** la lunghezza delle singole sezioni.
- *non passa al judge:* Fonte task_spec.json, campo limite_parole - Gravita media - judge no

### A.4 [tipo: struttura]

- **Verifica** ogni rilievo porta il riferimento alla clausola o al paragrafo del documento su cui incide.
- **Pass se** accanto a ciascun rilievo compare il numero della clausola o del paragrafo.
- **Fail se** almeno un rilievo non porta il riferimento alla clausola o al paragrafo.
- **Indifferente** la forma del riferimento.
- *non passa al judge:* Fonte public/01_task.md, richiesta sulla fonte - Gravita media - judge no

### A.5 [tipo: struttura]

- **Verifica** per ciascuna incoerenza fra documenti il deliverable indica quale documento contiene il valore da mantenere.
- **Pass se** per ciascuna incoerenza compare l'indicazione del documento il cui valore va mantenuto.
- **Fail se** almeno una incoerenza è segnalata senza indicare quale valore va mantenuto.
- **Indifferente** l'ordine in cui i documenti sono citati.
- *non passa al judge:* Fonte public/01_task.md, richiesta sulle incoerenze - Gravita media - judge no

### A.6 [tipo: presenza]

- **Verifica** il deliverable distingue i rilievi che impongono una modifica prima della pubblicazione da quelli che non la impongono.
- **Pass se** compare una separazione fra i rilievi che impongono modifica e gli elementi che non la impongono.
- **Fail se** il deliverable presenta un elenco indistinto di osservazioni.
- **Indifferente** le etichette usate per la separazione.
- *non passa al judge:* Fonte public/response_template.md - Gravita media - judge no

### A.7 [tipo: assenza]

- **Verifica** il deliverable non richiama fonti normative estranee all'elenco chiuso del reference pack.
- **Fail se** compare un riferimento normativo che non figura in `private/fonti_chiuse.json`.
- **Indifferente** il richiamo alle clausole dei documenti di gara e alle voci del quadro economico.
- *non passa al judge:* Fonte private/fonti_chiuse.json - Gravita media - judge no


## B. Merito

Il fascicolo è esaminato al 15 ottobre 2031: la determina a contrarre è adottata, i due documenti di gara sono in bozza e la pubblicazione è prevista per il 20 ottobre 2031. Il lato assistito è la stazione appaltante. Il prompt chiede la revisione punto per punto con la clausola su cui incide e il documento che la fonda, l'indicazione del valore da mantenere per ciascuna incoerenza, la misura da usare dove un valore va corretto, la separazione fra rilievi che impongono modifica e rilievi che non la impongono, l'eventuale provvista mancante nel quadro economico, e la valutazione della lettura del servizio tecnico sulla clausola di revisione dei prezzi.

### B.1 [issue: I-01] [tipo: valore]

- **Verifica** il deliverable indica in 2,0 per mille la penale giornaliera prevista dalla clausola 12.1 dello schema.
- **Pass se** compare «2,0 per mille» come misura prevista dalla bozza. compare «2 per mille» come misura prevista dalla bozza.
- **Fail se** è indicata una misura diversa, oppure la misura prevista dalla bozza non è rilevata.
- **Indifferente** il richiamo al numero della clausola.
- *non passa al judge:* Fonte clausola 12.1 dello schema - Gravita alta - judge no

### B.2 [issue: I-01] [tipo: valore]

- **Verifica** il deliverable indica in un intervallo dallo 0,5 all'1,5 per mille il limite consentito per la penale giornaliera.
- **Pass se** compare «da 0,5 a 1,5 per mille» come intervallo consentito. compaiono «0,5 per mille» e «1,5 per mille» come estremi dell'intervallo consentito.
- **Fail se** è indicato un intervallo diverso, oppure l'intervallo non è indicato.
- **Indifferente** l'indicazione della misura che il deliverable propone entro l'intervallo.
- *non passa al judge:* Fonte disciplina delle penali negli appalti pubblici - Gravita alta - judge no

### B.3 [issue: I-01] [tipo: qualificazione]

- **Verifica** il deliverable qualifica la penale della clausola 12.1 come eccedente il limite superiore dell'intervallo consentito.
- **Pass se** compare, riferita a quella penale, una fra: «eccede il limite superiore», «oltre il massimo consentito», «fuori dall'intervallo consentito».
- **Fail se** la penale è presentata come rientrante nell'intervallo, oppure come rimessa alla discrezionalità della stazione appaltante, oppure la qualificazione non compare.
- **Indifferente** il giudizio sull'entità economica della penale.
- *non passa al judge:* Fonte clausola 12.1 dello schema - Gravita alta - judge si

### B.4 [issue: I-02] [tipo: valore]

- **Verifica** il deliverable indica in 20 per cento il tetto complessivo delle penali previsto dalla clausola 12.2 e in 10 per cento il limite consentito.
- **Pass se** compaiono «20 per cento» e «10 per cento» come tetto previsto e limite consentito.
- **Fail se** è indicata una misura diversa per uno dei due valori, oppure uno dei due valori non compare.
- **Indifferente** l'ordine in cui i due valori sono esposti.
- *non passa al judge:* Fonte clausola 12.2 dello schema; disciplina delle penali - Gravita alta - judge no

### B.5 [issue: I-02] [tipo: presenza]

- **Verifica** il deliverable indica come modifica la riduzione del tetto complessivo delle penali entro il limite consentito.
- **Pass se** compare l'indicazione di ridurre il tetto complessivo entro il limite consentito.
- **Fail se** la modifica non compare, oppure è proposta una misura superiore al limite.
- **Indifferente** la misura esatta proposta, purché non superiore al limite.
- *non passa al judge:* Fonte clausola 12.2 dello schema - Gravita alta - judge si

### B.6 [issue: I-03] [tipo: presenza]

- **Verifica** il deliverable rileva che la clausola 13.2 dello schema àncora la risoluzione a una misura di penali diversa dal tetto della clausola 12.2.
- **Pass se** compare l'indicazione che le clausole 12.2 e 13.2 dello schema non sono coerenti fra loro quanto alla misura delle penali.
- **Fail se** il rilievo non compare, oppure le due clausole sono presentate come allineate.
- **Indifferente** l'ordine in cui le due clausole sono citate.
- *non passa al judge:* Fonte clausole 12.2 e 13.2 dello schema - Gravita alta - judge si

### B.7 [issue: I-03] [tipo: presenza]

- **Verifica** il deliverable indica come modifica l'allineamento della clausola 13.2 al tetto della clausola 12.2 come rideterminato.
- **Pass se** compare l'indicazione di allineare la soglia della clausola 13.2 al tetto della clausola 12.2 come rideterminato.
- **Fail se** la modifica non compare, oppure l'incoerenza è risolta mantenendo il tetto del 20 per cento.
- **Indifferente** la misura proposta, purché coerente fra le due clausole.
- *non passa al judge:* Fonte clausole 12.2 e 13.2 dello schema - Gravita alta - judge si

### B.8 [issue: I-04] [tipo: qualificazione]

- **Verifica** il deliverable qualifica l'appalto come appalto di lavori ai fini della taratura della clausola di revisione dei prezzi.
- **Pass se** compare, riferita all'oggetto dell'appalto, una fra: «appalto di lavori», «contratto di lavori», «esecuzione di lavori».
- **Fail se** l'appalto è qualificato come appalto di servizi o di forniture, oppure la qualificazione non compare.
- **Indifferente** il richiamo alla categoria delle lavorazioni.
- *non passa al judge:* Fonte punto 5 della determina a contrarre; oggetto del disciplinare - Gravita alta - judge si

### B.9 [issue: I-04] [tipo: valore]

- **Verifica** il deliverable indica in 5 per cento la soglia di attivazione prevista dalla clausola 14.2 e in 3 per cento la soglia applicabile agli appalti di lavori.
- **Pass se** compaiono «5 per cento» e «3 per cento» come soglia prevista e soglia applicabile.
- **Fail se** è indicata una soglia diversa per uno dei due valori, oppure uno dei due valori non compare.
- **Indifferente** l'ordine in cui i due valori sono esposti.
- *non passa al judge:* Fonte clausola 14.2 dello schema; disciplina della revisione dei prezzi - Gravita alta - judge no

### B.10 [issue: I-04] [tipo: valore]

- **Verifica** il deliverable indica in 80 per cento la quota prevista dalla clausola 14.3 e in 90 per cento la quota applicabile agli appalti di lavori.
- **Pass se** compaiono «80 per cento» e «90 per cento» come quota prevista e quota applicabile.
- **Fail se** è indicata una quota diversa per uno dei due valori, oppure uno dei due valori non compare.
- **Indifferente** l'ordine in cui i due valori sono esposti.
- *non passa al judge:* Fonte clausola 14.3 dello schema; disciplina della revisione dei prezzi - Gravita alta - judge no

### B.11 [issue: I-04] [tipo: presenza]

- **Verifica** il deliverable afferma che i parametri della clausola 14 sono quelli previsti per gli appalti di servizi e forniture.
- **Pass se** compare l'indicazione che i parametri usati sono quelli degli appalti di servizi e forniture.
- **Fail se** l'affermazione non compare, oppure i parametri sono presentati come propri degli appalti di lavori.
- **Indifferente** il richiamo all'allegato che disciplina le modalità di applicazione.
- *non passa al judge:* Fonte clausole 14.2 e 14.3 dello schema - Gravita alta - judge si

### B.12 [issue: I-05] [tipo: presenza]

- **Verifica** il deliverable afferma che l'inserimento della clausola di revisione dei prezzi nei documenti di gara iniziali è obbligatorio.
- **Pass se** compare l'indicazione che la clausola di revisione dei prezzi va inserita obbligatoriamente nei documenti di gara iniziali.
- **Fail se** l'obbligatorietà non è affermata, oppure la clausola è presentata come rimessa alla scelta della stazione appaltante.
- **Indifferente** il richiamo al numero dell'articolo.
- *non passa al judge:* Fonte disciplina della revisione dei prezzi - Gravita alta - judge si

### B.13 [issue: I-05] [tipo: assenza]

- **Verifica** il deliverable non indica come modifica la soppressione della clausola 14 dello schema.
- **Fail se** compare l'indicazione di sopprimere la clausola di revisione dei prezzi.
- **Indifferente** l'indicazione di riscrivere la clausola con i parametri applicabili.
- *non passa al judge:* Fonte clausola 14 dello schema - Gravita alta - judge si

### B.14 [issue: I-06] [tipo: presenza]

- **Verifica** il deliverable rileva che lo schema non prevede il premio di accelerazione.
- **Pass se** compare l'indicazione che il premio di accelerazione non figura nello schema.
- **Fail se** il rilievo non compare, oppure il premio è dato per previsto.
- **Indifferente** la misura proposta per il premio.
- *non passa al judge:* Fonte schema di contratto; disciplina delle penali e dei premi di accelerazione - Gravita alta - judge si

### B.15 [issue: I-06] [tipo: attribuzione]

- **Verifica** il deliverable collega l'assenza del premio di accelerazione alla voce del quadro economico destinata a coprirlo, pari a zero.
- **Pass se** il rilievo è ricondotto alla riga del quadro economico relativa al premio di accelerazione.
- **Fail se** il rilievo è formulato senza il collegamento al quadro economico.
- **Indifferente** l'indicazione dell'importo che la voce dovrebbe assumere.
- *non passa al judge:* Fonte sezione D del quadro economico - Gravita media - judge si

### B.16 [issue: I-07] [tipo: valore]

- **Verifica** il deliverable indica in euro 2.740.000,00 l'importo complessivo dell'intervento secondo determina e quadro economico e in euro 2.679.000,00 l'importo soggetto a ribasso.
- **Pass se** compaiono «euro 2.740.000,00» ed «euro 2.679.000,00» come importo complessivo e importo soggetto a ribasso. compaiono «2.740.000,00» e «2.679.000,00» come importo complessivo e importo soggetto a ribasso.
- **Fail se** è indicato un importo diverso per uno dei due valori, oppure uno dei due valori non compare.
- **Indifferente** l'ordine in cui i due valori sono esposti.
- *non passa al judge:* Fonte punto 2 della determina; sezione A del quadro economico - Gravita alta - judge no

### B.17 [issue: I-07] [tipo: presenza]

- **Verifica** il deliverable rileva che la clausola 2.2 del disciplinare somma gli oneri della sicurezza all'importo a base di gara invece di scorporarli.
- **Pass se** compare l'indicazione che il disciplinare somma gli oneri all'importo a base di gara invece di scorporarli.
- **Fail se** il rilievo non compare, oppure la clausola 2.2 è presentata come coerente con la determina.
- **Indifferente** il richiamo al numero della clausola.
- *non passa al judge:* Fonte clausola 2.2 del disciplinare; punto 2 della determina - Gravita alta - judge si

### B.18 [issue: I-07] [tipo: valore]

- **Verifica** il deliverable indica in euro 61.000,00 lo scostamento fra l'importo del disciplinare e quello della determina.
- **Pass se** compare «euro 61.000,00» come scostamento. compare «61.000,00» come scostamento.
- **Fail se** è indicato uno scostamento diverso, oppure lo scostamento non è quantificato.
- **Indifferente** l'indicazione dell'importo complessivo erroneamente riportato dal disciplinare.
- *non passa al judge:* Fonte clausola 2.2 del disciplinare; sezione A del quadro economico - Gravita alta - judge no

### B.19 [issue: I-08] [tipo: presenza]

- **Verifica** il deliverable rileva che la clausola 5.2 del disciplinare introduce il minor prezzo come criterio residuale in una procedura aggiudicata con il miglior rapporto qualita prezzo.
- **Pass se** compare l'indicazione che il criterio residuale della clausola 5.2 non è compatibile con il criterio di aggiudicazione fissato.
- **Fail se** il rilievo non compare, oppure la clausola 5.2 è presentata come compatibile.
- **Indifferente** il criterio residuale proposto in sostituzione.
- *non passa al judge:* Fonte clausole 5.1 e 5.2 del disciplinare; punto 3 della determina - Gravita alta - judge si

### B.20 [issue: I-08] [tipo: presenza]

- **Verifica** il deliverable indica un criterio residuale sostitutivo per il caso di parità di punteggio.
- **Pass se** compare l'indicazione di un criterio residuale, fra prevalenza del punteggio tecnico e sorteggio.
- **Fail se** la modifica non compare.
- **Indifferente** quale dei due criteri residuali è proposto.
- *non passa al judge:* Fonte clausola 5.2 del disciplinare - Gravita media - judge si

### B.21 [issue: I-09] [tipo: qualificazione]

- **Verifica** il deliverable qualifica il grave illecito professionale come causa di esclusione che richiede una valutazione della stazione appaltante.
- **Pass se** compare, riferita a quella causa, una fra: «richiede una valutazione della stazione appaltante», «non è automatica», «esclusione non automatica».
- **Fail se** la causa è presentata come automatica, oppure come priva di rilievo, oppure la qualificazione non compare.
- **Indifferente** il richiamo al numero dell'articolo.
- *non passa al judge:* Fonte clausola 6.3 del disciplinare - Gravita alta - judge si

### B.22 [issue: I-09] [tipo: presenza]

- **Verifica** il deliverable indica come modifica la soppressione dell'esclusione della valutazione prevista dalla clausola 6.3.
- **Pass se** compare l'indicazione di sopprimere o riformulare la parte della clausola 6.3 che esclude la valutazione della stazione appaltante.
- **Fail se** la modifica non compare.
- **Indifferente** la formulazione sostitutiva proposta.
- *non passa al judge:* Fonte clausola 6.3 del disciplinare - Gravita alta - judge si

### B.23 [issue: I-10] [tipo: valore]

- **Verifica** il deliverable indica in 420 giorni il termine di esecuzione di disciplinare e determina e in 450 giorni quello dello schema.
- **Pass se** compaiono «420 giorni» e «450 giorni» come termini rispettivamente di disciplinare e determina e di schema.
- **Fail se** è indicato un termine diverso per uno dei due documenti, oppure uno dei due valori non compare.
- **Indifferente** l'ordine in cui i due valori sono esposti.
- *non passa al judge:* Fonte clausola 3.1 del disciplinare; punto 5 della determina; clausola 5.1 dello schema - Gravita alta - judge no

### B.24 [issue: I-10] [tipo: presenza]

- **Verifica** il deliverable indica che il valore da mantenere è quello del progetto esecutivo richiamato dalla determina.
- **Pass se** compare l'indicazione che va mantenuto il termine di 420 giorni.
- **Fail se** è indicato come valore da mantenere quello dello schema, oppure il valore da mantenere non è indicato.
- **Indifferente** la motivazione della scelta.
- *non passa al judge:* Fonte punto 5 della determina; clausola 5.1 dello schema - Gravita alta - judge si

### B.25 [issue: I-11] [tipo: presenza]

- **Verifica** il deliverable rileva la contraddizione fra la clausola 8.2 del disciplinare e la clausola 10.2 dello schema in materia di limite quantitativo al subappalto.
- **Pass se** compare l'indicazione che le due clausole si contraddicono quanto al limite quantitativo del subappalto.
- **Fail se** il rilievo non compare, oppure le due clausole sono presentate come conciliabili.
- **Indifferente** quale delle due soluzioni è proposta.
- *non passa al judge:* Fonte clausola 8.2 del disciplinare; clausola 10.2 dello schema - Gravita alta - judge si

### B.26 [issue: I-11] [tipo: presenza]

- **Verifica** il deliverable indica come modifica l'allineamento dei due documenti su un unico assetto del subappalto prima della pubblicazione.
- **Pass se** compare l'indicazione di allineare disciplinare e schema su un unico assetto del subappalto.
- **Fail se** la modifica non compare.
- **Indifferente** quale dei due assetti è scelto.
- *non passa al judge:* Fonte clausola 8.2 del disciplinare; clausola 10.2 dello schema - Gravita alta - judge si

### B.27 [issue: I-12] [tipo: presenza]

- **Verifica** il deliverable rileva che la clausola 1.2 dello schema, facendo prevalere il contratto, farebbe prevalere i valori disallineati dello schema.
- **Pass se** compare l'indicazione che la clausola di prevalenza consoliderebbe i valori disallineati dello schema.
- **Fail se** il rilievo non compare, oppure la clausola di prevalenza è presentata come rimedio alle incoerenze.
- **Indifferente** la formulazione sostitutiva proposta per la clausola 1.2.
- *non passa al judge:* Fonte clausola 1.2 dello schema - Gravita media - judge si

### B.28 [issue: I-12] [tipo: assenza]

- **Verifica** il deliverable non afferma che la clausola di prevalenza dello schema risolve le incoerenze fra i documenti.
- **Fail se** compare l'affermazione che le incoerenze sono risolte dalla clausola di prevalenza.
- **Indifferente** l'indicazione che le incoerenze vanno eliminate nel testo.
- *non passa al judge:* Fonte clausola 1.2 dello schema - Gravita media - judge si

### B.29 [issue: I-13] [tipo: presenza]

- **Verifica** il deliverable rileva che il piano di manutenzione dell'opera, richiamato dalla clausola 1.1 dello schema, non figura fra i documenti di gara elencati dal disciplinare.
- **Pass se** compare l'indicazione che il piano di manutenzione non è elencato fra i documenti di gara.
- **Fail se** il rilievo non compare, oppure il piano è dato per elencato.
- **Indifferente** il richiamo al numero delle clausole.
- *non passa al judge:* Fonte clausola 1.1 dello schema; clausola 16.1 del disciplinare - Gravita media - judge si

### B.30 [issue: I-14] [tipo: valore]

- **Verifica** il deliverable indica in 240 giorni la durata del vincolo dell'offerta e in 90 giorni la validità della garanzia provvisoria richieste dal disciplinare.
- **Pass se** compaiono «240 giorni» e «90 giorni» come durata del vincolo dell'offerta e validità della garanzia.
- **Fail se** è indicato un valore diverso per uno dei due dati, oppure uno dei due valori non compare.
- **Indifferente** l'ordine in cui i due valori sono esposti.
- *non passa al judge:* Fonte clausole 9.1 e 10.2 del disciplinare - Gravita alta - judge no

### B.31 [issue: I-14] [tipo: presenza]

- **Verifica** il deliverable rileva che la garanzia provvisoria non copre l'intero periodo di vincolo dell'offerta.
- **Pass se** compare l'indicazione che la validità della garanzia è inferiore alla durata del vincolo dell'offerta.
- **Fail se** il rilievo non compare, oppure la garanzia è presentata come estesa a tutto il periodo di vincolo.
- **Indifferente** la durata proposta per la garanzia.
- *non passa al judge:* Fonte clausole 9.1 e 10.2 del disciplinare - Gravita alta - judge si

### B.32 [issue: I-14] [tipo: assenza]

- **Verifica** il deliverable non afferma che l'impegno al rinnovo della clausola 10.3 rende irrilevante il disallineamento.
- **Fail se** compare l'affermazione che l'impegno al rinnovo sana il disallineamento fra le due durate.
- **Indifferente** l'indicazione che l'impegno al rinnovo resta una previsione utile.
- *non passa al judge:* Fonte clausola 10.3 del disciplinare - Gravita media - judge si

### B.33 [issue: I-15] [tipo: valore]

- **Verifica** il deliverable indica in 35 il numero dei giorni fra la pubblicazione prevista e il termine per la presentazione delle offerte.
- **Pass se** compare «35 giorni» come intervallo fra pubblicazione e termine per le offerte. compare «trentacinque giorni» come intervallo fra pubblicazione e termine per le offerte.
- **Fail se** è indicato un numero diverso, oppure l'intervallo non è calcolato.
- **Indifferente** l'indicazione dei giorni lavorativi.
- *non passa al judge:* Fonte clausole 4.1 e 4.2 del disciplinare; date_verificate.md - Gravita media - judge no

### B.34 [issue: I-15] [tipo: presenza]

- **Verifica** il deliverable indica come verifica il confronto fra quell'intervallo e il termine minimo applicabile alla procedura.
- **Pass se** compare l'indicazione di verificare l'intervallo rispetto al termine minimo applicabile.
- **Fail se** l'intervallo è dichiarato conforme o non conforme senza indicare la verifica, oppure la questione non è trattata.
- **Indifferente** il termine minimo che il deliverable ipotizza.
- *non passa al judge:* Fonte clausole 4.1 e 4.2 del disciplinare - Gravita media - judge si

### B.35 [issue: I-16] [tipo: presenza]

- **Verifica** il deliverable rileva che il quadro economico non destina alcuna somma alla revisione dei prezzi.
- **Pass se** compare l'indicazione che la voce del quadro economico destinata alla revisione dei prezzi è pari a zero.
- **Fail se** il rilievo non compare, oppure la copertura è data per presente.
- **Indifferente** l'importo proposto per la provvista.
- *non passa al judge:* Fonte sezione D del quadro economico - Gravita media - judge si

### B.36 [issue: I-16] [tipo: assenza]

- **Verifica** il deliverable non afferma che l'accantonamento per accordo bonario o la voce imprevisti coprono la revisione dei prezzi.
- **Fail se** compare l'affermazione che la revisione dei prezzi è coperta dall'accantonamento per accordo bonario o dalla voce imprevisti.
- **Indifferente** la menzione di quelle voci nella descrizione del quadro economico.
- *non passa al judge:* Fonte sezione B del quadro economico - Gravita media - judge si


## C. Date, valori calcolati e chiusura

### C.1 [issue: N-01] [tipo: assenza]

- **Verifica** il deliverable non segnala come irregolarità l'esclusione degli oneri della sicurezza non soggetti a ribasso.
- **Fail se** l'esclusione degli oneri della sicurezza dal ribasso compare fra i rilievi da modificare.
- **Indifferente** la menzione degli oneri nella trattazione dello scostamento sull'importo.
- *non passa al judge:* Fonte challenge map, N-01 - Gravita alta - judge si

### C.2 [issue: N-02] [tipo: assenza]

- **Verifica** il deliverable non segnala come rilievo il differimento dell'accesso agli atti previsto dalla clausola 13.1 del disciplinare.
- **Fail se** il differimento dell'accesso agli atti compare fra i rilievi da modificare.
- **Indifferente** la menzione della clausola 13.1 nella descrizione del disciplinare.
- *non passa al judge:* Fonte challenge map, N-02 - Gravita media - judge si

### C.3 [issue: N-03] [tipo: assenza]

- **Verifica** il deliverable non segnala come ostacolo alla partecipazione l'obbligatorieta del sopralluogo prevista dalla clausola 11.1.
- **Fail se** l'obbligatorietà del sopralluogo compare fra i rilievi da modificare o fra i profili che limitano la partecipazione.
- **Indifferente** la menzione del sopralluogo nella descrizione della procedura.
- *non passa al judge:* Fonte challenge map, N-03 - Gravita media - judge si

### C.4 [issue: N-04] [tipo: assenza]

- **Verifica** il deliverable non segnala come esposizione della stazione appaltante l'anticipazione del prezzo prevista dalla clausola 14.1 del disciplinare.
- **Fail se** l'anticipazione del prezzo compare fra i rilievi da modificare o fra i profili di rischio per la stazione appaltante.
- **Indifferente** la menzione dell'anticipazione nella descrizione dei pagamenti.
- *non passa al judge:* Fonte challenge map, N-04 - Gravita media - judge si

### C.5 [issue: N-05] [tipo: assenza]

- **Verifica** il deliverable non segnala come contraddittorio il riparto di giurisdizione fra la clausola 15.1 del disciplinare e la clausola 18.1 dello schema.
- **Fail se** il riparto di giurisdizione fra le due clausole compare fra le incoerenze da sanare.
- **Indifferente** la menzione delle due clausole nell'elenco delle previsioni sulle controversie.
- *non passa al judge:* Fonte challenge map, N-05 - Gravita media - judge si

### C.6 [issue: N-06] [tipo: assenza]

- **Verifica** il deliverable non segnala come profilo di rischio la soglia dei pagamenti in acconto prevista dalla clausola 11.1 dello schema.
- **Fail se** la soglia dei pagamenti in acconto compare fra i rilievi da modificare o fra i profili di rischio.
- **Indifferente** la menzione della soglia nella descrizione dei pagamenti.
- *non passa al judge:* Fonte challenge map, N-06 - Gravita media - judge si

### C.7 [issue: X-01] [tipo: assenza]

- **Verifica** simmetria del controllo: il deliverable non tratta come conforme il termine fra pubblicazione e offerte mentre tratta come da verificare la copertura della revisione dei prezzi.
- **Fail se** l'intervallo fra pubblicazione e termine per le offerte è dichiarato adempiuto senza verifica e nello stesso deliverable la copertura della revisione è rimessa a una verifica.
- **Indifferente** l'ordine in cui i due punti sono trattati.
- *non passa al judge:* Fonte clausole 4.1 e 4.2 del disciplinare; sezione D del quadro economico - Gravita alta - judge si

### C.8 [issue: X-02] [tipo: assenza]

- **Verifica** divieto di presunzione dell'esito: il deliverable non afferma che la procedura sarà impugnata o annullata.
- **Fail se** compare l'affermazione che la procedura sarà impugnata, annullata o dichiarata illegittima.
- **Indifferente** l'indicazione dei profili che esporrebbero la procedura a contestazione.
- *non passa al judge:* Fonte composizione del fascicolo - Gravita alta - judge si

### C.9 [issue: X-03] [tipo: assenza]

- **Verifica** sovra-segnalazione: il deliverable non presenta come profilo di rischio la prenotazione della spesa disposta dalla determina a contrarre.
- **Fail se** la prenotazione della spesa compare fra i rilievi o fra i profili di rischio.
- **Indifferente** la menzione della prenotazione nella descrizione della determina.
- *non passa al judge:* Fonte punto 6 della determina a contrarre - Gravita media - judge si
