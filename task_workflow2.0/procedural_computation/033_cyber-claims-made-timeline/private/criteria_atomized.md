# WF2-033 - Rubrica atomizzata

Generato da `source/authoring/costruisci_rubrica_033.py`. Non modificare a mano.

13 issue di merito, 50 criteri atomici (15 a verifica meccanica, 35 al judge).

## A. Forma dell'output (interamente verifica meccanica)

### A.1  [issue: A]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable e' un file denominato timeline_copertura_denuncia.md di lunghezza non superiore a 1.900 parole.

**Pass se** &nbsp; il file si chiama timeline_copertura_denuncia.md e il conteggio delle parole non supera 1.900

**Fail se** &nbsp; il nome del file e' diverso oppure il conteggio supera 1.900 parole.

*Non passa al judge:* fonte: response_template.md | gravita': bassa

### A.2  [issue: A]  [tipo: struttura]  [verifica meccanica]

**Verifica** &nbsp; il deliverable contiene, nell'ordine, sei sezioni intitolate Linea del tempo, Che cosa la polizza copre e che cosa no, Quadro dei termini, Calcoli, Checklist delle attivita' da compiere, Elementi mancanti dal fascicolo.

**Pass se** &nbsp; le sei intestazioni compaiono tutte e nell'ordine indicato

**Fail se** &nbsp; manca una intestazione oppure l'ordine e' diverso.

*Non passa al judge:* fonte: response_template.md | gravita': bassa

### A.3  [issue: A]  [tipo: struttura]  [verifica meccanica]

**Verifica** &nbsp; ogni riga della tabella della sezione 1 riporta il documento del fascicolo da cui il fatto risulta.

**Pass se** &nbsp; in ciascuna riga la colonna del documento e' compilata

**Fail se** &nbsp; una o piu' righe non indicano il documento.

*Non passa al judge:* fonte: response_template.md | gravita': media

### A.4  [issue: A]  [tipo: assenza]  [verifica meccanica]

**Verifica** &nbsp; il deliverable non contiene riferimenti normativi diversi da quelli elencati in fonti_chiuse.json.

**Pass se** &nbsp; tutti i riferimenti presenti compaiono nell'elenco chiuso

**Fail se** &nbsp; compare un riferimento estraneo all'elenco chiuso.

*Non passa al judge:* fonte: public/03_legal_sources.md | gravita': alta

### A.5  [issue: A]  [tipo: struttura]  [verifica meccanica]

**Verifica** &nbsp; ogni riga della tabella della sezione 3 riporta lo stato del termine alla data di riferimento.

**Pass se** &nbsp; in ciascuna riga la colonna dello stato e' compilata

**Fail se** &nbsp; una o piu' righe non indicano lo stato.

*Non passa al judge:* fonte: response_template.md | gravita': media

## B. Merito

Stato del fascicolo alla data di riferimento dell'8 agosto 2031: Evento denunciato, Richiesta ricevuta e non ancora denunciata, posizione aperta dall'Assicuratore, nessuna valutazione sull'operativita' della garanzia.

### B.1  [issue: I-01]  [tipo: qualificazione]  [judge]

**Verifica** &nbsp; il deliverable qualifica il momento delle ore 06:20 del 14 marzo 2031 come Scoperta dell'Evento.

**Pass se** &nbsp; compare, riferito a quel momento, una fra: «Scoperta», «scoperta dell'evento», «momento in cui l'evento e' stato scoperto», «apertura dell'incidente»

**Fail se** &nbsp; la Scoperta e' collocata in un momento diverso, oppure non e' individuata.

*Non passa al judge:* fonte: relazione di analisi forense; condizioni di assicurazione, definizione di Scoperta | gravita': alta

### B.2  [issue: I-01]  [tipo: assenza]  [judge]

**Verifica** &nbsp; il deliverable non fa decorrere il termine di denuncia dell'Evento dal primo accesso non autorizzato del 12 marzo 2031.

**Pass se** &nbsp; non compare l'affermazione che il termine di denuncia decorra dal 12 marzo 2031

**Fail se** &nbsp; il termine e' fatto decorrere dal primo accesso non autorizzato.

