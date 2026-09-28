# WF2-095 - Criteri atomizzati

Identificativi e conteggio coincidono con `rubric.json` e `runtime_routing.json`:
i tre file sono emessi da un'unica fonte autoriale.

Il judge riceve il deliverable e il testo del criterio, nient'altro. La riga
`metadati non forniti al judge` e tutto ciò che segue sono metadati di build.

La decisione è binaria: il criterio passa se è soddisfatta almeno una condizione
`Pass se` o se ricorre esattamente il caso dichiarato `Indifferente`; fallisce se
ricorre `Fail se` oppure se il requisito verificato è solo parzialmente soddisfatto.


## Sezione A - forma dell'output (interamente verifica meccanica)

**A.1 file consegnato**  [issue: -] [tipo: struttura]

Verifica   La consegna contiene il file con il nome richiesto.
Pass se    è presente lease_enforcement_timeline.md
Fail se    il file manca oppure il nome diverge.

*metadati non forniti al judge* - fonte: public/response_template.md; gravita: media; instradamento: verifica meccanica

**A.2 sezioni della timeline**  [issue: -] [tipo: struttura]

Verifica   Il deliverable contiene le sezioni indicate, nell'ordine indicato.
Pass se    le intestazioni compaiono tutte e nella sequenza del response_template
Fail se    manca un'intestazione oppure l'ordine differisce.
Indifferente  la formulazione delle intestazioni oltre le prime ventidue battute.

*metadati non forniti al judge* - fonte: public/response_template.md; gravita: media; instradamento: verifica meccanica

**A.3 data di riferimento**  [issue: -] [tipo: valore]

Verifica   Il deliverable assume come data di riferimento il 6 agosto 2026.
Pass se    compare «6 agosto 2026» come data alla quale la ricostruzione è riferita
Fail se    è assunta una data diversa, oppure la data di riferimento non compare.
Indifferente  il formato della data.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: alta; instradamento: verifica meccanica

**A.4 quattro stati degli eventi**  [issue: -] [tipo: struttura]

Verifica   La cronologia distingue eventi avvenuti, termini calcolati, passaggi futuri condizionati e date non determinabili.
Pass se    ciascuna riga della cronologia porta uno dei quattro stati
Fail se    una o più righe non portano alcuno stato, oppure gli stati usati sono meno di quattro.
Indifferente  le etichette usate per i quattro stati.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: alta; instradamento: verifica meccanica

**A.5 documento indicato per ogni evento**  [issue: -] [tipo: struttura]

Verifica   Ogni evento della cronologia indica il documento del fascicolo da cui risulta.
Pass se    ciascuna riga riporta il nome di un allegato
Fail se    una o più righe non riportano alcun allegato.
Indifferente  la forma del riferimento al documento.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: alta; instradamento: verifica meccanica

**A.6 riferimenti entro l'elenco chiuso**  [issue: -] [tipo: assenza]

Verifica   Il deliverable non cita norme assenti dal reference pack.
Pass se    Il deliverable non cita norme assenti dal reference pack.
Fail se    compare un riferimento a un atto o a un articolo che non figura in public/02_reference_pack.md.
Indifferente  la scelta di non citare alcuna fonte in una singola riga.

*metadati non forniti al judge* - fonte: public/02_reference_pack.md e private/fonti_chiuse.json; gravita: alta; instradamento: verifica meccanica

**A.7 limite di parole**  [issue: -] [tipo: struttura]

Verifica   Il deliverable resta entro il limite di parole.
Pass se    il conteggio delle parole non supera 1900
Fail se    il conteggio supera il limite.

*metadati non forniti al judge* - fonte: public/response_template.md; gravita: bassa; instradamento: verifica meccanica


## Sezione B - merito

Stato del fascicolo alla data di riferimento: intimazione notificata; udienza di convalida fissata per il 20 agosto 2026 e non ancora tenuta; nessuna comparsa di costituzione depositata dalla conduttrice

**B.1 computo dei giorni liberi**  [issue: I-01] [tipo: presenza]

