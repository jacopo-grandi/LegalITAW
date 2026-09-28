# WF2-092 - Date e valori verificati

Prodotta da `source/gen/verifica_date_e_codici.py`, non a mano. Le festivita
nazionali italiane sono incluse nel calcolo tramite
`_tools/util_verifica_codici_e_date.py`.

**Data di riferimento:** 2026-11-05

| Milestone | Valore | Calcolo | Fonte |
|---|---|---|---|
| data di riferimento | 5 novembre 2026 | giovedì | public/01_task.md |
| quadratura dell'inventario delle dipendenze | 148 componenti | 96 permissivi + 21 a copyleft debole + 23 a copyleft forte o reciproco + 8 senza licenza dichiarata = 148, pari al totale dichiarato in testata al file | 02_inventario_dipendenze.csv |
| componenti senza licenza dichiarata | 8 componenti | righe con il campo licenza_spdx vuoto | 02_inventario_dipendenze.csv |
| ripartizione per canale dei componenti senza licenza dichiarata | 5 sull'apparecchiatura, 2 nel solo servizio in cloud, 1 su strumenti interni | 5 + 2 + 1 = 8 | 02_inventario_dipendenze.csv |
| componenti a copyleft forte o reciproco | 23 componenti | comprende GPL-2.0-only, GPL-2.0-or-later, GPL-3.0, AGPL-3.0 ed EUPL-1.2 | 02_inventario_dipendenze.csv |
| delibera che subordina l'adozione del pianificatore al parere legale | 4 giugno 2026 | alla data di riferimento sono decorsi 154 giorni senza che il parere risulti acquisito | 04_verbale_comitato_tecnico.md, punto 1 |
| richiesta scritta del cliente sul codice sorgente | 21 ottobre 2026 | precede la data di riferimento di 15 giorni | 06_richiesta_codice_sorgente.md |
| congelamento delle funzionalità | 6 novembre 2026 | successivo di 1 giorno alla data di riferimento | 07_piano_di_rilascio.md |
| rilascio agli ambienti dei clienti | 26 novembre 2026 | successivo di 21 giorni alla data di riferimento | 07_piano_di_rilascio.md |
| avvio dell'aggiornamento delle apparecchiature installate | 30 novembre 2026 | successivo di 4 giorni al rilascio | 07_piano_di_rilascio.md |

## Codici a struttura calcolata

Generati con l'algoritmo ufficiale e verificati sul carattere di controllo.

| Soggetto | Tipo | Valore |
|---|---|---|
| Solmarino Software S.r.l. | partita IVA | `06283749155` |
| Ostrivalle Pressofusioni S.p.A. | partita IVA | `04991276330` |

## Derivazioni errate escluse

Compaiono come criteri di assenza in sezione C: portano al risultato giusto per la
strada sbagliata, oppure a un risultato sbagliato per una strada intuitiva.

- dedurre il numero dei componenti a rischio dalla somma dei componenti a copyleft forte e di quelli senza licenza dichiarata, che risponde a una domanda diversa da quella sul canale di distribuzione
- qualificare come permissivi gli otto componenti senza licenza dichiarata, perché il campo vuoto dell'inventario non riporta alcun obbligo
- escludere l'obbligo sul pianificatore dal fatto che nessun eseguibile è consegnato al cliente, che è il presupposto del conveying e non quello dell'interazione a distanza
