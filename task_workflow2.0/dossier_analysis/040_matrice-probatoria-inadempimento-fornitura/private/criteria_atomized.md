# WF2-040 — Criteri atomizzati

> È ciò che viene somministrato al judge e alla verifica meccanica. Forma a campi, convenzione atomo v1.
>
> `required` = gravità alta; media e bassa = `optional`. Il campo `issue` porta l'identificativo della rubrica in prosa (`evaluation_criteria.md`). Ciò che segue la riga di separazione non passa al judge.
>
> **Inquadramento.** Il deliverable è la matrice probatoria resa nell'interesse di Valmadura Impianti S.p.A., fornitore destinatario di una diffida, alla data di riferimento di giovedì 22 giugno 2034. Nessun giudizio è pendente. La diffida è stata ricevuta il 12 giugno 2034, assegna trenta giorni e chiede 3.240.000 euro; nessuna risposta è stata inviata.

---


## A. FORMA DELL'OUTPUT

**A.1 sezioni obbligatorie**
`issue: - · tipo: valore · gravità: alta · judge: no · fonte: response_template.md`
Verifica: Il deliverable è un solo file markdown denominato evidence_matrix.md, non superiore a 2.800 parole, e contiene una sintesi, una sezione sulle tre cifre, la matrice probatoria, la scomposizione della richiesta voce per voce, una sezione su esposizione e punti di forza, una sezione su ciò che non va eccepito, una sezione su ciò che manca dal fascicolo, una tabella delle azioni e la risposta al consiglio.
Pass se: tutte e nove le parti sono presenti e distinte e il conteggio delle parole non supera 2.800.
Fail se: manca una delle nove parti, oppure due di esse non sono distinte, oppure il conteggio delle parole supera 2.800.

**A.2 matrice a cinque colonne**
`issue: - · tipo: struttura · gravità: alta · judge: no · fonte: response_template.md`
Verifica: La matrice probatoria è resa in forma di tabella e ciascuna riga porta il fatto affermato, la prova presente nel fascicolo, la contestazione opponibile, la lacuna residua e l'azione.
Pass se: la tabella è presente e ogni riga porta i cinque dati.
Fail se: la matrice non è in forma di tabella, oppure almeno una riga è priva di uno dei cinque dati.

**A.3 provenienza della prova**
`issue: - · tipo: presenza · gravità: alta · judge: no · fonte: response_template.md`
Verifica: Ogni riga della matrice qualifica la provenienza della prova come nostro documento, documento del cliente, documento di un terzo oppure nessuna.
Pass se: ogni riga porta una delle quattro qualificazioni.
Fail se: almeno una riga è priva della qualificazione, oppure si usa una scala che non distingue il documento di parte da quello del terzo.

**A.4 tabella delle azioni**
`issue: - · tipo: struttura · gravità: media · judge: no · fonte: response_template.md`
Verifica: Le azioni sono rese in forma di tabella e ciascuna riga indica l'azione, il soggetto cui spetta e il termine.
Pass se: la tabella è presente e ogni riga porta i tre dati.
Fail se: le azioni non sono in forma di tabella, oppure almeno una riga è priva di uno dei tre dati.

**A.5 nessuna bozza di atto**
`issue: - · tipo: assenza · gravità: alta · judge: no · fonte: prompt`
Verifica: Il deliverable non contiene la bozza di una lettera di risposta, di una memoria o di un atto.
Pass se: non compare testo redatto in forma di lettera o di atto difensivo.
Fail se: il deliverable contiene una bozza di lettera, di memoria o di atto.

**A.6 fonti nell'elenco chiuso**
`issue: - · tipo: assenza · gravità: alta · judge: no · fonte: public/02_reference_pack.md`
Verifica: Il deliverable non contiene riferimenti normativi estranei all'elenco chiuso delle fonti del reference pack.
Pass se: ogni riferimento normativo citato appartiene all'elenco.
Fail se: compare almeno un riferimento normativo fuori elenco.


## B. MERITO

**B.1 importo richiesto**
`issue: I-01 · tipo: valore · gravità: alta · judge: no · fonte: diffida, punto 6`
Verifica: Il deliverable indica 3.240.000 euro come importo complessivamente richiesto nella diffida.
Pass se: compare l'importo di 3.240.000 euro.
Fail se: compare un importo diverso, oppure l'importo non compare.

