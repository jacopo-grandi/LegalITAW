# WF2-032 - Rubrica atomizzata

Generato da `source/authoring/costruisci_rubrica_032.py`. Non modificare a mano.

13 issue di merito, 49 criteri atomici (12 a verifica meccanica, 37 al judge).

## A. Forma dell'output (interamente verifica meccanica)

### A.1  [issue: A]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable e' un file denominato audit_dei_termini.md di lunghezza non superiore a 1.800 parole.

**Pass se** &nbsp; il file si chiama audit_dei_termini.md e il conteggio delle parole non supera 1.800

**Fail se** &nbsp; il nome del file e' diverso oppure il conteggio supera 1.800 parole.

*Non passa al judge:* fonte: response_template.md | gravita': bassa

### A.2  [issue: A]  [tipo: struttura]  [verifica meccanica]

**Verifica** &nbsp; il deliverable contiene, nell'ordine, sette sezioni intitolate La data entro cui decidere, Quadro dei termini, Opzioni percorribili e opzioni esaurite, Calcoli, Attivita' da compiere, Che cosa non torna nella nota del consulente, Elementi mancanti dal fascicolo.

**Pass se** &nbsp; le sette intestazioni compaiono tutte e nell'ordine indicato

**Fail se** &nbsp; manca una intestazione oppure l'ordine e' diverso.

*Non passa al judge:* fonte: response_template.md | gravita': bassa

### A.3  [issue: A]  [tipo: struttura]  [verifica meccanica]

**Verifica** &nbsp; la sezione La data entro cui decidere contiene una sola data.

**Pass se** &nbsp; nella sezione compare una sola data di calendario

**Fail se** &nbsp; nella sezione compaiono piu' date oppure nessuna.

*Non passa al judge:* fonte: response_template.md | gravita': alta

### A.4  [issue: A]  [tipo: assenza]  [verifica meccanica]

**Verifica** &nbsp; il deliverable non contiene riferimenti normativi diversi da quelli elencati in fonti_chiuse.json, comprensivi dell'array dei riferimenti richiamati nei documenti del fascicolo.

**Pass se** &nbsp; tutti i riferimenti presenti compaiono nell'elenco chiuso

**Fail se** &nbsp; compare un riferimento estraneo all'elenco chiuso.

*Non passa al judge:* fonte: public/03_legal_sources.md | gravita': alta

### A.5  [issue: A]  [tipo: struttura]  [verifica meccanica]

**Verifica** &nbsp; ogni riga della tabella della sezione 2 riporta il documento del fascicolo da cui risulta l'evento iniziale.

**Pass se** &nbsp; in ciascuna riga la colonna del documento e' compilata

**Fail se** &nbsp; una o piu' righe non indicano il documento.

*Non passa al judge:* fonte: response_template.md | gravita': media

## B. Merito

Stato del fascicolo alla data di riferimento del 16 settembre 2030: avviso notificato, procedimento di adesione chiuso senza accordo, nessun ricorso proposto, nessun pagamento effettuato.

### B.1  [issue: I-01]  [tipo: qualificazione]  [judge]

**Verifica** &nbsp; il deliverable qualifica la ricevuta di avvenuta consegna come atto da cui decorre il termine per il ricorso.

**Pass se** &nbsp; compare, riferita alla decorrenza, una fra: «ricevuta di avvenuta consegna», «ricevuta di consegna», «data di consegna della posta elettronica certificata»

**Fail se** &nbsp; la decorrenza e' agganciata alla data dell'avviso, alla ricevuta di accettazione o a nessun documento.

*Non passa al judge:* fonte: ricevute di posta certificata | gravita': alta

### B.2  [issue: I-01]  [tipo: assenza]  [judge]

**Verifica** &nbsp; il deliverable non fa decorrere il termine per il ricorso dalla data dell'avviso di accertamento.

**Pass se** &nbsp; non compare l'affermazione che il termine decorra dal 17 giugno 2030

**Fail se** &nbsp; il termine e' fatto decorrere dalla data dell'atto.

*Non passa al judge:* fonte: avviso di accertamento | gravita': alta

