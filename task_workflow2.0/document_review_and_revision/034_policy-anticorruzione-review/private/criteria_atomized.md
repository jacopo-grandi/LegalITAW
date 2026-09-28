# WF2-034 - Rubrica atomizzata

Generato da `source/authoring/costruisci_rubrica_034.py`. Non modificare a mano.

16 issue di merito, 47 criteri atomici (10 a verifica meccanica, 37 al judge).

## A. Forma dell'output (interamente verifica meccanica)

### A.1  [issue: A]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable e' un file denominato nota_di_review.md di lunghezza non superiore a 2.000 parole.

**Pass se** &nbsp; il file si chiama nota_di_review.md e il conteggio delle parole non supera 2.000

**Fail se** &nbsp; il nome del file e' diverso oppure il conteggio supera 2.000 parole.

*Non passa al judge:* fonte: response_template.md | gravita': bassa

### A.2  [issue: A]  [tipo: struttura]  [verifica meccanica]

**Verifica** &nbsp; il deliverable contiene, nell'ordine, sei sezioni intitolate Sintesi per il comitato, Rilievi bloccanti, Rilievi non bloccanti, Che cosa non e' un rilievo, Coordinamento con i documenti in vigore, Elementi mancanti e limiti della review.

**Pass se** &nbsp; le sei intestazioni compaiono tutte e nell'ordine indicato

**Fail se** &nbsp; manca una intestazione oppure l'ordine e' diverso.

*Non passa al judge:* fonte: response_template.md | gravita': bassa

### A.3  [issue: A]  [tipo: struttura]  [verifica meccanica]

**Verifica** &nbsp; ogni riga delle tabelle delle sezioni 2 e 3 riporta la clausola o l'allegato da cui il rilievo deriva.

**Pass se** &nbsp; in ciascuna riga la colonna della clausola e' compilata

**Fail se** &nbsp; una o piu' righe non indicano la clausola o l'allegato.

*Non passa al judge:* fonte: response_template.md | gravita': alta

### A.4  [issue: A]  [tipo: assenza]  [verifica meccanica]

**Verifica** &nbsp; il deliverable non contiene riferimenti normativi diversi da quelli elencati in fonti_chiuse.json.

**Pass se** &nbsp; tutti i riferimenti presenti compaiono nell'elenco chiuso

**Fail se** &nbsp; compare un riferimento estraneo all'elenco chiuso.

*Non passa al judge:* fonte: public/03_legal_sources.md | gravita': alta

### A.5  [issue: A]  [tipo: assenza]  [verifica meccanica]

**Verifica** &nbsp; il deliverable non contiene testo riformulato delle clausole della bozza.

**Pass se** &nbsp; non compare alcun blocco di testo introdotto da una formula di riscrittura quale «il testo dell'articolo … e' sostituito dal seguente», «nuova formulazione», «testo proposto», «si propone il seguente testo»

**Fail se** &nbsp; compare almeno un blocco di testo presentato come nuova formulazione di una clausola.

*Non passa al judge:* fonte: response_template.md | gravita': alta

## B. Merito

Stato del fascicolo alla data di riferimento del 12 novembre 2032: bozza non adottata, esaminata dal comitato, consiglio fissato per il 3 dicembre 2032, codice etico e procedura sulle segnalazioni in vigore.

### B.1  [issue: I-01]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che il limite dell'articolo 5.2 opera per singola erogazione e non per destinatario.

**Pass se** &nbsp; compare l'affermazione che manca un limite cumulativo, un tetto annuo per destinatario oppure un'aggregazione delle erogazioni

**Fail se** &nbsp; il punto non e' trattato.

*Non passa al judge:* fonte: bozza, art. 5.2 | gravita': alta

### B.2  [issue: I-01]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che in assenza di limite cumulativo la regola si aggira frazionando le erogazioni.

**Pass se** &nbsp; compare una fra: «frazionamento», «frazionando», «erogazioni ripetute», «piu' omaggi allo stesso destinatario»

**Fail se** &nbsp; la conseguenza non e' indicata.

*Non passa al judge:* fonte: bozza, art. 5.2 | gravita': alta

### B.3  [issue: I-02]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che l'articolo 5.3 confligge con il divieto assoluto posto dal codice etico.

**Pass se** &nbsp; compare il riferimento al conflitto fra l'articolo 5.3 della bozza e l'articolo 4 del codice etico, oppure fra la deroga per il modico valore e il divieto assoluto in vigore

**Fail se** &nbsp; il conflitto non e' rilevato.