**B.2 importo documentato**
`issue: I-01 · tipo: valore · gravità: alta · judge: no · fonte: 640.000 + 212.400 + 180.000 + 287.600`
Verifica: Il deliverable indica 1.320.000 euro come importo della richiesta assistito da documenti presenti nel fascicolo.
Pass se: compare l'importo di 1.320.000 euro.
Fail se: compare un importo diverso, oppure l'importo non compare.

**B.3 esposizione prima del massimale**
`issue: I-01 · tipo: valore · gravità: alta · judge: no · fonte: 128.400 + 180.000 + 191.200`
Verifica: Il deliverable indica 499.600 euro come esposizione ricostruita voce per voce prima dell'applicazione del massimale.
Pass se: compare l'importo di 499.600 euro.
Fail se: compare un importo diverso, oppure l'importo non compare.

**B.4 esposizione dopo il massimale**
`issue: I-01 · tipo: valore · gravità: alta · judge: no · fonte: 15% di 2.480.000; contratto, art. 10.2`
Verifica: Il deliverable indica 372.000 euro come esposizione residua dopo l'applicazione del massimale contrattuale.
Pass se: compare l'importo di 372.000 euro.
Fail se: compare un importo diverso, oppure l'importo non compare.

**B.5 le tre cifre sono tenute distinte**
`issue: I-01 · tipo: presenza · gravità: alta · judge: sì · fonte: matrice probatoria`
Verifica: Il deliverable tiene distinti l'importo richiesto, l'importo documentato e l'esposizione stimata, e mostra il passaggio dall'uno all'altro.
Pass se: i tre importi compaiono distinti e il deliverable spiega che cosa cade fra l'uno e l'altro.
Fail se: i tre importi non sono distinti, oppure il deliverable si limita a contestare la richiesta senza ricostruire l'esposizione.

**B.6 divieto di equiparare richiesta ed esposizione**
`issue: I-01 · tipo: assenza · gravità: alta · judge: sì · fonte: diffida, punto 6`
Verifica: Il deliverable non presenta l'importo richiesto come misura dell'esposizione della società.
Pass se: non compare l'affermazione che l'esposizione è pari a 3.240.000 euro o che quello è il rischio.
Fail se: compare l'affermazione che la società rischia l'importo richiesto.

**B.7 voci prive di riscontro documentale**
`issue: I-02 · tipo: valore · gravità: alta · judge: no · fonte: 1.850.000 + 70.000`
Verifica: Il deliverable indica 1.920.000 euro come somma delle voci della richiesta prive di qualsiasi riscontro documentale.
Pass se: compare l'importo di 1.920.000 euro.
Fail se: compare un importo diverso, oppure l'importo non compare.

**B.8 quali voci non sono documentate**
`issue: I-02 · tipo: presenza · gravità: alta · judge: sì · fonte: diffida, punto 6, lettere d ed f; elenco degli allegati`
Verifica: Il deliverable afferma che la perdita di margine sugli ordini non evasi e il danno all'immagine non sono sostenute da alcun documento del fascicolo.
Pass se: compaiono entrambe le voci come prive di riscontro documentale.
Fail se: è indicata una sola delle due voci, oppure nessuna, oppure le voci sono trattate come documentate.

**B.9 esclusione contrattuale del lucro cessante**
`issue: I-03 · tipo: presenza · gravità: alta · judge: sì · fonte: contratto, art. 10.1`
Verifica: Il deliverable afferma che la perdita di margine sugli ordini e il danno all'immagine sono esclusi dalla clausola contrattuale sulla responsabilità.
Pass se: compare l'affermazione che quelle voci sono escluse dal contratto.
Fail se: l'affermazione non compare, oppure le voci sono contestate solo sul piano probatorio.

**B.10 doppia ragione di esclusione**
`issue: I-03 · tipo: presenza · gravità: media · judge: sì · fonte: contratto, art. 10.1; diffida, allegati`
Verifica: Il deliverable afferma che quelle due voci cadono per due ragioni distinte e autonome: l'esclusione contrattuale e l'assenza di prova.
Pass se: compare l'indicazione che le ragioni sono due e indipendenti.
Fail se: è indicata una sola ragione.

