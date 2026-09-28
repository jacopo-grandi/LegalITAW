# WF2-036 — Rubrica atomizzata

Forma a campi somministrata al judge e alla verifica meccanica. Generato da `source/gen/build_rubric_036.py` insieme a `private/rubric.json`: non modificare a mano.

Issue di merito: 17. Criteri atomici: 58, di cui 12 a verifica meccanica e 46 al judge.

---

## A. Forma dell'output  (interamente verifica meccanica)

### A.1  [issue: A]  [tipo: valore]  [verifica meccanica]

**Verifica** — sono stati prodotti due file, denominati contratto_redline.docx e nota_delle_modifiche.md.

**Pass se** — entrambi i file esistono e portano i nomi indicati

**Fail se** — manca uno dei due file oppure il nome è diverso.

<small>—— non passa al judge —— Fonte: response_template.md · Gravità: bassa</small>

### A.2  [issue: A]  [tipo: struttura]  [verifica meccanica]

**Verifica** — il file contratto_redline.docx contiene almeno una revisione tracciata di inserimento.

**Pass se** — nel documento è presente almeno un elemento w:ins

**Fail se** — il documento non contiene alcun inserimento tracciato.

<small>—— non passa al judge —— Fonte: response_template.md · Gravità: alta</small>

### A.3  [issue: A]  [tipo: struttura]  [verifica meccanica]

**Verifica** — il file contratto_redline.docx contiene almeno una revisione tracciata di cancellazione.

**Pass se** — nel documento è presente almeno un elemento w:del

**Fail se** — il documento non contiene alcuna cancellazione tracciata.

<small>—— non passa al judge —— Fonte: response_template.md · Gravità: alta</small>

### A.4  [issue: I-17]  [tipo: struttura]  [verifica meccanica]

**Verifica** — il file contratto_redline.docx non contiene alcuna revisione tracciata all'interno degli articoli 3, 4, 12, 13, 14, 15 e 16.

**Pass se** — nessun elemento w:ins e nessun elemento w:del ricade fra l'intestazione dell'articolo 3 e quella dell'articolo 5, né fra l'intestazione dell'articolo 12 e la fine del documento

**Fail se** — una revisione tracciata ricade in uno degli articoli esclusi dall'incarico.

<small>—— non passa al judge —— Fonte: 01_task.md, terzo capoverso · Gravità: alta</small>

### A.5  [issue: A]  [tipo: valore]  [verifica meccanica]

**Verifica** — il file nota_delle_modifiche.md non supera 2.200 parole.

**Pass se** — il conteggio delle parole non supera 2.200

**Fail se** — il conteggio supera 2.200 parole.

<small>—— non passa al judge —— Fonte: response_template.md · Gravità: bassa</small>

### A.6  [issue: A]  [tipo: struttura]  [verifica meccanica]

**Verifica** — la nota contiene, nell'ordine, otto sezioni intitolate: Sintesi delle modifiche; Titolarità dei Risultati; Componenti di terze parti e software a codice aperto; Deposito del codice sorgente; Verifica dell'uso del Software; Responsabilità per pretese di terzi; Affermazioni del fornitore da non dare per buone; Che cosa non è determinabile allo stato e che cosa serve.

**Pass se** — le otto intestazioni compaiono tutte e nell'ordine indicato

**Fail se** — manca una intestazione oppure l'ordine è diverso.

<small>—— non passa al judge —— Fonte: response_template.md · Gravità: bassa</small>

### A.7  [issue: A]  [tipo: struttura]  [verifica meccanica]

**Verifica** — ogni riga della tabella della sezione 1 della nota riporta l'articolo o la definizione su cui si è intervenuti e la ragione della modifica.

**Pass se** — nessuna riga della tabella della sezione 1 ha vuota la colonna dell'articolo o quella della ragione

**Fail se** — almeno una riga non riporta l'articolo oppure non riporta la ragione.

<small>—— non passa al judge —— Fonte: response_template.md · Gravità: alta</small>

### A.8  [issue: A]  [tipo: assenza]  [verifica meccanica]

**Verifica** — il deliverable non contiene riferimenti normativi, giurisprudenziali o di licenza diversi da quelli elencati nella tabella dell'elenco chiuso di 03_legal_sources.md.

**Pass se** — tutti i riferimenti presenti compaiono nell'elenco chiuso

**Fail se** — compare un riferimento estraneo all'elenco chiuso.

<small>—— non passa al judge —— Fonte: 03_legal_sources.md · Gravità: alta</small>

