# WF2-100 - Criteri atomizzati

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
Pass se    è presente remediation_timeline.md
Fail se    il file manca oppure il nome diverge.

*metadati non forniti al judge* - fonte: public/response_template.md; gravita: media; instradamento: verifica meccanica

**A.2 sezioni della timeline**  [issue: -] [tipo: struttura]

Verifica   Il deliverable contiene le sezioni indicate, nell'ordine indicato.
Pass se    le intestazioni compaiono tutte e nella sequenza del response_template
Fail se    manca un'intestazione oppure l'ordine differisce.
Indifferente  la formulazione delle intestazioni oltre le prime ventidue battute.

*metadati non forniti al judge* - fonte: public/response_template.md; gravita: media; instradamento: verifica meccanica

**A.3 data di riferimento**  [issue: -] [tipo: valore]

Verifica   Il deliverable assume come data di riferimento il 27 ottobre 2026.
Pass se    compare «27 ottobre 2026» come data alla quale la timeline è riferita
Fail se    è assunta una data diversa, oppure la data di riferimento non compare.
Indifferente  il formato della data.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: alta; instradamento: verifica meccanica

**A.4 evento di decorrenza per ogni termine**  [issue: -] [tipo: struttura]

Verifica   Ogni termine indica l'evento da cui decorre.
Pass se    ciascun termine riporta l'evento di decorrenza
Fail se    uno o più termini non indicano l'evento di decorrenza.
Indifferente  la forma dell'indicazione.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: alta; instradamento: verifica meccanica

**A.5 calcolo esposto per ogni termine**  [issue: -] [tipo: struttura]

Verifica   Ogni termine riporta il calcolo seguito.
Pass se    ciascun termine riporta il passaggio aritmetico o la regola di computo applicata
Fail se    uno o più termini riportano il solo risultato.
Indifferente  il livello di dettaglio del calcolo.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: alta; instradamento: verifica meccanica

**A.6 stato di ogni termine**  [issue: -] [tipo: struttura]

Verifica   Ogni termine indica se alla data di riferimento è rispettato, scaduto o non ancora maturato.
Pass se    ciascun termine riporta uno dei tre stati
Fail se    uno o più termini non riportano alcuno stato.
Indifferente  le etichette usate per i tre stati.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: alta; instradamento: verifica meccanica

**A.7 distinzione fra termini determinati e condizionati**  [issue: -] [tipo: struttura]

Verifica   Il deliverable tiene distinti i termini che hanno una data certa da quelli che dipendono da eventi non ancora avvenuti.
Pass se    le due categorie sono trattate in sezioni separate o comunque distinte termine per termine
Fail se    i termini sono elencati senza distinguere le due categorie.
Indifferente  il modo in cui la distinzione è resa graficamente.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: alta; instradamento: verifica meccanica

**A.8 documento indicato per ogni voce**  [issue: -] [tipo: struttura]

Verifica   Ogni voce indica il documento del fascicolo da cui i dati provengono.
Pass se    ciascuna voce riporta il nome di almeno un allegato
Fail se    una o più voci non riportano alcun allegato.
Indifferente  il numero degli allegati citati per voce.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: alta; instradamento: verifica meccanica

**A.9 riferimenti entro l'elenco chiuso**  [issue: -] [tipo: assenza]

Verifica   Il deliverable non cita norme assenti dal reference pack.
Pass se    Il deliverable non cita norme assenti dal reference pack.
Fail se    compare un riferimento a un atto o a un articolo che non figura in public/02_reference_pack.md.
Indifferente  la scelta di non citare alcuna fonte in una singola voce.

*metadati non forniti al judge* - fonte: public/02_reference_pack.md e private/fonti_chiuse.json; gravita: alta; instradamento: verifica meccanica

**A.10 limite di parole**  [issue: -] [tipo: struttura]

Verifica   Il deliverable resta entro il limite di parole.
Pass se    il conteggio delle parole non supera 2400
Fail se    il conteggio supera il limite.

*metadati non forniti al judge* - fonte: public/response_template.md; gravita: bassa; instradamento: verifica meccanica


## Sezione B - merito

Stato del fascicolo alla data di riferimento: comunicazione dell'evento e notizia del superamento trasmesse; misure di prevenzione e di messa in sicurezza d'emergenza in essere; piano di caratterizzazione non presentato e termine decorso; nessuna ordinanza né diffida notificata