**B.11 data di scoperta dell'episodio di gennaio**
`issue: I-04 · tipo: valore · gravità: alta · judge: no · fonte: rapporto di intervento del 12 gennaio 2034; PEC del 6 febbraio 2034`
Verifica: Il deliverable indica l'11 gennaio 2034 come data di scoperta del difetto denunciato nel febbraio 2034.
Pass se: compare la data dell'11 gennaio 2034 riferita alla scoperta.
Fail se: compare una data diversa, oppure la data non compare.

**B.12 giorni intercorsi**
`issue: I-04 · tipo: valore · gravità: alta · judge: no · fonte: dall'11 gennaio 2034 al 6 febbraio 2034`
Verifica: Il deliverable indica in ventisei i giorni intercorsi fra la scoperta e la denuncia scritta dell'episodio di gennaio.
Pass se: compare il valore 26 riferito a quei giorni.
Fail se: compare un valore diverso, oppure il numero di giorni non è indicato.

**B.13 superamento del termine convenzionale**
`issue: I-04 · tipo: qualificazione · gravità: alta · judge: sì · fonte: contratto, art. 9.3`
Verifica: Il deliverable qualifica la denuncia dell'episodio di gennaio come tardiva rispetto al termine convenzionale di quindici giorni previsto a pena di decadenza.
Pass se: compare, riferita a quella denuncia, una fra: «tardiva», «fuori termine», «oltre il termine di decadenza», «decaduta».
Fail se: la denuncia non è qualificata, oppure è indicata come tempestiva.

**B.14 il termine legale è più ampio**
`issue: I-05 · tipo: presenza · gravità: alta · judge: sì · fonte: art. 1667, comma 2, c.c.`
Verifica: Il deliverable afferma che il termine di denuncia previsto dalla legge per la garanzia nell'appalto è di sessanta giorni, più ampio di quello convenzionale.
Pass se: compare il confronto fra il termine convenzionale e il termine legale di sessanta giorni.
Fail se: il confronto non compare.

**B.15 esposizione del termine convenzionale al rilievo di nullità**
`issue: I-05 · tipo: presenza · gravità: alta · judge: sì · fonte: art. 2965 c.c.`
Verifica: Il deliverable afferma che il termine convenzionale di decadenza è esposto al rilievo di nullità in quanto può rendere eccessivamente difficile l'esercizio del diritto.
Pass se: compare l'indicazione che la validità del termine convenzionale può essere contestata.
Fail se: l'indicazione non compare.

**B.16 divieto di dare per acquisita la decadenza**
`issue: I-05 · tipo: assenza · gravità: alta · judge: sì · fonte: contratto, art. 9.3; art. 2965 c.c.`
Verifica: Il deliverable non presenta la decadenza sull'episodio di gennaio come acquisita o definitiva.
Pass se: non compare l'affermazione che quelle voci sono definitivamente escluse, che la decadenza è certa o che la questione è chiusa.
Fail se: compare l'affermazione che la decadenza è acquisita, certa o definitiva.
Indifferente: l'indicazione dell'eccezione di decadenza come difesa da sollevare.

**B.17 importo che cade con l'episodio di gennaio**
`issue: I-06 · tipo: valore · gravità: alta · judge: no · fonte: 640.000 + 84.000`
Verifica: Il deliverable indica 724.000 euro come somma delle voci riferite all'episodio di gennaio.
Pass se: compare l'importo di 724.000 euro.
Fail se: compare un importo diverso, oppure l'importo non compare.

**B.18 scomposizione dello straordinario**
`issue: I-06 · tipo: valore · gravità: alta · judge: no · fonte: prospetto dei maggiori costi, sezione B, riga 7`
Verifica: Il deliverable indica 84.000 euro come quota dei maggiori costi di manodopera riferita all'episodio di gennaio.
Pass se: compare l'importo di 84.000 euro.
Fail se: compare un importo diverso, oppure l'importo non compare.

**B.19 quota dello straordinario riferita a novembre**
`issue: I-06 · tipo: valore · gravità: alta · judge: no · fonte: prospetto dei maggiori costi, sezione B, riga 6`
Verifica: Il deliverable indica 128.400 euro come quota dei maggiori costi di manodopera riferita all'episodio di novembre.
Pass se: compare l'importo di 128.400 euro.
Fail se: compare un importo diverso, oppure l'importo non compare.