---

## B. Merito

Fascicolo ex ante alla data di riferimento del 16 ottobre 2028: la bozza è stata trasmessa, nulla è stato sottoscritto, il contratto del 2026 è quello che regola il rapporto e il Software è in esercizio. Il deliverable è un redline circoscritto al perimetro indicato nell'incarico più una nota delle modifiche. I criteri riguardano le modifiche introdotte nel testo e le ragioni esposte nella nota; non riguardano la convenienza economica del rinnovo né l'esito di una eventuale contestazione. Dove il criterio parla di «testo inserito» si riferisce alle parti del redline marcate come inserimento; dove parla di «testo cancellato», alle parti marcate come cancellazione.

### B.1  [issue: I-01]  [tipo: presenza]  [judge]

**Verifica** — il redline sostituisce il primo comma dell'articolo 6 con una clausola che attribuisce al Cliente i diritti di utilizzazione economica sui Risultati in via esclusiva.

**Pass se** — compare una fra le formulazioni seguenti:
- nel testo inserito compare una fra: «il Cliente acquista … in via esclusiva … i diritti di utilizzazione economica»
- «sono trasferiti al Cliente … in via esclusiva»
- «il Cliente è titolare esclusivo dei diritti di utilizzazione economica sui Risultati»
- «cessione al Cliente dei diritti di utilizzazione economica sui Risultati, in via esclusiva»

**Fail se** — il primo comma dell'articolo 6 resta invariato, oppure il testo inserito attribuisce al Cliente una licenza non esclusiva.

**Indifferente** — la scelta fra la tecnica della cessione dei diritti e quella della licenza esclusiva perpetua, purché il testo inserito attribuisca l'esclusiva.

<small>—— non passa al judge —— Fonte: documento 01, art. 6, comma 1 · Gravità: alta</small>

### B.2  [issue: I-01]  [tipo: presenza]  [judge]

**Verifica** — il redline attribuisce al Cliente, sui Componenti Preesistenti integrati nel Software, una licenza perpetua e trasferibile.

**Pass se** — nel testo inserito compaiono, riferiti alla licenza sui Componenti Preesistenti, sia il carattere perpetuo (o irrevocabile, o senza limiti di tempo) sia la trasferibilità (o la facoltà di concedere in sublicenza)

**Fail se** — la licenza sui Componenti Preesistenti resta a tempo determinato, oppure resta non trasferibile, oppure il punto non è trattato.

<small>—— non passa al judge —— Fonte: documento 01, art. 6, comma 2 · Gravità: alta</small>

### B.3  [issue: I-01]  [tipo: assenza]  [judge]

**Verifica** — la nota delle modifiche non afferma che il testo attuale dell'articolo 6 attribuisce al Cliente la titolarità dei Risultati.

**Pass se** — non compare l'affermazione che il codice sviluppato sia già del Cliente in base al testo trasmesso

**Fail se** — la nota recepisce l'affermazione del referente commerciale secondo cui l'articolo 6 dice espressamente che il codice è del Cliente.

<small>—— non passa al judge —— Fonte: documento 06, punto 1 · Gravità: alta</small>

### B.4  [issue: I-02]  [tipo: presenza]  [judge]

**Verifica** — il redline sottrae il modulo motore-di-riconciliazione alla qualificazione di Componente Preesistente.

**Pass se** — compare una fra le formulazioni seguenti:
- nel testo inserito il modulo motore-di-riconciliazione è escluso nominativamente dai Componenti Preesistenti
- nel testo inserito la definizione di Componenti Preesistenti è ancorata al completamento della realizzazione anteriormente alla Data di Inizio

**Fail se** — la definizione di Componenti Preesistenti resta invariata e il modulo non è escluso.

<small>—— non passa al judge —— Fonte: documento 01, art. 1; documento 03 · Gravità: alta</small>

### B.5  [issue: I-02]  [tipo: attribuzione]  [judge]

**Verifica** — la nota delle modifiche riconduce il rilievo sul modulo motore-di-riconciliazione al confronto fra la Data di Inizio del Progetto e la data del contratto d'opera con lo sviluppatore autonomo.

**Pass se** — il rilievo è agganciato a entrambi gli elementi: la Data di Inizio del Progetto e la data del contratto d'opera

**Fail se** — il rilievo è agganciato a uno solo dei due elementi, oppure a nessuno.

<small>—— non passa al judge —— Fonte: documento 01, premessa d); documento 05 · Gravità: alta</small>