*Non passa al judge:* fonte: bozza, art. 5.3; codice etico, art. 4 | gravita': alta

### B.4  [issue: I-02]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che il codice etico prevale sulla policy oppure che il conflitto va risolto dal consiglio di amministrazione prima dell'approvazione.

**Pass se** &nbsp; compare una fra: «il codice etico prevale», «prevale il codice etico», «la policy deve conformarsi al codice etico», «il conflitto va risolto prima dell'approvazione»

**Fail se** &nbsp; il deliverable afferma che la policy prevale sul codice etico in quanto successiva, oppure non indica come risolvere il conflitto.

*Non passa al judge:* fonte: codice etico, art. 9 | gravita': alta

### B.5  [issue: I-03]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che la bozza non definisce il modico valore.

**Pass se** &nbsp; compare l'affermazione che il modico valore non e' definito, non e' quantificato oppure e' privo di un criterio

**Fail se** &nbsp; il punto non e' trattato.

*Non passa al judge:* fonte: bozza, artt. 3 e 5.3 | gravita': alta

### B.6  [issue: I-03]  [tipo: assenza]  [judge]

**Verifica** &nbsp; il deliverable non afferma che il limite di euro 150,00 dell'articolo 5.2 si applica anche agli omaggi a pubblici ufficiali.

**Pass se** &nbsp; non compare l'affermazione che il limite dell'articolo 5.2 valga per i pubblici ufficiali

**Fail se** &nbsp; il limite dell'articolo 5.2 e' esteso agli omaggi a pubblici ufficiali.

*Non passa al judge:* fonte: bozza, artt. 5.2 e 5.3 | gravita': media

### B.7  [issue: I-04]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable segnala come rilievo il rimborso delle spese dell'accompagnatore previsto dall'articolo 6.2.

**Pass se** &nbsp; compare il riferimento all'accompagnatore fra i rilievi

**Fail se** &nbsp; il punto non e' trattato.

*Non passa al judge:* fonte: bozza, art. 6.2 | gravita': alta

### B.8  [issue: I-05]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che manca il divieto di ospitalita' verso soggetti che stiano decidendo su affari della societa'.

**Pass se** &nbsp; compare l'affermazione che manca il divieto durante gare, affidamenti, autorizzazioni o procedure decisorie in corso

**Fail se** &nbsp; il punto non e' trattato.

*Non passa al judge:* fonte: bozza, art. 6 | gravita': alta

### B.9  [issue: I-06]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che la verifica sul beneficiario delle sponsorizzazioni scatta solo oltre la soglia.

**Pass se** &nbsp; compare l'affermazione che sotto la soglia non e' prevista alcuna verifica

**Fail se** &nbsp; il punto non e' trattato.

*Non passa al judge:* fonte: bozza, art. 7.3 | gravita': alta

### B.10  [issue: I-07]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che la verifica dell'articolo 7.3 non comprende l'accertamento dei collegamenti fra il beneficiario e i soggetti che decidono su affari della societa'.

**Pass se** &nbsp; compare il riferimento alla mancata verifica dei collegamenti, dei rapporti o della riconducibilita' del beneficiario a decisori

**Fail se** &nbsp; il punto non e' trattato.

*Non passa al judge:* fonte: bozza, art. 7.3 | gravita': alta

### B.11  [issue: I-08]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che la due diligence sugli intermediari non e' rinnovata dopo la stipula.

**Pass se** &nbsp; compare una fra: «non e' previsto il rinnovo», «non e' rinnovata», «manca l'aggiornamento periodico», «la verifica resta ferma alla data iniziale», «resta ferma alla data della stipula»

**Fail se** &nbsp; il punto non e' trattato.

*Non passa al judge:* fonte: bozza, art. 9.1 | gravita': alta

### B.12  [issue: I-08]  [tipo: assenza]  [judge]

**Verifica** &nbsp; il deliverable non afferma che la bozza non prevede alcuna verifica sugli intermediari.

**Pass se** &nbsp; non compare l'affermazione che la due diligence iniziale manchi

**Fail se** &nbsp; la due diligence iniziale e' presentata come assente.

*Non passa al judge:* fonte: bozza, art. 9.1 | gravita': media

### B.13  [issue: I-09]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable segnala come rilievo il secondo periodo dell'articolo 9.4 sul pagamento a soggetto diverso o in Paese diverso.

**Pass se** &nbsp; compare il riferimento al pagamento su conto intestato a soggetto diverso oppure acceso in un Paese diverso

**Fail se** &nbsp; il punto non e' trattato.