Verifica   Il deliverable afferma che dal computo dei venti giorni si escludono sia il giorno della notificazione sia il giorno dell'udienza.
Pass se    compare l'affermazione che si tratta di giorni liberi e che entrambi i giorni estremi sono esclusi
Fail se    il computo include uno dei due giorni estremi, oppure la natura di giorni liberi non è affermata.
Indifferente  il richiamo alla facoltà di abbreviazione con decreto motivato.

*metadati non forniti al judge* - fonte: art. 660, comma 4, del codice di procedura civile; gravita: alta; instradamento: judge

**B.2 esito del computo**  [issue: I-01] [tipo: presenza]

Verifica   Il deliverable afferma che il termine di comparizione è rispettato.
Pass se    compare l'affermazione che il termine di comparizione è rispettato
Fail se    è affermato che il termine non è rispettato, oppure l'esito non compare.
Indifferente  l'osservazione che il termine coincide con il minimo di legge.

*metadati non forniti al judge* - fonte: 04_relazione_di_notificazione.md; 03_intimazione_sfratto.md; gravita: alta; instradamento: judge

**B.3 sospensione feriale inapplicabile**  [issue: I-02] [tipo: presenza]

Verifica   Il deliverable afferma che la sospensione feriale non si applica ai procedimenti di sfratto.
Pass se    compare l'affermazione che la sospensione feriale non si applica alle cause di sfratto
Fail se    è affermato che la sospensione si applica, oppure il punto non è trattato.
Indifferente  il richiamo all'elenco delle materie trattate nel periodo feriale.

*metadati non forniti al judge* - fonte: art. 3 della legge sulla sospensione dei termini; art. 92 dell'ordinamento giudiziario; gravita: alta; instradamento: judge

**B.4 risposta sulla validità dell'udienza**  [issue: I-02] [tipo: presenza]

Verifica   Il deliverable afferma che l'udienza del 20 agosto 2026 è validamente fissata.
Pass se    compare l'affermazione che l'udienza è validamente fissata
Fail se    è affermato che l'udienza non è valida o che va rifissata.
Indifferente  il tono con cui la posizione del commercialista è smentita.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: alta; instradamento: judge

**B.5 natura pattizia delle soglie**  [issue: I-03] [tipo: qualificazione]

Verifica   Il deliverable qualifica come pattuizioni delle parti la soglia dei venti giorni e quella delle due mensilità richiamate dall'articolo 6 del contratto.
Pass se    compare, riferita a quelle soglie, una fra: «pattuizione delle parti»; «soglia convenzionale»; «clausola contrattuale e non regola di legge»
Fail se    le soglie sono presentate come regole di legge applicabili alla locazione ad uso diverso.
Indifferente  il richiamo alla collocazione della disposizione fra quelle relative alle locazioni abitative.

*metadati non forniti al judge* - fonte: 01_contratto_locazione.md, art. 6; gravita: alta; instradamento: judge

**B.6 criterio di valutazione della gravità**  [issue: I-04] [tipo: presenza]

Verifica   Il deliverable afferma che la gravità dell'inadempimento va valutata secondo la disciplina generale della risoluzione.
Pass se    compare l'affermazione che la gravità si valuta secondo la disciplina generale, avuto riguardo all'interesse del locatore
Fail se    la risoluzione è fatta derivare dal solo decorso della soglia contrattuale.
Indifferente  il richiamo alla soglia contrattuale come elemento della valutazione.

*metadati non forniti al judge* - fonte: art. 1455 del codice civile; gravita: alta; instradamento: judge

**B.7 clausola di esclusione del termine - individuazione**  [issue: I-05] [tipo: presenza]

Verifica   Il deliverable individua la clausola 6.3 del contratto come pattuizione che esclude la concessione di un termine per il pagamento.
Pass se    compare l'indicazione della clausola 6.3 come clausola che esclude il termine per il pagamento
Fail se    la clausola non è individuata.
Indifferente  il richiamo al suo tenore letterale.

*metadati non forniti al judge* - fonte: 01_contratto_locazione.md, art. 6.3; gravita: alta; instradamento: judge

**B.8 clausola di esclusione del termine - inutilizzabilità**  [issue: I-05] [tipo: presenza]

