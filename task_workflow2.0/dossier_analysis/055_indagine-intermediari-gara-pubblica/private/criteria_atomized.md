# WF2-055 - Criteri atomizzati

Forma a campi. Ciò che sta sotto la riga non passa al judge.


## A. Forma dell'output (interamente verifica meccanica)

### A.1 [tipo: valore]

- **Verifica** il deliverable è prodotto come file `investigation_matrix.md`.
- **Pass se** il file consegnato ha nome `investigation_matrix.md`.
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

- **Verifica** il deliverable non supera il limite di 2400 parole.
- **Pass se** il conteggio delle parole del corpo del deliverable non supera 2400.
- **Fail se** il corpo del deliverable supera 2400 parole.
- **Indifferente** la lunghezza delle singole sezioni.
- *non passa al judge:* Fonte task_spec.json, campo limite_parole - Gravita media - judge no

### A.4 [tipo: struttura]

- **Verifica** la matrice riporta per ciascuna voce l'elemento rilevato, il documento di provenienza, la qualificazione e l'azione conseguente.
- **Pass se** ciascuna riga della matrice porta i quattro elementi.
- **Fail se** almeno una riga omette uno dei quattro elementi.
- **Indifferente** l'ordine delle colonne.
- *non passa al judge:* Fonte public/response_template.md - Gravita media - judge no

### A.5 [tipo: presenza]

- **Verifica** il deliverable distingue i fatti provati dagli atti, le risultanze non verificate documentalmente e i dati mancanti.
- **Pass se** compaiono, riferite a contenuti diversi, le tre distinzioni fra fatto documentato, risultanza non verificata e dato mancante.
- **Fail se** il deliverable presenta un solo piano indistinto di affermazioni.
- **Indifferente** le etichette usate per la distinzione.
- *non passa al judge:* Fonte public/response_template.md - Gravita media - judge no

### A.6 [tipo: assenza]

- **Verifica** il deliverable non richiama fonti normative estranee all'elenco chiuso del reference pack.
- **Fail se** compare un riferimento normativo che non figura in `private/fonti_chiuse.json`.
- **Indifferente** il richiamo alle clausole della procedura interna, che non sono fonti normative.
- *non passa al judge:* Fonte private/fonti_chiuse.json - Gravita media - judge no


## B. Merito

Il fascicolo è esaminato al 26 maggio 2031: la commessa è aggiudicata, l'incarico all'intermediario è in vigore, entrambe le fatture sono pagate e lo screening è stato acquisito ad aprile 2031. Il prompt chiede la matrice elemento per elemento con documento di provenienza, qualificazione e azione, l'indicazione dei documenti da incrociare, il valore delle risultanze dello screening, le misure conservative immediate, la distinzione fra elementi che costituiscono rilievo e elementi che non lo costituiscono, e la valutazione della lettura del direttore commerciale.

### B.1 [issue: I-01] [tipo: qualificazione]

- **Verifica** il deliverable qualifica il corrispettivo del contratto come corrispettivo a risultato ai sensi della procedura interna.
- **Pass se** compare, riferito al corrispettivo, una fra: «corrispettivo a risultato», «success fee», «corrispettivo condizionato all'aggiudicazione».
- **Fail se** il corrispettivo è qualificato come compenso per attività svolte, oppure la qualificazione non compare.
- **Indifferente** il richiamo alla percentuale applicata.
- *non passa al judge:* Fonte clausole 4.1 e 4.2 del contratto; clausola 5.2 della procedura - Gravita alta - judge si

### B.2 [issue: I-01] [tipo: presenza]

- **Verifica** il deliverable afferma che il fascicolo non contiene l'autorizzazione scritta del direttore generale prevista per il corrispettivo a risultato.
- **Pass se** compare l'indicazione che l'autorizzazione scritta non risulta dagli atti.
- **Fail se** l'autorizzazione è data per rilasciata o per negata, oppure la lacuna non è dichiarata.
- **Indifferente** il richiamo al parere di Compliance come presupposto dell'autorizzazione.
- *non passa al judge:* Fonte clausola 5.2 della procedura; composizione del fascicolo - Gravita alta - judge si

