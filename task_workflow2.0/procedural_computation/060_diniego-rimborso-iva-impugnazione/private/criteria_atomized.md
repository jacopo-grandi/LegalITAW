# WF2-060 - Criteri atomizzati

Forma a campi. Ciò che sta sotto la riga non passa al judge.


## A. Forma dell'output (interamente verifica meccanica)

### A.1 [tipo: valore]

- **Verifica** il deliverable è prodotto come file `tax_deadline_audit.md`.
- **Pass se** il file consegnato ha nome `tax_deadline_audit.md`.
- **Fail se** il file ha un altro nome o un'altra estensione.
- **Indifferente** la presenza di intestazioni aggiuntive.
- *non passa al judge:* Fonte task_spec.json, campo deliverable - Gravita media - judge no

### A.2 [tipo: struttura]

- **Verifica** il deliverable contiene, nell'ordine, le cinque sezioni obbligatorie del template.
- **Pass se** le cinque intestazioni di sezione compaiono nell'ordine indicato dal template.
- **Fail se** manca almeno una sezione o l'ordine è diverso.
- **Indifferente** la numerazione delle sottosezioni.
- *non passa al judge:* Fonte public/response_template.md - Gravita media - judge no

### A.3 [tipo: valore]

- **Verifica** il deliverable non supera il limite di 1800 parole.
- **Pass se** il conteggio delle parole del corpo del deliverable non supera 1800.
- **Fail se** il corpo del deliverable supera 1800 parole.
- **Indifferente** la lunghezza delle singole sezioni.
- *non passa al judge:* Fonte task_spec.json, campo limite_parole - Gravita media - judge no

### A.4 [tipo: struttura]

- **Verifica** ogni data indicata nella cronologia porta il riferimento al documento del fascicolo da cui è ricavata.
- **Pass se** accanto a ciascuna data compare il rinvio a uno dei quattro allegati.
- **Fail se** almeno una data della cronologia non porta alcun rinvio a un allegato.
- **Indifferente** la forma del rinvio, numero di documento o titolo.
- *non passa al judge:* Fonte public/01_task.md, richiesta sulla fonte - Gravita media - judge no

### A.5 [tipo: struttura]

- **Verifica** il calcolo della scadenza è esposto nei passaggi, con giorno iniziale, durata e risultato.
- **Pass se** nella sezione del computo compaiono il giorno di decorrenza, la durata del termine e la data di scadenza come passaggi distinti.
- **Fail se** la scadenza è indicata senza esporre i passaggi del computo.
- **Indifferente** la forma tabellare o discorsiva del computo.
- *non passa al judge:* Fonte public/01_task.md, richiesta sul percorso - Gravita media - judge no

### A.6 [tipo: presenza]

- **Verifica** il deliverable distingue i fatti provati dagli atti, le inferenze e i dati mancanti.
- **Pass se** compaiono, riferite a contenuti diversi, le tre distinzioni fra fatto documentato, inferenza e dato mancante.
- **Fail se** il deliverable presenta un solo piano indistinto di affermazioni.
- **Indifferente** le etichette usate per la distinzione.
- *non passa al judge:* Fonte public/response_template.md - Gravita media - judge no

### A.7 [tipo: assenza]

- **Verifica** il deliverable non richiama fonti normative estranee all'elenco chiuso del reference pack.
- **Fail se** compare un riferimento normativo che non figura in `private/fonti_chiuse.json`.
- **Indifferente** il richiamo ai protocolli e ai numeri di provvedimento del fascicolo.
- *non passa al judge:* Fonte private/fonti_chiuse.json - Gravita media - judge no


## B. Merito

Il fascicolo è esaminato al 30 giugno 2031: il diniego espresso è stato consegnato il 6 maggio 2031, il termine di sessanta giorni scade il 7 luglio 2031 e nessun ricorso è stato proposto. Il prompt chiede l'atto da impugnare, la scadenza con il calcolo esposto passaggio per passaggio, il documento da cui si ricava il giorno iniziale, gli adempimenti necessari, i passaggi che non servono e la valutazione della lettura del commercialista sul silenzio non impugnato.

### B.1 [issue: I-01] [tipo: qualificazione]

