# WF2-096 - Criteri atomizzati

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
Pass se    è presente construction_deadline_audit.md
Fail se    il file manca oppure il nome diverge.

*metadati non forniti al judge* - fonte: public/response_template.md; gravita: media; instradamento: verifica meccanica

**A.2 sezioni dell'audit**  [issue: -] [tipo: struttura]

Verifica   Il deliverable contiene le sezioni indicate, nell'ordine indicato.
Pass se    le intestazioni compaiono tutte e nella sequenza del response_template
Fail se    manca un'intestazione oppure l'ordine differisce.
Indifferente  la formulazione delle intestazioni oltre le prime ventidue battute.

*metadati non forniti al judge* - fonte: public/response_template.md; gravita: media; instradamento: verifica meccanica

**A.3 data di riferimento**  [issue: -] [tipo: valore]

Verifica   Il deliverable assume come data di riferimento il 2 dicembre 2026.
Pass se    compare «2 dicembre 2026» come data alla quale l'audit è riferito
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

**A.9 limite di parole**  [issue: -] [tipo: struttura]

Verifica   Il deliverable resta entro il limite di parole.
Pass se    il conteggio delle parole non supera 2500
Fail se    il conteggio supera il limite.

*metadati non forniti al judge* - fonte: public/response_template.md; gravita: bassa; instradamento: verifica meccanica


## Sezione B - merito

Stato del fascicolo alla data di riferimento: cantiere aperto; lavori iniziati l'11 maggio 2026, sospesi dal 15 giugno al 30 luglio 2026 e ripresi; nessuna istanza di proroga presentata; variante proposta dal direttore dei lavori e non ancora presentata

**B.1 termine di inizio - stato**  [issue: I-01] [tipo: presenza]

Verifica   Il deliverable afferma che il termine di inizio dei lavori è stato rispettato.
Pass se    compare l'affermazione che il termine di inizio dei lavori è rispettato
Fail se    il termine di inizio è presentato come pendente o come scaduto.
Indifferente  il richiamo alla data della comunicazione di inizio.

*metadati non forniti al judge* - fonte: 03_comunicazione_inizio_lavori.md; gravita: media; instradamento: judge

**B.2 dies a quo del termine di ultimazione**  [issue: I-02] [tipo: attribuzione]

Verifica   Il deliverable riconduce la decorrenza del termine di ultimazione all'inizio dei lavori.
Pass se    compare l'affermazione che il termine di ultimazione decorre dall'inizio dei lavori
Fail se    la decorrenza è ricondotta al rilascio del titolo o ad altro evento.
Indifferente  il richiamo alla prescrizione del titolo che riproduce la regola.

*metadati non forniti al judge* - fonte: 01_permesso_di_costruire.md, punto 3.1; art. 15, comma 2, del testo unico dell'edilizia; gravita: alta; instradamento: judge

**B.3 sospensione - assenza di effetto automatico**  [issue: I-03] [tipo: presenza]

Verifica   Il deliverable afferma che la sospensione dei lavori non proroga automaticamente il termine di ultimazione.
Pass se    compare l'affermazione che il termine non si allunga automaticamente per effetto della sospensione
Fail se    è affermato che il termine si è allungato della durata della sospensione senza necessità di istanza.
Indifferente  il richiamo alla durata dell'interruzione.

*metadati non forniti al judge* - fonte: art. 15, comma 2, del testo unico dell'edilizia; gravita: alta; instradamento: judge

**B.4 sospensione - proroga comunque accordata**  [issue: I-03] [tipo: presenza]

Verifica   Il deliverable afferma che nel caso di iniziative dell'amministrazione rivelatesi infondate la proroga è comunque accordata.
Pass se    compare l'affermazione che la proroga è comunque accordata in quel caso
Fail se    la proroga è presentata come discrezionale anche in presenza di quel presupposto, oppure il punto non è trattato.
Indifferente  il richiamo alla proroga discrezionale prevista per altri casi.

