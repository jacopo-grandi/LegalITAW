# WF2-093 - Criteri atomizzati

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
Pass se    è presente patent_timeline.md
Fail se    il file manca oppure il nome diverge.

*metadati non forniti al judge* - fonte: public/response_template.md; gravita: media; instradamento: verifica meccanica

**A.2 sezioni della timeline**  [issue: -] [tipo: struttura]

Verifica   Il deliverable contiene le sezioni indicate, nell'ordine indicato.
Pass se    le intestazioni compaiono tutte e nella sequenza del response_template
Fail se    manca un'intestazione oppure l'ordine differisce.
Indifferente  la formulazione delle intestazioni oltre le prime ventidue battute.

*metadati non forniti al judge* - fonte: public/response_template.md; gravita: media; instradamento: verifica meccanica

**A.3 data di riferimento**  [issue: -] [tipo: valore]

Verifica   Il deliverable assume come data di riferimento il 10 novembre 2026.
Pass se    compare «10 novembre 2026» come data alla quale la ricostruzione è riferita
Fail se    è assunta una data diversa, oppure la data di riferimento non compare.
Indifferente  il formato della data.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: alta; instradamento: verifica meccanica

**A.4 quattro stati degli eventi**  [issue: -] [tipo: struttura]

Verifica   La cronologia distingue eventi avvenuti, scadenze calcolate, passaggi futuri condizionati e date non determinabili.
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

**A.6 evento di decorrenza indicato per ogni termine**  [issue: -] [tipo: struttura]

Verifica   Ogni termine calcolato indica l'evento da cui decorre.
Pass se    ciascun termine riporta l'evento di decorrenza
Fail se    uno o più termini non indicano l'evento di decorrenza.
Indifferente  la forma dell'indicazione.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: alta; instradamento: verifica meccanica

**A.7 calcolo esposto per ogni termine**  [issue: -] [tipo: struttura]

Verifica   Ogni termine calcolato riporta il calcolo seguito.
Pass se    ciascun termine riporta il passaggio aritmetico o la regola di computo applicata
Fail se    uno o più termini riportano il solo risultato.
Indifferente  il livello di dettaglio del calcolo.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: alta; instradamento: verifica meccanica

**A.8 riferimenti entro l'elenco chiuso**  [issue: -] [tipo: assenza]

Verifica   Il deliverable non cita norme o disposizioni assenti dal reference pack.
Pass se    Il deliverable non cita norme o disposizioni assenti dal reference pack.
Fail se    compare un riferimento a un atto, a un articolo, a una regola o a una disposizione che non figura in public/02_reference_pack.md.
Indifferente  la scelta di non citare alcuna fonte in una singola riga.

*metadati non forniti al judge* - fonte: public/02_reference_pack.md e private/fonti_chiuse.json; gravita: alta; instradamento: verifica meccanica

**A.9 limite di parole**  [issue: -] [tipo: struttura]

Verifica   Il deliverable resta entro il limite di parole.
Pass se    il conteggio delle parole non supera 3000
Fail se    il conteggio supera il limite.

*metadati non forniti al judge* - fonte: public/response_template.md; gravita: bassa; instradamento: verifica meccanica


## Sezione B - merito

Stato del fascicolo alla data di riferimento: brevetto concesso e convalidato in Italia; termine di opposizione scaduto e opposizione depositata da un terzo; nessuna azione promossa e nessun provvedimento cautelare richiesto

**B.1 decorrenza dalla pubblicazione della menzione**  [issue: I-01] [tipo: attribuzione]

Verifica   Il deliverable riconduce la decorrenza dei termini post-concessione alla pubblicazione della menzione della concessione nel Bollettino europeo.
Pass se    compare l'affermazione che i termini decorrono dalla pubblicazione della menzione della concessione
Fail se    la decorrenza è ricondotta alla data di deposito, alla pubblicazione della domanda o alla decisione di concessione.
Indifferente  il richiamo al numero del fascicolo del Bollettino.

*metadati non forniti al judge* - fonte: 01_estratto_bollettino_concessione.md; gravita: alta; instradamento: judge

**B.2 data del fascicolo come data della menzione**  [issue: I-01] [tipo: presenza]

Verifica   Il deliverable afferma che la data di pubblicazione della menzione è la data del fascicolo del Bollettino.
Pass se    compare l'affermazione che la data della menzione è quella del fascicolo
Fail se    è indicata come data della menzione una data diversa da quella del fascicolo.
Indifferente  l'osservazione che il record della sezione non riporta il codice della data di pubblicazione.

*metadati non forniti al judge* - fonte: 01_estratto_bollettino_concessione.md, nota d'archivio; gravita: media; instradamento: judge

**B.3 durata del termine di opposizione**  [issue: I-02] [tipo: presenza]