### B.3  [issue: I-02]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che la sospensione conseguente all'istanza di adesione e' di trenta giorni.

**Pass se** &nbsp; compare «trenta giorni» oppure «30 giorni» riferito alla sospensione del termine di impugnazione

**Fail se** &nbsp; e' indicata una durata diversa, oppure la durata non e' indicata.

*Non passa al judge:* fonte: art. 6, commi 2-bis e 3, D.Lgs. 218/1997 | gravita': alta

### B.4  [issue: I-02]  [tipo: attribuzione]  [judge]

**Verifica** &nbsp; il deliverable riconduce la durata di trenta giorni alla circostanza che l'avviso e' stato preceduto dalla comunicazione dello schema di atto e che l'istanza e' stata presentata dopo la notifica.

**Pass se** &nbsp; compare il riferimento allo schema di atto, oppure al contraddittorio preventivo, come ragione della durata ridotta della sospensione

**Fail se** &nbsp; la durata non e' motivata, oppure e' motivata con una ragione diversa.

*Non passa al judge:* fonte: comunicazione dello schema di atto; istanza del 1 luglio 2030 | gravita': alta

### B.5  [issue: I-02]  [tipo: assenza]  [judge]

**Verifica** &nbsp; il deliverable non afferma che la sospensione conseguente all'istanza di adesione e' di novanta giorni.

**Pass se** &nbsp; non compare «novanta giorni» ne' «90 giorni» riferito alla sospensione applicabile al caso

**Fail se** &nbsp; la sospensione e' indicata in novanta giorni.

*Non passa al judge:* fonte: nota del consulente fiscale; art. 6, comma 2-bis, D.Lgs. 218/1997 | gravita': alta

### B.6  [issue: I-03]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che alla sospensione da adesione si aggiunge la sospensione feriale.

**Pass se** &nbsp; compare una fra: «si cumula», «si aggiunge», «si somma», «entrambe le sospensioni» riferito alla sospensione feriale

**Fail se** &nbsp; la sospensione feriale non e' applicata, oppure e' presentata come assorbita da quella da adesione.

*Non passa al judge:* fonte: art. 1 legge 742/1969 | gravita': alta

### B.7  [issue: I-05]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che alla data di riferimento il termine per il ricorso e' ancora pendente.

**Pass se** &nbsp; compare una fra: «e' ancora pendente», «non e' ancora scaduto», «e' in corso», «aperto», «restano … giorni»

**Fail se** &nbsp; il termine e' presentato come scaduto, oppure il suo stato non e' indicato.

*Non passa al judge:* fonte: data di riferimento del fascicolo | gravita': alta

### B.8  [issue: I-06]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che l'istanza di accertamento con adesione e' stata presentata nel termine.

**Pass se** &nbsp; compare una fra: «tempestiva», «nel termine», «entro il termine», «regolarmente presentata» riferito all'istanza

**Fail se** &nbsp; l'istanza e' qualificata come tardiva, oppure la sua tempestivita' non e' trattata.

*Non passa al judge:* fonte: istanza con ricevuta di protocollo | gravita': alta

### B.9  [issue: I-07]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che la sospensione non si e' interrotta con il verbale di mancato accordo.

**Pass se** &nbsp; compare l'affermazione che la sospensione opera per l'intero periodo, oppure che la chiusura del procedimento non incide sul decorso del termine

**Fail se** &nbsp; il punto non e' trattato.

*Non passa al judge:* fonte: art. 6, comma 3, D.Lgs. 218/1997 | gravita': alta

### B.10  [issue: I-07]  [tipo: assenza]  [judge]

**Verifica** &nbsp; il deliverable non fa riprendere il decorso del termine dal verbale di mancato accordo del 4 settembre 2030.

**Pass se** &nbsp; non compare l'affermazione che il termine abbia ripreso a decorrere dal verbale

**Fail se** &nbsp; il termine e' calcolato facendolo riprendere dal verbale.

*Non passa al judge:* fonte: nota del consulente fiscale; verbale di contraddittorio | gravita': alta

### B.11  [issue: I-08]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che la riduzione delle sanzioni a un terzo per omessa impugnazione presuppone anche la rinuncia a formulare istanza di accertamento con adesione.