*metadati non forniti al judge* - fonte: art. 15, comma 2-bis, del testo unico dell'edilizia; gravita: alta; instradamento: judge

**B.5 presupposto - accertamento della revoca**  [issue: I-04] [tipo: attribuzione]

Verifica   Il deliverable riconduce il presupposto della proroga all'accertamento contenuto nella determinazione di revoca.
Pass se    il presupposto è ricondotto alla determinazione che accerta l'insussistenza della difformità
Fail se    il presupposto è ricondotto alla sola esistenza dell'ordinanza di sospensione.
Indifferente  il richiamo alle distanze accertate nel sopralluogo congiunto.

*metadati non forniti al judge* - fonte: 05_provvedimento_revoca.md, punti 1 e 2; gravita: alta; instradamento: judge

**B.6 momento dell'istanza di proroga**  [issue: I-05] [tipo: presenza]

Verifica   Il deliverable afferma che la proroga va richiesta anteriormente alla scadenza del termine di ultimazione.
Pass se    compare l'affermazione che l'istanza va presentata prima della scadenza del termine
Fail se    è affermato che la proroga può essere richiesta anche dopo la scadenza, oppure il punto non è trattato.
Indifferente  l'indicazione del momento in cui presentarla.

*metadati non forniti al judge* - fonte: art. 15, comma 2, del testo unico dell'edilizia; gravita: alta; instradamento: judge

**B.7 assenza di istanza alla data di riferimento**  [issue: I-05] [tipo: presenza]

Verifica   Il deliverable afferma che alla data di riferimento nessuna istanza di proroga risulta presentata.
Pass se    compare l'affermazione che nessuna istanza di proroga è stata presentata
Fail se    è affermato che la proroga è stata richiesta o ottenuta.
Indifferente  il richiamo alla nota della direzione tecnica.

*metadati non forniti al judge* - fonte: 06_cronoprogramma_e_stato_avanzamento.md, punto 5; gravita: alta; instradamento: judge

**B.8 iniziativa da assumere sulla proroga**  [issue: I-05] [tipo: presenza]

Verifica   Il deliverable indica la presentazione dell'istanza di proroga fra le azioni da compiere.
Pass se    fra le azioni compare la presentazione dell'istanza di proroga
Fail se    l'azione non è indicata.
Indifferente  il momento proposto per la presentazione.

*metadati non forniti al judge* - fonte: art. 15, commi 2 e 2-bis, del testo unico dell'edilizia; gravita: alta; instradamento: judge

**B.9 durata dell'interruzione**  [issue: I-06] [tipo: presenza]

Verifica   Il deliverable afferma che l'interruzione è durata dal 15 giugno al 30 luglio 2026.
Pass se    compare l'indicazione dell'intervallo fra le due date come durata dell'interruzione
Fail se    è indicato un intervallo diverso, oppure la durata non compare.
Indifferente  il richiamo alla data di notificazione dei due provvedimenti.

*metadati non forniti al judge* - fonte: 04_ordinanza_sospensione_lavori.md; 05_provvedimento_revoca.md; gravita: media; instradamento: judge

**B.10 effetto sul cronoprogramma**  [issue: I-07] [tipo: presenza]

Verifica   Il deliverable afferma che l'ultimazione programmata resta anteriore al termine di ultimazione del permesso.
Pass se    compare l'affermazione che la nuova data di programma precede il termine di legge
Fail se    è affermato che lo slittamento espone il titolo al rischio di decadenza, oppure il confronto non compare.
Indifferente  l'indicazione del margine residuo.

*metadati non forniti al judge* - fonte: 06_cronoprogramma_e_stato_avanzamento.md, punti 1 e 4; gravita: media; instradamento: judge

**B.11 riprogrammazione non comunicata - qualificazione**  [issue: I-08] [tipo: qualificazione]

