# WF2-098 - Criteri atomizzati

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
Pass se    sono presenti environmental_schedule_redline.docx e note.md
Fail se    manca uno dei due file oppure un nome diverge.

*metadati non forniti al judge* - fonte: public/response_template.md; gravita: media; instradamento: verifica meccanica

**A.2 revisioni tracciate nel docx**  [issue: -] [tipo: struttura]

Verifica   Il file docx consegnato contiene almeno una revisione tracciata.
Pass se    il documento contiene almeno un elemento di inserimento o di cancellazione tracciata
Fail se    il documento non contiene alcuna revisione tracciata, oppure le modifiche sono state applicate al testo senza tracciatura.
Indifferente  il numero delle revisioni e la loro formattazione.

*metadati non forniti al judge* - fonte: public/response_template.md; gravita: alta; instradamento: verifica meccanica

**A.3 sezioni della nota**  [issue: -] [tipo: struttura]

Verifica   Il file note.md contiene le sezioni indicate, nell'ordine indicato.
Pass se    le intestazioni compaiono tutte e nella sequenza del response_template
Fail se    manca un'intestazione oppure l'ordine differisce.
Indifferente  la formulazione delle intestazioni oltre le prime ventidue battute.

*metadati non forniti al judge* - fonte: public/response_template.md; gravita: media; instradamento: verifica meccanica

**A.4 data di riferimento**  [issue: -] [tipo: valore]

Verifica   Il deliverable assume come data di riferimento il 18 novembre 2026.
Pass se    compare «18 novembre 2026» come data alla quale la nota è riferita
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

**A.8 distinzione fra interventi sul testo e azioni esterne**  [issue: -] [tipo: struttura]

Verifica   La nota tiene distinti gli interventi sul testo dell'Allegato dalle azioni che non passano dal testo.
Pass se    le due categorie sono trattate in sezioni separate
Fail se    le azioni esterne al testo sono elencate insieme agli interventi sulle clausole.
Indifferente  l'ordine interno a ciascuna categoria.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: alta; instradamento: verifica meccanica

**A.9 riferimenti entro l'elenco chiuso**  [issue: -] [tipo: assenza]

Verifica   Il deliverable non cita norme assenti dal reference pack.
Pass se    Il deliverable non cita norme assenti dal reference pack.
Fail se    compare un riferimento a un atto o a un articolo che non figura in public/02_reference_pack.md.
Indifferente  la scelta di non citare alcuna fonte in un singolo intervento.

*metadati non forniti al judge* - fonte: public/02_reference_pack.md e private/fonti_chiuse.json; gravita: alta; instradamento: verifica meccanica

**A.10 limite di parole**  [issue: -] [tipo: struttura]

Verifica   Il file note.md resta entro il limite di parole.
Pass se    il conteggio delle parole non supera 2600
Fail se    il conteggio supera il limite.

*metadati non forniti al judge* - fonte: public/response_template.md; gravita: bassa; instradamento: verifica meccanica


## Sezione B - merito

Stato del fascicolo alla data di riferimento: bozza dell'Allegato 7 circolata dai legali del cedente e non negoziata; closing previsto per il 15 dicembre 2026 e non ancora avvenuto; interventi di bonifica approvati e non avviati; nessuna pretesa avanzata

**B.1 insufficienza del massimale**  [issue: I-01] [tipo: presenza]

Verifica   Il deliverable afferma che il massimale della clausola 3.2 non copre l'esposizione documentata.
Pass se    compare l'affermazione che il massimale è inferiore all'esposizione documentata
Fail se    è affermato che l'esposizione è coperta, oppure il confronto non compare.
Indifferente  il modo in cui la differenza è espressa.

*metadati non forniti al judge* - fonte: 01_bozza_schedule_ambientale.docx, clausola 3.2; 04_stima_oneri_ambientali.md; gravita: alta; instradamento: judge

**B.2 autonomia dei due massimali**  [issue: I-01] [tipo: attribuzione]

