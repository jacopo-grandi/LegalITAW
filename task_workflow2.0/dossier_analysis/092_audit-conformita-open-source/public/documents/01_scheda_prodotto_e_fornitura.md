SOLMARINO SOFTWARE S.R.L.
Scheda tecnica di prodotto e modalità di fornitura
Piattaforma Solmarino - versione 5.1.4
Edizione del 28 ottobre 2026 - documento interno, revisione tecnica

1. Descrizione della piattaforma

La piattaforma Solmarino gestisce l'acquisizione, la validazione e l'archiviazione
dei dati di collaudo di linee di produzione. È organizzata in cinque moduli.

solmarino-core
  Motore di acquisizione e validazione. Contiene le librerie di cifratura, di
  parsing dei tracciati e di compressione degli archivi.

solmarino-orchestratore
  Pianificatore delle esecuzioni. Assegna le priorità alle code di elaborazione e
  gestisce i tentativi di ripetizione.

solmarino-report
  Generatore dei rapporti di collaudo in formato stampabile.

solmarino-portale
  Interfaccia web di consultazione e di compilazione guidata dei moduli di
  collaudo.

solmarino-strumenti
  Utilità di diagnosi e di caricamento dei dati di collaudo. Non è rilasciata ai
  clienti: è usata dal servizio assistenza sui sistemi interni di Solmarino.

2. Modalità di fornitura

2.1 Fornitura come appliance
Il cliente riceve un'apparecchiatura preconfigurata con i moduli solmarino-core e
solmarino-report installati. L'apparecchiatura resta nella disponibilità del
cliente, che ne acquista la proprietà, ed è collegata alla sua rete di
stabilimento. Il software è consegnato in forma eseguibile, con l'immagine di
sistema, e il cliente riceve la licenza d'uso di cui al contratto di fornitura.

2.2 Fornitura come servizio in cloud
Il cliente accede ai moduli solmarino-orchestratore e solmarino-portale attraverso
un'interfaccia web e un'interfaccia programmatica esposte su rete pubblica. Le
istanze sono eseguite sull'infrastruttura di Solmarino. Nessun eseguibile è
consegnato al cliente. Gli utenti del cliente interagiscono con il portale e con
l'orchestratore attraverso il proprio browser o attraverso chiamate al servizio.

2.3 Configurazione mista
Il contratto in essere con il cliente principale prevede la configurazione mista:
appliance in stabilimento per l'acquisizione, servizio in cloud per la
pianificazione e per la consultazione.

3. Tracciamento delle dipendenze di terze parti

Il sistema di build produce a ogni rilascio l'inventario delle dipendenze, con
l'identificativo di licenza dichiarato dal pacchetto, la modalità di collegamento
e l'indicazione delle modifiche locali applicate. L'inventario della versione
5.1.4 è allegato.

4. Modifiche locali applicate nella versione 5.1.4

Le modifiche locali riguardano cinque pacchetti di terze parti e sono conservate
come patch nel repository interno. La procedura di build le applica prima della
compilazione.

5. Componenti raggiungibili dalla rete pubblica

Sono raggiungibili dalla rete pubblica le interfacce esposte da
solmarino-orchestratore e da solmarino-portale. Le librerie di solmarino-core
eseguite nel servizio in cloud non espongono interfacce proprie e sono invocate
dai due moduli precedenti.

6. Interlocutori tecnici

Direzione tecnica: Ludovica Sperandini.
Responsabile sviluppo piattaforma: Amilcare Bozzetto.
Responsabile rilasci: Delfina Cusumano.
