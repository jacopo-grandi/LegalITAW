# WF2-092 - Criteri atomizzati

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
Pass se    è presente open_source_audit.md
Fail se    il file manca oppure il nome diverge.

*metadati non forniti al judge* - fonte: public/response_template.md; gravita: media; instradamento: verifica meccanica

**A.2 sezioni della matrice**  [issue: -] [tipo: struttura]

Verifica   Il deliverable contiene le sezioni indicate, nell'ordine indicato.
Pass se    le intestazioni compaiono tutte e nella sequenza del response_template
Fail se    manca un'intestazione oppure l'ordine differisce.
Indifferente  la formulazione delle intestazioni oltre le prime ventidue battute.

*metadati non forniti al judge* - fonte: public/response_template.md; gravita: media; instradamento: verifica meccanica

**A.3 data di riferimento**  [issue: -] [tipo: valore]

Verifica   Il deliverable assume come data di riferimento il 5 novembre 2026.
Pass se    compare «5 novembre 2026» come data alla quale l'analisi è riferita
Fail se    è assunta una data diversa, oppure la data di riferimento non compare.
Indifferente  il formato della data.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: alta; instradamento: verifica meccanica

**A.4 componente indicato per ogni rilievo**  [issue: -] [tipo: struttura]

Verifica   Ogni rilievo indica il componente a cui si riferisce.
Pass se    ciascuna voce riporta il nome di un pacchetto dell'inventario
Fail se    una o più voci non indicano alcun componente.
Indifferente  l'indicazione della versione oltre al nome.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: alta; instradamento: verifica meccanica

**A.5 canale di fornitura indicato per ogni rilievo**  [issue: -] [tipo: struttura]

Verifica   Ogni rilievo indica il canale di fornitura interessato.
Pass se    ciascuna voce indica se il componente è distribuito sull'apparecchiatura, erogato come servizio o usato solo internamente
Fail se    una o più voci non indicano il canale.
Indifferente  la denominazione usata per i canali.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: alta; instradamento: verifica meccanica

**A.6 stati probatori distinti**  [issue: -] [tipo: struttura]

Verifica   Ogni rilievo distingue il fatto documentato dalla dichiarazione di parte.
Pass se    ciascuna voce qualifica l'elemento su cui poggia come risultante da un documento oppure come dichiarato in una nota interna
Fail se    una dichiarazione di parte è riportata come fatto documentato senza distinzione.
Indifferente  la terminologia usata per la distinzione.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: alta; instradamento: verifica meccanica

**A.7 responsabile indicato per ogni rilievo**  [issue: -] [tipo: struttura]

Verifica   Ogni rilievo indica chi deve chiudere il punto.
Pass se    ciascuna voce indica una funzione o una posizione responsabile della chiusura
Fail se    una o più voci non indicano alcun responsabile.
Indifferente  l'indicazione del nome della persona anziché della funzione.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: media; instradamento: verifica meccanica

**A.8 riferimenti entro l'elenco chiuso**  [issue: -] [tipo: assenza]

Verifica   Il deliverable non cita norme o licenze assenti dal reference pack.
Pass se    Il deliverable non cita norme o licenze assenti dal reference pack.
Fail se    compare un riferimento a una norma, a una licenza o a una sezione di licenza che non figura in public/02_reference_pack.md.
Indifferente  la scelta di non citare alcuna fonte in una singola voce.

*metadati non forniti al judge* - fonte: public/02_reference_pack.md e private/fonti_chiuse.json; gravita: alta; instradamento: verifica meccanica

**A.9 limite di parole**  [issue: -] [tipo: struttura]

Verifica   Il deliverable resta entro il limite di parole.
Pass se    il conteggio delle parole non supera 2400
Fail se    il conteggio supera il limite.

*metadati non forniti al judge* - fonte: public/response_template.md; gravita: bassa; instradamento: verifica meccanica


## Sezione B - merito

Stato del fascicolo alla data di riferimento: audit in corso; versione 5.1.4 in esercizio, versione 5.2 pianificata per il 26 novembre 2026; parere legale e atto di cessione non acquisiti

**B.1 pianificatore - presupposto della modifica**  [issue: I-01] [tipo: presenza]