Verifica   Il deliverable riconduce le perdite ambientali al solo massimale della clausola 3.2 dell'Allegato.
Pass se    compare l'affermazione che il massimale generale del contratto non copre le perdite ambientali
Fail se    i due massimali sono sommati, oppure il massimale generale è indicato come applicabile anche alle perdite ambientali.
Indifferente  il richiamo all'importo del massimale generale.

*metadati non forniti al judge* - fonte: 02_bozza_contratto_cessione_ramo.md, clausole 5.2 e 5.4; gravita: alta; instradamento: judge

**B.3 intervento sul massimale**  [issue: I-01] [tipo: presenza]

Verifica   Il deliverable interviene sulla clausola 3.2 elevando il massimale all'esposizione documentata oppure escludendo dal computo del massimale le voci di costo stimate.
Pass se    la clausola 3.2 è modificata in uno dei due modi
Fail se    la clausola 3.2 non è modificata.
Indifferente  quale dei due modi è scelto.

*metadati non forniti al judge* - fonte: 01_bozza_schedule_ambientale.docx, clausola 3.2; gravita: alta; instradamento: judge

**B.4 durata della garanzia contro durata degli adempimenti**  [issue: I-02] [tipo: presenza]

Verifica   Il deliverable afferma che la garanzia ambientale si estingue prima della conclusione degli adempimenti di monitoraggio prescritti.
Pass se    compare il confronto fra la scadenza della garanzia e la durata del monitoraggio
Fail se    la durata di ventiquattro mesi è accettata senza confronto con la durata degli adempimenti.
Indifferente  il modo in cui il confronto è espresso.

*metadati non forniti al judge* - fonte: 01_bozza_schedule_ambientale.docx, clausola 3.4; 05_provvedimento_regionale_approvazione_progetto.md, punto 3; gravita: alta; instradamento: judge

**B.5 intervento sulla durata**  [issue: I-02] [tipo: presenza]

Verifica   Il deliverable interviene sulla clausola 3.4 estendendo la durata della garanzia ambientale e ancorandola alla scadenza dell'ultimo adempimento di monitoraggio.
Pass se    la clausola 3.4 è modificata estendendo la durata e ancorandola agli adempimenti
Fail se    la clausola 3.4 non è modificata, oppure è modificata indicando una durata fissa senza ancoraggio agli adempimenti.
Indifferente  la durata numerica proposta.

*metadati non forniti al judge* - fonte: 01_bozza_schedule_ambientale.docx, clausola 3.4; gravita: alta; instradamento: judge

**B.6 effetto della informativa generale**  [issue: I-03] [tipo: presenza]

Verifica   Il deliverable afferma che la clausola 6.1, combinata con la disclosure letter, esclude la garanzia sulle condizioni ambientali documentate.
Pass se    compare l'affermazione che l'informativa generale svuota la manleva sulle voci documentate
Fail se    la clausola 6.1 è trattata come formula di stile, oppure il collegamento con la disclosure letter non compare.
Indifferente  il richiamo al punto della disclosure letter.

*metadati non forniti al judge* - fonte: 01_bozza_schedule_ambientale.docx, clausola 6.1; 06_disclosure_letter.md; gravita: alta; instradamento: judge

**B.7 intervento sull'informativa generale**  [issue: I-03] [tipo: presenza]

Verifica   Il deliverable interviene sulla clausola 6.1 limitando l'effetto all'informativa specifica e facendo salva la copertura delle condizioni ambientali descritte nella relazione di due diligence.
Pass se    la clausola 6.1 è modificata limitando l'effetto e facendo salve le condizioni documentate
Fail se    la clausola 6.1 non è modificata, oppure è modificata senza fare salve le condizioni documentate.
Indifferente  la formulazione con cui il limite è espresso.

*metadati non forniti al judge* - fonte: 01_bozza_schedule_ambientale.docx, clausola 6.1; gravita: alta; instradamento: judge

**B.8 non omogeneità delle due campagne**  [issue: I-04] [tipo: presenza]

Verifica   Il deliverable afferma che la relazione di due diligence contiene due campagne analitiche con punti di indagine non coincidenti.
Pass se    compare l'affermazione che le due campagne non sono omogenee sull'intero set di punti
Fail se    le due campagne sono trattate come un unico set, oppure il punto non è trattato.
Indifferente  l'indicazione dei punti aggiunti nella campagna integrativa.

