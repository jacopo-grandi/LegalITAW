# WF2-091 - Criteri atomizzati

Identificativi e conteggio coincidono con `rubric.json` e `runtime_routing.json`:
i tre file sono emessi da un'unica fonte autoriale.

Il judge riceve il deliverable e il testo del criterio, nient'altro. La riga
`metadati non forniti al judge` e tutto ciò che segue sono metadati di build.

La decisione è binaria: il criterio passa se è soddisfatta almeno una condizione
`Pass se` o se ricorre esattamente il caso dichiarato `Indifferente`; fallisce se
ricorre `Fail se` oppure se il requisito verificato è solo parzialmente soddisfatto.


## Sezione A - forma dell'output (interamente verifica meccanica)

**A.1 file consegnati**  [issue: -] [tipo: struttura]

Verifica   La consegna contiene due file con i nomi richiesti.
Pass se    sono presenti clean_team_protocol_redline.docx e note.md
Fail se    manca uno dei due file oppure un nome diverge da quello richiesto.

*metadati non forniti al judge* - fonte: public/01_task.md e response_template.md; gravita: media; instradamento: verifica meccanica

**A.2 revisioni tracciate presenti**  [issue: -] [tipo: struttura]

Verifica   Il file docx consegnato contiene almeno una revisione tracciata.
Pass se    il documento contiene almeno un elemento di inserimento o di cancellazione tracciata
Fail se    il documento non contiene alcuna revisione tracciata, oppure le modifiche sono state applicate al testo senza tracciatura.
Indifferente  il numero delle revisioni e la scelta fra sostituzione e riscrittura del periodo.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: alta; instradamento: verifica meccanica

**A.3 sezioni della nota**  [issue: -] [tipo: struttura]

Verifica   Il file note.md contiene le sette sezioni indicate, nell'ordine indicato.
Pass se    le sette intestazioni compaiono tutte e nella sequenza del response_template
Fail se    manca un'intestazione oppure l'ordine differisce.
Indifferente  la formulazione delle intestazioni oltre le prime ventidue battute.

*metadati non forniti al judge* - fonte: public/response_template.md; gravita: media; instradamento: verifica meccanica

**A.4 data di riferimento**  [issue: -] [tipo: valore]

Verifica   Il deliverable assume come data di riferimento il 14 ottobre 2026.
Pass se    compare «14 ottobre 2026» come data alla quale l'analisi è riferita
Fail se    è assunta una data diversa, oppure la data di riferimento non compare.
Indifferente  il formato della data.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: alta; instradamento: verifica meccanica

**A.5 clausola indicata per ogni intervento**  [issue: -] [tipo: struttura]

Verifica   Ogni intervento elencato nella nota indica il numero della clausola su cui incide.
Pass se    ciascuna voce dell'elenco degli interventi riporta un numero di clausola
Fail se    una o più voci non riportano alcun numero di clausola.
Indifferente  la forma del riferimento alla clausola.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: alta; instradamento: verifica meccanica

**A.6 allegato indicato per ogni intervento**  [issue: -] [tipo: struttura]

Verifica   Ogni intervento elencato nella nota indica almeno un allegato del fascicolo.
Pass se    ciascuna voce dell'elenco degli interventi riporta il nome di almeno un allegato
Fail se    una o più voci non riportano alcun allegato.
Indifferente  il numero degli allegati citati per voce.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: alta; instradamento: verifica meccanica

**A.7 posizione minima indicata per ogni intervento**  [issue: -] [tipo: struttura]

Verifica   Ogni intervento elencato nella nota indica la posizione minima proposta.
Pass se    ciascuna voce dell'elenco degli interventi riporta una posizione di ripiego
Fail se    una o più voci non indicano alcuna posizione minima.
Indifferente  il contenuto della posizione minima, che è valutato nei criteri di merito.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: alta; instradamento: verifica meccanica

**A.8 riferimenti normativi entro l'elenco chiuso**  [issue: -] [tipo: assenza]

Verifica   Il deliverable non cita riferimenti normativi assenti dal reference pack.
Pass se    Il deliverable non cita riferimenti normativi assenti dal reference pack.
Fail se    compare un riferimento a un atto, a un articolo o a un provvedimento che non figura in public/02_reference_pack.md.
Indifferente  la scelta di non citare alcuna fonte in una singola voce.

*metadati non forniti al judge* - fonte: public/02_reference_pack.md e private/fonti_chiuse.json; gravita: alta; instradamento: verifica meccanica

**A.9 limite di parole**  [issue: -] [tipo: struttura]

Verifica   Il file note.md resta entro il limite di parole.
Pass se    il conteggio delle parole di note.md non supera 3000
Fail se    il conteggio supera il limite.

*metadati non forniti al judge* - fonte: public/response_template.md; gravita: bassa; instradamento: verifica meccanica


## Sezione B - merito

Stato del fascicolo alla data di riferimento: trattativa in corso; bozza di protocollo rimandata dalla controparte e non sottoscritta; nessuna reazione registrata all'accesso del 5 e 6 ottobre 2026

**B.1 direttore vendite - ruolo sostanziale**  [issue: I-01] [tipo: qualificazione]

Verifica   Il deliverable qualifica il direttore vendite di Tramontina come soggetto che partecipa alle decisioni di prezzo, sconto o allocazione dei volumi fra clienti.
Pass se    compare, riferita a quella posizione, una fra: «decide sconti»; «decide i target per cliente»; «decide l'allocazione dei volumi»; «partecipa alla determinazione dei prezzi»
Fail se    la posizione è descritta solo come funzione commerciale generica, oppure la qualificazione non compare.
Indifferente  il nome della persona che occupa la posizione.