Verifica   Il deliverable qualifica la mancata comunicazione della riprogrammazione come non imposta dal titolo.
Pass se    compare, riferita alla comunicazione della riprogrammazione, una fra: «non è imposta dal titolo»; «non è un adempimento prescritto»; «non costituisce violazione di prescrizione»
Fail se    la mancata comunicazione è indicata come violazione di una prescrizione del titolo.
Indifferente  la proposta di comunicarla comunque.

*metadati non forniti al judge* - fonte: 01_permesso_di_costruire.md, prescrizioni; 06_cronoprogramma_e_stato_avanzamento.md, punto 5; gravita: media; instradamento: judge

**B.12 riprogrammazione non comunicata - conseguenza pratica**  [issue: I-08] [tipo: presenza]

Verifica   Il deliverable indica l'opportunità di portare l'interruzione a conoscenza dell'amministrazione ai fini dell'istanza di proroga.
Pass se    fra le azioni compare la comunicazione dell'interruzione o della riprogrammazione a sostegno dell'istanza di proroga
Fail se    l'azione non è indicata.
Indifferente  la forma proposta per la comunicazione.

*metadati non forniti al judge* - fonte: 06_cronoprogramma_e_stato_avanzamento.md, punto 5; gravita: media; instradamento: judge

**B.13 variante - incremento rilevato**  [issue: I-09] [tipo: presenza]

Verifica   Il deliverable afferma che la variante incrementa la superficie di solaio.
Pass se    compare l'affermazione che la variante comporta un incremento della superficie di solaio
Fail se    l'incremento non è rilevato, oppure è affermato che la variante non incide su alcun parametro.
Indifferente  il richiamo alle grandezze che restano invariate.

*metadati non forniti al judge* - fonte: 07_relazione_direzione_lavori_variante.md, punto 3; gravita: alta; instradamento: judge

**B.14 variante - grandezze invariate**  [issue: I-09] [tipo: presenza]

Verifica   Il deliverable afferma che volume fuori terra, superficie coperta, altezza e numero dei piani restano invariati.
Pass se    compare l'affermazione che quelle grandezze restano invariate
Fail se    è affermato che la variante incide anche su volume o sagoma.
Indifferente  l'ordine in cui le grandezze sono elencate.

*metadati non forniti al judge* - fonte: 07_relazione_direzione_lavori_variante.md, punto 3; gravita: media; instradamento: judge

**B.15 variante - condizione di essenzialità**  [issue: I-10] [tipo: presenza]

Verifica   Il deliverable afferma che l'aumento consistente della superficie di solaio è una delle condizioni in cui può ricorrere la variazione essenziale.
Pass se    compare l'affermazione che l'aumento della superficie di solaio è fra le condizioni di essenzialità
Fail se    l'incremento è trattato come irrilevante ai fini dell'essenzialità.
Indifferente  il richiamo al carattere tassativo dell'elenco.

*metadati non forniti al judge* - fonte: art. 32 del testo unico dell'edilizia; gravita: alta; instradamento: judge

**B.16 variante - sospensione della qualificazione**  [issue: I-10] [tipo: presenza]

Verifica   Il deliverable afferma che la determinazione delle variazioni essenziali è rimessa alla legge regionale e indica che il fascicolo non la contiene.
Pass se    compare l'affermazione che la qualificazione dipende dalla legge regionale e l'indicazione che essa manca
Fail se    la variante è qualificata come essenziale o come non essenziale, oppure è dichiarata l'impossibilità di concludere senza indicare che cosa manca.
Indifferente  l'esposizione della percentuale di incremento.

*metadati non forniti al judge* - fonte: art. 32 del testo unico dell'edilizia; 07_relazione_direzione_lavori_variante.md, punto 5.1; gravita: alta; instradamento: judge

**B.17 variante - percorso condizionato**  [issue: I-11] [tipo: presenza]

Verifica   Il deliverable espone entrambi i percorsi, quello praticabile con segnalazione certificata se la variante non è essenziale e quello che richiede un titolo se lo è.
Pass se    compaiono entrambi i percorsi, ciascuno condizionato alla qualificazione
Fail se    è indicato un solo percorso come praticabile.
Indifferente  l'ordine in cui i due percorsi sono esposti.

