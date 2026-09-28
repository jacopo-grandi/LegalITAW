# WF2-094 - Date e valori verificati

Prodotta da `source/gen/verifica_date_e_codici.py`, non a mano. Le festivita
nazionali italiane sono incluse nel calcolo tramite
`_tools/util_verifica_codici_e_date.py`.

**Data di riferimento:** 2026-10-06

| Milestone | Valore | Calcolo | Fonte |
|---|---|---|---|
| data di riferimento | 6 ottobre 2026 | martedì | public/01_task.md |
| rilascio del permesso di costruire | 18 marzo 2024 | lunedì; successivo al 31 dicembre 2025 non è: il titolo è anteriore, ma i lavori risultano ultimati e nessun termine è decorso inutilmente | 02_permesso_di_costruire.md |
| inizio dei lavori | 2 settembre 2024 | entro un anno dal rilascio del titolo | 02_permesso_di_costruire.md, annotazioni |
| presentazione della segnalazione di variante | 14 febbraio 2025 | anteriore alla dichiarazione di ultimazione dei lavori | 03_scia_variante.md |
| ultimazione dei lavori di finitura | 12 maggio 2025 | lunedì | 02_permesso_di_costruire.md, annotazioni |
| termine per la segnalazione certificata di agibilità | 27 maggio 2025 | quindici giorni dall'ultimazione dei lavori di finitura | art. 24, comma 2, del testo unico dell'edilizia |
| presentazione della segnalazione certificata di agibilità | 3 giugno 2025 | successiva al termine di 7 giorni | 05_segnalazione_certificata_agibilita.md |
| rilascio del certificato di destinazione urbanistica | 15 luglio 2026 | mercoledì; alla data di riferimento sono decorsi 83 giorni | 01_certificato_destinazione_urbanistica.md |
| termine di validità del certificato | 15 luglio 2027 | un anno dal rilascio, subordinato alla dichiarazione dell'alienante che non siano intervenute modificazioni degli strumenti urbanistici | art. 30, comma 3, del testo unico dell'edilizia |
| termine della verifica tecnica e documentale | 31 ottobre 2026 | successivo di 25 giorni alla data di riferimento | 06_contratto_preliminare.md, punto 5.1 |
| termine per la stipulazione dell'atto definitivo | 20 gennaio 2027 | anteriore di 176 giorni alla scadenza della validità del certificato | 06_contratto_preliminare.md, punto 3.1 |
| superficie dell'area pertinenziale | 6.240 mq | superficie fondiaria del compendio; supera i 5.000 mq oltre i quali l'esclusione dall'obbligo di allegazione del certificato non opera | 06_contratto_preliminare.md, punto 1.2 |
| superficie utile assentita dal permesso di costruire | 1.840,00 mq | dato dichiarato al punto 2 del titolo | 02_permesso_di_costruire.md |
| superficie utile dichiarata nella segnalazione di variante | 1.902,00 mq | 1.840,00 + 62,00 mq del soppalco del corpo accessorio | 03_scia_variante.md |
| superficie utile rilevata | 1.958,00 mq | somma dei vani misurati; comprende un soppalco di 56,00 mq nel corpo principale non dichiarato in alcun titolo | 04_rilievo_metrico.md, punto 2 |
| scostamento non assentito di superficie utile | 56 mq | 1.958 - 1.902 = 56 mq; il termine di confronto è la superficie dichiarata nella variante, non quella del permesso originario | 04_rilievo_metrico.md e 03_scia_variante.md |
| scostamento in percentuale | 2,94 per cento | 56 / 1.902 = 0,0294; sulla superficie del permesso originario si otterrebbe invece il 6,41 per cento, che è la derivazione da escludere | 04_rilievo_metrico.md |
| altezza assentita, dichiarata e rilevata | 7,20 / 7,24 / 7,24 m | l'altezza rilevata coincide con quella dichiarata nella variante: nessuno scostamento non assentito | 02_permesso_di_costruire.md, 03_scia_variante.md, 04_rilievo_metrico.md |
| superficie a parcheggio prescritta e rilevata | 412,00 mq contro 338,00 mq | differenza di 74 mq | 02_permesso_di_costruire.md e 04_rilievo_metrico.md |
| dotazione minima di parcheggio | 391,6 mq | 20 per cento di 1.958 mq di superficie utile rilevata; la superficie rilevata di 338 mq resta inferiore di 53,6 mq. Sulla superficie utile assentita si otterrebbero 368 mq, che è la derivazione da escludere | 01_certificato_destinazione_urbanistica.md, allegato, art. 31.3 |

## Codici a struttura calcolata

Generati con l'algoritmo ufficiale e verificati sul carattere di controllo.

| Soggetto | Tipo | Valore |
|---|---|---|
| Immobiliare Cordevalle S.r.l. | partita IVA | `03845612971` |
| Sartorena Immobili S.r.l. | partita IVA | `02184996045` |

## Derivazioni errate escluse

Compaiono come criteri di assenza in sezione C: portano al risultato giusto per la
strada sbagliata, oppure a un risultato sbagliato per una strada intuitiva.

- calcolare lo scostamento sulla superficie utile del permesso originario, ottenendo 118 metri quadrati e il 6,41 per cento, anziché sulla superficie dichiarata nella variante
- applicare allo scostamento una soglia di tolleranza superiore al 2 per cento invocando la graduazione prevista per gli interventi realizzati entro il 24 maggio 2024
- calcolare la dotazione minima di parcheggio sul 20 per cento della superficie utile assentita dal permesso, ottenendo 368 metri quadrati, anziché sulla superficie utile rilevata
- quantificare l'oblazione applicando il doppio e l'incremento del 20 per cento all'intero contributo di costruzione di euro 74.180,00
