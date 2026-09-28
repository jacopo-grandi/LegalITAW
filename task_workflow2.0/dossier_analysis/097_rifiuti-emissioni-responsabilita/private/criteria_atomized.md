# WF2-097 - Criteri atomizzati

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
Pass se    è presente environmental_compliance_memo.md
Fail se    il file manca oppure il nome diverge.

*metadati non forniti al judge* - fonte: public/response_template.md; gravita: media; instradamento: verifica meccanica

**A.2 sezioni del memo**  [issue: -] [tipo: struttura]

Verifica   Il deliverable contiene le sezioni indicate, nell'ordine indicato.
Pass se    le intestazioni compaiono tutte e nella sequenza del response_template
Fail se    manca un'intestazione oppure l'ordine differisce.
Indifferente  la formulazione delle intestazioni oltre le prime ventidue battute.

*metadati non forniti al judge* - fonte: public/response_template.md; gravita: media; instradamento: verifica meccanica

**A.3 data di riferimento**  [issue: -] [tipo: valore]

Verifica   Il deliverable assume come data di riferimento il 10 settembre 2026.
Pass se    compare «10 settembre 2026» come data alla quale il memo è riferito
Fail se    è assunta una data diversa, oppure la data di riferimento non compare.
Indifferente  il formato della data.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: alta; instradamento: verifica meccanica

**A.4 evento di decorrenza per ogni scadenza**  [issue: -] [tipo: struttura]

Verifica   Ogni scadenza indica l'evento da cui decorre.
Pass se    ciascuna scadenza riporta l'evento di decorrenza
Fail se    una o più scadenze non indicano l'evento di decorrenza.
Indifferente  la forma dell'indicazione.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: alta; instradamento: verifica meccanica

**A.5 calcolo esposto per ogni scadenza**  [issue: -] [tipo: struttura]

Verifica   Ogni scadenza riporta il calcolo seguito.
Pass se    ciascuna scadenza riporta il passaggio aritmetico o la regola di computo applicata
Fail se    una o più scadenze riportano il solo risultato.
Indifferente  il livello di dettaglio del calcolo.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: alta; instradamento: verifica meccanica

**A.6 distinzione fra esposizione della società e delle persone**  [issue: -] [tipo: struttura]

Verifica   Il deliverable tiene distinte le conseguenze che riguardano la società da quelle che riguardano le persone fisiche.
Pass se    le due categorie sono trattate separatamente o comunque distinte voce per voce
Fail se    le conseguenze sono esposte senza distinguere i due piani.
Indifferente  il modo in cui la distinzione è resa graficamente.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: alta; instradamento: verifica meccanica

**A.7 documento indicato per ogni voce**  [issue: -] [tipo: struttura]

Verifica   Ogni voce indica il documento del fascicolo da cui i dati provengono.
Pass se    ciascuna voce riporta il nome di almeno un allegato
Fail se    una o più voci non riportano alcun allegato.
Indifferente  il numero degli allegati citati per voce.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: alta; instradamento: verifica meccanica

**A.8 riferimenti entro l'elenco chiuso**  [issue: -] [tipo: assenza]

Verifica   Il deliverable non cita norme assenti dal reference pack.
Pass se    Il deliverable non cita norme assenti dal reference pack.
Fail se    compare un riferimento a un atto o a un articolo che non figura in public/02_reference_pack.md.
Indifferente  la scelta di non citare alcuna fonte in una singola voce.

*metadati non forniti al judge* - fonte: public/02_reference_pack.md e private/fonti_chiuse.json; gravita: alta; instradamento: verifica meccanica

**A.9 azioni distinte per vincolo temporale**  [issue: -] [tipo: struttura]

Verifica   Le azioni sono distinte fra quelle da compiere entro una data determinata e quelle il cui momento resta a scelta della società.
Pass se    l'elenco delle azioni distingue le due categorie
Fail se    le azioni sono elencate senza alcuna distinzione temporale.
Indifferente  l'ordine interno a ciascuna categoria.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: alta; instradamento: verifica meccanica

**A.10 limite di parole**  [issue: -] [tipo: struttura]

Verifica   Il deliverable resta entro il limite di parole.
Pass se    il conteggio delle parole non supera 3200
Fail se    il conteggio supera il limite.

*metadati non forniti al judge* - fonte: public/response_template.md; gravita: bassa; instradamento: verifica meccanica


## Sezione B - merito

Stato del fascicolo alla data di riferimento: verbale di prescrizioni ricevuto il 3 settembre 2026 e termini non ancora scaduti; nessuna domanda di rinnovo dell'autorizzazione presentata; intervento sul sistema di abbattimento avviato e non concluso; nessun procedimento sanzionatorio amministrativo avviato

**B.1 decorrenza della durata dell'autorizzazione**  [issue: I-01] [tipo: attribuzione]

Verifica   Il deliverable riconduce la decorrenza della durata dell'autorizzazione alla data del suo rilascio.
Pass se    compare l'affermazione che i quindici anni decorrono dal rilascio del provvedimento
Fail se    la decorrenza è ricondotta a un evento diverso dal rilascio.
Indifferente  il richiamo alla data di messa a regime.

*metadati non forniti al judge* - fonte: 01_autorizzazione_emissioni_in_atmosfera.md; art. 269, comma 7, del codice dell'ambiente; gravita: alta; instradamento: judge

**B.2 anticipo della domanda di rinnovo**  [issue: I-01] [tipo: presenza]