**B.20 attribuzione dell'episodio di aprile al materiale**
`issue: I-07 · tipo: qualificazione · gravità: alta · judge: sì · fonte: rapporto del 19 aprile 2034; contratto, art. 9.4`
Verifica: Il deliverable qualifica il calo di rendimento dell'aprile 2034 come non imputabile alla linea, in quanto derivante dall'impiego di un film non conforme alla specifica contrattuale.
Pass se: compare l'affermazione che il difetto non è imputabile alla macchina o che deriva dal materiale fornito dal committente.
Fail se: l'episodio è attribuito alla macchina, oppure la questione dell'attribuzione non è affrontata.

**B.21 misura dello scostamento del film**
`issue: I-07 · tipo: valore · gravità: alta · judge: no · fonte: rapporto del 19 aprile 2034, punto 2`
Verifica: Il deliverable indica lo spessore misurato del film impiegato nell'aprile 2034.
Pass se: compaiono i valori 21,4 e 22,6 riferiti allo spessore misurato in micron.
Fail se: compaiono valori diversi, oppure lo spessore misurato non è indicato.

**B.22 specifica contrattuale del film**
`issue: I-07 · tipo: valore · gravità: alta · judge: no · fonte: contratto, Allegato 1, punto 3`
Verifica: Il deliverable indica lo spessore del film previsto dalla specifica contrattuale e la relativa tolleranza.
Pass se: compaiono il valore 28 e la tolleranza di 2 micron.
Fail se: compaiono valori diversi, oppure la specifica non è indicata.

**B.23 prova con film conforme**
`issue: I-07 · tipo: presenza · gravità: media · judge: sì · fonte: rapporto del 19 aprile 2034, punto 4`
Verifica: Il deliverable richiama la prova eseguita con film conforme alla specifica, che ha restituito un rendimento superiore a quello garantito.
Pass se: compare il riferimento alla prova con film conforme e al rendimento che ne è risultato.
Fail se: il riferimento non compare.

**B.24 l'episodio di novembre è indifendibile nell'an**
`issue: I-08 · tipo: presenza · gravità: alta · judge: sì · fonte: rapporto del 14 novembre 2033, punto 3`
Verifica: Il deliverable afferma che l'episodio del novembre 2033 è imputabile alla società, in quanto il rapporto del suo stesso tecnico lo qualifica come difetto di progetto.
Pass se: compare l'affermazione che su quell'episodio non vi sono difese sull'an, o che la responsabilità è documentata dal nostro rapporto.
Fail se: l'affermazione non compare, oppure l'episodio è presentato come contestabile nell'an.

**B.25 tempestività della denuncia di novembre**
`issue: I-08 · tipo: presenza · gravità: media · judge: sì · fonte: PEC del 16 novembre 2033; contratto, art. 9.3`
Verifica: Il deliverable afferma che la denuncia dell'episodio di novembre è stata tempestiva rispetto al termine convenzionale.
Pass se: compare l'affermazione che quella denuncia è in termine o tempestiva.
Fail se: l'affermazione non compare, oppure la denuncia è indicata come tardiva.

**B.26 penali del cliente finale documentate**
`issue: I-09 · tipo: presenza · gravità: alta · judge: sì · fonte: nota di addebito n. 118`
Verifica: Il deliverable afferma che le penali applicate dal cliente finale sono documentate da un documento proveniente da un terzo.
Pass se: compare l'affermazione che quella voce è sostenuta da un documento di un terzo.
Fail se: l'affermazione non compare, oppure la voce è trattata come non documentata.

**B.27 prevedibilità documentata dalle premesse**
`issue: I-09 · tipo: attribuzione · gravità: alta · judge: sì · fonte: contratto, premessa C`
Verifica: Il deliverable riconduce la prevedibilità delle penali del cliente finale alle premesse del contratto, che danno atto della destinazione della linea e dell'esistenza di penali.
Pass se: compare il riferimento alla premessa del contratto sulla destinazione della linea al contratto con il cliente finale.
Fail se: la prevedibilità è ricondotta ad altro, oppure non è affrontata.

