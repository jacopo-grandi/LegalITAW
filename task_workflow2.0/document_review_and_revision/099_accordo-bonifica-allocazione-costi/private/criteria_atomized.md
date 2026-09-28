# WF2-099 - Criteri atomizzati

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
Pass se    sono presenti remediation_agreement_redline.docx e issue_note.md
Fail se    manca uno dei due file oppure un nome diverge.

*metadati non forniti al judge* - fonte: public/response_template.md; gravita: media; instradamento: verifica meccanica

**A.2 revisioni tracciate nel docx**  [issue: -] [tipo: struttura]

Verifica   Il file docx consegnato contiene almeno una revisione tracciata.
Pass se    il documento contiene almeno un elemento di inserimento o di cancellazione tracciata
Fail se    il documento non contiene alcuna revisione tracciata, oppure le modifiche sono state applicate al testo senza tracciatura.
Indifferente  il numero delle revisioni e la loro formattazione.

*metadati non forniti al judge* - fonte: public/response_template.md; gravita: alta; instradamento: verifica meccanica

**A.3 sezioni della nota**  [issue: -] [tipo: struttura]

Verifica   Il file issue_note.md contiene le sezioni indicate, nell'ordine indicato.
Pass se    le intestazioni compaiono tutte e nella sequenza del response_template
Fail se    manca un'intestazione oppure l'ordine differisce.
Indifferente  la formulazione delle intestazioni oltre le prime ventidue battute.

*metadati non forniti al judge* - fonte: public/response_template.md; gravita: media; instradamento: verifica meccanica

**A.4 data di riferimento**  [issue: -] [tipo: valore]

Verifica   Il deliverable assume come data di riferimento il 9 dicembre 2026.
Pass se    compare «9 dicembre 2026» come data alla quale la nota è riferita
Fail se    è assunta una data diversa, oppure la data di riferimento non compare.
Indifferente  il formato della data.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: alta; instradamento: verifica meccanica

**A.5 clausola indicata per ogni intervento**  [issue: -] [tipo: struttura]

Verifica   Ogni intervento elencato nella nota indica il numero della clausola su cui incide.
Pass se    ciascun intervento riporta il numero della clausola
Fail se    uno o più interventi non indicano la clausola.
Indifferente  la forma dell'indicazione.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: alta; instradamento: verifica meccanica

**A.6 allegato indicato per ogni intervento**  [issue: -] [tipo: struttura]

Verifica   Ogni intervento elencato nella nota indica almeno un allegato del fascicolo.
Pass se    ciascun intervento riporta il nome di almeno un allegato
Fail se    uno o più interventi non riportano alcun allegato.
Indifferente  il numero degli allegati citati per intervento.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: alta; instradamento: verifica meccanica

**A.7 posizione minima per ogni intervento**  [issue: -] [tipo: struttura]

Verifica   Ogni intervento elencato nella nota indica la posizione minima proposta.
Pass se    ciascun intervento riporta la posizione minima
Fail se    uno o più interventi non riportano alcuna posizione minima.
Indifferente  il livello di dettaglio della posizione minima.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: alta; instradamento: verifica meccanica

**A.8 riferimenti entro l'elenco chiuso**  [issue: -] [tipo: assenza]

Verifica   Il deliverable non cita norme assenti dal reference pack.
Pass se    Il deliverable non cita norme assenti dal reference pack.
Fail se    compare un riferimento a un atto o a un articolo che non figura in public/02_reference_pack.md.
Indifferente  la scelta di non citare alcuna fonte in un singolo intervento.

*metadati non forniti al judge* - fonte: public/02_reference_pack.md e private/fonti_chiuse.json; gravita: alta; instradamento: verifica meccanica

**A.9 limite di parole**  [issue: -] [tipo: struttura]

Verifica   Il file issue_note.md resta entro il limite di parole.
Pass se    il conteggio delle parole non supera 2100
Fail se    il conteggio supera il limite.

*metadati non forniti al judge* - fonte: public/response_template.md; gravita: bassa; instradamento: verifica meccanica


## Sezione B - merito