Verifica   Il deliverable afferma che la domanda di rinnovo va presentata almeno un anno prima della scadenza.
Pass se    compare l'affermazione dell'anticipo di almeno un anno rispetto alla scadenza
Fail se    è indicato un anticipo diverso, oppure il punto non è trattato.
Indifferente  il richiamo all'effetto del rinnovo sulla nuova durata.

*metadati non forniti al judge* - fonte: art. 269, comma 7, del codice dell'ambiente; gravita: alta; instradamento: judge

**B.3 assenza della domanda di rinnovo**  [issue: I-01] [tipo: presenza]

Verifica   Il deliverable afferma che nel fascicolo non risulta presentata alcuna domanda di rinnovo e che il termine è decorso.
Pass se    compare l'affermazione che nessuna domanda risulta presentata e che il termine è decorso
Fail se    è affermato che la domanda è stata presentata, oppure che il termine non è ancora decorso.
Indifferente  l'indicazione dei giorni di ritardo.

*metadati non forniti al judge* - fonte: 09_nota_del_consulente_ambientale.md, punto 5.3; gravita: alta; instradamento: judge

**B.4 efficacia dell'autorizzazione alla data di riferimento**  [issue: I-02] [tipo: presenza]

Verifica   Il deliverable afferma che alla data di riferimento l'autorizzazione è ancora efficace e l'esercizio è legittimo sotto questo profilo.
Pass se    compare l'affermazione che l'autorizzazione è ancora efficace alla data di riferimento
Fail se    è affermato che la società esercita con autorizzazione scaduta o decaduta.
Indifferente  l'indicazione del tempo residuo.

*metadati non forniti al judge* - fonte: 01_autorizzazione_emissioni_in_atmosfera.md; gravita: alta; instradamento: judge

**B.5 sanzione dell'esercizio con autorizzazione scaduta**  [issue: I-02] [tipo: presenza]

Verifica   Il deliverable afferma che continuare l'esercizio con autorizzazione scaduta è punito con sanzione penale.
Pass se    compare l'affermazione che la prosecuzione dell'esercizio con autorizzazione scaduta è penalmente sanzionata
Fail se    la conseguenza è qualificata come sanzione amministrativa, oppure il punto non è trattato.
Indifferente  l'indicazione della cornice edittale.

*metadati non forniti al judge* - fonte: art. 279, comma 1, del codice dell'ambiente; gravita: alta; instradamento: judge

**B.6 iniziativa sul rinnovo**  [issue: I-02] [tipo: presenza]

Verifica   Il deliverable indica fra le azioni la presentazione immediata della domanda di rinnovo.
Pass se    fra le azioni compare la presentazione della domanda di rinnovo senza attendere
Fail se    l'azione non è indicata, oppure è collocata in una data successiva scelta per comodità.
Indifferente  la forma proposta per la domanda.

*metadati non forniti al judge* - fonte: art. 269, comma 7, del codice dell'ambiente; gravita: alta; instradamento: judge

**B.7 qualificazione del superamento del valore limite**  [issue: I-03] [tipo: qualificazione]

Verifica   Il deliverable qualifica il superamento del valore limite al punto E2 come contravvenzione punita con pena alternativa.
Pass se    compare, riferita al superamento del valore limite, una fra: «contravvenzione»; «reato contravvenzionale»; «illecito penale punito con l'arresto o con l'ammenda»
Fail se    il superamento è qualificato come illecito amministrativo, oppure come inadempimento verso l'autorità.
Indifferente  l'indicazione della cornice edittale.

*metadati non forniti al judge* - fonte: art. 279, comma 2, del codice dell'ambiente; gravita: alta; instradamento: judge

**B.8 mancato autocontrollo del primo semestre**  [issue: I-04] [tipo: presenza]

Verifica   Il deliverable rileva che per il primo semestre 2026 non risulta alcun autocontrollo alle emissioni.
Pass se    compare il rilievo dell'assenza dell'autocontrollo del primo semestre 2026
Fail se    il rilievo non compare, oppure è affermato che gli autocontrolli sono stati eseguiti regolarmente.
Indifferente  l'indicazione dei punti che l'autocontrollo avrebbe dovuto riguardare.

*metadati non forniti al judge* - fonte: 09_nota_del_consulente_ambientale.md, punto 3; 01_autorizzazione_emissioni_in_atmosfera.md, Allegato tecnico; gravita: alta; instradamento: judge

**B.9 mancata sostituzione del corredo filtrante**  [issue: I-04] [tipo: presenza]

Verifica   Il deliverable rileva che il corredo filtrante del punto E2 non è stato sostituito entro la periodicità prescritta.
Pass se    compare il rilievo che la sostituzione integrale del corredo filtrante non è avvenuta entro la periodicità prescritta
Fail se    il rilievo non compare, oppure la manutenzione è presentata come conforme alla prescrizione.
Indifferente  il richiamo alle sostituzioni parziali annotate.

*metadati non forniti al judge* - fonte: 01_autorizzazione_emissioni_in_atmosfera.md, prescrizione 5.2; 09_nota_del_consulente_ambientale.md, punto 4; gravita: alta; instradamento: judge

**B.10 regime della violazione delle prescrizioni**  [issue: I-04] [tipo: qualificazione]

Verifica   Il deliverable qualifica la violazione delle prescrizioni dell'autorizzazione come assoggettata a sanzione amministrativa pecuniaria irrogata dall'autorità competente.
Pass se    compare, riferita alla violazione delle prescrizioni, una fra: «sanzione amministrativa pecuniaria»; «illecito amministrativo»; «sanzione irrogata dall'autorità competente»
Fail se    la violazione delle prescrizioni è qualificata come reato.
Indifferente  l'indicazione dell'importo minimo e massimo.

