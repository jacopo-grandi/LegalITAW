Convenzione atomo v1. required = gravità alta; media e bassa = optional. Un atomo con punto di validazione aperto che potrebbe invertire il gold resta a media.
Gli atomi sono numerati solo A.n, B.n, C.n; il campo issue porta l'identificativo della rubrica (A-xx forma, I-xx merito, N-xx controlled non-issue, S-xx chiusura, C-xx derivazioni errate).
Inquadramento: alla data di riferimento (mercoledì 9 dicembre 2026, ore 10:00) l'istruttoria interna è in corso: la notifica all'autorità non risulta trasmessa e la decisione sulla comunicazione agli iscritti non è stata assunta. I passaggi di computo e i valori esatti stanno tutti in sezione C e non sono duplicati in sezione B.

A. FORMA DELL'OUTPUT

A.1 struttura delle voci
issue: A-01 · tipo: struttura · gravità: alta · judge: sì · fonte: prompt
Verifica: ogni voce dell'elenco riporta quattro elementi: adempimento, termine, decorrenza, stato.
Pass se: in ciascuna voce compaiono tutti e quattro gli elementi.
Fail se: in almeno una voce manca uno dei quattro elementi.

A.2 ancoraggio della decorrenza
issue: A-02 · tipo: struttura · gravità: media · judge: sì · fonte: prompt
Verifica: ogni decorrenza riporta il nome o il numero di un documento del fascicolo.
Pass se: in ciascuna voce compare un riferimento a un documento.
Fail se: almeno una decorrenza è priva di riferimento.

A.3 percorso di calcolo
issue: A-03 · tipo: presenza · gravità: media · judge: sì · fonte: prompt
Verifica: per ogni termine è riportato il calcolo seguito.
Pass se: per ciascun termine compare il passaggio da decorrenza a scadenza.
Fail se: almeno un termine riporta solo la data finale.

A.4 vocabolario dello stato
issue: A-04 · tipo: valore · gravità: media · judge: no · fonte: prompt
Verifica: lo stato di ciascun adempimento è espresso con una delle formulazioni ammesse per i quattro stati.
Pass se: ciascuno stato usa una fra: adempimento eseguito nei termini (rispettato, adempiuto, eseguito nei termini); termine già decorso (scaduto, decorso, non rispettato, fuori termine); adempimento da eseguire con termine non ancora decorso (pendente, in corso, da eseguire, non ancora scaduto); adempimento privo di termine di legge (senza termine, nessun termine di legge, adempimento continuativo).
Fail se: compare uno stato formulato fuori da questo elenco.

A.5 fonti nell'elenco chiuso
issue: A-05 · tipo: assenza · gravità: alta · judge: no · fonte: reference pack
Verifica: il deliverable non contiene riferimenti normativi estranei all'elenco chiuso delle fonti del reference pack.
Pass se: ogni riferimento normativo appartiene all'elenco.
Fail se: compare un riferimento fuori elenco.

B. MERITO

B.1 esclusione della riunione del comitato
issue: I-01 · tipo: assenza · gravità: media · judge: sì · fonte: All. 4 + All. 5, Sez. C.2 e C.3 + All. 6, scheda VIO-2026-005
Verifica: il deliverable non indica il 7 dicembre 2026 come momento in cui il titolare è venuto a conoscenza della violazione.
Pass se: il 7 dicembre non compare come momento della conoscenza.
Fail se: il 7 dicembre è indicato come momento della conoscenza.
Indifferente: la menzione della riunione del comitato come fatto.

B.2 esclusione dell'alert del monitoraggio
issue: I-01 · tipo: assenza · gravità: media · judge: sì · fonte: All. 1
Verifica: il deliverable non indica il 3 dicembre 2026 come momento in cui il titolare è venuto a conoscenza della violazione.
Pass se: il 3 dicembre non compare come momento della conoscenza.
Fail se: il 3 dicembre è indicato come momento della conoscenza.

