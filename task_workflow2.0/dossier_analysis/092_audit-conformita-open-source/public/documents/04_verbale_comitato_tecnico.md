SOLMARINO SOFTWARE S.R.L.
COMITATO TECNICO DI PRODOTTO
Verbale della riunione n. 7 del 2026

Data: 4 giugno 2026, ore 14.30
Luogo: sede di Vimercate, sala Grifone, e in collegamento telematico
Presenti: Ludovica Sperandini (direzione tecnica, presidente), Amilcare Bozzetto
(responsabile sviluppo piattaforma), Delfina Cusumano (responsabile rilasci),
Osvaldo Ranfagni (architettura), Nives Baldracchi (qualità)
Assenti giustificati: Ercole Vantasso (collaboratore esterno, architettura codec)
Segretario verbalizzante: Nives Baldracchi

Ordine del giorno
1. Adozione del pianificatore corvenza-scheduler nel modulo orchestratore
2. Adozione del componente aurendo-forms nel portale
3. Stato del codec di trama
4. Varie ed eventuali

--------------------------------------------------------------------------------
Punto 1 - Adozione del pianificatore corvenza-scheduler
--------------------------------------------------------------------------------

Bozzetto illustra l'esito della valutazione tecnica. Il pianificatore
corvenza-scheduler, versione 4.2.1, risolve i limiti dell'attuale gestione delle
code e consente di introdurre le priorità richieste dal cliente principale.
Riferisce che il pacchetto è distribuito con licenza AGPL-3.0-only e che la
squadra ha già predisposto una patch che modifica la gestione della coda e
l'assegnazione delle priorità.

Ranfagni chiede se il componente sarà eseguito anche sull'appliance. Bozzetto
risponde che l'esecuzione è prevista soltanto nel servizio in cloud, perché il
pianificatore non serve nella configurazione in stabilimento.

Sperandini osserva che la licenza del pacchetto richiede una verifica dedicata e
chiede che l'adozione sia subordinata al parere dell'ufficio legale, da acquisire
prima della messa in produzione.

Il comitato delibera l'adozione di corvenza-scheduler 4.2.1 nel modulo
solmarino-orchestratore, subordinatamente all'acquisizione del parere
dell'ufficio legale sulla licenza del pacchetto e sulle modifiche applicate.
Incaricata dell'acquisizione: Nives Baldracchi.

--------------------------------------------------------------------------------
Punto 2 - Adozione del componente aurendo-forms
--------------------------------------------------------------------------------

Bozzetto riferisce che il componente aurendo-forms 6.3.0 realizza la compilazione
guidata dei moduli di collaudo e sarà esposto agli utenti del portale. Il
pacchetto è distribuito con licenza EUPL-1.2 e non richiede modifiche.

Il comitato delibera l'adozione di aurendo-forms 6.3.0 nel modulo
solmarino-portale, senza modifiche al pacchetto.

--------------------------------------------------------------------------------
Punto 3 - Stato del codec di trama
--------------------------------------------------------------------------------

Ranfagni riferisce che il codec di trama ferlaino-codec è stato scritto da Ercole
Vantasso nell'autunno 2024 nell'ambito del rapporto di collaborazione in essere e
che il pacchetto non riporta alcuna licenza. Chiede se sia stato regolarizzato il
titolo.

Baldracchi riferisce che la richiesta di sottoscrizione dell'atto di cessione è
stata trasmessa a Vantasso il 12 marzo 2025 e che non risulta riscontro.

Il comitato prende atto e rinvia il punto.

--------------------------------------------------------------------------------
Punto 4 - Varie ed eventuali
--------------------------------------------------------------------------------

Cusumano comunica che il calendario dei rilasci sarà aggiornato a settembre.

La riunione si chiude alle ore 16.05.

Il presidente                          Il segretario verbalizzante
Ludovica Sperandini                    Nives Baldracchi