Verifica   Il deliverable afferma che il pianificatore corvenza-scheduler è stato modificato localmente.
Pass se    compare l'affermazione che corvenza-scheduler è stato modificato
Fail se    il componente è descritto come usato senza modifiche, oppure la modifica non è affermata.
Indifferente  l'indicazione di quanti file sono stati modificati.

*metadati non forniti al judge* - fonte: 02_inventario_dipendenze.csv; 08_email_responsabile_sviluppo.md; gravita: alta; instradamento: judge

**B.2 pianificatore - interazione a distanza**  [issue: I-01] [tipo: presenza]

Verifica   Il deliverable afferma che gli utenti del cliente interagiscono con il pianificatore a distanza attraverso una rete.
Pass se    compare l'affermazione che il pianificatore è raggiunto dagli utenti attraverso il portale o attraverso l'interfaccia programmatica
Fail se    l'interazione a distanza non è affermata, oppure è esclusa perché il componente è eseguito sull'infrastruttura di Solmarino.
Indifferente  il richiamo al numero dei clienti che usano l'interfaccia programmatica.

*metadati non forniti al judge* - fonte: 01_scheda_prodotto_e_fornitura.md, punti 2.2 e 5; 08_email_responsabile_sviluppo.md; gravita: alta; instradamento: judge

**B.3 pianificatore - conseguenza**  [issue: I-01] [tipo: qualificazione]

Verifica   Il deliverable qualifica la conseguenza come obbligo di offrire agli utenti remoti la possibilità di ricevere il codice sorgente corrispondente della versione modificata.
Pass se    compare, riferita al pianificatore, una fra: «offerta del codice sorgente agli utenti remoti»; «obbligo di rendere disponibile il codice sorgente corrispondente agli utenti che interagiscono via rete»; «messa a disposizione del sorgente su server di rete»
Fail se    la conseguenza è esclusa, oppure è descritta come obbligo di consegna al cliente contrattuale.
Indifferente  la scelta della modalità tecnica di messa a disposizione.

*metadati non forniti al judge* - fonte: sezione 13 AGPL-3.0; gravita: alta; instradamento: judge

**B.4 pianificatore - errore sul conveying**  [issue: I-01] [tipo: assenza]

Verifica   Il deliverable non esclude l'obbligo sul pianificatore per il fatto che nessun eseguibile è consegnato al cliente.
Pass se    Il deliverable non esclude l'obbligo sul pianificatore per il fatto che nessun eseguibile è consegnato al cliente.
Fail se    l'assenza di consegna di un eseguibile è usata per escludere l'obbligo relativo al pianificatore.
Indifferente  il richiamo all'assenza di consegna in relazione ad altri componenti.

*metadati non forniti al judge* - fonte: sezioni 0 e 13 AGPL-3.0; gravita: alta; instradamento: judge

**B.5 menzione delle modifiche - fatto**  [issue: I-02] [tipo: presenza]

Verifica   Il deliverable afferma che le intestazioni dei file modificati di algen-crypto non dichiarano la modifica.
Pass se    compare l'affermazione che i file modificati riportano soltanto l'avviso di licenza originale
Fail se    il fatto non è rilevato, oppure è affermato che gli avvisi di modifica sono presenti.
Indifferente  l'indicazione dei nomi dei file.

*metadati non forniti al judge* - fonte: 03_notice_e_intestazioni.md, parte seconda; gravita: alta; instradamento: judge

**B.6 menzione delle modifiche - rimedio**  [issue: I-02] [tipo: presenza]

Verifica   Il deliverable indica come rimedio l'apposizione su ciascun file modificato di un avviso che dichiara la modifica.
Pass se    fra le azioni compare l'apposizione dell'avviso di modifica sui file modificati
Fail se    il rimedio indicato è l'aggiornamento del file NOTICE, oppure non è indicato alcun rimedio.
Indifferente  l'indicazione della data della modifica nell'avviso.

*metadati non forniti al judge* - fonte: sezione 4, lettera b, Apache-2.0; gravita: alta; instradamento: judge

**B.7 avvisi di attribuzione - fatto**  [issue: I-03] [tipo: presenza]

