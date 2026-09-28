# WF2-092 - Gold standard

**Data di riferimento:** 5 novembre 2026. **Lato assistito:** Solmarino Software S.r.l.

## Esito operativo

Il fascicolo non regge una conclusione unica. Alcuni rilievi impediscono il rilascio del 26 novembre
2026, altri no; due posizioni restano aperte perché il fascicolo non contiene i documenti che
servono a chiuderle. Il canale di fornitura, e non il componente, decide quale obbligo si applica:
lo stesso pacchetto Apache produce conseguenze diverse sull'apparecchiatura e nel servizio in cloud.

## Rilievi che impediscono il rilascio

**Pianificatore corvenza-scheduler 4.2.1 - servizio in cloud.** L'inventario registra il pacchetto
come AGPL-3.0-only con modifiche locali; il responsabile sviluppo dichiara che la patch tocca tre
file ed è in produzione dal 14 settembre 2026. La scheda di prodotto e la stessa nota interna
documentano che il pianificatore è raggiunto dagli utenti del cliente attraverso il portale e
attraverso l'interfaccia programmatica che due clienti usano dai propri sistemi. Ne segue l'obbligo
di offerta del codice sorgente agli utenti remoti della versione modificata, con messa a
disposizione del sorgente su server di rete. L'assenza di consegna di un eseguibile non esclude
l'obbligo: riguarda un presupposto diverso. Chiude: responsabile sviluppo piattaforma, con
verifica della direzione tecnica.

**Componente aurendo-forms 6.3.0 - servizio in cloud.** L'inventario lo registra come EUPL-1.2 senza
modifiche; la nota interna e il verbale del 4 giugno 2026 documentano che il componente rende
accessibili agli utenti le funzioni di compilazione guidata dei moduli di collaudo. L'obbligo si
attiva anche senza modifiche al componente: qui il presupposto è la messa a disposizione online
dell'accesso alle funzionalità, non la modifica. Chiude: responsabile sviluppo piattaforma.

**Combinazione meridolo-compress e algen-crypto - apparecchiatura e servizio.** L'inventario registra
un componente GPL-2.0-only e un componente Apache-2.0 collegati staticamente nello stesso modulo
solmarino-core. Sono licenze incompatibili. Il rimedio non è documentale: occorre la sostituzione del
componente, la sua rimozione o la modifica della modalità di collegamento. Chiude: architettura.

**Otto componenti senza licenza dichiarata.** L'inventario riporta «otto componenti» con il campo
della licenza vuoto su «148 componenti» totali; cinque di quei componenti sono distribuiti
sull'apparecchiatura, due sono presenti solo nel servizio in cloud e uno solo su strumenti interni.
L'assenza di dichiarazione non equivale a una licenza permissiva. Prima della distribuzione occorre,
per ciascuno, l'acquisizione del titolo, la sostituzione o la rimozione. Chiude: architettura, con
verifica dell'ufficio legale.

**Menzione delle modifiche sui file di algen-crypto.** Le intestazioni dei tre file modificati
riportano soltanto l'avviso di licenza originale; la nota interna conferma che non sono stati
aggiunti avvisi. Va apposto su ciascun file modificato un avviso che dichiara la modifica. Chiude:
responsabile sviluppo piattaforma.

**Avvisi di attribuzione di belfonte-parser.** Il pacchetto include un proprio NOTICE con avvisi di
attribuzione che il NOTICE distribuito con la piattaforma non riproduce: l'elencazione del pacchetto
fra i componenti Apache è un'attribuzione diversa da quella richiesta. Va riprodotto il contenuto
degli avvisi in una delle collocazioni ammesse. Chiude: responsabile rilasci.

**Richiesta del cliente del «21 ottobre 2026».** La consegna riguarda i componenti installati
sull'apparecchiatura e non i moduli erogati come servizio, che il cliente stesso esclude. Comprende
gli script di generazione, installazione ed esecuzione. Se la consegna avviene mediante archivio in
rete, va indicato il periodo di disponibilità dell'archivio. Chiude: responsabile rilasci, con
riscontro scritto al cliente.

## Rilievi che non impediscono il rilascio

**quadrelli-render 2.2.0 - apparecchiatura.** Componente GPL-3.0-only modificato, collegato
staticamente nel modulo solmarino-report distribuito sull'apparecchiatura. Occorre verificare quale
sia l'opera distribuita, e non soltanto la porzione modificata. Il fascicolo non consente di
stabilire se il modulo costituisca un'opera unica o un aggregato: servono la mappa delle dipendenze
interne e i confini di compilazione. Fino a quel dato il perimetro resta aperto.