- **Verifica** il deliverable qualifica il provvedimento del 6 maggio 2031 come atto autonomamente impugnabile in quanto rifiuto espresso della restituzione.
- **Pass se** compare, riferita al provvedimento, una fra: «rifiuto espresso della restituzione», «diniego espresso di rimborso», «atto autonomamente impugnabile».
- **Fail se** l'atto è qualificato come non impugnabile, oppure la qualificazione non compare.
- **Indifferente** l'indicazione della lettera dell'elenco degli atti impugnabili.
- *non passa al judge:* Fonte dispositivo del provvedimento di diniego - Gravita alta - judge si

### B.2 [issue: I-01] [tipo: assenza]

- **Verifica** il deliverable non indica la richiesta di documentazione del 12 febbraio 2031 come l'atto da impugnare.
- **Fail se** la richiesta del 12 febbraio 2031 è indicata come atto da impugnare.
- **Indifferente** la menzione della richiesta nella cronologia.
- *non passa al judge:* Fonte richiesta del 12 febbraio 2031 - Gravita alta - judge si

### B.3 [issue: I-02] [tipo: valore]

- **Verifica** il deliverable indica il 6 maggio 2031 come giorno da cui decorre il termine di impugnazione.
- **Pass se** compare «6 maggio 2031» come giorno di decorrenza del termine. compare «06/05/2031» come giorno di decorrenza del termine.
- **Fail se** è indicato un giorno di decorrenza diverso, oppure la decorrenza non è indicata.
- **Indifferente** l'indicazione dell'ora della consegna.
- *non passa al judge:* Fonte ricevuta di avvenuta consegna; date_verificate.md - Gravita alta - judge no

### B.4 [issue: I-02] [tipo: attribuzione]

- **Verifica** il deliverable riconduce la decorrenza alla ricevuta di avvenuta consegna del provvedimento.
- **Pass se** la decorrenza è ricondotta a una fra: «ricevuta di avvenuta consegna», «consegna della posta elettronica certificata», «notificazione del provvedimento».
- **Fail se** la decorrenza è ricondotta alla data apposta sul provvedimento, al numero di protocollo, oppure l'atto di decorrenza non è indicato.
- **Indifferente** la menzione del gestore del servizio.
- *non passa al judge:* Fonte ricevuta di avvenuta consegna - Gravita alta - judge si

### B.5 [issue: I-02] [tipo: assenza]

- **Verifica** il deliverable non indica il 29 aprile 2031 come giorno da cui decorre il termine.
- **Fail se** il 29 aprile 2031 è indicato come giorno di decorrenza del termine.
- **Indifferente** la menzione del 29 aprile 2031 come data apposta sul provvedimento.
- *non passa al judge:* Fonte intestazione del provvedimento - Gravita alta - judge si

### B.6 [issue: I-03] [tipo: valore]

- **Verifica** il deliverable indica in sessanta giorni la durata del termine per proporre ricorso.
- **Pass se** compare «sessanta giorni» come durata del termine. compare «60 giorni» come durata del termine.
- **Fail se** è indicata una durata diversa, oppure la durata non è indicata.
- **Indifferente** il richiamo all'articolo che fissa il termine.
- *non passa al judge:* Fonte disciplina del processo tributario - Gravita alta - judge no

### B.7 [issue: I-03] [tipo: presenza]

- **Verifica** il deliverable afferma che il giorno di notificazione non si computa nel termine.
- **Pass se** compare l'affermazione che il giorno iniziale non si computa. compare l'affermazione che il termine decorre dal giorno successivo alla notificazione.
- **Fail se** il termine è computato includendo il 6 maggio 2031, oppure la regola di computo non compare.
- **Indifferente** la citazione della norma sul computo dei termini.
- *non passa al judge:* Fonte disciplina sul computo dei termini processuali - Gravita media - judge si

### B.8 [issue: I-04] [tipo: valore]

- **Verifica** il deliverable indica il 7 luglio 2031 come scadenza del termine per proporre ricorso.
- **Pass se** compare «7 luglio 2031» come scadenza del termine. compare «07/07/2031» come scadenza del termine.
- **Fail se** è indicata una data di scadenza diversa, oppure la scadenza non è indicata.
- **Indifferente** l'indicazione dell'ora entro cui l'atto va notificato.
- *non passa al judge:* Fonte computo verificato; date_verificate.md - Gravita alta - judge no

### B.9 [issue: I-04] [tipo: presenza]

- **Verifica** il deliverable afferma che il sessantesimo giorno cade di sabato e che il termine è prorogato al primo giorno successivo non festivo.
- **Pass se** compare l'indicazione che la scadenza nominale cade di sabato e che opera la proroga al giorno non festivo successivo.
- **Fail se** la proroga non è affermata, oppure è affermata senza indicare il fatto che la determina.
- **Indifferente** la citazione della norma sulla proroga.
- *non passa al judge:* Fonte calendario 2031; disciplina sulla proroga dei termini processuali - Gravita alta - judge si