B.3 obbligo di trasmettere comunque
issue: I-04 · tipo: presenza · gravità: alta · judge: sì · fonte: prompt, terza riga
Verifica: il deliverable afferma che la notifica all'autorità va trasmessa senza ulteriore ritardo.
Pass se: compare l'indicazione di trasmettere la notifica adesso, oppure subito, oppure senza ulteriore ritardo.
Fail se: il deliverable afferma che la notifica non è più dovuta, oppure rinvia la trasmissione a una data successiva.

B.4 motivi del ritardo
issue: I-04 · tipo: presenza · gravità: media · judge: sì · fonte: art. 33 par. 1 ultimo periodo + All. 5, Sez. C.4 (campo vuoto)
Verifica: il deliverable afferma che la notifica tardiva è corredata dei motivi del ritardo.
Pass se: l'indicazione dei motivi del ritardo compare.
Varianti accettate: «indicare i motivi del ritardo», «motivare il ritardo», «allegare la giustificazione del ritardo».
Fail se: non compare nessuna delle formulazioni ammesse.
Indifferente: il contenuto proposto per la motivazione.

B.5 bozza contro trasmissione
issue: I-05 · tipo: presenza · gravità: media · judge: sì · fonte: All. 5, campi di protocollo, data e ora di trasmissione e ricevuta vuoti
Verifica: il deliverable afferma che la bozza predisposta non è stata trasmessa all'autorità.
Pass se: la mancata trasmissione è affermata.
Varianti accettate: «la notifica non risulta trasmessa», «manca la ricevuta», «la bozza è rimasta interna».
Fail se: il deliverable tratta la notifica come già effettuata.

B.6 notifica per fasi
issue: I-06 · tipo: presenza · gravità: alta · judge: sì · fonte: All. 9; EDPB 9/2022, parr. 56-57 e 62
Verifica: il deliverable afferma che le informazioni mancanti possono essere fornite in un momento successivo alla prima notifica.
Pass se: la possibilità di integrare in un secondo momento è affermata.
Varianti accettate: «notifica per fasi», «notifica preliminare seguita da integrazione», «integrazione successiva».
Fail se: il deliverable subordina la notifica al completamento dell'analisi tecnica.

B.7 divieto di attendere il referto
issue: I-06 · tipo: assenza · gravità: media · judge: sì · fonte: All. 4, punto 3 + All. 6, scheda VIO-2026-005
Verifica: il deliverable non afferma che si deve attendere il referto definitivo del fornitore prima di notificare.
Pass se: non compare l'indicazione di attendere l'esito dell'analisi prima di notificare.
Fail se: compare tale indicazione.

B.8 comunicazione agli iscritti dovuta
issue: I-07 · tipo: presenza · gravità: alta · judge: sì · fonte: All. 9, sezione 1
Verifica: il deliverable afferma che la violazione va comunicata agli iscritti.
Pass se: compare l'indicazione di scrivere agli iscritti, oppure di comunicare la violazione agli interessati.
Fail se: il deliverable afferma che la comunicazione agli iscritti non è dovuta, oppure lascia la questione senza risposta.

B.9 natura delle attestazioni
issue: I-07 · tipo: qualificazione · gravità: alta · judge: sì · fonte: All. 9, sezione 1, prima riga
Verifica: il deliverable qualifica le attestazioni di invalidità civile presenti nelle registrazioni estratte come dati relativi alla salute.
Pass se: quelle attestazioni sono qualificate come categoria particolare di dati.
Varianti accettate: «dati relativi alla salute», «dati sanitari», «categoria particolare di dati», «dati particolari», «dati di cui all'art. 9».
Fail se: quelle attestazioni restano qualificate come normali dati anagrafici o documentali, oppure la qualificazione non compare.
Indifferente: la citazione dell'articolo.