*Non passa al judge:* fonte: messaggio del direttore operativo; condizioni di assicurazione, art. 7 | gravita': alta

### B.3  [issue: I-02]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che la denuncia dell'Evento e' stata trasmessa entro il termine.

**Pass se** &nbsp; compare una fra: «tempestiva», «nel termine», «entro le settantadue ore», «entro il termine» riferito alla denuncia dell'Evento

**Fail se** &nbsp; la denuncia e' qualificata come tardiva, oppure la sua tempestivita' non e' trattata.

*Non passa al judge:* fonte: denuncia di sinistro con ricevuta di consegna | gravita': alta

### B.4  [issue: I-02]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable risponde alla tesi del broker affermando che non e' fondata.

**Pass se** &nbsp; compare l'affermazione che la tesi del broker sulla tardivita' e' errata, non fondata oppure smentita dai documenti

**Fail se** &nbsp; la tesi del broker non e' trattata, oppure e' condivisa.

*Non passa al judge:* fonte: messaggio del direttore operativo | gravita': alta

### B.5  [issue: I-03]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che la notifica all'autorita' di controllo e' stata effettuata entro settantadue ore dalla conoscenza della violazione.

**Pass se** &nbsp; compare l'affermazione che la notifica e' stata effettuata nel termine di settantadue ore

**Fail se** &nbsp; la notifica e' presentata come omessa o tardiva, oppure il punto non e' trattato.

*Non passa al judge:* fonte: notifica di violazione con ricevuta di protocollo; art. 33 Reg. UE 2016/679 | gravita': media

### B.6  [issue: I-04]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che il periodo di attesa decorre dall'inizio dell'Interruzione di Attivita'.

**Pass se** &nbsp; compare l'affermazione che le dodici ore si computano dall'inizio dell'interruzione, oppure dalle ore 05:40 del 14 marzo 2031

**Fail se** &nbsp; il periodo di attesa e' fatto decorrere dalla Scoperta o da altro momento.

*Non passa al judge:* fonte: condizioni di assicurazione, definizione di Periodo di Attesa | gravita': alta

### B.7  [issue: I-05]  [tipo: assenza]  [judge]

**Verifica** &nbsp; il deliverable non presenta come indennizzabile l'intera durata dell'interruzione.

**Pass se** &nbsp; non compare l'affermazione che il periodo indennizzabile coincide con l'intera durata dell'interruzione

**Fail se** &nbsp; l'intera durata dell'interruzione e' presentata come indennizzabile.

*Non passa al judge:* fonte: messaggio del direttore operativo; scheda di polizza | gravita': alta

### B.8  [issue: I-06]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che il termine di denuncia della Richiesta di Risarcimento decorre dalla ricezione della richiesta.

**Pass se** &nbsp; compare l'affermazione che i trenta giorni decorrono dalla ricezione, oppure dalla consegna risultante dalla ricevuta

**Fail se** &nbsp; il termine e' fatto decorrere dalla data della lettera.

*Non passa al judge:* fonte: condizioni di assicurazione, art. 8 | gravita': alta

### B.9  [issue: I-06]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che alla data di riferimento il termine di denuncia della Richiesta e' ancora aperto.

**Pass se** &nbsp; compare una fra: «pendente», «non ancora scaduto», «aperto», «restano … giorni» riferito a quel termine

**Fail se** &nbsp; il termine e' presentato come scaduto, oppure il suo stato non e' indicato.

*Non passa al judge:* fonte: data di riferimento del fascicolo | gravita': alta

### B.10  [issue: I-07]  [tipo: assenza]  [judge]

**Verifica** &nbsp; il deliverable non applica al termine di denuncia della Richiesta la sospensione dei termini nel periodo feriale.

**Pass se** &nbsp; non compare l'affermazione che il termine sia sospeso nel mese di agosto

**Fail se** &nbsp; al termine di denuncia e' applicata la sospensione feriale.

*Non passa al judge:* fonte: messaggio del direttore operativo; condizioni di assicurazione, art. 8 | gravita': alta

### B.11  [issue: I-08]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che lo studio legale incaricato non compare fra i Fornitori Autorizzati.