*metadati non forniti al judge* - fonte: art. 279, comma 2-bis, del codice dell'ambiente; gravita: alta; instradamento: judge

**B.11 presupposto dell'aggravante**  [issue: I-05] [tipo: presenza]

Verifica   Il deliverable afferma che la pena dell'arresto si applica sempre se il superamento dei valori limite di emissione determina anche il superamento dei valori limite di qualità dell'aria.
Pass se    compare l'affermazione che l'aggravante presuppone il superamento dei valori limite di qualità dell'aria
Fail se    l'aggravante è collegata alla misura del superamento del valore limite di emissione, oppure il punto non è trattato.
Indifferente  l'indicazione della pena.

*metadati non forniti al judge* - fonte: art. 279, comma 5, del codice dell'ambiente; gravita: alta; instradamento: judge

**B.12 perimetro della responsabilità dell'ente**  [issue: I-05] [tipo: attribuzione]

Verifica   Il deliverable riconduce la responsabilità dell'ente alla sola ipotesi aggravata.
Pass se    compare l'affermazione che è reato presupposto la sola ipotesi aggravata e non il superamento semplice
Fail se    la responsabilità dell'ente è ricondotta al superamento del valore limite in quanto tale, oppure è esclusa senza indicarne la ragione.
Indifferente  l'indicazione del numero massimo di quote.

*metadati non forniti al judge* - fonte: art. 25-undecies, comma 2, lettera h), del decreto sulla responsabilità degli enti; gravita: alta; instradamento: judge

**B.13 dati mancanti sulla qualità dell'aria**  [issue: I-05] [tipo: presenza]

Verifica   Il deliverable indica che il fascicolo non contiene dati di qualità dell'aria e che senza quei dati il presupposto dell'aggravante non è verificabile.
Pass se    compare l'indicazione che i dati di qualità dell'aria mancano e che il presupposto non è verificabile
Fail se    il presupposto è dato per accertato o per escluso, oppure è dichiarata l'impossibilità di concludere senza indicare che cosa manca.
Indifferente  la proposta su come acquisire i dati.

*metadati non forniti al judge* - fonte: 09_nota_del_consulente_ambientale.md, punto 5.6; gravita: alta; instradamento: judge

**B.14 presupposto della procedura estintiva**  [issue: I-06] [tipo: presenza]

Verifica   Il deliverable afferma che la procedura estintiva si applica alle contravvenzioni che non hanno cagionato danno o pericolo concreto e attuale di danno alle risorse protette.
Pass se    compare l'affermazione del presupposto dell'assenza di danno o di pericolo concreto e attuale di danno
Fail se    la procedura è presentata come applicabile a qualunque violazione, oppure il presupposto non è indicato.
Indifferente  l'osservazione che il verbale ne presuppone la sussistenza senza motivarla.

*metadati non forniti al judge* - fonte: art. 318-bis del codice dell'ambiente; gravita: alta; instradamento: judge

**B.15 decorrenza dei termini delle prescrizioni**  [issue: I-07] [tipo: attribuzione]

Verifica   Il deliverable riconduce la decorrenza dei termini delle prescrizioni al ricevimento del verbale.
Pass se    compare l'affermazione che i termini decorrono dal ricevimento del verbale
Fail se    la decorrenza è ricondotta al sopralluogo o alla data di emissione del verbale.
Indifferente  il richiamo alla ricevuta di avvenuta consegna.

*metadati non forniti al judge* - fonte: 02_verbale_di_prescrizioni.md, prescrizioni 1 e 2 e relata di notifica; gravita: alta; instradamento: judge

**B.16 distinzione dei due termini**  [issue: I-07] [tipo: presenza]

Verifica   Il deliverable tratta separatamente i termini delle due prescrizioni.
Pass se    le due prescrizioni compaiono con termini distinti
Fail se    è indicato un unico termine per entrambe le prescrizioni.
Indifferente  l'ordine in cui le due prescrizioni sono esposte.

*metadati non forniti al judge* - fonte: 02_verbale_di_prescrizioni.md, prescrizioni 1 e 2; gravita: alta; instradamento: judge

**B.17 condizioni della proroga**  [issue: I-08] [tipo: presenza]

Verifica   Il deliverable afferma che la proroga è concessa per una sola volta, per un periodo non superiore a sei mesi, su richiesta e in presenza di specifiche e documentate circostanze non imputabili al contravventore.
Pass se    compaiono l'unicità della proroga, il limite di sei mesi e il presupposto delle circostanze non imputabili
Fail se    la proroga è presentata come rinnovabile o come concedibile su semplice richiesta, oppure le condizioni non sono indicate.
Indifferente  il richiamo alla comunicazione al pubblico ministero.

*metadati non forniti al judge* - fonte: art. 318-ter, comma 1, del codice dell'ambiente; gravita: media; instradamento: judge

**B.18 misura della somma per l'estinzione**  [issue: I-09] [tipo: presenza]

Verifica   Il deliverable afferma che la somma da pagare è pari a un quarto del massimo dell'ammenda stabilita per la contravvenzione.
Pass se    compare l'affermazione che la somma è pari a un quarto del massimo dell'ammenda
Fail se    è indicata una frazione diversa, oppure il riferimento è al minimo dell'ammenda.
Indifferente  l'indicazione del massimo su cui la frazione è calcolata.

*metadati non forniti al judge* - fonte: art. 318-quater, comma 2, del codice dell'ambiente; gravita: alta; instradamento: judge

**B.19 effetto del pagamento**  [issue: I-09] [tipo: presenza]