### B.10 [issue: I-04] [tipo: assenza]

- **Verifica** il deliverable non indica il 5 luglio 2031 come scadenza del termine per proporre ricorso.
- **Fail se** il 5 luglio 2031 è indicato come data entro cui il ricorso va proposto.
- **Indifferente** la menzione del 5 luglio 2031 come sessantesimo giorno nominale.
- *non passa al judge:* Fonte computo verificato - Gravita alta - judge si

### B.11 [issue: I-05] [tipo: valore]

- **Verifica** il deliverable indica in sette il numero dei giorni che residuano alla data di riferimento.
- **Pass se** compare «sette giorni» come tempo residuo. compare «7 giorni» come tempo residuo.
- **Fail se** è indicato un numero diverso di giorni residui, oppure il tempo residuo non è indicato.
- **Indifferente** l'indicazione dei giorni lavorativi residui.
- *non passa al judge:* Fonte data di riferimento e scadenza calcolata - Gravita alta - judge no

### B.12 [issue: I-06] [tipo: qualificazione]

- **Verifica** il deliverable qualifica la richiesta del 12 febbraio 2031 come atto istruttorio non compreso fra quelli autonomamente impugnabili.
- **Pass se** compare, riferita a quella richiesta, una fra: «atto istruttorio», «non autonomamente impugnabile», «non rientra fra gli atti impugnabili».
- **Fail se** la richiesta è qualificata come autonomamente impugnabile, oppure la qualificazione non compare.
- **Indifferente** il rilievo che la richiesta stessa dichiara di non essere un provvedimento.
- *non passa al judge:* Fonte richiesta del 12 febbraio 2031 - Gravita alta - judge si

### B.13 [issue: I-07] [tipo: valore]

- **Verifica** il deliverable indica il 18 febbraio 2030 come giorno in cui si è compiuto il decorso dei novanta giorni dall'istanza di rimborso.
- **Pass se** compare «18 febbraio 2030» come compimento dei novanta giorni. compare «18/02/2030» come compimento dei novanta giorni.
- **Fail se** è indicata una data diversa, oppure il decorso dei novanta giorni non è collocato nel tempo.
- **Indifferente** l'indicazione del giorno della settimana.
- *non passa al judge:* Fonte istanza del 20 novembre 2029; date_verificate.md - Gravita alta - judge no

### B.14 [issue: I-07] [tipo: presenza]

- **Verifica** il deliverable afferma che il rifiuto tacito formatosi per decorso dei novanta giorni era impugnabile senza termine di decadenza.
- **Pass se** compare l'indicazione che l'impugnazione del rifiuto tacito non era soggetta a un termine di decadenza.
- **Fail se** è affermato che il rifiuto tacito andava impugnato entro un termine di decadenza, oppure la questione non è trattata.
- **Indifferente** il richiamo al termine di prescrizione del diritto al rimborso.
- *non passa al judge:* Fonte disciplina del processo tributario sul rifiuto tacito - Gravita alta - judge si

### B.15 [issue: I-07] [tipo: assenza]

- **Verifica** il deliverable non afferma che il diritto al rimborso è decaduto per non aver impugnato il rifiuto tacito.
- **Fail se** compare l'affermazione che la mancata impugnazione del rifiuto tacito ha prodotto decadenza o inammissibilità del ricorso attuale.
- **Indifferente** il rilievo sul tempo trascorso fra l'istanza e il provvedimento.
- *non passa al judge:* Fonte disciplina del processo tributario sul rifiuto tacito - Gravita alta - judge si

### B.16 [issue: I-08] [tipo: qualificazione]

- **Verifica** il deliverable indica come organo giurisdizionale competente la corte di giustizia tributaria di primo grado.
- **Pass se** compare «corte di giustizia tributaria di primo grado» come organo davanti al quale proporre il ricorso.
- **Fail se** è indicato un altro organo, oppure l'organo competente non è indicato.
- **Indifferente** l'indicazione della sede territoriale.
- *non passa al judge:* Fonte avvertenze del provvedimento; riforma della giustizia tributaria - Gravita alta - judge si

### B.17 [issue: I-08] [tipo: assenza]