**Pass se** &nbsp; compare il riferimento alla rinuncia a formulare istanza di accertamento con adesione fra le condizioni della riduzione

**Fail se** &nbsp; la condizione non e' indicata.

*Non passa al judge:* fonte: art. 15, comma 1, D.Lgs. 218/1997 | gravita': alta

### B.12  [issue: I-08]  [tipo: assenza]  [judge]

**Verifica** &nbsp; il deliverable non afferma che la riduzione delle sanzioni a un terzo e' acquisita alla societa'.

**Pass se** &nbsp; non compare l'affermazione che, pagando, le sanzioni si riducono in ogni caso a un terzo

**Fail se** &nbsp; la riduzione e' presentata come disponibile senza riserve.

*Non passa al judge:* fonte: nota del consulente fiscale; art. 15, comma 1, D.Lgs. 218/1997 | gravita': alta

### B.13  [issue: I-09]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che in pendenza di ricorso l'Ufficio puo' iscrivere a titolo provvisorio un terzo delle maggiori imposte accertate.

**Pass se** &nbsp; compare una fra: «un terzo», «1/3», «iscrizione a titolo provvisorio» riferita alle maggiori imposte accertate

**Fail se** &nbsp; il punto non e' trattato.

*Non passa al judge:* fonte: art. 15, comma 1, d.P.R. 602/1973 | gravita': alta

### B.14  [issue: I-09]  [tipo: assenza]  [judge]

**Verifica** &nbsp; il deliverable non afferma che in pendenza di ricorso nessuna somma puo' essere iscritta a ruolo.

**Pass se** &nbsp; non compare l'affermazione che le somme restino sospese fino alla sentenza per effetto del solo ricorso

**Fail se** &nbsp; il deliverable afferma che il ricorso impedisce ogni iscrizione a ruolo.

*Non passa al judge:* fonte: nota del consulente fiscale; art. 15, comma 1, d.P.R. 602/1973 | gravita': alta

### B.15  [issue: I-09]  [tipo: assenza]  [judge]

**Verifica** &nbsp; il deliverable non include le sanzioni nella base dell'iscrizione a titolo provvisorio.

**Pass se** &nbsp; non compare l'affermazione che l'iscrizione a titolo provvisorio comprenda un terzo delle sanzioni

**Fail se** &nbsp; le sanzioni sono conteggiate nella base dell'iscrizione a titolo provvisorio.

*Non passa al judge:* fonte: art. 15, comma 1, d.P.R. 602/1973 | gravita': media

### B.16  [issue: I-10]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che la sospensione dell'atto impugnato si chiede con istanza motivata proposta nel ricorso o con atto separato.

**Pass se** &nbsp; compare una fra: «istanza motivata nel ricorso», «con atto separato», «istanza di sospensione»

**Fail se** &nbsp; la sospensione e' presentata come effetto automatico del ricorso, oppure il punto non e' trattato.

*Non passa al judge:* fonte: art. 47, comma 1, D.Lgs. 546/1992 | gravita': media

### B.17  [issue: I-10]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable indica il danno grave e irreparabile come presupposto dell'istanza di sospensione.

**Pass se** &nbsp; compare «danno grave e irreparabile» oppure «danno grave ed irreparabile»

**Fail se** &nbsp; il presupposto non e' indicato.

*Non passa al judge:* fonte: art. 47, comma 1, D.Lgs. 546/1992 | gravita': media

### B.18  [issue: I-11]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che la costituzione in giudizio va effettuata entro trenta giorni dalla proposizione del ricorso.

**Pass se** &nbsp; compare «trenta giorni» oppure «30 giorni» riferito alla costituzione in giudizio del ricorrente

**Fail se** &nbsp; e' indicato un termine diverso, oppure la costituzione non e' trattata.

*Non passa al judge:* fonte: art. 22, comma 1, D.Lgs. 546/1992 | gravita': alta

### B.19  [issue: I-11]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che la costituzione tardiva comporta l'inammissibilita' del ricorso.