Stato del fascicolo alla data di riferimento: bozza dell'accordo circolata dai legali del proponente e non negoziata; sottoscrizione prevista per il 15 dicembre 2026 e non avvenuta; progetto operativo approvato e lavori non avviati; nessuna ordinanza né diffida notificata alla proprietaria

**B.1 perimetro degli interventi**  [issue: I-01] [tipo: presenza]

Verifica   Il deliverable interviene sulla clausola 2.1 identificando il provvedimento di approvazione e comprendendo nel perimetro le attività prescritte dall'autorità in corso d'opera.
Pass se    la clausola 2.1 è modificata con l'identificazione del provvedimento e con l'estensione alle prescrizioni sopravvenute
Fail se    la clausola 2.1 non è modificata, oppure è modificata senza estendere il perimetro alle prescrizioni sopravvenute.
Indifferente  il modo in cui il provvedimento è identificato.

*metadati non forniti al judge* - fonte: 01_bozza_accordo_bonifica.docx, clausola 2.1; gravita: media; instradamento: judge

**B.2 vincolo di risultato sullo standard di bonifica**  [issue: I-02] [tipo: presenza]

Verifica   Il deliverable interviene sulla clausola 3.3 vincolando la scelta dell'alternativa tecnica al conseguimento degli obiettivi di bonifica fissati dal progetto approvato.
Pass se    la clausola 3.3 è modificata ancorando la scelta agli obiettivi di bonifica
Fail se    la facoltà di scelta è soppressa, oppure la clausola non è modificata, oppure la scelta resta ancorata alla sola conformità alla normativa.
Indifferente  la previsione di una comunicazione preventiva della scelta.

*metadati non forniti al judge* - fonte: 01_bozza_accordo_bonifica.docx, clausola 3.3; 02_decreto_regionale_approvazione_progetto.md, punto 3; gravita: alta; instradamento: judge

**B.3 obiettivi di bonifica da acquisire**  [issue: I-03] [tipo: presenza]

Verifica   Il deliverable indica che il documento di analisi di rischio o gli elaborati che contengono gli obiettivi di bonifica non sono nel fascicolo e vanno acquisiti prima della sottoscrizione.
Pass se    compaiono l'indicazione della documentazione mancante e la richiesta di acquisirla prima della firma
Fail se    la lacuna non è indicata, oppure è dichiarata l'impossibilità di formulare il vincolo di risultato senza indicare quale documento serve.
Indifferente  il modo in cui la documentazione è denominata.

*metadati non forniti al judge* - fonte: 06_nota_del_consulente.md, punti 4.1 e 4.2; gravita: alta; instradamento: judge

**B.4 accertamento del completamento**  [issue: I-04] [tipo: attribuzione]

Verifica   Il deliverable riconduce l'accertamento del completamento degli interventi e della loro conformità al progetto approvato alla certificazione della provincia, resa sulla base della relazione tecnica dell'agenzia regionale.
Pass se    compare l'affermazione che il completamento è accertato dalla provincia sulla base della relazione tecnica dell'agenzia regionale
Fail se    l'accertamento è ricondotto al proponente, al suo consulente, all'agenzia regionale da sola o alla regione.
Indifferente  il richiamo all'effetto della certificazione sullo svincolo delle garanzie.

*metadati non forniti al judge* - fonte: art. 248, comma 2, del codice dell'ambiente; gravita: alta; instradamento: judge

**B.5 intervento sulla definizione di completamento**  [issue: I-04] [tipo: presenza]

Verifica   Il deliverable interviene sulla clausola 2.2 sostituendo la comunicazione del proponente con la certificazione dell'autorità.
Pass se    la clausola 2.2 è modificata ancorando il completamento alla certificazione
Fail se    la clausola 2.2 non è modificata.
Indifferente  la formulazione con cui la certificazione è richiamata.

*metadati non forniti al judge* - fonte: 01_bozza_accordo_bonifica.docx, clausola 2.2; gravita: alta; instradamento: judge

**B.6 esposizione della proprietaria oltre l'alea**  [issue: I-05] [tipo: presenza]

