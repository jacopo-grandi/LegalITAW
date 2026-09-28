# WF2-094 - Criteri atomizzati

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
Pass se    è presente real_estate_red_flag_matrix.md
Fail se    il file manca oppure il nome diverge.

*metadati non forniti al judge* - fonte: public/response_template.md; gravita: media; instradamento: verifica meccanica

**A.2 sezioni della matrice**  [issue: -] [tipo: struttura]

Verifica   Il deliverable contiene le sezioni indicate, nell'ordine indicato.
Pass se    le intestazioni compaiono tutte e nella sequenza del response_template
Fail se    manca un'intestazione oppure l'ordine differisce.
Indifferente  la formulazione delle intestazioni oltre le prime ventidue battute.

*metadati non forniti al judge* - fonte: public/response_template.md; gravita: media; instradamento: verifica meccanica

**A.3 data di riferimento**  [issue: -] [tipo: valore]

Verifica   Il deliverable assume come data di riferimento il 6 ottobre 2026.
Pass se    compare «6 ottobre 2026» come data alla quale l'analisi è riferita
Fail se    è assunta una data diversa, oppure la data di riferimento non compare.
Indifferente  il formato della data.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: alta; instradamento: verifica meccanica

**A.4 stato probatorio per ogni rilievo**  [issue: -] [tipo: struttura]

Verifica   Ogni rilievo indica se poggia su un fatto accertato dal rilievo, su una dichiarazione della venditrice o su un dato mancante.
Pass se    ciascuna voce riporta uno dei tre stati probatori
Fail se    una o più voci non riportano alcuno stato probatorio.
Indifferente  le etichette usate per i tre stati.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: alta; instradamento: verifica meccanica

**A.5 gravità per ogni rilievo**  [issue: -] [tipo: struttura]

Verifica   Ogni rilievo indica la gravità.
Pass se    ciascuna voce riporta un livello di gravità
Fail se    una o più voci non riportano la gravità.
Indifferente  la scala usata per la gravità.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: media; instradamento: verifica meccanica

**A.6 conseguenza sul closing e azione**  [issue: -] [tipo: struttura]

Verifica   Ogni rilievo indica la conseguenza sul closing e l'azione da compiere.
Pass se    ciascuna voce riporta sia la conseguenza sul closing sia l'azione
Fail se    una o più voci riportano solo uno dei due elementi.
Indifferente  l'ordine in cui i due elementi compaiono.

*metadati non forniti al judge* - fonte: public/01_task.md; gravita: alta; instradamento: verifica meccanica

**A.7 documento indicato per ogni rilievo**  [issue: -] [tipo: struttura]

Verifica   Ogni rilievo indica il documento del fascicolo da cui i dati provengono.
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

**A.9 limite di parole**  [issue: -] [tipo: struttura]

Verifica   Il deliverable resta entro il limite di parole.
Pass se    il conteggio delle parole non supera 2600
Fail se    il conteggio supera il limite.

*metadati non forniti al judge* - fonte: public/response_template.md; gravita: bassa; instradamento: verifica meccanica


## Sezione B - merito

Stato del fascicolo alla data di riferimento: preliminare sottoscritto e caparra versata; verifica tecnica e documentale in corso, con termine al 31 ottobre 2026; atto definitivo previsto entro il 20 gennaio 2027

**B.1 oggetto misto - composizione**  [issue: I-01] [tipo: presenza]

Verifica   Il deliverable afferma che la compravendita ha per oggetto sia un fabbricato sia terreni.
Pass se    compare l'affermazione che l'oggetto comprende il fabbricato e i terreni pertinenziali
Fail se    l'oggetto è trattato come unitario, oppure la composizione non è rilevata.
Indifferente  l'indicazione degli identificativi catastali.

*metadati non forniti al judge* - fonte: 06_contratto_preliminare.md, articolo 1; gravita: alta; instradamento: judge

**B.2 oggetto misto - adempimento per il fabbricato**  [issue: I-01] [tipo: presenza]

Verifica   Il deliverable afferma che per il fabbricato l'atto deve riportare, per dichiarazione dell'alienante, gli estremi del titolo edilizio.
Pass se    compare l'affermazione che l'atto deve riportare gli estremi del titolo edilizio del fabbricato
Fail se    l'adempimento relativo al fabbricato non è indicato, oppure è ricondotto all'obbligo di allegazione del certificato di destinazione urbanistica.
Indifferente  il richiamo alla confermabilità dell'atto.