**Pass se** &nbsp; compare una fra: «a pena di inammissibilita'», «il ricorso e' inammissibile», «si decade dal ricorso»

**Fail se** &nbsp; la conseguenza non e' indicata.

*Non passa al judge:* fonte: art. 22, comma 1, D.Lgs. 546/1992 | gravita': media

### B.20  [issue: I-12]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che il procedimento di accertamento con adesione e' esaurito.

**Pass se** &nbsp; compare una fra: «esaurito», «concluso», «chiuso», «non piu' percorribile» riferito al procedimento di adesione

**Fail se** &nbsp; il procedimento di adesione e' presentato come ancora aperto, oppure il punto non e' trattato.

*Non passa al judge:* fonte: verbale di contraddittorio del 4 settembre 2030 | gravita': alta

### B.21  [issue: I-12]  [tipo: assenza]  [judge]

**Verifica** &nbsp; il deliverable non indica la presentazione di una nuova istanza di accertamento con adesione fra le azioni possibili.

**Pass se** &nbsp; non compare l'indicazione di presentare una seconda istanza di accertamento con adesione

**Fail se** &nbsp; una nuova istanza di adesione e' indicata fra le azioni possibili.

*Non passa al judge:* fonte: nota del consulente fiscale; art. 6 D.Lgs. 218/1997 | gravita': alta

### B.22  [issue: I-13]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable indica fra i documenti da acquisire la documentazione contabile su cui si fondano i rilievi.

**Pass se** &nbsp; compare la richiesta dei documenti di trasporto, delle fatture o delle scritture contabili relative ai rilievi

**Fail se** &nbsp; la richiesta non compare.

*Non passa al judge:* fonte: composizione del fascicolo | gravita': media

### B.23  [issue: I-13]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che non e' possibile stabilire quale sara' l'esito del ricorso.

**Pass se** &nbsp; compare una fra: «non e' possibile stabilire», «non e' prevedibile allo stato», «l'esito dipende da elementi non disponibili» riferito al ricorso

**Fail se** &nbsp; il deliverable afferma che il ricorso sara' accolto oppure che sara' respinto.

*Non passa al judge:* fonte: composizione del fascicolo | gravita': alta

### B.24  [issue: I-12]  [tipo: assenza]  [judge]

**Verifica** &nbsp; sovra-segnalazione: il deliverable non indica il reclamo con proposta di mediazione fra i passaggi da compiere prima del ricorso.

**Pass se** &nbsp; il reclamo non compare fra le attivita' da compiere

**Fail se** &nbsp; il reclamo e' indicato come passaggio necessario o possibile.

*Non passa al judge:* fonte: art. 2, comma 3, lettera a), D.Lgs. 220/2023 | gravita': alta

### B.25  [issue: I-13]  [tipo: assenza]  [judge]

**Verifica** &nbsp; sovra-segnalazione: il deliverable non segnala come vizio dell'atto la mancanza del contraddittorio preventivo.

**Pass se** &nbsp; la mancanza del contraddittorio preventivo non compare fra i vizi dell'atto

**Fail se** &nbsp; la mancanza del contraddittorio preventivo e' segnalata come vizio.

*Non passa al judge:* fonte: comunicazione dello schema di atto; osservazioni del 27 maggio 2030 | gravita': alta

### B.26  [issue: I-06]  [tipo: assenza]  [judge]

**Verifica** &nbsp; sovra-segnalazione: il deliverable non qualifica come tardiva l'istanza di accertamento con adesione del 1 luglio 2030.

**Pass se** &nbsp; non compare l'affermazione che l'istanza sia tardiva o inefficace

**Fail se** &nbsp; l'istanza e' qualificata come tardiva.

*Non passa al judge:* fonte: istanza con ricevuta di protocollo | gravita': alta

### B.27  [issue: I-12]  [tipo: assenza]  [judge]

**Verifica** &nbsp; sovra-segnalazione: il deliverable non inserisce fra i termini aperti il termine di venti giorni per il versamento delle somme dovute per effetto dell'adesione.

**Pass se** &nbsp; il termine di venti giorni non compare fra i termini aperti

**Fail se** &nbsp; il termine di venti giorni e' indicato come aperto o come imminente.