*metadati non forniti al judge* - fonte: 04_organigramma_e_deleghe.md; clausola 4.2; gravita: alta; instradamento: judge

**B.2 direttore vendite - intervento sulla clausola 4.2**  [issue: I-01] [tipo: presenza]

Verifica   Il deliverable interviene sulla clausola 4.2 rimuovendo l'obbligo di designare il direttore vendite fra i membri del clean team.
Pass se    la clausola 4.2 è indicata fra le clausole modificate e l'intervento sopprime la designazione del direttore vendite
Fail se    l'intervento riguarda soltanto l'Allegato A, oppure la clausola 4.2 non è modificata.
Indifferente  la formulazione del testo sostitutivo.

*metadati non forniti al judge* - fonte: clausola 4.2 della bozza; gravita: alta; instradamento: judge

**B.3 direttore vendite - criterio sostitutivo**  [issue: I-01] [tipo: presenza]

Verifica   Il deliverable propone un criterio di esclusione riferito alla partecipazione alle decisioni commerciali, e non alla qualifica formale.
Pass se    il testo proposto esclude dal clean team chi partecipa alla determinazione dei prezzi, degli sconti, dei target per cliente o dell'allocazione dei volumi
Fail se    il testo proposto esclude soltanto posizioni indicate per denominazione o per funzione.
Indifferente  l'elenco delle decisioni commerciali richiamate, purché comprenda i prezzi.

*metadati non forniti al judge* - fonte: clausola 4.2 della bozza; gravita: alta; instradamento: judge

**B.4 cumulo di ruoli - rilevazione**  [issue: I-01] [tipo: presenza]

Verifica   Il deliverable afferma che lo stesso soggetto è designato membro del clean team ed è titolare della gestione operativa delle richieste informative verso la controparte.
Pass se    compare l'affermazione del cumulo fra la qualità di membro del clean team e il ruolo di project manager con delega alle richieste informative
Fail se    il cumulo non è rilevato, oppure i due ruoli sono trattati come questioni separate.
Indifferente  la data da cui il cumulo sussiste.

*metadati non forniti al judge* - fonte: 04_organigramma_e_deleghe.md, nota alla posizione di direttore vendite; gravita: alta; instradamento: judge

**B.5 cumulo di ruoli - divieto nel testo**  [issue: I-01] [tipo: presenza]

Verifica   Il deliverable introduce nel protocollo un divieto di cumulo fra la qualità di membro del clean team e la gestione operativa delle richieste informative.
Pass se    fra gli interventi compare l'inserimento di una clausola che vieta quel cumulo
Fail se    il punto è risolto soltanto sostituendo la persona designata.
Indifferente  la collocazione della nuova clausola.

*metadati non forniti al judge* - fonte: clausole 4.2 e 7.1 della bozza; gravita: alta; instradamento: judge

**B.6 accesso indifferenziato - rilevazione**  [issue: I-02] [tipo: presenza]

Verifica   Il deliverable afferma che la clausola 5.2 consente ai membri del clean team e ai consulenti ammessi l'accesso all'intero contenuto della sala documentale.
Pass se    compare l'affermazione che l'accesso previsto dalla clausola 5.2 è indifferenziato
Fail se    la clausola 5.2 non è rilevata, oppure è descritta come conforme.
Indifferente  il richiamo alla configurazione riportata nel registro accessi.

*metadati non forniti al judge* - fonte: clausola 5.2 della bozza; gravita: alta; instradamento: judge

**B.7 accesso indifferenziato - classificazione priva di effetto**  [issue: I-02] [tipo: qualificazione]

Verifica   Il deliverable qualifica la classificazione dell'Allegato B come priva di effetto vincolante per come è richiamata dalla clausola 5.2.
Pass se    compare, riferita alla classificazione dell'Allegato B, una fra: «ha valore soltanto informativo»; «non vincola l'accesso»; «non produce effetti sui permessi»
Fail se    è affermato che la classificazione dell'Allegato B vincola l'accesso ai documenti.
Indifferente  la proposta di riscrivere l'Allegato B anziché la clausola 5.2.

*metadati non forniti al judge* - fonte: clausola 5.2 e Allegato B della bozza; gravita: alta; instradamento: judge

**B.8 accesso indifferenziato - matrice sostitutiva**  [issue: I-02] [tipo: presenza]

Verifica   Il deliverable propone una matrice di accesso che distingue almeno la raccolta, l'analisi e la destinazione della restituzione.
Pass se    il testo proposto associa profili distinti alle fasi di raccolta, di analisi e di restituzione
Fail se    il testo proposto introduce un unico livello di autorizzazione, oppure rinvia la definizione dei profili a un momento successivo senza indicarne il contenuto.
Indifferente  il nome dato all'allegato che contiene la matrice.

*metadati non forniti al judge* - fonte: clausola 5.2 della bozza; gravita: alta; instradamento: judge

**B.9 download locale - intervento**  [issue: I-03] [tipo: presenza]

Verifica   Il deliverable esclude il download dei documenti che contengono informazioni commercialmente sensibili sui dispositivi in uso ai membri del clean team.
Pass se    fra gli interventi compare l'esclusione del download dei documenti classificati CT-RESTRICTED
Fail se    il download resta consentito, oppure è subordinato al solo obbligo di conservazione riservata.
Indifferente  la disciplina proposta per il download dei documenti non riservati.

