# WF2-098 - Date e valori verificati

Prodotta da `source/gen/verifica_date_e_codici.py`, non a mano. Le festivita
nazionali italiane sono incluse nel calcolo tramite
`_tools/util_verifica_codici_e_date.py`.

**Data di riferimento:** 2026-11-18

| Milestone | Valore | Calcolo | Fonte |
|---|---|---|---|
| data di riferimento | 18 novembre 2026 | mercoledì | public/01_task.md |
| corrispettivo della cessione | 14.500.000 euro | il massimale ambientale di 900.000 euro corrisponde al 6,21 per cento del corrispettivo | 02_bozza_contratto_cessione_ramo.md, clausola 3.1 |
| stima complessiva degli oneri ambientali | 2.150.000 euro | 1.240.000 + 185.000 + 430.000 + 295.000 = 2.150.000 | 04_stima_oneri_ambientali.md |
| massimale dell'indennità ambientale specifica | 900.000 euro | copre il 41,9 per cento della stima complessiva | 01_bozza_schedule_ambientale.docx, clausola 3.2 |
| esposizione non coperta dal massimale | 1.250.000 euro | 2.150.000 - 900.000 = 1.250.000 | quadratura fra clausola 3.2 e 04_stima_oneri_ambientali.md |
| massimale generale del contratto | 1.450.000 euro | opera autonomamente e non concorre al massimale ambientale, che è riservato all'Allegato 7 | 02_bozza_contratto_cessione_ramo.md, clausole 5.2 e 5.4 |
| derivazione errata: somma dei due massimali | 2.350.000 euro | i due massimali non si sommano sulle perdite ambientali | derivazione da escludere |
| soglia di irrilevanza per singola condizione ambientale | 25.000 euro | nessuna delle quattro voci di costo stimate resta sotto la soglia | 01_bozza_schedule_ambientale.docx, clausola 3.3 |
| franchigia aggregata | 150.000 euro | costruita come importo deducibile; sull'esposizione stimata il massimale opera prima della franchigia, quindi la formulazione non incide sul recupero massimo | 01_bozza_schedule_ambientale.docx, clausola 3.3 |
| recupero massimo sull'esposizione stimata | 900.000 euro | il minore fra 2.150.000 meno 150.000 e 900.000 è 900.000: il massimale opera prima della franchigia | quadratura fra clausola 3.2, clausola 3.3 e 04_stima_oneri_ambientali.md |
| data prevista di closing | 15 dicembre 2026 | martedì | 02_bozza_contratto_cessione_ramo.md, clausola 4.1 |
| scadenza della garanzia ambientale | 15 dicembre 2028 | ventiquattro mesi dal closing | 01_bozza_schedule_ambientale.docx, clausola 3.4 |
| costo annuo del monitoraggio della falda | 43.000 euro | 430.000 euro su dieci annualità di importo omogeneo; ciascuna annualità supera la soglia di irrilevanza di 25.000 euro | 04_stima_oneri_ambientali.md, voce 3 |
| notifica del decreto regionale di approvazione | 25 novembre 2024 | lunedì | 05_provvedimento_regionale_approvazione_progetto.md, relata di notifica |
| termine per l'avvio dei lavori | 25 novembre 2025 | dodici mesi dalla notifica del decreto; alla data di riferimento il termine è decorso da 358 giorni e i lavori non risultano avviati | 05_provvedimento_regionale_approvazione_progetto.md, punto 6 |
| termine del monitoraggio decennale | non determinabile | il decennio decorre dall'avvio dell'esercizio della barriera idraulica, che non è realizzata; assumendo l'avvio nel quarto trimestre 2027, indicato dalla stima degli oneri, il monitoraggio si chiuderebbe non prima del quarto trimestre 2037, quindi in ogni caso dopo la scadenza della garanzia ambientale | 05_provvedimento_regionale_approvazione_progetto.md, punto 3 |
| rapporto fra scadenza della garanzia e durata del monitoraggio | la garanzia scade prima che il monitoraggio inizi a decorrere | alla data di riferimento la barriera idraulica non è realizzata e il decennio di monitoraggio non ha iniziato a decorrere | quadratura fra clausola 3.4 e 05_provvedimento_regionale_approvazione_progetto.md |
| garanzie finanziarie da prestare alla regione | non determinabile | il decreto rinvia alla misura massima consentita dalla legge, che è il cinquanta per cento del costo stimato dell'intervento; il computo allegato al progetto operativo del 2023 non è presente nel fascicolo, quindi la base di calcolo e l'importo non sono determinabili | 05_provvedimento_regionale_approvazione_progetto.md, punto 5 |
| termine di notifica del claim | trenta giorni dalla conoscenza | a pena di decadenza e senza rilievo del pregiudizio per il cedente | 01_bozza_schedule_ambientale.docx, clausola 4.1 |

## Codici a struttura calcolata

Generati con l'algoritmo ufficiale e verificati sul carattere di controllo.

| Soggetto | Tipo | Valore |
|---|---|---|
| Turrivalle Industriale S.p.A. | partita IVA | `01746395829` |
| Nordovest Polimeri S.p.A. | partita IVA | `09254173066` |

## Derivazioni errate escluse

Compaiono come criteri di assenza in sezione C: portano al risultato giusto per la
strada sbagliata, oppure a un risultato sbagliato per una strada intuitiva.

- sommare il massimale generale del contratto e il massimale ambientale per concludere che l'esposizione documentata è coperta
- valutare la sufficienza del massimale ambientale rapportandolo al corrispettivo della cessione anziché all'esposizione documentata
- leggere la franchigia della clausola 3.3 come soglia di attivazione e quantificare in 150.000 euro una perdita di recupero
- indicare una data determinata di conclusione del monitoraggio decennale, che decorre da un evento non ancora verificatosi