Verifica   Il deliverable afferma che il NOTICE distribuito con la piattaforma non riproduce gli avvisi di attribuzione contenuti nel NOTICE di belfonte-parser.
Pass se    compare l'affermazione che il contenuto del NOTICE del pacchetto non è riprodotto
Fail se    il fatto non è rilevato, oppure è affermato che l'elencazione del pacchetto fra i componenti Apache assolve l'obbligo.
Indifferente  il richiamo al contenuto specifico dell'avviso.

*metadati non forniti al judge* - fonte: 03_notice_e_intestazioni.md; gravita: alta; instradamento: judge

**B.8 avvisi di attribuzione - rimedio**  [issue: I-03] [tipo: presenza]

Verifica   Il deliverable indica come rimedio la riproduzione del contenuto degli avvisi di attribuzione in una delle collocazioni ammesse.
Pass se    fra le azioni compare la riproduzione del contenuto del NOTICE del pacchetto
Fail se    il rimedio indicato è la sola citazione del pacchetto, oppure non è indicato.
Indifferente  la collocazione scelta fra quelle ammesse.

*metadati non forniti al judge* - fonte: sezione 4, lettera d, Apache-2.0; gravita: media; instradamento: judge

**B.9 combinazione incompatibile - individuazione**  [issue: I-04] [tipo: presenza]

Verifica   Il deliverable individua la combinazione fra meridolo-compress e algen-crypto come problematica.
Pass se    compare l'indicazione della combinazione fra un componente GPL-2.0-only e un componente Apache-2.0 collegati staticamente nello stesso modulo
Fail se    la combinazione non è individuata, oppure è presentata come ammissibile.
Indifferente  l'indicazione del modulo in cui la combinazione si realizza.

*metadati non forniti al judge* - fonte: 02_inventario_dipendenze.csv; gravita: alta; instradamento: judge

**B.10 combinazione incompatibile - qualificazione**  [issue: I-04] [tipo: qualificazione]

Verifica   Il deliverable qualifica la combinazione come incompatibile.
Pass se    compare, riferita a quella combinazione, una fra: «licenze incompatibili»; «incompatibilità di licenza»; «non combinabili»
Fail se    la combinazione è qualificata come meramente da documentare, oppure la qualificazione non compare.
Indifferente  l'indicazione della ragione tecnica dell'incompatibilità.

*metadati non forniti al judge* - fonte: voce #apache2 della Free Software Foundation; gravita: alta; instradamento: judge

**B.11 combinazione incompatibile - rimedio distinto**  [issue: I-04] [tipo: presenza]

Verifica   Il deliverable indica un rimedio che incide sulla combinazione e non sulla sola documentazione.
Pass se    fra le azioni compare, riferita a quella combinazione, la sostituzione del componente, la sua rimozione o la modifica della modalità di collegamento
Fail se    l'unico rimedio indicato è l'aggiunta di un avviso o l'aggiornamento dell'inventario.
Indifferente  la scelta fra sostituzione, rimozione e modifica del collegamento.

*metadati non forniti al judge* - fonte: 02_inventario_dipendenze.csv; gravita: media; instradamento: judge

**B.12 richiesta del cliente - perimetro**  [issue: I-05] [tipo: presenza]

Verifica   Il deliverable circoscrive la consegna ai componenti installati sull'apparecchiatura.
Pass se    compare l'affermazione che la consegna riguarda i componenti installati sull'apparecchiatura e non i moduli erogati come servizio
Fail se    il perimetro è esteso ai moduli erogati come servizio, oppure non è delimitato.
Indifferente  il richiamo alla circostanza che il cliente stesso escluda i moduli in servizio.

*metadati non forniti al judge* - fonte: 06_richiesta_codice_sorgente.md; 01_scheda_prodotto_e_fornitura.md, punto 2.1; gravita: alta; instradamento: judge

**B.13 richiesta del cliente - contenuto della consegna**  [issue: I-05] [tipo: presenza]

Verifica   Il deliverable afferma che la consegna comprende gli script necessari alla generazione, all'installazione e all'esecuzione del codice oggetto.
Pass se    compare l'affermazione che gli script di generazione, installazione ed esecuzione fanno parte del sorgente corrispondente
Fail se    la consegna è limitata al codice dei componenti, oppure il contenuto non è specificato.
Indifferente  l'esclusione delle librerie di sistema.

