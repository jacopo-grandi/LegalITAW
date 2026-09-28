# WF2-039 — Criteri atomizzati

> È ciò che viene somministrato al judge e alla verifica meccanica. Forma a campi, convenzione atomo v1.
>
> `required` = gravità alta; media e bassa = `optional`. Il campo `issue` porta l'identificativo della rubrica in prosa (`evaluation_criteria.md`). Ciò che segue la riga di separazione non passa al judge.
>
> **Inquadramento.** Il deliverable è la matrice dei red flag ambientali resa nell'interesse di Ferrera Superfici S.p.A., acquirente del ramo d'azienda e del compendio immobiliare, alla data di riferimento di martedì 5 aprile 2033. Il closing è previsto per il 30 giugno 2033 e non si è verificato. Sul sito è aperto dal dicembre 2031 un procedimento amministrativo in materia di bonifica.

---


## A. FORMA DELL'OUTPUT

**A.1 sezioni obbligatorie**
`issue: - · tipo: valore · gravità: alta · judge: no · fonte: response_template.md`
Verifica: Il deliverable è un solo file markdown denominato red_flag_matrix.md, non superiore a 2.800 parole, e contiene una sintesi, la matrice dei red flag, una sezione sulla qualificazione del sito e sulla posizione del compratore, una tabella delle azioni pre-closing, una sezione su date quantità e importi con il calcolo, una sezione su ciò che non è un red flag, una sezione su ciò che manca dal fascicolo e la risposta al consiglio.
Pass se: tutte e otto le parti sono presenti e distinte e il conteggio delle parole non supera 2.800.
Fail se: manca una delle otto parti, oppure due di esse non sono distinte, oppure il conteggio delle parole supera 2.800.

**A.2 matrice in forma di tabella**
`issue: - · tipo: struttura · gravità: alta · judge: no · fonte: response_template.md`
Verifica: La matrice dei red flag è resa in forma di tabella e ciascuna riga indica il rilievo, il documento o la fonte, lo stato del fatto, la conseguenza per il compratore, il soggetto su cui grava e la gravità.
Pass se: la tabella è presente e ogni riga porta i sei dati.
Fail se: la matrice non è in forma di tabella, oppure almeno una riga è priva di uno dei sei dati.

**A.3 qualificazione dello stato del fatto**
`issue: - · tipo: presenza · gravità: alta · judge: no · fonte: response_template.md`
Verifica: Ogni riga della matrice qualifica lo stato del fatto come accertato dal fascicolo, dichiarato da una parte oppure non ancora determinato.
Pass se: ogni riga porta una delle tre qualificazioni.
Fail se: almeno una riga è priva della qualificazione, oppure si usa una scala che non distingue il fatto accertato da quello dichiarato.

**A.4 azioni pre-closing in forma di tabella**
`issue: - · tipo: struttura · gravità: alta · judge: no · fonte: response_template.md`
Verifica: Le azioni pre-closing sono rese in forma di tabella e ciascuna riga indica l'azione, il soggetto cui spetta, il termine e la conseguenza dell'omissione.
Pass se: la tabella è presente e ogni riga porta i quattro dati.
Fail se: le azioni non sono in forma di tabella, oppure almeno una riga è priva di uno dei quattro dati.

**A.5 nessuna bozza di atto**
`issue: - · tipo: assenza · gravità: alta · judge: no · fonte: prompt`
Verifica: Il deliverable non contiene testo redatto in forma di clausola contrattuale, di lettera o di atto amministrativo.
Pass se: non compare testo in forma di clausola, di lettera o di provvedimento.
Fail se: il deliverable contiene una clausola, una bozza di lettera o una bozza di atto.

**A.6 fonti nell'elenco chiuso**
`issue: - · tipo: assenza · gravità: alta · judge: no · fonte: public/02_reference_pack.md`
Verifica: Il deliverable non contiene riferimenti normativi estranei all'elenco chiuso delle fonti del reference pack.
Pass se: ogni riferimento normativo citato appartiene all'elenco.
Fail se: compare almeno un riferimento normativo fuori elenco.


## B. MERITO

**B.1 qualificazione del sito**
`issue: I-01 · tipo: qualificazione · gravità: alta · judge: sì · fonte: art. 240; relazione Fase II, § 7`
Verifica: Il deliverable qualifica il sito, alla data di riferimento, come sito potenzialmente contaminato e non come sito contaminato.
Pass se: compare, riferita al sito o all'area B, l'espressione «sito potenzialmente contaminato» oppure «potenzialmente contaminato».
Fail se: il sito è qualificato come sito contaminato, oppure la qualificazione non compare.

