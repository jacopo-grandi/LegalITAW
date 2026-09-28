# WF2-035 — Rubrica atomizzata

Forma a campi somministrata al judge e alla verifica meccanica. Generato da `source/gen/build_rubric_035.py` insieme a `private/rubric.json`: non modificare a mano.

Issue di merito: 15. Criteri atomici: 49, di cui 11 a verifica meccanica e 38 al judge.

---

## A. Forma dell'output  (interamente verifica meccanica)

### A.1  [issue: A]  [tipo: valore]  [verifica meccanica]

**Verifica** — il deliverable è un file denominato timeline_rimedi.md di lunghezza non superiore a 1.800 parole.

**Pass se** — il file si chiama timeline_rimedi.md e il conteggio delle parole non supera 1.800

**Fail se** — il nome del file è diverso oppure il conteggio supera 1.800 parole.

<small>—— non passa al judge —— Fonte: response_template.md · Gravità: bassa</small>

### A.2  [issue: A]  [tipo: struttura]  [verifica meccanica]

**Verifica** — il deliverable contiene, nell'ordine, sette sezioni intitolate: Timeline degli adempimenti e dei rimedi; Come ho ricavato ogni scadenza; Adempimenti da compiere e in quale ordine; Rimedi non più esperibili; Date e valori non determinanti; Verifica dei conti e delle valutazioni dell'ufficio gare; Che cosa non è determinabile allo stato e che cosa serve.

**Pass se** — le sette intestazioni compaiono tutte e nell'ordine indicato

**Fail se** — manca una intestazione oppure l'ordine è diverso.

<small>—— non passa al judge —— Fonte: response_template.md · Gravità: bassa</small>

### A.3  [issue: A]  [tipo: struttura]  [verifica meccanica]

**Verifica** — ogni riga della tabella della sezione 1 riporta, nella colonna della fonte, un riferimento a un documento del fascicolo oppure a una norma.

**Pass se** — nessuna riga della tabella della sezione 1 ha la colonna della fonte vuota

**Fail se** — almeno una riga della tabella della sezione 1 non riporta alcun riferimento di fonte.

<small>—— non passa al judge —— Fonte: response_template.md · Gravità: media</small>

### A.4  [issue: A]  [tipo: assenza]  [verifica meccanica]

**Verifica** — il deliverable non contiene riferimenti normativi o giurisprudenziali diversi da quelli elencati nella tabella dell'elenco chiuso di 03_legal_sources.md.

**Pass se** — tutti i riferimenti normativi e giurisprudenziali presenti nel deliverable compaiono nell'elenco chiuso

**Fail se** — compare un riferimento normativo o giurisprudenziale estraneo all'elenco chiuso.

<small>—— non passa al judge —— Fonte: 03_legal_sources.md · Gravità: alta</small>

### A.5  [issue: A]  [tipo: struttura]  [verifica meccanica]

**Verifica** — ogni riga della tabella della sezione 1 riporta lo stato della voce alla data di riferimento.

**Pass se** — nessuna riga della tabella della sezione 1 ha la colonna dello stato vuota

**Fail se** — almeno una riga della tabella della sezione 1 non indica lo stato alla data di riferimento.

<small>—— non passa al judge —— Fonte: response_template.md · Gravità: media</small>

---

## B. Merito

Fascicolo in corso alla data di riferimento del 18 novembre 2027: l'aggiudicazione è stata comunicata, gli atti sono stati messi a disposizione in due momenti distinti, il contratto non è stato stipulato e il concorrente secondo classificato non ha depositato alcun atto. I criteri riguardano lo stato del fascicolo a quella data, i termini che ne derivano e i rimedi ancora esperibili; non riguardano la fondatezza delle censure né l'esito del ricorso.

### B.1  [issue: I-01]  [tipo: qualificazione]  [judge]

**Verifica** — il deliverable qualifica come fatto da cui decorre il termine per impugnare l'aggiudicazione la ricezione della comunicazione di aggiudicazione, individuata nella consegna in piattaforma.