*metadati non forniti al judge* - fonte: sezione 1 GPL-3.0; gravita: alta; instradamento: judge

**B.14 richiesta del cliente - durata della disponibilità**  [issue: I-05] [tipo: presenza]

Verifica   Il deliverable afferma che, se la consegna avviene mediante archivio in rete, va dichiarato per quanto tempo l'archivio resta disponibile.
Pass se    compare l'affermazione che va indicato il periodo di disponibilità dell'archivio
Fail se    il punto non è trattato, pur essendo stato chiesto dal cliente.
Indifferente  la durata proposta.

*metadati non forniti al judge* - fonte: sezione 6 GPL-3.0; 06_richiesta_codice_sorgente.md; gravita: media; instradamento: judge

**B.15 componente GPL-3.0 sull'appliance - individuazione**  [issue: I-06] [tipo: presenza]

Verifica   Il deliverable individua quadrelli-render come componente GPL-3.0 modificato e distribuito sull'apparecchiatura.
Pass se    compare l'indicazione di quadrelli-render come componente modificato distribuito sull'apparecchiatura
Fail se    il componente non è individuato, oppure è collocato nel servizio in cloud.
Indifferente  il richiamo alla modalità di collegamento.

*metadati non forniti al judge* - fonte: 02_inventario_dipendenze.csv; 01_scheda_prodotto_e_fornitura.md, punto 2.1; gravita: alta; instradamento: judge

**B.16 componente GPL-3.0 sull'appliance - perimetro da verificare**  [issue: I-06] [tipo: presenza]

Verifica   Il deliverable indica come necessaria la verifica del perimetro dell'opera così come distribuita nel modulo che incorpora il componente.
Pass se    compare l'indicazione di verificare quale sia l'opera distribuita, e non soltanto la porzione modificata
Fail se    la conseguenza è circoscritta al solo pacchetto modificato.
Indifferente  il richiamo alla distinzione fra opera unica e aggregato.

*metadati non forniti al judge* - fonte: sezione 5 GPL-3.0; gravita: alta; instradamento: judge

**B.17 componente GPL-3.0 sull'appliance - divieto di conclusione anticipata**  [issue: I-06] [tipo: assenza]

Verifica   Il deliverable non afferma che il modulo costituisce un aggregato di opere separate.
Pass se    Il deliverable non afferma che il modulo costituisce un aggregato di opere separate.
Fail se    è affermato che il modulo costituisce un aggregato, o che la licenza non si estende oltre il pacchetto, senza che il fascicolo consenta di stabilirlo.
Indifferente  l'indicazione dei dati tecnici necessari a stabilirlo.

*metadati non forniti al judge* - fonte: sezione 5 GPL-3.0; gravita: media; instradamento: judge

**B.18 componente EUPL - presupposto**  [issue: I-07] [tipo: presenza]

Verifica   Il deliverable afferma che aurendo-forms espone agli utenti del portale l'accesso alle funzioni con cui compilano i moduli di collaudo.
Pass se    compare l'affermazione che il componente rende accessibili agli utenti le funzioni di compilazione guidata
Fail se    il presupposto non è affermato, oppure il componente è descritto come non esposto agli utenti.
Indifferente  il richiamo alla delibera del comitato tecnico che lo ha adottato.

*metadati non forniti al judge* - fonte: 08_email_responsabile_sviluppo.md; 04_verbale_comitato_tecnico.md, punto 2; gravita: alta; instradamento: judge

**B.19 componente EUPL - indipendenza dalla modifica**  [issue: I-07] [tipo: presenza]

Verifica   Il deliverable afferma che l'obbligo relativo al componente EUPL non dipende dalla presenza di modifiche.
Pass se    compare l'affermazione che l'obbligo si attiva anche senza modifiche al componente
Fail se    l'obbligo è escluso perché il componente non è stato modificato.
Indifferente  il confronto esplicito con il meccanismo dell'AGPL.

*metadati non forniti al judge* - fonte: artt. 1 e 5 EUPL-1.2; gravita: alta; instradamento: judge