- **Verifica** il deliverable non indica la commissione tributaria provinciale come organo davanti al quale proporre il ricorso.
- **Fail se** la commissione tributaria provinciale è indicata come organo competente.
- **Indifferente** il richiamo alla denominazione previgente con la qualificazione di denominazione storica.
- *non passa al judge:* Fonte riforma della giustizia tributaria - Gravita media - judge si

### B.18 [issue: I-09] [tipo: presenza]

- **Verifica** il deliverable afferma che il provvedimento di diniego non contiene iscrizione a ruolo ne intimazione di pagamento.
- **Pass se** compare l'indicazione che l'atto non contiene iscrizione a ruolo o intimazione di pagamento.
- **Fail se** è affermato che l'atto impone un pagamento, oppure la questione non è trattata.
- **Indifferente** il rilievo che il credito resta esposto in dichiarazione.
- *non passa al judge:* Fonte dispositivo del provvedimento di diniego - Gravita media - judge si

### B.19 [issue: I-10] [tipo: presenza]

- **Verifica** il deliverable indica il contributo unificato come adempimento da assolvere e documentare al momento della costituzione in giudizio.
- **Pass se** compare l'indicazione che il contributo unificato va versato e documentato alla costituzione in giudizio.
- **Fail se** l'adempimento non compare, oppure è presentato come non dovuto.
- **Indifferente** l'indicazione della modalità di versamento.
- *non passa al judge:* Fonte disciplina sul contributo unificato - Gravita media - judge si

### B.20 [issue: I-10] [tipo: assenza]

- **Verifica** il deliverable non indica un importo determinato del contributo unificato.
- **Fail se** compare un importo in euro presentato come contributo unificato dovuto per questa controversia.
- **Indifferente** l'indicazione che l'importo dipende dallo scaglione di valore e va verificato sulle tabelle vigenti.
- *non passa al judge:* Fonte disciplina sul contributo unificato - Gravita media - judge si

### B.21 [issue: I-11] [tipo: valore]

- **Verifica** il deliverable indica in euro 318.400,00 il valore della controversia.
- **Pass se** compare «euro 318.400,00» come valore della controversia. compare «318.400,00» come valore della controversia.
- **Fail se** è indicato un valore diverso, oppure il valore della controversia non è indicato.
- **Indifferente** l'indicazione degli interessi maturati sul credito.
- *non passa al judge:* Fonte dispositivo del provvedimento; prospetto della destinazione del credito - Gravita media - judge no

### B.22 [issue: I-12] [tipo: presenza]

- **Verifica** il deliverable afferma che il fascicolo non contiene il messaggio del 10 marzo 2031 ne la documentazione con esso trasmessa.
- **Pass se** compare, riferita alla trasmissione del 10 marzo 2031, una fra: «non è nel fascicolo», «non risulta dagli atti disponibili», «il contenuto non è verificabile sui documenti presenti».
- **Fail se** la trasmissione è data per verificata nel contenuto, oppure la lacuna non è dichiarata.
- **Indifferente** il rilievo che la trasmissione è riferita dall'ufficio.
- *non passa al judge:* Fonte punto 3 della motivazione; composizione del fascicolo - Gravita alta - judge si

### B.23 [issue: I-12] [tipo: presenza]

- **Verifica** il deliverable indica quali documenti occorrono per verificare la ricostruzione dell'ufficio sulla documentazione trasmessa.
- **Pass se** compare l'indicazione di almeno un documento fra il messaggio del 10 marzo 2031, le sue ricevute e le dichiarazioni doganali di esportazione.
- **Fail se** la lacuna è dichiarata senza indicare che cosa serve per colmarla.
- **Indifferente** il numero di documenti elencati.
- *non passa al judge:* Fonte public/01_task.md, richiesta sui dati mancanti - Gravita alta - judge si

### B.24 [issue: I-13] [tipo: valore]

- **Verifica** il deliverable indica in euro 1.020.000,00 l'ammontare delle operazioni la cui qualificazione l'ufficio dichiara di non avere riscontrato.
- **Pass se** compare «euro 1.020.000,00» come ammontare delle operazioni contestate. compare «1.020.000,00» come ammontare delle operazioni contestate.
- **Fail se** è indicato un ammontare diverso, oppure l'ammontare contestato non è isolato.
- **Indifferente** l'indicazione della percentuale di incidenza rideterminata.
- *non passa al judge:* Fonte punto 4 della motivazione; prospetto della dichiarazione - Gravita media - judge no

### B.25 [issue: I-13] [tipo: assenza]