**B.2 da che cosa dipende la qualificazione**
`issue: I-01 · tipo: presenza · gravità: alta · judge: sì · fonte: art. 240`
Verifica: Il deliverable afferma che la qualificazione come sito contaminato dipende dal superamento delle concentrazioni soglia di rischio determinate dall'analisi di rischio.
Pass se: compare l'affermazione che occorre il superamento delle concentrazioni soglia di rischio, o delle CSR, perché il sito sia contaminato.
Fail se: l'affermazione non compare, oppure il superamento delle concentrazioni soglia di contaminazione è presentato come bastante alla qualificazione.

**B.3 divieto di dare per accertata la contaminazione**
`issue: I-01 · tipo: assenza · gravità: alta · judge: sì · fonte: art. 240`
Verifica: Il deliverable non afferma che il sito sia un sito contaminato ai sensi della definizione di legge.
Pass se: non compare l'affermazione che il sito è contaminato, che la contaminazione è accertata o che il sito va bonificato in quanto contaminato.
Fail se: compare l'affermazione che il sito è un sito contaminato.

**B.4 esito dell'analisi di rischio dell'area A**
`issue: I-02 · tipo: presenza · gravità: alta · judge: sì · fonte: verbale della conferenza di servizi, punti 4 e 5`
Verifica: Il deliverable afferma che per l'area A l'analisi di rischio approvata ha concluso per il non superamento delle concentrazioni soglia di rischio e che il procedimento è chiuso per quell'area.
Pass se: compare l'affermazione che per l'area A le CSR non sono superate e che il procedimento è concluso, chiuso o positivamente definito per quell'area.
Fail se: l'affermazione non compare, oppure l'area A è presentata come ancora in procedimento.

**B.5 valore della concentrazione soglia di rischio dell'area A**
`issue: I-02 · tipo: valore · gravità: media · judge: no · fonte: verbale della conferenza di servizi, punto 4`
Verifica: Il deliverable indica 4.400 milligrammi per chilogrammo come concentrazione soglia di rischio determinata per il cromo totale nel suolo dell'area A.
Pass se: compare il valore 4.400.
Fail se: compare un valore diverso, oppure il valore non compare.

**B.6 l'area A non va bonificata**
`issue: N-01 · tipo: assenza · gravità: alta · judge: sì · fonte: verbale della conferenza di servizi, punto 5`
Verifica: Il deliverable non indica l'area A fra le aree che richiedono interventi di bonifica.
Pass se: l'area A non compare fra le aree da bonificare.
Fail se: l'area A è indicata come area da bonificare o come area contaminata.

**B.7 responsabile non individuato**
`issue: I-03 · tipo: presenza · gravità: alta · judge: sì · fonte: verbale della conferenza di servizi, punto 6`
Verifica: Il deliverable afferma che alla data di riferimento non è stato adottato alcun atto di individuazione del responsabile della contaminazione.
Pass se: compare l'affermazione che il responsabile non è stato individuato, che il procedimento di individuazione è in corso o che non esiste un atto di individuazione.
Fail se: l'affermazione non compare.

**B.8 a chi spetta l'accertamento**
`issue: I-03 · tipo: attribuzione · gravità: alta · judge: sì · fonte: art. 244, comma 2`
Verifica: Il deliverable riconduce alla provincia l'accertamento del responsabile della contaminazione.
Pass se: compare l'indicazione che l'individuazione del responsabile spetta alla provincia o all'autorità amministrativa competente.
Fail se: l'accertamento è attribuito ad altro soggetto, oppure non è attribuito.

**B.9 divieto di attribuire la responsabilità al venditore**
`issue: I-03 · tipo: assenza · gravità: alta · judge: sì · fonte: comunicazione del 9 dicembre 2031, punto 5; verbale, punto 6`
Verifica: Il deliverable non afferma che il venditore sia il responsabile della contaminazione.
Pass se: non compare l'affermazione che il venditore è il responsabile, né che lo è in quanto ha esercitato l'attività industriale sul sito.
Fail se: compare l'affermazione che il venditore è il responsabile della contaminazione.
Indifferente: l'indicazione del venditore come soggetto verso cui il compratore può rivalersi in via contrattuale.

**B.10 assenza di obbligo di bonifica per il compratore**
`issue: I-04 · tipo: presenza · gravità: alta · judge: sì · fonte: art. 245`
Verifica: Il deliverable afferma che il compratore, divenuto proprietario non responsabile, non è obbligato a eseguire la bonifica.
Pass se: compare l'affermazione che l'esecuzione della bonifica non è un obbligo del proprietario non responsabile, oppure che per lui è una facoltà.
Fail se: l'affermazione non compare, oppure si afferma che il compratore erediterà l'obbligo di bonificare.