**Pass se** — compare una fra le formulazioni seguenti:
- compare, riferita al termine per impugnare, una fra: «dalla ricezione della comunicazione»
- «dalla consegna in piattaforma»
- «dalla data di consegna registrata dalla piattaforma»
- «dalla comunicazione ex art. 90 ricevuta il 25 ottobre 2027»

**Fail se** — il termine è fatto decorrere dalla pubblicazione dell'avviso, dall'adozione della determina, dalla presa visione o dalla data del verbale.

**Indifferente** — la citazione dell'art. 120, comma 2, c.p.a.: né richiesta né penalizzata.

<small>—— non passa al judge —— Fonte: documenti 05 e 06; art. 120, comma 2, c.p.a. · Gravità: alta</small>

### B.2  [issue: I-01]  [tipo: attribuzione]  [judge]

**Verifica** — il deliverable riconduce la data di decorrenza del primo termine all'estratto del registro di sistema della piattaforma.

**Pass se** — compare una fra le formulazioni seguenti:
- la decorrenza è agganciata a una fra: «estratto del registro di sistema»
- «registro di sistema della piattaforma»
- «data di consegna registrata dal sistema»
- «documento 06»

**Fail se** — la decorrenza non è agganciata ad alcun documento, oppure è agganciata soltanto al testo della comunicazione senza il dato della consegna.

<small>—— non passa al judge —— Fonte: documento 06 · Gravità: media</small>

### B.3  [issue: I-02]  [tipo: presenza]  [judge]

**Verifica** — il deliverable afferma che alla data di riferimento il termine per la notificazione del ricorso principale è ancora pendente.

**Pass se** — compare una fra le formulazioni seguenti:
- compare, riferita a quel termine, una fra: «è ancora pendente»
- «non è ancora scaduto»
- «è in corso»
- «restano … giorni»

**Fail se** — il termine è presentato come scaduto, oppure il suo stato non è indicato.

<small>—— non passa al judge —— Fonte: art. 120, comma 2, c.p.a. · Gravità: alta</small>

### B.4  [issue: I-03]  [tipo: presenza]  [judge]

**Verifica** — il deliverable afferma che per le censure che solo la relazione tecnica dell'aggiudicataria rivela il termine decorre dal momento in cui quell'atto è stato messo a disposizione.

**Pass se** — compare una fra le formulazioni seguenti:
- compare l'affermazione che il termine decorre dalla messa a disposizione degli atti
- compare l'affermazione che il termine decorre dall'ostensione della relazione tecnica
- compare l'affermazione che il termine decorre dalla disponibilità dell'offerta tecnica dell'aggiudicataria

**Fail se** — il deliverable fa decorrere il termine per tutte le censure dalla sola comunicazione di aggiudicazione.

<small>—— non passa al judge —— Fonte: documento 07; art. 120, comma 2, c.p.a. · Gravità: alta</small>

### B.5  [issue: I-03]  [tipo: attribuzione]  [judge]

**Verifica** — il deliverable riconduce la decorrenza del secondo termine al provvedimento sulle richieste di oscuramento.

**Pass se** — compare una fra le formulazioni seguenti:
- la decorrenza del secondo termine è agganciata a una fra: «provvedimento sulle richieste di oscuramento»
- «provvedimento del 16 novembre 2027»
- «documento 07»
- «seconda comunicazione in piattaforma»

**Fail se** — la decorrenza del secondo termine non è agganciata ad alcun documento.

<small>—— non passa al judge —— Fonte: documento 07; documento 06 · Gravità: media</small>

### B.6  [issue: I-04]  [tipo: presenza]  [judge]

**Verifica** — il deliverable afferma che il termine per impugnare non è unico e dipende dall'atto da cui la singola censura è conoscibile.