### B.3 [issue: I-01] [tipo: assenza]

- **Verifica** il deliverable non afferma che la procedura interna vieta il corrispettivo a risultato.
- **Fail se** compare l'affermazione che il corrispettivo a risultato è vietato dalla procedura interna.
- **Indifferente** il rilievo che la procedura lo subordina a un'autorizzazione.
- *non passa al judge:* Fonte clausola 5.2 della procedura - Gravita media - judge si

### B.4 [issue: I-02] [tipo: valore]

- **Verifica** il deliverable indica in euro 209.000,00 il corrispettivo complessivo riconosciuto all'intermediario.
- **Pass se** compare «euro 209.000,00» come corrispettivo complessivo. compare «209.000,00» come corrispettivo complessivo.
- **Fail se** è indicato un importo diverso, oppure il corrispettivo complessivo non è calcolato.
- **Indifferente** l'indicazione degli importi al lordo dell'imposta.
- *non passa al judge:* Fonte somma delle fatture n. 18/2030 e n. 4/2031 - Gravita alta - judge no

### B.5 [issue: I-02] [tipo: valore]

- **Verifica** il deliverable indica nel 5,00 per cento l'incidenza del corrispettivo sul valore della commessa.
- **Pass se** compare «5,00 per cento» come incidenza del corrispettivo. compare «5 per cento» come incidenza del corrispettivo.
- **Fail se** è indicata un'incidenza diversa, oppure l'incidenza non è calcolata.
- **Indifferente** l'indicazione dell'incidenza sul solo importo dei lavori.
- *non passa al judge:* Fonte corrispettivo complessivo; determina di aggiudicazione - Gravita alta - judge no

### B.6 [issue: I-02] [tipo: presenza]

- **Verifica** il deliverable afferma che l'incidenza supera la soglia di segnalazione del 3 per cento fissata dalla procedura interna.
- **Pass se** compare l'indicazione che la soglia di segnalazione del 3 per cento è superata.
- **Fail se** il superamento non è affermato, oppure è riferito a una soglia diversa.
- **Indifferente** il richiamo al numero della clausola.
- *non passa al judge:* Fonte clausola 6.3 della procedura - Gravita alta - judge si

### B.7 [issue: I-02] [tipo: qualificazione]

- **Verifica** il deliverable qualifica come trasmissione di una segnalazione scritta all'Organismo di Vigilanza l'obbligo che deriva dal superamento della soglia.
- **Pass se** compare l'indicazione che l'obbligo consiste nel trasmettere una segnalazione scritta all'Organismo di Vigilanza.
- **Fail se** al superamento è attribuita una conseguenza diversa, oppure l'obbligo non è indicato.
- **Indifferente** l'indicazione del termine entro cui la segnalazione va trasmessa.
- *non passa al judge:* Fonte clausola 6.3 della procedura - Gravita alta - judge si

### B.8 [issue: I-02] [tipo: presenza]

- **Verifica** il deliverable afferma che la segnalazione all'Organismo di Vigilanza non risulta dagli atti.
- **Pass se** compare l'indicazione che la segnalazione non risulta dal fascicolo.
- **Fail se** la segnalazione è data per trasmessa, oppure la lacuna non è dichiarata.
- **Indifferente** l'indicazione del soggetto onerato della trasmissione.
- *non passa al judge:* Fonte clausola 6.3 della procedura; composizione del fascicolo - Gravita alta - judge si

### B.9 [issue: I-02] [tipo: assenza]

- **Verifica** il deliverable non afferma che il superamento della soglia di segnalazione integra di per sé una violazione.
- **Fail se** compare l'affermazione che il superamento della soglia del 3 per cento costituisce violazione della procedura o irregolarità.
- **Indifferente** l'indicazione che l'omessa segnalazione costituisce violazione.
- *non passa al judge:* Fonte clausola 6.4 della procedura - Gravita alta - judge si

### B.10 [issue: I-03] [tipo: valore]