*Non passa al judge:* fonte: bozza, art. 9.4 | gravita': alta

### B.14  [issue: I-09]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable indica come intervento la soppressione del secondo periodo dell'articolo 9.4.

**Pass se** &nbsp; compare una fra: «sopprimere», «eliminare», «espungere», «cancellare» riferita a quella previsione

**Fail se** &nbsp; l'intervento indicato consiste nel subordinare la previsione a condizioni ulteriori anziche' nella sua soppressione.

*Non passa al judge:* fonte: bozza, art. 9.4 | gravita': alta

### B.15  [issue: I-10]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che nella matrice l'autorizzazione e' attribuita al medesimo soggetto che propone la spesa.

**Pass se** &nbsp; compare una fra: «coincidenza fra proponente e autorizzante», «chi propone autorizza», «attribuita al medesimo soggetto che propone», «difetto di segregazione», «assenza di separazione dei ruoli»

**Fail se** &nbsp; il punto non e' trattato.

*Non passa al judge:* fonte: Allegato 1 | gravita': alta

### B.16  [issue: I-10]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable nomina entrambe le righe della matrice affette dal difetto: l'ospitalita' fino a euro 1.000,00 e la sponsorizzazione fino a euro 25.000,00.

**Pass se** &nbsp; compaiono entrambe le righe della matrice

**Fail se** &nbsp; e' nominata una sola delle due righe, oppure nessuna.

*Non passa al judge:* fonte: Allegato 1 | gravita': media

### B.17  [issue: I-11]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable segnala come rilievo la regolarizzazione successiva prevista dall'articolo 10.2.

**Pass se** &nbsp; compare il riferimento all'autorizzazione richiesta dopo l'operazione, oppure alla sanatoria entro trenta giorni

**Fail se** &nbsp; il punto non e' trattato.

*Non passa al judge:* fonte: bozza, art. 10.2 | gravita': alta

### B.18  [issue: I-11]  [tipo: assenza]  [judge]

**Verifica** &nbsp; il deliverable non indica come intervento la sola riduzione del termine di trenta giorni.

**Pass se** &nbsp; non compare l'indicazione di ridurre il termine mantenendo la possibilita' di autorizzazione successiva

**Fail se** &nbsp; l'intervento indicato consiste nella riduzione del termine.

*Non passa al judge:* fonte: bozza, art. 10.2 | gravita': media

### B.19  [issue: I-12]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che l'ambito soggettivo della bozza e' piu' ristretto di quello del codice etico.

**Pass se** &nbsp; compare l'affermazione che la policy si applica ai soli dipendenti mentre il codice etico si rivolge anche a terzi

**Fail se** &nbsp; il punto non e' trattato.

*Non passa al judge:* fonte: bozza, art. 2; codice etico, art. 2 | gravita': alta

### B.20  [issue: I-12]  [tipo: assenza]  [judge]

**Verifica** &nbsp; il deliverable non afferma che l'estensione ai terzi e' assicurata dalle clausole contrattuali previste dall'articolo 9.2.

**Pass se** &nbsp; non compare l'affermazione che l'articolo 9.2 supplisca alla ristrettezza dell'ambito soggettivo

**Fail se** &nbsp; la clausola contrattuale dell'articolo 9.2 e' presentata come rimedio che elimina il rilievo sull'ambito soggettivo.

*Non passa al judge:* fonte: bozza, artt. 2 e 9.2 | gravita': media

### B.21  [issue: I-13]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che manca il divieto dei pagamenti di facilitazione.

**Pass se** &nbsp; compare una fra: «pagamenti di facilitazione», «facilitation payment», «pagamenti per accelerare attivita' di routine»

**Fail se** &nbsp; il punto non e' trattato.

*Non passa al judge:* fonte: bozza, testo integrale | gravita': alta

### B.22  [issue: I-14]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che manca il registro degli omaggi e delle ospitalita'.

**Pass se** &nbsp; compare una fra: «registro degli omaggi», «registro delle ospitalita'», «assenza di registrazione delle erogazioni»

**Fail se** &nbsp; il punto non e' trattato.

*Non passa al judge:* fonte: bozza, artt. 5, 6 e 14 | gravita': alta

### B.23  [issue: I-15]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che l'articolo 11.1 non garantisce la riservatezza dell'identita' del segnalante.

**Pass se** &nbsp; compare l'affermazione che l'identita' del segnalante viene comunicata a soggetti diversi da quelli competenti, oppure che la riservatezza non e' garantita

**Fail se** &nbsp; il punto non e' trattato.