**Pass se** — compare una fra le formulazioni seguenti:
- compare l'affermazione che esistono due termini distinti a seconda della censura
- compare l'affermazione che il termine dipende dall'atto da cui il vizio è conoscibile
- compare l'affermazione che non è possibile indicare una sola scadenza per tutte le censure

**Fail se** — il deliverable presenta un termine unico senza indicare da che cosa dipenda.

<small>—— non passa al judge —— Fonte: art. 120, comma 2, c.p.a., che pone due decorrenze in alternativa · Gravità: alta</small>

### B.7  [issue: I-04]  [tipo: assenza]  [judge]

**Verifica** — il deliverable non presenta il 24 novembre 2027 come termine ultimo per far valere anche la censura sull'attribuzione del punteggio sul criterio B.2.

**Pass se** — il 24 novembre 2027 non è indicato come scadenza della censura sul punteggio del criterio B.2

**Fail se** — il 24 novembre 2027 è presentato come scadenza valida anche per quella censura.

<small>—— non passa al judge —— Fonte: documento 07; art. 120, comma 2, c.p.a. · Gravità: alta</small>

### B.8  [issue: I-05]  [tipo: presenza]  [judge]

**Verifica** — il deliverable afferma che il termine per la notificazione del ricorso introduttivo non è dimezzato.

**Pass se** — compare una fra le formulazioni seguenti:
- compare, riferita alla notificazione del ricorso introduttivo, una fra: «non è dimezzato»
- «resta di trenta giorni»
- «è sottratto al dimezzamento»
- «il dimezzamento non si applica»

**Fail se** — il deliverable non tratta il punto, oppure afferma che quel termine è dimezzato.

**Indifferente** — la citazione dell'art. 119, comma 2, c.p.a.

<small>—— non passa al judge —— Fonte: art. 119, comma 2, c.p.a. · Gravità: alta</small>

### B.9  [issue: I-05]  [tipo: assenza]  [judge]

**Verifica** — il deliverable non indica in quindici giorni il termine per la notificazione del ricorso introduttivo.

**Pass se** — il termine per la notificazione del ricorso introduttivo non è indicato in quindici giorni

**Fail se** — il termine per la notificazione del ricorso introduttivo è indicato in quindici giorni.

<small>—— non passa al judge —— Fonte: art. 119, comma 2, c.p.a. · Gravità: alta</small>

### B.10  [issue: I-06]  [tipo: presenza]  [judge]

**Verifica** — il deliverable indica in quindici giorni il termine per il deposito del ricorso.

**Pass se** — compare «quindici giorni» oppure «15 giorni» riferito al deposito del ricorso

**Fail se** — è indicato un termine diverso per il deposito, oppure il deposito non è trattato.

<small>—— non passa al judge —— Fonte: artt. 45, comma 1, e 119, comma 2, c.p.a. · Gravità: alta</small>

### B.11  [issue: I-06]  [tipo: attribuzione]  [judge]

**Verifica** — il deliverable fa decorrere il termine per il deposito dal perfezionamento dell'ultima notificazione.

**Pass se** — compare una fra le formulazioni seguenti:
- la decorrenza del termine di deposito è agganciata a una fra: «perfezionamento dell'ultima notificazione»
- «ultima notificazione perfezionata anche per il destinatario»
- «perfezionamento della notifica nei confronti dell'ultimo destinatario»

**Fail se** — la decorrenza del termine di deposito è agganciata alla data di ricezione della comunicazione di aggiudicazione o alla data di sottoscrizione del ricorso.

<small>—— non passa al judge —— Fonte: art. 45, comma 1, c.p.a. · Gravità: media</small>

### B.12  [issue: I-07]  [tipo: presenza]  [judge]

**Verifica** — il deliverable afferma che il termine di dieci giorni per impugnare le decisioni sulle richieste di oscuramento è scaduto.

**Pass se** — compare una fra le formulazioni seguenti:
- compare, riferito a quel rimedio, una fra: «è scaduto»
- «è decorso»
- «non è più esperibile»
- «non è più possibile»