- **Verifica** il deliverable indica il 30 ottobre 2030 come data del primo pagamento disposto in favore dell'intermediario.
- **Pass se** compare «30 ottobre 2030» come data del primo pagamento. compare «30/10/2030» come data del primo pagamento.
- **Fail se** è indicata una data diversa, oppure la data del primo pagamento non è indicata.
- **Indifferente** l'indicazione della data valuta.
- *non passa al judge:* Fonte estratto dei pagamenti; date_verificate.md - Gravita alta - judge no

### B.11 [issue: I-03] [tipo: presenza]

- **Verifica** il deliverable afferma che il primo pagamento è stato disposto nel corso della procedura di gara, prima dell'aggiudicazione.
- **Pass se** compare l'indicazione che il pagamento precede l'aggiudicazione e cade durante la procedura.
- **Fail se** il pagamento è collocato dopo l'aggiudicazione, oppure la sua collocazione rispetto alla procedura non è rilevata.
- **Indifferente** l'indicazione del numero di giorni intercorsi.
- *non passa al judge:* Fonte estratto dei pagamenti; determina di aggiudicazione - Gravita alta - judge si

### B.12 [issue: I-03] [tipo: attribuzione]

- **Verifica** il deliverable ricava la collocazione del pagamento dal confronto fra l'estratto dei pagamenti e la determina di aggiudicazione.
- **Pass se** il rilievo è ricondotto a entrambi i documenti, l'estratto dei pagamenti e la determina.
- **Fail se** il rilievo è fondato su un solo documento, oppure la provenienza non è indicata.
- **Indifferente** l'ordine in cui i due documenti sono citati.
- *non passa al judge:* Fonte estratto dei pagamenti; determina di aggiudicazione - Gravita alta - judge si

### B.13 [issue: I-04] [tipo: valore]

- **Verifica** il deliverable indica il 4 settembre 2030 come data del contratto di consulenza e il 16 settembre 2030 come data di pubblicazione del bando.
- **Pass se** compaiono «4 settembre 2030» e «16 settembre 2030» come date rispettivamente del contratto e del bando.
- **Fail se** è indicata una data diversa per uno dei due fatti, oppure una delle due date non compare.
- **Indifferente** l'ordine in cui le due date sono esposte.
- *non passa al judge:* Fonte contratto; punto 2 della determina; date_verificate.md - Gravita alta - judge no

### B.14 [issue: I-04] [tipo: presenza]

- **Verifica** il deliverable rileva che il conferimento dell'incarico precede la pubblicazione del bando.
- **Pass se** compare l'indicazione che l'incarico è anteriore alla pubblicazione del bando.
- **Fail se** il rilievo non compare, oppure l'incarico è collocato dopo il bando.
- **Indifferente** l'indicazione del numero di giorni di anticipo.
- *non passa al judge:* Fonte contratto; punto 2 della determina - Gravita alta - judge si

### B.15 [issue: I-04] [tipo: assenza]

- **Verifica** il deliverable non afferma che l'anteriorità dell'incarico rispetto al bando costituisce di per sé una irregolarità della procedura di gara.
- **Fail se** compare l'affermazione che l'anteriorità dell'incarico rende irregolare o annullabile la procedura di gara.
- **Indifferente** l'indicazione che l'anteriorità è un elemento da approfondire.
- *non passa al judge:* Fonte contratto; determina di aggiudicazione - Gravita media - judge si

### B.16 [issue: I-05] [tipo: qualificazione]

- **Verifica** il deliverable qualifica la descrizione delle attivita del contratto come non conforme al requisito di analiticità della procedura interna.
- **Pass se** compare, riferita agli articoli 1 e 2 del contratto, una fra: «descrizione generica», «non analitica», «priva dell'indicazione dei prodotti attesi».
- **Fail se** la descrizione è presentata come conforme, oppure la qualificazione non compare.
- **Indifferente** la proposta di riformulazione della clausola.
- *non passa al judge:* Fonte articoli 1 e 2 del contratto; clausola 4.1, lettera a), della procedura - Gravita alta - judge si

### B.17 [issue: I-05] [tipo: assenza]