**Pass se** &nbsp; compare l'affermazione che lo studio incaricato non e' fra i Fornitori Autorizzati elencati in polizza

**Fail se** &nbsp; il punto non e' trattato.

*Non passa al judge:* fonte: lettera di incarico; scheda di polizza, Allegato 2 | gravita': alta

### B.12  [issue: I-08]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che la condizione posta dalla polizza per l'indennizzabilita' delle spese legali non e' soddisfatta.

**Pass se** &nbsp; compare l'affermazione che le spese non sono indennizzabili allo stato, oppure che la condizione della polizza non e' rispettata

**Fail se** &nbsp; le spese legali sono presentate come indennizzabili senza riserve.

*Non passa al judge:* fonte: condizioni di assicurazione, artt. 9 e 10 | gravita': alta

### B.13  [issue: I-08]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable indica fra le attivita' da compiere la richiesta del consenso scritto dell'Assicuratore alla nomina gia' effettuata.

**Pass se** &nbsp; compare l'indicazione di chiedere all'Assicuratore il consenso scritto sulla nomina dello studio

**Fail se** &nbsp; l'indicazione non compare.

*Non passa al judge:* fonte: condizioni di assicurazione, art. 9 | gravita': alta

### B.14  [issue: I-09]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che le spese di resistenza sono a carico dell'Assicuratore entro il limite del quarto della somma assicurata.

**Pass se** &nbsp; compare una fra: «un quarto», «il quarto», «25 per cento» riferito al limite delle spese di resistenza

**Fail se** &nbsp; il limite non e' indicato.

**Indifferente** &nbsp; il richiamo all'art. 1932 del codice civile e la discussione sulla derogabilita' della clausola: ne' richiesti ne' penalizzati.

*Non passa al judge:* fonte: art. 1917, comma 3, del codice civile; condizioni di assicurazione, art. 10 | gravita': media

### B.15  [issue: I-10]  [tipo: qualificazione]  [judge]

**Verifica** &nbsp; il deliverable qualifica come esclusa dalla copertura la voce della richiesta del terzo relativa alle sanzioni amministrative pecuniarie.

**Pass se** &nbsp; compare, riferita a quella voce, una fra: «esclusa», «non coperta», «non indennizzabile», «fuori copertura»

**Fail se** &nbsp; la voce e' trattata come coperta, oppure non e' trattata.

*Non passa al judge:* fonte: condizioni di assicurazione, art. 6, lettera c) | gravita': alta

### B.16  [issue: I-11]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che la documentazione richiesta dall'Assicuratore va consegnata entro quindici giorni dalla richiesta.

**Pass se** &nbsp; compare «quindici giorni» oppure «15 giorni» riferito alla consegna della documentazione

**Fail se** &nbsp; e' indicato un termine diverso, oppure l'obbligo non e' trattato.

*Non passa al judge:* fonte: condizioni di assicurazione, art. 11 | gravita': alta

### B.17  [issue: I-11]  [tipo: assenza]  [judge]

**Verifica** &nbsp; il deliverable non indica la consegna della documentazione all'Assicuratore come attivita' differibile a dopo il periodo feriale.

**Pass se** &nbsp; non compare l'indicazione di trasmettere la documentazione dopo Ferragosto o alla ripresa delle attivita'

**Fail se** &nbsp; la consegna e' collocata dopo la scadenza del termine.

*Non passa al judge:* fonte: messaggio del direttore operativo; condizioni di assicurazione, art. 11 | gravita': alta

### B.18  [issue: I-12]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che l'ammontare dell'indennizzo per interruzione di attivita' non e' determinabile dal fascicolo.

**Pass se** &nbsp; compare una fra: «non e' determinabile», «non e' quantificabile allo stato», «non e' possibile stabilire l'importo» riferito all'indennizzo per interruzione

**Fail se** &nbsp; e' indicato un importo di indennizzo per interruzione di attivita'.

*Non passa al judge:* fonte: condizioni di assicurazione, art. 3, lettera c) | gravita': alta