*metadati non forniti al judge* - fonte: art. 22, commi 2 e 2-bis, del testo unico dell'edilizia; gravita: alta; instradamento: judge

**B.18 variante - condizione dell'assenso paesaggistico**  [issue: I-11] [tipo: presenza]

Verifica   Il deliverable afferma che la segnalazione certificata per le varianti non essenziali presuppone l'acquisizione degli atti di assenso prescritti dalla normativa sui vincoli paesaggistici.
Pass se    compare l'affermazione che l'assenso paesaggistico va acquisito prima dell'attuazione della variante
Fail se    la condizione non è indicata.
Indifferente  il richiamo alla comunicazione a fine lavori con attestazione del professionista.

*metadati non forniti al judge* - fonte: art. 22, comma 2-bis, del testo unico dell'edilizia; gravita: alta; instradamento: judge

**B.19 assenso paesaggistico - oggetto della verifica**  [issue: I-12] [tipo: presenza]

Verifica   Il deliverable individua nella modifica dei materiali del fronte est e nell'arretramento della facciata sud gli elementi che richiedono la verifica paesaggistica.
Pass se    compaiono entrambi gli elementi come oggetto della verifica
Fail se    nessuno dei due elementi è individuato, oppure la verifica è riferita ad altro.
Indifferente  l'indicazione di uno solo dei due elementi, purché sia la modifica dei materiali.

*metadati non forniti al judge* - fonte: 02_autorizzazione_paesaggistica.md, prescrizioni 1 e 2; 07_relazione_direzione_lavori_variante.md, punti 2.3 e 2.4; gravita: alta; instradamento: judge

**B.20 assenso paesaggistico - carattere preventivo**  [issue: I-12] [tipo: presenza]

Verifica   Il deliverable afferma che l'assenso paesaggistico va acquisito prima dell'esecuzione, perché l'autorizzazione non può essere rilasciata in sanatoria dopo la realizzazione anche parziale degli interventi fuori dalle ipotesi tassative.
Pass se    compare l'affermazione del carattere preventivo dell'assenso e del divieto di rilascio in sanatoria
Fail se    l'assenso è collocato dopo l'esecuzione, oppure il divieto non è menzionato.
Indifferente  il richiamo alle ipotesi tassative di accertamento di compatibilità.

*metadati non forniti al judge* - fonte: art. 146, comma 4, del codice dei beni culturali e del paesaggio; gravita: alta; instradamento: judge

**B.21 momento di presentazione della variante**  [issue: I-13] [tipo: presenza]

Verifica   Il deliverable afferma che la variante realizzabile con segnalazione certificata va presentata prima della dichiarazione di ultimazione dei lavori.
Pass se    compare l'affermazione che la presentazione precede la dichiarazione di ultimazione dei lavori
Fail se    la presentazione è collocata dopo l'ultimazione, oppure il vincolo temporale non è indicato.
Indifferente  la collocazione della presentazione in una fase determinata del cronoprogramma.

*metadati non forniti al judge* - fonte: art. 22, comma 2, del testo unico dell'edilizia; gravita: media; instradamento: judge

**B.22 parte non ultimata**  [issue: I-14] [tipo: presenza]

Verifica   Il deliverable afferma che, alla scadenza del termine, la parte non eseguita richiede un nuovo permesso salvo che rientri fra le opere realizzabili con segnalazione certificata.
Pass se    compare l'affermazione che il nuovo titolo riguarda la parte non eseguita, con la riserva delle opere realizzabili con segnalazione
Fail se    è affermato che la scadenza travolge l'intero titolo, oppure la riserva non è indicata.
Indifferente  il richiamo alla decadenza di diritto per la parte non eseguita.

*metadati non forniti al judge* - fonte: art. 15, comma 3, del testo unico dell'edilizia; gravita: media; instradamento: judge