**B.11 obblighi che gravano comunque sul proprietario**
`issue: I-04 · tipo: presenza · gravità: alta · judge: sì · fonte: art. 245, comma 2`
Verifica: Il deliverable afferma che sul proprietario o gestore gravano l'obbligo di comunicare il superamento delle concentrazioni soglia di contaminazione e quello di attuare le misure di prevenzione.
Pass se: compaiono entrambi gli obblighi, quello di comunicazione e quello di prevenzione.
Fail se: manca uno dei due obblighi, oppure nessuno dei due compare.

**B.12 divieto di trasferire l'obbligo di bonifica**
`issue: I-04 · tipo: assenza · gravità: alta · judge: sì · fonte: art. 245`
Verifica: Il deliverable non afferma che l'acquisto del sito comporti per il compratore l'obbligo di eseguire la bonifica.
Pass se: non compare l'affermazione che il compratore subentra nell'obbligo di bonifica o che lo eredita con la proprietà.
Fail se: compare l'affermazione che il compratore è o sarà obbligato a bonificare.

**B.13 presupposto dell'onere reale**
`issue: I-05 · tipo: presenza · gravità: alta · judge: sì · fonte: art. 253, comma 1`
Verifica: Il deliverable afferma che l'onere reale e il privilegio speciale presuppongono che gli interventi siano stati eseguiti d'ufficio dall'amministrazione.
Pass se: compare l'affermazione che l'onere reale sorge se e quando l'amministrazione esegue gli interventi in via sostitutiva o d'ufficio.
Fail se: l'affermazione non compare, oppure l'onere reale è presentato come già gravante sul sito alla data di riferimento.

**B.14 limite del recupero verso il proprietario non responsabile**
`issue: I-05 · tipo: presenza · gravità: alta · judge: sì · fonte: art. 253, comma 4`
Verifica: Il deliverable afferma che il recupero delle spese nei confronti del proprietario non responsabile è contenuto nel limite del valore di mercato dell'area determinato dopo l'esecuzione degli interventi.
Pass se: compare il riferimento al limite del valore di mercato dell'area dopo gli interventi.
Fail se: l'affermazione non compare, oppure si afferma che il proprietario risponde per l'intero costo.

**B.15 provvedimento motivato richiesto**
`issue: I-05 · tipo: presenza · gravità: media · judge: sì · fonte: art. 253, comma 3`
Verifica: Il deliverable afferma che il recupero verso il proprietario non responsabile richiede un provvedimento motivato dell'autorità sull'impossibilità di individuare il responsabile o di agire in rivalsa.
Pass se: compare il riferimento al provvedimento motivato o alla motivazione sull'impossibilità di escutere il responsabile.
Fail se: l'affermazione non compare.

**B.16 termine scaduto per l'analisi di rischio**
`issue: I-06 · tipo: valore · gravità: alta · judge: no · fonte: 6 mesi dal 10 febbraio 2032; art. 242, comma 4`
Verifica: Il deliverable indica il 10 agosto 2032 come data di scadenza del termine per presentare l'analisi di rischio.
Pass se: compare la data del 10 agosto 2032.
Fail se: compare una data diversa, oppure la data non compare.

**B.17 decorrenza del termine**
`issue: I-06 · tipo: attribuzione · gravità: alta · judge: sì · fonte: art. 242, comma 4`
Verifica: Il deliverable riconduce la decorrenza del termine per l'analisi di rischio all'approvazione del piano di caratterizzazione.
Pass se: compare l'indicazione che il termine decorre dall'approvazione del piano di caratterizzazione.
Fail se: il termine è fatto decorrere dalla comunicazione, dalla scoperta della contaminazione o da altra data, oppure la decorrenza non è indicata.

**B.18 serbatoio non documentato**
`issue: I-07 · tipo: presenza · gravità: alta · judge: sì · fonte: AIA, Allegato A, punto A.7; attestazione, punto 2`
Verifica: Il deliverable afferma che uno dei quattro serbatoi interrati censiti non risulta né rimosso né documentato come messo in sicurezza.
Pass se: compare l'affermazione che il serbatoio S4, o il quarto serbatoio, non è coperto dall'attestazione di rimozione o non è documentato.
Fail se: l'affermazione non compare, oppure si afferma che tutti i serbatoi sono stati rimossi.