### B.19  [issue: I-12]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable indica il margine di contribuzione fra i dati mancanti necessari alla quantificazione.

**Pass se** &nbsp; compare il riferimento al margine di contribuzione fra i dati da acquisire

**Fail se** &nbsp; il riferimento non compare.

*Non passa al judge:* fonte: condizioni di assicurazione, art. 3, lettera c) | gravita': media

### B.20  [issue: I-13]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable indica fra i documenti da acquisire la relazione di analisi forense nella versione definitiva.

**Pass se** &nbsp; compare la richiesta della relazione forense definitiva

**Fail se** &nbsp; la richiesta non compare.

*Non passa al judge:* fonte: relazione di analisi forense, versione preliminare | gravita': media

### B.21  [issue: I-13]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che non e' possibile stabilire se e in che misura l'indennizzo sara' corrisposto.

**Pass se** &nbsp; compare una fra: «non e' possibile stabilire», «non e' possibile affermare», «resta da verificare», «l'esito dipende dagli accertamenti in corso» riferito all'indennizzo

**Fail se** &nbsp; il deliverable afferma che l'indennizzo sara' corrisposto oppure che sara' negato.

*Non passa al judge:* fonte: richiesta di documentazione dell'Assicuratore | gravita': alta

### B.22  [issue: I-05]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable distingue la durata complessiva dell'interruzione dalla durata indennizzabile.

**Pass se** &nbsp; compaiono due durate distinte, una riferita all'interruzione e una al periodo indennizzabile

**Fail se** &nbsp; e' indicata una sola durata.

*Non passa al judge:* fonte: relazione di analisi forense; scheda di polizza | gravita': alta

### B.23  [issue: I-10]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable indica l'importo della richiesta del terzo riferibile alla copertura al netto della voce esclusa.

**Pass se** &nbsp; compare un importo riferibile alla copertura distinto dal totale della richiesta

**Fail se** &nbsp; e' indicato soltanto il totale della richiesta.

*Non passa al judge:* fonte: richiesta di risarcimento del terzo | gravita': media

### B.24  [issue: I-02]  [tipo: assenza]  [judge]

**Verifica** &nbsp; sovra-segnalazione: il deliverable non segnala come rilievo la tardivita' della denuncia dell'Evento.

**Pass se** &nbsp; la tardivita' della denuncia dell'Evento non compare fra i rilievi

**Fail se** &nbsp; la denuncia dell'Evento e' segnalata come tardiva.

*Non passa al judge:* fonte: denuncia di sinistro con ricevuta di consegna | gravita': alta

### B.25  [issue: I-13]  [tipo: assenza]  [judge]

**Verifica** &nbsp; sovra-segnalazione: il deliverable non segnala la Data di Retroattivita' come ostacolo alla copertura.

**Pass se** &nbsp; la retroattivita' non compare fra i profili che limitano la copertura

**Fail se** &nbsp; la Data di Retroattivita' e' presentata come ostacolo.

*Non passa al judge:* fonte: scheda di polizza | gravita': media

### B.26  [issue: I-13]  [tipo: assenza]  [judge]

**Verifica** &nbsp; sovra-segnalazione: il deliverable non presenta come incapiente il sublimite per l'estorsione informatica.

**Pass se** &nbsp; il sublimite non compare fra i limiti che lasciano scoperta una parte dei costi sostenuti

**Fail se** &nbsp; il sublimite e' presentato come insufficiente rispetto ai costi di negoziazione.

*Non passa al judge:* fonte: scheda di polizza | gravita': media

### B.27  [issue: I-08]  [tipo: assenza]  [judge]

**Verifica** &nbsp; sovra-segnalazione: il deliverable non segnala come non indennizzabili le spese di analisi forense.

**Pass se** &nbsp; le spese di analisi forense non compaiono fra quelle non indennizzabili

**Fail se** &nbsp; le spese di analisi forense sono presentate come non indennizzabili.

*Non passa al judge:* fonte: scheda di polizza, Allegato 2 | gravita': alta

### B.28  [issue: I-13]  [tipo: assenza]  [judge]

**Verifica** &nbsp; sovra-segnalazione: il deliverable non presenta la scadenza della polizza come profilo che incide sulla copertura del sinistro.