**B.23 ricalcolo del contributo**  [issue: I-14] [tipo: presenza]

Verifica   Il deliverable afferma che in caso di nuovo permesso si procede ove necessario al ricalcolo del contributo di costruzione.
Pass se    compare l'affermazione che il contributo di costruzione può essere ricalcolato
Fail se    è affermato che il contributo già versato copre in ogni caso l'intervento, oppure il punto non è trattato.
Indifferente  l'indicazione dell'importo già versato.

*metadati non forniti al judge* - fonte: art. 15, comma 3, del testo unico dell'edilizia; gravita: media; instradamento: judge

**B.24 agibilità - termine**  [issue: I-15] [tipo: presenza]

Verifica   Il deliverable afferma che la segnalazione certificata di agibilità va presentata entro quindici giorni dall'ultimazione dei lavori di finitura.
Pass se    compare l'indicazione del termine di quindici giorni dall'ultimazione dei lavori di finitura
Fail se    è indicato un termine diverso, oppure il termine non compare.
Indifferente  il richiamo agli allegati richiesti.

*metadati non forniti al judge* - fonte: art. 24, comma 2, del testo unico dell'edilizia; gravita: media; instradamento: judge

**B.25 agibilità parziale**  [issue: I-15] [tipo: presenza]

Verifica   Il deliverable afferma che è ammessa l'agibilità parziale per singoli edifici o porzioni funzionalmente autonome e per singole unità immobiliari.
Pass se    compare l'affermazione che l'agibilità parziale è ammessa
Fail se    l'agibilità parziale è esclusa, oppure il punto non è trattato.
Indifferente  l'indicazione delle condizioni previste.

*metadati non forniti al judge* - fonte: art. 24, comma 4, del testo unico dell'edilizia; gravita: media; instradamento: judge

**B.26 sovra-segnalazione - autorizzazione paesaggistica**  [issue: N-01] [tipo: assenza]

Verifica   Il deliverable non indica la scadenza dell'autorizzazione paesaggistica fra i termini a rischio.
Pass se    Il deliverable non indica la scadenza dell'autorizzazione paesaggistica fra i termini a rischio.
Fail se    è affermato che l'autorizzazione paesaggistica scade prima della fine dei lavori, o che va rinnovata prima dell'ultimazione.
Indifferente  la menzione dell'autorizzazione fra i titoli verificati e in corso di efficacia.

*metadati non forniti al judge* - fonte: 02_autorizzazione_paesaggistica.md, avvertenze; gravita: alta; instradamento: judge

**B.27 sovra-segnalazione - impugnazione dell'ordinanza**  [issue: N-02] [tipo: assenza]

Verifica   Il deliverable non indica l'impugnazione dell'ordinanza di sospensione fra le azioni.
Pass se    Il deliverable non indica l'impugnazione dell'ordinanza di sospensione fra le azioni.
Fail se    è indicata l'impugnazione dell'ordinanza o il calcolo del termine per il ricorso al giudice amministrativo.
Indifferente  la menzione dell'ordinanza fra gli atti che hanno esaurito i propri effetti.

*metadati non forniti al judge* - fonte: 05_provvedimento_revoca.md; gravita: media; instradamento: judge

**B.28 sovra-segnalazione - proroga straordinaria**  [issue: N-03] [tipo: assenza]

Verifica   Il deliverable non invoca la proroga straordinaria di quarantotto mesi.
Pass se    Il deliverable non invoca la proroga straordinaria di quarantotto mesi.
Fail se    la proroga straordinaria di quarantotto mesi è indicata come applicabile al permesso.
Indifferente  la menzione della proroga straordinaria per escluderne l'applicabilità in ragione della data di rilascio del titolo.

*metadati non forniti al judge* - fonte: 01_permesso_di_costruire.md, data di rilascio; gravita: alta; instradamento: judge

**B.29 sovra-segnalazione - contributo di costruzione**  [issue: N-04] [tipo: assenza]