**B.28 righe della fattura estranee al difetto**
`issue: I-10 · tipo: valore · gravità: alta · judge: no · fonte: fattura n. 214, righe 4 e 5`
Verifica: Il deliverable indica 96.400 euro come parte della fattura di ripristino riferita a interventi richiesti dal committente ed estranei ai difetti dedotti.
Pass se: compare l'importo di 96.400 euro.
Fail se: compare un importo diverso, oppure l'importo non compare.

**B.29 quali righe sono estranee**
`issue: I-10 · tipo: presenza · gravità: alta · judge: sì · fonte: fattura n. 214, righe 4 e 5`
Verifica: Il deliverable afferma che le righe della fattura relative al sistema di regolazione automatica della tensione del film e alla modifica del nastro per il nuovo formato sono estranee ai difetti dedotti.
Pass se: compaiono entrambe le voci come estranee.
Fail se: è indicata una sola delle due voci, oppure nessuna.

**B.30 parte della fattura riferibile al fermo**
`issue: I-10 · tipo: valore · gravità: media · judge: no · fonte: fattura n. 214, righe 1, 2 e 3`
Verifica: Il deliverable indica 191.200 euro come parte della fattura di ripristino riferibile al fermo della linea.
Pass se: compare l'importo di 191.200 euro.
Fail se: compare un importo diverso, oppure l'importo non compare.

**B.31 il massimale contiene l'esposizione**
`issue: I-11 · tipo: presenza · gravità: alta · judge: sì · fonte: contratto, art. 10.2`
Verifica: Il deliverable afferma che l'esposizione ricostruita supera il massimale contrattuale e che quest'ultimo la contiene.
Pass se: compare l'affermazione che il massimale è inferiore all'esposizione ricostruita e che opera come limite.
Fail se: l'affermazione non compare, oppure il massimale è applicato prima della ricostruzione voce per voce.

**B.32 il massimale non opera per dolo o colpa grave**
`issue: I-12 · tipo: presenza · gravità: alta · judge: sì · fonte: contratto, art. 10.3; art. 1229 c.c.`
Verifica: Il deliverable afferma che il massimale e le esclusioni non operano in caso di dolo o di colpa grave.
Pass se: compare l'affermazione che le limitazioni non operano in caso di dolo o colpa grave.
Fail se: l'affermazione non compare, oppure il massimale è presentato come operante in ogni caso.

**B.33 elemento su cui si costruisce la colpa grave**
`issue: I-12 · tipo: attribuzione · gravità: alta · judge: sì · fonte: rapporto del 14 novembre 2033, punto 3; contratto, art. 10.3`
Verifica: Il deliverable individua nel riconoscimento, contenuto nel rapporto di intervento del novembre 2033, di un difetto di progetto comune alla serie e già oggetto di una modifica rilasciata dall'ufficio tecnico, l'elemento su cui la controparte può fondare l'eccezione di colpa grave.
Pass se: compare il collegamento fra quel rapporto e il rischio che il massimale sia superato.
Fail se: il collegamento non compare.

**B.34 pericolosità dell'email**
`issue: I-13 · tipo: presenza · gravità: alta · judge: sì · fonte: email del 24 maggio 2034`
Verifica: Il deliverable afferma che il messaggio del direttore commerciale del 24 maggio 2034 espone la società, in quanto contiene un'offerta economica e un'ammissione sui difetti.
Pass se: compare l'affermazione che quel messaggio è un elemento a nostro sfavore o un rischio.
Fail se: l'affermazione non compare, oppure il messaggio non è esaminato.

**B.35 qualificazione del rischio dell'email**
`issue: I-13 · tipo: qualificazione · gravità: alta · judge: sì · fonte: email del 24 maggio 2034; art. 2944 c.c.`
Verifica: Il deliverable qualifica il messaggio come possibile riconoscimento del debito o come dichiarazione utilizzabile contro la società.
Pass se: compare, riferita a quel messaggio, una fra: «riconoscimento», «riconoscimento del debito», «ammissione», «dichiarazione utilizzabile contro di noi», «confessione stragiudiziale».
Fail se: il messaggio è qualificato come irrilevante, oppure non è qualificato.