**B.20 componenti senza licenza - conteggio e canale**  [issue: I-08] [tipo: presenza]

Verifica   Il deliverable afferma che alcuni dei componenti senza licenza dichiarata sono distribuiti sull'apparecchiatura.
Pass se    compare l'affermazione che componenti senza licenza dichiarata sono distribuiti sull'apparecchiatura
Fail se    i componenti senza licenza sono trattati come questione uniforme senza distinguere il canale.
Indifferente  l'elenco nominativo dei componenti.

*metadati non forniti al judge* - fonte: 02_inventario_dipendenze.csv; gravita: alta; instradamento: judge

**B.21 componenti senza licenza - divieto di presunzione**  [issue: I-08] [tipo: assenza]

Verifica   Il deliverable non qualifica come permissivi i componenti che non dichiarano licenza.
Pass se    Il deliverable non qualifica come permissivi i componenti che non dichiarano licenza.
Fail se    i componenti senza licenza dichiarata sono presentati come utilizzabili in via residuale o come permissivi.
Indifferente  l'osservazione che l'inventario non riporta obblighi per quelle righe.

*metadati non forniti al judge* - fonte: 02_inventario_dipendenze.csv; gravita: alta; instradamento: judge

**B.22 componenti senza licenza - conseguenza operativa**  [issue: I-08] [tipo: presenza]

Verifica   Il deliverable indica la risoluzione della posizione prima della distribuzione.
Pass se    fra le azioni compare, riferita a quei componenti, la sostituzione, la rimozione o l'acquisizione del titolo prima della distribuzione
Fail se    l'azione indicata è il solo aggiornamento dell'inventario o della documentazione.
Indifferente  la scelta fra le azioni indicate.

*metadati non forniti al judge* - fonte: 02_inventario_dipendenze.csv; gravita: alta; instradamento: judge

**B.23 titolo sul codec - fatto**  [issue: I-09] [tipo: presenza]

Verifica   Il deliverable afferma che non risulta agli atti alcun atto di cessione sottoscritto relativo al codec di trama.
Pass se    compare l'affermazione che l'atto di cessione non risulta sottoscritto o non risulta agli atti
Fail se    è affermato che il titolo è stato regolarizzato, oppure il punto non è trattato.
Indifferente  il richiamo alla data di trasmissione della richiesta.

*metadati non forniti al judge* - fonte: 04_verbale_comitato_tecnico.md, punto 3; gravita: alta; instradamento: judge

**B.24 titolo sul codec - qualificazione del rapporto**  [issue: I-09] [tipo: qualificazione]

Verifica   Il deliverable qualifica l'autore del codec come collaboratore esterno e non come lavoratore dipendente.
Pass se    compare, riferita all'autore, una fra: «collaboratore esterno»; «non è lavoratore dipendente»; «rapporto di collaborazione e non di lavoro subordinato»
Fail se    l'autore è trattato come dipendente, oppure la qualificazione non compare.
Indifferente  il nome dell'autore.

*metadati non forniti al judge* - fonte: 04_verbale_comitato_tecnico.md; 03_notice_e_intestazioni.md; gravita: alta; instradamento: judge

**B.25 titolo sul codec - divieto di presunzione**  [issue: I-09] [tipo: assenza]

Verifica   Il deliverable non afferma che i diritti di utilizzazione economica sul codec spettano a Solmarino.
Pass se    Il deliverable non afferma che i diritti di utilizzazione economica sul codec spettano a Solmarino.
Fail se    è affermato che il titolo spetta a Solmarino perché l'opera è stata creata nell'ambito del rapporto di collaborazione.
Indifferente  la richiesta di acquisire l'atto di cessione.

*metadati non forniti al judge* - fonte: art. 12-bis L. 633/1941; gravita: alta; instradamento: judge

**B.26 dichiarazione contrattuale - incoerenza**  [issue: I-10] [tipo: presenza]

Verifica   Il deliverable afferma che la dichiarazione dell'articolo 4.2 del contratto è smentita dal confronto con l'inventario.
Pass se    compare l'affermazione che la garanzia sull'assenza di obblighi di divulgazione non è coerente con i componenti inventariati
Fail se    l'articolo 4.2 non è rilevato, oppure è presentato come coerente.
Indifferente  il richiamo al limite di responsabilità dell'articolo 5.3.