### B.6  [issue: I-03]  [tipo: presenza]  [judge]

**Verifica** — il redline introduce una dichiarazione o garanzia del Fornitore sull'acquisizione per iscritto dei diritti dai soggetti che hanno partecipato alla realizzazione dei Risultati e che non sono suoi dipendenti.

**Pass se** — nel testo inserito compare l'obbligo o la garanzia relativa all'acquisizione per iscritto dei diritti dai collaboratori non dipendenti

**Fail se** — il punto non è trattato nel redline.

<small>—— non passa al judge —— Fonte: artt. 12-bis e 110 l. 633/1941 · Gravità: alta</small>

### B.7  [issue: I-03]  [tipo: presenza]  [judge]

**Verifica** — il redline obbliga il Fornitore a consegnare al Cliente copia degli atti scritti di trasmissione dei diritti.

**Pass se** — nel testo inserito compare l'obbligo di consegna, esibizione o trasmissione di copia di quegli atti

**Fail se** — l'obbligo di consegna non compare.

<small>—— non passa al judge —— Fonte: art. 110 l. 633/1941 · Gravità: media</small>

### B.8  [issue: I-04]  [tipo: presenza]  [judge]

**Verifica** — il redline circoscrive la clausola sui miglioramenti e i suggerimenti provenienti dal Cliente, escludendone le informazioni riservate e la proprietà intellettuale preesistente del Cliente.

**Pass se** — nel testo inserito compare l'esclusione delle informazioni riservate del Cliente e della sua proprietà intellettuale preesistente

**Fail se** — il quinto comma dell'articolo 6 resta invariato, oppure l'esclusione non compare.

**Indifferente** — la conservazione di una licenza non esclusiva a favore del Fornitore sulle sole segnalazioni di difetto.

<small>—— non passa al judge —— Fonte: documento 01, art. 6, comma 5 · Gravità: media</small>

### B.9  [issue: I-05]  [tipo: presenza]  [judge]

**Verifica** — il redline estende la garanzia del terzo comma dell'articolo 7 agli obblighi che si attivano per effetto dell'uso, dell'accesso o dell'interazione con il Software da parte di utenti attraverso una rete.

**Pass se** — nel testo inserito compare, accanto alla distribuzione, almeno uno fra: l'uso, l'accesso, l'interazione attraverso una rete, la messa a disposizione via rete

**Fail se** — la garanzia resta riferita alla sola distribuzione a terzi del Software.

<small>—— non passa al judge —— Fonte: documento 01, art. 7, comma 3; AGPL-3.0, sezione 13 · Gravità: alta</small>

### B.10  [issue: I-05]  [tipo: attribuzione]  [judge]

**Verifica** — la nota delle modifiche riconduce il rilievo sulla garanzia dell'articolo 7 al componente melograno-reportd e alla licenza AGPL-3.0.

**Pass se** — il rilievo è agganciato sia al nome del componente melograno-reportd sia alla licenza AGPL-3.0

**Fail se** — il rilievo è agganciato a uno solo dei due elementi, oppure a nessuno.

<small>—— non passa al judge —— Fonte: documento 03, riga melograno-reportd · Gravità: alta</small>

### B.11  [issue: I-05]  [tipo: assenza]  [judge]

**Verifica** — la nota delle modifiche non afferma che i componenti a codice aperto integrati nel Software sono tutti a licenza permissiva.

**Pass se** — non compare l'affermazione che tutte le licenze dei componenti siano permissive

**Fail se** — la nota recepisce l'affermazione del referente commerciale secondo cui i componenti sono tutti a licenza permissiva.

<small>—— non passa al judge —— Fonte: documento 06, punto 3 · Gravità: alta</small>

### B.12  [issue: I-06]  [tipo: presenza]  [judge]

**Verifica** — il redline introduce una dichiarazione o garanzia specifica riferita al componente melograno-reportd.

**Pass se** — nel testo inserito il componente melograno-reportd è nominato in una dichiarazione o garanzia del Fornitore

**Fail se** — nel redline non compare alcuna clausola specifica su quel componente.

<small>—— non passa al judge —— Fonte: documento 03 · Gravità: alta</small>

### B.13  [issue: I-06]  [tipo: presenza]  [judge]

**Verifica** — il redline obbliga il Fornitore a sostituire o a rimuovere il componente a proprie spese qualora l'obbligo di messa a disposizione del codice sorgente risulti attivato.