*metadati non forniti al judge* - fonte: clausola 5.3 della bozza; gravita: alta; instradamento: judge

**B.10 download locale - obbligo di comportamento insufficiente**  [issue: I-03] [tipo: qualificazione]

Verifica   Il deliverable qualifica l'obbligo di conservazione riservata previsto dalla clausola 5.3 come obbligo di comportamento e non come misura tecnica.
Pass se    compare, riferito a quell'obbligo, una fra: «obbligo di comportamento»; «non è una misura tecnica»; «non impedisce la duplicazione»
Fail se    l'obbligo è presentato come presidio equivalente a una misura tecnica.
Indifferente  il richiamo al contenitore gestito come soluzione alternativa.

*metadati non forniti al judge* - fonte: clausola 5.3 della bozza; gravita: media; instradamento: judge

**B.11 aggregazione - eccezione rilevata**  [issue: I-04] [tipo: presenza]

Verifica   Il deliverable afferma che la clausola 6.2 ammette la restituzione in forma disaggregata per singolo cliente quando ciò sia necessario alla finalità ammessa.
Pass se    compare l'affermazione che la clausola 6.2 contiene un'eccezione all'obbligo di aggregazione
Fail se    la clausola 6.2 è registrata come conforme perché prevede la restituzione aggregata, oppure l'eccezione non è rilevata.
Indifferente  il richiamo alla definizione del punto 4.2 del term sheet.

*metadati non forniti al judge* - fonte: clausola 6.2 della bozza; gravita: alta; instradamento: judge

**B.12 aggregazione - eccezione soppressa**  [issue: I-04] [tipo: presenza]

Verifica   Il deliverable sopprime l'eccezione della clausola 6.2.
Pass se    fra gli interventi compare la soppressione della restituzione in forma disaggregata per singolo cliente
Fail se    l'eccezione è mantenuta con una condizione ulteriore, oppure non è oggetto di intervento.
Indifferente  la scelta di riscrivere l'intera clausola anziché il solo periodo.

*metadati non forniti al judge* - fonte: clausola 6.2 della bozza; gravita: alta; instradamento: judge

**B.13 aggregazione - eccezione rimessa al richiedente**  [issue: I-04] [tipo: qualificazione]

Verifica   Il deliverable qualifica la valutazione di necessità prevista dalla clausola 6.2 come rimessa al soggetto che formula la richiesta.
Pass se    compare, riferita a quella valutazione, una fra: «rimessa al richiedente»; «nella disponibilità della parte richiedente»; «non affidata a un terzo»
Fail se    la valutazione di necessità è presentata come vincolata o come affidata a un terzo.
Indifferente  la proposta di affidare la valutazione al consulente indipendente in via subordinata.

*metadati non forniti al judge* - fonte: clausola 6.2 della bozza; gravita: media; instradamento: judge

**B.14 destinatari della restituzione - rilevazione**  [issue: I-05] [tipo: presenza]

Verifica   Il deliverable afferma che la clausola 6.3 rimette al richiedente l'indicazione dei destinatari della restituzione.
Pass se    compare l'affermazione che i destinatari sono indicati dal richiedente
Fail se    la clausola 6.3 non è rilevata, oppure è presentata come neutra.
Indifferente  il richiamo alla voce 22 della data request list.

*metadati non forniti al judge* - fonte: clausola 6.3 della bozza; gravita: alta; instradamento: judge

**B.15 destinatari della restituzione - vincolo proposto**  [issue: I-05] [tipo: presenza]

Verifica   Il deliverable propone di escludere dalla restituzione chi partecipa alle decisioni di prezzo, sconto o allocazione dei volumi.
Pass se    il testo proposto esclude la restituzione a chi partecipa a quelle decisioni
Fail se    il testo proposto si limita a richiedere l'autorizzazione del clean team lead per l'individuazione dei destinatari.
Indifferente  il rinvio alla matrice di accesso.

*metadati non forniti al judge* - fonte: clausola 6.3 della bozza; gravita: alta; instradamento: judge

**B.16 documenti derivati - perimetro**  [issue: I-06] [tipo: presenza]

Verifica   Il deliverable estende la disciplina della clausola 6.4 ai documenti derivati diversi dalle elaborazioni dei consulenti.
Pass se    il testo proposto comprende almeno gli appunti e i fogli di lavoro fra i documenti che ereditano la classificazione del documento di origine
Fail se    la clausola 6.4 resta riferita alle sole elaborazioni intermedie dei consulenti.
Indifferente  l'elenco dei tipi di documento derivato, purché non si limiti alle elaborazioni dei consulenti.

*metadati non forniti al judge* - fonte: clausola 6.4 della bozza; gravita: media; instradamento: judge

**B.17 documenti derivati - ereditarietà della classificazione**  [issue: I-06] [tipo: presenza]

Verifica   Il deliverable afferma che i documenti derivati devono ereditare la classificazione del documento da cui derivano.
Pass se    compare l'affermazione dell'ereditarietà della classificazione
Fail se    i documenti derivati sono ricondotti al solo obbligo generale di riservatezza.
Indifferente  la scelta di collocare la regola nella clausola 6.4 o in un allegato.

*metadati non forniti al judge* - fonte: clausola 6.4 della bozza; 05_email_direttore_vendite.md; gravita: media; instradamento: judge