**B.1 termine di ventiquattro ore rispettato**  [issue: I-01] [tipo: presenza]

Verifica   Il deliverable afferma che le misure di prevenzione e la comunicazione sono state compiute entro ventiquattro ore dall'evento.
Pass se    compare l'affermazione che il termine di ventiquattro ore è rispettato
Fail se    il termine è presentato come non rispettato, oppure lo stato del termine non è indicato.
Indifferente  il richiamo alla data delle singole misure adottate.

*metadati non forniti al judge* - fonte: 01_rapporto_di_intervento_e_messa_in_sicurezza.md; 02_comunicazione_dell_evento.md; gravita: alta; instradamento: judge

**B.2 destinatari della comunicazione dell'evento**  [issue: I-02] [tipo: presenza]

Verifica   Il deliverable afferma che la comunicazione dell'evento va indirizzata al comune, alla provincia, alla regione e al prefetto, e che il prefetto informa il Ministro dell'ambiente nelle ventiquattro ore successive.
Pass se    compaiono i quattro destinatari e l'informativa del prefetto al Ministro
Fail se    manca il prefetto fra i destinatari, oppure i destinatari della comunicazione sono confusi con quelli della notizia di superamento.
Indifferente  l'ordine in cui i destinatari sono elencati.

*metadati non forniti al judge* - fonte: art. 304, comma 2, del codice dell'ambiente; 02_comunicazione_dell_evento.md; gravita: alta; instradamento: judge

**B.3 effetto abilitante della comunicazione**  [issue: I-03] [tipo: presenza]

Verifica   Il deliverable afferma che la comunicazione, non appena pervenuta al comune, abilita immediatamente l'operatore alla realizzazione degli interventi.
Pass se    compare l'affermazione dell'effetto abilitante immediato
Fail se    la prosecuzione degli interventi è subordinata a un provvedimento di assenso, oppure il punto non è trattato.
Indifferente  il richiamo alla sanzione prevista per l'omessa comunicazione.

*metadati non forniti al judge* - fonte: art. 304, comma 2, del codice dell'ambiente; gravita: media; instradamento: judge

**B.4 autocertificazione preclusa**  [issue: I-04] [tipo: presenza]

Verifica   Il deliverable afferma che l'autocertificazione di ripristino opera soltanto se l'indagine preliminare accerta che le soglie di contaminazione non sono superate, e che nel caso la via è preclusa.
Pass se    compaiono la condizione di operatività e l'affermazione che nel caso è preclusa
Fail se    l'autocertificazione è presentata come adempimento mancato, oppure la condizione di operatività non è indicata.
Indifferente  il richiamo al termine di quarantotto ore.

*metadati non forniti al judge* - fonte: art. 242, comma 2, del codice dell'ambiente; gravita: alta; instradamento: judge

**B.5 dies a quo del piano di caratterizzazione**  [issue: I-05] [tipo: attribuzione]

Verifica   Il deliverable riconduce la decorrenza dei trenta giorni per il piano di caratterizzazione alla notizia del superamento.
Pass se    compare l'affermazione che i trenta giorni decorrono dalla notizia del superamento
Fail se    la decorrenza è ricondotta all'evento, alla comunicazione dell'evento o all'emissione del rapporto di prova.
Indifferente  il richiamo alla data della notizia.

*metadati non forniti al judge* - fonte: 03_notizia_di_superamento.md; art. 242, comma 3, del codice dell'ambiente; gravita: alta; instradamento: judge

**B.6 stato del termine e destinatari del piano**  [issue: I-06] [tipo: presenza]

Verifica   Il deliverable afferma che alla data di riferimento il termine è scaduto e il piano non risulta presentato, e indica che il piano va presentato al comune, alle province e alla regione.
Pass se    compaiono lo stato scaduto del termine e i destinatari del piano
Fail se    il termine è presentato come pendente, oppure i destinatari del piano non sono indicati o sono indicati in modo diverso.
Indifferente  l'indicazione dei giorni di ritardo.

*metadati non forniti al judge* - fonte: 07_nota_del_consulente_ambientale.md, punto 3.1; art. 242, comma 3, del codice dell'ambiente; gravita: alta; instradamento: judge

