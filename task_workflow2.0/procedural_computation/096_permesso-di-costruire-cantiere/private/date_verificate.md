# WF2-096 - Date e valori verificati

Prodotta da `source/gen/verifica_date_e_codici.py`, non a mano. Le festivita
nazionali italiane sono incluse nel calcolo tramite
`_tools/util_verifica_codici_e_date.py`.

**Data di riferimento:** 2026-12-02

| Milestone | Valore | Calcolo | Fonte |
|---|---|---|---|
| data di riferimento | 2 dicembre 2026 | mercoledì | public/01_task.md |
| rilascio dell'autorizzazione paesaggistica | 2 marzo 2023 | giovedì; anteriore al titolo edilizio | 02_autorizzazione_paesaggistica.md |
| rilascio del permesso di costruire | 12 febbraio 2026 | giovedì; successivo al 31 dicembre 2025, quindi fuori dall'ambito della proroga straordinaria di quarantotto mesi | 01_permesso_di_costruire.md |
| termine massimo di inizio dei lavori | 12 febbraio 2027 | un anno dal rilascio del titolo | art. 15, comma 2, del testo unico dell'edilizia |
| comunicazione di inizio dei lavori | 11 maggio 2026 | lunedì; precede il termine di inizio di 277 giorni | 03_comunicazione_inizio_lavori.md |
| termine di ultimazione dei lavori | 11 maggio 2029 | tre anni dall'inizio dei lavori, non dal rilascio del titolo | art. 15, comma 2, del testo unico dell'edilizia |
| derivazione errata: tre anni dal rilascio del titolo | 12 febbraio 2029 | il termine di ultimazione non decorre dal rilascio del titolo | derivazione da escludere |
| efficacia dell'autorizzazione paesaggistica | dal 12 febbraio 2026 al 12 febbraio 2031 | cinque anni decorrenti dal giorno in cui acquista efficacia il titolo edilizio, non dalla data di rilascio dell'autorizzazione | art. 146, comma 4, del codice dei beni culturali e del paesaggio |
| termine ultimo di conclusione dei lavori iniziati nel quinquennio | 12 febbraio 2032 | un anno successivo alla scadenza del quinquennio; posteriore di 1007 giorni al termine di ultimazione del permesso, che resta quindi il vincolo operativo | art. 146, comma 4, del codice dei beni culturali e del paesaggio |
| derivazione errata: quinquennio computato dal rilascio dell'autorizzazione | 2 marzo 2028 | il quinquennio non decorre dalla data di rilascio dell'autorizzazione paesaggistica | derivazione da escludere |
| sospensione dei lavori disposta | dal 15 giugno al 30 luglio 2026 | quarantasei giorni di calendario compresi gli estremi | 04_ordinanza_sospensione_lavori.md e 05_provvedimento_revoca.md |
| giorni lavorativi perduti nella sospensione | trentaquattro | conteggio dei giorni lavorativi fra il 15 giugno e il 30 luglio 2026, estremi inclusi, con esclusione dei sabati, delle domeniche e delle festività nazionali; non è la misura dello slittamento del cronoprogramma | 04_ordinanza_sospensione_lavori.md |
| ultimazione programmata dal cronoprogramma originario | 9 aprile 2027 | venerdì; data di programma, non ancora avvenuta | 06_cronoprogramma_e_stato_avanzamento.md |
| ultimazione programmata dopo lo slittamento | 25 maggio 2027 | 9 aprile 2027 più quarantasei giorni di calendario; resta anteriore di 717 giorni al termine di ultimazione del permesso | 06_cronoprogramma_e_stato_avanzamento.md |
| termine per la segnalazione certificata di agibilità | quindici giorni dall'ultimazione dei lavori di finitura | la data effettiva di ultimazione dei lavori di finitura non è nota e il termine non è fissabile in una data determinata | art. 24, comma 2, del testo unico dell'edilizia |
| superficie di solaio assentita | 1.640 metri quadrati | dato del progetto approvato | 01_permesso_di_costruire.md, punto 2 |
| superficie di solaio della variante | 1.880 metri quadrati | dato della relazione di variante | 07_relazione_direzione_lavori_variante.md, punto 3 |
| incremento della superficie di solaio | 240 metri quadrati, pari al 14,63 per cento | 1.880 meno 1.640 uguale 240 metri quadrati; 240 diviso 1.640 uguale 0,1463 | 07_relazione_direzione_lavori_variante.md, punto 3 |

## Codici a struttura calcolata

Generati con l'algoritmo ufficiale e verificati sul carattere di controllo.

| Soggetto | Tipo | Valore |
|---|---|---|
| Costruzioni Pratomagno S.p.A. | partita IVA | `02917364800` |

## Derivazioni errate escluse

Compaiono come criteri di assenza in sezione C: portano al risultato giusto per la
strada sbagliata, oppure a un risultato sbagliato per una strada intuitiva.

- computare il termine di ultimazione tre anni dal rilascio del titolo, ottenendo il 12 febbraio 2029
- computare il quinquennio di efficacia dell'autorizzazione paesaggistica dalla data del suo rilascio, ottenendo la scadenza al 2 marzo 2028
- usare i giorni lavorativi perduti nella sospensione come misura dello slittamento del cronoprogramma, quando le fasi sono programmate in giorni di calendario
- invocare la proroga straordinaria di quarantotto mesi su un titolo rilasciato dopo il 31 dicembre 2025