*Non passa al judge:* fonte: art. 8, comma 1, D.Lgs. 218/1997; verbale di mancato accordo | gravita': media

### B.28  [issue: I-01]  [tipo: assenza]  [judge]

**Verifica** &nbsp; sovra-segnalazione: il deliverable non segnala come vizio la notificazione dell'avviso a mezzo posta elettronica certificata.

**Pass se** &nbsp; la notificazione non compare fra i vizi dell'atto

**Fail se** &nbsp; la notificazione e' segnalata come nulla o irregolare.

*Non passa al judge:* fonte: ricevute di posta certificata | gravita': media

### B.29  [issue: I-04]  [tipo: assenza]  [judge]

**Verifica** &nbsp; simmetria del controllo: il deliverable non afferma che il termine per il ricorso e' gia' scaduto.

**Pass se** &nbsp; non compare l'affermazione che il termine sia scaduto prima della data di riferimento

**Fail se** &nbsp; il termine e' presentato come gia' scaduto.

*Non passa al judge:* fonte: art. 21 D.Lgs. 546/1992 | gravita': alta

### B.30  [issue: I-13]  [tipo: assenza]  [judge]

**Verifica** &nbsp; divieto di presunzione dell'esito: il deliverable non afferma che i rilievi saranno annullati in sede di ricorso.

**Pass se** &nbsp; non compare l'affermazione che i rilievi saranno annullati

**Fail se** &nbsp; l'annullamento dei rilievi e' presentato come esito atteso.

*Non passa al judge:* fonte: composizione del fascicolo alla data di riferimento | gravita': alta

## C. Date e valori calcolati

### C.1  [issue: I-01]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable indica il 20 giugno 2030 come data da cui decorre il termine per il ricorso.

**Pass se** &nbsp; compare «20 giugno 2030» oppure «20/06/2030» come decorrenza

**Fail se** &nbsp; e' indicata una data diversa.

*Non passa al judge:* fonte: ricevuta di avvenuta consegna | gravita': alta

### C.2  [issue: I-01]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che il giorno iniziale non si computa.

**Pass se** &nbsp; compare una fra: «il giorno iniziale non si computa», «a decorrere dal giorno successivo», «escluso il giorno di notificazione», «dal 21 giugno 2030»

**Fail se** &nbsp; il passaggio non compare.

*Non passa al judge:* fonte: art. 155, comma 1, del codice di procedura civile | gravita': media

### C.3  [issue: I-04]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable indica il 19 ottobre 2030 come scadenza nominale del termine per il ricorso.

**Pass se** &nbsp; compare «19 ottobre 2030» oppure «19/10/2030» come scadenza prima della proroga

**Fail se** &nbsp; la scadenza nominale non e' indicata, oppure e' indicata una data diversa.

*Non passa al judge:* fonte: art. 21 D.Lgs. 546/1992 | gravita': alta

### C.4  [issue: I-04]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che la scadenza cade di sabato ed e' percio' prorogata.

**Pass se** &nbsp; compare una fra: «cade di sabato», «e' un sabato», «prorogata al primo giorno non festivo», «slitta al lunedi'»

**Fail se** &nbsp; il passaggio non compare.

*Non passa al judge:* fonte: art. 155, commi 4 e 5, del codice di procedura civile | gravita': alta

### C.5  [issue: I-04]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable indica il 21 ottobre 2030 come termine ultimo per la proposizione del ricorso.

**Pass se** &nbsp; compare «21 ottobre 2030» oppure «21/10/2030» come termine ultimo

**Fail se** &nbsp; e' indicata una data diversa.

*Non passa al judge:* fonte: art. 21 D.Lgs. 546/1992; art. 155 del codice di procedura civile | gravita': alta

### C.6  [issue: I-06]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable indica il 5 luglio 2030 come termine entro cui l'istanza di adesione doveva essere presentata.

**Pass se** &nbsp; compare «5 luglio 2030» oppure «05/07/2030» come termine per l'istanza

**Fail se** &nbsp; e' indicata una data diversa, oppure il termine non e' indicato.