**B.7 qualificazione del sito**  [issue: I-07] [tipo: qualificazione]

Verifica   Il deliverable qualifica il sito come potenzialmente contaminato.
Pass se    compare, riferita al sito, una fra: «sito potenzialmente contaminato»; «potenzialmente contaminato in attesa della caratterizzazione e dell'analisi di rischio»
Fail se    il sito è qualificato come contaminato, oppure la qualificazione non compare.
Indifferente  il richiamo alla differenza fra le due soglie.

*metadati non forniti al judge* - fonte: art. 240, comma 1, lettere d) ed e), del codice dell'ambiente; gravita: alta; instradamento: judge

**B.8 decorrenze della catena successiva**  [issue: I-08] [tipo: attribuzione]

Verifica   Il deliverable riconduce i sei mesi per le risultanze della caratterizzazione all'approvazione del piano, e i sessanta giorni per l'approvazione del documento di analisi di rischio alla sua ricezione.
Pass se    compaiono entrambe le decorrenze come indicate
Fail se    i sei mesi sono fatti decorrere dalla presentazione del piano, oppure i sessanta giorni sono fatti decorrere da un evento diverso dalla ricezione del documento.
Indifferente  il richiamo ai due termini di venti giorni.

*metadati non forniti al judge* - fonte: art. 242, commi 3 e 4, del codice dell'ambiente; gravita: alta; instradamento: judge

**B.9 esito negativo dell'analisi di rischio**  [issue: I-09] [tipo: presenza]

Verifica   Il deliverable afferma che, se la contaminazione non supera le concentrazioni soglia di rischio, la conferenza di servizi dichiara concluso positivamente il procedimento con l'approvazione del documento di analisi di rischio, e può prescrivere un programma di monitoraggio.
Pass se    compaiono la dichiarazione di conclusione positiva e l'eventuale programma di monitoraggio
Fail se    l'esito negativo non è trattato, oppure è presentata come necessaria la presentazione del progetto operativo.
Indifferente  l'indicazione dei termini del piano di monitoraggio.

*metadati non forniti al judge* - fonte: art. 242, commi 5 e 6, del codice dell'ambiente; gravita: alta; instradamento: judge

**B.10 esito positivo dell'analisi di rischio**  [issue: I-09] [tipo: presenza]

Verifica   Il deliverable afferma che, se le concentrazioni soglia di rischio sono superate, il progetto operativo va presentato nei successivi sei mesi dall'approvazione del documento di analisi di rischio e la regione lo approva entro sessanta giorni dal ricevimento.
Pass se    compaiono il termine di sei mesi e quello di sessanta giorni con le rispettive decorrenze
Fail se    l'esito positivo non è trattato, oppure una delle due decorrenze è indicata in modo diverso.
Indifferente  il richiamo alle garanzie finanziarie stabilite con il provvedimento di approvazione.

*metadati non forniti al judge* - fonte: art. 242, comma 7, del codice dell'ambiente; gravita: alta; instradamento: judge

**B.11 assenza di un termine di conclusione**  [issue: I-10] [tipo: presenza]

Verifica   Il deliverable afferma che non esiste un termine complessivo di conclusione del procedimento e indica gli eventi da cui le date successive dipendono.
Pass se    compaiono l'assenza di un termine complessivo e l'indicazione degli eventi da cui le date dipendono
Fail se    è indicata una data determinata di conclusione del procedimento, oppure la sua indeterminabilità è dichiarata senza indicare da che cosa dipende.
Indifferente  l'esposizione di un calcolo condizionato a un'ipotesi dichiarata.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: alta; instradamento: judge

**B.12 persistenza del superamento al netto dell'incertezza**  [issue: I-11] [tipo: presenza]

Verifica   Il deliverable afferma che il superamento del nichel persiste anche detratta l'incertezza estesa, secondo la regola decisionale dichiarata dal laboratorio.
Pass se    compare l'affermazione che il superamento persiste detratta l'incertezza estesa
Fail se    è affermato che il superamento è controvertibile sul dato analitico, oppure il punto non è trattato.
Indifferente  il richiamo al giudizio di conformità espresso dal rapporto.

*metadati non forniti al judge* - fonte: 04_rapporto_di_prova_suolo.md, punti 6 e 7; gravita: alta; instradamento: judge

