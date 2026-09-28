# WF2-035 — Appalti pubblici: aggiudicazione, comunicazione, accesso, termine dilatorio e termini per impugnare

**Stato: draft, in attesa di validazione professionale. Non `pilot_ready`. Nulla è stato caricato su
Notion, nessun commit è stato eseguito.**

## In una riga

Un concorrente secondo classificato per 1,20 punti chiede la timeline degli adempimenti e dei rimedi.
Il fascicolo è costruito perché non esista una sola data certa: gli atti di gara sono stati messi a
disposizione in due momenti distinti e ciascuna delle due censure che il cliente vuole muovere dipende
da un atto diverso.

## Coordinate

| Campo | Valore |
|---|---|
| Macro-area | Public Procurement / Amministrativo + Contenzioso |
| Verticale | appalti pubblici |
| Use-case family (board) | Procedural timeline |
| Workflow family / subtask | `procedural_computation` / `procedural_timeline` |
| Data di riferimento | giovedì 18 novembre 2027, fascicolo *in corso* |
| Committente | direttore affari legali e societari del concorrente secondo classificato |
| Deliverable | `timeline_rimedi.md`, sette sezioni, massimo 1.800 parole |
| Documenti | 10 (PDF, con versione markdown canonica accanto) |
| Issue di merito | 15 |
| Controlled non-issue | 5 |
| Criteri atomici | 49 — 11 a verifica meccanica, 38 al judge |
| Fonti ammesse | 11, elenco chiuso, congelate al 28 agosto 2026 |

## Struttura

```
WF2-035_appalti-standstill-termini-impugnazione/
├── README.md                          questo file
├── task_spec.json                     scheda macchina del task
├── public/                            tutto ciò che il modello vede
│   ├── 01_task.md                     l'incarico, come va sul board
│   ├── 02_reference_pack.md           testo delle fonti utilizzabili
│   ├── 03_legal_sources.md            registro delle fonti, elenco chiuso, data di congelamento
│   ├── response_template.md           struttura attesa del deliverable
│   └── documents/                     i dieci documenti del fascicolo
├── private/                           mai accessibile durante il run
│   ├── evaluation_criteria.md         rubrica in prosa, a livello di issue → colonna del board
│   ├── criteria_atomized.md           rubrica atomizzata, forma a campi → colonna del board
│   ├── rubric.json                    la stessa, per la macchina
│   ├── runtime_routing.json           instradamento fra verifica meccanica e judge
│   └── review_notes.md                bivi, scelte discrezionali, fragilità note
├── source/                            materiale di costruzione
│   ├── authoring/
│   │   ├── challenge_map.json         issue, controlled non-issue, meccanismi, punti neutri
│   │   ├── fonti_documentali.md       esemplare reale seguito per ciascun documento
│   │   ├── anagrafica.json            nomi, date, importi e codici, per il controllo collisioni
│   │   ├── date_e_valori_verificati.md output dello script di verifica
│   │   ├── verifica_wf2_035.py        lo script: date, festività, importi, punteggi, codici
│   │   ├── gold_standard.md           gold + verifica del gold contro la propria rubrica
│   │   ├── distractor.md              versione sbagliata su tre punti, con i criteri attesi
│   │   └── legal_validation.md        scheda per la lettura blind e domande al validatore
│   └── gen/                           generatori dei documenti e della rubrica
└── runs/README.md                     convenzione degli artefatti di esecuzione
```

## Come si rigenera

```bash
cd batch_WF2-035_037/WF2-035_appalti-standstill-termini-impugnazione
python3 source/authoring/verifica_wf2_035.py --md    # date e valori: deve dare 0 errori
python3 source/gen/docs_035_a.py                     # documenti 01-04
python3 source/gen/docs_035_b.py                     # documenti 05-07
python3 source/gen/docs_035_c.py                     # documenti 08-10
python3 source/gen/build_rubric_035.py               # rubric.json + criteria_atomized.md
cd .. && python3 _tools/verifica_collisioni.py \
  WF2-035_appalti-standstill-termini-impugnazione/source/authoring/anagrafica.json
```

I documenti `.md` e `.pdf` sono generati dalla stessa sorgente da `_tools/render.py`: non modificarli a
mano, perché la prossima rigenerazione li sovrascrive.

## Come è costruita la difficoltà

Cinque meccanismi, nessuno dei quali è la lunghezza:

1. **Termini dipendenti da più eventi.** L'art. 120, comma 2, c.p.a. àncora il termine di trenta giorni
   in alternativa alla ricezione della comunicazione ex art. 90 e al momento in cui gli atti sono messi
   a disposizione ex art. 36. Nel fascicolo i due momenti sono distinti — 25 ottobre e 16 novembre 2027 —
   e ciascuna censura dipende da un atto diverso: non esiste una sola scadenza.
2. **Data del documento contro data di efficacia.** Determina e pubblicazione dell'avviso il 20 ottobre,
   invio e consegna della comunicazione il 25, presa visione il 26. Tre date a pochi giorni di distanza,
   una sola delle quali è la ricezione, e la più favorevole al cliente è quella sbagliata.
3. **Presenza contro adeguatezza.** La comunicazione ex art. 90 c'è, è tempestiva e formalmente
   completa; il difetto è nella contestualità della messa a disposizione degli atti, differita quanto
   alla relazione tecnica dell'aggiudicataria.
4. **Dichiarazione di parte smentita dai documenti e dalla norma.** La nota interna dell'ufficio gare
   afferma trentacinque giorni di termine dilatorio, ritiene che l'istanza all'ANAC sospenda i termini e
   colloca la decorrenza alla presa visione. Tutte e tre le affermazioni sono sbagliate, e una di esse
   contraddice un documento della stazione appaltante.
5. **Metodo di calcolo controintuitivo.** Nel rito degli appalti i termini processuali sono dimezzati,
   ma il dimezzamento non tocca la notificazione del ricorso introduttivo e tocca invece il deposito. Il
   risultato intuitivo è sbagliato in entrambe le direzioni.

## Che cosa il caso non misura

La fondatezza delle censure — che il cliente enuncia da sé nella nota interna — la conseguenza
dell'eventuale stipulazione del contratto in violazione del termine dilatorio, la quantificazione del
danno e la scelta fra tutela in forma specifica e per equivalente. Le esclusioni sono deliberate e
motivate in `private/evaluation_criteria.md`, sezione «Punti neutri».

## Che cosa manca prima del freeze

1. Calibrazione del Passo 5: il gold sottoposto ai tre judge, il fallimento del distrattore misurato.
2. Lettura blind di un professionista e risposta alle nove domande di
   `source/authoring/legal_validation.md`.
3. Decisione sul punto 5 di quella scheda: il caso è ambientato al 2027 ma le fonti sono congelate al
   2026. Se si scegliesse di riportare l'ambientazione entro la data di congelamento, il calendario va
   rifatto interamente.