Verifica   Il deliverable afferma che il pagamento, da effettuare entro trenta giorni dall'ammissione, è ciò che produce l'estinzione del reato.
Pass se    compare l'affermazione che l'estinzione consegue al pagamento nel termine di trenta giorni
Fail se    l'estinzione è ricondotta al solo adempimento alla prescrizione.
Indifferente  il richiamo alle modalità del pagamento.

*metadati non forniti al judge* - fonte: art. 318-quater, comma 2, del codice dell'ambiente; gravita: alta; instradamento: judge

**B.20 decorrenza dei termini dell'organo accertatore**  [issue: I-09] [tipo: attribuzione]

Verifica   Il deliverable riconduce i termini di verifica e di comunicazione al pubblico ministero alla scadenza del termine fissato nella prescrizione.
Pass se    compare l'affermazione che quei termini decorrono dalla scadenza del termine fissato nella prescrizione
Fail se    i termini sono fatti decorrere dalla comunicazione di adempimento della società o dalla verifica.
Indifferente  l'ordine in cui i tre termini sono esposti.

*metadati non forniti al judge* - fonte: art. 318-quater, commi 1, 2 e 3, del codice dell'ambiente; gravita: media; instradamento: judge

**B.21 struttura della soglia volumetrica**  [issue: I-10] [tipo: presenza]

Verifica   Il deliverable afferma che la soglia è di trenta metri cubi complessivi, di cui al massimo dieci metri cubi di rifiuti pericolosi.
Pass se    compare l'affermazione che i dieci metri cubi di pericolosi sono un sotto-limite interno ai trenta complessivi
Fail se    la soglia è letta come trenta metri cubi di non pericolosi ai quali si aggiungono dieci metri cubi di pericolosi.
Indifferente  l'ordine in cui i due valori sono esposti.

*metadati non forniti al judge* - fonte: art. 185-bis, comma 2, lettera b), del codice dell'ambiente; gravita: alta; instradamento: judge

**B.22 superamento del sotto-limite**  [issue: I-10] [tipo: presenza]

Verifica   Il deliverable afferma che il quantitativo di rifiuti pericolosi in deposito supera il sotto-limite.
Pass se    compare l'affermazione che i rifiuti pericolosi in deposito superano il sotto-limite
Fail se    è affermato che il deposito rispetta la soglia, oppure il superamento non è rilevato.
Indifferente  l'indicazione della misura del superamento.

*metadati non forniti al judge* - fonte: 06_procedura_deposito_temporaneo.md, punto 6; gravita: alta; instradamento: judge

**B.23 conseguenza sul regime del deposito**  [issue: I-11] [tipo: presenza]

Verifica   Il deliverable afferma che il deposito temporaneo non necessita di autorizzazione soltanto alle condizioni di legge e che, venuta meno una di esse, il deposito non è più coperto da quella previsione.
Pass se    compare l'affermazione che il deposito perde la copertura dell'esonero
Fail se    il superamento è presentato come irregolarità meramente formale, oppure la conseguenza sul regime non è trattata.
Indifferente  la qualificazione sanzionatoria, che il reference pack non consente di verificare.

*metadati non forniti al judge* - fonte: art. 185-bis, commi 2 e 3, del codice dell'ambiente; gravita: alta; instradamento: judge

**B.24 azione sul quantitativo in deposito**  [issue: I-11] [tipo: presenza]

Verifica   Il deliverable indica fra le azioni l'avvio a recupero o smaltimento dei rifiuti pericolosi per riportare il quantitativo entro il sotto-limite.
Pass se    fra le azioni compare l'avvio dei rifiuti pericolosi per rientrare nel sotto-limite
Fail se    l'azione non è indicata.
Indifferente  il momento proposto per l'avvio.

*metadati non forniti al judge* - fonte: 06_procedura_deposito_temporaneo.md, punto 6; gravita: alta; instradamento: judge

**B.25 alternatività delle modalità**  [issue: I-12] [tipo: presenza]

Verifica   Il deliverable afferma che le due modalità di avvio sono alternative e rimesse alla scelta del produttore.
Pass se    compare l'affermazione che le due modalità sono alternative e a scelta del produttore
Fail se    la cadenza trimestrale è presentata come obbligo che si somma alla soglia volumetrica.
Indifferente  l'ordine in cui le due modalità sono esposte.

*metadati non forniti al judge* - fonte: art. 185-bis, comma 2, lettera b), del codice dell'ambiente; gravita: media; instradamento: judge

**B.26 scelta compiuta dalla società**  [issue: I-12] [tipo: presenza]

Verifica   Il deliverable afferma che la società ha scelto la modalità volumetrica con la procedura interna e che il passaggio alla cadenza almeno trimestrale è una scelta disponibile.
Pass se    compaiono la scelta già compiuta e la disponibilità del passaggio alla cadenza trimestrale
Fail se    la scelta compiuta non è rilevata, oppure il passaggio è presentato come imposto.
Indifferente  il momento proposto per l'eventuale passaggio.

*metadati non forniti al judge* - fonte: 06_procedura_deposito_temporaneo.md, punto 4; gravita: media; instradamento: judge

**B.27 unità di misura della soglia**  [issue: I-13] [tipo: presenza]

Verifica   Il deliverable afferma che la soglia è espressa in metri cubi.
Pass se    compare l'affermazione che la soglia è espressa in metri cubi
Fail se    la soglia è riferita a un'unità di misura di peso.
Indifferente  il richiamo ai pesi riportati dalla procedura interna in altra funzione.