**B.36 azione sull'email**
`issue: I-13 · tipo: presenza · gravità: alta · judge: sì · fonte: email del 24 maggio 2034`
Verifica: Il deliverable indica fra le azioni la circoscrizione degli effetti del messaggio e il divieto che proposte transattive siano formulate da funzioni diverse da quella legale.
Pass se: compare l'azione di chiarire alla controparte la portata del messaggio o di riservare alla funzione legale ogni contatto sulla vertenza.
Fail se: l'azione non compare.

**B.37 divieto di svalutare l'email per difetto di poteri**
`issue: I-13 · tipo: assenza · gravità: media · judge: sì · fonte: email del 24 maggio 2034`
Verifica: Il deliverable non afferma che il messaggio sia privo di rilievo perché proveniente da una funzione priva del potere di impegnare la società.
Pass se: non compare l'affermazione che il messaggio è irrilevante per difetto di poteri.
Fail se: compare quell'affermazione.
Indifferente: l'indicazione del difetto di poteri come argomento da spendere, purché non presentato come risolutivo.

**B.38 importo della penale per il ritardo**
`issue: I-14 · tipo: valore · gravità: media · judge: no · fonte: 3 settimane compiute allo 0,5% di 2.480.000`
Verifica: Il deliverable indica 37.200 euro come penale maturata per il ritardo nella consegna.
Pass se: compare l'importo di 37.200 euro.
Fail se: compare un importo diverso, oppure l'importo non compare.

**B.39 esclusività della penale**
`issue: I-14 · tipo: presenza · gravità: media · judge: sì · fonte: contratto, art. 6.3`
Verifica: Il deliverable afferma che la penale è per contratto l'unico rimedio spettante al committente per il ritardo nella consegna.
Pass se: compare l'affermazione che la penale esclude ogni ulteriore pretesa risarcitoria per il ritardo.
Fail se: l'affermazione non compare.

**B.40 scadenza del termine della diffida**
`issue: I-15 · tipo: valore · gravità: alta · judge: no · fonte: 30 giorni dal 12 giugno 2034; diffida, punto 7`
Verifica: Il deliverable indica il 12 luglio 2034 come data di scadenza del termine assegnato dalla diffida.
Pass se: compare la data del 12 luglio 2034.
Fail se: compare una data diversa, oppure la data non compare.

**B.41 componente sostituito non conservato**
`issue: I-16 · tipo: presenza · gravità: alta · judge: sì · fonte: relazione tecnica di parte, punto 3`
Verifica: Il deliverable indica fra gli elementi mancanti il componente sostituito nel gennaio 2034, che il consulente della controparte dà atto di non avere potuto esaminare.
Pass se: compare l'indicazione che il componente non è stato conservato o non è disponibile.
Fail se: l'indicazione non compare.

**B.42 documentazione degli ordini persi mancante**
`issue: I-16 · tipo: presenza · gravità: alta · judge: sì · fonte: diffida, punto 6, lett. d ed elenco degli allegati`
Verifica: Il deliverable indica fra gli elementi mancanti la documentazione degli ordini asseritamente non evasi e dei relativi margini.
Pass se: compare l'indicazione che quella documentazione manca o non è allegata.
Fail se: l'indicazione non compare.

**B.43 storico eventi della linea**
`issue: I-16 · tipo: presenza · gravità: media · judge: sì · fonte: rapporto del 19 aprile 2034, allegati; relazione di parte, punto 1`
Verifica: Il deliverable indica fra gli elementi da acquisire o da conservare i dati di funzionamento registrati dalla linea.
Pass se: compare il riferimento allo storico eventi, ai dati di macchina o ai log della linea.
Fail se: il riferimento non compare.

**B.44 divieto di prudenza paralizzante**
`issue: I-16 · tipo: assenza · gravità: alta · judge: sì · fonte: matrice probatoria`
Verifica: Il deliverable non afferma che la pretesa non sia valutabile in assenza di una consulenza tecnica disposta da un giudice o da un arbitro.
Pass se: non compare l'affermazione che nulla può essere concluso senza una consulenza tecnica d'ufficio.
Fail se: compare quell'affermazione.

**B.45 azione di risposta alla diffida**
`issue: I-17 · tipo: presenza · gravità: alta · judge: sì · fonte: diffida, punto 7`
Verifica: Il deliverable indica fra le azioni la risposta alla diffida entro la scadenza del termine.
Pass se: compare l'azione di rispondere alla diffida, con l'indicazione del termine.
Fail se: l'azione non compare, oppure è priva di termine.