Verifica   Il deliverable afferma che la locatrice non può fondarsi sulla clausola 6.3 perché il canone annuo pattuito è inferiore alla soglia oltre la quale le parti possono derogare alle disposizioni di legge.
Pass se    compare l'affermazione che la clausola non è utilizzabile per il mancato superamento della soglia di derogabilità
Fail se    la clausola è presentata come utilizzabile, oppure la verifica della soglia non compare.
Indifferente  l'indicazione dell'importo della soglia.

*metadati non forniti al judge* - fonte: 01_contratto_locazione.md, artt. 4.1 e 6.3; art. 79 della legge sulle locazioni; gravita: alta; instradamento: judge

**B.9 clausola di esclusione del termine - divieto di errore di lato**  [issue: I-05] [tipo: assenza]

Verifica   Il deliverable non presenta la clausola 6.3 come esposizione della locatrice.
Pass se    Il deliverable non presenta la clausola 6.3 come esposizione della locatrice.
Fail se    la clausola 6.3 è indicata fra i rischi o fra le esposizioni del lato assistito.
Indifferente  l'osservazione che la clausola è stata scritta a favore della locatrice.

*metadati non forniti al judge* - fonte: 01_contratto_locazione.md, art. 6.3; gravita: media; instradamento: judge

**B.10 attestazione della persistenza della morosità**  [issue: I-06] [tipo: presenza]

Verifica   Il deliverable indica fra gli adempimenti per l'udienza l'attestazione in giudizio che la morosità persiste.
Pass se    fra gli adempimenti per l'udienza compare l'attestazione della persistenza della morosità
Fail se    l'attestazione non è indicata, oppure la convalida è presentata come conseguenza automatica della mancata opposizione.
Indifferente  il richiamo alla facoltà del giudice di ordinare la prestazione di cauzione.

*metadati non forniti al judge* - fonte: art. 663, comma 2, del codice di procedura civile; gravita: alta; instradamento: judge

**B.11 omissione dell'avviso sul patrocinio**  [issue: I-07] [tipo: presenza]

Verifica   Il deliverable afferma che la citazione non contiene l'avviso relativo all'istanza per l'ammissione al patrocinio a spese dello Stato.
Pass se    compare l'affermazione che l'avviso sul patrocinio a spese dello Stato non è contenuto nell'atto
Fail se    l'omissione non è rilevata, oppure è affermato che l'avviso è presente.
Indifferente  l'osservazione che l'avvertimento sulla convalida è invece presente.

*metadati non forniti al judge* - fonte: 03_intimazione_sfratto.md, punto 15; art. 660, comma 3, del codice di procedura civile; gravita: alta; instradamento: judge

**B.12 omissione dell'avviso - divieto di conclusione eccedente**  [issue: I-07] [tipo: assenza]

Verifica   Il deliverable non afferma che l'atto è nullo per effetto dell'omissione.
Pass se    Il deliverable non afferma che l'atto è nullo per effetto dell'omissione.
Fail se    è affermato che l'atto di intimazione è nullo o inefficace per la mancanza dell'avviso sul patrocinio.
Indifferente  l'indicazione che la conseguenza dell'omissione si atteggia diversamente secondo che l'intimato compaia o no.

*metadati non forniti al judge* - fonte: art. 660 del codice di procedura civile; gravita: alta; instradamento: judge

**B.13 notificazione non in mani proprie**  [issue: I-08] [tipo: presenza]

Verifica   Il deliverable afferma che l'atto non è stato notificato in mani proprie e che in tal caso l'ufficiale giudiziario deve spedire avviso a mezzo di lettera raccomandata allegando la ricevuta all'originale.
Pass se    compare l'affermazione che la notificazione non è avvenuta in mani proprie e l'indicazione dell'adempimento ulteriore
Fail se    la notificazione è presentata come regolare senza rilevare l'adempimento ulteriore.
Indifferente  l'indicazione della qualifica del soggetto che ha ricevuto l'atto.

*metadati non forniti al judge* - fonte: 04_relazione_di_notificazione.md; art. 660 del codice di procedura civile; gravita: media; instradamento: judge