Verifica   Il deliverable non indica il versamento del contributo di costruzione fra gli adempimenti da compiere.
Pass se    Il deliverable non indica il versamento del contributo di costruzione fra gli adempimenti da compiere.
Fail se    il versamento del contributo di costruzione è indicato fra gli adempimenti mancanti.
Indifferente  il richiamo al possibile ricalcolo in caso di nuovo permesso.

*metadati non forniti al judge* - fonte: 01_permesso_di_costruire.md, quietanza richiamata in premessa; gravita: bassa; instradamento: judge

**B.30 simmetria del controllo - responsabilità dell'interruzione**  [issue: -] [tipo: assenza]

Verifica   Il deliverable non attribuisce a Pratomagno la responsabilità dell'interruzione.
Pass se    Il deliverable non attribuisce a Pratomagno la responsabilità dell'interruzione.
Fail se    l'interruzione è descritta come imputabile alla titolare del permesso o alla direzione dei lavori.
Indifferente  l'osservazione che la segnalazione che ha originato l'ordinanza proveniva da un terzo.

*metadati non forniti al judge* - fonte: 04_ordinanza_sospensione_lavori.md; 05_provvedimento_revoca.md; gravita: media; instradamento: judge

**B.31 presunzione dell'esito - proroga e assenso**  [issue: -] [tipo: assenza]

Verifica   Il deliverable non presenta come acquisiti la proroga né l'assenso paesaggistico sulla variante.
Pass se    Il deliverable non presenta come acquisiti la proroga né l'assenso paesaggistico sulla variante.
Fail se    è affermato che la proroga sarà concessa, o che l'assenso paesaggistico sulla variante sarà rilasciato.
Indifferente  l'indicazione dei presupposti su cui l'istanza si fonda.

*metadati non forniti al judge* - fonte: private/challenge_map.json, dati mancanti; gravita: alta; instradamento: judge


## Sezione C - date e valori calcolati

**C.1 termine di inizio dei lavori**  [issue: I-01] [tipo: valore]

Verifica   Il deliverable indica il 12 febbraio 2027 come termine massimo di inizio dei lavori.
Pass se    compare la data «12 febbraio 2027» riferita al termine di inizio dei lavori
Fail se    è indicata una data diversa, oppure il termine non compare.
Indifferente  l'osservazione che il termine è stato rispettato.

*metadati non forniti al judge* - fonte: art. 15, comma 2, del testo unico dell'edilizia; gravita: media; instradamento: verifica meccanica

**C.2 termine di ultimazione dei lavori**  [issue: I-02] [tipo: valore]

Verifica   Il deliverable indica l'11 maggio 2029 come termine di ultimazione dei lavori.
Pass se    compare la data «11 maggio 2029» riferita al termine di ultimazione
Fail se    è indicata una data diversa, oppure il termine non compare.
Indifferente  l'indicazione del margine residuo.

*metadati non forniti al judge* - fonte: art. 15, comma 2, del testo unico dell'edilizia; gravita: alta; instradamento: verifica meccanica

**C.3 derivazione errata dal rilascio**  [issue: I-02] [tipo: assenza]

Verifica   Il deliverable non computa il termine di ultimazione dal rilascio del titolo.
Pass se    Il deliverable non computa il termine di ultimazione dal rilascio del titolo.
Fail se    compare la data «12 febbraio 2029» come termine di ultimazione, oppure i tre anni sono computati dal rilascio del titolo.
Indifferente  la menzione della data di rilascio in altra funzione.

*metadati non forniti al judge* - fonte: derivazione da escludere; gravita: alta; instradamento: judge

**C.4 durata dell'interruzione in giorni di calendario**  [issue: I-06] [tipo: valore]

Verifica   Il deliverable indica in quarantasei giorni la durata dell'interruzione.
Pass se    compare il numero «quarantasei giorni» riferito alla durata dell'interruzione
Fail se    è indicato un numero diverso, oppure la durata non è quantificata.
Indifferente  l'indicazione dell'intervallo di date corrispondente.