*metadati non forniti al judge* - fonte: art. 185-bis, comma 2, lettera b), del codice dell'ambiente; gravita: media; instradamento: judge

**B.28 termine di annotazione sul registro**  [issue: I-14] [tipo: presenza]

Verifica   Il deliverable afferma che il produttore annota almeno entro dieci giorni lavorativi dalla produzione del rifiuto.
Pass se    compare l'indicazione del termine di dieci giorni lavorativi dalla produzione
Fail se    è indicato un termine diverso, oppure i giorni sono qualificati come di calendario.
Indifferente  il richiamo al termine per l'annotazione dello scarico.

*metadati non forniti al judge* - fonte: art. 190, comma 3, del codice dell'ambiente; gravita: media; instradamento: judge

**B.29 annotazione tardiva rilevata**  [issue: I-14] [tipo: presenza]

Verifica   Il deliverable rileva che l'annotazione del rifiuto prodotto il 24 agosto 2026 è avvenuta oltre il termine.
Pass se    compare il rilievo che quell'annotazione è tardiva
Fail se    il rilievo non compare, oppure l'annotazione è presentata come tempestiva.
Indifferente  l'indicazione dell'entità del ritardo.

*metadati non forniti al judge* - fonte: 06_procedura_deposito_temporaneo.md, punto 7; 04_registro_cronologico_carico_scarico.md, registrazione n. 118; gravita: media; instradamento: judge

**B.30 consegna e responsabilità**  [issue: I-15] [tipo: presenza]

Verifica   Il deliverable afferma che la consegna dei rifiuti non costituisce esclusione automatica della responsabilità.
Pass se    compare l'affermazione che la consegna non esclude automaticamente la responsabilità
Fail se    è affermato che con la consegna al trasportatore la responsabilità è trasferita.
Indifferente  il richiamo alla responsabilità di ciascun operatore per la parte di propria competenza.

*metadati non forniti al judge* - fonte: art. 188, comma 4, del codice dell'ambiente; gravita: alta; instradamento: judge

**B.31 alternativa per l'esclusione della responsabilità**  [issue: I-15] [tipo: presenza]

Verifica   Il deliverable espone entrambe le condizioni alternative: la ricezione della copia controfirmata e datata in arrivo dal destinatario entro tre mesi dal conferimento al trasportatore, ovvero, alla scadenza, la comunicazione della mancata ricezione alle autorità competenti.
Pass se    compaiono entrambe le condizioni alternative
Fail se    è indicata una sola delle due condizioni.
Indifferente  l'ordine in cui le due condizioni sono esposte.

*metadati non forniti al judge* - fonte: art. 188, comma 4, del codice dell'ambiente; gravita: alta; instradamento: judge

**B.32 stato del termine di tre mesi**  [issue: I-15] [tipo: presenza]

Verifica   Il deliverable afferma che alla data di riferimento il termine di tre mesi non è scaduto.
Pass se    compare l'affermazione che il termine non è ancora scaduto
Fail se    è affermato che il termine è scaduto e che la responsabilità non è esclusa, oppure lo stato del termine non è indicato.
Indifferente  l'indicazione dei giorni residui.

*metadati non forniti al judge* - fonte: 05_formulario_identificazione_rifiuti.md; 09_nota_del_consulente_ambientale.md, punto 5.5; gravita: alta; instradamento: judge

**B.33 criterio di individuazione del gestore**  [issue: I-16] [tipo: attribuzione]

Verifica   Il deliverable riconduce la posizione di gestore al potere decisionale circa l'installazione o l'esercizio dello stabilimento.
Pass se    compare l'affermazione che il gestore è individuato in base al potere decisionale
Fail se    la posizione di gestore è ricondotta alla qualifica formale, alla titolarità della procura o alla sola indicazione contenuta nell'autorizzazione.
Indifferente  il richiamo all'unicità del gestore dello stabilimento.

*metadati non forniti al judge* - fonte: art. 268, comma 1, lettere h) e n), del codice dell'ambiente; gravita: alta; instradamento: judge

**B.34 elementi esposti sulla posizione di gestore**  [issue: I-16] [tipo: presenza]

Verifica   Il deliverable espone sia l'indicazione del gestore contenuta nell'autorizzazione sia le riserve al consiglio di amministrazione contenute nella procura.
Pass se    compaiono entrambi gli elementi
Fail se    è esposto uno solo dei due elementi.
Indifferente  il richiamo ai limiti di spesa per singolo contratto.

*metadati non forniti al judge* - fonte: 01_autorizzazione_emissioni_in_atmosfera.md, articolo 1; 07_procura_speciale_direttore_stabilimento.md, riserve finali; gravita: alta; instradamento: judge

**B.35 sospensione della conclusione sul gestore**  [issue: I-16] [tipo: presenza]

Verifica   Il deliverable non attribuisce la posizione di gestore a uno dei due soggetti e indica la documentazione da acquisire per rispondere.
Pass se    la questione è tenuta aperta e la documentazione mancante è indicata
Fail se    la posizione di gestore è attribuita a uno dei due soggetti, oppure è dichiarata l'impossibilità di concludere senza indicare che cosa manca.
Indifferente  l'ordine in cui la documentazione mancante è elencata.

*metadati non forniti al judge* - fonte: 08_email_direttore_di_stabilimento.md; 09_nota_del_consulente_ambientale.md, punto 5.8; gravita: alta; instradamento: judge

**B.36 comunicazione della variazione del gestore**  [issue: I-16] [tipo: presenza]