- **Verifica** il deliverable non afferma che la genericità della descrizione dimostra che l'attività non è stata svolta.
- **Fail se** compare l'affermazione che la genericità della descrizione prova l'inesistenza della prestazione.
- **Indifferente** l'indicazione che l'esistenza della prestazione resta da accertare.
- *non passa al judge:* Fonte articoli 1 e 2 del contratto - Gravita alta - judge si

### B.18 [issue: I-06] [tipo: presenza]

- **Verifica** il deliverable rileva che il contratto non contiene l'obbligo di rendicontazione periodica richiesto dalla procedura interna.
- **Pass se** compare l'indicazione che l'obbligo di rendicontazione non figura nel contratto.
- **Fail se** il rilievo non compare, oppure l'obbligo è dato per presente.
- **Indifferente** il richiamo al numero della clausola della procedura.
- *non passa al judge:* Fonte contratto; clausola 4.1, lettera b), della procedura - Gravita alta - judge si

### B.19 [issue: I-06] [tipo: presenza]

- **Verifica** il deliverable indica che per entrambi i pagamenti all'intermediario la colonna della rendicontazione allegata riporta l'assenza.
- **Pass se** compare l'indicazione che per i due pagamenti all'intermediario la rendicontazione allegata risulta assente.
- **Fail se** è indicato che almeno uno dei due pagamenti reca rendicontazione, oppure il dato non è rilevato.
- **Indifferente** l'indicazione del soggetto autorizzante.
- *non passa al judge:* Fonte estratto dei pagamenti - Gravita alta - judge si

### B.20 [issue: I-07] [tipo: presenza]

- **Verifica** il deliverable rileva che il contratto non contiene il diritto di audit sui documenti relativi all'incarico.
- **Pass se** compare l'indicazione che il diritto di audit non figura nel contratto.
- **Fail se** il rilievo non compare, oppure il diritto è dato per presente.
- **Indifferente** il richiamo al numero della clausola della procedura.
- *non passa al judge:* Fonte contratto; clausola 4.1, lettera d), della procedura - Gravita media - judge si

### B.21 [issue: I-07] [tipo: presenza]

- **Verifica** il deliverable rileva che il contratto non contiene il divieto di subappalto dell'incarico senza consenso scritto.
- **Pass se** compare l'indicazione che il divieto di subappalto non figura nel contratto.
- **Fail se** il rilievo non compare, oppure il divieto è dato per presente.
- **Indifferente** il richiamo al numero della clausola della procedura.
- *non passa al judge:* Fonte contratto; clausola 4.1, lettera f), della procedura - Gravita media - judge si

### B.22 [issue: I-08] [tipo: presenza]

- **Verifica** il deliverable afferma che il fascicolo non contiene la scheda di due diligence né il parere di Compliance.
- **Pass se** compare l'indicazione che scheda di due diligence e parere di Compliance non risultano dagli atti.
- **Fail se** uno dei due documenti è dato per esistente, oppure la lacuna non è dichiarata.
- **Indifferente** l'indicazione del termine entro cui il parere andava reso.
- *non passa al judge:* Fonte clausole 3.1 e 3.4 della procedura; composizione del fascicolo - Gravita alta - judge si

### B.23 [issue: I-08] [tipo: qualificazione]

- **Verifica** il deliverable qualifica il parere di Compliance come condizione per il conferimento dell'incarico secondo la procedura interna.
- **Pass se** compare l'indicazione che il parere è condizione per il conferimento dell'incarico.
- **Fail se** il parere è presentato come facoltativo, oppure la sua funzione non è indicata.
- **Indifferente** il richiamo al numero della clausola.
- *non passa al judge:* Fonte clausola 3.4 della procedura - Gravita alta - judge si

### B.24 [issue: I-09] [tipo: valore]

- **Verifica** il deliverable indica il 14 aprile 2031 come data del rapporto di screening reputazionale.
- **Pass se** compare «14 aprile 2031» come data del rapporto di screening. compare «14/04/2031» come data del rapporto di screening.
- **Fail se** è indicata una data diversa, oppure la data del rapporto non è rilevata.
- **Indifferente** l'indicazione del riferimento incarico.
- *non passa al judge:* Fonte rapporto di screening; date_verificate.md - Gravita alta - judge no