*metadati non forniti al judge* - fonte: 03_relazione_due_diligence_ambientale.md, tabelle 3 e 4; gravita: alta; instradamento: judge

**B.9 intervento sullo stato di riferimento**  [issue: I-04] [tipo: presenza]

Verifica   Il deliverable interviene sulla clausola 1.5 identificando la relazione per data e indicando il set analitico che costituisce lo stato di riferimento.
Pass se    la clausola 1.5 è modificata con l'indicazione della data della relazione e del set analitico
Fail se    la clausola 1.5 non è modificata, oppure è modificata senza indicare il set analitico.
Indifferente  il modo in cui il set analitico è individuato.

*metadati non forniti al judge* - fonte: 01_bozza_schedule_ambientale.docx, clausola 1.5; gravita: alta; instradamento: judge

**B.10 accertamento del completamento**  [issue: I-05] [tipo: attribuzione]

Verifica   Il deliverable riconduce l'accertamento del completamento degli interventi e della loro conformità al progetto approvato alla certificazione della provincia, resa sulla base della relazione tecnica dell'agenzia regionale.
Pass se    compare l'affermazione che il completamento è accertato dalla provincia sulla base della relazione tecnica dell'agenzia regionale
Fail se    l'accertamento è ricondotto al consulente del cedente, all'agenzia regionale da sola o alla regione.
Indifferente  il richiamo all'effetto della certificazione sullo svincolo delle garanzie.

*metadati non forniti al judge* - fonte: art. 248, comma 2, del codice dell'ambiente; gravita: alta; instradamento: judge

**B.11 intervento sulla definizione di completamento**  [issue: I-05] [tipo: presenza]

Verifica   Il deliverable interviene sulla clausola 1.7 sostituendo la comunicazione del consulente con la certificazione dell'autorità.
Pass se    la clausola 1.7 è modificata ancorando il completamento alla certificazione
Fail se    la clausola 1.7 non è modificata.
Indifferente  la formulazione con cui la certificazione è richiamata.

*metadati non forniti al judge* - fonte: 01_bozza_schedule_ambientale.docx, clausola 1.7; gravita: alta; instradamento: judge

**B.12 criterio di imputazione temporale**  [issue: I-06] [tipo: presenza]

Verifica   Il deliverable interviene sulla clausola 1.8 sostituendo il criterio della causazione da parte del cedente con quello della presenza della condizione ambientale alla data del closing.
Pass se    la clausola 1.8 è modificata sostituendo la causazione con la presenza alla data del closing
Fail se    la clausola 1.8 non è modificata, oppure il criterio della causazione è mantenuto.
Indifferente  l'eventuale estensione alla migrazione dai fondi limitrofi.

*metadati non forniti al judge* - fonte: 01_bozza_schedule_ambientale.docx, clausola 1.8; gravita: alta; instradamento: judge

**B.13 onere della prova**  [issue: I-06] [tipo: presenza]

Verifica   Il deliverable interviene sulla clausola 3.1 spostando sul cedente l'onere della prova per le classi analitiche già riscontrate nello stato di riferimento.
Pass se    la clausola 3.1 è modificata spostando l'onere della prova sul cedente
Fail se    la clausola 3.1 non è modificata, oppure l'onere resta a carico del cessionario.
Indifferente  il modo in cui le classi analitiche sono individuate.

*metadati non forniti al judge* - fonte: 01_bozza_schedule_ambientale.docx, clausola 3.1; gravita: alta; instradamento: judge

**B.14 migrazione dai fondi limitrofi**  [issue: I-07] [tipo: presenza]

Verifica   Il deliverable rileva che l'allegato non disciplina la migrazione di sostanze pericolose dai fondi limitrofi e vi interviene.
Pass se    il rilievo compare e una clausola è modificata o inserita per disciplinare la migrazione
Fail se    il rilievo non compare, oppure non è accompagnato da alcun intervento sul testo.
Indifferente  se l'intervento è una modifica o un inserimento.