*metadati non forniti al judge* - fonte: 04_ordinanza_sospensione_lavori.md; 05_provvedimento_revoca.md; gravita: media; instradamento: verifica meccanica

**C.5 derivazione errata in giorni lavorativi**  [issue: I-06] [tipo: assenza]

Verifica   Il deliverable non usa i giorni lavorativi perduti come misura dello slittamento del cronoprogramma.
Pass se    Il deliverable non usa i giorni lavorativi perduti come misura dello slittamento del cronoprogramma.
Fail se    lo slittamento del cronoprogramma è quantificato in giorni lavorativi anziché in giorni di calendario.
Indifferente  la menzione dei giorni lavorativi perduti in altra funzione.

*metadati non forniti al judge* - fonte: derivazione da escludere; gravita: media; instradamento: judge

**C.6 ultimazione programmata dopo lo slittamento**  [issue: I-07] [tipo: valore]

Verifica   Il deliverable indica il 25 maggio 2027 come ultimazione programmata dopo lo slittamento.
Pass se    compare la data «25 maggio 2027» riferita all'ultimazione programmata
Fail se    è indicata una data diversa, oppure la data non compare.
Indifferente  il richiamo alla data del cronoprogramma originario.

*metadati non forniti al judge* - fonte: 06_cronoprogramma_e_stato_avanzamento.md, punto 4; gravita: media; instradamento: verifica meccanica

**C.7 efficacia dell'autorizzazione paesaggistica**  [issue: N-01] [tipo: presenza]

Verifica   Il deliverable afferma che il quinquennio di efficacia dell'autorizzazione paesaggistica decorre dal giorno in cui acquista efficacia il titolo edilizio.
Pass se    compare l'affermazione che il quinquennio decorre dall'efficacia del titolo edilizio
Fail se    il quinquennio è computato dalla data di rilascio dell'autorizzazione.
Indifferente  l'indicazione della data di scadenza risultante.

*metadati non forniti al judge* - fonte: 02_autorizzazione_paesaggistica.md, avvertenze; gravita: alta; instradamento: judge

**C.8 derivazione errata sull'autorizzazione paesaggistica**  [issue: N-01] [tipo: assenza]

Verifica   Il deliverable non computa il quinquennio di efficacia dalla data di rilascio dell'autorizzazione paesaggistica.
Pass se    Il deliverable non computa il quinquennio di efficacia dalla data di rilascio dell'autorizzazione paesaggistica.
Fail se    compare la data «2 marzo 2028» come scadenza dell'autorizzazione paesaggistica, oppure il quinquennio è computato dal 2 marzo 2023.
Indifferente  la menzione della data di rilascio dell'autorizzazione in altra funzione.

*metadati non forniti al judge* - fonte: derivazione da escludere; gravita: alta; instradamento: judge

**C.9 incremento della superficie di solaio**  [issue: I-09] [tipo: valore]

Verifica   Il deliverable indica in 240 metri quadrati l'incremento della superficie di solaio.
Pass se    compare la misura «240» riferita all'incremento della superficie di solaio
Fail se    è indicata una misura diversa, oppure l'incremento non compare.
Indifferente  l'unità di misura usata.

*metadati non forniti al judge* - fonte: 07_relazione_direzione_lavori_variante.md, punto 3; gravita: alta; instradamento: verifica meccanica

**C.10 incremento in percentuale**  [issue: I-09] [tipo: valore]

Verifica   Il deliverable indica nel 14,63 per cento l'incremento percentuale della superficie di solaio.
Pass se    compare la percentuale «14,63» riferita all'incremento della superficie di solaio
Fail se    è indicata una percentuale diversa, oppure la percentuale non compare.
Indifferente  il numero di decimali usato.

*metadati non forniti al judge* - fonte: 07_relazione_direzione_lavori_variante.md, punto 3; gravita: media; instradamento: verifica meccanica