**Articolo 4.2 del contratto di fornitura.** La garanzia sull'assenza di obblighi di divulgazione del
codice sorgente non è coerente con i componenti inventariati. La posizione va gestita con una
comunicazione al cliente e con la modifica della clausola in sede di rinnovo. Il limite di
responsabilità dell'articolo 5.3 non sana la dichiarazione. Chiude: ufficio legale.

**Delibera del comitato tecnico del 4 giugno 2026.** L'adozione del pianificatore era subordinata
all'acquisizione del parere dell'ufficio legale, incaricata Nives Baldracchi. Nel fascicolo non c'è
alcun parere e non si può presumere che sia stato reso: il componente è in esercizio dal 14
settembre 2026, che è un fatto, non l'avveramento della condizione. Chiude: direzione tecnica.

**Codec ferlaino-codec 2.8.1.** Il pacchetto non dichiara licenza e l'intestazione riporta il nome
di un collaboratore esterno, non di un lavoratore dipendente. L'atto di cessione, trasmesso il 12
marzo 2025, non risulta sottoscritto né agli atti. Il titolo di Solmarino non è dimostrato dal
fascicolo e non si presume dall'esistenza del rapporto di collaborazione. Chiude: ufficio legale.

## Effetto sul rilascio del 26 novembre 2026

Il rilascio non riguarda soltanto il servizio: distribuisce l'immagine aggiornata anche alle
apparecchiature già installate, con installazione secondo il calendario per stabilimento. I sette
rilievi del primo gruppo vanno chiusi prima di quella data. La nota del responsabile rilasci, per
cui le attività aperte non figurano fra le condizioni di rilascio e non ne impediscono l'esecuzione,
è una dichiarazione sulla procedura interna: non è una valutazione sugli obblighi di licenza e non
può essere assunta come tale.

## Elementi verificati e privi di rilievo

**tessitura-queue 1.9.0.** AGPL-3.0-only ma usato senza modifiche: sul testo della licenza l'obbligo
verso gli utenti remoti non si attiva. Non va indicato fra i componenti che impongono l'offerta del
sorgente.

**vestrigo-imaging 5.0.2.** GPL-2.0-or-later, collegato staticamente insieme allo stesso componente
Apache-2.0. L'opzione della versione successiva consente di collocare la combinazione sotto la
versione 3 della GPL: la situazione non è quella di meridolo-compress e serve a illustrare la
differenza fra licenza limitata a una versione e licenza che ammette le successive.

**nabissa-loader 1.0.4.** GPL-3.0-only modificato, ma resta sui sistemi interni e non è consegnato ad
alcun destinatario: non impone il rilascio del sorgente.

**Componenti Apache-2.0 eseguiti nel servizio in cloud.** La licenza non contiene disposizioni
sull'uso in rete: restano gli obblighi di attribuzione, non nasce alcun obbligo di divulgazione del
sorgente.

**Modulo solmarino-strumenti.** Non è rilasciato ai clienti: non è un canale di distribuzione e non
gli si applicano gli obblighi di consegna del sorgente.

Sul perimetro dell'obbligo non va usata la categoria dell'opera derivata come se fosse definita
dalla GPL-3.0: la licenza parla di opera basata sul programma, di versione modificata e di opera
coperta, e la nozione di opera derivata appartiene al diritto d'autore applicabile.

## Lacune e richieste documentali

Mancano il parere dell'ufficio legale del giugno 2026 e l'atto di cessione sul codec: nessuno dei
due può essere presentato come acquisito. Mancano i testi di licenza dei cinque componenti senza
licenza distribuiti sull'apparecchiatura e l'esito della verifica presso le rispettive origini.
Manca la delimitazione tecnica dell'opera nei moduli che incorporano componenti a copyleft: senza di
essa il perimetro di quadrelli-render resta indeterminato. Mancano l'elenco degli utenti del cliente
che accedono all'interfaccia programmatica dell'orchestratore e il periodo di attivazione. Non
risulta quando l'inventario sia stato trasmesso al cliente per la prima volta: la sua lettera
riferisce una trasmissione del 6 ottobre 2026 in risposta a una richiesta del 29 settembre.

I due conteggi vanno tenuti distinti: i ventitre componenti a copyleft forte o reciproco e gli otto
senza licenza dichiarata rispondono a domande diverse, e la loro somma non misura nulla.

## Decisioni del committente

Se rinviare il rilascio del 26 novembre o rilasciare il solo servizio, tenendo ferma la
distribuzione alle apparecchiature. Se anticipare al cliente la posizione sull'articolo 4.2 o
attendere. Se sostituire il codec di trama o riaprire la trattativa con il collaboratore esterno.