**Pass se** &nbsp; la scadenza della polizza non compare fra i profili che incidono sulla copertura

**Fail se** &nbsp; la scadenza della polizza e' presentata come profilo rilevante.

*Non passa al judge:* fonte: scheda di polizza | gravita': media

### B.29  [issue: I-03]  [tipo: assenza]  [judge]

**Verifica** &nbsp; sovra-segnalazione: il deliverable non segnala come omessa la notifica all'autorita' di controllo.

**Pass se** &nbsp; l'omissione della notifica non compare fra i rilievi

**Fail se** &nbsp; la notifica all'autorita' e' presentata come omessa.

*Non passa al judge:* fonte: notifica di violazione con ricevuta di protocollo | gravita': media

### B.30  [issue: I-06]  [tipo: assenza]  [judge]

**Verifica** &nbsp; simmetria del controllo: il deliverable non afferma che il termine di denuncia della Richiesta di Risarcimento e' gia' scaduto.

**Pass se** &nbsp; non compare l'affermazione che quel termine sia scaduto prima della data di riferimento

**Fail se** &nbsp; il termine e' presentato come scaduto.

*Non passa al judge:* fonte: condizioni di assicurazione, art. 8 | gravita': alta

### B.31  [issue: I-13]  [tipo: assenza]  [judge]

**Verifica** &nbsp; divieto di presunzione dell'esito: il deliverable non afferma che l'Assicuratore corrispondera' l'indennizzo.

**Pass se** &nbsp; non compare l'affermazione che l'indennizzo sara' corrisposto

**Fail se** &nbsp; il pagamento dell'indennizzo e' presentato come esito atteso.

*Non passa al judge:* fonte: richiesta di documentazione dell'Assicuratore | gravita': alta

## C. Date, orari, durate e valori calcolati

### C.1  [issue: I-01]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable indica le ore 06:20 del 14 marzo 2031 come momento della Scoperta.

**Pass se** &nbsp; compare «06:20» riferito al 14 marzo 2031

**Fail se** &nbsp; e' indicato un momento diverso.

*Non passa al judge:* fonte: relazione di analisi forense | gravita': alta

### C.2  [issue: I-02]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable indica le ore 06:20 del 17 marzo 2031 come scadenza del termine di denuncia dell'Evento.

**Pass se** &nbsp; compare «17 marzo 2031» riferito alla scadenza del termine di denuncia dell'Evento

**Fail se** &nbsp; e' indicata una data diversa, oppure la scadenza non e' indicata.

*Non passa al judge:* fonte: condizioni di assicurazione, art. 7 | gravita': alta

### C.3  [issue: I-01]  [tipo: assenza]  [judge]

**Verifica** &nbsp; il deliverable non indica il 15 marzo 2031 come scadenza del termine di denuncia dell'Evento.

**Pass se** &nbsp; non compare il 15 marzo 2031 come scadenza del termine di denuncia

**Fail se** &nbsp; la scadenza del termine di denuncia e' indicata nel 15 marzo 2031, cioe' settantadue ore dal primo accesso non autorizzato.

*Non passa al judge:* fonte: derivazione errata ricostruita in fase di build | gravita': alta

### C.4  [issue: I-04]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable indica le ore 17:40 del 14 marzo 2031 come inizio del periodo indennizzabile.

**Pass se** &nbsp; compare «17:40» riferito all'inizio del periodo indennizzabile

**Fail se** &nbsp; e' indicato un momento diverso, oppure l'inizio non e' indicato.

*Non passa al judge:* fonte: scheda di polizza; relazione di analisi forense | gravita': alta

### C.5  [issue: I-04]  [tipo: assenza]  [judge]

**Verifica** &nbsp; il deliverable non indica le ore 18:20 del 14 marzo 2031 come inizio del periodo indennizzabile.

**Pass se** &nbsp; non compare «18:20» come inizio del periodo indennizzabile

**Fail se** &nbsp; l'inizio del periodo indennizzabile e' calcolato applicando il periodo di attesa alla Scoperta anziche' all'inizio dell'interruzione.