**B.14 assenza della ricevuta di spedizione**  [issue: I-08] [tipo: presenza]

Verifica   Il deliverable afferma che la ricevuta di spedizione dell'avviso non risulta allegata all'originale.
Pass se    compare l'affermazione che la ricevuta di spedizione non risulta agli atti
Fail se    è affermato che la ricevuta è presente, oppure la lacuna non è dichiarata.
Indifferente  la richiesta di acquisirla dall'ufficio notifiche.

*metadati non forniti al judge* - fonte: 04_relazione_di_notificazione.md, annotazione di studio; gravita: media; instradamento: judge

**B.15 contestazione parziale della conduttrice**  [issue: I-09] [tipo: presenza]

Verifica   Il deliverable afferma che la conduttrice non contesta i canoni e contesta una quota degli oneri accessori.
Pass se    compare l'affermazione che la contestazione riguarda una quota degli oneri accessori e non i canoni
Fail se    la contestazione è presentata come integrale, oppure il contenuto della contestazione non è esaminato.
Indifferente  il richiamo alla ragione addotta dalla conduttrice.

*metadati non forniti al judge* - fonte: 06_email_conduttrice.md; gravita: alta; instradamento: judge

**B.16 somma non controversa e termine**  [issue: I-09] [tipo: presenza]

Verifica   Il deliverable afferma che, se la conduttrice comparendo nega la morosità contestandone l'ammontare, il giudice può disporre il pagamento della somma non controversa con un termine non superiore a venti giorni.
Pass se    compare l'affermazione del possibile ordine di pagamento della somma non controversa con il termine massimo di venti giorni
Fail se    il passaggio non è indicato, oppure è indicato un termine diverso.
Indifferente  il richiamo alla convalida e al decreto ingiuntivo in caso di inottemperanza.

*metadati non forniti al judge* - fonte: art. 666 del codice di procedura civile; gravita: alta; instradamento: judge

**B.17 ordinanza provvisoria di rilascio**  [issue: I-10] [tipo: presenza]

Verifica   Il deliverable indica fra i passaggi possibili l'ordinanza di rilascio con riserva delle eccezioni.
Pass se    compare l'indicazione dell'ordinanza di rilascio con riserva delle eccezioni fra i passaggi possibili
Fail se    il passaggio non è indicato.
Indifferente  il richiamo alla subordinazione a cauzione.

*metadati non forniti al judge* - fonte: art. 665 del codice di procedura civile; gravita: alta; instradamento: judge

**B.18 necessità dell'istanza del locatore**  [issue: I-10] [tipo: presenza]

Verifica   Il deliverable afferma che l'ordinanza di rilascio è pronunciata su istanza del locatore.
Pass se    compare l'affermazione che l'ordinanza richiede l'istanza del locatore
Fail se    l'ordinanza è presentata come adottata d'ufficio.
Indifferente  il richiamo al presupposto delle eccezioni non fondate su prova scritta.

*metadati non forniti al judge* - fonte: art. 665 del codice di procedura civile; gravita: alta; instradamento: judge

**B.19 perimetro del decreto d'ingiunzione**  [issue: I-11] [tipo: presenza]

Verifica   Il deliverable afferma che il decreto d'ingiunzione comprende i canoni scaduti e da scadere fino all'esecuzione dello sfratto e le spese dell'intimazione.
Pass se    compare l'affermazione che l'ingiunzione comprende anche i canoni da scadere fino all'esecuzione dello sfratto
Fail se    l'ingiunzione è limitata ai canoni già scaduti alla data dell'atto.
Indifferente  il richiamo all'immediata esecutività del decreto.

*metadati non forniti al judge* - fonte: art. 664 del codice di procedura civile; gravita: media; instradamento: judge

**B.20 termine di grazia - questione controversa**  [issue: I-12] [tipo: presenza]

Verifica   Il deliverable afferma che l'applicabilità della sanatoria giudiziale alle locazioni ad uso diverso non è risolta dal testo di legge.
Pass se    compare l'affermazione che la questione è controversa o non risolta dal testo
Fail se    è affermato senza riserve che il termine di grazia è concedibile, oppure che non lo è.
Indifferente  l'esposizione degli argomenti nei due sensi.