B.10 assenza di un termine di 72 ore verso gli iscritti
issue: I-08 · tipo: assenza · gravità: alta · judge: sì · fonte: art. 34 par. 1
Verifica: il deliverable non indica un termine di 72 ore per la comunicazione agli iscritti.
Pass se: le 72 ore sono riferite soltanto alla notifica all'autorità.
Fail se: le 72 ore sono riferite anche alla comunicazione agli iscritti.

B.11 tempistica della comunicazione agli iscritti
issue: I-08 · tipo: presenza · gravità: media · judge: sì · fonte: prompt, quarta riga
Verifica: il deliverable afferma che la comunicazione agli iscritti va effettuata senza ingiustificato ritardo.
Pass se: la tempistica è espressa senza indicazione di una scadenza fissa.
Varianti accettate: «senza ingiustificato ritardo», «senza indugio», «il prima possibile».
Fail se: è indicata una scadenza a giorni o a ore, oppure la tempistica non compare.

B.12 archivio cifrato fuori perimetro
issue: N-03 · tipo: assenza · gravità: media · judge: sì · fonte: All. 9, sezione 1, terza riga
Verifica: il deliverable non include nel perimetro della comunicazione agli iscritti gli interessati dell'archivio di backup cifrato.
Pass se: l'archivio cifrato non compare tra le ragioni per avvisare gli iscritti.
Fail se: il perimetro è esteso all'archivio cifrato.
Indifferente: la menzione dell'archivio nella descrizione dell'accaduto.

B.13 credenziali: decisione motivata sul perimetro
issue: I-10 · tipo: presenza · gravità: alta · judge: sì · fonte: All. 9, sezione 1, seconda riga + All. 3, corpo lett. a
Verifica: il deliverable valuta espressamente se includere nella comunicazione anche i 41.027 utenti le cui email e credenziali non reversibili sono state esposte.
Pass se: il deliverable prende una posizione motivata, considerando almeno il carattere non reversibile delle credenziali e il rischio residuo collegato agli indirizzi email, come phishing o credential stuffing.
Fail se: i 41.027 utenti sono ignorati, oppure inclusi o esclusi senza motivazione.
Indifferente: la conclusione adottata; la raccomandazione di reimpostare le password.

B.14 ritardo del responsabile
issue: I-11 · tipo: presenza · gravità: alta · judge: sì · fonte: All. 7 clausola 9.2 + All. 2 (4/12 ore 09:10) + All. 3 (messaggio del 5/12 ore 18:40)
Verifica: il deliverable afferma che il responsabile ha comunicato la violazione al titolare oltre il termine di 24 ore previsto dal contratto.
Pass se: il superamento del termine contrattuale è affermato.
Varianti accettate: «comunicazione oltre le 24 ore», «termine contrattuale non rispettato», «inadempimento della clausola 9.2».
Fail se: il deliverable afferma che il termine contrattuale è stato rispettato, oppure il tema non compare.
Indifferente: l'ora esatta della scadenza contrattuale.

B.15 il termine contrattuale non anticipa la decorrenza
issue: I-11 · tipo: assenza · gravità: media · judge: sì · fonte: All. 2 + All. 3, corpo lett. a
Verifica: il deliverable non fa decorrere il termine di notifica all'autorità dal 4 dicembre 2026.
Pass se: il 4 dicembre non compare come decorrenza del termine verso l'autorità.
Fail se: il 4 dicembre è usato come decorrenza di quel termine.

B.16 registro senza termine
issue: N-06 · tipo: qualificazione · gravità: media · judge: sì · fonte: All. 6 (registro aggiornato al 9/12/2026; art. 33 par. 5, che non fissa alcun termine)
Verifica: il deliverable qualifica la registrazione della violazione nel registro come adempimento senza termine di legge.
Pass se: al registro non è assegnato un termine di legge.
Varianti accettate: «senza termine», «nessun termine di legge», «adempimento continuativo».
Fail se: al registro è assegnata una data di scadenza.
Indifferente: l'indicazione di aggiornarlo subito come buona prassi.