- **Verifica** il deliverable non afferma che la contestazione dell'ufficio riguarda le cessioni intracomunitarie dichiarate per euro 3.148.000,00.
- **Fail se** le cessioni intracomunitarie per euro 3.148.000,00 sono indicate fra le operazioni contestate dall'ufficio.
- **Indifferente** la menzione delle cessioni intracomunitarie nella descrizione della dichiarazione.
- *non passa al judge:* Fonte punti 3 e 4 della motivazione - Gravita media - judge si


## C. Date, valori calcolati e chiusura

### C.1 [issue: I-04] [tipo: assenza]

- **Verifica** il deliverable non presenta il 7 luglio 2031 come risultato di un termine decorrente dal 29 aprile 2031.
- **Fail se** il 7 luglio 2031 è ricavato da un computo che parte dal 29 aprile 2031.
- **Indifferente** la menzione del 29 aprile 2031 come data del provvedimento.
- *non passa al judge:* Fonte computo verificato - Gravita alta - judge si

### C.2 [issue: N-01] [tipo: assenza]

- **Verifica** il deliverable non applica la sospensione feriale dei termini al periodo che va dal 6 maggio al 7 luglio 2031.
- **Fail se** la sospensione feriale è applicata per spostare la scadenza oltre il 7 luglio 2031.
- **Indifferente** la menzione della sospensione feriale con l'indicazione che il periodo non la interseca.
- *non passa al judge:* Fonte challenge map, N-01 - Gravita alta - judge si

### C.3 [issue: N-02] [tipo: assenza]

- **Verifica** il deliverable non indica il reclamo e mediazione come fase da percorrere prima del ricorso.
- **Fail se** il reclamo e mediazione compare come adempimento necessario o come termine da computare.
- **Indifferente** la menzione dell'istituto con l'indicazione che non è più applicabile.
- *non passa al judge:* Fonte challenge map, N-02 - Gravita alta - judge si

### C.4 [issue: N-03] [tipo: assenza]

- **Verifica** il deliverable non indica l'istanza di sospensione dell'atto impugnato come passaggio necessario.
- **Fail se** l'istanza cautelare di sospensione compare fra gli adempimenti necessari o fra i profili di rischio.
- **Indifferente** la menzione del rimedio cautelare con l'indicazione che l'atto non produce effetti esecutivi.
- *non passa al judge:* Fonte challenge map, N-03 - Gravita media - judge si

### C.5 [issue: N-04] [tipo: assenza]

- **Verifica** il deliverable non qualifica come perentorio il termine di trenta giorni assegnato dalla richiesta del 12 febbraio 2031.
- **Fail se** il termine di trenta giorni della richiesta istruttoria è qualificato come perentorio o come decadenziale.
- **Indifferente** la menzione del termine di trenta giorni come termine assegnato dall'ufficio.
- *non passa al judge:* Fonte challenge map, N-04 - Gravita media - judge si

### C.6 [issue: X-01] [tipo: assenza]

- **Verifica** simmetria del controllo: il deliverable non tratta come provata la trasmissione parziale del 10 marzo 2031 mentre tratta come non provata la documentazione mancante.
- **Fail se** il contenuto della trasmissione del 10 marzo 2031 è dato per accertato e nello stesso deliverable la documentazione mancante è dichiarata non verificabile.
- **Indifferente** l'ordine in cui i due punti sono trattati.
- *non passa al judge:* Fonte punto 3 della motivazione; composizione del fascicolo - Gravita media - judge si

### C.7 [issue: X-02] [tipo: assenza]

- **Verifica** divieto di presunzione dell'esito: il deliverable non afferma che il ricorso contro il diniego sarà accolto.
- **Fail se** compare l'affermazione che il ricorso sarà accolto o che il rimborso sarà riconosciuto.
- **Indifferente** l'indicazione dei documenti da produrre in giudizio.
- *non passa al judge:* Fonte motivazione del provvedimento - Gravita alta - judge si

### C.8 [issue: X-03] [tipo: assenza]

- **Verifica** sovra-segnalazione: il deliverable non presenta come profilo di rischio il tempo trascorso fra l'istanza del 20 novembre 2029 e la richiesta del 12 febbraio 2031.
- **Fail se** la durata dell'istruttoria compare fra i profili di rischio o fra le irregolarità che incidono sulla proponibilità del ricorso.
- **Indifferente** la menzione della durata dell'istruttoria nella cronologia.
- *non passa al judge:* Fonte cronologia degli atti - Gravita media - judge si