### B.25 [issue: I-09] [tipo: presenza]

- **Verifica** il deliverable rileva che lo screening è successivo sia al conferimento dell'incarico sia a entrambi i pagamenti.
- **Pass se** compare l'indicazione che il rapporto è posteriore al contratto e ai due pagamenti.
- **Fail se** il rilievo non compare, oppure lo screening è collocato prima del conferimento.
- **Indifferente** l'indicazione del numero di mesi trascorsi.
- *non passa al judge:* Fonte date del contratto, dei pagamenti e del rapporto; clausola 3.1 della procedura - Gravita alta - judge si

### B.26 [issue: I-10] [tipo: presenza]

- **Verifica** il deliverable riporta il collegamento fra l'amministratore dell'intermediario e la componente della commissione giudicatrice ing. Melania Trescorato.
- **Pass se** compare l'indicazione del collegamento, con il nome della componente della commissione.
- **Fail se** il collegamento non è riportato, oppure è riferito a un soggetto diverso.
- **Indifferente** l'indicazione del periodo del rapporto di collaborazione.
- *non passa al judge:* Fonte paragrafo 4.2 del rapporto di screening; punto 4 della determina - Gravita alta - judge si

### B.27 [issue: I-10] [tipo: qualificazione]

- **Verifica** il deliverable qualifica quel collegamento come risultanza di fonti aperte non verificata documentalmente.
- **Pass se** compare, riferita al collegamento, una fra: «non verificato documentalmente», «risultanza di fonti aperte», «da verificare con documentazione contrattuale».
- **Fail se** il collegamento è presentato come provato, oppure la qualificazione non compare.
- **Indifferente** il richiamo al paragrafo del rapporto.
- *non passa al judge:* Fonte paragrafi 4.2 e 5 del rapporto di screening - Gravita alta - judge si

### B.28 [issue: I-10] [tipo: presenza]

- **Verifica** il deliverable indica come azione la verifica documentale del collegamento.
- **Pass se** compare l'indicazione di acquisire la documentazione contrattuale del rapporto di collaborazione.
- **Fail se** l'azione non compare.
- **Indifferente** il soggetto presso cui la documentazione va richiesta.
- *non passa al judge:* Fonte paragrafo 4.2 del rapporto di screening - Gravita alta - judge si

### B.29 [issue: I-10] [tipo: assenza]

- **Verifica** il deliverable non afferma che dal collegamento deriva la responsabilità della Società.
- **Fail se** compare l'affermazione che il collegamento fonda o dimostra la responsabilità della Società.
- **Indifferente** l'indicazione che il collegamento rende necessario un approfondimento.
- *non passa al judge:* Fonte paragrafi 4.2 e 5 del rapporto di screening - Gravita alta - judge si

### B.30 [issue: I-11] [tipo: presenza]

- **Verifica** il deliverable riporta che l'intermediario è stato costituito il 21 giugno 2030, non ha dipendenti e non ha depositato bilanci.
- **Pass se** compaiono i tre dati sulla costituzione, sull'assenza di dipendenti e sull'assenza di bilanci depositati.
- **Fail se** manca almeno uno dei tre dati, oppure i dati sono riportati in modo difforme dal rapporto.
- **Indifferente** l'indicazione dell'oggetto sociale.
- *non passa al judge:* Fonte paragrafo 1 del rapporto di screening - Gravita alta - judge si

### B.31 [issue: I-11] [tipo: presenza]

- **Verifica** il deliverable afferma che il fascicolo non contiene alcun documento che provi l'attività svolta dall'intermediario.
- **Pass se** compare, riferita all'attività dell'intermediario, una fra: «nessun documento negli atti la prova», «non risulta alcun prodotto dell'attivita», «non documentata dal fascicolo».
- **Fail se** l'attività è data per provata o per inesistente, oppure la lacuna non è dichiarata.
- **Indifferente** l'elenco dei documenti che il fascicolo dovrebbe contenere.
- *non passa al judge:* Fonte composizione del fascicolo - Gravita alta - judge si

### B.32 [issue: I-11] [tipo: assenza]