*metadati non forniti al judge* - fonte: art. 46 del testo unico dell'edilizia; gravita: alta; instradamento: judge

**B.3 area pertinenziale - misura**  [issue: I-02] [tipo: valore]

Verifica   Il deliverable indica in 6.240 metri quadrati la superficie dell'area di pertinenza.
Pass se    compare la misura «6.240» riferita alla superficie fondiaria o all'area di pertinenza
Fail se    è indicata una misura diversa, oppure la misura non compare.
Indifferente  l'unità di misura usata.

*metadati non forniti al judge* - fonte: 06_contratto_preliminare.md, punto 1.2; gravita: alta; instradamento: verifica meccanica

**B.4 area pertinenziale - conseguenza**  [issue: I-02] [tipo: presenza]

Verifica   Il deliverable afferma che l'esclusione dall'obbligo di allegazione del certificato non opera perché la superficie dell'area di pertinenza supera la soglia.
Pass se    compare l'affermazione che l'esclusione non opera per il superamento della soglia di superficie
Fail se    è affermato che l'esclusione opera, oppure la verifica della soglia non compare.
Indifferente  l'indicazione del valore della soglia.

*metadati non forniti al judge* - fonte: art. 30, comma 2, del testo unico dell'edilizia; gravita: alta; instradamento: judge

**B.5 perimetro del certificato**  [issue: I-03] [tipo: presenza]

Verifica   Il deliverable afferma che il certificato esclude dal proprio perimetro i vincoli imposti da altri enti e i vincoli del piano paesaggistico non riportati sul piano regolatore.
Pass se    compare l'affermazione che il certificato contiene riserve che escludono quei vincoli
Fail se    le clausole di riserva non sono rilevate.
Indifferente  l'elenco degli enti richiamati dalla clausola.

*metadati non forniti al judge* - fonte: 01_certificato_destinazione_urbanistica.md, clausole di riserva; gravita: alta; instradamento: judge

**B.6 verifica autonoma sui vincoli**  [issue: I-03] [tipo: presenza]

Verifica   Il deliverable indica come necessaria una verifica autonoma sui vincoli non coperti dal certificato.
Pass se    fra le azioni compare la verifica autonoma sui vincoli esclusi dal certificato
Fail se    l'azione non è indicata.
Indifferente  l'indicazione degli enti presso cui svolgere la verifica.

*metadati non forniti al judge* - fonte: 01_certificato_destinazione_urbanistica.md; gravita: alta; instradamento: judge

**B.7 divieto di dedurre l'assenza di vincoli**  [issue: I-03] [tipo: assenza]

Verifica   Il deliverable non afferma che il compendio è libero da vincoli.
Pass se    Il deliverable non afferma che il compendio è libero da vincoli.
Fail se    è affermato che sul compendio non gravano vincoli, o che l'assenza di vincoli risulta dal certificato.
Indifferente  l'indicazione dei vincoli che il certificato riporta.

*metadati non forniti al judge* - fonte: 01_certificato_destinazione_urbanistica.md; gravita: alta; instradamento: judge

**B.8 soppalco non assentito - individuazione**  [issue: I-04] [tipo: presenza]

Verifica   Il deliverable afferma che il soppalco del corpo principale non è descritto in alcun titolo.
Pass se    compare l'affermazione che il soppalco del corpo principale non figura né nel permesso di costruire né nella segnalazione di variante
Fail se    il soppalco non assentito non è individuato, oppure è confuso con quello del corpo accessorio.
Indifferente  l'indicazione dell'altezza libera del soppalco.

*metadati non forniti al judge* - fonte: 04_rilievo_metrico.md, punti 2 e 4; gravita: alta; instradamento: judge

**B.9 soppalco assentito - distinzione**  [issue: I-04] [tipo: assenza]

Verifica   Il deliverable non tratta come non assentito il soppalco del corpo accessorio.
Pass se    Il deliverable non tratta come non assentito il soppalco del corpo accessorio.
Fail se    il soppalco del corpo accessorio è indicato fra le opere non assentite, o le superfici dei due soppalchi sono sommate in un unico scostamento.
Indifferente  la menzione del soppalco del corpo accessorio fra gli elementi verificati.