**B.18 approvazione delle richieste - rilevazione**  [issue: I-07] [tipo: presenza]

Verifica   Il deliverable afferma che la clausola 7.1 affida l'approvazione delle nuove richieste informative al project manager.
Pass se    compare l'affermazione che l'approvazione prevista dalla clausola 7.1 spetta al project manager
Fail se    la clausola 7.1 non è rilevata, oppure è affermato che l'approvazione del project manager basta a rendere ammissibile la richiesta.
Indifferente  il richiamo alle voci 18, 19 e 22 della data request list.

*metadati non forniti al judge* - fonte: clausola 7.1 della bozza; gravita: alta; instradamento: judge

**B.19 approvazione delle richieste - presidio proposto**  [issue: I-07] [tipo: presenza]

Verifica   Il deliverable propone che l'approvazione delle nuove richieste sia rilasciata dal clean team lead con il visto del consulente legale, prima dell'inoltro alla controparte.
Pass se    il testo proposto richiede sia il clean team lead sia il consulente legale e colloca l'approvazione prima dell'inoltro
Fail se    il testo proposto richiede un solo approvante, oppure colloca il controllo dopo l'inoltro.
Indifferente  la denominazione data al consulente legale incaricato.

*metadati non forniti al judge* - fonte: clausola 7.1 della bozza; gravita: alta; instradamento: judge

**B.20 voce 18 - contenuto della richiesta**  [issue: I-08] [tipo: qualificazione]

Verifica   Il deliverable qualifica la voce 18 della data request list come richiesta di prezzi futuri, sconti programmati e volumi riferibili a singoli clienti identificati.
Pass se    compare, riferita alla voce 18, una fra: «prezzi futuri per singolo cliente»; «dati individualizzati»; «riferibili a clienti identificati»
Fail se    la voce 18 è descritta come richiesta di dati commerciali generici, oppure non è qualificata.
Indifferente  il richiamo al carattere prospettico del dato oltre al carattere individualizzato.

*metadati non forniti al judge* - fonte: 03_data_request_list.md, voce 18; gravita: alta; instradamento: judge

**B.21 voce 18 - ritiro dal flusso**  [issue: I-08] [tipo: presenza]

Verifica   Il deliverable indica il ritiro della voce 18 dal flusso informativo.
Pass se    fra le azioni compare il ritiro o lo stralcio della voce 18
Fail se    la voce 18 è mantenuta subordinandola al transito dal clean team o all'aggregazione successiva.
Indifferente  la proposta di sostituire la voce 18 con una richiesta di dati storici aggregati.

*metadati non forniti al judge* - fonte: 03_data_request_list.md, voce 18; gravita: alta; instradamento: judge

**B.22 voce 22 - destinatario commerciale**  [issue: I-08] [tipo: presenza]

Verifica   Il deliverable afferma che la voce 22 prevede la restituzione ai referenti commerciali delle parti.
Pass se    compare l'affermazione che il destinatario indicato nella voce 22 è la struttura commerciale
Fail se    la voce 22 è trattata come problema di forma del dato senza rilevare il destinatario.
Indifferente  il richiamo al numero delle posizioni oggetto della restituzione.

*metadati non forniti al judge* - fonte: 03_data_request_list.md, voce 22; gravita: alta; instradamento: judge

**B.23 voce 22 - rifiuto**  [issue: I-08] [tipo: presenza]

Verifica   Il deliverable indica il rifiuto della voce 22.
Pass se    fra le azioni compare il rifiuto o lo stralcio della voce 22
Fail se    la voce 22 è mantenuta imponendo l'aggregazione del dato restituito.
Indifferente  la proposta di restituire alla sola funzione amministrazione, finanza e controllo.

*metadati non forniti al judge* - fonte: 03_data_request_list.md, voce 22; gravita: alta; instradamento: judge

**B.24 classe D - conseguenza operativa**  [issue: I-09] [tipo: presenza]

Verifica   Il deliverable indica la sospensione della restituzione sulla classe D oppure la sua ricomposizione.
Pass se    fra le azioni compare, riferita alla classe D, la sospensione della restituzione oppure la ricomposizione della classe
Fail se    la classe D è trattata come utilizzabile, oppure la conseguenza operativa non è indicata.
Indifferente  la scelta fra sospensione e ricomposizione.

*metadati non forniti al judge* - fonte: voce 21 di 03_data_request_list.md; punto 4.2 del term sheet; gravita: media; instradamento: judge

**B.25 classe D - fonte della convenzione**  [issue: I-09] [tipo: attribuzione]

Verifica   Il deliverable riconduce il requisito delle cinque unità al punto 4.2 del term sheet.
Pass se    il requisito è ricondotto al punto 4.2 del term sheet del 24 luglio 2026
Fail se    il requisito è presentato come regola di fonte esterna al fascicolo, oppure non è ricondotto ad alcun documento.
Indifferente  il richiamo contestuale al punto 4.3 del term sheet.

*metadati non forniti al judge* - fonte: punto 4.2 del term sheet; gravita: media; instradamento: judge

**B.26 riunioni - presenza del consulente**  [issue: I-10] [tipo: presenza]

Verifica   Il deliverable rende necessaria la presenza del consulente legale alle riunioni fra le parti.
Pass se    il testo proposto qualifica la presenza del consulente legale come necessaria
Fail se    la presenza resta facoltativa o rimessa a una valutazione di opportunità.
Indifferente  l'individuazione del consulente per denominazione.