*metadati non forniti al judge* - fonte: art. 55 della legge sulle locazioni; 06_email_conduttrice.md; gravita: alta; instradamento: judge

**B.21 termine di grazia - richiesta di istruzioni**  [issue: I-12] [tipo: presenza]

Verifica   Il deliverable chiede istruzioni al committente sulla posizione da assumere in udienza sulla richiesta di termine.
Pass se    fra le decisioni rimesse al committente compare la posizione da assumere sulla richiesta di termine
Fail se    la questione è rilevata senza rimettere alcuna decisione al committente.
Indifferente  il numero delle alternative prospettate.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: alta; instradamento: judge

**B.22 termine di grazia - misura massima**  [issue: I-12] [tipo: valore]

Verifica   Il deliverable indica in novanta giorni il termine massimo assegnabile.
Pass se    compare il termine di «novanta giorni» riferito alla misura massima del termine assegnabile
Fail se    è indicata una misura diversa, oppure la misura non compare.
Indifferente  il richiamo al rinvio dell'udienza a non oltre dieci giorni dalla scadenza.

*metadati non forniti al judge* - fonte: art. 55, comma 2, della legge sulle locazioni; gravita: media; instradamento: verifica meccanica

**B.23 sovra-segnalazione - mediazione**  [issue: N-01] [tipo: assenza]

Verifica   Il deliverable non indica l'esperimento della mediazione fra gli adempimenti mancanti.
Pass se    Il deliverable non indica l'esperimento della mediazione fra gli adempimenti mancanti.
Fail se    la mancata mediazione è indicata come vizio dell'iniziativa o come adempimento da compiere prima dell'udienza.
Indifferente  l'osservazione che la mediazione diventa condizione di procedibilità dopo il mutamento del rito.

*metadati non forniti al judge* - fonte: art. 5, comma 6, lettera b), del decreto legislativo sulla mediazione; gravita: alta; instradamento: judge

**B.24 sovra-segnalazione - soglia delle due mensilità**  [issue: N-02] [tipo: assenza]

Verifica   Il deliverable non indica il mancato pagamento degli oneri accessori come motivo autonomo di risoluzione.
Pass se    Il deliverable non indica il mancato pagamento degli oneri accessori come motivo autonomo di risoluzione.
Fail se    è affermato che la soglia delle due mensilità è superata, o che il mancato pagamento degli oneri accessori costituisce motivo autonomo di risoluzione da azionare.
Indifferente  il confronto fra l'importo degli oneri non pagati e quello di due mensilità.

*metadati non forniti al judge* - fonte: 01_contratto_locazione.md, art. 6.2; 05_estratto_partitario.csv; gravita: alta; instradamento: judge

**B.25 sovra-segnalazione - registrazione del contratto**  [issue: N-03] [tipo: assenza]

Verifica   Il deliverable non indica la registrazione del contratto di locazione fra i documenti da acquisire.
Pass se    Il deliverable non indica la registrazione del contratto di locazione fra i documenti da acquisire.
Fail se    la registrazione del contratto è indicata fra gli adempimenti mancanti o fra i documenti da acquisire.
Indifferente  la menzione degli estremi di registrazione fra gli elementi verificati.

*metadati non forniti al judge* - fonte: 01_contratto_locazione.md, estremi di registrazione; gravita: media; instradamento: judge

**B.26 simmetria del controllo - posizione della conduttrice**  [issue: -] [tipo: assenza]

Verifica   Il deliverable non presenta la difficoltà economica dichiarata dalla conduttrice come fatto accertato.
Pass se    Il deliverable non presenta la difficoltà economica dichiarata dalla conduttrice come fatto accertato.
Fail se    la chiusura del tratto di strada e la riduzione degli incassi sono riportate come fatti accertati anziché come dichiarazioni della conduttrice.
Indifferente  la menzione della dichiarazione come elemento che il giudice potrà valutare.

*metadati non forniti al judge* - fonte: 06_email_conduttrice.md; gravita: media; instradamento: judge