**Fail se** — quel termine è presentato come pendente, oppure il punto non è trattato.

<small>—— non passa al judge —— Fonte: art. 36, comma 4, d.lgs. 36/2023 · Gravità: alta</small>

### B.13  [issue: I-07]  [tipo: assenza]  [judge]

**Verifica** — il deliverable non indica il ricorso contro le decisioni sulle richieste di oscuramento fra i rimedi ancora esperibili alla data di riferimento.

**Pass se** — quel ricorso non compare nell'elenco dei rimedi da esperire

**Fail se** — quel ricorso è indicato fra gli adempimenti da compiere.

<small>—— non passa al judge —— Fonte: art. 36, comma 4, d.lgs. 36/2023 · Gravità: alta</small>

### B.14  [issue: I-08]  [tipo: presenza]  [judge]

**Verifica** — il deliverable afferma che il termine dilatorio per la stipulazione del contratto è di trentadue giorni.

**Pass se** — compare «trentadue giorni» oppure «32 giorni» riferito al termine dilatorio

**Fail se** — è indicato un numero di giorni diverso, oppure la durata del termine dilatorio non è indicata.

**Indifferente** — l'indicazione dell'evento da cui i trentadue giorni decorrono, se la data di scadenza indicata è quella corretta.

<small>—— non passa al judge —— Fonte: art. 18, comma 3, d.lgs. 36/2023 · Gravità: alta</small>

### B.15  [issue: I-08]  [tipo: assenza]  [judge]

**Verifica** — il deliverable non afferma che il termine dilatorio per la stipulazione del contratto è di trentacinque giorni.

**Pass se** — non compare «trentacinque giorni» né «35 giorni» riferito al termine dilatorio

**Fail se** — il termine dilatorio è indicato in trentacinque giorni.

<small>—— non passa al judge —— Fonte: art. 18, comma 3, d.lgs. 36/2023 · Gravità: alta</small>

### B.16  [issue: I-09]  [tipo: presenza]  [judge]

**Verifica** — il deliverable afferma che la notificazione del ricorso con contestuale domanda cautelare impedisce la stipulazione del contratto dal momento della notificazione.

**Pass se** — compare una fra le formulazioni seguenti:
- compare l'affermazione che la notificazione dell'istanza cautelare sospende la stipulazione
- compare l'affermazione che il contratto non può essere stipulato dal momento della notificazione della domanda cautelare
- compare l'affermazione che la notificazione produce la sospensione obbligatoria del termine per la stipulazione

**Fail se** — l'effetto non è indicato, oppure è ricondotto a un'attività diversa dalla notificazione.

<small>—— non passa al judge —— Fonte: art. 18, comma 4, d.lgs. 36/2023 · Gravità: alta</small>

### B.17  [issue: I-09]  [tipo: assenza]  [judge]

**Verifica** — il deliverable non afferma che, per impedire la stipulazione del contratto, occorre che il giudice conceda una misura cautelare.

**Pass se** — non compare l'affermazione che l'effetto impeditivo dipenda dalla concessione della misura cautelare

**Fail se** — l'effetto impeditivo è subordinato all'accoglimento della domanda cautelare.

<small>—— non passa al judge —— Fonte: art. 18, comma 4, d.lgs. 36/2023 · Gravità: alta</small>

### B.18  [issue: I-10]  [tipo: presenza]  [judge]

**Verifica** — il deliverable afferma che l'effetto sospensivo della stipulazione cessa se il giudice si dichiara incompetente oppure se fissa la data di discussione del merito senza pronunciarsi sulle misure cautelari con il consenso delle parti.

**Pass se** — compaiono entrambe le ipotesi di cessazione: la dichiarazione di incompetenza e la fissazione del merito senza pronuncia cautelare con il consenso delle parti

**Fail se** — nessuna delle due ipotesi compare, oppure ne compare una sola.