B.17 evento del 30 novembre non notificabile
issue: N-05 · tipo: assenza · gravità: media · judge: sì · fonte: All. 8, conferma di cancellazione da parte di un ente in rapporto continuativo
Verifica: il deliverable non indica la notifica all'autorità tra gli adempimenti relativi all'invio del 30 novembre 2026 al destinatario errato.
Pass se: per quell'evento non è prevista la notifica all'autorità.
Fail se: per quell'evento è prevista la notifica all'autorità.

B.18 scheda di registro del 30 novembre da completare
issue: I-13 · tipo: presenza · gravità: media · judge: sì · fonte: All. 6, scheda VIO-2026-004 (campi Notifica al Garante, Comunicazione agli interessati e Valutazione registrata vuoti, verificato sull'allegato in revisione 18/08/2026)
Verifica: il deliverable afferma che la scheda di registro dell'invio del 30 novembre 2026 va completata con la valutazione e con l'esito su notifica e comunicazione.
Pass se: il completamento della scheda è indicato fra gli adempimenti.
Varianti accettate: «completare la scheda VIO-2026-004», «chiudere la scheda del 30 novembre», «registrare la valutazione dell'evento del 30 novembre», «formalizzare nel registro l'esito di quell'evento».
Fail se: l'evento non compare tra gli adempimenti, oppure è dichiarato irrilevante, oppure il deliverable afferma che la scheda è già completa.
Indifferente: l'indicazione che la scheda esiste già.

B.19 nessuna notifica cumulativa
issue: I-14 · tipo: assenza · gravità: media · judge: sì · fonte: All. 6 + All. 8
Verifica: il deliverable non propone di notificare i due eventi in un'unica notifica.
Pass se: i due eventi restano trattati separatamente.
Fail se: è proposta una notifica unica o cumulativa dei due eventi.

B.20 tentativo bloccato
issue: N-01 · tipo: assenza · gravità: media · judge: sì · fonte: All. 1, EVT-6702
Verifica: il deliverable non qualifica come violazione dei dati personali il tentativo di injection bloccato dai controlli il 2 dicembre 2026.
Pass se: quel tentativo non compare tra le violazioni né genera adempimenti.
Fail se: il tentativo è qualificato come violazione o gli è associato un termine.
Indifferente: la sua menzione come evento di sicurezza.

B.21 manutenzione programmata
issue: N-02 · tipo: assenza · gravità: media · judge: sì · fonte: All. 1, EVT-6621
Verifica: il deliverable non qualifica come violazione dei dati personali l'indisponibilità del portale nella finestra di manutenzione del 29 novembre 2026.
Pass se: quell'indisponibilità non compare tra le violazioni né genera adempimenti.
Fail se: è qualificata come violazione o le è associato un termine.

B.22 soggetto obbligato
issue: N-07 · tipo: assenza · gravità: media · judge: sì · fonte: All. 5, Sez. A e B1
Verifica: il deliverable non attribuisce al responsabile della protezione dei dati l'obbligo di notificare all'autorità.
Pass se: l'obbligo è attribuito al titolare, oppure il soggetto obbligato non è nominato.
Fail se: l'obbligo è attribuito al responsabile della protezione dei dati.
Indifferente: l'indicazione del responsabile della protezione dei dati come punto di contatto o come estensore.

B.23 simmetria sull'integrità
issue: S-01 · tipo: assenza · gravità: media · judge: sì · fonte: All. 9, sezione 3 + All. 3, corpo lett. c
Verifica: il deliverable non afferma che i dati sono stati modificati o cancellati.
Pass se: non compare l'affermazione di una modifica o di una cancellazione dei dati.
Fail se: compare tale affermazione.

B.24 divieto di presunzione dell'esito
issue: S-03 · tipo: assenza · gravità: media · judge: sì · fonte: All. 9, esito tecnico non determinato
Verifica: il deliverable non afferma che i contenuti estratti sono stati diffusi o pubblicati.
Pass se: non compare l'affermazione di una diffusione o pubblicazione avvenuta.
Fail se: compare tale affermazione.
Indifferente: l'indicazione del rischio che ciò avvenga.

C. VALORI CALCOLATI

C.1 decorrenza
issue: I-01 · tipo: valore · gravità: alta · judge: no · fonte: All. 3, intestazioni del messaggio (Date/Received 5/12/2026 ore 18:40)
Verifica: il deliverable indica come decorrenza del termine di notifica all'autorità il 5 dicembre 2026.
Pass se: compare quella data come decorrenza, con o senza l'ora.
Fail se: compare un'altra data.
Indifferente: l'indicazione dell'ora e del fuso orario.

C.2 computo continuo
issue: I-02 · tipo: presenza · gravità: alta · judge: sì · fonte: reg. (CEE, Euratom) 1182/71, art. 3, par. 3 + calendario 5-8 dicembre 2026
Verifica: il deliverable afferma che nel computo delle 72 ore rientrano il sabato, la domenica e il giorno festivo.
Pass se: la continuità del computo è affermata.
Varianti accettate: «i giorni festivi e il fine settimana rientrano nel computo», «il termine corre anche di sabato e domenica», «il computo è continuo», «72 ore consecutive», «ore naturali e consecutive», «il termine non si sospende nei giorni festivi», «il termine non si sospende nel fine settimana».
Fail se: il deliverable esclude dal computo il fine settimana o il festivo, oppure non si pronuncia.

C.3 nessuna proroga
issue: I-03 · tipo: presenza · gravità: alta · judge: sì · fonte: reg. 1182/71, art. 3, par. 4 (il differimento riguarda i periodi espressi non in ore) + 8 dicembre 2026 festivo
Verifica: il deliverable afferma che la scadenza non si sposta al primo giorno lavorativo successivo pur cadendo in giorno festivo.
Pass se: l'assenza di proroga è affermata.
Varianti accettate: «non si applica la proroga», «il termine non slitta», «la scadenza resta l'8 dicembre nonostante la festività», «il termine in ore non si proroga», «la proroga al primo giorno lavorativo successivo non si applica ai termini in ore», «l'8 dicembre resta il giorno di scadenza benché festivo».
Fail se: il deliverable sposta la scadenza al 9 dicembre o a un giorno successivo per effetto della festività.

C.4 scadenza della notifica
issue: I-03 · tipo: valore · gravità: alta · judge: no · fonte: 5/12/2026 ore 18:40 più 72 ore; l'ora nel corso della quale si verifica l'evento non si computa (reg. 1182/71, art. 3, par. 1), da cui le ore 19:00
Verifica: il deliverable indica come scadenza della notifica all'autorità martedì 8 dicembre 2026.
Pass se: compare la data 8 dicembre 2026; se è indicata anche l'ora, sono ammesse le ore 19:00 e le ore 18:40.
Fail se: compare un'altra data.

C.5 stato del termine
issue: I-04 · tipo: valore · gravità: alta · judge: no · fonte: All. 5 senza ricevuta + data di riferimento 9/12/2026 ore 10:00
Verifica: il deliverable indica il termine di notifica all'autorità come scaduto alla data di riferimento.
Pass se: compare, riferita a quel termine, una fra scaduto, decorso, non rispettato.
Fail se: compare pendente o rispettato, oppure lo stato non compare.

C.6 derivazione errata: proroga per festivo
issue: C-06 · tipo: assenza · gravità: media · judge: sì · fonte: diagnostica
Verifica: il deliverable non indica il 9 dicembre 2026 come scadenza della notifica.
Pass se: quella data non compare come scadenza.
Fail se: compare come scadenza.
Indifferente: la menzione del 9 dicembre 2026 come data di riferimento.

C.7 derivazione errata: 72 ore dalla riunione
issue: C-06 · tipo: assenza · gravità: media · judge: sì · fonte: diagnostica
Verifica: il deliverable non presenta il 10 dicembre 2026 come risultato di 72 ore decorrenti dalla riunione del comitato del 7 dicembre.
Pass se: quel calcolo non compare.
Fail se: compare.

B.25 aggiornamento della scheda VIO-2026-005
issue: I-16 · tipo: presenza · gravità: media · judge: sì · fonte: All. 6, scheda VIO-2026-005 + All. 9
Verifica: il deliverable indica fra le azioni immediate l'aggiornamento delle categorie di dati nella scheda VIO-2026-005 sulla base del referto già disponibile.
Pass se: è richiesto di completare o aggiornare il registro con le categorie accertate nel referto.
Fail se: la scheda è trattata come completa, oppure l'aggiornamento non compare fra le azioni.

C.8 derivazione errata: tre giorni lavorativi
issue: C-06 · tipo: assenza · gravità: media · judge: sì · fonte: diagnostica
Verifica: il deliverable non presenta il 10 dicembre 2026 come risultato di un computo in giorni lavorativi.
Pass se: quel calcolo non compare.
Fail se: compare.

C.9 derivazione errata: computo dall'alert del monitoraggio
issue: C-06 · tipo: assenza · gravità: media · judge: no · fonte: diagnostica (3/12/2026 ore 23:47 più 72 ore uguale domenica 6/12/2026 ore 23:47)
Verifica: il deliverable non presenta il 6 dicembre 2026 come scadenza calcolata dall'alert del monitoraggio del 3 dicembre.
Pass se: quel calcolo non compare.
Fail se: compare.

C.10 interessati da avvisare
issue: I-09 · tipo: valore · gravità: alta · judge: sì · fonte: All. 9, sezione 1 + All. 3, corpo lett. a
Verifica: il deliverable identifica 12.400 interessati come perimetro minimo certamente destinatario della comunicazione.
Pass se: compare il numero 12.400 come gruppo certamente da avvisare, anche se il deliverable propone motivatamente di estendere la comunicazione ai 41.027 utenti valutati in B.13.
Fail se: i 12.400 interessati non sono inclusi nel perimetro, oppure il perimetro minimo non è quantificato.
Indifferente: un perimetro finale più ampio, se motivato; l'indicazione che il numero è approssimativo.

C.11 registrazioni con attestazione di invalidità
issue: I-07 · tipo: valore · gravità: alta · judge: no · fonte: All. 9, sezione 1
Verifica: il deliverable indica in 380 le registrazioni estratte in chiaro che contengono un'attestazione di invalidità civile.
Pass se: compare il numero 380 riferito alle attestazioni di invalidità o ai dati sulla salute.
Fail se: quel dato non compare.

RACCORDO ISSUE → ATOMI

A-01 → A.1 · A-02 → A.2 · A-03 → A.3 · A-04 → A.4 · A-05 → A.5.
I-01 → B.1, B.2, C.1 · I-02 → C.2 · I-03 → C.3, C.4 · I-04 → B.3, B.4, C.5 · I-05 → B.5 · I-06 → B.6, B.7 · I-07 → B.8, B.9, C.11 · I-08 → B.10, B.11 · I-09 → C.10 · I-10 → B.13 · I-11 → B.14, B.15 · I-12 → B.16 · I-13 → B.17, B.18 · I-14 → B.19 · I-15 → B.20.
N-01 → B.20 · N-02 → B.21 · N-03 → B.12 · N-04 → B.13 · N-05 → B.17 · N-06 → B.16 · N-07 → B.22.
S-01 → B.23 · S-02 → B.12, B.13, B.16, B.17, B.20, B.21, B.22 (un divieto nominato per ciascun controlled non-issue) · S-03 → B.24.
C-06 → C.6, C.7, C.8, C.9.
Nessun atomo orfano, nessun issue scoperto. 40 atomi: 5 forma, 24 merito, 11 valori calcolati. Required 15, optional 25. Judge sì 34, judge no 6.
Quattro atomi portano un doppio riferimento nella versione precedente (I-09/N.3, I-10/N.4, I-12/N.6, I-15/N.1): il campo issue ora ne porta uno solo e il doppio legame è registrato qui nel raccordo, così da non avere due identificativi in un campo che deve restare a valore singolo.
Nessun atomo è duplicato fra B e C: i passaggi di computo e i valori esatti stanno solo in C e portano l'identificativo dell'issue di merito, così che un solo errore non faccia cadere due issue.

NOTA DI BUILD

Workflow: deadline_chain (deadline audit). Use-case family impostata su Procedural timeline in mancanza di un'opzione dedicata sul board, come già fatto per review_only.

Diversità rispetto ai due deadline_chain esistenti (civile e insolvenza): variano verticale (data protection), meccanismo (termine in ore, dove il festivo non proroga: inversione, non ripetizione, della catena di festività degli altri due) e forma del deliverable (audit multi-adempimento con qualificazione degli eventi, non catena su un unico termine).

Grounding verificato su fonte per i non-issue e per gli issue portanti (linee guida EDPB 9/2022): par. 21 manutenzione programmata non è violazione di sicurezza (N-02); par. 114 destinatario affidabile in rapporto continuativo, rischio neutralizzato ma obbligo di documentazione fermo (N-05 e I-13); par. 64 notifica cumulativa solo per stesso tipo di dati violati nello stesso modo (I-14); par. 76-78 dati cifrati con chiave non compromessa e backup disponibile (N-03, N-04); par. 102 danno probabile quando la violazione riguarda dati relativi alla salute (I-07); par. 15 non ogni incidente di sicurezza è una violazione (I-15); par. 56-57 e 62 notifica per fasi e motivi del ritardo (I-06, I-04). Il computo delle 72 ore è rinviato dalle stesse linee guida (nota 27) al reg. (CEE, Euratom) 1182/71.

Elenco chiuso delle fonti del reference pack (serve ad A.5, resta in busta privata): artt. 4 n. 12, 9, 33 e 34 GDPR; reg. (CEE, Euratom) 1182/71, art. 3; linee guida EDPB 9/2022; clausole 9.1 e 9.2 dell'accordo sul trattamento (All. 7).

Revisione allegati 18/08/2026: nella scheda VIO-2026-004 dell'All. 6 sono stati svuotati i campi Notifica al Garante, Comunicazione agli interessati e Valutazione registrata. Erano compilati e producevano due difetti: rendevano falso il criterio su I-13 e anticipavano nel documento la conclusione del non-issue N-05, in violazione della regola sul non scrivere nel documento la regola o l'esito che l'agente deve dedurre.

Resta non misurato, per scelta: la scheda VIO-2026-005 riporta ancora «categorie di dati in corso di determinazione» pur essendo il registro aggiornato al 9 dicembre e il referto agli atti dall'8 dicembre. Coincidenza di build, non trappola: nessun criterio la premia o la penalizza.

Decisioni pilot confermate il 24 agosto 2026:
1. Il momento della conoscenza coincide con la comunicazione ricevuta dal responsabile; C.1 resta alta.
2. L'estrazione in chiaro delle 12.400 posizioni costituisce il perimetro minimo certo della comunicazione.
3. Sui 41.027 indirizzi email il gold accetta entrambe le conclusioni, purché motivate considerando insieme hashing e rischio residuo di phishing o credential stuffing.
4. L'All. 7 è qualificato come accordo individuale ex art. 28 GDPR; non è presentato come riproduzione invariata delle SCC 2021/915.
5. C.4 ammette sia le ore 19:00 sia le 18:40 e, come risposta minima, il solo giorno 8 dicembre.

Il sign-off legale blind del gold resta uno stato separato e non riapre questi bivi di design.
