# WF2-091 - Date e valori verificati

Prodotta da `source/gen/verifica_date_e_codici.py`, non a mano. Le festivita
nazionali italiane sono incluse nel calcolo tramite
`_tools/util_verifica_codici_e_date.py`.

**Data di riferimento:** 2026-10-14

| Milestone | Valore | Calcolo | Fonte |
|---|---|---|---|
| data di riferimento | 14 ottobre 2026 | mercoledì, giorno feriale | public/01_task.md |
| visualizzazione della cartella riservata da parte dell'utenza CT-ALL | 5 ottobre 2026, ore 17:22 | precede la data di riferimento di 9 giorni | 06_log_accessi_data_room.csv |
| download del prospetto della marginalità | 6 ottobre 2026 | precede la data di riferimento di 8 giorni; il messaggio interno è dello stesso giorno | 06_log_accessi_data_room.csv e 05_email_direttore_vendite.md |
| riunione congiunta fissata | 16 ottobre 2026 | successiva di 2 giorni alla data di riferimento | 05_email_direttore_vendite.md |
| numerosità delle classi di restituzione | A=7, B=6, C=5, D=4 clienti | la convenzione del punto 4.2 del term sheet richiede almeno 5 clienti per classe: la classe D con quattro clienti non la soddisfa | 02_term_sheet_joint_venture.md e 03_data_request_list.md, voce 21 |
| fatturato aggregato realizzato in Italia dalle due parti | 349.800.000 euro | 198.100.000 + 151.700.000 = 349.800.000 | 02_term_sheet_joint_venture.md, Allegato 1 |
| confronto con la soglia riferita all'insieme delle imprese interessate | 349.800.000 < 595.000.000 | la soglia aggregata vigente al freeze non è raggiunta: non sorge l'obbligo di comunicazione preventiva | art. 16, comma 1, L. 287/1990 e provv. AGCM 31873/2026 |
| confronto con la soglia riferita individualmente ad almeno due imprese | 198.100.000 e 151.700.000 > 36.000.000 | entrambe le parti la superano: una sola delle due soglie è superata | art. 16, comma 1, L. 287/1990 e provv. AGCM 31873/2026 |
| fatturato mondiale aggregato | 382.800.000 euro | 214.500.000 + 168.300.000 = 382.800.000; resta sotto i 5 miliardi di euro richiamati dall'art. 16, comma 1-bis | 02_term_sheet_joint_venture.md, Allegato 1 |

## Codici a struttura calcolata

Generati con l'algoritmo ufficiale e verificati sul carattere di controllo.

| Soggetto | Tipo | Valore |
|---|---|---|
| Tramontina Azionamenti S.p.A. | partita IVA | `04728193659` |
| Belvederi Trasmissioni S.p.A. | partita IVA | `09132647588` |

## Derivazioni errate escluse

Compaiono come criteri di assenza in sezione C: portano al risultato giusto per la
strada sbagliata, oppure a un risultato sbagliato per una strada intuitiva.

- dedurre l'obbligo di comunicazione preventiva dal fatturato mondiale aggregato di 382.800.000 euro, che non è il parametro dell'art. 16, comma 1
- dedurre l'obbligo di comunicazione preventiva dal solo superamento individuale della soglia di 36 milioni di euro da parte di entrambe le parti, senza verificare la soglia aggregata
- ritenere la classe D conforme perché il numero delle classi concordate nel term sheet è quattro, confondendo il numero delle classi con la numerosità di ciascuna