*metadati non forniti al judge* - fonte: 03_scia_variante.md; 04_rilievo_metrico.md, punto 4; gravita: alta; instradamento: judge

**B.10 termine di confronto dello scostamento**  [issue: I-05] [tipo: presenza]

Verifica   Il deliverable calcola lo scostamento rispetto alla superficie utile dichiarata nella segnalazione di variante.
Pass se    compare l'affermazione che il termine di confronto è la superficie dichiarata nella variante
Fail se    lo scostamento è calcolato rispetto alla superficie del permesso originario.
Indifferente  la menzione di entrambe le superfici a fini descrittivi.

*metadati non forniti al judge* - fonte: 03_scia_variante.md; 04_rilievo_metrico.md; gravita: alta; instradamento: judge

**B.11 superamento della tolleranza**  [issue: I-05] [tipo: presenza]

Verifica   Il deliverable afferma che lo scostamento supera la tolleranza del 2 per cento.
Pass se    compare l'affermazione che la tolleranza del 2 per cento è superata
Fail se    è affermato che lo scostamento rientra nella tolleranza, oppure il confronto non compare.
Indifferente  il richiamo alla natura di tolleranza costruttiva.

*metadati non forniti al judge* - fonte: art. 34-bis, comma 1, del testo unico dell'edilizia; gravita: alta; instradamento: judge

**B.12 inapplicabilità della graduazione**  [issue: I-05] [tipo: presenza]

Verifica   Il deliverable afferma che la graduazione delle soglie di tolleranza non si applica.
Pass se    compare l'affermazione che la graduazione non si applica, per la data dei lavori oppure per la dimensione dell'unità
Fail se    è applicata una soglia superiore al 2 per cento invocando la graduazione.
Indifferente  quale delle due ragioni è addotta, purché ne sia addotta almeno una.

*metadati non forniti al judge* - fonte: art. 34-bis, comma 1-bis, del testo unico dell'edilizia; gravita: alta; instradamento: judge

**B.13 qualificazione dello scostamento**  [issue: I-06] [tipo: qualificazione]

Verifica   Il deliverable qualifica lo scostamento come parziale difformità dal titolo.
Pass se    compare, riferita allo scostamento, una fra: «parziale difformità»; «difformità parziale»; «parzialmente difforme dal titolo»
Fail se    lo scostamento è qualificato come assenza di titolo, come totale difformità o come tolleranza.
Indifferente  il richiamo alla possibile qualificazione come variazione essenziale, se accompagnato dall'indicazione che dipende dalla legge regionale.

*metadati non forniti al judge* - fonte: 04_rilievo_metrico.md; art. 34 del testo unico dell'edilizia; gravita: alta; instradamento: judge

**B.14 binario dell'accertamento di conformità**  [issue: I-06] [tipo: presenza]

Verifica   Il deliverable afferma che l'accertamento di conformità applicabile è quello previsto per le parziali difformità e le variazioni essenziali.
Pass se    compare l'affermazione che si applica l'accertamento di conformità previsto per le parziali difformità
Fail se    è indicato l'accertamento previsto per l'assenza di titolo o per la totale difformità, oppure la sanatoria è trattata come istituto unitario.
Indifferente  il numero dell'articolo citato, purché il regime descritto sia quello corretto.

*metadati non forniti al judge* - fonte: artt. 36 e 36-bis del testo unico dell'edilizia; gravita: alta; instradamento: judge

**B.15 termine del procedimento**  [issue: I-07] [tipo: valore]

Verifica   Il deliverable indica in quarantacinque giorni il termine del procedimento applicabile.
Pass se    compare il termine «quarantacinque giorni» riferito al procedimento di accertamento di conformità applicabile
Fail se    è indicato un termine diverso, oppure il termine non compare.
Indifferente  l'indicazione del termine dell'altro binario a fini di confronto.

*metadati non forniti al judge* - fonte: art. 36-bis, comma 6, del testo unico dell'edilizia; gravita: alta; instradamento: verifica meccanica

**B.16 regime del silenzio**  [issue: I-07] [tipo: qualificazione]

Verifica   Il deliverable qualifica il silenzio nel binario applicabile come accoglimento.
Pass se    compare, riferito al silenzio, una fra: «si intende accolta»; «silenzio-accoglimento»; «silenzio assenso»
Fail se    il silenzio è qualificato come rifiuto.
Indifferente  il richiamo al regime opposto dell'altro binario a fini di confronto.