*Non passa al judge:* fonte: art. 6, comma 2-bis, D.Lgs. 218/1997 | gravita': media

### C.7  [issue: I-11]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable indica il 20 novembre 2030 come termine per la costituzione in giudizio nell'ipotesi di ricorso notificato il 21 ottobre 2030.

**Pass se** &nbsp; compare «20 novembre 2030» oppure «20/11/2030» come termine di costituzione

**Fail se** &nbsp; e' indicata una data diversa, oppure il termine non e' indicato.

*Non passa al judge:* fonte: art. 22, comma 1, D.Lgs. 546/1992 | gravita': alta

### C.8  [issue: I-09]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable indica euro 166.000,00 come importo iscrivibile a titolo provvisorio.

**Pass se** &nbsp; compare «166.000» come importo iscrivibile a titolo provvisorio

**Fail se** &nbsp; e' indicato un importo diverso, oppure l'importo non e' indicato.

*Non passa al judge:* fonte: avviso di accertamento; art. 15, comma 1, d.P.R. 602/1973 | gravita': alta

### C.9  [issue: I-02]  [tipo: assenza]  [judge]

**Verifica** &nbsp; il deliverable non indica il 18 dicembre 2030 come termine per il ricorso.

**Pass se** &nbsp; non compare «18 dicembre 2030» ne' «18/12/2030» come termine

**Fail se** &nbsp; il termine per il ricorso e' indicato nel 18 dicembre 2030, cioe' il risultato di una sospensione di novanta giorni.

*Non passa al judge:* fonte: derivazione errata ricostruita in fase di build | gravita': alta

### C.10  [issue: I-07]  [tipo: assenza]  [judge]

**Verifica** &nbsp; il deliverable non indica il 23 ottobre 2030 come termine per il ricorso.

**Pass se** &nbsp; non compare «23 ottobre 2030» ne' «23/10/2030» come termine

**Fail se** &nbsp; il termine per il ricorso e' indicato nel 23 ottobre 2030, cioe' il risultato del decorso ripreso dal verbale di mancato accordo.

*Non passa al judge:* fonte: derivazione errata ricostruita in fase di build | gravita': alta

### C.11  [issue: I-03]  [tipo: assenza]  [judge]

**Verifica** &nbsp; il deliverable non indica il 18 settembre 2030 come termine per il ricorso.

**Pass se** &nbsp; non compare «18 settembre 2030» ne' «18/09/2030» come termine

**Fail se** &nbsp; il termine per il ricorso e' indicato nel 18 settembre 2030, cioe' il risultato del computo senza sospensione feriale.

*Non passa al judge:* fonte: derivazione errata ricostruita in fase di build | gravita': alta

### C.12  [issue: I-02]  [tipo: assenza]  [judge]

**Verifica** &nbsp; il deliverable non indica il 19 settembre 2030 come termine per il ricorso.

**Pass se** &nbsp; non compare «19 settembre 2030» ne' «19/09/2030» come termine

**Fail se** &nbsp; il termine per il ricorso e' indicato nel 19 settembre 2030, cioe' il risultato del computo senza la sospensione da adesione.

*Non passa al judge:* fonte: derivazione errata ricostruita in fase di build | gravita': alta

### C.13  [issue: I-01]  [tipo: assenza]  [judge]

**Verifica** &nbsp; il deliverable non indica il 16 ottobre 2030 come termine per il ricorso.

**Pass se** &nbsp; non compare «16 ottobre 2030» ne' «16/10/2030» come termine

**Fail se** &nbsp; il termine per il ricorso e' indicato nel 16 ottobre 2030, cioe' il risultato del computo dalla data dell'avviso.

*Non passa al judge:* fonte: derivazione errata ricostruita in fase di build | gravita': alta

### C.14  [issue: I-05]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable indica trentacinque giorni come giorni residui alla data di riferimento.

**Pass se** &nbsp; compare «35 giorni» oppure «trentacinque giorni» come giorni residui

**Fail se** &nbsp; e' indicato un numero diverso, oppure i giorni residui non sono indicati.

*Non passa al judge:* fonte: data di riferimento del fascicolo | gravita': media