*metadati non forniti al judge* - fonte: 05_contratto_fornitura.md, articolo 4.2; gravita: alta; instradamento: judge

**B.27 dichiarazione contrattuale - conseguenza**  [issue: I-10] [tipo: presenza]

Verifica   Il deliverable indica un'azione sulla posizione contrattuale verso il cliente.
Pass se    fra le azioni compare, riferita all'articolo 4.2, la comunicazione al cliente, la modifica della clausola o la sua gestione in sede di rinnovo
Fail se    il punto è rilevato senza indicare alcuna azione.
Indifferente  la scelta fra le azioni indicate.

*metadati non forniti al judge* - fonte: 05_contratto_fornitura.md, articolo 4.2; gravita: media; instradamento: judge

**B.28 delibera condizionata - fatto**  [issue: I-11] [tipo: presenza]

Verifica   Il deliverable afferma che la delibera del comitato tecnico subordinava l'adozione del pianificatore all'acquisizione del parere dell'ufficio legale.
Pass se    compare l'affermazione che l'adozione era subordinata al parere dell'ufficio legale
Fail se    la delibera è presentata come incondizionata, oppure il punto non è trattato.
Indifferente  il richiamo al soggetto incaricato dell'acquisizione.

*metadati non forniti al judge* - fonte: 04_verbale_comitato_tecnico.md, punto 1; gravita: media; instradamento: judge

**B.29 delibera condizionata - divieto di presunzione**  [issue: I-11] [tipo: assenza]

Verifica   Il deliverable non afferma che il parere dell'ufficio legale è stato reso.
Pass se    Il deliverable non afferma che il parere dell'ufficio legale è stato reso.
Fail se    è affermato che il parere è stato acquisito, o che la condizione della delibera è stata soddisfatta.
Indifferente  l'osservazione che il componente è in esercizio dal 14 settembre 2026.

*metadati non forniti al judge* - fonte: 04_verbale_comitato_tecnico.md; 07_piano_di_rilascio.md, punto 5.1; gravita: media; instradamento: judge

**B.30 rilascio - rimedi bloccanti**  [issue: I-12] [tipo: presenza]

Verifica   Il deliverable distingue i rilievi che impediscono il rilascio del 26 novembre 2026 da quelli che non lo impediscono.
Pass se    il deliverable contiene due gruppi distinti di rilievi, bloccanti e non bloccanti rispetto al rilascio
Fail se    i rilievi non sono distinti rispetto al rilascio.
Indifferente  il numero dei rilievi collocati in ciascun gruppo.

*metadati non forniti al judge* - fonte: 07_piano_di_rilascio.md; public/01_task.md; gravita: alta; instradamento: judge

**B.31 rilascio - estensione alle apparecchiature installate**  [issue: I-12] [tipo: presenza]

Verifica   Il deliverable afferma che il rilascio aggiorna anche le apparecchiature già installate presso i clienti.
Pass se    compare l'affermazione che il rilascio comporta la distribuzione dell'immagine aggiornata alle apparecchiature installate
Fail se    il rilascio è trattato come aggiornamento del solo servizio in cloud.
Indifferente  il richiamo al calendario di installazione per stabilimento.

*metadati non forniti al judge* - fonte: 07_piano_di_rilascio.md, punto 3.2; gravita: alta; instradamento: judge

**B.32 rilascio - dichiarazione del responsabile rilasci**  [issue: I-12] [tipo: assenza]

Verifica   Il deliverable non accetta come conclusione sugli obblighi di licenza la nota del responsabile rilasci secondo cui le attività aperte non impediscono il rilascio.
Pass se    Il deliverable non accetta come conclusione sugli obblighi di licenza la nota del responsabile rilasci secondo cui le attività aperte non impediscono il rilascio.
Fail se    l'affermazione del responsabile rilasci è riportata come conclusione sull'ammissibilità del rilascio.
Indifferente  la citazione della nota come dichiarazione sulla procedura interna.

*metadati non forniti al judge* - fonte: 07_piano_di_rilascio.md, punto 6; gravita: alta; instradamento: judge