*metadati non forniti al judge* - fonte: art. 36-bis, comma 6, del testo unico dell'edilizia; gravita: alta; instradamento: judge

**B.17 doppia conformità asimmetrica**  [issue: I-08] [tipo: presenza]

Verifica   Il deliverable afferma che il presupposto richiede la conformità urbanistica al momento della domanda e la conformità ai requisiti edilizi al momento della realizzazione.
Pass se    compare l'affermazione che le due conformità sono riferite a due momenti diversi
Fail se    è richiesta la conformità piena a entrambe le date, oppure l'asimmetria non è rilevata.
Indifferente  l'ordine in cui i due profili sono esposti.

*metadati non forniti al judge* - fonte: art. 36-bis, comma 1, del testo unico dell'edilizia; gravita: alta; instradamento: judge

**B.18 criterio dell'oblazione**  [issue: I-09] [tipo: presenza]

Verifica   Il deliverable afferma che l'oblazione è pari al doppio del contributo di costruzione incrementato del 20 per cento per le parziali difformità.
Pass se    compare l'indicazione del doppio del contributo di costruzione con l'incremento del 20 per cento
Fail se    è indicato un criterio diverso, oppure il criterio non compare.
Indifferente  il richiamo all'ipotesi in cui l'incremento non si applica.

*metadati non forniti al judge* - fonte: art. 36-bis, comma 5, del testo unico dell'edilizia; gravita: media; instradamento: judge

**B.19 oblazione - dato mancante**  [issue: I-09] [tipo: presenza]

Verifica   Il deliverable afferma che il fascicolo non contiene il contributo di costruzione riferito alle sole opere in difformità.
Pass se    compare l'affermazione che manca il calcolo del contributo riferito alle opere in difformità
Fail se    l'oblazione è quantificata, oppure la lacuna non è dichiarata.
Indifferente  la richiesta di acquisire il calcolo dal Comune.

*metadati non forniti al judge* - fonte: 02_permesso_di_costruire.md; gravita: media; instradamento: judge

**B.20 oblazione - derivazione errata**  [issue: I-09] [tipo: assenza]

Verifica   Il deliverable non quantifica l'oblazione applicando il criterio all'intero contributo di costruzione dell'intervento.
Pass se    Il deliverable non quantifica l'oblazione applicando il criterio all'intero contributo di costruzione dell'intervento.
Fail se    l'oblazione è quantificata applicando il doppio e l'incremento al contributo complessivo versato per l'intero intervento.
Indifferente  la menzione dell'importo complessivo del contributo a fini descrittivi.

*metadati non forniti al judge* - fonte: 02_permesso_di_costruire.md; gravita: media; instradamento: judge

**B.21 parcheggio - misure a confronto**  [issue: I-10] [tipo: presenza]

Verifica   Il deliverable afferma che la superficie destinata a parcheggio è inferiore sia a quella prescritta dal permesso sia alla dotazione minima delle norme di attuazione.
Pass se    compare l'affermazione del doppio scostamento, rispetto al permesso e rispetto alla dotazione minima
Fail se    è rilevato un solo scostamento, oppure nessuno.
Indifferente  l'ordine dei due confronti.

*metadati non forniti al judge* - fonte: 04_rilievo_metrico.md; 02_permesso_di_costruire.md; 01_certificato_destinazione_urbanistica.md, allegato; gravita: alta; instradamento: judge

**B.22 parcheggio - base di calcolo**  [issue: I-10] [tipo: presenza]

Verifica   Il deliverable calcola la dotazione minima sul 20 per cento della superficie utile rilevata.
Pass se    compare l'indicazione che la dotazione minima è il 20 per cento della superficie utile rilevata
Fail se    la dotazione minima è calcolata sulla superficie utile assentita dal permesso.
Indifferente  l'esposizione anche del calcolo sulla superficie assentita a fini di confronto.

*metadati non forniti al judge* - fonte: 01_certificato_destinazione_urbanistica.md, allegato, art. 31.3; gravita: alta; instradamento: judge

**B.23 parcheggio - qualificazione**  [issue: I-10] [tipo: qualificazione]