Verifica   Il deliverable afferma che la clausola 4.3 pone a carico della proprietaria l'intera eccedenza oltre la somma di costo base e alea, senza alcun limite di importo, e che quell'esposizione non è quantificabile sul fascicolo.
Pass se    compaiono l'assenza di limite e l'indicazione che l'importo non è quantificabile
Fail se    l'esposizione è presentata come coperta dall'alea, oppure è quantificata in un importo determinato.
Indifferente  il richiamo alle voci escluse dal computo metrico.

*metadati non forniti al judge* - fonte: 01_bozza_accordo_bonifica.docx, clausole 4.3 e 4.4; 03_computo_metrico.md; gravita: alta; instradamento: judge

**B.7 imputazione dell'eccedenza**  [issue: I-06] [tipo: presenza]

Verifica   Il deliverable interviene sulla clausola 4.3 ponendo l'eccedenza a carico del proponente salvo previa approvazione scritta della proprietaria.
Pass se    la clausola 4.3 è modificata invertendo l'imputazione e subordinandola all'approvazione preventiva
Fail se    la clausola 4.3 non è modificata, oppure l'eccedenza resta a carico della proprietaria con un tetto di importo.
Indifferente  il contenuto richiesto alla richiesta di approvazione.

*metadati non forniti al judge* - fonte: 01_bozza_accordo_bonifica.docx, clausola 4.3; gravita: alta; instradamento: judge

**B.8 comunicazione e rendiconto sui costi**  [issue: I-06] [tipo: presenza]

Verifica   Il deliverable interviene sulla clausola 4.4 introducendo l'obbligo di comunicare le circostanze da cui possa derivare il superamento e un rendiconto periodico sull'andamento dei costi.
Pass se    la clausola 4.4 è modificata con l'obbligo di comunicazione e con il rendiconto periodico
Fail se    la clausola 4.4 non è modificata, oppure è modificata introducendo uno solo dei due obblighi.
Indifferente  la periodicità proposta per il rendiconto.

*metadati non forniti al judge* - fonte: 01_bozza_accordo_bonifica.docx, clausola 4.4; gravita: alta; instradamento: judge

**B.9 assenza del termine di ultimazione**  [issue: I-07] [tipo: presenza]

Verifica   Il deliverable afferma che l'accordo fissa il solo termine di avvio e non contiene alcun termine di ultimazione, mentre il decreto lo fissa.
Pass se    compare il confronto fra l'accordo, privo del termine di ultimazione, e il decreto che lo contiene
Fail se    è affermato che l'accordo contiene un termine di ultimazione, oppure il confronto non compare.
Indifferente  l'indicazione della durata fissata dal decreto.

*metadati non forniti al judge* - fonte: 01_bozza_accordo_bonifica.docx, clausole 5.1 e 5.2; 02_decreto_regionale_approvazione_progetto.md, punto 4; gravita: alta; instradamento: judge

**B.10 recepimento del termine e proroghe**  [issue: I-07] [tipo: presenza]

Verifica   Il deliverable interviene sulla clausola 5.2 recependo il termine di ultimazione fissato dal decreto e disciplinando le proroghe per le sospensioni disposte dall'autorità e per le circostanze non imputabili al proponente.
Pass se    la clausola 5.2 è modificata con il termine del decreto e con la disciplina delle proroghe
Fail se    la clausola 5.2 non è modificata, oppure è modificata introducendo un termine convenzionale diverso da quello del decreto.
Indifferente  la previsione di un rendiconto sugli scostamenti.

*metadati non forniti al judge* - fonte: 01_bozza_accordo_bonifica.docx, clausola 5.2; gravita: alta; instradamento: judge

**B.11 disciplina dell'accesso**  [issue: I-08] [tipo: presenza]

Verifica   Il deliverable interviene sulla clausola 6.1 circoscrivendo l'accesso alle aree interessate e subordinandolo a preavviso e a orari, con salvezza dell'emergenza e con la previsione che il diniego motivato da ragioni di sicurezza non costituisce inadempimento della proprietaria.
Pass se    la clausola 6.1 è modificata con perimetro, preavviso, orari e le due salvezze
Fail se    il diritto di accesso è soppresso, oppure la clausola non è modificata, oppure manca una delle due salvezze.
Indifferente  la durata del preavviso proposto.