Verifica   Il deliverable afferma che il termine per proporre opposizione è di nove mesi.
Pass se    compare l'indicazione del termine di nove mesi per l'opposizione
Fail se    è indicata una durata diversa, oppure la durata non compare.
Indifferente  il richiamo alla regola di computo dei termini a mesi.

*metadati non forniti al judge* - fonte: art. 99(1) della Convenzione; gravita: alta; instradamento: judge

**B.4 tempestività dell'atto di opposizione**  [issue: I-03] [tipo: presenza]

Verifica   Il deliverable afferma che l'atto di opposizione è stato depositato entro il termine.
Pass se    compare l'affermazione che il deposito dell'atto è avvenuto entro la scadenza
Fail se    il deposito è indicato come tardivo, oppure la tempestività dell'atto non è esaminata.
Indifferente  il richiamo al timbro di ricezione.

*metadati non forniti al judge* - fonte: 05_atto_opposizione.md; gravita: media; instradamento: judge

**B.5 distinzione fra atto e tassa**  [issue: I-03] [tipo: presenza]

Verifica   Il deliverable esamina separatamente la data di deposito dell'atto e la data del pagamento della tassa.
Pass se    le due date sono esaminate come elementi distinti
Fail se    l'esame si arresta alla data di deposito dell'atto.
Indifferente  l'ordine in cui i due elementi sono trattati.

*metadati non forniti al judge* - fonte: 05_atto_opposizione.md; 06_estratto_conto_deposito_epo.md; gravita: alta; instradamento: judge

**B.6 data di valuta del pagamento**  [issue: I-04] [tipo: presenza]

Verifica   Il deliverable afferma che la data di valuta dell'addebito della tassa è successiva alla scadenza del termine di opposizione.
Pass se    compare l'affermazione che la data di valuta è posteriore alla scadenza
Fail se    è usata la data di registrazione dell'addebito, oppure il rapporto fra le due date non è esaminato.
Indifferente  il richiamo alla ragione dello scarto fra registrazione e valuta.

*metadati non forniti al judge* - fonte: 06_estratto_conto_deposito_epo.md; gravita: alta; instradamento: judge

**B.7 esito sull'opposizione**  [issue: I-04] [tipo: qualificazione]

Verifica   Il deliverable qualifica l'opposizione come non proposta.
Pass se    compare, riferita all'opposizione, una fra: «si considera non proposta»; «non si considera proposta»; «considerata non presentata»
Fail se    l'opposizione è qualificata come pendente, come ammissibile o come inammissibile.
Indifferente  il richiamo alla facoltà dell'Ufficio di trascurare importi minimi mancanti.

*metadati non forniti al judge* - fonte: art. 99(1) della Convenzione; Guidelines D-IV, 1.2.1; gravita: alta; instradamento: judge

**B.8 distinzione dall'inammissibilità**  [issue: I-04] [tipo: assenza]

Verifica   Il deliverable non qualifica l'esito come rigetto per inammissibilità.
Pass se    Il deliverable non qualifica l'esito come rigetto per inammissibilità.
Fail se    l'esito del mancato pagamento nel termine è presentato come inammissibilità dell'opposizione.
Indifferente  il richiamo all'inammissibilità in relazione a carenze diverse dal pagamento.

*metadati non forniti al judge* - fonte: Guidelines D-IV, 1.2.1; Regola 77 della Convenzione; gravita: alta; instradamento: judge

**B.9 iniziativa da assumere sull'opposizione**  [issue: I-04] [tipo: presenza]

Verifica   Il deliverable indica di far valere la circostanza presso l'Ufficio europeo dei brevetti.
Pass se    fra le azioni compare la segnalazione o l'istanza all'Ufficio sulla data di valuta del pagamento
Fail se    la circostanza è rilevata senza indicare alcuna iniziativa.
Indifferente  la forma dell'iniziativa proposta.

*metadati non forniti al judge* - fonte: 06_estratto_conto_deposito_epo.md; gravita: alta; instradamento: judge

**B.10 assenza di sospensione automatica**  [issue: I-05] [tipo: presenza]

Verifica   Il deliverable afferma che la pendenza dell'opposizione non sospende l'efficacia del brevetto.
Pass se    compare l'affermazione che l'opposizione non sospende l'efficacia del brevetto
Fail se    è affermato che il brevetto è inefficace o sospeso in pendenza dell'opposizione.
Indifferente  il richiamo all'effetto retroattivo dell'eventuale revoca.

*metadati non forniti al judge* - fonte: artt. 68 e 99(2) della Convenzione; gravita: alta; instradamento: judge

**B.11 azionabilità della tutela in Italia**  [issue: I-05] [tipo: presenza]