**B.19 confronto fra i due documenti**
`issue: I-07 · tipo: attribuzione · gravità: media · judge: sì · fonte: AIA, punto A.7; attestazione, punti 2 e 6`
Verifica: Il deliverable riconduce la lacuna al confronto fra la planimetria che censisce quattro serbatoi e l'attestazione che ne copre tre.
Pass se: compare l'indicazione che i serbatoi censiti sono quattro e quelli attestati come rimossi sono tre.
Fail se: il confronto non compare.

**B.20 volume complessivo in deposito**
`issue: I-08 · tipo: valore · gravità: alta · judge: no · fonte: prospetto delle giacenze`
Verifica: Il deliverable indica 34,2 metri cubi come volume complessivo dei rifiuti in deposito al 31 marzo 2033.
Pass se: compare il valore 34,2.
Fail se: compare un valore diverso, oppure il valore non compare.

**B.21 volume dei rifiuti pericolosi**
`issue: I-08 · tipo: valore · gravità: alta · judge: no · fonte: prospetto delle giacenze`
Verifica: Il deliverable indica 11,6 metri cubi come volume dei rifiuti pericolosi in deposito al 31 marzo 2033.
Pass se: compare il valore 11,6.
Fail se: compare un valore diverso, oppure il valore non compare.

**B.22 entrambi i limiti superati**
`issue: I-08 · tipo: presenza · gravità: alta · judge: sì · fonte: art. 185-bis, comma 1`
Verifica: Il deliverable afferma che sono superati sia il limite complessivo di 30 metri cubi sia quello di 10 metri cubi per i rifiuti pericolosi.
Pass se: compaiono entrambi i superamenti, quello del limite complessivo e quello del limite dei rifiuti pericolosi.
Fail se: è indicato un solo superamento, oppure nessuno dei due.

**B.23 conseguenza del superamento**
`issue: I-08 · tipo: qualificazione · gravità: alta · judge: sì · fonte: art. 185-bis; art. 208`
Verifica: Il deliverable afferma che, superati i limiti, il deposito non è più deposito temporaneo prima della raccolta e richiede un titolo abilitativo.
Pass se: compare l'affermazione che viene meno la qualificazione di deposito temporaneo, oppure che il deposito diventa soggetto ad autorizzazione.
Fail se: l'affermazione non compare, oppure il superamento è presentato come mera irregolarità formale.

**B.24 conferimenti a trasportatore non iscritto**
`issue: I-09 · tipo: presenza · gravità: alta · judge: sì · fonte: certificato di iscrizione; registro`
Verifica: Il deliverable afferma che due conferimenti sono avvenuti dopo la scadenza dell'iscrizione all'Albo del trasportatore.
Pass se: compare l'affermazione che i conferimenti del 9 febbraio 2033 e del 16 marzo 2033 sono successivi alla scadenza dell'iscrizione.
Fail se: l'affermazione non compare, oppure è indicato un numero diverso di conferimenti successivi alla scadenza.

**B.25 data di scadenza dell'iscrizione**
`issue: I-09 · tipo: valore · gravità: alta · judge: no · fonte: certificato di iscrizione`
Verifica: Il deliverable indica il 14 gennaio 2033 come data fino alla quale l'iscrizione all'Albo del trasportatore è efficace.
Pass se: compare la data del 14 gennaio 2033.
Fail se: compare una data diversa, oppure la data non compare.

**B.26 effetto sulla responsabilità del produttore**
`issue: I-09 · tipo: presenza · gravità: alta · judge: sì · fonte: art. 188, comma 4`
Verifica: Il deliverable afferma che l'esclusione della responsabilità del produttore presuppone il conferimento a soggetti autorizzati e che per quei due conferimenti non opera.
Pass se: compare l'affermazione che la responsabilità del produttore non è esclusa per quei conferimenti.
Fail se: l'affermazione non compare, oppure si afferma che la responsabilità è comunque esclusa.

**B.27 relazione di riferimento non trasmessa**
`issue: I-10 · tipo: presenza · gravità: media · judge: sì · fonte: AIA, Allegato B, prescrizione 11`
Verifica: Il deliverable afferma che la relazione di riferimento prescritta dall'autorizzazione non risulta trasmessa.
Pass se: compare l'affermazione che la relazione di riferimento manca, non risulta trasmessa o non è nel fascicolo.
Fail se: l'affermazione non compare.

**B.28 termine della relazione di riferimento**
`issue: I-10 · tipo: valore · gravità: media · judge: no · fonte: 12 mesi dal 17 settembre 2029; AIA, prescrizione 11`
Verifica: Il deliverable indica il 17 settembre 2030 come termine entro cui la relazione di riferimento andava trasmessa.
Pass se: compare la data del 17 settembre 2030.
Fail se: compare una data diversa, oppure la data non compare.