Verifica   Il deliverable qualifica la carenza di parcheggio come violazione di una prescrizione del titolo.
Pass se    compare, riferita alla carenza, una fra: «violazione di prescrizione»; «prescrizione del titolo non rispettata»; «inosservanza di una prescrizione»
Fail se    la carenza è qualificata come scostamento dimensionale o come tolleranza.
Indifferente  il richiamo alla scelta della proprietà di mantenere l'area a verde.

*metadati non forniti al judge* - fonte: 02_permesso_di_costruire.md, punto 3.6; gravita: alta; instradamento: judge

**B.24 destinazione d'uso - categorie funzionali**  [issue: I-11] [tipo: presenza]

Verifica   Il deliverable afferma che la destinazione assentita e quella voluta appartengono a categorie funzionali diverse.
Pass se    compare l'affermazione che si tratta di categorie funzionali diverse
Fail se    le due destinazioni sono trattate come appartenenti alla stessa categoria.
Indifferente  l'indicazione delle denominazioni delle categorie.

*metadati non forniti al judge* - fonte: 02_permesso_di_costruire.md, punto 2; art. 23-ter del testo unico dell'edilizia; gravita: alta; instradamento: judge

**B.25 destinazione d'uso - mutamento rilevante**  [issue: I-11] [tipo: qualificazione]

Verifica   Il deliverable qualifica il mutamento come urbanisticamente rilevante.
Pass se    compare, riferito al mutamento, una fra: «urbanisticamente rilevante»; «mutamento rilevante»; «rilevante ai fini urbanistici»
Fail se    il mutamento è qualificato come irrilevante o come consentito senza titolo.
Indifferente  il richiamo alla possibilità di eseguirlo senza opere.

*metadati non forniti al judge* - fonte: art. 23-ter del testo unico dell'edilizia; gravita: alta; instradamento: judge

**B.26 destinazione d'uso - sospensione motivata**  [issue: I-11] [tipo: presenza]

Verifica   Il deliverable afferma che la conclusione sull'ammissibilità del mutamento non è raggiungibile sul fascicolo e indica che mancano lo strumento comunale di programmazione commerciale e la legge regionale.
Pass se    compare l'affermazione che la conclusione resta sospesa e l'indicazione dei due documenti mancanti
Fail se    è formulata una conclusione sull'ammissibilità, oppure è dichiarata l'impossibilità di concludere senza indicare che cosa manca.
Indifferente  l'indicazione di uno solo dei due documenti, purché sia indicato lo strumento di programmazione commerciale.

*metadati non forniti al judge* - fonte: 01_certificato_destinazione_urbanistica.md, allegato; 04_rilievo_metrico.md, punti 5.2 e 5.3; gravita: alta; instradamento: judge

**B.27 agibilità - tardività**  [issue: I-12] [tipo: presenza]

Verifica   Il deliverable afferma che la segnalazione di agibilità è stata presentata oltre il termine di quindici giorni dall'ultimazione dei lavori di finitura.
Pass se    compare l'affermazione che la presentazione è avvenuta oltre il termine di quindici giorni
Fail se    la presentazione è indicata come tempestiva, oppure il confronto non compare.
Indifferente  il numero dei giorni di ritardo.

*metadati non forniti al judge* - fonte: 05_segnalazione_certificata_agibilita.md; 02_permesso_di_costruire.md, annotazioni; gravita: media; instradamento: judge

**B.28 agibilità - conseguenza**  [issue: I-12] [tipo: qualificazione]

Verifica   Il deliverable qualifica la conseguenza della tardività come sanzione amministrativa pecuniaria.
Pass se    compare, riferita alla tardività, una fra: «sanzione amministrativa pecuniaria»; «sanzione pecuniaria»; «sanzione amministrativa»
Fail se    la conseguenza è indicata come inefficacia della segnalazione o come illegittimità dell'utilizzo.
Indifferente  l'indicazione dell'intervallo dell'importo.

*metadati non forniti al judge* - fonte: art. 24, comma 3, del testo unico dell'edilizia; gravita: media; instradamento: judge

**B.29 agibilità - divieto di conclusione eccedente**  [issue: I-12] [tipo: assenza]

Verifica   Il deliverable non afferma che l'utilizzo dell'immobile è illegittimo.
Pass se    Il deliverable non afferma che l'utilizzo dell'immobile è illegittimo.
Fail se    è affermato che l'immobile non è utilizzabile, o che l'utilizzo in corso è illegittimo.
Indifferente  l'indicazione che l'utilizzo può iniziare dalla data di presentazione.