**B.13 cedevolezza delle soglie rispetto ai valori di fondo**  [issue: I-12] [tipo: presenza]

Verifica   Il deliverable afferma che, se il sito ricade in un'area interessata da fenomeni antropici o naturali che hanno determinato il superamento, le soglie si assumono pari al valore di fondo esistente per i parametri superati.
Pass se    compare l'affermazione della cedevolezza delle soglie rispetto ai valori di fondo
Fail se    il confronto con il valore tabellare è presentato come definitivo, oppure è affermato che il superamento viene meno per il solo fatto che nell'area il nichel sia elevato.
Indifferente  il richiamo alla destinazione d'uso industriale dell'area.

*metadati non forniti al judge* - fonte: art. 240, comma 1, lettera b), del codice dell'ambiente; gravita: alta; instradamento: judge

**B.14 procedura sui valori di fondo**  [issue: I-13] [tipo: presenza]

Verifica   Il deliverable afferma che il piano di indagine sui valori di fondo va presentato all'agenzia regionale, che ne definisce i valori, con realizzazione in contraddittorio entro sessanta giorni dalla presentazione, e rileva che nel fascicolo nessun piano risulta presentato.
Pass se    compaiono l'attribuzione all'agenzia regionale, il termine del contraddittorio e l'assenza del piano nel fascicolo
Fail se    la determinazione dei valori di fondo è attribuita al laboratorio, al consulente o alla regione, oppure il termine del contraddittorio non è indicato.
Indifferente  la collocazione dell'iniziativa fra le azioni proposte.

*metadati non forniti al judge* - fonte: art. 242, comma 13-ter, del codice dell'ambiente; 07_nota_del_consulente_ambientale.md, punto 4.1; gravita: alta; instradamento: judge

**B.15 posizione del punto di monitoraggio**  [issue: I-14] [tipo: presenza]

Verifica   Il deliverable afferma che il piezometro esistente si trova a monte idrogeologico dell'area interessata e che le sue letture non escludono il coinvolgimento delle acque sotterranee.
Pass se    compaiono la posizione a monte del piezometro e l'inidoneità delle sue letture a escludere il coinvolgimento della falda
Fail se    è accolta l'affermazione del rapporto di intervento sulla posizione a valle, oppure dalle letture del piezometro è tratta la conclusione che le acque sotterranee non sono coinvolte.
Indifferente  la proposta di realizzare punti a valle nel piano di caratterizzazione.

*metadati non forniti al judge* - fonte: 07_nota_del_consulente_ambientale.md, punto 5.5; 01_rapporto_di_intervento_e_messa_in_sicurezza.md, punto 2; gravita: alta; instradamento: judge

**B.16 estensione del perimetro di indagine**  [issue: I-15] [tipo: presenza]

Verifica   Il deliverable indica che le ulteriori lesioni della pavimentazione rilevate fuori dall'area dell'evento vanno considerate nella definizione del perimetro di indagine del piano di caratterizzazione.
Pass se    compare l'indicazione che quelle lesioni incidono sul perimetro di indagine
Fail se    le ulteriori lesioni sono trattate come irrilevanti, oppure sono qualificate come contaminazione accertata.
Indifferente  l'indicazione della lunghezza rilevata.

*metadati non forniti al judge* - fonte: 05_verbale_di_sopralluogo_arpa.md, punto 2.6; gravita: media; instradamento: judge

**B.17 ordinanza-diffida provinciale**  [issue: I-16] [tipo: attribuzione]

Verifica   Il deliverable riconduce alla provincia l'ordinanza motivata con cui il responsabile della potenziale contaminazione è diffidato a provvedere, e indica che l'ordinanza è comunque notificata anche al proprietario del sito.
Pass se    compaiono l'attribuzione alla provincia e la notifica anche al proprietario
Fail se    l'ordinanza è attribuita al comune, alla regione o all'agenzia regionale, oppure la notifica al proprietario non è indicata.
Indifferente  il richiamo alle indagini per identificare il responsabile con oneri a suo carico.

*metadati non forniti al judge* - fonte: art. 244, commi 2 e 3, del codice dell'ambiente; gravita: alta; instradamento: judge