*metadati non forniti al judge* - fonte: clausola 8.1 della bozza; gravita: alta; instradamento: judge

**B.27 riunioni - verbalizzazione**  [issue: I-10] [tipo: presenza]

Verifica   Il deliverable introduce l'obbligo di verbalizzare le informazioni condivise nelle riunioni fra le parti.
Pass se    il testo proposto prevede un verbale con indicazione delle informazioni condivise
Fail se    la verbalizzazione resta esclusa, oppure è prevista senza indicazione delle informazioni condivise.
Indifferente  il termine entro cui il verbale deve essere redatto.

*metadati non forniti al judge* - fonte: clausola 8.1 della bozza; gravita: alta; instradamento: judge

**B.28 riunioni - ordine del giorno preventivo**  [issue: I-10] [tipo: presenza]

Verifica   Il deliverable introduce l'obbligo di trasmettere un ordine del giorno prima della riunione.
Pass se    il testo proposto prevede la trasmissione preventiva dell'ordine del giorno
Fail se    l'ordine del giorno preventivo non è previsto.
Indifferente  il numero di giorni di preavviso.

*metadati non forniti al judge* - fonte: clausola 8.1 della bozza; gravita: media; instradamento: judge

**B.29 durata - difetto rilevato**  [issue: I-11] [tipo: qualificazione]

Verifica   Il deliverable qualifica il termine della clausola 9.1 come non determinato.
Pass se    compare, riferito al termine della clausola 9.1, una fra: «non determinato»; «privo di un termine finale»; «rimesso a un evento non definito»
Fail se    il termine è presentato come determinato perché ancorato al completamento della valutazione.
Indifferente  il richiamo alla durata dell'esclusiva prevista dal term sheet.

*metadati non forniti al judge* - fonte: clausola 9.1 della bozza; gravita: alta; instradamento: judge

**B.30 durata - eventi proposti**  [issue: I-11] [tipo: presenza]

Verifica   Il deliverable ancora la cessazione di efficacia sia al provvedimento conclusivo del procedimento di autorizzazione sia all'abbandono dell'operazione.
Pass se    il testo proposto indica entrambi gli eventi, con applicazione di quello anteriore
Fail se    il testo proposto indica un solo evento, oppure non indica quale prevale.
Indifferente  la formulazione dell'evento di abbandono.

*metadati non forniti al judge* - fonte: clausola 9.1 della bozza; gravita: alta; instradamento: judge

**B.31 distruzione - perimetro esteso**  [issue: I-12] [tipo: presenza]

Verifica   Il deliverable estende il perimetro della distruzione ai documenti derivati, alle copie presenti sui dispositivi e alle copie di backup.
Pass se    il testo proposto comprende tutte e tre le categorie
Fail se    il perimetro resta limitato ai file caricati nella sala documentale, oppure comprende solo una parte delle tre categorie.
Indifferente  l'ordine in cui le categorie sono elencate.

*metadati non forniti al judge* - fonte: clausola 10.1 della bozza; 07_bozza_certificato_distruzione.md; gravita: alta; instradamento: judge

**B.32 distruzione - copia di difesa segregata**  [issue: I-12] [tipo: presenza]

Verifica   Il deliverable introduce una copia di difesa conservata in ambiente segregato.
Pass se    il testo proposto prevede la conservazione di una copia in ambiente segregato per fini di difesa
Fail se    la copia di difesa non è prevista.
Indifferente  la denominazione data all'ambiente segregato.

*metadati non forniti al judge* - fonte: clausola 10.1 della bozza; gravita: alta; instradamento: judge

**B.33 distruzione - termine e responsabile della copia**  [issue: I-12] [tipo: presenza]

Verifica   Il deliverable indica sia il termine di conservazione della copia di difesa sia i soggetti che possono accedervi.
Pass se    il testo proposto indica un termine di conservazione e individua i soggetti abilitati all'accesso
Fail se    manca il termine, oppure manca l'individuazione dei soggetti abilitati.
Indifferente  la durata del termine proposto.

*metadati non forniti al judge* - fonte: clausole 9.2 e 10.1 della bozza; gravita: alta; instradamento: judge

**B.34 autoqualificazione - rilevazione**  [issue: I-13] [tipo: presenza]

Verifica   Il deliverable afferma che la clausola 3.3 attribuisce all'adozione del protocollo l'effetto di assicurare il rispetto della normativa in materia di concorrenza.
Pass se    compare l'affermazione che la clausola 3.3 contiene una qualificazione di conformità
Fail se    la clausola 3.3 non è rilevata.
Indifferente  il richiamo alla natura di misura organizzativa del protocollo.

*metadati non forniti al judge* - fonte: clausola 3.3 della bozza; gravita: media; instradamento: judge

**B.35 autoqualificazione - intervento**  [issue: I-13] [tipo: presenza]

Verifica   Il deliverable sopprime o sostituisce la qualificazione di conformità della clausola 3.3.
Pass se    fra gli interventi compare la soppressione della clausola 3.3 oppure la sua sostituzione con una dichiarazione che non qualifica la liceità delle condotte
Fail se    la clausola 3.3 è mantenuta invariata.
Indifferente  la scelta fra soppressione e sostituzione.

*metadati non forniti al judge* - fonte: clausola 3.3 della bozza; gravita: media; instradamento: judge

**B.36 incidente - fatto accertato**  [issue: I-14] [tipo: presenza]