*metadati non forniti al judge* - fonte: art. 24, comma 6, del testo unico dell'edilizia; gravita: alta; instradamento: judge

**B.30 rinvio a disposizione abrogata - rilevazione**  [issue: I-13] [tipo: presenza]

Verifica   Il deliverable afferma che la segnalazione di agibilità rinvia a una disposizione abrogata.
Pass se    compare l'affermazione che la disposizione richiamata nell'intestazione della segnalazione è abrogata
Fail se    il rinvio non è rilevato.
Indifferente  l'indicazione dell'atto che ha disposto l'abrogazione.

*metadati non forniti al judge* - fonte: 05_segnalazione_certificata_agibilita.md, intestazione; gravita: media; instradamento: judge

**B.31 rinvio a disposizione abrogata - divieto di sovra-reazione**  [issue: I-13] [tipo: assenza]

Verifica   Il deliverable non fa derivare dal rinvio errato l'inefficacia della segnalazione.
Pass se    Il deliverable non fa derivare dal rinvio errato l'inefficacia della segnalazione.
Fail se    è affermato che la segnalazione è nulla, inefficace o da ripresentare per effetto del rinvio alla disposizione abrogata.
Indifferente  la proposta di rettificare l'intestazione.

*metadati non forniti al judge* - fonte: art. 24 del testo unico dell'edilizia; gravita: alta; instradamento: judge

**B.32 garanzia contrattuale smentita**  [issue: I-14] [tipo: presenza]

Verifica   Il deliverable afferma che la dichiarazione della venditrice sulla conformità ai titoli è smentita dal rilievo metrico.
Pass se    compare l'affermazione che la garanzia sulla conformità è smentita dal rilievo
Fail se    la dichiarazione della venditrice è riportata come stato accertato dell'immobile, oppure la difformità è rilevata senza collegarla alla garanzia.
Indifferente  il richiamo alla dichiarazione sull'assenza di atti di accertamento.

*metadati non forniti al judge* - fonte: 06_contratto_preliminare.md, punti 4.2 e 4.4; gravita: alta; instradamento: judge

**B.33 valutazioni della relazione asseverata**  [issue: I-14] [tipo: qualificazione]

Verifica   Il deliverable qualifica come valutazioni di parte le considerazioni della relazione asseverata sull'irrilevanza del soppalco interno e sulla dotazione a verde.
Pass se    compare, riferita a quelle considerazioni, una fra: «valutazione di parte»; «giudizio del tecnico della venditrice»; «non è un fatto accertato»
Fail se    le considerazioni sono riportate come asseverazioni o come fatti.
Indifferente  il richiamo alla qualifica del tecnico come progettista e direttore dei lavori.

*metadati non forniti al judge* - fonte: 07_relazione_tecnica_asseverata.md, punto 4; gravita: alta; instradamento: judge

**B.34 collocazione nelle condizioni - difformità regolarizzabili**  [issue: I-15] [tipo: presenza]

Verifica   Il deliverable colloca lo scostamento di superficie utile fra le difformità per cui il preliminare prevede la rinegoziazione del prezzo.
Pass se    compare la collocazione dello scostamento fra le difformità regolarizzabili con rinegoziazione del prezzo
Fail se    lo scostamento è collocato fra le difformità non regolarizzabili, oppure la collocazione non è indicata.
Indifferente  l'indicazione dell'importo su cui rinegoziare.

*metadati non forniti al judge* - fonte: 06_contratto_preliminare.md, punto 5.2; gravita: alta; instradamento: judge

**B.35 collocazione nelle condizioni - punto sospeso**  [issue: I-15] [tipo: presenza]

Verifica   Il deliverable afferma che la collocazione del mutamento di destinazione d'uso fra le due categorie del preliminare non è determinabile sul fascicolo.
Pass se    compare l'affermazione che la collocazione del mutamento di destinazione d'uso resta sospesa
Fail se    il mutamento di destinazione è collocato in una delle due categorie, oppure il punto non è trattato.
Indifferente  l'indicazione del termine del 31 ottobre 2026 per la verifica.

*metadati non forniti al judge* - fonte: 06_contratto_preliminare.md, punti 5.1, 5.2 e 5.3; gravita: alta; instradamento: judge