*Non passa al judge:* fonte: derivazione errata ricostruita in fase di build | gravita': alta

### C.6  [issue: I-05]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable indica in 61 ore e 30 minuti la durata complessiva dell'interruzione.

**Pass se** &nbsp; compare «61 ore e 30 minuti» oppure «61,5 ore» come durata complessiva

**Fail se** &nbsp; e' indicata una durata diversa, oppure la durata complessiva non e' indicata.

*Non passa al judge:* fonte: relazione di analisi forense | gravita': alta

### C.7  [issue: I-05]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable indica in 49 ore e 30 minuti la durata indennizzabile dell'interruzione.

**Pass se** &nbsp; compare «49 ore e 30 minuti» oppure «49,5 ore» come durata indennizzabile

**Fail se** &nbsp; e' indicata una durata diversa, oppure la durata indennizzabile non e' indicata.

*Non passa al judge:* fonte: scheda di polizza; relazione di analisi forense | gravita': alta

### C.8  [issue: I-06]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable indica il 22 agosto 2031 come termine per la denuncia della Richiesta di Risarcimento.

**Pass se** &nbsp; compare «22 agosto 2031» oppure «22/08/2031» come termine di denuncia della Richiesta

**Fail se** &nbsp; e' indicata una data diversa.

*Non passa al judge:* fonte: condizioni di assicurazione, art. 8 | gravita': alta

### C.9  [issue: I-06]  [tipo: assenza]  [judge]

**Verifica** &nbsp; il deliverable non indica il 20 agosto 2031 come termine per la denuncia della Richiesta.

**Pass se** &nbsp; non compare il 20 agosto 2031 come termine di denuncia della Richiesta

**Fail se** &nbsp; il termine e' calcolato dalla data della lettera del terzo anziche' dalla data di ricezione.

*Non passa al judge:* fonte: derivazione errata ricostruita in fase di build | gravita': alta

### C.10  [issue: I-07]  [tipo: assenza]  [judge]

**Verifica** &nbsp; il deliverable non indica il 22 settembre 2031 come termine per la denuncia della Richiesta.

**Pass se** &nbsp; non compare il 22 settembre 2031 come termine di denuncia della Richiesta

**Fail se** &nbsp; il termine e' calcolato applicando la sospensione feriale.

*Non passa al judge:* fonte: derivazione errata ricostruita in fase di build | gravita': alta

### C.11  [issue: I-11]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable indica il 14 agosto 2031 come termine per la consegna della documentazione all'Assicuratore.

**Pass se** &nbsp; compare «14 agosto 2031» oppure «14/08/2031» come termine di consegna

**Fail se** &nbsp; e' indicata una data diversa, oppure il termine non e' indicato.

*Non passa al judge:* fonte: richiesta di documentazione dell'Assicuratore; condizioni di assicurazione, art. 11 | gravita': alta

### C.12  [issue: I-09]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable indica euro 500.000,00 come limite delle spese di resistenza.

**Pass se** &nbsp; compare «500.000» come limite delle spese di resistenza

**Fail se** &nbsp; e' indicato un importo diverso, oppure il limite non e' quantificato.

*Non passa al judge:* fonte: scheda di polizza; art. 1917, comma 3, del codice civile | gravita': media

### C.13  [issue: I-10]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable indica euro 1.130.000,00 come importo della richiesta del terzo riferibile alla copertura.

**Pass se** &nbsp; compare «1.130.000» come importo riferibile alla copertura

**Fail se** &nbsp; e' indicato un importo diverso, oppure l'importo non e' indicato.

*Non passa al judge:* fonte: richiesta di risarcimento del terzo; condizioni di assicurazione, art. 6 | gravita': alta

### C.14  [issue: I-06]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable indica quattordici giorni come giorni residui del termine di denuncia della Richiesta alla data di riferimento.

**Pass se** &nbsp; compare «14 giorni» oppure «quattordici giorni» come giorni residui

**Fail se** &nbsp; e' indicato un numero diverso, oppure i giorni residui non sono indicati.

*Non passa al judge:* fonte: data di riferimento del fascicolo | gravita': media