Verifica   Il deliverable afferma che un'utenza ha scaricato file classificati CT-RESTRICTED pur appartenendo al gruppo con accesso indifferenziato.
Pass se    compare l'affermazione del download di file CT-RESTRICTED da parte di un'utenza del gruppo CT-ALL
Fail se    il download non è rilevato, oppure è presentato come accesso conforme.
Indifferente  l'indicazione dell'orario degli eventi.

*metadati non forniti al judge* - fonte: 06_log_accessi_data_room.csv, eventi del 5 ottobre 2026; gravita: alta; instradamento: judge

**B.37 incidente - assenza di reazione**  [issue: I-14] [tipo: presenza]

Verifica   Il deliverable afferma che nel registro non risulta alcuna revoca, sospensione o segnalazione di incidente successiva agli eventi.
Pass se    compare l'affermazione che il registro non riporta revoche, sospensioni o segnalazioni
Fail se    è affermato che l'utenza è stata sospesa o che l'incidente è stato gestito.
Indifferente  il richiamo all'esportazione del registro effettuata il 6 ottobre.

*metadati non forniti al judge* - fonte: 06_log_accessi_data_room.csv; gravita: alta; instradamento: judge

**B.38 incidente - azioni immediate**  [issue: I-14] [tipo: presenza]

Verifica   Il deliverable indica la sospensione dell'utenza, la ricostruzione del materiale effettivamente visto e il recupero o la distruzione della copia locale.
Pass se    fra le azioni compaiono tutte e tre: sospensione dell'utenza, ricostruzione del materiale visto, recupero o distruzione della copia locale
Fail se    manca una delle tre azioni.
Indifferente  l'ordine in cui le azioni sono elencate.

*metadati non forniti al judge* - fonte: 06_log_accessi_data_room.csv; 05_email_direttore_vendite.md; gravita: alta; instradamento: judge

**B.39 incidente - collocazione fra gli interventi urgenti**  [issue: I-14] [tipo: presenza]

Verifica   Il deliverable colloca la gestione dell'incidente fra gli adempimenti da eseguire subito e non fra le modifiche del testo.
Pass se    l'incidente compare nella sezione degli interventi urgenti indipendenti dalla revisione del testo
Fail se    l'incidente è trattato soltanto come difetto contrattuale da correggere in redline.
Indifferente  la presenza di un rinvio all'incidente anche nella parte sulle clausole.

*metadati non forniti al judge* - fonte: public/response_template.md; gravita: alta; instradamento: judge

**B.40 coordinamento commerciale - qualificazione**  [issue: I-15] [tipo: qualificazione]

Verifica   Il deliverable qualifica la proposta di allineare il calendario delle campagne promozionali come condotta di coordinamento fra concorrenti.
Pass se    compare, riferita a quella proposta, una fra: «coordinamento fra concorrenti»; «condotta coordinata»; «allineamento delle strategie commerciali»
Fail se    la proposta è descritta come scambio informativo da disciplinare, oppure non è qualificata.
Indifferente  il richiamo alla finestra temporale indicata nel messaggio.

*metadati non forniti al judge* - fonte: 05_email_direttore_vendite.md, secondo punto; gravita: alta; instradamento: judge

**B.41 coordinamento commerciale - interruzione immediata**  [issue: I-15] [tipo: presenza]

Verifica   Il deliverable indica l'interruzione immediata della condotta.
Pass se    fra le azioni compare l'istruzione di non dare seguito alla proposta e di non discuterla in riunione
Fail se    l'azione indicata è soltanto l'inserimento di una clausola nel protocollo.
Indifferente  la forma dell'istruzione interna proposta.

*metadati non forniti al judge* - fonte: 05_email_direttore_vendite.md; gravita: alta; instradamento: judge

**B.42 coordinamento commerciale - autonomia del piano**  [issue: I-15] [tipo: presenza]

Verifica   Il deliverable afferma che la condotta non è risolvibile con una modifica del protocollo.
Pass se    compare l'affermazione che la modifica del protocollo non copre la condotta e che questa va interrotta a prescindere dal testo
Fail se    la condotta è presentata come risolta dalla revisione della clausola sulle riunioni.
Indifferente  la proposta di aggiungere comunque una clausola sul punto.

*metadati non forniti al judge* - fonte: 05_email_direttore_vendite.md; gravita: alta; instradamento: judge

**B.43 regime di controllo - conclusione**  [issue: I-16] [tipo: presenza]

Verifica   Il deliverable afferma che l'operazione non è soggetta a comunicazione preventiva obbligatoria.
Pass se    compare l'affermazione che non sorge l'obbligo di comunicazione preventiva
Fail se    è affermato che l'operazione va comunicata, oppure la conclusione non compare.
Indifferente  il richiamo alla condizione sospensiva del term sheet.

*metadati non forniti al judge* - fonte: 02_term_sheet_joint_venture.md, Allegato 1; gravita: media; instradamento: judge

**B.44 regime di controllo - potere di richiesta della notifica**  [issue: I-16] [tipo: presenza]

Verifica   Il deliverable afferma che l'operazione resta fra quelle di cui l'Autorità può richiedere la notifica.
Pass se    compare l'affermazione che l'Autorità conserva il potere di richiedere la notifica dell'operazione
Fail se    il potere di richiesta non è menzionato, oppure è presentato come obbligo di notifica.
Indifferente  il termine entro cui il potere può essere esercitato.