Verifica   Il deliverable afferma che la tutela in Italia può essere azionata nonostante la pendenza dell'opposizione.
Pass se    compare l'affermazione che l'azione in Italia può essere promossa
Fail se    è affermato che occorre attendere la definizione dell'opposizione.
Indifferente  il richiamo alla facoltà di intervento del presunto contraffattore nell'opposizione.

*metadati non forniti al judge* - fonte: artt. 99(2) e 105 della Convenzione; gravita: alta; instradamento: judge

**B.12 accelerazione del procedimento di opposizione**  [issue: I-05] [tipo: presenza]

Verifica   Il deliverable indica che l'Ufficio può accelerare il procedimento di opposizione se informato della pendenza di un'azione.
Pass se    compare l'indicazione della possibilità di accelerazione su informativa relativa all'azione nazionale
Fail se    la possibilità di accelerazione non è menzionata.
Indifferente  la scelta di proporre o non proporre l'informativa.

*metadati non forniti al judge* - fonte: Guidelines E-VIII, 5; gravita: media; instradamento: judge

**B.13 oggetto della traduzione richiesta**  [issue: I-06] [tipo: presenza]

Verifica   Il deliverable afferma che la convalida italiana richiede la traduzione dell'intero testo del brevetto concesso.
Pass se    compare l'affermazione che la traduzione riguarda l'intero testo del brevetto concesso
Fail se    è affermato che la convalida richiedeva la traduzione delle sole rivendicazioni.
Indifferente  il richiamo alla dichiarazione di conformità.

*metadati non forniti al judge* - fonte: art. 56, comma 3, del Codice della proprietà industriale; gravita: alta; instradamento: judge

**B.14 tempestività della traduzione**  [issue: I-06] [tipo: presenza]

Verifica   Il deliverable afferma che la traduzione è stata depositata entro il termine.
Pass se    compare l'affermazione che il deposito della traduzione è avvenuto entro il termine di tre mesi
Fail se    il deposito è indicato come tardivo, oppure la tempestività non è esaminata.
Indifferente  il richiamo al numero di deposito telematico.

*metadati non forniti al judge* - fonte: 03_deposito_traduzione_italiana.md; gravita: alta; instradamento: judge

**B.15 effetto in Italia del brevetto**  [issue: I-06] [tipo: qualificazione]

Verifica   Il deliverable qualifica il brevetto come avente effetto in Italia.
Pass se    compare, riferita al brevetto, una fra: «ha effetto in Italia»; «efficace in Italia»; «convalidato in Italia»
Fail se    è affermato che il brevetto è privo di effetto in Italia.
Indifferente  il richiamo alla conferma dell'ambito di protezione in pendenza di opposizione.

*metadati non forniti al judge* - fonte: art. 56 del Codice della proprietà industriale; gravita: alta; instradamento: judge

**B.16 difformità della rivendicazione 7**  [issue: I-07] [tipo: presenza]

Verifica   Il deliverable afferma che la rivendicazione 7 del testo concesso indica tre stimatori alternativi mentre la traduzione depositata indica il solo filtro di Kalman.
Pass se    compare l'affermazione della difformità fra le due formulazioni della rivendicazione 7
Fail se    la difformità non è rilevata, oppure è descritta come irrilevante.
Indifferente  l'indicazione dei nomi dei tre stimatori.

*metadati non forniti al judge* - fonte: 02_testo_di_concessione_rivendicazioni.md; 03_deposito_traduzione_italiana.md; gravita: alta; instradamento: judge

**B.17 qualificazione della difformità**  [issue: I-07] [tipo: qualificazione]

Verifica   Il deliverable qualifica la traduzione come conferente una protezione meno estesa.
Pass se    compare, riferita alla traduzione, una fra: «protezione meno estesa»; «portata più ristretta»; «ambito più limitato»
Fail se    la difformità è qualificata come errore materiale irrilevante, oppure la qualificazione non compare.
Indifferente  il richiamo alla dichiarazione di conformità sottoscritta.

*metadati non forniti al judge* - fonte: art. 57, comma 2, del Codice della proprietà industriale; gravita: alta; instradamento: judge

**B.18 testo che fa fede in Italia**  [issue: I-07] [tipo: presenza]

Verifica   Il deliverable afferma che, per la portata della protezione in Italia, fa fede la traduzione.
Pass se    compare l'affermazione che in Italia fa fede la traduzione perché conferisce una protezione meno estesa
Fail se    è affermato che fa fede in ogni caso il testo nella lingua del procedimento.
Indifferente  il richiamo al principio generale sull'autenticità del testo nella lingua di procedura.

*metadati non forniti al judge* - fonte: art. 57, commi 1 e 2, del Codice della proprietà industriale; gravita: alta; instradamento: judge

**B.19 eccezione del giudizio di nullità**  [issue: I-08] [tipo: presenza]