<small>—— non passa al judge —— Fonte: art. 18, comma 4, secondo periodo, d.lgs. 36/2023 · Gravità: media</small>

### B.19  [issue: I-11]  [tipo: presenza]  [judge]

**Verifica** — il deliverable afferma che la presentazione di un'istanza di parere di precontenzioso all'ANAC non sospende né proroga il termine per la proposizione del ricorso.

**Pass se** — compare una fra le formulazioni seguenti:
- compare, riferita al termine per ricorrere, una fra: «non sospende»
- «non proroga»
- «non interrompe»
- «continua a decorrere»

**Fail se** — il deliverable afferma che l'istanza all'ANAC sospende, proroga o interrompe il termine, oppure il punto non è trattato.

**Indifferente** — il giudizio sull'opportunità di presentare comunque l'istanza all'ANAC.

<small>—— non passa al judge —— Fonte: art. 220, comma 1, d.lgs. 36/2023; documento 10 · Gravità: alta</small>

### B.20  [issue: I-11]  [tipo: assenza]  [judge]

**Verifica** — il deliverable non suggerisce di attendere il parere dell'ANAC prima di notificare il ricorso.

**Pass se** — non compare l'indicazione di attendere il parere prima di ricorrere

**Fail se** — è suggerito di presentare l'istanza all'ANAC e attendere il parere prima di notificare il ricorso.

<small>—— non passa al judge —— Fonte: art. 220, comma 1, d.lgs. 36/2023 · Gravità: alta</small>

### B.21  [issue: I-12]  [tipo: presenza]  [judge]

**Verifica** — il deliverable afferma che, se il contratto viene stipulato, il giudice che annulla l'aggiudicazione stabilisce se dichiarare inefficace il contratto.

**Pass se** — compare una fra le formulazioni seguenti:
- compare l'affermazione che la stipulazione non preclude la tutela
- compare l'affermazione che il giudice può dichiarare inefficace il contratto
- compare l'affermazione che l'inefficacia del contratto è rimessa alla valutazione del giudice

**Fail se** — il deliverable afferma che la stipulazione rende inutile o inammissibile il ricorso, oppure il punto non è trattato.

<small>—— non passa al judge —— Fonte: art. 122 c.p.a. · Gravità: media</small>

### B.22  [issue: I-12]  [tipo: presenza]  [judge]

**Verifica** — il deliverable indica fra gli adempimenti la proposizione della domanda di subentro nel contratto.

**Pass se** — compare una fra le formulazioni seguenti:
- compare, fra le domande da proporre, una fra: «domanda di subentro»
- «subentro nel contratto»
- «domanda di subentrare»

**Fail se** — la domanda di subentro non compare fra gli adempimenti.

<small>—— non passa al judge —— Fonte: art. 122 c.p.a. · Gravità: media</small>

### B.23  [issue: I-13]  [tipo: qualificazione]  [judge]

**Verifica** — il deliverable colloca la censura sulla nomina della commissione giudicatrice fra quelle da far valere entro il primo termine, quello decorrente dalla comunicazione di aggiudicazione.

**Pass se** — compare una fra le formulazioni seguenti:
- la censura sulla nomina della commissione è associata al termine del 24 novembre 2027
- la censura sulla nomina della commissione è associata al primo termine
- la censura sulla nomina della commissione è associata al termine decorrente dalla comunicazione di aggiudicazione

**Fail se** — quella censura è associata al secondo termine, oppure la sua collocazione temporale non è indicata.

**Indifferente** — il giudizio sulla fondatezza della censura.

<small>—— non passa al judge —— Fonte: documenti 02 e 03; art. 93, comma 1, d.lgs. 36/2023 · Gravità: alta</small>

### B.24  [issue: I-14]  [tipo: qualificazione]  [judge]

**Verifica** — il deliverable colloca la censura sull'attribuzione del punteggio sul criterio B.2 fra quelle che ricadono nel secondo termine, quello decorrente dalla messa a disposizione della relazione tecnica.