**Pass se** — nel testo inserito compare l'obbligo di sostituzione o di rimozione del componente a spese del Fornitore

**Fail se** — l'obbligo di sostituzione o rimozione non compare.

<small>—— non passa al judge —— Fonte: documento 01, art. 7 · Gravità: alta</small>

### B.14  [issue: I-07]  [tipo: presenza]  [judge]

**Verifica** — il redline subordina alla preventiva approvazione scritta del Cliente la modifica dei Componenti di Terze Parti e dell'Allegato B.

**Pass se** — compare una fra le formulazioni seguenti:
- nel testo inserito compare una fra: «previa approvazione scritta del Cliente»
- «previo consenso scritto del Cliente»
- «subordinata all'accettazione scritta del Cliente»

**Fail se** — il quarto comma dell'articolo 7 resta invariato, oppure la modifica resta possibile senza il consenso del Cliente.

**Indifferente** — l'introduzione di un termine di preavviso, purché il consenso sia richiesto.

<small>—— non passa al judge —— Fonte: documento 01, art. 7, comma 4 · Gravità: alta</small>

### B.15  [issue: I-08]  [tipo: presenza]  [judge]

**Verifica** — il redline elenca nel contratto gli eventi che consentono il rilascio del Materiale Depositato, in luogo del rinvio all'Accordo di Deposito.

**Pass se** — nel testo inserito compare un elenco di eventi di rilascio

**Fail se** — il secondo comma dell'articolo 8 resta un rinvio all'Accordo di Deposito.

<small>—— non passa al judge —— Fonte: documento 01, art. 8, comma 2; documento 04, art. 7 · Gravità: alta</small>

### B.16  [issue: I-08]  [tipo: presenza]  [judge]

**Verifica** — il redline comprende fra gli eventi di rilascio l'inadempimento del Fornitore agli obblighi di manutenzione o di rimozione dei difetti.

**Pass se** — nel testo inserito compare, fra gli eventi di rilascio, l'inadempimento agli obblighi di manutenzione, di assistenza o di rimozione dei difetti

**Fail se** — l'elenco degli eventi di rilascio non comprende l'inadempimento.

<small>—— non passa al judge —— Fonte: documento 04, art. 7 · Gravità: alta</small>

### B.17  [issue: I-09]  [tipo: presenza]  [judge]

**Verifica** — il redline prevede che il rilascio del Materiale Depositato avvenga su richiesta del solo Cliente.

**Pass se** — compare una fra le formulazioni seguenti:
- nel testo inserito compare una fra: «su richiesta del solo Cliente»
- «su richiesta scritta del Cliente», riferita al rilascio
- «a prima richiesta del Cliente»

**Fail se** — il rilascio resta subordinato alla richiesta congiunta delle Parti.

**Indifferente** — la previsione di una facoltà di opposizione del Fornitore davanti a un terzo.

<small>—— non passa al judge —— Fonte: documento 04, art. 8 · Gravità: alta</small>

### B.18  [issue: I-09]  [tipo: assenza]  [judge]

**Verifica** — la nota delle modifiche non presenta il ricorso all'autorità giudiziaria come rimedio equivalente al rilascio su richiesta del Cliente.

**Pass se** — non compare l'affermazione che l'ordine dell'autorità giudiziaria renda comunque effettivo il deposito

**Fail se** — la nota conclude che, potendo il Cliente rivolgersi al giudice, la clausola dell'Accordo di Deposito non richiede modifiche.

<small>—— non passa al judge —— Fonte: documento 04, art. 8 · Gravità: media</small>

### B.19  [issue: I-10]  [tipo: presenza]  [judge]

**Verifica** — il redline lega l'aggiornamento del Materiale Depositato a ogni rilascio in produzione.

**Pass se** — nel testo inserito l'aggiornamento è riferito a ogni rilascio in produzione, a ogni nuova versione rilasciata o a ogni versione messa in esercizio

**Fail se** — l'aggiornamento resta a periodicità annuale.

**Indifferente** — l'indicazione del numero di giorni entro cui l'aggiornamento va eseguito.

<small>—— non passa al judge —— Fonte: documento 01, art. 8, comma 3 · Gravità: alta</small>

### B.20  [issue: I-10]  [tipo: presenza]  [judge]

**Verifica** — il redline estende il Materiale Depositato agli script di compilazione o di distribuzione e all'elenco delle dipendenze software di terzi.