**B.29 monitoraggio semestrale omesso**
`issue: I-11 · tipo: presenza · gravità: media · judge: sì · fonte: nota di ARPA, punto 3; AIA, prescrizione 7`
Verifica: Il deliverable afferma che il campionamento semestrale delle acque sotterranee dovuto dopo il 18 maggio 2032 non è stato eseguito.
Pass se: compare l'affermazione che il campionamento semestrale successivo è stato omesso o non è stato trasmesso.
Fail se: l'affermazione non compare.

**B.30 il procedimento di bonifica non sostituisce gli autocontrolli**
`issue: I-11 · tipo: presenza · gravità: media · judge: sì · fonte: nota di ARPA, punto 3`
Verifica: Il deliverable afferma che le attività del procedimento di bonifica non sostituiscono gli autocontrolli prescritti dall'autorizzazione.
Pass se: compare l'affermazione che i due obblighi restano distinti, o che il procedimento di bonifica non esonera dagli autocontrolli.
Fail se: l'affermazione non compare.

**B.31 meccanismo del subentro nell'autorizzazione**
`issue: I-12 · tipo: presenza · gravità: media · judge: sì · fonte: art. 29-nonies, comma 4`
Verifica: Il deliverable afferma che il subentro nell'autorizzazione integrata ambientale si perfeziona con la comunicazione del vecchio e del nuovo gestore all'autorità competente entro trenta giorni dal trasferimento.
Pass se: compare l'affermazione che occorre una comunicazione congiunta entro trenta giorni dal trasferimento.
Fail se: l'affermazione non compare.

**B.32 divieto di trattare la voltura come adempimento pre-closing**
`issue: I-12 · tipo: assenza · gravità: media · judge: sì · fonte: art. 29-nonies, comma 4`
Verifica: Il deliverable non afferma che il closing non possa perfezionarsi prima della voltura dell'autorizzazione o che occorra il rilascio di una nuova autorizzazione.
Pass se: non compare l'affermazione che la voltura è condizione del closing, né che serve una nuova autorizzazione.
Fail se: compare l'affermazione che il closing è subordinato alla voltura o che occorre una nuova autorizzazione.
Indifferente: l'indicazione della comunicazione di subentro fra le azioni da programmare.

**B.33 scopertura del massimale**
`issue: I-13 · tipo: valore · gravità: alta · judge: no · fonte: 2.900.000 - 1.500.000`
Verifica: Il deliverable indica 1.400.000 euro come differenza fra la stima degli interventi e il massimale dell'indennizzo.
Pass se: compare l'importo di 1.400.000 euro.
Fail se: compare un importo diverso, oppure l'importo non compare.

**B.34 il massimale non copre la stima**
`issue: I-13 · tipo: presenza · gravità: alta · judge: sì · fonte: contratto preliminare, art. 9.3, lett. c; relazione Fase II, § 8`
Verifica: Il deliverable afferma che il massimale dell'indennizzo è inferiore alla stima degli interventi riportata nella relazione di indagine.
Pass se: compare l'affermazione che il massimale non copre la stima, o che è inferiore a essa.
Fail se: l'affermazione non compare, oppure il massimale è presentato come capiente.

**B.35 scadenza dell'indennizzo**
`issue: I-14 · tipo: valore · gravità: alta · judge: no · fonte: 24 mesi dal closing del 30 giugno 2033; contratto preliminare, art. 9.4`
Verifica: Il deliverable indica il 30 giugno 2035 come termine entro cui l'indennizzo ambientale può essere fatto valere.
Pass se: compare la data del 30 giugno 2035.
Fail se: compare una data diversa, oppure la data non compare.

**B.36 disallineamento fra durata dell'indennizzo e procedimento**
`issue: I-14 · tipo: presenza · gravità: alta · judge: sì · fonte: contratto preliminare, art. 9.4; artt. 242 e 248`
Verifica: Il deliverable afferma che la durata dell'indennizzo è più breve del tempo necessario a concludere il procedimento di bonifica.
Pass se: compare l'affermazione che l'indennizzo scade prima della conclusione del procedimento o prima della certificazione dell'autorità.
Fail se: l'affermazione non compare.

**B.37 liberazione anche per fatti non ancora noti**
`issue: I-14 · tipo: presenza · gravità: media · judge: sì · fonte: contratto preliminare, art. 9.4`
Verifica: Il deliverable afferma che, decorso il termine, il venditore è liberato anche in relazione a fatti verificatisi prima della scadenza e non ancora noti al compratore.
Pass se: compare l'affermazione che la liberazione opera anche per i fatti non ancora noti.
Fail se: l'affermazione non compare.