*metadati non forniti al judge* - fonte: 03_relazione_due_diligence_ambientale.md, punto 5; gravita: alta; instradamento: judge

**B.15 condizioni scoperte in corso d'opera**  [issue: I-07] [tipo: presenza]

Verifica   Il deliverable interviene inserendo una disciplina delle condizioni ambientali che emergano da scavi successivi al closing, distinguendo gli scavi imposti dall'autorità o dalla normativa da quelli scelti dal cessionario.
Pass se    la distinzione fra scavi imposti e scavi scelti compare nel testo modificato
Fail se    nessuna disciplina delle condizioni scoperte in corso d'opera è inserita, oppure è inserita senza la distinzione.
Indifferente  la collocazione della clausola inserita.

*metadati non forniti al judge* - fonte: 04_stima_oneri_ambientali.md, voce 4; gravita: alta; instradamento: judge

**B.16 termine di notifica del claim**  [issue: I-08] [tipo: presenza]

Verifica   Il deliverable interviene sulla clausola 4.1 allungando il termine di notifica.
Pass se    la clausola 4.1 è modificata allungando il termine
Fail se    la clausola 4.1 non è modificata sul termine.
Indifferente  la durata proposta.

*metadati non forniti al judge* - fonte: 01_bozza_schedule_ambientale.docx, clausola 4.1; gravita: alta; instradamento: judge

**B.17 condizione della decadenza**  [issue: I-08] [tipo: presenza]

Verifica   Il deliverable interviene sulla clausola 4.1 subordinando la perdita del diritto all'indennizzo all'esistenza di un pregiudizio effettivo per il cedente e limitandola alla misura di tale pregiudizio.
Pass se    la clausola 4.1 è modificata con la condizione del pregiudizio effettivo
Fail se    la decadenza automatica è mantenuta, oppure l'intervento riguarda la sola durata del termine.
Indifferente  la formulazione della condizione.

*metadati non forniti al judge* - fonte: 01_bozza_schedule_ambientale.docx, clausola 4.1; gravita: alta; instradamento: judge

**B.18 consenso alla definizione della pretesa**  [issue: I-09] [tipo: presenza]

Verifica   Il deliverable interviene sulla clausola 4.2 subordinando la definizione transattiva della pretesa al consenso del cessionario.
Pass se    la clausola 4.2 è modificata introducendo il consenso del cessionario
Fail se    la clausola 4.2 non è modificata.
Indifferente  l'eventuale qualificazione del consenso come non irragionevolmente negabile.

*metadati non forniti al judge* - fonte: 01_bozza_schedule_ambientale.docx, clausola 4.2; gravita: alta; instradamento: judge

**B.19 vincoli che gravano sul sito**  [issue: I-09] [tipo: presenza]

Verifica   Il deliverable collega l'intervento sulla clausola 4.2 all'effetto che prescrizioni, obblighi di monitoraggio o vincoli d'uso concordati dal cedente producono sul sito dopo il completamento.
Pass se    il collegamento con i vincoli che gravano sul sito compare nella nota o nel testo modificato
Fail se    l'intervento è motivato soltanto con l'interesse a partecipare alla trattativa.
Indifferente  il modo in cui i vincoli sono elencati.

*metadati non forniti al judge* - fonte: 01_bozza_schedule_ambientale.docx, clausole 4.2 e 4.4; gravita: alta; instradamento: judge

**B.20 partecipazione ai rapporti con l'autorità**  [issue: I-09] [tipo: presenza]

Verifica   Il deliverable interviene inserendo il diritto del cessionario di conoscere in anticipo le comunicazioni del cedente all'autorità competente e di assistere agli incontri.
Pass se    il diritto di preventiva conoscenza e di presenza compare nel testo modificato
Fail se    nessun intervento è previsto sui rapporti con l'autorità.
Indifferente  il preavviso proposto.

*metadati non forniti al judge* - fonte: 01_bozza_schedule_ambientale.docx, clausola 4; gravita: media; instradamento: judge

**B.21 conflitto fra divieto di contatto e obblighi di legge**  [issue: I-10] [tipo: presenza]