*Non passa al judge:* fonte: bozza, art. 11.1; artt. 4 e 12 D.Lgs. 24/2023 | gravita': alta

### B.24  [issue: I-15]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che l'articolo 11.1 confligge con la procedura sulle segnalazioni in vigore.

**Pass se** &nbsp; compare il riferimento al contrasto fra l'articolo 11.1 e la procedura sulle segnalazioni, oppure fra il superiore gerarchico e l'ufficio autonomo dedicato

**Fail se** &nbsp; il conflitto con la procedura in vigore non e' rilevato.

*Non passa al judge:* fonte: procedura sulle segnalazioni, artt. 3 e 4 | gravita': alta

### B.25  [issue: I-15]  [tipo: assenza]  [judge]

**Verifica** &nbsp; il deliverable non afferma che il divieto di ritorsione dell'articolo 11.2 rende conforme il canale previsto dall'articolo 11.1.

**Pass se** &nbsp; non compare l'affermazione che l'articolo 11.2 sani il difetto del canale

**Fail se** &nbsp; il divieto di ritorsione e' presentato come elemento che rende conforme il canale.

*Non passa al judge:* fonte: bozza, art. 11.2 | gravita': media

### B.26  [issue: I-16]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable indica fra gli elementi mancanti l'Allegato 2 richiamato dall'articolo 7.3.

**Pass se** &nbsp; compare la richiesta dell'Allegato 2, del questionario di verifica sul beneficiario oppure del documento richiamato dall'articolo 7.3

**Fail se** &nbsp; la richiesta non compare.

*Non passa al judge:* fonte: bozza, art. 7.3; verbale del comitato | gravita': media

### B.27  [issue: I-16]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che la review non consente di esprimersi sulla tenuta complessiva del modello di organizzazione, gestione e controllo.

**Pass se** &nbsp; compare una fra: «non e' possibile esprimersi», «non consente di esprimersi», «esula dalla presente review», «non e' valutabile sulla base del fascicolo» riferito al modello

**Fail se** &nbsp; il deliverable esprime una valutazione sulla tenuta complessiva del modello.

*Non passa al judge:* fonte: composizione del fascicolo | gravita': alta

### B.28  [issue: I-09]  [tipo: assenza]  [judge]

**Verifica** &nbsp; sovra-segnalazione: il deliverable non indica fra le richieste della direzione commerciale accoglibili quella relativa al pagamento su conto di soggetto diverso.

**Pass se** &nbsp; quella richiesta non compare fra quelle accoglibili

**Fail se** &nbsp; la richiesta e' indicata come accoglibile.

*Non passa al judge:* fonte: messaggio della direzione commerciale; bozza, art. 9.4 | gravita': alta

### B.29  [issue: I-01]  [tipo: assenza]  [judge]

**Verifica** &nbsp; sovra-segnalazione: il deliverable non presenta la misura della soglia di euro 150,00 come rilievo autonomo.

**Pass se** &nbsp; la misura della soglia non compare fra i rilievi

**Fail se** &nbsp; il valore di euro 150,00 e' segnalato come inadeguato in se'.

*Non passa al judge:* fonte: bozza, art. 5.2 | gravita': alta

### B.30  [issue: I-16]  [tipo: assenza]  [judge]

**Verifica** &nbsp; sovra-segnalazione: il deliverable non segnala come rilievo il divieto di omaggi in denaro dell'articolo 5.1.

**Pass se** &nbsp; il divieto di omaggi in denaro non compare fra i rilievi

**Fail se** &nbsp; l'articolo 5.1 e' segnalato come rilievo.

*Non passa al judge:* fonte: bozza, art. 5.1 | gravita': media

### B.31  [issue: I-16]  [tipo: assenza]  [judge]

**Verifica** &nbsp; sovra-segnalazione: il deliverable non segnala come insufficiente la formazione prevista dall'articolo 12.

**Pass se** &nbsp; la formazione non compare fra i rilievi

**Fail se** &nbsp; la periodicita' o il contenuto della formazione sono segnalati come rilievo.

*Non passa al judge:* fonte: bozza, art. 12; verbale del comitato | gravita': media

### B.32  [issue: I-16]  [tipo: assenza]  [judge]

**Verifica** &nbsp; sovra-segnalazione: il deliverable non segnala come mancante il richiamo al sistema disciplinare.

**Pass se** &nbsp; il sistema disciplinare non compare fra gli elementi mancanti

**Fail se** &nbsp; l'assenza del richiamo al sistema disciplinare e' segnalata come rilievo.

*Non passa al judge:* fonte: bozza, art. 13 | gravita': media