Verifica   Il deliverable afferma che la regola per cui fa fede la traduzione non si applica nel giudizio di nullità.
Pass se    compare l'affermazione che l'eccezione riguarda il giudizio di nullità
Fail se    l'eccezione non è menzionata.
Indifferente  il richiamo alla corrispondente disposizione della Convenzione.

*metadati non forniti al judge* - fonte: art. 57, comma 3, del Codice della proprietà industriale; gravita: media; instradamento: judge

**B.20 perimetro dell'effetto della restrizione**  [issue: I-08] [tipo: assenza]

Verifica   Il deliverable non presenta la restrizione come indebolimento della posizione del titolare anche in nullità.
Pass se    Il deliverable non presenta la restrizione come indebolimento della posizione del titolare anche in nullità.
Fail se    è affermato che la traduzione restrittiva riduce l'oggetto dell'accertamento di nullità o espone il brevetto a un'azione di nullità più ampia.
Indifferente  l'indicazione che la restrizione opera in contraffazione.

*metadati non forniti al judge* - fonte: art. 57, comma 3, del Codice della proprietà industriale; gravita: media; instradamento: judge

**B.21 deposito della traduzione rettificata**  [issue: I-09] [tipo: presenza]

Verifica   Il deliverable indica il deposito di una traduzione rettificata.
Pass se    fra le azioni compare il deposito della traduzione rettificata
Fail se    il deposito della traduzione rettificata non è indicato.
Indifferente  l'indicazione del momento del deposito.

*metadati non forniti al judge* - fonte: art. 57, comma 4, del Codice della proprietà industriale; gravita: alta; instradamento: judge

**B.22 condizione di efficacia della rettifica**  [issue: I-09] [tipo: presenza]

Verifica   Il deliverable afferma che la traduzione rettificata esplica effetti solo dopo essere stata resa accessibile al pubblico presso l'Ufficio italiano brevetti e marchi ovvero notificata al presunto contraffattore.
Pass se    compare l'affermazione che l'efficacia dipende dalla messa a disposizione del pubblico o dalla notificazione al presunto contraffattore
Fail se    è affermato che il solo deposito rende opponibile la rettifica, oppure la condizione di efficacia non compare.
Indifferente  la scelta fra le due modalità.

*metadati non forniti al judge* - fonte: art. 57, comma 4, del Codice della proprietà industriale; gravita: alta; instradamento: judge

**B.23 assenza di retroattività della rettifica**  [issue: I-09] [tipo: assenza]

Verifica   Il deliverable non attribuisce alla traduzione rettificata effetto retroattivo.
Pass se    Il deliverable non attribuisce alla traduzione rettificata effetto retroattivo.
Fail se    è affermato che la rettifica opera dalla data del deposito originario della traduzione o dalla concessione.
Indifferente  l'indicazione della data da cui la rettifica opererà.

*metadati non forniti al judge* - fonte: art. 57, comma 4, del Codice della proprietà industriale; gravita: alta; instradamento: judge

**B.24 salvezza del preuso in buona fede**  [issue: I-10] [tipo: presenza]

Verifica   Il deliverable afferma che è salvo lo sfruttamento a titolo gratuito di chi in buona fede abbia iniziato l'attuazione quando questa non costituiva contraffazione secondo la traduzione inizialmente depositata.
Pass se    compare l'affermazione della salvezza del preuso in buona fede
Fail se    la salvezza del preuso non è menzionata.
Indifferente  il richiamo agli effettivi preparativi oltre all'attuazione.

*metadati non forniti al judge* - fonte: art. 57, comma 5, del Codice della proprietà industriale; gravita: media; instradamento: judge

**B.25 preuso - lacuna sulla data di immissione**  [issue: I-10] [tipo: presenza]

Verifica   Il deliverable afferma che il fascicolo non consente di stabilire da quando il dispositivo concorrente è distribuito in Italia.
Pass se    compare l'affermazione che la data di prima immissione sul mercato italiano non risulta dal fascicolo
Fail se    è indicata una data di prima immissione sul mercato, oppure la lacuna non è dichiarata.
Indifferente  la richiesta di acquisire il dato.

*metadati non forniti al judge* - fonte: 07_rapporto_test_buy.md, punto 5.3; gravita: media; instradamento: judge

**B.26 prova tecnica - lacuna dichiarata**  [issue: I-11] [tipo: presenza]

Verifica   Il deliverable afferma che il rapporto tecnico non contiene il confronto elemento per elemento fra le rivendicazioni e il dispositivo.
Pass se    compare l'affermazione che il confronto elemento per elemento non è stato eseguito
Fail se    il rapporto è presentato come contenente il confronto, oppure la lacuna non è rilevata.
Indifferente  il richiamo al punto del rapporto che lo dichiara.

*metadati non forniti al judge* - fonte: 07_rapporto_test_buy.md, punto 5.1; gravita: alta; instradamento: judge