Verifica   Il deliverable afferma che la clausola 4.3 è incompatibile con gli obblighi di comunicazione e di adozione delle misure di prevenzione che la legge pone al proprietario o gestore dell'area.
Pass se    compare l'affermazione dell'incompatibilità con gli obblighi di legge
Fail se    la clausola 4.3 è accettata, oppure il conflitto non è rilevato.
Indifferente  l'indicazione delle amministrazioni destinatarie della comunicazione.

*metadati non forniti al judge* - fonte: art. 245, comma 2, del codice dell'ambiente; gravita: alta; instradamento: judge

**B.22 intervento sul divieto di contatto**  [issue: I-10] [tipo: presenza]

Verifica   Il deliverable interviene sulla clausola 4.3 facendo salvi gli obblighi di legge e mantenendo l'obbligo di trasmissione delle comunicazioni ricevute.
Pass se    la clausola 4.3 è modificata facendo salvi gli obblighi di legge
Fail se    la clausola 4.3 è soppressa integralmente, oppure non è modificata.
Indifferente  la formulazione della salvezza.

*metadati non forniti al judge* - fonte: 01_bozza_schedule_ambientale.docx, clausola 4.3; gravita: alta; instradamento: judge

**B.23 disciplina dell'accesso**  [issue: I-11] [tipo: presenza]

Verifica   Il deliverable interviene sulla clausola 5.1 circoscrivendo l'accesso alle aree interessate e subordinandolo a preavviso e a modalità compatibili con l'attività produttiva.
Pass se    la clausola 5.1 è modificata con perimetro, preavviso e modalità
Fail se    il diritto di accesso è soppresso, oppure la clausola non è modificata.
Indifferente  la durata del preavviso proposto.

*metadati non forniti al judge* - fonte: 01_bozza_schedule_ambientale.docx, clausola 5.1; gravita: media; instradamento: judge

**B.24 salvezza dell'emergenza e del diniego motivato**  [issue: I-11] [tipo: presenza]

Verifica   Il deliverable fa salvo l'accesso senza preavviso nei casi di emergenza e prevede che il diniego di accesso motivato da ragioni di sicurezza non costituisca inadempimento del cessionario.
Pass se    compaiono entrambe le salvezze nel testo modificato
Fail se    nessuna delle due salvezze compare.
Indifferente  l'ordine in cui le due salvezze sono esposte.

*metadati non forniti al judge* - fonte: 01_bozza_schedule_ambientale.docx, clausola 5.1; gravita: media; instradamento: judge

**B.25 divergenza sull'imputazione del monitoraggio**  [issue: I-12] [tipo: presenza]

Verifica   Il deliverable afferma che la clausola 7.1 imputa il monitoraggio al cessionario mentre il decreto regionale lo imputa al cedente.
Pass se    compare l'affermazione della divergenza fra clausola e provvedimento
Fail se    la divergenza non è rilevata, oppure l'imputazione al cessionario è accettata.
Indifferente  il richiamo al punto del decreto.

*metadati non forniti al judge* - fonte: 05_provvedimento_regionale_approvazione_progetto.md, punti 3 e 4; gravita: alta; instradamento: judge

**B.26 intervento sull'imputazione del monitoraggio**  [issue: I-12] [tipo: presenza]

Verifica   Il deliverable interviene sulla clausola 7.1 imputando il monitoraggio al cedente per l'intera durata prescritta.
Pass se    la clausola 7.1 è modificata imputando il monitoraggio al cedente
Fail se    la clausola 7.1 non è modificata.
Indifferente  la previsione dell'accesso ai punti di monitoraggio.

*metadati non forniti al judge* - fonte: 01_bozza_schedule_ambientale.docx, clausola 7.1; gravita: alta; instradamento: judge

**B.27 assenza di garanzia finanziaria**  [issue: I-13] [tipo: presenza]

Verifica   Il deliverable rileva che il corrispettivo è pagato integralmente al closing e che nessuna garanzia finanziaria assiste gli obblighi di manleva.
Pass se    compare il rilievo dell'assenza di garanzia finanziaria a fronte della manleva
Fail se    il rilievo non compare.
Indifferente  il richiamo all'importo del corrispettivo.