*metadati non forniti al judge* - fonte: 01_bozza_accordo_bonifica.docx, clausola 6.1; gravita: media; instradamento: judge

**B.12 obblighi e facoltà di legge della proprietaria**  [issue: I-09] [tipo: presenza]

Verifica   Il deliverable afferma che il proprietario dell'area che rilevi il superamento o il pericolo concreto e attuale del superamento delle soglie di contaminazione deve darne comunicazione alle amministrazioni competenti e attuare le misure di prevenzione, e che conserva la facoltà di intervenire volontariamente.
Pass se    compaiono sia l'obbligo di comunicazione e di misure di prevenzione sia la facoltà di intervento volontario
Fail se    è indicato uno solo dei due profili, oppure alla proprietaria è attribuito un obbligo di bonifica.
Indifferente  l'indicazione delle amministrazioni destinatarie della comunicazione.

*metadati non forniti al judge* - fonte: art. 245, commi 1 e 2, del codice dell'ambiente; gravita: alta; instradamento: judge

**B.13 intervento sul divieto di comunicare con l'autorità**  [issue: I-09] [tipo: presenza]

Verifica   Il deliverable interviene sulla clausola 7.2 facendo salvi gli obblighi e la facoltà di legge e mantenendo l'obbligo di trasmissione delle comunicazioni ricevute.
Pass se    la clausola 7.2 è modificata facendo salvi gli obblighi e la facoltà di legge
Fail se    la clausola 7.2 è soppressa integralmente, oppure non è modificata.
Indifferente  la formulazione della salvezza.

*metadati non forniti al judge* - fonte: 01_bozza_accordo_bonifica.docx, clausola 7.2; gravita: alta; instradamento: judge

**B.14 partecipazione ai rapporti con l'autorità**  [issue: I-10] [tipo: presenza]

Verifica   Il deliverable interviene introducendo il diritto della proprietaria di conoscere in anticipo le istanze e le comunicazioni del proponente all'autorità e di far assistere un proprio rappresentante agli incontri.
Pass se    il diritto di preventiva conoscenza e di presenza compare nel testo modificato
Fail se    nessun intervento è previsto sui rapporti con l'autorità, oppure è chiesto di sottrarre al proponente la titolarità di quei rapporti.
Indifferente  il preavviso proposto.

*metadati non forniti al judge* - fonte: 01_bozza_accordo_bonifica.docx, clausola 7.1; gravita: media; instradamento: judge

**B.15 contaminazione sopravvenuta**  [issue: I-11] [tipo: presenza]

Verifica   Il deliverable interviene sulla clausola 8.1 ponendo gli oneri a carico del proponente per le sostanze appartenenti alle classi analitiche già riscontrate negli elaborati, con onere di provare il contrario a suo carico.
Pass se    la clausola 8.1 è modificata con il criterio delle classi analitiche e con l'onere della prova a carico del proponente
Fail se    la clausola 8.1 non è modificata, oppure ogni contaminazione sopravvenuta è addossata al proponente senza distinguere le classi analitiche.
Indifferente  il richiamo alla riserva contenuta nel verbale di restituzione.

*metadati non forniti al judge* - fonte: 01_bozza_accordo_bonifica.docx, clausole 2.5 e 8.1; gravita: alta; instradamento: judge

**B.16 condizione e delimitazione della rinuncia**  [issue: I-12] [tipo: presenza]

Verifica   Il deliverable interviene sulla clausola 9.1 differendo l'efficacia della rinuncia al rilascio della certificazione e facendo salvo il diritto di rivalsa nel caso in cui sia la proprietaria a provvedere alla bonifica.
Pass se    la clausola 9.1 è modificata differendo la rinuncia alla certificazione e facendo salvo il diritto di rivalsa
Fail se    la rinuncia è soppressa, oppure la clausola non è modificata, oppure il differimento è introdotto senza salvezza della rivalsa.
Indifferente  la delimitazione della rinuncia alle matrici e alle aree certificate.

*metadati non forniti al judge* - fonte: 01_bozza_accordo_bonifica.docx, clausola 9.1; art. 253, comma 4, del codice dell'ambiente; gravita: alta; instradamento: judge

**B.17 garanzia finanziaria a favore della proprietaria**  [issue: I-13] [tipo: presenza]