### B.33  [issue: I-14]  [tipo: assenza]  [judge]

**Verifica** &nbsp; sovra-segnalazione: il deliverable non segnala come inadeguato il periodo di conservazione di dieci anni previsto dall'articolo 14.

**Pass se** &nbsp; il periodo di conservazione non compare fra i rilievi

**Fail se** &nbsp; la durata della conservazione e' segnalata come inadeguata.

*Non passa al judge:* fonte: bozza, art. 14 | gravita': media

### B.34  [issue: I-16]  [tipo: assenza]  [judge]

**Verifica** &nbsp; sovra-segnalazione: il deliverable non segnala come rilievo la disciplina delle erogazioni liberali dell'articolo 8.

**Pass se** &nbsp; le erogazioni liberali non compaiono fra i rilievi

**Fail se** &nbsp; l'articolo 8 e' segnalato come rilievo.

*Non passa al judge:* fonte: bozza, art. 8; Allegato 1 | gravita': media

### B.35  [issue: I-16]  [tipo: assenza]  [judge]

**Verifica** &nbsp; sovra-segnalazione: il deliverable non indica come accoglibile la richiesta di elevare dal cinque per cento al nove per cento il limite al compenso degli intermediari.

**Pass se** &nbsp; quella richiesta non compare fra quelle accoglibili

**Fail se** &nbsp; l'elevazione del limite e' indicata come accoglibile.

*Non passa al judge:* fonte: messaggio della direzione commerciale; bozza, art. 9.3 | gravita': alta

### B.36  [issue: I-05]  [tipo: assenza]  [judge]

**Verifica** &nbsp; simmetria del controllo: il deliverable non afferma che l'ospitalita' e' vietata in quanto tale dalla bozza.

**Pass se** &nbsp; non compare l'affermazione che la bozza vieti l'ospitalita'

**Fail se** &nbsp; l'ospitalita' e' presentata come vietata dalla bozza.

*Non passa al judge:* fonte: bozza, art. 6.1 | gravita': media

### B.37  [issue: I-16]  [tipo: assenza]  [judge]

**Verifica** &nbsp; divieto di presunzione dell'esito: il deliverable non afferma che il consiglio di amministrazione approvera' o respingera' la bozza.

**Pass se** &nbsp; non compare alcuna previsione sull'esito della seduta del consiglio

**Fail se** &nbsp; l'esito della deliberazione del consiglio e' presentato come noto.

*Non passa al judge:* fonte: verbale del comitato controllo e rischi | gravita': media

## C. Soglie, termini e date

### C.1  [issue: I-01]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable indica euro 150,00 come limite per singola erogazione previsto dall'articolo 5.2.

**Pass se** &nbsp; compare «150» riferito al limite per singola erogazione

**Fail se** &nbsp; e' indicato un importo diverso, oppure il limite non e' indicato.

*Non passa al judge:* fonte: bozza, art. 5.2 | gravita': media

### C.2  [issue: I-06]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable indica euro 25.000,00 come soglia oltre la quale scatta la verifica sul beneficiario.

**Pass se** &nbsp; compare «25.000» come soglia della verifica

**Fail se** &nbsp; e' indicato un importo diverso, oppure la soglia non e' indicata.

*Non passa al judge:* fonte: bozza, art. 7.3 | gravita': media

### C.3  [issue: I-10]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable indica euro 1.000,00 come soglia dell'ospitalita' autorizzata dal proponente.

**Pass se** &nbsp; compare «1.000» come soglia dell'ospitalita'

**Fail se** &nbsp; e' indicato un importo diverso, oppure la soglia non e' indicata.

*Non passa al judge:* fonte: Allegato 1 | gravita': media

### C.4  [issue: I-11]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable indica trenta giorni come termine della regolarizzazione successiva prevista dall'articolo 10.2.

**Pass se** &nbsp; compare «trenta giorni» oppure «30 giorni» riferito alla regolarizzazione successiva

**Fail se** &nbsp; e' indicato un termine diverso, oppure il termine non e' indicato.

*Non passa al judge:* fonte: bozza, art. 10.2 | gravita': bassa

### C.5  [issue: I-16]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable indica il 3 dicembre 2032 come data della seduta del consiglio di amministrazione entro cui la review deve essere utilizzabile.

**Pass se** &nbsp; compare «3 dicembre 2032» oppure «03/12/2032»

**Fail se** &nbsp; e' indicata una data diversa, oppure la data non e' indicata.

*Non passa al judge:* fonte: verbale del comitato controllo e rischi | gravita': media

