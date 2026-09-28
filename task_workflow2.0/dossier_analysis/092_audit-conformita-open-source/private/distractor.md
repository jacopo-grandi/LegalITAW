# WF2-092 - Distrattore controllato

## Criteri che questa esecuzione intende far fallire

B.4 (errore sul conveying per il pianificatore), B.19 (indipendenza dell'obbligo EUPL dalla
modifica), B.21 (divieto di presunzione sui componenti senza licenza), B.33 (sovra-segnalazione su
tessitura-queue), B.34 (sovra-segnalazione su vestrigo-imaging), C.6 (derivazione errata sul
conteggio).

Gli altri criteri devono restare superati: il distrattore sbaglia sul presupposto delle due licenze
reciproche, sul trattamento dei componenti senza licenza e sull'assimilazione fra componenti simili.

## Esecuzione

### Esito operativo

Il quadro è sostanzialmente sotto controllo. I componenti a rischio sono trentuno, somma dei
ventitre a copyleft forte o reciproco e degli otto senza licenza dichiarata.

### Rilievi

Menzione delle modifiche sui file di algen-crypto: le intestazioni dei tre file modificati riportano
soltanto l'avviso di licenza originale e va apposto l'avviso di modifica. Chiude: responsabile
sviluppo piattaforma.

Avvisi di attribuzione di belfonte-parser: il contenuto del NOTICE del pacchetto non è riprodotto e
va riprodotto in una delle collocazioni ammesse. Chiude: responsabile rilasci.

Combinazione meridolo-compress e algen-crypto: licenze incompatibili, collegate staticamente nello
stesso modulo. Rimedio: sostituzione del componente o modifica del collegamento. Nella stessa
condizione si trova vestrigo-imaging, collegato staticamente insieme allo stesso componente
Apache-2.0: anche quella combinazione è incompatibile e va risolta.

Pianificatore corvenza-scheduler: il pacchetto è AGPL-3.0-only ed è stato modificato, ma nel
servizio in cloud nessun eseguibile viene consegnato al cliente. Non essendovi consegna, non nasce
alcun obbligo di messa a disposizione del sorgente. Il punto resta da monitorare.

Coda secondaria tessitura-queue: pacchetto AGPL-3.0-only eseguito in cloud. Va offerto il codice
sorgente agli utenti che interagiscono a distanza, come per il pianificatore.

Componente aurendo-forms: pacchetto EUPL-1.2 usato senza modifiche. In assenza di modifiche l'obbligo
non si attiva e il componente non richiede interventi.

Componenti senza licenza dichiarata: otto componenti su 148, di cui cinque distribuiti
sull'apparecchiatura. In assenza di indicazioni contrarie nei rispettivi pacchetti, sono trattabili
come componenti a licenza permissiva; è comunque opportuno aggiornare l'inventario alla prossima
estrazione. Chiude: architettura.

quadrelli-render: componente GPL-3.0-only modificato e distribuito sull'apparecchiatura. Occorre
verificare quale sia l'opera distribuita: il fascicolo non consente di stabilire se il modulo sia
un'opera unica o un aggregato.

Richiesta del cliente del 21 ottobre 2026: la consegna riguarda i componenti installati
sull'apparecchiatura e non i moduli erogati come servizio; comprende gli script di generazione,
installazione ed esecuzione; va indicato il periodo di disponibilità dell'archivio.

Articolo 4.2 del contratto: la garanzia non è coerente con i componenti inventariati e va gestita
con una comunicazione al cliente e con la modifica in sede di rinnovo. Chiude: ufficio legale.

Delibera del 4 giugno 2026: l'adozione era subordinata al parere dell'ufficio legale, che non
risulta agli atti. Chiude: direzione tecnica.

Codec ferlaino-codec: nessuna licenza dichiarata, autore collaboratore esterno, atto di cessione non
sottoscritto. Il titolo non è dimostrato. Chiude: ufficio legale.

### Effetto sul rilascio del 26 novembre 2026

Il rilascio distribuisce l'immagine aggiornata anche alle apparecchiature installate. Vanno chiusi
prima di quella data gli avvisi di modifica, gli avvisi di attribuzione, le due combinazioni
incompatibili e la risposta al cliente. Gli altri punti possono seguire.

### Elementi verificati e privi di rilievo

Il modulo solmarino-strumenti non è rilasciato ai clienti. I componenti Apache-2.0 eseguiti nel
servizio in cloud restano soggetti agli obblighi di attribuzione e non fanno nascere obblighi di
divulgazione del sorgente.

### Lacune e richieste documentali

Mancano il parere dell'ufficio legale e l'atto di cessione sul codec, la delimitazione tecnica
dell'opera nei moduli con componenti a copyleft, l'elenco degli utenti dell'interfaccia
programmatica e la data della prima trasmissione dell'inventario al cliente.

### Decisioni del committente

Se rinviare il rilascio, se anticipare al cliente la posizione sull'articolo 4.2, se sostituire il
codec di trama.