Verifica   Il deliverable interviene introducendo una garanzia a favore della proprietaria, commisurata alla somma di costo base e alea, con indicazione del momento dello svincolo, e la tiene distinta dalle garanzie prestate in favore della regione.
Pass se    la garanzia compare nel testo modificato con importo di riferimento, momento dello svincolo e distinzione dalle garanzie verso la regione
Fail se    nessuna garanzia è introdotta, oppure è introdotta senza distinguerla da quelle prestate in favore della regione, oppure senza indicare il momento dello svincolo.
Indifferente  la forma della garanzia proposta.

*metadati non forniti al judge* - fonte: 01_bozza_accordo_bonifica.docx, clausola 4; 02_decreto_regionale_approvazione_progetto.md, punto 7; gravita: alta; instradamento: judge

**B.18 termine di avvio decorso e collocazione dell'intervento**  [issue: I-14] [tipo: presenza]

Verifica   Il deliverable rileva che il termine di avvio dei lavori fissato dal decreto è decorso e che nessun cantiere è stato allestito, e colloca il relativo intervento fra le azioni che non passano dal testo dell'accordo.
Pass se    compaiono il rilievo del termine decorso e la collocazione dell'intervento fra le azioni esterne al testo
Fail se    il termine è presentato come pendente, il rilievo non compare, oppure l'intervento è presentato come modifica di una clausola dell'accordo.
Indifferente  la forma proposta per l'azione.

*metadati non forniti al judge* - fonte: 02_decreto_regionale_approvazione_progetto.md, punto 5 e relata di notifica; 06_nota_del_consulente.md, punto 3; gravita: alta; instradamento: judge

**B.19 sovra-segnalazione - misura dell'alea**  [issue: N-01] [tipo: assenza]

Verifica   Il deliverable non chiede la soppressione né la riduzione della misura dell'alea.
Pass se    Il deliverable non chiede la soppressione né la riduzione della misura dell'alea.
Fail se    è chiesta la soppressione dell'alea o la riduzione della sua percentuale, oppure la misura dell'alea è indicata fra i difetti dell'assetto economico.
Indifferente  la menzione della misura dell'alea per osservare che resta a carico del proponente.

*metadati non forniti al judge* - fonte: 01_bozza_accordo_bonifica.docx, clausole 2.4 e 4.2; gravita: alta; instradamento: judge

**B.20 sovra-segnalazione - scelta dell'appaltatore**  [issue: N-02] [tipo: assenza]

Verifica   Il deliverable non indica la scelta dell'appaltatore fra gli interventi da chiedere.
Pass se    Il deliverable non indica la scelta dell'appaltatore fra gli interventi da chiedere.
Fail se    è chiesto di individuare l'appaltatore, di subordinarne la scelta al consenso della proprietaria o di verificarne l'iscrizione come condizione della sottoscrizione.
Indifferente  la menzione dell'appaltatore fra gli elementi già individuati dalla bozza, o l'indicazione del provvedimento di iscrizione fra la documentazione da acquisire.

*metadati non forniti al judge* - fonte: 01_bozza_accordo_bonifica.docx, clausola 3.2; gravita: media; instradamento: judge

**B.21 sovra-segnalazione - esclusione del lucro cessante**  [issue: N-03] [tipo: assenza]

Verifica   Il deliverable non chiede di sopprimere né di rendere unilaterale l'esclusione del lucro cessante.
Pass se    Il deliverable non chiede di sopprimere né di rendere unilaterale l'esclusione del lucro cessante.
Fail se    è chiesta la soppressione della clausola 10.1 o la sua limitazione a una sola delle parti.
Indifferente  la menzione della clausola 10.1 per osservare che opera in modo reciproco e non incide sugli oneri di bonifica.

*metadati non forniti al judge* - fonte: 01_bozza_accordo_bonifica.docx, clausola 10.1; gravita: media; instradamento: judge

**B.22 simmetria del controllo - clausole favorevoli alla proprietaria**  [issue: -] [tipo: assenza]