**B.46 azione di richiesta dei documenti**
`issue: I-17 · tipo: presenza · gravità: media · judge: sì · fonte: diffida, elenco degli allegati`
Verifica: Il deliverable indica fra le azioni la richiesta alla controparte dei documenti mancanti.
Pass se: compare l'azione di chiedere alla controparte la documentazione a sostegno delle voci non documentate.
Fail se: l'azione non compare.

**B.47 azione di verifica tecnica**
`issue: I-17 · tipo: presenza · gravità: media · judge: sì · fonte: relazione tecnica di parte; rapporti di intervento`
Verifica: Il deliverable indica fra le azioni l'incarico a un tecnico di fiducia o la valutazione di un accertamento tecnico preventivo.
Pass se: compare l'azione di far verificare le conclusioni tecniche o di attivare un accertamento tecnico prima che la linea sia ulteriormente modificata.
Fail se: l'azione non compare.

**B.48 la relazione di controparte non è inutilizzabile**
`issue: N-01 · tipo: assenza · gravità: alta · judge: sì · fonte: relazione tecnica di parte, punto 1`
Verifica: Il deliverable non afferma che la relazione tecnica del consulente della controparte sia inutilizzabile o priva di valore in quanto redatta fuori dal contraddittorio.
Pass se: non compare l'affermazione che la relazione è inutilizzabile, inammissibile o priva di valore.
Fail se: compare quell'affermazione.
Indifferente: la contestazione delle conclusioni della relazione e il rilievo dei limiti che essa stessa dichiara.

**B.49 il pagamento del saldo non estingue la garanzia**
`issue: N-02 · tipo: assenza · gravità: alta · judge: sì · fonte: contratto, art. 3.3`
Verifica: Il deliverable non eccepisce che il pagamento del saldo senza riserve abbia estinto le pretese del committente.
Pass se: non compare l'eccezione fondata sul pagamento del saldo senza riserve.
Fail se: compare l'affermazione che il pagamento del saldo ha estinto o precluso le pretese.

**B.50 la clausola arbitrale non invalida la diffida**
`issue: N-03 · tipo: assenza · gravità: media · judge: sì · fonte: contratto, art. 14.2`
Verifica: Il deliverable non eccepisce l'invalidità o l'inefficacia della diffida per effetto della clausola compromissoria.
Pass se: non compare l'eccezione di invalidità della diffida fondata sulla clausola arbitrale.
Fail se: compare quell'eccezione.
Indifferente: l'indicazione della clausola arbitrale come sede della futura controversia.

**B.51 il ritardo nella consegna è chiuso**
`issue: N-04 · tipo: assenza · gravità: media · judge: sì · fonte: contratto, art. 6.3; verbale di avviamento, premessa b`
Verifica: Il deliverable non presenta il ritardo nella consegna come voce di rischio ulteriore rispetto alla penale già applicata.
Pass se: il ritardo non compare fra i rischi o fra le voci di esposizione.
Fail se: il ritardo è presentato come rischio ulteriore o come voce di esposizione.

**B.52 le riserve del verbale non riguardano le prestazioni**
`issue: N-05 · tipo: assenza · gravità: media · judge: sì · fonte: verbale di avviamento, punti 3 e 4`
Verifica: Il deliverable non presenta le riserve apposte nel verbale di avviamento come indice di un collaudo non superato.
Pass se: non compare l'affermazione che il collaudo non è stato superato o che le riserve incidono sulle prestazioni.
Fail se: compare quell'affermazione.

**B.53 il collaudo è un punto di forza**
`issue: N-07 · tipo: assenza · gravità: media · judge: sì · fonte: verbale di avviamento, punti 2 e 3`
Verifica: Il deliverable non presenta l'esito delle prove prestazionali del 4 novembre 2033 come elemento sfavorevole alla società.
Pass se: il collaudo non compare fra i punti di debolezza.
Fail se: il collaudo è presentato come punto di debolezza o come elemento a sfavore.