**B.38 perimetro della Contaminazione Nota**
`issue: I-15 · tipo: presenza · gravità: alta · judge: sì · fonte: contratto preliminare, artt. 1.2 e 9.2`
Verifica: Il deliverable afferma che l'indennizzo copre soltanto la contaminazione descritta nella relazione di indagine allegata e non la contaminazione che dovesse emergere in seguito.
Pass se: compare l'affermazione che il perimetro dell'indennizzo è ancorato alla relazione allegata e che quanto emergerà oltre quel perimetro resta escluso.
Fail se: l'affermazione non compare, oppure l'indennizzo è presentato come esteso a ogni contaminazione preesistente.

**B.39 knowledge qualifier sulle garanzie ambientali**
`issue: I-16 · tipo: presenza · gravità: alta · judge: sì · fonte: contratto preliminare, art. 8.1, lett. b e c`
Verifica: Il deliverable afferma che le dichiarazioni e garanzie ambientali sono rese nei limiti della conoscenza del venditore.
Pass se: compare l'affermazione che le garanzie ambientali sono limitate a quanto a conoscenza del venditore, o che contengono un knowledge qualifier.
Fail se: l'affermazione non compare, oppure le garanzie sono presentate come incondizionate.

**B.40 dichiarazione di conformità smentita**
`issue: I-17 · tipo: presenza · gravità: media · judge: sì · fonte: contratto preliminare, art. 8.1, lett. b; AIA, prescrizioni 7 e 11`
Verifica: Il deliverable afferma che la garanzia di gestione conforme alle prescrizioni dell'autorizzazione è smentita da prescrizioni non adempiute.
Pass se: compare l'affermazione che la dichiarazione di conformità non regge a fronte delle prescrizioni non adempiute.
Fail se: l'affermazione non compare.

**B.41 analisi di rischio dell'area B mancante**
`issue: I-18 · tipo: presenza · gravità: alta · judge: sì · fonte: verbale della conferenza di servizi, punto 3`
Verifica: Il deliverable indica fra gli elementi mancanti l'analisi di rischio relativa all'area B.
Pass se: compare l'indicazione che l'analisi di rischio dell'area B manca o non è stata presentata.
Fail se: l'indicazione non compare.

**B.42 atto di individuazione del responsabile mancante**
`issue: I-18 · tipo: presenza · gravità: media · judge: sì · fonte: verbale della conferenza di servizi, punto 6`
Verifica: Il deliverable indica fra gli elementi mancanti l'atto della provincia sull'individuazione del responsabile della contaminazione.
Pass se: compare l'indicazione che quell'atto manca o non è stato adottato.
Fail se: l'indicazione non compare.

**B.43 documentazione del serbatoio mancante**
`issue: I-18 · tipo: presenza · gravità: media · judge: sì · fonte: attestazione, punto 6; relazione Fase II, § 9.4`
Verifica: Il deliverable indica fra gli elementi mancanti la documentazione di dismissione del quarto serbatoio interrato.
Pass se: compare l'indicazione che quella documentazione manca.
Fail se: l'indicazione non compare.

**B.44 divieto di prudenza paralizzante**
`issue: I-18 · tipo: assenza · gravità: alta · judge: sì · fonte: relazione Fase II; verbale della conferenza di servizi`
Verifica: Il deliverable non afferma che l'operazione non sia valutabile prima della conclusione del procedimento di bonifica.
Pass se: non compare l'affermazione che non è possibile valutare l'operazione, che occorre attendere la chiusura del procedimento o che nulla può essere concluso.
Fail se: compare l'affermazione che l'operazione non è valutabile.

**B.45 azione sull'analisi di rischio**
`issue: I-19 · tipo: presenza · gravità: alta · judge: sì · fonte: verbale della conferenza di servizi, punto 3`
Verifica: Il deliverable indica fra le azioni pre-closing l'acquisizione dell'analisi di rischio dell'area B, ovvero la sua presentazione come condizione del closing.
Pass se: compare l'azione di ottenere il documento di analisi di rischio dell'area B o di subordinarvi il closing.
Fail se: l'azione non compare.

**B.46 azione sul massimale**
`issue: I-19 · tipo: presenza · gravità: alta · judge: sì · fonte: contratto preliminare, art. 9.3`
Verifica: Il deliverable indica fra le azioni pre-closing la modifica del massimale dell'indennizzo, ovvero l'esclusione della contaminazione preesistente dal massimale.
Pass se: compare l'azione di innalzare il massimale, di escluderne la contaminazione preesistente o di prevedere un indennizzo specifico senza limite.
Fail se: l'azione non compare.