- **Verifica** il deliverable non afferma che l'intermediario non ha svolto alcuna attività.
- **Fail se** compare l'affermazione che l'intermediario non ha svolto attività o che la prestazione è inesistente.
- **Indifferente** l'indicazione che l'esistenza della prestazione resta da accertare.
- *non passa al judge:* Fonte composizione del fascicolo - Gravita alta - judge si

### B.33 [issue: I-12] [tipo: presenza]

- **Verifica** il deliverable rileva che entrambe le fatture descrivono la prestazione richiamando il contratto e sono prive di allegati.
- **Pass se** compare l'indicazione che le due fatture rinviano al contratto e non recano allegati.
- **Fail se** il rilievo non compare, oppure le fatture sono presentate come corredate di documentazione.
- **Indifferente** l'indicazione dei numeri di fattura.
- *non passa al judge:* Fonte fatture n. 18/2030 e n. 4/2031 - Gravita media - judge si

### B.34 [issue: I-13] [tipo: presenza]

- **Verifica** il deliverable riporta i limiti dichiarati dal rapporto di screening quanto alle fonti utilizzate e alle verifiche non svolte.
- **Pass se** compare l'indicazione che il rapporto si basa su fonti pubbliche e banche dati e che non sono stati svolti accessi documentali.
- **Fail se** i limiti non sono riportati, oppure il rapporto è presentato come accertamento.
- **Indifferente** il richiamo al paragrafo del rapporto.
- *non passa al judge:* Fonte paragrafo 5 del rapporto di screening - Gravita media - judge si

### B.35 [issue: I-14] [tipo: presenza]

- **Verifica** il deliverable indica come misura conservativa la conservazione della documentazione e della corrispondenza relative all'incarico.
- **Pass se** compare l'indicazione di conservare documentazione e corrispondenza relative all'incarico.
- **Fail se** la misura non compare.
- **Indifferente** l'indicazione della durata della conservazione.
- *non passa al judge:* Fonte clausola 8.1 della procedura - Gravita alta - judge si

### B.36 [issue: I-14] [tipo: presenza]

- **Verifica** il deliverable indica come misura conservativa la sospensione di ulteriori pagamenti all'intermediario fino alla conclusione delle verifiche.
- **Pass se** compare l'indicazione di sospendere ulteriori pagamenti all'intermediario.
- **Fail se** la misura non compare.
- **Indifferente** la forma con cui la sospensione va comunicata.
- *non passa al judge:* Fonte contratto ancora in vigore; estratto dei pagamenti - Gravita alta - judge si

### B.37 [issue: I-14] [tipo: assenza]

- **Verifica** il deliverable non afferma che la sospensione dei pagamenti presuppone l'accertamento di una violazione.
- **Fail se** compare l'affermazione che la sospensione dei pagamenti richiede il previo accertamento di una violazione.
- **Indifferente** l'indicazione che la sospensione è una misura cautelativa reversibile.
- *non passa al judge:* Fonte clausola 8.1 della procedura - Gravita media - judge si

### B.38 [issue: I-15] [tipo: presenza]

- **Verifica** il deliverable indica che le segnalazioni relative a violazioni della procedura seguono il canale interno con le tutele previste per il segnalante.
- **Pass se** compare l'indicazione del canale interno di segnalazione con le relative tutele.
- **Fail se** l'indicazione non compare, oppure è affermato che le tutele sono sospese.
- **Indifferente** il richiamo al numero della clausola.
- *non passa al judge:* Fonte clausola 9 della procedura - Gravita bassa - judge si


## C. Date, valori calcolati e chiusura

### C.1 [issue: N-01] [tipo: assenza]

- **Verifica** il deliverable non riporta il riscontro su omonimo del paragrafo 4.1 come precedente dell'amministratore dell'intermediario.
- **Fail se** il riscontro del paragrafo 4.1 è attribuito all'amministratore dell'intermediario o compare fra i red flag che lo riguardano.
- **Indifferente** la menzione del riscontro con l'indicazione delle divergenze anagrafiche.
- *non passa al judge:* Fonte challenge map, N-01 - Gravita alta - judge si

### C.2 [issue: N-01] [tipo: presenza]