**B.54 simmetria sulla clausola a nostro favore**
`issue: N-06 · tipo: assenza · gravità: media · judge: sì · fonte: contratto, art. 10.1`
Verifica: Il deliverable non presenta come rischio la clausola che esclude il lucro cessante e i danni indiretti.
Pass se: quella clausola non compare fra i rischi.
Fail se: la clausola è presentata come rischio o come criticità.

**B.55 divieto di presumere l'accoglimento dell'eccezione**
`issue: I-19 · tipo: assenza · gravità: alta · judge: sì · fonte: contratto, art. 9.3; art. 2965 c.c.`
Verifica: Il deliverable non afferma che l'eccezione di decadenza sarà accolta.
Pass se: non compare l'affermazione che l'eccezione sarà accolta o che la controparte perderà su quel punto.
Fail se: compare quell'affermazione.

**B.56 divieto di presumere la definizione della vertenza**
`issue: I-19 · tipo: assenza · gravità: media · judge: sì · fonte: -`
Verifica: Il deliverable non afferma che la controversia si chiuderà a una determinata cifra o che la controparte rinuncerà alle proprie pretese.
Pass se: non compare l'affermazione che la vertenza si chiuderà a una cifra determinata o che la controparte rinuncerà.
Fail se: compare quell'affermazione.
Indifferente: l'indicazione di un intervallo di riferimento per una eventuale trattativa, purché presentato come tale.

**B.57 simmetria sugli elementi neutri**
`issue: I-18 · tipo: assenza · gravità: bassa · judge: sì · fonte: -`
Verifica: Il deliverable non presenta come rilievo la certificazione di qualità del fornitore.
Pass se: la certificazione di qualità non compare fra i rilievi.
Fail se: la certificazione di qualità è indicata come rilievo o come rischio.


## C. INDICI, DATE E VALORI CALCOLATI

**C.1 differenza fra richiesta ed esposizione**
`issue: I-01 · tipo: valore · gravità: bassa · judge: no · fonte: 3.240.000 - 372.000`
Verifica: Il deliverable indica la differenza fra l'importo richiesto e l'esposizione stimata.
Pass se: compare il valore 2.868.000 riferito a quella differenza.
Fail se: compare un valore diverso, oppure la differenza non è indicata.

**C.2 quota non documentata della richiesta**
`issue: I-02 · tipo: valore · gravità: bassa · judge: no · fonte: 1.920.000 / 3.240.000`
Verifica: Il deliverable indica la quota percentuale della richiesta priva di riscontro documentale.
Pass se: compare il valore 59,26 per cento, oppure 59,26%.
Fail se: compare un valore diverso, oppure la quota non è indicata.

**C.3 ordine dei passaggi nel calcolo**
`issue: I-11 · tipo: presenza · gravità: alta · judge: sì · fonte: contratto, art. 10.2`
Verifica: Il deliverable applica il massimale dopo avere ricostruito l'esposizione voce per voce, e non come riduzione diretta dell'importo richiesto.
Pass se: compare la sequenza: ricostruzione voce per voce, somma, applicazione del massimale.
Fail se: il massimale è applicato direttamente all'importo richiesto, oppure l'ordine dei passaggi non è esplicitato.

**C.4 derivazione errata dell'esposizione**
`issue: I-11 · tipo: assenza · gravità: media · judge: sì · fonte: matrice probatoria`
Verifica: Il deliverable non presenta l'esposizione come risultato della sottrazione dall'importo richiesto delle sole voci contestate, senza ricostruzione voce per voce.
Pass se: non compare un calcolo che parta da 3.240.000 euro e sottragga le voci contestate.
Fail se: l'esposizione è presentata come differenza fra l'importo richiesto e le voci contestate.

**C.5 derivazione errata della decadenza**
`issue: I-04 · tipo: assenza · gravità: media · judge: sì · fonte: contratto, art. 9.3`
Verifica: Il deliverable non fa decorrere il termine di denuncia dell'episodio di gennaio dalla data del rapporto di intervento anziché dalla data della scoperta.
Pass se: non compare l'indicazione che il termine decorre dal 12 gennaio 2034.
Fail se: il termine è fatto decorrere dalla data del rapporto di intervento.

---

**Conteggi.** 19 issue di merito, 7 controlled non-issue, 68 criteri atomici, di cui 44 al judge e 24 a verifica meccanica.