**B.47 azione sulla durata dell'indennizzo**
`issue: I-19 · tipo: presenza · gravità: alta · judge: sì · fonte: contratto preliminare, art. 9.4`
Verifica: Il deliverable indica fra le azioni pre-closing l'allineamento della durata dell'indennizzo alla conclusione del procedimento di bonifica.
Pass se: compare l'azione di estendere o di ancorare la durata dell'indennizzo alla certificazione dell'autorità o alla chiusura del procedimento.
Fail se: l'azione non compare.

**B.48 azione di garanzia patrimoniale**
`issue: I-19 · tipo: presenza · gravità: media · judge: sì · fonte: contratto preliminare, art. 9`
Verifica: Il deliverable indica fra le azioni pre-closing la costituzione di una garanzia o di un deposito vincolato a copertura dell'obbligo di indennizzo.
Pass se: compare l'azione di costituire un deposito vincolato, una garanzia bancaria o assicurativa o un trattenimento di prezzo.
Fail se: l'azione non compare.

**B.49 azione sui rifiuti**
`issue: I-19 · tipo: presenza · gravità: media · judge: sì · fonte: prospetto delle giacenze`
Verifica: Il deliverable indica fra le azioni pre-closing la regolarizzazione del deposito dei rifiuti.
Pass se: compare l'azione di avviare a recupero o smaltimento le giacenze eccedenti, o di riportare il deposito nei limiti.
Fail se: l'azione non compare.

**B.50 simmetria sulla clausola a favore**
`issue: N-05 · tipo: assenza · gravità: alta · judge: sì · fonte: contratto preliminare, art. 9.6`
Verifica: Il deliverable non presenta come rischio per il compratore l'obbligo del venditore di completare a proprie spese la messa in sicurezza d'emergenza fuori dal massimale.
Pass se: quella clausola non compare fra i red flag o fra i rischi.
Fail se: la clausola è presentata come rischio, come criticità o come clausola sfavorevole.

**B.51 il riesame pendente non è un rilievo**
`issue: N-06 · tipo: assenza · gravità: media · judge: sì · fonte: AIA, articolo 5`
Verifica: Il deliverable non presenta come rilievo la pendenza o l'approssimarsi del riesame dell'autorizzazione integrata ambientale.
Pass se: il riesame non compare fra i red flag.
Fail se: il riesame è indicato come red flag o come rischio.

**B.52 il sito di interesse nazionale non si applica**
`issue: N-02 · tipo: assenza · gravità: alta · judge: sì · fonte: relazione Fase II, § 2; determinazione n. 1187`
Verifica: Il deliverable non afferma che al sito si applichi il regime dei siti di interesse nazionale.
Pass se: non compare l'affermazione che il sito è ricompreso nel perimetro di un sito di interesse nazionale o che la competenza è ministeriale.
Fail se: compare l'affermazione che si applica il regime dei siti di interesse nazionale.

**B.53 l'amianto non va rimosso**
`issue: N-03 · tipo: assenza · gravità: alta · judge: sì · fonte: relazione amianto, punti 5 e 7; D.M. 6 settembre 1994`
Verifica: Il deliverable non indica la rimozione delle coperture in cemento-amianto come obbligo o come azione dovuta.
Pass se: non compare l'affermazione che le coperture devono essere rimosse.
Fail se: compare l'affermazione che la rimozione dell'amianto è obbligatoria o dovuta.
Indifferente: l'indicazione della rimozione come opzione economica futura, purché non presentata come obbligo.

**B.54 la diffida di ARPA è chiusa**
`issue: N-04 · tipo: assenza · gravità: media · judge: sì · fonte: nota di ARPA, punto 2`
Verifica: Il deliverable non indica fra i rilievi aperti la diffida di ARPA relativa al punto di emissione E7.
Pass se: quella diffida non compare fra i red flag aperti.
Fail se: la diffida è indicata come rilievo aperto o come procedimento pendente.

**B.55 il piezometro di monte non prova la contaminazione del sito**
`issue: N-07 · tipo: assenza · gravità: alta · judge: sì · fonte: relazione Fase II, § 7`
Verifica: Il deliverable non attribuisce all'attività dello stabilimento il superamento riscontrato nel piezometro a monte idrogeologico.
Pass se: non compare l'affermazione che il dato del piezometro di monte è riconducibile al sito o che costituisce prova della contaminazione.
Fail se: compare l'affermazione che il superamento nel piezometro di monte è attribuibile allo stabilimento.