Verifica   Il deliverable afferma che la variazione del gestore va comunicata dal nuovo gestore entro dieci giorni dalla data in cui essa acquista efficacia e che nel fascicolo non risulta alcuna comunicazione.
Pass se    compaiono il termine di dieci giorni a carico del nuovo gestore e l'assenza della comunicazione
Fail se    il termine è attribuito al gestore uscente, è indicato un termine diverso, oppure il punto non è trattato.
Indifferente  l'osservazione che la data di decorrenza non è determinabile.

*metadati non forniti al judge* - fonte: art. 269, comma 11-bis, del codice dell'ambiente; 09_nota_del_consulente_ambientale.md, punto 5.2; gravita: media; instradamento: judge

**B.37 sovra-segnalazione - formulario cartaceo**  [issue: N-01] [tipo: assenza]

Verifica   Il deliverable non indica come irregolare il formato cartaceo del formulario emesso il 26 agosto 2026.
Pass se    Il deliverable non indica come irregolare il formato cartaceo del formulario emesso il 26 agosto 2026.
Fail se    è affermato che quel formulario è irregolare perché emesso in formato cartaceo, o che il relativo trasporto è privo di titolo.
Indifferente  l'indicazione del termine finale entro cui il formato cartaceo è ammesso.

*metadati non forniti al judge* - fonte: art. 13, comma 5-bis, del decreto-legge 200/2025; gravita: alta; instradamento: judge

**B.38 sovra-segnalazione - soglia complessiva**  [issue: N-02] [tipo: assenza]

Verifica   Il deliverable non afferma che il deposito supera la soglia complessiva di trenta metri cubi.
Pass se    Il deliverable non afferma che il deposito supera la soglia complessiva di trenta metri cubi.
Fail se    è affermato che il volume complessivo in deposito supera i trenta metri cubi.
Indifferente  l'indicazione del volume complessivo in altra funzione.

*metadati non forniti al judge* - fonte: 06_procedura_deposito_temporaneo.md, punto 6; gravita: alta; instradamento: judge

**B.39 sovra-segnalazione - esonero dal registro**  [issue: N-03] [tipo: assenza]

Verifica   Il deliverable non accoglie l'applicazione dell'esonero dalla tenuta del registro.
Pass se    Il deliverable non accoglie l'applicazione dell'esonero dalla tenuta del registro.
Fail se    è affermato che la società è esonerata dalla tenuta del registro, o che l'esonero si applica perché ciascun reparto conta meno di dieci addetti.
Indifferente  la menzione dell'esonero per escluderne l'applicabilità.

*metadati non forniti al judge* - fonte: art. 190, comma 5, del codice dell'ambiente; 06_procedura_deposito_temporaneo.md, punto 2; gravita: media; instradamento: judge

**B.40 sovra-segnalazione - punto di emissione E4**  [issue: N-04] [tipo: assenza]

Verifica   Il deliverable non indica un superamento al punto di emissione E4.
Pass se    Il deliverable non indica un superamento al punto di emissione E4.
Fail se    è affermato che al punto E4 il valore limite è superato, o che i superamenti sono due.
Indifferente  la menzione del punto E4 fra quelli misurati e conformi.

*metadati non forniti al judge* - fonte: 03_rapporto_di_prova_emissioni.md, punti 4, 5 e 6; gravita: alta; instradamento: judge

**B.41 sovra-segnalazione - perdita di carico**  [issue: N-05] [tipo: assenza]

Verifica   Il deliverable non fonda la violazione della prescrizione sulla perdita di carico differenziale.
Pass se    Il deliverable non fonda la violazione della prescrizione sulla perdita di carico differenziale.
Fail se    è affermato che la perdita di carico rilevata supera la soglia prescritta, o che è quel superamento a rendere dovuta la sostituzione.
Indifferente  la menzione del valore rilevato in altra funzione.

*metadati non forniti al judge* - fonte: 09_nota_del_consulente_ambientale.md, punto 4; gravita: media; instradamento: judge

**B.42 sovra-segnalazione - iscrizione all'Albo**  [issue: N-06] [tipo: assenza]

Verifica   Il deliverable non indica l'iscrizione della società all'Albo fra gli adempimenti mancanti.
Pass se    Il deliverable non indica l'iscrizione della società all'Albo fra gli adempimenti mancanti.
Fail se    è affermato che la società deve iscriversi all'Albo dei gestori ambientali.
Indifferente  la menzione dell'iscrizione del trasportatore.

*metadati non forniti al judge* - fonte: 06_procedura_deposito_temporaneo.md, punto 8; art. 212, commi 5 e 8, del codice dell'ambiente; gravita: media; instradamento: judge

**B.43 simmetria del controllo - elementi favorevoli**  [issue: -] [tipo: assenza]

Verifica   Il deliverable non omette gli elementi che riducono l'esposizione della società.
Pass se    Il deliverable non omette gli elementi che riducono l'esposizione della società.
Fail se    non compare alcuno degli elementi favorevoli documentati, quali l'efficacia dell'autorizzazione alla data di riferimento, la conformità del punto E4, l'intervento già avviato sul sistema di abbattimento o la pendenza del termine di tre mesi.
Indifferente  quali fra questi elementi sono esposti, purché ne compaia almeno uno.

*metadati non forniti al judge* - fonte: private/challenge_map.json, controlled non-issue; gravita: media; instradamento: judge

**B.44 presunzione dell'esito - estinzione e rinnovo**  [issue: -] [tipo: assenza]