**B.27 prova tecnica - oggetto del confronto**  [issue: I-11] [tipo: presenza]

Verifica   Il deliverable indica che il confronto deve esaminare ciascun elemento della rivendicazione 1.
Pass se    compare l'indicazione di un confronto per ciascun elemento della rivendicazione 1
Fail se    il confronto è indicato in termini generici, oppure è riferito alla sola rivendicazione 7.
Indifferente  l'estensione del confronto anche alle rivendicazioni dipendenti.

*metadati non forniti al judge* - fonte: 02_testo_di_concessione_rivendicazioni.md; gravita: alta; instradamento: judge

**B.28 prova tecnica - insufficienza delle diciture commerciali**  [issue: I-11] [tipo: assenza]

Verifica   Il deliverable non ricava la corrispondenza tecnica dalle diciture del manuale d'uso o della scheda tecnica del distributore.
Pass se    Il deliverable non ricava la corrispondenza tecnica dalle diciture del manuale d'uso o della scheda tecnica del distributore.
Fail se    la corrispondenza fra il dispositivo e le rivendicazioni è affermata sulla base delle diciture del manuale o della scheda tecnica.
Indifferente  la citazione di quelle diciture come indizio da verificare.

*metadati non forniti al judge* - fonte: 07_rapporto_test_buy.md, punto 3.5; gravita: alta; instradamento: judge

**B.29 diffida - non è presupposto della tutela**  [issue: I-12] [tipo: presenza]

Verifica   Il deliverable afferma che la diffida non è presupposto della tutela cautelare.
Pass se    compare l'affermazione che la tutela cautelare non richiede la previa diffida
Fail se    la diffida è presentata come condizione per agire.
Indifferente  l'osservazione che la diffida documenta la conoscenza dell'illecito da parte del destinatario.

*metadati non forniti al judge* - fonte: 08_diffida_contraffazione.md; gravita: media; instradamento: judge

**B.30 diffida - natura del termine assegnato**  [issue: I-12] [tipo: qualificazione]

Verifica   Il deliverable qualifica il termine di quindici giorni assegnato nella diffida come convenzionale.
Pass se    compare, riferito a quel termine, una fra: «termine convenzionale»; «assegnato dalla parte»; «non è un termine di legge»
Fail se    il termine è presentato come termine di legge o di decadenza.
Indifferente  il richiamo alla data di scadenza del termine.

*metadati non forniti al judge* - fonte: 08_diffida_contraffazione.md; gravita: media; instradamento: judge

**B.31 ordine dei passaggi - rettifica prima dell'azione**  [issue: I-13] [tipo: presenza]

Verifica   Il deliverable colloca la messa in opponibilità della traduzione rettificata prima della richiesta di misure cautelari.
Pass se    nella sequenza proposta la rettifica opponibile precede la richiesta cautelare
Fail se    la richiesta cautelare precede la rettifica opponibile, oppure l'ordine non è indicato.
Indifferente  il numero dei passaggi intermedi.

*metadati non forniti al judge* - fonte: art. 57, comma 4, del Codice della proprietà industriale; gravita: alta; instradamento: judge

**B.32 ordine dei passaggi - prova prima della scelta dello strumento**  [issue: I-13] [tipo: presenza]

Verifica   Il deliverable colloca la costruzione del confronto tecnico prima della scelta fra descrizione, sequestro e inibitoria.
Pass se    nella sequenza proposta il confronto tecnico precede la scelta dello strumento
Fail se    lo strumento è scelto prima della costruzione del confronto.
Indifferente  la scelta dello strumento fra quelli disponibili.

*metadati non forniti al judge* - fonte: artt. 129 e 131 del Codice della proprietà industriale; gravita: alta; instradamento: judge

**B.33 ordine dei passaggi - strumenti disponibili**  [issue: I-13] [tipo: presenza]

Verifica   Il deliverable elenca fra gli strumenti disponibili la descrizione, il sequestro e l'inibitoria.
Pass se    i tre strumenti compaiono tutti fra quelli indicati
Fail se    manca uno dei tre strumenti.
Indifferente  l'inclusione dell'ordine di ritiro dal commercio fra gli strumenti.

*metadati non forniti al judge* - fonte: artt. 129 e 131 del Codice della proprietà industriale; gravita: media; instradamento: judge

**B.34 termine per il merito - regola applicabile**  [issue: I-14] [tipo: presenza]

Verifica   Il deliverable afferma che il termine per iniziare il giudizio di merito, se il giudice non lo stabilisce, è il più lungo fra venti giorni lavorativi e trentuno giorni di calendario.
Pass se    compare l'indicazione di entrambi i termini alternativi e della prevalenza del più lungo
Fail se    è indicato uno solo dei due termini, oppure non è indicata la prevalenza del più lungo.
Indifferente  il richiamo alla decorrenza dalla pronuncia in udienza o dalla comunicazione.