**Pass se** — compare una fra le formulazioni seguenti:
- la censura sul punteggio del criterio B.2 è associata al termine del 16 dicembre 2027
- la censura sul punteggio del criterio B.2 è associata al secondo termine
- la censura sul punteggio del criterio B.2 è associata al termine decorrente dalla messa a disposizione della relazione tecnica

**Fail se** — quella censura è associata al primo termine, oppure la sua collocazione temporale non è indicata.

**Indifferente** — il giudizio sulla fondatezza della censura.

<small>—— non passa al judge —— Fonte: documenti 03 e 08 · Gravità: alta</small>

### B.25  [issue: I-14]  [tipo: attribuzione]  [judge]

**Verifica** — il deliverable riconduce la censura sul punteggio del criterio B.2 al confronto fra la motivazione del verbale n. 4 e il contenuto della relazione tecnica dell'aggiudicataria.

**Pass se** — la censura è agganciata a entrambi i documenti: il verbale n. 4 e la relazione tecnica dell'aggiudicataria

**Fail se** — la censura è agganciata a uno solo dei due documenti, oppure a nessuno.

<small>—— non passa al judge —— Fonte: documento 03, criterio B.2; documento 08, paragrafo 3 · Gravità: media</small>

### B.26  [issue: I-15]  [tipo: presenza]  [judge]

**Verifica** — il deliverable afferma che le parti oscurate della relazione tecnica non consentono di stabilire se esistano ulteriori elementi rilevanti.

**Pass se** — compare una fra le formulazioni seguenti:
- compare, riferita alle parti oscurate, una fra: «non è possibile stabilire»
- «non è possibile verificare»
- «resta da verificare»
- «non si può escludere»

**Fail se** — il deliverable afferma che le parti oscurate sono irrilevanti, oppure non tratta il punto.

<small>—— non passa al judge —— Fonte: documenti 07 e 08 · Gravità: media</small>

### B.27  [issue: I-15]  [tipo: presenza]  [judge]

**Verifica** — il deliverable afferma che l'ostensione delle parti oscurate non è consentita prima del decorso del termine per impugnare le decisioni sull'oscuramento.

**Pass se** — compare una fra le formulazioni seguenti:
- compare l'affermazione che l'ostensione delle parti oscurate è differita al decorso di quel termine
- compare l'affermazione che le parti oscurate non sono ostensibili prima della scadenza di quel termine

**Fail se** — il punto non è trattato, oppure è affermato che le parti oscurate sono ottenibili con una nuova istanza di accesso.

<small>—— non passa al judge —— Fonte: art. 36, comma 5, d.lgs. 36/2023 · Gravità: media</small>

### B.28  [issue: I-02]  [tipo: assenza]  [judge]

**Verifica** — simmetria del controllo: il deliverable non afferma che il termine per la notificazione del ricorso principale è già scaduto alla data di riferimento.

**Pass se** — non compare l'affermazione che quel termine sia scaduto

**Fail se** — il termine per il ricorso principale è presentato come già scaduto.

<small>—— non passa al judge —— Fonte: art. 120, comma 2, c.p.a. · Gravità: alta</small>

### B.29  [issue: I-09]  [tipo: assenza]  [judge]

**Verifica** — sovra-segnalazione: il deliverable non indica fra gli adempimenti la notificazione del ricorso presso la sede reale della stazione appaltante o presso l'Avvocatura dello Stato.

**Pass se** — la notificazione presso la sede reale e la notificazione presso l'Avvocatura dello Stato non compaiono fra gli adempimenti

**Fail se** — è indicata come adempimento la notificazione presso la sede reale o presso l'Avvocatura dello Stato.

<small>—— non passa al judge —— Fonte: art. 120, comma 4, c.p.a.; documento 04, punto 16 · Gravità: alta</small>

### B.30  [issue: I-08]  [tipo: assenza]  [judge]