Verifica   Il deliverable non omette le clausole della bozza che operano a favore della proprietaria.
Pass se    Il deliverable non omette le clausole della bozza che operano a favore della proprietaria.
Fail se    non compare alcuna delle clausole favorevoli, quali l'imputazione integrale del costo base e dell'alea al proponente, l'assunzione da parte del proponente delle spese tecniche e di collaudo, l'indennità per le sanzioni amministrative o la reciprocità dell'esclusione dei danni indiretti.
Indifferente  quali fra queste clausole sono richiamate, purché ne compaia almeno una.

*metadati non forniti al judge* - fonte: private/challenge_map.json, controlled non-issue; gravita: media; instradamento: judge

**B.23 presunzione dell'esito - accettazione delle richieste**  [issue: -] [tipo: assenza]

Verifica   Il deliverable non presenta come acquisita l'accettazione delle richieste da parte del proponente.
Pass se    Il deliverable non presenta come acquisita l'accettazione delle richieste da parte del proponente.
Fail se    è affermato che il proponente accetterà gli interventi proposti, o che la sottoscrizione avverrà alle condizioni modificate.
Indifferente  l'indicazione della posizione minima per ciascun intervento.

*metadati non forniti al judge* - fonte: private/challenge_map.json, dati mancanti; gravita: alta; instradamento: judge


## Sezione C - date e valori calcolati

**C.1 costo base degli interventi**  [issue: I-05] [tipo: valore]

Verifica   Il deliverable indica in 740.000 euro il costo base risultante dal computo metrico.
Pass se    compare l'importo «740.000» riferito al costo base
Fail se    è indicato un importo diverso, oppure il costo base non compare.
Indifferente  il modo in cui l'importo è scritto.

*metadati non forniti al judge* - fonte: 03_computo_metrico.md; gravita: alta; instradamento: verifica meccanica

**C.2 misura dell'alea**  [issue: I-05] [tipo: valore]

Verifica   Il deliverable indica in 111.000 euro l'alea a carico del proponente.
Pass se    compare l'importo «111.000» riferito all'alea
Fail se    è indicato un importo diverso, oppure l'alea non è quantificata.
Indifferente  l'indicazione della percentuale accanto all'importo.

*metadati non forniti al judge* - fonte: quadratura fra clausole 2.4 e 4.2 e 03_computo_metrico.md; gravita: media; instradamento: verifica meccanica

**C.3 soglia oltre la quale l'eccedenza è a carico della proprietaria**  [issue: I-05] [tipo: valore]

Verifica   Il deliverable indica in 851.000 euro la somma di costo base e alea, oltre la quale la bozza pone l'eccedenza a carico della proprietaria.
Pass se    compare l'importo «851.000» riferito alla somma di costo base e alea
Fail se    è indicato un importo diverso, oppure la somma non è calcolata.
Indifferente  il modo in cui l'importo è scritto.

*metadati non forniti al judge* - fonte: quadratura fra clausole 2.4, 4.2 e 4.3 e 03_computo_metrico.md; gravita: alta; instradamento: verifica meccanica

**C.4 termine di avvio dei lavori**  [issue: I-14] [tipo: valore]

Verifica   Il deliverable indica il 27 ottobre 2026 come termine entro cui i lavori andavano avviati.
Pass se    compare la data «27 ottobre 2026» riferita al termine di avvio dei lavori
Fail se    è indicata una data diversa, oppure il termine non è calcolato.
Indifferente  l'indicazione dei giorni di ritardo.

*metadati non forniti al judge* - fonte: 02_decreto_regionale_approvazione_progetto.md, punto 5 e relata di notifica; gravita: alta; instradamento: verifica meccanica

**C.5 derivazione errata dalla data del decreto**  [issue: I-14] [tipo: assenza]

Verifica   Il deliverable non computa il termine di avvio dei lavori dalla data del decreto.
Pass se    Il deliverable non computa il termine di avvio dei lavori dalla data del decreto.
Fail se    compare la data «20 ottobre 2026» come termine di avvio dei lavori, oppure i novanta giorni sono computati dalla data del decreto anziché dalla data della sua notifica.
Indifferente  la menzione della data del decreto in altra funzione.

*metadati non forniti al judge* - fonte: derivazione da escludere; gravita: alta; instradamento: judge