**B.36 sovra-segnalazione - validità del certificato**  [issue: N-01] [tipo: assenza]

Verifica   Il deliverable non indica la necessità di un nuovo certificato di destinazione urbanistica per intervenuta scadenza.
Pass se    Il deliverable non indica la necessità di un nuovo certificato di destinazione urbanistica per intervenuta scadenza.
Fail se    è indicata la scadenza del certificato di destinazione urbanistica come rilievo o come adempimento da compiere prima dell'atto definitivo.
Indifferente  l'osservazione che la validità è subordinata alla dichiarazione dell'alienante sull'assenza di modificazioni degli strumenti urbanistici.

*metadati non forniti al judge* - fonte: 01_certificato_destinazione_urbanistica.md; 06_contratto_preliminare.md, punto 3.1; gravita: media; instradamento: judge

**B.37 sovra-segnalazione - altezza**  [issue: N-02] [tipo: assenza]

Verifica   Il deliverable non indica l'altezza rilevata fra gli scostamenti non assentiti.
Pass se    Il deliverable non indica l'altezza rilevata fra gli scostamenti non assentiti.
Fail se    l'altezza rilevata di 7,24 metri è indicata come difformità rispetto al titolo.
Indifferente  la menzione dell'altezza fra gli elementi verificati e corrispondenti.

*metadati non forniti al judge* - fonte: 03_scia_variante.md; 04_rilievo_metrico.md; gravita: media; instradamento: judge

**B.38 sovra-segnalazione - decadenza del titolo**  [issue: N-03] [tipo: assenza]

Verifica   Il deliverable non segnala un rischio di decadenza del permesso di costruire.
Pass se    Il deliverable non segnala un rischio di decadenza del permesso di costruire.
Fail se    è indicata la decadenza del permesso di costruire fra i rilievi, o è invocata una proroga dei termini.
Indifferente  la menzione delle date di inizio e ultimazione fra gli elementi verificati.

*metadati non forniti al judge* - fonte: 02_permesso_di_costruire.md, annotazioni; gravita: media; instradamento: judge

**B.39 sovra-segnalazione - clausola di non producibilità**  [issue: N-04] [tipo: assenza]

Verifica   Il deliverable non presenta come limite la clausola di non producibilità agli organi della pubblica amministrazione.
Pass se    Il deliverable non presenta come limite la clausola di non producibilità agli organi della pubblica amministrazione.
Fail se    la clausola di non producibilità agli organi della pubblica amministrazione è indicata come limite all'utilizzabilità del certificato nell'atto.
Indifferente  la menzione della clausola fra le formule del certificato.

*metadati non forniti al judge* - fonte: 01_certificato_destinazione_urbanistica.md; gravita: bassa; instradamento: judge

**B.40 simmetria del controllo - opere assentite**  [issue: -] [tipo: assenza]

Verifica   Il deliverable non attribuisce alle opere assentite dalla segnalazione di variante lo stesso trattamento delle opere non assentite.
Pass se    Il deliverable non attribuisce alle opere assentite dalla segnalazione di variante lo stesso trattamento delle opere non assentite.
Fail se    le opere descritte nella segnalazione di variante sono elencate fra quelle prive di titolo.
Indifferente  la menzione della variante fra i titoli che disciplinano l'immobile.

*metadati non forniti al judge* - fonte: 03_scia_variante.md; gravita: media; instradamento: judge

**B.41 presunzione dell'esito - accertamento di conformità**  [issue: -] [tipo: assenza]

Verifica   Il deliverable non presenta come acquisito l'esito dell'accertamento di conformità.
Pass se    Il deliverable non presenta come acquisito l'esito dell'accertamento di conformità.
Fail se    è affermato che la domanda di accertamento di conformità sarà accolta, o che la difformità è sanabile con certezza.
Indifferente  l'indicazione dei presupposti da verificare per l'accoglimento.

*metadati non forniti al judge* - fonte: private/challenge_map.json, dati mancanti; gravita: alta; instradamento: judge


## Sezione C - date e valori calcolati

**C.1 superficie utile rilevata**  [issue: I-04] [tipo: valore]

Verifica   Il deliverable indica in 1.958 metri quadrati la superficie utile rilevata.
Pass se    compare la misura «1.958» riferita alla superficie utile rilevata
Fail se    è indicata una misura diversa, oppure la misura non compare.
Indifferente  l'unità di misura usata.