**Verifica** — sovra-segnalazione: il deliverable non afferma che il termine dilatorio non si applica perché l'appalto è basato su un accordo quadro.

**Pass se** — compare una fra le formulazioni seguenti:
- non compare l'affermazione che l'appalto in esame sia basato su un accordo quadro
- non compare l'affermazione che il termine dilatorio non si applichi

**Fail se** — il termine dilatorio è dichiarato inapplicabile, in tutto o in parte, per effetto dell'accordo quadro richiamato nella nota interna.

<small>—— non passa al judge —— Fonte: art. 18, comma 3, lettera b), d.lgs. 36/2023; documento 10 · Gravità: media</small>

### B.31  [issue: I-01]  [tipo: assenza]  [judge]

**Verifica** — sovra-segnalazione: il deliverable non indica la presa visione in piattaforma come momento da cui decorre il termine per impugnare.

**Pass se** — la presa visione non compare come decorrenza di alcun termine

**Fail se** — la presa visione del 26 ottobre 2027 è indicata come decorrenza.

<small>—— non passa al judge —— Fonte: documento 06 · Gravità: alta</small>

### B.32  [issue: I-15]  [tipo: assenza]  [judge]

**Verifica** — sovra-segnalazione: il deliverable non afferma che il prospetto dei punteggi analitici non è stato reso disponibile.

**Pass se** — non compare l'affermazione che il prospetto dei punteggi analitici manchi o non sia stato ostenso

**Fail se** — è segnalata la mancata messa a disposizione del prospetto dei punteggi analitici.

<small>—— non passa al judge —— Fonte: documenti 05 e 06 · Gravità: media</small>

### B.33  [issue: I-02]  [tipo: assenza]  [judge]

**Verifica** — sovra-segnalazione: il deliverable non indica fra gli adempimenti del cliente alcuna attività relativa allo svincolo della garanzia provvisoria.

**Pass se** — lo svincolo della garanzia provvisoria non compare fra gli adempimenti

**Fail se** — è indicato come adempimento lo svincolo o la richiesta di svincolo della garanzia provvisoria.

<small>—— non passa al judge —— Fonte: documento 05 · Gravità: media</small>

### B.34  [issue: I-15]  [tipo: assenza]  [judge]

**Verifica** — divieto di presunzione dell'esito: il deliverable non afferma che il ricorso sarà accolto né che sarà respinto.

**Pass se** — non compare un pronostico sull'esito del ricorso

**Fail se** — il deliverable pronostica l'esito del ricorso.

**Indifferente** — l'indicazione dei punti che restano da verificare e dei profili di incertezza.

<small>—— non passa al judge —— Fonte: 01_task.md, ultima riga dell'incarico · Gravità: alta</small>

---

## C. Date e valori calcolati

### C.1  [issue: I-01]  [tipo: valore]  [verifica meccanica]

**Verifica** — il deliverable indica il 25 ottobre 2027 come data da cui decorre il primo termine per impugnare.

**Pass se** — compare «25 ottobre 2027» oppure «25/10/2027» come decorrenza del primo termine

**Fail se** — è indicata una data diversa.

<small>—— non passa al judge —— Fonte: documenti 05 e 06 · Gravità: alta</small>

### C.2  [issue: I-02]  [tipo: presenza]  [judge]

**Verifica** — il deliverable afferma che il giorno da cui il termine decorre non si computa.

**Pass se** — compare una fra le formulazioni seguenti:
- compare una fra: «il giorno iniziale non si computa»
- «a decorrere dal giorno successivo»
- «escluso il giorno di ricezione»
- «dal 26 ottobre 2027»

**Fail se** — il passaggio non compare, oppure il termine è contato includendo il giorno iniziale.

<small>—— non passa al judge —— Fonte: computo dei termini a giorni · Gravità: media</small>

### C.3  [issue: I-02]  [tipo: valore]  [verifica meccanica]

**Verifica** — il deliverable indica il 24 novembre 2027 come termine per la notificazione del ricorso principale.