**Pass se** — nel testo inserito compaiono entrambi gli elementi: gli script di compilazione o di distribuzione e l'elenco delle dipendenze

**Fail se** — il perimetro del Materiale Depositato resta invariato, oppure è esteso a uno solo dei due elementi.

**Indifferente** — l'estensione anche alla documentazione tecnica di esercizio.

<small>—— non passa al judge —— Fonte: documento 04, art. 5, comma 2 · Gravità: alta</small>

### B.21  [issue: I-10]  [tipo: assenza]  [judge]

**Verifica** — la nota delle modifiche non afferma che il codice sorgente depositato è aggiornato.

**Pass se** — non compare l'affermazione che il deposito sia aggiornato o regolarmente aggiornato

**Fail se** — la nota recepisce l'affermazione del referente commerciale secondo cui il sorgente viene aggiornato regolarmente.

<small>—— non passa al judge —— Fonte: documento 06, punto 2; documento 04, art. 4, comma 3 · Gravità: alta</small>

### B.22  [issue: I-11]  [tipo: presenza]  [judge]

**Verifica** — il redline introduce un preavviso scritto per l'esercizio della verifica dell'uso del Software.

**Pass se** — nel testo inserito compare un preavviso scritto, con o senza indicazione del numero di giorni

**Fail se** — la verifica resta esercitabile senza preavviso.

<small>—— non passa al judge —— Fonte: documento 01, art. 9, comma 1 · Gravità: alta</small>

### B.23  [issue: I-11]  [tipo: presenza]  [judge]

**Verifica** — il redline impone che la verifica sia eseguita da un terzo indipendente vincolato alla riservatezza.

**Pass se** — nel testo inserito compaiono entrambi gli elementi: l'indipendenza del verificatore rispetto al Fornitore e il suo obbligo di riservatezza verso il Cliente

**Fail se** — il verificatore resta designato dal Fornitore, oppure non è vincolato alla riservatezza, oppure il punto non è trattato.

**Indifferente** — il divieto che il verificatore sia concorrente del Cliente e il limite di frequenza.

<small>—— non passa al judge —— Fonte: documento 01, art. 9, comma 1 · Gravità: alta</small>

### B.24  [issue: I-11]  [tipo: presenza]  [judge]

**Verifica** — il redline esclude dall'oggetto della verifica l'accesso al codice sorgente e ai dati del Cliente.

**Pass se** — nel testo inserito compare l'esclusione dell'accesso al codice o ai dati del Cliente, oppure la circoscrizione dell'oggetto della verifica ai soli dati di utilizzazione del Software

**Fail se** — l'accesso ai sistemi e alle registrazioni del Cliente resta senza limiti di oggetto.

<small>—— non passa al judge —— Fonte: documento 01, art. 9, comma 2; documento 07, punto 5 · Gravità: alta</small>

### B.25  [issue: I-12]  [tipo: presenza]  [judge]

**Verifica** — il redline attribuisce al Cliente il diritto di ottenere periodicamente l'elenco aggiornato dei Componenti di Terze Parti con le rispettive licenze.

**Pass se** — nel testo inserito compare un obbligo del Fornitore di consegnare o mettere a disposizione l'elenco aggiornato dei componenti con le licenze

**Fail se** — il diritto del Cliente non compare.

**Indifferente** — la richiesta di un'attestazione di conformità e l'estensione alle dipendenze transitive.

<small>—— non passa al judge —— Fonte: documento 01, artt. 7 e 9 · Gravità: media</small>

### B.26  [issue: I-13]  [tipo: presenza]  [judge]

**Verifica** — il redline sopprime o rende inoperante, per i Componenti di Terze Parti elencati nell'Allegato B, l'eccezione alla manleva.

**Pass se** — compare una fra le formulazioni seguenti:
- il testo cancellato comprende la lettera e) del terzo comma dell'articolo 11
- nel testo inserito compare la disapplicazione dell'eccezione per i componenti elencati nell'Allegato B

**Fail se** — l'eccezione per i Componenti di Terze Parti resta operante.

<small>—— non passa al judge —— Fonte: documento 01, art. 11, comma 3, lettera e) · Gravità: alta</small>

### B.27  [issue: I-14]  [tipo: presenza]  [judge]

**Verifica** — il redline impone che la modifica o la sostituzione del Software assicuri funzionalità e prestazioni non inferiori a quelle descritte nell'Allegato A.