**B.18 iniziativa da assumere sul piano**  [issue: I-16] [tipo: presenza]

Verifica   Il deliverable indica fra le azioni la presentazione immediata del piano di caratterizzazione e afferma che nessuna ordinanza risulta notificata alla data di riferimento.
Pass se    compaiono l'azione della presentazione immediata e l'assenza di ordinanze notificate
Fail se    l'azione non è indicata, oppure è affermato che il ritardo preclude la presentazione del piano.
Indifferente  l'ordine in cui l'azione è collocata.

*metadati non forniti al judge* - fonte: 07_nota_del_consulente_ambientale.md, punto 3.2; gravita: alta; instradamento: judge

**B.19 sovra-segnalazione - autocertificazione di ripristino**  [issue: N-01] [tipo: assenza]

Verifica   Il deliverable non indica fra gli adempimenti scaduti l'autocertificazione di ripristino.
Pass se    Il deliverable non indica fra gli adempimenti scaduti l'autocertificazione di ripristino.
Fail se    l'autocertificazione di ripristino è indicata fra gli adempimenti mancati o scaduti, oppure alla scadenza di quel termine sono attribuite conseguenze.
Indifferente  la menzione dell'autocertificazione per escluderne l'operatività nel caso.

*metadati non forniti al judge* - fonte: art. 242, comma 2, del codice dell'ambiente; gravita: alta; instradamento: judge

**B.20 sovra-segnalazione - superamento per il piombo**  [issue: N-02] [tipo: assenza]

Verifica   Il deliverable non indica il piombo fra i parametri in superamento.
Pass se    Il deliverable non indica il piombo fra i parametri in superamento.
Fail se    è affermato che il piombo supera la soglia applicabile, oppure per il piombo è aperta una posizione autonoma nel procedimento.
Indifferente  la menzione del piombo fra i parametri determinati e conformi, o il richiamo alla linea dismessa nel 1994 in altra funzione.

*metadati non forniti al judge* - fonte: 04_rapporto_di_prova_suolo.md, punto 7; gravita: alta; instradamento: judge

**B.21 sovra-segnalazione - qualificazione come sito contaminato**  [issue: N-03] [tipo: assenza]

Verifica   Il deliverable non qualifica il sito come contaminato alla data di riferimento.
Pass se    Il deliverable non qualifica il sito come contaminato alla data di riferimento.
Fail se    è affermato che il sito è contaminato, oppure che le concentrazioni soglia di rischio sono superate.
Indifferente  la menzione delle concentrazioni soglia di rischio come da determinare.

*metadati non forniti al judge* - fonte: art. 240, comma 1, lettera e), del codice dell'ambiente; gravita: alta; instradamento: judge

**B.22 sovra-segnalazione - data di conclusione del procedimento**  [issue: N-04] [tipo: assenza]

Verifica   Il deliverable non indica una data determinata di conclusione del procedimento.
Pass se    Il deliverable non indica una data determinata di conclusione del procedimento.
Fail se    è indicata una data di conclusione del procedimento presentata come certa, oppure è affermato che il procedimento si chiude entro un termine complessivo determinato.
Indifferente  l'esposizione di un calcolo condizionato a un'ipotesi dichiarata.

*metadati non forniti al judge* - fonte: 06_email_del_direttore_di_stabilimento.md; gravita: alta; instradamento: judge

**B.23 simmetria del controllo - adempimenti compiuti**  [issue: -] [tipo: assenza]

Verifica   Il deliverable non omette gli adempimenti che risultano compiuti nei termini.
Pass se    Il deliverable non omette gli adempimenti che risultano compiuti nei termini.
Fail se    non compare alcuno degli adempimenti compiuti, quali le misure di prevenzione entro ventiquattro ore, la comunicazione dell'evento ai quattro destinatari, la notizia immediata del superamento o il mantenimento delle misure di messa in sicurezza.
Indifferente  quali fra questi adempimenti sono richiamati, purché ne compaia almeno uno.

*metadati non forniti al judge* - fonte: private/challenge_map.json, controlled non-issue; gravita: media; instradamento: judge

**B.24 presunzione dell'esito - analisi di rischio**  [issue: -] [tipo: assenza]