*metadati non forniti al judge* - fonte: 02_bozza_contratto_cessione_ramo.md, clausola 3.1; gravita: alta; instradamento: judge

**B.28 intervento sulla garanzia finanziaria**  [issue: I-13] [tipo: presenza]

Verifica   Il deliverable interviene inserendo una garanzia finanziaria a carico del cedente, commisurata all'esposizione stimata e con svincolo progressivo.
Pass se    la garanzia finanziaria compare nel testo modificato con importo di riferimento e meccanismo di svincolo
Fail se    nessuna garanzia è inserita, oppure è inserita senza indicare né la commisurazione né il meccanismo di svincolo.
Indifferente  la forma della garanzia proposta.

*metadati non forniti al judge* - fonte: 01_bozza_schedule_ambientale.docx, clausola 3; gravita: alta; instradamento: judge

**B.29 termine di avvio dei lavori**  [issue: I-14] [tipo: presenza]

Verifica   Il deliverable rileva che il termine per l'avvio dei lavori fissato dal decreto regionale è decorso e che i lavori non risultano avviati.
Pass se    compare il rilievo che il termine è decorso e i lavori non sono avviati
Fail se    il rilievo non compare, oppure il termine è presentato come pendente.
Indifferente  l'indicazione dei giorni di ritardo.

*metadati non forniti al judge* - fonte: 05_provvedimento_regionale_approvazione_progetto.md, punto 6 e relata di notifica; gravita: alta; instradamento: judge

**B.30 collocazione dell'intervento fuori dal testo**  [issue: I-14] [tipo: presenza]

Verifica   Il deliverable colloca l'intervento sul termine di avvio dei lavori fra le azioni che non passano dal testo dell'Allegato.
Pass se    l'intervento compare fra le azioni esterne al testo, come condizione al closing o come richiesta al cedente prima del closing
Fail se    l'intervento è presentato come modifica di una clausola dell'Allegato, oppure non è collocato.
Indifferente  la forma proposta per l'azione.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: alta; instradamento: judge

**B.31 correzione sull'affermazione del ritardo**  [issue: I-14] [tipo: presenza]

Verifica   Il deliverable corregge l'affermazione secondo cui il ritardo nell'avvio dei lavori resta un problema del cedente fino al closing.
Pass se    compare l'affermazione che l'adempimento verso l'autorità riguarda il sito e non si esaurisce con il trasferimento
Fail se    l'affermazione della committente è accolta, oppure il punto non è trattato.
Indifferente  il modo in cui la correzione è formulata.

*metadati non forniti al judge* - fonte: 07_email_responsabile_ma.md; gravita: alta; instradamento: judge

**B.32 sovra-segnalazione - formulazione della franchigia**  [issue: N-01] [tipo: assenza]

Verifica   Il deliverable non presenta la formulazione della franchigia fra gli interventi prioritari.
Pass se    Il deliverable non presenta la formulazione della franchigia fra gli interventi prioritari.
Fail se    la formulazione della franchigia della clausola 3.3 è indicata come intervento prioritario, oppure le è attribuita una perdita di recupero di 150.000 euro sull'esposizione documentata.
Indifferente  la menzione della clausola 3.3 per osservare che sull'esposizione documentata il massimale opera prima della franchigia.

*metadati non forniti al judge* - fonte: 01_bozza_schedule_ambientale.docx, clausola 3.3; gravita: alta; instradamento: judge

**B.33 sovra-segnalazione - modifiche normative successive**  [issue: N-02] [tipo: assenza]

Verifica   Il deliverable non chiede la soppressione dell'esclusione per modifiche normative successive.
Pass se    Il deliverable non chiede la soppressione dell'esclusione per modifiche normative successive.
Fail se    è chiesta la soppressione della clausola 3.5, oppure la clausola è indicata come svuotamento della manleva.
Indifferente  la menzione della clausola 3.5 per osservare che l'avverbio ne circoscrive la portata.

*metadati non forniti al judge* - fonte: 01_bozza_schedule_ambientale.docx, clausola 3.5; gravita: media; instradamento: judge