*metadati non forniti al judge* - fonte: 04_rilievo_metrico.md, punto 2; gravita: alta; instradamento: verifica meccanica

**C.2 scostamento non assentito**  [issue: I-05] [tipo: valore]

Verifica   Il deliverable indica in 56 metri quadrati lo scostamento non assentito.
Pass se    compare la misura «56» riferita allo scostamento non assentito di superficie utile
Fail se    è indicata una misura diversa, oppure lo scostamento non compare.
Indifferente  l'unità di misura usata.

*metadati non forniti al judge* - fonte: 04_rilievo_metrico.md; gravita: alta; instradamento: verifica meccanica

**C.3 scostamento in percentuale**  [issue: I-05] [tipo: valore]

Verifica   Il deliverable indica nel 2,94 per cento lo scostamento percentuale.
Pass se    compare la percentuale «2,94» riferita allo scostamento
Fail se    è indicata una percentuale diversa, oppure la percentuale non compare.
Indifferente  il numero di decimali usato.

*metadati non forniti al judge* - fonte: 04_rilievo_metrico.md e 03_scia_variante.md; gravita: alta; instradamento: verifica meccanica

**C.4 derivazione errata sulla base di calcolo dello scostamento**  [issue: I-05] [tipo: assenza]

Verifica   Il deliverable non calcola lo scostamento percentuale sulla superficie utile del permesso originario.
Pass se    Il deliverable non calcola lo scostamento percentuale sulla superficie utile del permesso originario.
Fail se    lo scostamento percentuale è calcolato dividendo la differenza rispetto alla superficie del permesso originario, oppure è indicato come «6,41».
Indifferente  la menzione della superficie del permesso originario a fini descrittivi.

*metadati non forniti al judge* - fonte: 02_permesso_di_costruire.md e 03_scia_variante.md; gravita: alta; instradamento: judge

**C.5 dotazione minima di parcheggio**  [issue: I-10] [tipo: valore]

Verifica   Il deliverable indica in 391,6 metri quadrati la dotazione minima di parcheggio.
Pass se    compare la misura «391,6» riferita alla dotazione minima di parcheggio
Fail se    è indicata una misura diversa, oppure la dotazione minima non compare.
Indifferente  l'arrotondamento del valore.

*metadati non forniti al judge* - fonte: 01_certificato_destinazione_urbanistica.md, allegato, art. 31.3; gravita: alta; instradamento: verifica meccanica

**C.6 derivazione errata sulla base di calcolo del parcheggio**  [issue: I-10] [tipo: assenza]

Verifica   Il deliverable non calcola la dotazione minima di parcheggio sulla superficie utile assentita dal permesso.
Pass se    Il deliverable non calcola la dotazione minima di parcheggio sulla superficie utile assentita dal permesso.
Fail se    la dotazione minima è indicata come «368» metri quadrati o è calcolata sul 20 per cento della superficie utile assentita dal permesso.
Indifferente  la menzione della superficie assentita a fini descrittivi.

*metadati non forniti al judge* - fonte: 02_permesso_di_costruire.md; gravita: media; instradamento: judge

**C.7 termine per la verifica contrattuale**  [issue: I-15] [tipo: valore]

Verifica   Il deliverable indica il 31 ottobre 2026 come termine della verifica prevista dal preliminare.
Pass se    compare la data «31 ottobre 2026» riferita al termine della verifica
Fail se    è indicata una data diversa, oppure la data non compare.
Indifferente  il richiamo alla data dell'atto definitivo.

*metadati non forniti al judge* - fonte: 06_contratto_preliminare.md, punto 5.1; gravita: media; instradamento: verifica meccanica

**C.8 data dell'atto definitivo**  [issue: N-01] [tipo: valore]

Verifica   Il deliverable indica il 20 gennaio 2027 come termine per la stipulazione dell'atto definitivo.
Pass se    compare la data «20 gennaio 2027» riferita all'atto definitivo
Fail se    è indicata una data diversa, oppure la data non compare.
Indifferente  il richiamo alla scadenza della validità del certificato.

*metadati non forniti al judge* - fonte: 06_contratto_preliminare.md, punto 3.1; gravita: media; instradamento: verifica meccanica
