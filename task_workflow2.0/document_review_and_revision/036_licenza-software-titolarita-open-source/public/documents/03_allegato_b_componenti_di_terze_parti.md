<small>**ALVEARIA SOFTWARE S.R.L.** - Via Nino Bixio 9 - 35131 Padova (PD)</small>

---

# ALLEGATO B

*Elenco dei componenti software di terze parti e dei Componenti Preesistenti - Piattaforma MERIDIO, versione 3.4 - allegato al contratto versione 2.0*

Il presente allegato elenca i componenti software non sviluppati nell'ambito del Progetto che sono integrati nella piattaforma, con l'indicazione della licenza applicabile secondo l'identificativo SPDX, del tipo di collegamento, dell'eventuale modifica da parte del Fornitore e dell'inclusione negli artefatti consegnati al Cliente.

L'elenco riporta le **dipendenze dirette**. La distinta delle dipendenze transitive è generata automaticamente dal sistema di compilazione ed è conservata dal Fornitore.

| Componente | Ver. | Licenza (SPDX) | Tipo di collegamento | Modif. | Incluso nel Software consegnato | Funzione svolta | Note |
|---|---|---|---|---|---|---|---|
| **quadrifoglio-orm** | 4.2.1 | MIT | libreria collegata staticamente | No | Si | mappatura fra oggetti applicativi e base di dati | avviso di copyright e testo della licenza conservati nel file NOTICE |
| **tessitura-http** | 2.9.0 | Apache-2.0 | libreria collegata staticamente | No | Si | client per le chiamate ai servizi esterni | file NOTICE conservato; nessuna modifica ai file originali |
| **vetrata-charts** | 1.14.3 | LGPL-2.1-only | libreria condivisa, collegata dinamicamente a tempo di esecuzione | No | Si | generazione dei grafici nelle schermate di analisi | distribuita come libreria condivisa separata; nessuna modifica |
| **melograno-reportd** | 3.0.2 | AGPL-3.0-only | libreria collegata all'interno del processo del server applicativo | Si | Si | motore di composizione e generazione dei prospetti e delle stampe | adattata dal Fornitore per la gestione dei modelli di stampa multi-marchio |
| **ferrobatte-build** | 0.8.7 | GPL-2.0-only | strumento di compilazione, eseguito soltanto in fase di build | No | No | generazione degli artefatti di distribuzione | non incluso negli artefatti consegnati al Cliente |
| **motore-di-riconciliazione** | 1.0 | proprietaria del Fornitore | modulo interno del Software | n/a | Si | riconciliazione contabile fra ordini, documenti di trasporto e fatture | Componente Preesistente del Fornitore, sviluppato anteriormente all'avvio del Progetto |

Copia dei testi delle licenze applicabili ai componenti sopra elencati è consegnata al Cliente unitamente agli artefatti di ciascun rilascio ed è riprodotta nel file NOTICE contenuto nella distribuzione.

<small>Elenco aggiornato alla versione 3.4 del 5 settembre 2028. Redatto a cura dell'ufficio tecnico del Fornitore.</small>