*metadati non forniti al judge* - fonte: 02_term_sheet_joint_venture.md, Allegato 1; gravita: media; instradamento: judge

**B.45 sovra-segnalazione - listino pubblicato**  [issue: N-01] [tipo: assenza]

Verifica   Il deliverable non chiede il ritiro o lo stralcio della voce 20 della data request list.
Pass se    Il deliverable non chiede il ritiro o lo stralcio della voce 20 della data request list.
Fail se    la voce 20, relativa al listino di vendita 2026 pubblicato sul sito, è indicata fra le richieste da ritirare, da stralciare o da subordinare ad autorizzazione.
Indifferente  la menzione della voce 20 fra gli elementi che non richiedono intervento.

*metadati non forniti al judge* - fonte: 03_data_request_list.md, voce 20; gravita: media; instradamento: judge

**B.46 sovra-segnalazione - capacità produttiva aggregata**  [issue: N-02] [tipo: assenza]

Verifica   Il deliverable non indica le voci 16 e 19 fra le richieste da ritirare.
Pass se    Il deliverable non indica le voci 16 e 19 fra le richieste da ritirare.
Fail se    la richiesta di capacità produttiva installata per stabilimento in forma aggregata è indicata come richiesta da ritirare o come violazione.
Indifferente  l'osservazione che la voce 19 è stata approvata dal project manager, che è un rilievo sul presidio e non sul contenuto del dato.

*metadati non forniti al judge* - fonte: 03_data_request_list.md, voci 16 e 19; gravita: media; instradamento: judge

**B.47 sovra-segnalazione - divieto di perfezionamento**  [issue: N-03] [tipo: assenza]

Verifica   Il deliverable non afferma l'esistenza di un divieto di perfezionare l'operazione prima della decisione dell'Autorità.
Pass se    Il deliverable non afferma l'esistenza di un divieto di perfezionare l'operazione prima della decisione dell'Autorità.
Fail se    compare l'affermazione che le parti non possono perfezionare l'operazione prima di una decisione dell'Autorità, o che il perfezionamento anticipato è vietato.
Indifferente  il richiamo al potere dell'Autorità di ordinare la sospensione in caso di istruttoria e di imporre misure ripristinatorie a operazione già realizzata.

*metadati non forniti al judge* - fonte: art. 16 e art. 17 L. 287/1990; art. 7 Reg. (CE) 139/2004; gravita: alta; instradamento: judge

**B.48 sovra-segnalazione - dato grezzo al consulente**  [issue: N-04] [tipo: assenza]

Verifica   Il deliverable non chiede che il consulente indipendente riceva soltanto dati aggregati.
Pass se    Il deliverable non chiede che il consulente indipendente riceva soltanto dati aggregati.
Fail se    il trattamento del dato grezzo da parte del consulente indipendente è indicato come esposizione da eliminare, o è chiesto che anche il consulente riceva dati già aggregati.
Indifferente  la richiesta di rafforzare la separazione dichiarata nella lettera di incarico del consulente.

*metadati non forniti al judge* - fonte: clausola 6.1 della bozza; 04_organigramma_e_deleghe.md; gravita: media; instradamento: judge

**B.49 sovra-segnalazione - clausola penale**  [issue: N-05] [tipo: assenza]

Verifica   Il deliverable non indica la clausola penale del punto 11.2 fra le esposizioni di Tramontina.
Pass se    Il deliverable non indica la clausola penale del punto 11.2 fra le esposizioni di Tramontina.
Fail se    la clausola penale di cui al punto 11.2 è presentata come rischio o come esposizione del lato assistito.
Indifferente  la proposta di rivedere l'importo della penale.

*metadati non forniti al judge* - fonte: clausola 11.2 della bozza; gravita: bassa; instradamento: judge

**B.50 simmetria del controllo - accesso dell'utenza di Tramontina**  [issue: -] [tipo: assenza]

Verifica   Il deliverable non presenta l'accesso registrato il 5 ottobre 2026 come episodio riferibile a entrambe le parti.
Pass se    Il deliverable non presenta l'accesso registrato il 5 ottobre 2026 come episodio riferibile a entrambe le parti.
Fail se    l'accesso ai file CT-RESTRICTED è descritto come problema comune alle due parti, o è attribuito anche a utenze della controparte.
Indifferente  l'osservazione che la configurazione dei permessi era comune alle due parti, che riguarda la piattaforma e non l'accesso.

*metadati non forniti al judge* - fonte: 06_log_accessi_data_room.csv; gravita: media; instradamento: judge

**B.51 presunzione dell'esito - copia sul dispositivo locale**  [issue: -] [tipo: assenza]

Verifica   Il deliverable non afferma che la copia salvata sul dispositivo locale è stata cancellata o che non è stata ulteriormente trasmessa.
Pass se    Il deliverable non afferma che la copia salvata sul dispositivo locale è stata cancellata o che non è stata ulteriormente trasmessa.
Fail se    compare l'affermazione che la copia locale è stata eliminata, o che non risultano ulteriori trasmissioni o duplicazioni.
Indifferente  la richiesta di verificare se la copia sia stata trasmessa o duplicata.

*metadati non forniti al judge* - fonte: 05_email_direttore_vendite.md; private/challenge_map.json, dati mancanti; gravita: alta; instradamento: judge


## Sezione C - date e valori calcolati

**C.1 data del download non autorizzato**  [issue: I-14] [tipo: valore]