*metadati non forniti al judge* - fonte: art. 132, comma 2, del Codice della proprietà industriale; gravita: media; instradamento: judge

**B.35 gara - elemento di fatto sull'urgenza**  [issue: I-15] [tipo: presenza]

Verifica   Il deliverable usa la scadenza della gara come elemento di fatto sull'urgenza.
Pass se    la scadenza della gara compare fra gli elementi di fatto rilevanti per l'urgenza
Fail se    la scadenza della gara non è utilizzata, oppure è presentata come termine giuridico che condiziona l'iniziativa.
Indifferente  il richiamo al requisito tecnico del disciplinare.

*metadati non forniti al judge* - fonte: 09_avviso_gara_ospedaliera.md; gravita: media; instradamento: judge

**B.36 gara - divieto di presumere la partecipazione**  [issue: I-15] [tipo: assenza]

Verifica   Il deliverable non afferma che il concorrente partecipa alla gara.
Pass se    Il deliverable non afferma che il concorrente partecipa alla gara.
Fail se    è affermato che il concorrente ha presentato o presenterà offerta nella gara.
Indifferente  l'osservazione che il requisito tecnico del disciplinare corrisponde alla funzione del dispositivo concorrente.

*metadati non forniti al judge* - fonte: 09_avviso_gara_ospedaliera.md; gravita: alta; instradamento: judge

**B.37 gara - risposta al direttore commerciale**  [issue: I-15] [tipo: presenza]

Verifica   Il deliverable indica se sia possibile ottenere una misura prima della scadenza della gara e da quali passaggi ciò dipende.
Pass se    la risposta al direttore commerciale indica i passaggi da compiere e non un esito
Fail se    la risposta afferma che il concorrente sarà bloccato prima della gara, oppure che non è possibile fare nulla senza indicare che cosa manca.
Indifferente  il tono della risposta.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: media; instradamento: judge

**B.38 sovra-segnalazione - annualità**  [issue: N-01] [tipo: assenza]

Verifica   Il deliverable non segnala un ritardo o una decadenza relativi all'annualità italiana.
Pass se    Il deliverable non segnala un ritardo o una decadenza relativi all'annualità italiana.
Fail se    il pagamento dell'annualità del 26 giugno 2026 è presentato come tardivo, o è indicata l'applicazione di un diritto di mora o una decadenza.
Indifferente  la menzione dell'annualità fra gli adempimenti verificati e regolari.

*metadati non forniti al judge* - fonte: 04_ricevuta_annualita.md; gravita: alta; instradamento: judge

**B.39 sovra-segnalazione - designazione tedesca**  [issue: N-02] [tipo: assenza]

Verifica   Il deliverable non presenta la mancata convalida della designazione tedesca come rischio per l'azione in Italia.
Pass se    Il deliverable non presenta la mancata convalida della designazione tedesca come rischio per l'azione in Italia.
Fail se    la mancata convalida della designazione tedesca è indicata fra i rischi o fra i punti da sanare prima di agire in Italia.
Indifferente  la menzione della designazione fra gli elementi verificati.

*metadati non forniti al judge* - fonte: 10_nota_consulente_brevetti.md, punto 4.1; gravita: media; instradamento: judge

**B.40 sovra-segnalazione - domanda divisionale**  [issue: N-03] [tipo: assenza]

Verifica   Il deliverable non presenta la pendenza della domanda divisionale come elemento che indebolisce il titolo azionato.
Pass se    Il deliverable non presenta la pendenza della domanda divisionale come elemento che indebolisce il titolo azionato.
Fail se    la domanda divisionale n. 25171188.4 è indicata come elemento di debolezza del brevetto concesso o come ragione per attendere.
Indifferente  la menzione della divisionale fra gli elementi verificati.

*metadati non forniti al judge* - fonte: 10_nota_consulente_brevetti.md, punto 4.2; gravita: media; instradamento: judge

**B.41 sovra-segnalazione - consulenza tecnica preventiva**  [issue: N-04] [tipo: assenza]

Verifica   Il deliverable non indica la mancata richiesta della consulenza tecnica preventiva fra le omissioni da sanare.
Pass se    Il deliverable non indica la mancata richiesta della consulenza tecnica preventiva fra le omissioni da sanare.
Fail se    la mancata richiesta della consulenza tecnica preventiva è indicata fra le omissioni o fra gli adempimenti preliminari mancanti.
Indifferente  la proposta di ricorrervi come opzione.

*metadati non forniti al judge* - fonte: 10_nota_consulente_brevetti.md, punto 4.3; gravita: media; instradamento: judge

**B.42 simmetria del controllo - posizione dell'opponente**  [issue: -] [tipo: assenza]