**Pass se** — compare «24 novembre 2027» oppure «24/11/2027» come termine per la notificazione del ricorso principale

**Fail se** — è indicata una data diversa.

<small>—— non passa al judge —— Fonte: art. 120, comma 2, c.p.a. · Gravità: alta</small>

### C.4  [issue: I-03]  [tipo: valore]  [verifica meccanica]

**Verifica** — il deliverable indica il 16 novembre 2027 come data da cui decorre il secondo termine.

**Pass se** — compare «16 novembre 2027» oppure «16/11/2027» come decorrenza del secondo termine

**Fail se** — è indicata una data diversa.

<small>—— non passa al judge —— Fonte: documenti 06 e 07 · Gravità: alta</small>

### C.5  [issue: I-03]  [tipo: valore]  [verifica meccanica]

**Verifica** — il deliverable indica il 16 dicembre 2027 come termine per far valere le censure che dipendono dalla relazione tecnica dell'aggiudicataria.

**Pass se** — compare «16 dicembre 2027» oppure «16/12/2027» come termine

**Fail se** — è indicata una data diversa, oppure il secondo termine non è datato.

<small>—— non passa al judge —— Fonte: art. 120, comma 2, c.p.a. · Gravità: alta</small>

### C.6  [issue: I-07]  [tipo: valore]  [verifica meccanica]

**Verifica** — il deliverable indica il 4 novembre 2027 come data di scadenza del termine per impugnare le decisioni sulle richieste di oscuramento.

**Pass se** — compare «4 novembre 2027» oppure «04/11/2027» come scadenza di quel termine

**Fail se** — è indicata una data diversa, oppure la scadenza non è datata.

<small>—— non passa al judge —— Fonte: art. 36, comma 4, d.lgs. 36/2023 · Gravità: alta</small>

### C.7  [issue: I-08]  [tipo: valore]  [verifica meccanica]

**Verifica** — il deliverable indica il 26 novembre 2027 come data di scadenza del termine dilatorio per la stipulazione del contratto.

**Pass se** — compare «26 novembre 2027» oppure «26/11/2027» come scadenza del termine dilatorio

**Fail se** — è indicata una data diversa.

<small>—— non passa al judge —— Fonte: art. 18, comma 3, d.lgs. 36/2023; documento 05 · Gravità: alta</small>

### C.8  [issue: I-01]  [tipo: assenza]  [judge]

**Verifica** — il deliverable non indica il 19 novembre 2027 come termine per la notificazione del ricorso.

**Pass se** — non compare «19 novembre 2027» né «19/11/2027» come termine per la notificazione del ricorso

**Fail se** — è indicato come termine il risultato di trenta giorni decorrenti dalla pubblicazione dell'avviso di appalto aggiudicato o dall'adozione della determina di aggiudicazione.

<small>—— non passa al judge —— Fonte: derivazione errata ricostruita in fase di build · Gravità: alta</small>

### C.9  [issue: I-01]  [tipo: assenza]  [judge]

**Verifica** — il deliverable non indica il 25 novembre 2027 come termine per la notificazione del ricorso.

**Pass se** — non compare «25 novembre 2027» né «25/11/2027» come termine per la notificazione del ricorso

**Fail se** — è indicato come termine il risultato di trenta giorni decorrenti dalla presa visione in piattaforma.

<small>—— non passa al judge —— Fonte: derivazione errata ricostruita in fase di build · Gravità: alta</small>

### C.10  [issue: I-08]  [tipo: assenza]  [judge]

**Verifica** — il deliverable non indica il 29 novembre 2027 come data di scadenza del termine dilatorio.

**Pass se** — non compare «29 novembre 2027» né «29/11/2027» come scadenza del termine dilatorio

**Fail se** — è indicata come scadenza del termine dilatorio il risultato di trentacinque giorni.

<small>—— non passa al judge —— Fonte: derivazione errata affermata nel documento 10 · Gravità: alta</small>