Verifica   Il deliverable non presenta come acquisiti l'estinzione della contravvenzione né il rinnovo dell'autorizzazione.
Pass se    Il deliverable non presenta come acquisiti l'estinzione della contravvenzione né il rinnovo dell'autorizzazione.
Fail se    è affermato che la contravvenzione si estinguerà, o che il rinnovo sarà concesso.
Indifferente  l'indicazione dei presupposti da cui l'uno e l'altro dipendono.

*metadati non forniti al judge* - fonte: private/challenge_map.json, dati mancanti; gravita: alta; instradamento: judge


## Sezione C - date e valori calcolati

**C.1 scadenza dell'autorizzazione**  [issue: I-01] [tipo: valore]

Verifica   Il deliverable indica il 22 marzo 2027 come scadenza dell'autorizzazione alle emissioni.
Pass se    compare la data «22 marzo 2027» riferita alla scadenza dell'autorizzazione
Fail se    è indicata una data diversa, oppure la scadenza non compare.
Indifferente  l'indicazione del tempo residuo.

*metadati non forniti al judge* - fonte: art. 269, comma 7, del codice dell'ambiente; gravita: alta; instradamento: verifica meccanica

**C.2 termine per la domanda di rinnovo**  [issue: I-01] [tipo: valore]

Verifica   Il deliverable indica il 22 marzo 2026 come termine per la presentazione della domanda di rinnovo.
Pass se    compare la data «22 marzo 2026» riferita al termine per la domanda di rinnovo
Fail se    è indicata una data diversa, oppure il termine non compare.
Indifferente  l'indicazione dei giorni di ritardo.

*metadati non forniti al judge* - fonte: art. 269, comma 7, del codice dell'ambiente; gravita: alta; instradamento: verifica meccanica

**C.3 valore misurato al punto E2**  [issue: I-03] [tipo: valore]

Verifica   Il deliverable indica in 68 milligrammi per normal metro cubo il valore misurato al punto E2.
Pass se    compare la misura «68 mg/Nm3» riferita al punto E2
Fail se    è indicata una misura diversa, oppure il valore misurato non compare.
Indifferente  il modo in cui l'unità di misura è scritta.

*metadati non forniti al judge* - fonte: 03_rapporto_di_prova_emissioni.md, punto 4; gravita: alta; instradamento: verifica meccanica

**C.4 scadenza dell'autocontrollo del primo semestre**  [issue: I-04] [tipo: valore]

Verifica   Il deliverable indica il 30 giugno 2026 come termine entro cui l'autocontrollo del primo semestre 2026 andava eseguito.
Pass se    compare la data «30 giugno 2026» riferita al termine dell'autocontrollo del primo semestre
Fail se    è indicata una data diversa, oppure il termine non compare.
Indifferente  l'indicazione dei giorni decorsi.

*metadati non forniti al judge* - fonte: 01_autorizzazione_emissioni_in_atmosfera.md, Allegato tecnico; gravita: media; instradamento: verifica meccanica

**C.5 termine della sostituzione periodica del corredo filtrante**  [issue: I-04] [tipo: valore]

Verifica   Il deliverable indica il 14 settembre 2022 come termine entro cui la sostituzione integrale del corredo filtrante andava effettuata.
Pass se    compare la data «14 settembre 2022» riferita al termine della sostituzione
Fail se    è indicata una data diversa, oppure il termine non compare.
Indifferente  l'indicazione dei giorni decorsi.

*metadati non forniti al judge* - fonte: 01_autorizzazione_emissioni_in_atmosfera.md, prescrizione 5.2; gravita: media; instradamento: verifica meccanica

**C.6 scadenza della prima prescrizione**  [issue: I-07] [tipo: valore]

Verifica   Il deliverable indica il 13 ottobre 2026 come scadenza della prescrizione 1.
Pass se    compare la data «13 ottobre 2026» riferita alla scadenza della prescrizione 1
Fail se    è indicata una data diversa, oppure la scadenza non compare.
Indifferente  l'indicazione dei giorni residui.

*metadati non forniti al judge* - fonte: 02_verbale_di_prescrizioni.md, prescrizione 1; gravita: alta; instradamento: verifica meccanica

**C.7 scadenza della seconda prescrizione**  [issue: I-07] [tipo: valore]

Verifica   Il deliverable indica il 23 settembre 2026 come scadenza della prescrizione 2.
Pass se    compare la data «23 settembre 2026» riferita alla scadenza della prescrizione 2
Fail se    è indicata una data diversa, oppure la scadenza non compare.
Indifferente  l'indicazione dei giorni residui.

*metadati non forniti al judge* - fonte: 02_verbale_di_prescrizioni.md, prescrizione 2; gravita: alta; instradamento: verifica meccanica

**C.8 derivazione errata dal sopralluogo**  [issue: I-07] [tipo: assenza]

Verifica   Il deliverable non computa i termini delle prescrizioni dal sopralluogo.
Pass se    Il deliverable non computa i termini delle prescrizioni dal sopralluogo.
Fail se    compare la data «6 ottobre 2026» oppure la data «16 settembre 2026» come scadenza di una delle due prescrizioni.
Indifferente  la menzione della data del sopralluogo in altra funzione.

*metadati non forniti al judge* - fonte: derivazione da escludere; gravita: alta; instradamento: judge

**C.9 somma per l'estinzione**  [issue: I-09] [tipo: valore]

Verifica   Il deliverable indica in 2.500 euro la somma da pagare in sede amministrativa.
Pass se    compare l'importo «2.500» riferito alla somma da pagare in sede amministrativa
Fail se    è indicato un importo diverso, oppure la somma non è quantificata.
Indifferente  il modo in cui l'importo è scritto.