**B.34 sovra-segnalazione - esclusione del lucro cessante**  [issue: N-03] [tipo: assenza]

Verifica   Il deliverable non indica l'esclusione del lucro cessante fra gli interventi da chiedere.
Pass se    Il deliverable non indica l'esclusione del lucro cessante fra gli interventi da chiedere.
Fail se    è chiesto di estendere la definizione di perdita al lucro cessante o ai danni indiretti.
Indifferente  la menzione della definizione di perdita per osservare che le voci documentate sono danno emergente.

*metadati non forniti al judge* - fonte: 01_bozza_schedule_ambientale.docx, clausola 1.10; gravita: media; instradamento: judge

**B.35 sovra-segnalazione - dichiarazione del cessionario sulle verifiche svolte**  [issue: N-04] [tipo: assenza]

Verifica   Il deliverable non interviene sulla dichiarazione del cessionario sulle verifiche svolte.
Pass se    Il deliverable non interviene sulla dichiarazione del cessionario sulle verifiche svolte.
Fail se    la clausola 6.2 è modificata o soppressa, oppure le è attribuito l'effetto di una rinuncia alle garanzie.
Indifferente  la menzione della clausola 6.2 per distinguerla dalla clausola 6.1.

*metadati non forniti al judge* - fonte: 01_bozza_schedule_ambientale.docx, clausola 6.2; gravita: media; instradamento: judge

**B.36 simmetria del controllo - clausole favorevoli al cessionario**  [issue: -] [tipo: assenza]

Verifica   Il deliverable non omette le clausole della bozza che operano a favore del cessionario.
Pass se    Il deliverable non omette le clausole della bozza che operano a favore del cessionario.
Fail se    non compare alcuna delle clausole favorevoli, quali l'inoperatività delle limitazioni in caso di dolo, l'autonomia del massimale ambientale rispetto a quello generale o l'esclusione delle condizioni determinate da attività del cessionario.
Indifferente  quali fra queste clausole sono richiamate, purché ne compaia almeno una.

*metadati non forniti al judge* - fonte: private/challenge_map.json, controlled non-issue; gravita: media; instradamento: judge

**B.37 presunzione dell'esito - accettazione delle richieste**  [issue: -] [tipo: assenza]

Verifica   Il deliverable non presenta come acquisita l'accettazione delle richieste da parte del cedente.
Pass se    Il deliverable non presenta come acquisita l'accettazione delle richieste da parte del cedente.
Fail se    è affermato che il cedente accetterà gli interventi proposti, o che il closing avverrà alle condizioni modificate.
Indifferente  l'indicazione della posizione minima per ciascun intervento.

*metadati non forniti al judge* - fonte: private/challenge_map.json, dati mancanti; gravita: alta; instradamento: judge


## Sezione C - date e valori calcolati

**C.1 esposizione documentata**  [issue: I-01] [tipo: valore]

Verifica   Il deliverable indica in 2.150.000 euro l'esposizione ambientale documentata.
Pass se    compare l'importo «2.150.000» riferito all'esposizione ambientale documentata
Fail se    è indicato un importo diverso, oppure l'esposizione non è quantificata.
Indifferente  il modo in cui l'importo è scritto.

*metadati non forniti al judge* - fonte: 04_stima_oneri_ambientali.md; gravita: alta; instradamento: verifica meccanica

**C.2 esposizione non coperta**  [issue: I-01] [tipo: valore]

Verifica   Il deliverable indica in 1.250.000 euro la parte dell'esposizione non coperta dal massimale.
Pass se    compare l'importo «1.250.000» riferito alla parte non coperta dal massimale
Fail se    è indicato un importo diverso, oppure la parte non coperta non è quantificata.
Indifferente  il modo in cui l'importo è scritto.

*metadati non forniti al judge* - fonte: quadratura fra clausola 3.2 e 04_stima_oneri_ambientali.md; gravita: alta; instradamento: verifica meccanica

**C.3 derivazione errata dalla somma dei massimali**  [issue: I-01] [tipo: assenza]