Verifica   Il deliverable non presume l'esito dell'analisi di rischio né quello del procedimento.
Pass se    Il deliverable non presume l'esito dell'analisi di rischio né quello del procedimento.
Fail se    è affermato che l'analisi di rischio dimostrerà il mancato superamento delle concentrazioni soglia di rischio, o che il procedimento si concluderà positivamente.
Indifferente  l'esposizione di entrambi gli esiti come alternativi.

*metadati non forniti al judge* - fonte: private/challenge_map.json, dati mancanti; gravita: alta; instradamento: judge


## Sezione C - date e valori calcolati

**C.1 termine di ventiquattro ore**  [issue: I-01] [tipo: valore]

Verifica   Il deliverable indica il 22 settembre 2026 come scadenza del termine di ventiquattro ore.
Pass se    compare la data «22 settembre 2026» riferita al termine di ventiquattro ore
Fail se    è indicata una data diversa, oppure il termine non è calcolato.
Indifferente  il richiamo all'ora dell'evento.

*metadati non forniti al judge* - fonte: art. 242, comma 1, e art. 304, comma 2, del codice dell'ambiente; gravita: alta; instradamento: verifica meccanica

**C.2 termine per il piano di caratterizzazione**  [issue: I-05] [tipo: valore]

Verifica   Il deliverable indica il 23 ottobre 2026 come scadenza del termine per la presentazione del piano di caratterizzazione.
Pass se    compare la data «23 ottobre 2026» riferita al termine per il piano di caratterizzazione
Fail se    è indicata una data diversa, oppure il termine non è calcolato.
Indifferente  l'indicazione dei giorni di ritardo.

*metadati non forniti al judge* - fonte: art. 242, comma 3, del codice dell'ambiente; gravita: alta; instradamento: verifica meccanica

**C.3 derivazione errata dall'evento**  [issue: I-05] [tipo: assenza]

Verifica   Il deliverable non computa i trenta giorni dall'evento.
Pass se    Il deliverable non computa i trenta giorni dall'evento.
Fail se    compare la data «21 ottobre 2026» come scadenza del termine per il piano di caratterizzazione, oppure i trenta giorni sono computati dall'evento.
Indifferente  la menzione della data dell'evento in altra funzione.

*metadati non forniti al judge* - fonte: derivazione da escludere; gravita: alta; instradamento: judge

**C.4 nichel al netto dell'incertezza estesa**  [issue: I-11] [tipo: valore]

Verifica   Il deliverable indica in 658 milligrammi per chilogrammo il valore del nichel detratta l'incertezza estesa.
Pass se    compare la misura «658» riferita al nichel detratta l'incertezza estesa
Fail se    è indicata una misura diversa, oppure il calcolo non compare.
Indifferente  il modo in cui l'unità di misura è scritta.

*metadati non forniti al judge* - fonte: 04_rapporto_di_prova_suolo.md, punto 7; gravita: alta; instradamento: verifica meccanica

**C.5 autorizzazione del piano nel calcolo condizionato**  [issue: I-08] [tipo: valore]

Verifica   Il deliverable indica il 26 novembre 2026 come termine per l'autorizzazione del piano di caratterizzazione, assumendo la presentazione alla data di riferimento.
Pass se    compare la data «26 novembre 2026» riferita all'autorizzazione del piano
Fail se    è indicata una data diversa a partire dalla medesima ipotesi, oppure il calcolo condizionato non compare.
Indifferente  il modo in cui l'ipotesi di presentazione è dichiarata.

*metadati non forniti al judge* - fonte: art. 242, comma 3, del codice dell'ambiente; gravita: media; instradamento: verifica meccanica

**C.6 risultanze della caratterizzazione nel calcolo condizionato**  [issue: I-08] [tipo: valore]

Verifica   Il deliverable indica il 26 maggio 2027 come termine per la trasmissione delle risultanze della caratterizzazione, assumendo la presentazione del piano alla data di riferimento.
Pass se    compare la data «26 maggio 2027» riferita alla trasmissione delle risultanze della caratterizzazione
Fail se    è indicata una data diversa a partire dalla medesima ipotesi, oppure il calcolo condizionato non compare.
Indifferente  il modo in cui l'ipotesi di presentazione è dichiarata.

*metadati non forniti al judge* - fonte: art. 242, comma 4, del codice dell'ambiente; gravita: media; instradamento: verifica meccanica