Verifica   Il deliverable non presenta il difetto sul pagamento della tassa come problema anche del lato assistito.
Pass se    Il deliverable non presenta il difetto sul pagamento della tassa come problema anche del lato assistito.
Fail se    il difetto sul pagamento della tassa di opposizione è descritto come rischio o come criticità per Nevalta.
Indifferente  l'osservazione che la circostanza va verificata prima di farla valere.

*metadati non forniti al judge* - fonte: 06_estratto_conto_deposito_epo.md; gravita: media; instradamento: judge

**B.43 presunzione dell'esito - opposizione e contraffazione**  [issue: -] [tipo: assenza]

Verifica   Il deliverable non presenta come acquisiti l'esito dell'opposizione né l'accertamento della contraffazione.
Pass se    Il deliverable non presenta come acquisiti l'esito dell'opposizione né l'accertamento della contraffazione.
Fail se    è affermato che l'opposizione sarà dichiarata non proposta, oppure che la contraffazione sussiste.
Indifferente  l'indicazione della probabilità dei due esiti come valutazione riservata al committente.

*metadati non forniti al judge* - fonte: private/challenge_map.json, dati mancanti; gravita: alta; instradamento: judge


## Sezione C - date e valori calcolati

**C.1 data della pubblicazione della menzione**  [issue: I-01] [tipo: valore]

Verifica   Il deliverable indica il 28 gennaio 2026 come data di pubblicazione della menzione della concessione.
Pass se    compare la data «28 gennaio 2026» riferita alla pubblicazione della menzione
Fail se    è indicata una data diversa, oppure la data non compare.
Indifferente  il richiamo al numero del fascicolo.

*metadati non forniti al judge* - fonte: 01_estratto_bollettino_concessione.md; gravita: alta; instradamento: verifica meccanica

**C.2 scadenza del termine di opposizione**  [issue: I-02] [tipo: valore]

Verifica   Il deliverable indica il 28 ottobre 2026 come scadenza del termine di opposizione.
Pass se    compare la data «28 ottobre 2026» riferita alla scadenza del termine di opposizione
Fail se    è indicata una data diversa, oppure la scadenza non compare.
Indifferente  l'osservazione che il giorno non è festivo.

*metadati non forniti al judge* - fonte: art. 99(1) della Convenzione; gravita: alta; instradamento: verifica meccanica

**C.3 derivazione errata dal deposito della domanda**  [issue: I-02] [tipo: assenza]

Verifica   Il deliverable non computa il termine di opposizione dalla data di deposito della domanda.
Pass se    Il deliverable non computa il termine di opposizione dalla data di deposito della domanda.
Fail se    il termine di opposizione è computato dal 14 giugno 2019, o è indicata come sua scadenza una data derivata da quel giorno.
Indifferente  la menzione della data di deposito in altra funzione.

*metadati non forniti al judge* - fonte: 01_estratto_bollettino_concessione.md; gravita: alta; instradamento: judge

**C.4 derivazione errata dalla pubblicazione della domanda**  [issue: I-02] [tipo: assenza]

Verifica   Il deliverable non computa il termine di opposizione dalla pubblicazione della domanda.
Pass se    Il deliverable non computa il termine di opposizione dalla pubblicazione della domanda.
Fail se    il termine di opposizione è computato dal 16 dicembre 2020, o è indicata come sua scadenza una data derivata da quel giorno.
Indifferente  la menzione della pubblicazione della domanda in altra funzione.

*metadati non forniti al judge* - fonte: 10_nota_consulente_brevetti.md, cronologia; gravita: alta; instradamento: judge

**C.5 data di deposito dell'atto di opposizione**  [issue: I-03] [tipo: valore]

Verifica   Il deliverable indica il 27 ottobre 2026 come data di deposito dell'atto di opposizione.
Pass se    compare la data «27 ottobre 2026» riferita al deposito dell'atto
Fail se    è indicata una data diversa, oppure la data non compare.
Indifferente  il richiamo al numero della ricevuta di deposito.

*metadati non forniti al judge* - fonte: 05_atto_opposizione.md; gravita: media; instradamento: verifica meccanica

**C.6 data di valuta del pagamento della tassa**  [issue: I-04] [tipo: valore]

Verifica   Il deliverable indica il 29 ottobre 2026 come data di valuta del pagamento della tassa di opposizione.
Pass se    compare la data «29 ottobre 2026» riferita alla valuta del pagamento
Fail se    è indicata una data diversa, oppure è usata la data di registrazione dell'addebito.
Indifferente  il richiamo all'importo della tassa.

*metadati non forniti al judge* - fonte: 06_estratto_conto_deposito_epo.md; gravita: alta; instradamento: verifica meccanica

**C.7 scadenza del termine per la traduzione**  [issue: I-06] [tipo: valore]

