# WF2-093 - Date e valori verificati

Prodotta da `source/gen/verifica_date_e_codici.py`, non a mano. Le festivita
nazionali italiane sono incluse nel calcolo tramite
`_tools/util_verifica_codici_e_date.py`.

**Data di riferimento:** 2026-11-10

| Milestone | Valore | Calcolo | Fonte |
|---|---|---|---|
| data di riferimento | 10 novembre 2026 | martedì | public/01_task.md |
| deposito della domanda di brevetto europeo n. 19180446.7 | 14 giugno 2019 | il mese di deposito determina la scadenza dell'annualità italiana | 01_estratto_bollettino_concessione.md |
| pubblicazione della domanda | 16 dicembre 2020 | anteriore di 1869 giorni alla pubblicazione della menzione della concessione | 10_nota_consulente_brevetti.md |
| deposito della domanda divisionale n. 25171188.4 | 12 marzo 2025 | anteriore alla pubblicazione della menzione; la divisionale è in fase di esame | 10_nota_consulente_brevetti.md |
| pubblicazione della menzione della concessione | 28 gennaio 2026 | mercoledì; il Bollettino europeo esce il mercoledì e la data della menzione è la data del fascicolo 2026/05 | 01_estratto_bollettino_concessione.md |
| scadenza del termine di opposizione | 28 ottobre 2026 | 28 gennaio 2026 + 9 mesi; il termine a mesi scade nel giorno dello stesso numero del mese finale; mercoledì, non festività nazionale italiana | art. 99(1) della Convenzione; Regola 131(4) |
| scadenza del termine per la traduzione italiana | 28 aprile 2026 | 28 gennaio 2026 + 3 mesi; martedì | art. 56, comma 4, del Codice della proprietà industriale |
| deposito della traduzione italiana integrale | 24 aprile 2026 | precede la scadenza di 4 giorni | 03_deposito_traduzione_italiana.md |
| mese di riferimento dell'annualità italiana | giugno | mese in cui è caduta la data di deposito della domanda europea, il 14 giugno 2019 | art. 227, comma 1, del Codice della proprietà industriale |
| scadenza dell'annualità dovuta nel 2026 | 30 giugno 2026 | ultimo giorno del mese di riferimento | 04_ricevuta_annualita.md |
| versamento dell'annualità 2026 | 26 giugno 2026 | precede la scadenza di 4 giorni; nessun diritto di mora e nessuna decadenza | 04_ricevuta_annualita.md |
| acquisto in anonimo del dispositivo concorrente | 22 settembre 2026 | anteriore di 49 giorni alla data di riferimento | 07_rapporto_test_buy.md |
| trasmissione della diffida | 6 ottobre 2026 | anteriore di 35 giorni alla data di riferimento; il termine convenzionale di quindici giorni assegnato nella diffida è scaduto il 21 ottobre 2026 | 08_diffida_contraffazione.md |
| pubblicazione del bando di gara | 16 ottobre 2026 | anteriore di 25 giorni alla data di riferimento | 09_avviso_gara_ospedaliera.md |
| deposito dell'atto di opposizione | 27 ottobre 2026 | precede la scadenza del termine di opposizione di 1 giorno | 05_atto_opposizione.md |
| valuta dell'addebito della tassa di opposizione | 29 ottobre 2026 | successiva alla scadenza del termine di opposizione di 1 giorno; la data di registrazione dell'addebito è invece il 27 ottobre 2026 | 06_estratto_conto_deposito_epo.md |
| termine di presentazione delle offerte nella gara | 15 dicembre 2026 | successivo di 35 giorni alla data di riferimento | 09_avviso_gara_ospedaliera.md |
| termine per l'inizio del giudizio di merito | non determinabile | il termine è il più lungo fra venti giorni lavorativi e trentuno giorni di calendario dalla pronuncia in udienza o dalla comunicazione; alla data di riferimento nessun provvedimento è stato richiesto né emesso. Calcolo illustrativo su data ipotetica di comunicazione del 27 novembre 2026: venti giorni lavorativi scadrebbero il 29 dicembre 2026, trentuno giorni di calendario il 28 dicembre 2026, si applicherebbe il 29 dicembre 2026 | art. 132, comma 2, del Codice della proprietà industriale |

## Codici a struttura calcolata

Generati con l'algoritmo ufficiale e verificati sul carattere di controllo.

| Soggetto | Tipo | Valore |
|---|---|---|
| Nevalta Medical S.p.A. | codice fiscale e partita IVA | `05174938265` |

## Derivazioni errate escluse

Compaiono come criteri di assenza in sezione C: portano al risultato giusto per la
strada sbagliata, oppure a un risultato sbagliato per una strada intuitiva.

- computare i nove mesi dalla data di deposito della domanda europea, che darebbe il 14 marzo 2020
- computare i nove mesi dalla pubblicazione della domanda, che darebbe il 16 settembre 2021
- computare la scadenza dell'annualità dall'ultimo giorno del mese della concessione, che darebbe il 31 gennaio 2027
- ricavare la tempestività dell'opposizione dalla sola data di registrazione dell'addebito, anziché dalla data di valuta indicata dall'estratto