**B.56 simmetria sulla prescrizione di monitoraggio dell'area A**
`issue: I-20 · tipo: assenza · gravità: media · judge: sì · fonte: verbale della conferenza di servizi, punto 5, lett. c`
Verifica: Il deliverable non presenta come red flag la prescrizione di monitoraggio disposta per l'area A dalla conferenza di servizi.
Pass se: quella prescrizione non compare fra i red flag.
Fail se: la prescrizione di monitoraggio dell'area A è indicata come red flag.
Indifferente: la sua indicazione fra gli adempimenti che il compratore erediterà.

**B.57 divieto di presumere l'esito dell'analisi di rischio**
`issue: I-21 · tipo: assenza · gravità: alta · judge: sì · fonte: verbale della conferenza di servizi, punto 3`
Verifica: Il deliverable non afferma che l'analisi di rischio dell'area B concluderà per il superamento delle concentrazioni soglia di rischio.
Pass se: non compare l'affermazione che le CSR dell'area B risulteranno superate.
Fail se: compare l'affermazione che l'analisi di rischio concluderà per il superamento.

**B.58 divieto di presumere l'entità dei costi**
`issue: I-21 · tipo: assenza · gravità: media · judge: sì · fonte: relazione Fase II, § 8`
Verifica: Il deliverable non presenta la stima di 2.900.000 euro come costo certo degli interventi.
Pass se: non compare l'affermazione che il costo degli interventi è pari a 2.900.000 euro.
Fail se: compare l'affermazione che gli interventi costeranno 2.900.000 euro.
Indifferente: l'uso della stima come termine di confronto con il massimale, purché indicata come stima.

**B.59 divieto di presumere l'individuazione del responsabile**
`issue: I-21 · tipo: assenza · gravità: media · judge: sì · fonte: verbale della conferenza di servizi, punto 6`
Verifica: Il deliverable non afferma che la provincia individuerà il responsabile nel venditore.
Pass se: non compare l'affermazione che la provincia individuerà il venditore come responsabile.
Fail se: compare quell'affermazione.


## C. INDICI, DATE E VALORI CALCOLATI

**C.1 concentrazione rappresentativa alla sorgente dell'area A**
`issue: I-02 · tipo: valore · gravità: bassa · judge: no · fonte: verbale della conferenza di servizi, punto 4`
Verifica: Il deliverable indica 940 milligrammi per chilogrammo come concentrazione rappresentativa alla sorgente determinata per l'area A.
Pass se: compare il valore 940.
Fail se: compare un valore diverso, oppure il valore non compare.

**C.2 giorni di ritardo dell'analisi di rischio**
`issue: I-06 · tipo: valore · gravità: bassa · judge: no · fonte: dal 10 agosto 2032 al 5 aprile 2033`
Verifica: Il deliverable indica il ritardo maturato alla data di riferimento sul termine per l'analisi di rischio dell'area B.
Pass se: compare il valore 238 riferito ai giorni di ritardo.
Fail se: compare un valore diverso, oppure il ritardo non è quantificato.

**C.3 derivazione errata del termine dell'analisi di rischio**
`issue: I-06 · tipo: assenza · gravità: media · judge: sì · fonte: art. 242, comma 4`
Verifica: Il deliverable non presenta il termine per l'analisi di rischio come decorrente dalla comunicazione del 9 dicembre 2031 o dalla data della relazione di indagine.
Pass se: non compare l'indicazione che il termine decorre dalla comunicazione o dalla relazione di indagine.
Fail se: il termine è fatto decorrere dalla comunicazione del 9 dicembre 2031 o dalla relazione dell'11 novembre 2032.

**C.4 quota del massimale sulla stima**
`issue: I-13 · tipo: valore · gravità: bassa · judge: no · fonte: 1.500.000 / 2.900.000`
Verifica: Il deliverable indica la quota della stima coperta dal massimale dell'indennizzo.
Pass se: compare il valore 51,72 per cento, oppure 51,72%.
Fail se: compare un valore diverso, oppure la quota non è indicata.

**C.5 derivazione errata dell'obbligo di bonifica**
`issue: I-04 · tipo: assenza · gravità: alta · judge: sì · fonte: artt. 244 e 245`
Verifica: Il deliverable non fonda un obbligo di bonifica del compratore sulla circostanza che l'attività industriale è stata esercitata sul sito o sulla circostanza che il compratore ne diverrà proprietario.
Pass se: non compare un ragionamento che ricavi l'obbligo di bonifica dalla titolarità dell'immobile o dalla storia industriale del sito.
Fail se: compare l'affermazione che il compratore risponde della bonifica in quanto proprietario o in quanto subentrante nell'attività.

---

**Conteggi.** 21 issue di merito, 7 controlled non-issue, 70 criteri atomici, di cui 53 al judge e 17 a verifica meccanica.