**Pass se** — compare una fra le formulazioni seguenti:
- nel testo inserito compare una fra: «equivalenza funzionale»
- «funzionalità e prestazioni non inferiori»
- «senza riduzione delle funzionalità»

**Fail se** — il quarto comma dell'articolo 11 resta invariato quanto all'equivalenza.

**Indifferente** — l'attribuzione al Cliente della facoltà di rifiutare la sostituzione non equivalente.

<small>—— non passa al judge —— Fonte: documento 01, art. 11, comma 4 · Gravità: alta</small>

### B.28  [issue: I-14]  [tipo: presenza]  [judge]

**Verifica** — il redline sostituisce il rimborso dei soli canoni del periodo residuo con un ristoro più ampio.

**Pass se** — nel testo inserito il ristoro comprende almeno uno fra: il corrispettivo di sviluppo, i canoni corrisposti in un periodo pregresso, i costi di migrazione

**Fail se** — il rimborso resta limitato ai canoni corrisposti per il periodo residuo.

<small>—— non passa al judge —— Fonte: documento 01, art. 11, comma 4 · Gravità: alta</small>

### B.29  [issue: I-15]  [tipo: presenza]  [judge]

**Verifica** — il redline attribuisce al Cliente il diritto di partecipare alla difesa nei confronti del terzo.

**Pass se** — nel testo inserito compare il diritto del Cliente di partecipare alla difesa, di nominare propri difensori o di essere informato del suo andamento

**Fail se** — il controllo della difesa resta esclusivo del Fornitore senza alcuna facoltà del Cliente.

<small>—— non passa al judge —— Fonte: documento 01, art. 11, comma 5 · Gravità: media</small>

### B.30  [issue: I-15]  [tipo: presenza]  [judge]

**Verifica** — il redline vieta al Fornitore di definire la pretesa in via transattiva quando la transazione comporti ammissioni di responsabilità od oneri a carico del Cliente, senza il consenso scritto di quest'ultimo.

**Pass se** — nel testo inserito compare il divieto di transigere senza il consenso scritto del Cliente nei casi indicati

**Fail se** — il potere di transigere resta libero.

<small>—— non passa al judge —— Fonte: documento 01, art. 11, comma 5 · Gravità: media</small>

### B.31  [issue: I-16]  [tipo: presenza]  [judge]

**Verifica** — la nota delle modifiche afferma che il fascicolo non contiene la distinta delle dipendenze transitive né la documentazione dell'architettura di distribuzione.

**Pass se** — compare una fra le formulazioni seguenti:
- compare una fra: «non è possibile stabilire»
- «non è possibile verificare»
- «il fascicolo non contiene»
- «resta da verificare»
- «non si può escludere»
- riferita alle dipendenze transitive o all'architettura di distribuzione

**Fail se** — il punto non è trattato, oppure la nota afferma che l'elenco dell'Allegato B è completo.

<small>—— non passa al judge —— Fonte: documento 03; documento 02, punto A.3 · Gravità: media</small>

### B.32  [issue: I-16]  [tipo: presenza]  [judge]

**Verifica** — la nota delle modifiche indica fra le informazioni da acquisire la distinta completa delle dipendenze software.

**Pass se** — compare la richiesta della distinta completa, dell'elenco completo o delle dipendenze transitive

**Fail se** — la richiesta non compare.

<small>—— non passa al judge —— Fonte: documento 03 · Gravità: media</small>

### B.33  [issue: I-01]  [tipo: assenza]  [judge]

**Verifica** — simmetria del controllo: la nota non afferma che il testo attuale del contratto non presenta esposizioni sulla titolarità dei Risultati.

**Pass se** — non compare l'affermazione che sulla titolarità non vi siano rilievi da muovere

**Fail se** — la nota conclude che sulla titolarità il testo è soddisfacente.

<small>—— non passa al judge —— Fonte: documento 01, art. 6 · Gravità: alta</small>

### B.34  [issue: I-05]  [tipo: assenza]  [judge]

**Verifica** — sovra-segnalazione: la nota non segnala come rischio di contaminazione il componente quadrifoglio-orm.

**Pass se** — il componente quadrifoglio-orm non compare fra i componenti che espongono il Cliente a obblighi di messa a disposizione del codice sorgente

**Fail se** — il componente quadrifoglio-orm è segnalato come rischio di contaminazione.

**Indifferente** — la menzione dell'obbligo di conservare l'avviso di copyright.

<small>—— non passa al judge —— Fonte: documento 03; MIT License · Gravità: alta</small>