Verifica   Il deliverable non somma il massimale generale e quello ambientale.
Pass se    Il deliverable non somma il massimale generale e quello ambientale.
Fail se    compare l'importo «2.350.000» come misura della copertura complessiva, oppure la copertura è calcolata sommando i due massimali.
Indifferente  la menzione dell'importo del massimale generale in altra funzione.

*metadati non forniti al judge* - fonte: derivazione da escludere; gravita: alta; instradamento: judge

**C.4 data di closing**  [issue: I-02] [tipo: valore]

Verifica   Il deliverable indica il 15 dicembre 2026 come data prevista di closing.
Pass se    compare la data «15 dicembre 2026» riferita al closing
Fail se    è indicata una data diversa, oppure la data di closing non compare.
Indifferente  il formato della data.

*metadati non forniti al judge* - fonte: 02_bozza_contratto_cessione_ramo.md, clausola 4.1; gravita: media; instradamento: verifica meccanica

**C.5 scadenza della garanzia ambientale**  [issue: I-02] [tipo: valore]

Verifica   Il deliverable indica il 15 dicembre 2028 come scadenza della garanzia ambientale nella formulazione della bozza.
Pass se    compare la data «15 dicembre 2028» riferita alla scadenza della garanzia ambientale
Fail se    è indicata una data diversa, oppure la scadenza non è calcolata.
Indifferente  l'indicazione del numero di mesi.

*metadati non forniti al judge* - fonte: 01_bozza_schedule_ambientale.docx, clausola 3.4; gravita: alta; instradamento: verifica meccanica

**C.6 termine di avvio dei lavori**  [issue: I-14] [tipo: valore]

Verifica   Il deliverable indica il 25 novembre 2025 come termine entro cui i lavori andavano avviati.
Pass se    compare la data «25 novembre 2025» riferita al termine di avvio dei lavori
Fail se    è indicata una data diversa, oppure il termine non è calcolato.
Indifferente  l'indicazione dei giorni di ritardo.

*metadati non forniti al judge* - fonte: 05_provvedimento_regionale_approvazione_progetto.md, punto 6 e relata di notifica; gravita: alta; instradamento: verifica meccanica

**C.7 costo annuo del monitoraggio**  [issue: I-12] [tipo: valore]

Verifica   Il deliverable indica in 43.000 euro il costo annuo del monitoraggio delle acque sotterranee.
Pass se    compare l'importo «43.000» riferito al costo annuo del monitoraggio
Fail se    è indicato un importo diverso, oppure il costo annuo non è calcolato.
Indifferente  il modo in cui l'importo è scritto.

*metadati non forniti al judge* - fonte: 04_stima_oneri_ambientali.md, voce 3; gravita: media; instradamento: verifica meccanica

**C.8 indeterminabilità della fine del monitoraggio**  [issue: I-02] [tipo: presenza]

Verifica   Il deliverable afferma che la data di conclusione del monitoraggio decennale non è determinabile, perché il decennio decorre dall'avvio dell'esercizio della barriera idraulica, non realizzata.
Pass se    compare l'affermazione che la data di conclusione non è determinabile e l'indicazione dell'evento da cui il decennio decorre
Fail se    è indicata una data determinata di conclusione del monitoraggio, oppure è dichiarata l'impossibilità di concludere senza indicare l'evento di decorrenza.
Indifferente  l'indicazione della data di avvio prevista dalla stima.

*metadati non forniti al judge* - fonte: 05_provvedimento_regionale_approvazione_progetto.md, punto 3; gravita: alta; instradamento: judge

**C.9 derivazione errata sulla franchigia**  [issue: N-01] [tipo: assenza]

Verifica   Il deliverable non quantifica una perdita di recupero derivante dalla formulazione della franchigia.
Pass se    Il deliverable non quantifica una perdita di recupero derivante dalla formulazione della franchigia.
Fail se    è affermato che la formulazione della franchigia riduce di 150.000 euro il recupero sull'esposizione documentata.
Indifferente  la menzione dell'importo della franchigia in altra funzione.

*metadati non forniti al judge* - fonte: derivazione da escludere; gravita: media; instradamento: judge