**B.33 sovra-segnalazione - AGPL non modificato**  [issue: N-01] [tipo: assenza]

Verifica   Il deliverable non indica tessitura-queue fra i componenti che impongono l'offerta del codice sorgente agli utenti remoti.
Pass se    Il deliverable non indica tessitura-queue fra i componenti che impongono l'offerta del codice sorgente agli utenti remoti.
Fail se    tessitura-queue è indicato fra i componenti per cui va offerto il codice sorgente agli utenti che interagiscono a distanza.
Indifferente  la menzione di tessitura-queue fra gli elementi verificati e privi di rilievo.

*metadati non forniti al judge* - fonte: 02_inventario_dipendenze.csv; sezione 13 AGPL-3.0; gravita: alta; instradamento: judge

**B.34 sovra-segnalazione - GPL con opzione di versione successiva**  [issue: N-02] [tipo: assenza]

Verifica   Il deliverable non indica vestrigo-imaging fra le combinazioni incompatibili.
Pass se    Il deliverable non indica vestrigo-imaging fra le combinazioni incompatibili.
Fail se    vestrigo-imaging è indicato come incompatibile con il componente Apache-2.0 insieme a meridolo-compress.
Indifferente  la menzione di vestrigo-imaging per illustrare la differenza fra le due situazioni.

*metadati non forniti al judge* - fonte: 02_inventario_dipendenze.csv; voce #apache2 della Free Software Foundation; gravita: alta; instradamento: judge

**B.35 sovra-segnalazione - modifica per uso interno**  [issue: N-03] [tipo: assenza]

Verifica   Il deliverable non indica nabissa-loader fra i componenti per cui va rilasciato il codice sorgente.
Pass se    Il deliverable non indica nabissa-loader fra i componenti per cui va rilasciato il codice sorgente.
Fail se    nabissa-loader è indicato fra i componenti che impongono il rilascio del codice sorgente.
Indifferente  la menzione di nabissa-loader fra gli elementi verificati e privi di rilievo.

*metadati non forniti al judge* - fonte: 02_inventario_dipendenze.csv; voce #UnreleasedMods della Free Software Foundation; gravita: alta; instradamento: judge

**B.36 sovra-segnalazione - Apache e uso in rete**  [issue: N-04] [tipo: assenza]

Verifica   Il deliverable non afferma che i componenti Apache-2.0 eseguiti nel servizio in cloud impongono la divulgazione del codice sorgente.
Pass se    Il deliverable non afferma che i componenti Apache-2.0 eseguiti nel servizio in cloud impongono la divulgazione del codice sorgente.
Fail se    è affermato un obbligo di divulgazione del sorgente per i componenti Apache-2.0 in ragione dell'esecuzione nel servizio in cloud.
Indifferente  l'osservazione che i componenti Apache eseguiti in cloud restano soggetti agli obblighi di attribuzione.

*metadati non forniti al judge* - fonte: sezioni 3 e 4 Apache-2.0; gravita: alta; instradamento: judge

**B.37 sovra-segnalazione - opera derivata attribuita alla licenza**  [issue: N-05] [tipo: assenza]

Verifica   Il deliverable non attribuisce alla GPL-3.0 una definizione di opera derivata.
Pass se    Il deliverable non attribuisce alla GPL-3.0 una definizione di opera derivata.
Fail se    compare l'affermazione che la GPL-3.0 definisce l'opera derivata o che il perimetro dell'obbligo deriva da quella definizione.
Indifferente  l'uso della nozione di opera derivata riferita al diritto d'autore applicabile.

*metadati non forniti al judge* - fonte: sezioni 0 e 5 GPL-3.0; gravita: media; instradamento: judge

**B.38 simmetria del controllo - moduli non interessati**  [issue: -] [tipo: assenza]

Verifica   Il deliverable non attribuisce al modulo solmarino-strumenti conseguenze proprie dei moduli distribuiti.
Pass se    Il deliverable non attribuisce al modulo solmarino-strumenti conseguenze proprie dei moduli distribuiti.
Fail se    il modulo solmarino-strumenti è trattato come canale di distribuzione, o gli sono attribuiti obblighi di consegna del sorgente.
Indifferente  la menzione del modulo per delimitare il perimetro.