*metadati non forniti al judge* - fonte: art. 318-quater, comma 2, del codice dell'ambiente; gravita: alta; instradamento: verifica meccanica

**C.10 termine della verifica dell'adempimento**  [issue: I-09] [tipo: valore]

Verifica   Il deliverable indica il 12 dicembre 2026 come termine entro cui l'organo accertatore verifica l'adempimento alla prescrizione 1.
Pass se    compare la data «12 dicembre 2026» riferita alla verifica dell'adempimento
Fail se    è indicata una data diversa, oppure il termine non compare.
Indifferente  il richiamo alla modalità della verifica.

*metadati non forniti al judge* - fonte: art. 318-quater, comma 1, del codice dell'ambiente; gravita: media; instradamento: verifica meccanica

**C.11 termine della comunicazione dell'adempimento**  [issue: I-09] [tipo: valore]

Verifica   Il deliverable indica il 10 febbraio 2027 come termine entro cui l'organo accertatore comunica al pubblico ministero l'adempimento alla prescrizione 1.
Pass se    compare la data «10 febbraio 2027» riferita alla comunicazione dell'adempimento
Fail se    è indicata una data diversa, oppure il termine non compare.
Indifferente  l'ordine in cui i termini sono esposti.

*metadati non forniti al judge* - fonte: art. 318-quater, comma 2, del codice dell'ambiente; gravita: media; instradamento: verifica meccanica

**C.12 termine della comunicazione dell'inadempimento**  [issue: I-09] [tipo: valore]

Verifica   Il deliverable indica l'11 gennaio 2027 come termine entro cui l'organo accertatore comunica l'inadempimento alla prescrizione 1.
Pass se    compare la data «11 gennaio 2027» riferita alla comunicazione dell'inadempimento
Fail se    è indicata una data diversa, oppure il termine non compare.
Indifferente  l'ordine in cui i termini sono esposti.

*metadati non forniti al judge* - fonte: art. 318-quater, comma 3, del codice dell'ambiente; gravita: media; instradamento: verifica meccanica

**C.13 volume dei rifiuti pericolosi in deposito**  [issue: I-10] [tipo: valore]

Verifica   Il deliverable indica in 11,8 metri cubi il volume dei rifiuti pericolosi in deposito.
Pass se    compare la misura «11,8» riferita al volume dei rifiuti pericolosi in deposito
Fail se    è indicata una misura diversa, oppure il volume dei pericolosi non compare.
Indifferente  l'indicazione del volume complessivo accanto a quello dei pericolosi.

*metadati non forniti al judge* - fonte: 06_procedura_deposito_temporaneo.md, punto 6; gravita: alta; instradamento: verifica meccanica

**C.14 derivazione errata sui pesi**  [issue: I-13] [tipo: assenza]

Verifica   Il deliverable non verifica il rispetto della soglia del deposito sui pesi.
Pass se    Il deliverable non verifica il rispetto della soglia del deposito sui pesi.
Fail se    il rispetto della soglia è verificato confrontando i pesi in chilogrammi o in tonnellate con la soglia di legge.
Indifferente  la menzione dei pesi in altra funzione.

*metadati non forniti al judge* - fonte: derivazione da escludere; gravita: media; instradamento: judge

**C.15 termine di annotazione del rifiuto**  [issue: I-14] [tipo: valore]

Verifica   Il deliverable indica il 7 settembre 2026 come termine entro cui il rifiuto prodotto il 24 agosto 2026 andava annotato.
Pass se    compare la data «7 settembre 2026» riferita al termine di annotazione
Fail se    è indicata una data diversa, oppure il termine non compare.
Indifferente  l'indicazione dell'entità del ritardo.

*metadati non forniti al judge* - fonte: art. 190, comma 3, del codice dell'ambiente; gravita: media; instradamento: verifica meccanica

**C.16 derivazione errata in giorni di calendario**  [issue: I-14] [tipo: assenza]

Verifica   Il deliverable non computa il termine di annotazione in giorni di calendario.
Pass se    Il deliverable non computa il termine di annotazione in giorni di calendario.
Fail se    il termine di annotazione è computato in giorni di calendario dalla produzione del rifiuto anziché in giorni lavorativi.
Indifferente  la menzione della data di produzione in altra funzione.

*metadati non forniti al judge* - fonte: derivazione da escludere; gravita: media; instradamento: judge

**C.17 termine per la copia controfirmata del formulario**  [issue: I-15] [tipo: valore]

Verifica   Il deliverable indica il 26 novembre 2026 come termine entro cui la copia controfirmata del formulario deve essere ricevuta.
Pass se    compare la data «26 novembre 2026» riferita al termine di tre mesi
Fail se    è indicata una data diversa, oppure il termine non compare.
Indifferente  l'indicazione dei giorni residui.

*metadati non forniti al judge* - fonte: art. 188, comma 4, del codice dell'ambiente; gravita: alta; instradamento: verifica meccanica

**C.18 derivazione errata sull'incertezza al punto E4**  [issue: N-04] [tipo: assenza]

Verifica   Il deliverable non somma l'incertezza estesa al valore misurato al punto E4 per ricavarne un superamento.
Pass se    Il deliverable non somma l'incertezza estesa al valore misurato al punto E4 per ricavarne un superamento.
Fail se    compare la misura «52 mg/Nm3» come valore del punto E4, oppure il superamento al punto E4 è ricavato sommando l'incertezza estesa al valore misurato.
Indifferente  la menzione dell'incertezza estesa in altra funzione.

*metadati non forniti al judge* - fonte: derivazione da escludere; gravita: alta; instradamento: judge