**B.27 presunzione dell'esito - condotta della conduttrice**  [issue: -] [tipo: assenza]

Verifica   Il deliverable non presenta come avvenuta la comparizione della conduttrice né la sua opposizione.
Pass se    Il deliverable non presenta come avvenuta la comparizione della conduttrice né la sua opposizione.
Fail se    è affermato che la conduttrice comparirà, che si opporrà o che pagherà, anziché prospettare i passaggi come condizionati.
Indifferente  l'indicazione che la conduttrice ha annunciato di dare mandato a un legale.

*metadati non forniti al judge* - fonte: 06_email_conduttrice.md; gravita: alta; instradamento: judge


## Sezione C - date e valori calcolati

**C.1 data della notificazione**  [issue: I-01] [tipo: valore]

Verifica   Il deliverable indica il 30 luglio 2026 come data della notificazione dell'intimazione.
Pass se    compare la data «30 luglio 2026» riferita alla notificazione
Fail se    è indicata una data diversa, oppure la data non compare.
Indifferente  l'indicazione dell'ora della consegna.

*metadati non forniti al judge* - fonte: 04_relazione_di_notificazione.md; gravita: alta; instradamento: verifica meccanica

**C.2 numero dei giorni liberi**  [issue: I-01] [tipo: valore]

Verifica   Il deliverable indica in venti il numero dei giorni liberi fra notificazione e udienza.
Pass se    compare il numero «venti giorni liberi» riferito all'intervallo fra notificazione e udienza
Fail se    è indicato un numero diverso, oppure il numero non compare.
Indifferente  l'indicazione dell'intervallo di date corrispondente.

*metadati non forniti al judge* - fonte: art. 660, comma 4, del codice di procedura civile; gravita: alta; instradamento: verifica meccanica

**C.3 derivazione errata con sospensione feriale**  [issue: I-02] [tipo: assenza]

Verifica   Il deliverable non indica come prima udienza utile una data ottenuta applicando la sospensione feriale.
Pass se    Il deliverable non indica come prima udienza utile una data ottenuta applicando la sospensione feriale.
Fail se    compare la data «21 settembre 2026» come udienza, oppure il termine di comparizione è computato dal 1 settembre 2026.
Indifferente  la menzione del periodo di sospensione feriale per spiegare perché non si applica.

*metadati non forniti al judge* - fonte: derivazione da escludere; gravita: alta; instradamento: judge

**C.4 importo intimato**  [issue: I-11] [tipo: valore]

Verifica   Il deliverable indica in 13.086,00 euro l'importo intimato.
Pass se    compare l'importo «13.086,00» riferito alla morosità intimata
Fail se    è indicato un importo diverso, oppure l'importo non compare.
Indifferente  la scomposizione fra canoni e oneri accessori.

*metadati non forniti al judge* - fonte: 03_intimazione_sfratto.md, punto 12; gravita: alta; instradamento: verifica meccanica

**C.5 derivazione errata sull'importo**  [issue: I-11] [tipo: assenza]

Verifica   Il deliverable non indica come morosità intimata il totale delle partite aperte del partitario.
Pass se    Il deliverable non indica come morosità intimata il totale delle partite aperte del partitario.
Fail se    il totale delle partite aperte del partitario è presentato come importo intimato, oppure il canone di agosto 2026 è computato nell'importo dell'atto.
Indifferente  la menzione delle partite aperte per illustrare l'aggravarsi della morosità dopo l'atto.

*metadati non forniti al judge* - fonte: 05_estratto_partitario.csv; gravita: alta; instradamento: judge

**C.6 somma non controversa**  [issue: I-09] [tipo: valore]

Verifica   Il deliverable indica in 12.872,00 euro la somma non controversa.
Pass se    compare l'importo «12.872,00» riferito alla somma non controversa
Fail se    è indicato un importo diverso, oppure la somma non controversa non è quantificata.
Indifferente  l'esposizione del calcolo in due addendi.

*metadati non forniti al judge* - fonte: 06_email_conduttrice.md e 05_estratto_partitario.csv; gravita: alta; instradamento: verifica meccanica