Verifica   Il deliverable indica il 6 ottobre 2026 come data in cui l'utenza ha scaricato il prospetto della marginalità.
Pass se    compare la data «6 ottobre 2026» riferita al download del prospetto
Fail se    è indicata una data diversa, oppure la data non compare.
Indifferente  l'indicazione dell'orario.

*metadati non forniti al judge* - fonte: 06_log_accessi_data_room.csv; gravita: alta; instradamento: verifica meccanica

**C.2 numerosità della classe D**  [issue: I-09] [tipo: valore]

Verifica   Il deliverable indica in quattro il numero dei clienti che compongono la classe D.
Pass se    compare, riferito alla classe D, il numero «quattro clienti»
Fail se    è indicato un numero diverso, oppure la numerosità della classe non compare.
Indifferente  l'elenco delle denominazioni dei quattro clienti.

*metadati non forniti al judge* - fonte: 03_data_request_list.md, voce 21; gravita: media; instradamento: verifica meccanica

**C.3 confronto fra classe D e convenzione**  [issue: I-09] [tipo: presenza]

Verifica   Il deliverable afferma che la classe D non raggiunge il minimo convenzionale di cinque clienti.
Pass se    compare l'affermazione che la classe D è sotto il minimo di cinque clienti
Fail se    la classe D è presentata come conforme alla convenzione, oppure il confronto non compare.
Indifferente  il richiamo alla numerosità delle altre tre classi.

*metadati non forniti al judge* - fonte: punto 4.2 del term sheet; voce 21 di 03_data_request_list.md; gravita: media; instradamento: judge

**C.4 derivazione errata sul numero delle classi**  [issue: I-09] [tipo: assenza]

Verifica   Il deliverable non giustifica la conformità della classe D con il numero delle classi concordate.
Pass se    Il deliverable non giustifica la conformità della classe D con il numero delle classi concordate.
Fail se    la conformità della classe D è fatta derivare dal fatto che il term sheet concorda quattro classi di restituzione.
Indifferente  il richiamo al punto 4.3 del term sheet in altra funzione.

*metadati non forniti al judge* - fonte: punto 4.3 del term sheet; gravita: media; instradamento: judge

**C.5 fatturato aggregato realizzato in Italia**  [issue: I-16] [tipo: valore]

Verifica   Il deliverable indica in 349.800.000 euro il fatturato realizzato in Italia dall'insieme delle parti.
Pass se    compare l'importo «349.800.000 euro» riferito al fatturato realizzato in Italia dall'insieme delle parti
Fail se    è indicato un importo diverso, oppure l'importo aggregato non compare.
Indifferente  la scelta di indicare anche i due importi individuali.

*metadati non forniti al judge* - fonte: 02_term_sheet_joint_venture.md, Allegato 1; gravita: media; instradamento: verifica meccanica

**C.6 passaggio sulla soglia aggregata**  [issue: I-16] [tipo: presenza]

Verifica   Il deliverable afferma che il fatturato aggregato realizzato in Italia non raggiunge la soglia riferita all'insieme delle imprese interessate.
Pass se    compare l'affermazione che la soglia aggregata non è raggiunta
Fail se    il confronto con la soglia aggregata non compare, oppure è affermato che la soglia è raggiunta.
Indifferente  l'indicazione dell'importo della soglia.

*metadati non forniti al judge* - fonte: art. 16, comma 1, L. 287/1990; gravita: media; instradamento: judge

**C.7 passaggio sulla soglia individuale**  [issue: I-16] [tipo: presenza]

Verifica   Il deliverable afferma che entrambe le parti superano individualmente la soglia riferita ad almeno due delle imprese interessate.
Pass se    compare l'affermazione che entrambe le parti superano la soglia individuale
Fail se    il confronto individuale non compare, oppure è affermato che nessuna delle due la supera.
Indifferente  l'indicazione dell'importo della soglia.

*metadati non forniti al judge* - fonte: art. 16, comma 1, L. 287/1990; gravita: media; instradamento: judge

**C.8 derivazione errata dal fatturato mondiale**  [issue: I-16] [tipo: assenza]

Verifica   Il deliverable non fa derivare l'obbligo o l'assenza di obbligo di comunicazione dal fatturato mondiale aggregato.
Pass se    Il deliverable non fa derivare l'obbligo o l'assenza di obbligo di comunicazione dal fatturato mondiale aggregato.
Fail se    la conclusione sul regime di comunicazione è fatta derivare dal fatturato mondiale aggregato delle parti.
Indifferente  la menzione del fatturato mondiale in relazione al potere di richiesta della notifica.

*metadati non forniti al judge* - fonte: 02_term_sheet_joint_venture.md, Allegato 1; gravita: media; instradamento: judge

**C.9 derivazione errata dalla sola soglia individuale**  [issue: I-16] [tipo: assenza]

Verifica   Il deliverable non fa derivare l'obbligo di comunicazione preventiva dal solo superamento individuale della soglia da parte di entrambe le parti.
Pass se    Il deliverable non fa derivare l'obbligo di comunicazione preventiva dal solo superamento individuale della soglia da parte di entrambe le parti.
Fail se    è affermato che l'obbligo di comunicazione sorge perché entrambe le parti superano la soglia individuale.
Indifferente  l'uso del superamento individuale per fondare il potere di richiesta della notifica.

*metadati non forniti al judge* - fonte: art. 16, commi 1 e 1-bis, L. 287/1990; gravita: media; instradamento: judge