Verifica   Il deliverable indica il 28 aprile 2026 come scadenza del termine per il deposito della traduzione.
Pass se    compare la data «28 aprile 2026» riferita alla scadenza del termine per la traduzione
Fail se    è indicata una data diversa, oppure la scadenza non compare.
Indifferente  il richiamo alla durata di tre mesi.

*metadati non forniti al judge* - fonte: art. 56, comma 4, del Codice della proprietà industriale; gravita: alta; instradamento: verifica meccanica

**C.8 data di deposito della traduzione**  [issue: I-06] [tipo: valore]

Verifica   Il deliverable indica il 24 aprile 2026 come data di deposito della traduzione italiana.
Pass se    compare la data «24 aprile 2026» riferita al deposito della traduzione
Fail se    è indicata una data diversa, oppure la data non compare.
Indifferente  il richiamo al numero di deposito telematico.

*metadati non forniti al judge* - fonte: 03_deposito_traduzione_italiana.md; gravita: alta; instradamento: verifica meccanica

**C.9 identità dell'evento di decorrenza dei due termini**  [issue: I-01] [tipo: presenza]

Verifica   Il deliverable afferma che il termine di opposizione e il termine per la traduzione decorrono dal medesimo evento.
Pass se    compare l'affermazione che i due termini decorrono dalla pubblicazione della menzione della concessione
Fail se    ai due termini sono attribuite decorrenze diverse.
Indifferente  l'ordine in cui i due termini sono esposti.

*metadati non forniti al judge* - fonte: art. 99(1) della Convenzione; art. 56, comma 4, del Codice della proprietà industriale; gravita: alta; instradamento: judge

**C.10 scadenza dell'annualità italiana**  [issue: N-01] [tipo: valore]

Verifica   Il deliverable indica il 30 giugno 2026 come scadenza dell'annualità dovuta nel 2026.
Pass se    compare la data «30 giugno 2026» riferita alla scadenza dell'annualità
Fail se    è indicata una data diversa, oppure la scadenza non compare.
Indifferente  l'indicazione dell'importo versato.

*metadati non forniti al judge* - fonte: art. 227, comma 1, del Codice della proprietà industriale; gravita: alta; instradamento: verifica meccanica

**C.11 mese di riferimento dell'annualità**  [issue: N-01] [tipo: presenza]

Verifica   Il deliverable afferma che il mese di riferimento dell'annualità è quello in cui è caduta la data di deposito della domanda europea.
Pass se    compare l'affermazione che il mese di riferimento è quello del deposito della domanda
Fail se    il mese di riferimento è ricondotto alla concessione, alla convalida o alla pubblicazione della menzione.
Indifferente  il richiamo al codice tributo usato per il versamento.

*metadati non forniti al judge* - fonte: art. 227, comma 1, del Codice della proprietà industriale; gravita: alta; instradamento: judge

**C.12 derivazione errata sull'annualità**  [issue: N-01] [tipo: assenza]

Verifica   Il deliverable non computa la scadenza dell'annualità dal mese della concessione.
Pass se    Il deliverable non computa la scadenza dell'annualità dal mese della concessione.
Fail se    la scadenza dell'annualità è indicata nell'ultimo giorno del mese di gennaio o in altra data derivata dal mese della concessione.
Indifferente  la menzione del mese della concessione in altra funzione.

*metadati non forniti al judge* - fonte: 04_ricevuta_annualita.md; gravita: alta; instradamento: judge

**C.13 termine per il merito non determinabile**  [issue: I-14] [tipo: presenza]

Verifica   Il deliverable afferma che il termine per l'inizio del giudizio di merito non è determinabile alla data di riferimento e indica che manca il provvedimento da cui decorrerebbe.
Pass se    compare l'affermazione che il termine non è determinabile e l'indicazione che manca il provvedimento cautelare da cui decorre
Fail se    è indicata una data determinata per l'inizio del giudizio di merito, oppure è affermato che il termine non è determinabile senza indicare che cosa manca.
Indifferente  l'esposizione di un calcolo su una data ipotetica, purché dichiarata come tale.

*metadati non forniti al judge* - fonte: art. 132, comma 2, del Codice della proprietà industriale; gravita: media; instradamento: judge

**C.14 termine di presentazione delle offerte**  [issue: I-15] [tipo: valore]

Verifica   Il deliverable indica il 15 dicembre 2026 come termine di presentazione delle offerte nella gara.
Pass se    compare la data «15 dicembre 2026» riferita al termine di presentazione delle offerte
Fail se    è indicata una data diversa, oppure la data non compare.
Indifferente  l'indicazione dell'ora e della data della prima seduta pubblica.

*metadati non forniti al judge* - fonte: 09_avviso_gara_ospedaliera.md; gravita: media; instradamento: verifica meccanica