### B.35  [issue: I-05]  [tipo: assenza]  [judge]

**Verifica** — sovra-segnalazione: la nota non segnala come rischio per il Cliente la concessione di licenza di brevetto della licenza applicabile al componente tessitura-http.

**Pass se** — la concessione di licenza di brevetto non compare fra i rischi o le esposizioni del Cliente

**Fail se** — la concessione di licenza di brevetto è presentata come rischio o come esposizione del Cliente.

<small>—— non passa al judge —— Fonte: documento 03; Apache-2.0, sezione 3 · Gravità: alta</small>

### B.36  [issue: I-05]  [tipo: assenza]  [judge]

**Verifica** — sovra-segnalazione: la nota non segnala come rischio di contaminazione il componente vetrata-charts.

**Pass se** — il componente vetrata-charts non compare fra i componenti che espongono il Cliente a obblighi di messa a disposizione del codice sorgente

**Fail se** — il componente vetrata-charts è segnalato come rischio di contaminazione.

**Indifferente** — la menzione degli obblighi di avviso.

<small>—— non passa al judge —— Fonte: documento 03; LGPL-2.1, sezioni 5 e 6 · Gravità: alta</small>

### B.37  [issue: I-05]  [tipo: assenza]  [judge]

**Verifica** — sovra-segnalazione: la nota non segnala come rischio di contaminazione il componente ferrobatte-build.

**Pass se** — il componente ferrobatte-build non compare fra i componenti che espongono il Cliente a obblighi di messa a disposizione del codice sorgente

**Fail se** — il componente ferrobatte-build è segnalato come rischio di contaminazione.

<small>—— non passa al judge —— Fonte: documento 03; GPL-2.0, sezione 0 · Gravità: alta</small>

### B.38  [issue: I-01]  [tipo: assenza]  [judge]

**Verifica** — sovra-segnalazione: la nota non segnala come limite alla titolarità del Cliente la clausola che fa salvo il diritto degli autori di essere riconosciuti tali.

**Pass se** — quella clausola non compare fra i rilievi né fra le modifiche proposte

**Fail se** — la clausola sul diritto di essere riconosciuti autori è segnalata come limite alla titolarità oppure ne è proposta la soppressione.

<small>—— non passa al judge —— Fonte: documento 01, art. 6, comma 6; art. 22 l. 633/1941 · Gravità: media</small>

### B.39  [issue: I-05]  [tipo: assenza]  [judge]

**Verifica** — sovra-segnalazione: la nota non segnala come difetto la clausola per cui il Cliente non acquisisce sui Componenti di Terze Parti diritti diversi e ulteriori rispetto a quelli concessi dalle rispettive licenze.

**Pass se** — quella clausola non compare fra i rilievi né fra le modifiche proposte

**Fail se** — quella clausola è segnalata come difetto oppure ne è proposta la soppressione.

<small>—— non passa al judge —— Fonte: documento 01, art. 7, comma 1 · Gravità: media</small>

### B.40  [issue: I-01]  [tipo: assenza]  [judge]

**Verifica** — sovra-segnalazione: la nota non segnala come esposizione la subordinazione dell'acquisto dei diritti all'integrale pagamento del corrispettivo.

**Pass se** — la subordinazione all'integrale pagamento non compare fra le esposizioni del Cliente

**Fail se** — la subordinazione all'integrale pagamento è presentata come esposizione.

**Indifferente** — la conservazione della clausola nel testo modificato.

<small>—— non passa al judge —— Fonte: documento 01, art. 6, comma 4 · Gravità: media</small>

### B.41  [issue: I-16]  [tipo: assenza]  [judge]

**Verifica** — divieto di presunzione dell'esito: la nota non afferma che il Cliente è già in violazione della licenza applicabile al componente melograno-reportd.

**Pass se** — non compare l'affermazione che la violazione si sia già verificata

**Fail se** — la nota afferma che il Cliente è in violazione, oppure che non lo è in alcun caso.

**Indifferente** — l'indicazione del rischio come possibile e da verificare.

<small>—— non passa al judge —— Fonte: documento 03; AGPL-3.0, sezione 13 · Gravità: alta</small>

### B.42  [issue: I-17]  [tipo: assenza]  [judge]

**Verifica** — la nota non propone modifiche al massimale di responsabilità dell'articolo 12.

**Pass se** — l'articolo 12 non compare fra le clausole di cui si propone la modifica

**Fail se** — la nota propone di modificare il massimale dell'articolo 12.