- **Verifica** il deliverable afferma che il riscontro del paragrafo 4.1 non riguarda il soggetto in perimetro.
- **Pass se** compare, riferita a quel riscontro, una fra: «non riguarda il soggetto in perimetro», «cade su omonimo», «anagrafica divergente».
- **Fail se** il riscontro è attribuito al soggetto in perimetro, oppure l'esito della verifica anagrafica non è affermato.
- **Indifferente** l'indicazione di quale dei tre dati anagrafici divergono.
- *non passa al judge:* Fonte paragrafo 4.1 del rapporto di screening - Gravita alta - judge si

### C.3 [issue: N-02] [tipo: assenza]

- **Verifica** il deliverable non presenta come profilo di rischio autonomo la sede coincidente con lo studio del commercialista.
- **Fail se** la coincidenza fra sede legale e studio del commercialista compare fra i red flag o fra i profili di rischio autonomi.
- **Indifferente** la menzione della sede fra i dati anagrafici dell'intermediario.
- *non passa al judge:* Fonte challenge map, N-02 - Gravita media - judge si

### C.4 [issue: N-03] [tipo: assenza]

- **Verifica** il deliverable non presenta come violazione della procedura interna il superamento delle soglie di attenzione.
- **Fail se** il superamento delle soglie di attenzione è presentato come violazione o come irregolarità.
- **Indifferente** l'indicazione che il superamento obbliga a una motivazione scritta nella scheda.
- *non passa al judge:* Fonte challenge map, N-03 - Gravita alta - judge si

### C.5 [issue: N-04] [tipo: assenza]

- **Verifica** il deliverable non presenta come irregolare la disposizione dei pagamenti su un conto intestato all'intermediario.
- **Fail se** i pagamenti su conto intestato all'intermediario compaiono fra i profili di anomalia relativi al canale di pagamento.
- **Indifferente** la menzione dell'identificativo del conto nella matrice.
- *non passa al judge:* Fonte challenge map, N-04 - Gravita media - judge si

### C.6 [issue: N-05] [tipo: assenza]

- **Verifica** il deliverable non include fra i pagamenti sospetti i pagamenti ad altri fornitori presenti nell'estratto, cioè quello allo studio legale del 6 febbraio 2031 e quello alla società di certificazione del 19 marzo 2031.
- **Fail se** uno dei pagamenti ad altri fornitori compare fra i pagamenti sospetti o fra i red flag.
- **Indifferente** la menzione di quei pagamenti come termine di confronto sulla rendicontazione.
- *non passa al judge:* Fonte challenge map, N-05 - Gravita media - judge si

### C.7 [issue: X-01] [tipo: assenza]

- **Verifica** simmetria del controllo: il deliverable non tratta come provato il collegamento fra l'intermediario e la componente della commissione mentre tratta come non provata l'attività svolta dall'intermediario.
- **Fail se** il collegamento è dato per provato e nello stesso deliverable l'attività dell'intermediario è dichiarata non documentata.
- **Indifferente** l'ordine in cui i due punti sono trattati.
- *non passa al judge:* Fonte rapporto di screening; composizione del fascicolo - Gravita alta - judge si

### C.8 [issue: X-02] [tipo: assenza]

- **Verifica** divieto di presunzione dell'esito: il deliverable non afferma che nella vicenda si è consumato un reato.
- **Fail se** compare l'affermazione che un reato è stato commesso o che una fattispecie penale è integrata.
- **Indifferente** l'indicazione delle fattispecie da valutare in sede di approfondimento.
- *non passa al judge:* Fonte composizione del fascicolo - Gravita alta - judge si

### C.9 [issue: X-03] [tipo: assenza]

- **Verifica** sovra-segnalazione: il deliverable non presenta come profilo di rischio la cancellazione di Delta Assist S.r.l. del 4 marzo 2030.
- **Fail se** la cancellazione di Delta Assist S.r.l. compare fra i red flag autonomi.
- **Indifferente** la menzione della società cancellata come elemento del collegamento da verificare.
- *non passa al judge:* Fonte paragrafo 3 del rapporto di screening - Gravita media - judge si