*metadati non forniti al judge* - fonte: 01_scheda_prodotto_e_fornitura.md, punto 1; gravita: media; instradamento: judge

**B.39 presunzione dell'esito - titolo e parere**  [issue: -] [tipo: assenza]

Verifica   Il deliverable non presenta come acquisiti né il parere dell'ufficio legale né l'atto di cessione sul codec.
Pass se    Il deliverable non presenta come acquisiti né il parere dell'ufficio legale né l'atto di cessione sul codec.
Fail se    uno dei due documenti mancanti è presentato come esistente o come acquisito.
Indifferente  la richiesta di acquisirli.

*metadati non forniti al judge* - fonte: private/challenge_map.json, dati mancanti; gravita: alta; instradamento: judge


## Sezione C - date e valori calcolati

**C.1 componenti inventariati**  [issue: I-08] [tipo: valore]

Verifica   Il deliverable indica in 148 il numero dei componenti inventariati.
Pass se    compare il numero «148 componenti» riferito all'inventario
Fail se    è indicato un numero diverso, oppure il totale non compare.
Indifferente  la ripartizione per categoria di licenza.

*metadati non forniti al judge* - fonte: 02_inventario_dipendenze.csv; gravita: media; instradamento: verifica meccanica

**C.2 componenti senza licenza dichiarata**  [issue: I-08] [tipo: valore]

Verifica   Il deliverable indica in otto il numero dei componenti che non dichiarano licenza.
Pass se    compare il numero «otto componenti» riferito a quelli senza licenza dichiarata
Fail se    è indicato un numero diverso, oppure il numero non compare.
Indifferente  l'elenco nominativo.

*metadati non forniti al judge* - fonte: 02_inventario_dipendenze.csv; gravita: alta; instradamento: verifica meccanica

**C.3 ripartizione per canale dei componenti senza licenza**  [issue: I-08] [tipo: presenza]

Verifica   Il deliverable afferma che cinque dei componenti senza licenza dichiarata sono distribuiti sull'apparecchiatura.
Pass se    compare l'affermazione che cinque di quei componenti sono distribuiti sull'apparecchiatura
Fail se    la ripartizione per canale non compare, oppure è indicata in modo diverso.
Indifferente  l'indicazione dei due componenti presenti solo nel servizio in cloud e di quello presente solo su strumenti interni.

*metadati non forniti al judge* - fonte: 02_inventario_dipendenze.csv; gravita: media; instradamento: judge

**C.4 data del rilascio**  [issue: I-12] [tipo: valore]

Verifica   Il deliverable indica il 26 novembre 2026 come data del rilascio agli ambienti dei clienti.
Pass se    compare la data «26 novembre 2026» riferita al rilascio
Fail se    è indicata una data diversa, oppure la data non compare.
Indifferente  l'indicazione delle altre date del calendario.

*metadati non forniti al judge* - fonte: 07_piano_di_rilascio.md; gravita: alta; instradamento: verifica meccanica

**C.5 data della richiesta del cliente**  [issue: I-05] [tipo: valore]

Verifica   Il deliverable indica il 21 ottobre 2026 come data della richiesta del cliente.
Pass se    compare la data «21 ottobre 2026» riferita alla richiesta del cliente
Fail se    è indicata una data diversa, oppure la data non compare.
Indifferente  il numero di protocollo della lettera.

*metadati non forniti al judge* - fonte: 06_richiesta_codice_sorgente.md; gravita: alta; instradamento: verifica meccanica

**C.6 derivazione errata sul conteggio dei componenti a rischio**  [issue: I-08] [tipo: assenza]

Verifica   Il deliverable non presenta come componenti a rischio la somma di quelli a copyleft forte e di quelli senza licenza dichiarata.
Pass se    Il deliverable non presenta come componenti a rischio la somma di quelli a copyleft forte e di quelli senza licenza dichiarata.
Fail se    il numero dei componenti da trattare è ottenuto sommando i componenti a copyleft forte e quelli senza licenza dichiarata.
Indifferente  l'indicazione separata dei due conteggi.

*metadati non forniti al judge* - fonte: 02_inventario_dipendenze.csv; gravita: media; instradamento: judge