**Indifferente** — la menzione dell'articolo 12 per dire che è fuori perimetro.

<small>—— non passa al judge —— Fonte: 01_task.md, terzo capoverso · Gravità: alta</small>

### B.43  [issue: I-17]  [tipo: assenza]  [judge]

**Verifica** — la nota non propone modifiche alla clausola di accettazione tacita del collaudo dell'articolo 4.

**Pass se** — l'articolo 4 non compare fra le clausole di cui si propone la modifica

**Fail se** — la nota propone di modificare il termine o il meccanismo di accettazione del collaudo.

**Indifferente** — la menzione dell'articolo 4 per dire che è fuori perimetro.

<small>—— non passa al judge —— Fonte: 01_task.md, terzo capoverso · Gravità: media</small>

### B.44  [issue: I-17]  [tipo: assenza]  [judge]

**Verifica** — la nota non propone modifiche alla clausola compromissoria dell'articolo 16.

**Pass se** — l'articolo 16 non compare fra le clausole di cui si propone la modifica

**Fail se** — la nota propone di modificare la clausola compromissoria o il foro.

**Indifferente** — la menzione dell'articolo 16 per dire che è fuori perimetro, e il richiamo dell'articolo 16 nel testo inserito all'articolo 8 come sede di accertamento dell'evento di rilascio.

<small>—— non passa al judge —— Fonte: 01_task.md, terzo capoverso · Gravità: media</small>

---

## C. Date e valori calcolati

### C.1  [issue: I-02]  [tipo: valore]  [verifica meccanica]

**Verifica** — la nota indica il 9 marzo 2026 come Data di Inizio del Progetto.

**Pass se** — compare «9 marzo 2026» oppure «09/03/2026» come Data di Inizio

**Fail se** — è indicata una data diversa, oppure la Data di Inizio non è indicata.

<small>—— non passa al judge —— Fonte: documento 01, premessa d) · Gravità: alta</small>

### C.2  [issue: I-02]  [tipo: valore]  [verifica meccanica]

**Verifica** — la nota indica il 4 maggio 2026 come data del contratto d'opera con lo sviluppatore autonomo.

**Pass se** — compare «4 maggio 2026» oppure «04/05/2026»

**Fail se** — è indicata una data diversa, oppure la data non è indicata.

<small>—— non passa al judge —— Fonte: documento 05 · Gravità: alta</small>

### C.3  [issue: I-02]  [tipo: presenza]  [judge]

**Verifica** — la nota afferma che la data del contratto d'opera è posteriore alla Data di Inizio del Progetto.

**Pass se** — compare una fra le formulazioni seguenti:
- compare, riferita al rapporto fra le due date, una fra: «posteriore»
- «successiva»
- «dopo l'avvio del Progetto»
- «a Progetto già iniziato»

**Fail se** — il rapporto fra le due date non è affermato, oppure è affermato in senso inverso.

<small>—— non passa al judge —— Fonte: documento 01, premessa d); documento 05 · Gravità: alta</small>

### C.4  [issue: I-10]  [tipo: valore]  [verifica meccanica]

**Verifica** — la nota indica il 16 febbraio 2027 come data dell'ultimo aggiornamento del Materiale Depositato.

**Pass se** — compare «16 febbraio 2027» oppure «16/02/2027»

**Fail se** — è indicata una data diversa, oppure la data non è indicata.

<small>—— non passa al judge —— Fonte: documento 04, art. 4, comma 3 · Gravità: alta</small>

### C.5  [issue: I-10]  [tipo: valore]  [verifica meccanica]

**Verifica** — la nota indica il 5 settembre 2028 come data di rilascio in produzione della versione 3.4.

**Pass se** — compare «5 settembre 2028» oppure «05/09/2028»

**Fail se** — è indicata una data diversa, oppure la data non è indicata.

<small>—— non passa al judge —— Fonte: documento 02, punto A.3 · Gravità: media</small>

### C.6  [issue: I-17]  [tipo: assenza]  [judge]

**Verifica** — la nota non presenta il 31 ottobre 2028 come termine di decadenza o come termine di legge.

**Pass se** — il 31 ottobre 2028 non compare qualificato come decadenza, come termine perentorio o come termine di legge

**Fail se** — la scadenza dell'offerta commerciale è presentata come decadenza o come termine di legge.

**Indifferente** — la menzione della scadenza come termine commerciale.

<small>—— non passa al judge —— Fonte: documento 06, punto 5 · Gravità: media</small>
