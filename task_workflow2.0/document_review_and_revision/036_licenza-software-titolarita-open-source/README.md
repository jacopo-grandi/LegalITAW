# WF2-036 — Software licensing: titolarità dei risultati, componenti a codice aperto, deposito del sorgente, verifica e responsabilità per pretese di terzi

**Stato: draft, in attesa di validazione professionale. Non `pilot_ready`. Nulla è stato caricato su
Notion, nessun commit è stato eseguito.**

## In una riga

Una socia dello studio chiede un redline circoscritto sulla bozza che il fornitore del gestionale
chiede al cliente di firmare. Il difetto principale non è costruito ad arte: è la clausola di
titolarità che i fornitori di servizi ICT scrivono davvero, per cui il cliente paga uno sviluppo su
commessa e riceve una licenza non esclusiva per uso interno.

## Coordinate

| Campo | Valore |
|---|---|
| Macro-area | IP / Technology |
| Verticale | software licensing |
| Use-case family (board) | Review and redline |
| Workflow family / subtask | `document_review` / `targeted_redline` |
| Data di riferimento | lunedì 16 ottobre 2028, fascicolo *ex ante* |
| Committente | una socia dello studio |
| Deliverable | `contratto_redline.docx` con revisioni tracciate + `nota_delle_modifiche.md`, otto sezioni, massimo 2.200 parole |
| Documenti | 7 — un DOCX (la bozza da revisionare) e sei PDF |
| Issue di merito | 17 |
| Controlled non-issue | 7 |
| Criteri atomici | 58 — 12 a verifica meccanica, 46 al judge |
| Fonti ammesse | 13, elenco chiuso, congelate al 28 agosto 2026 |

## Struttura

```
WF2-036_licenza-software-titolarita-open-source/
├── README.md
├── task_spec.json
├── public/
│   ├── 01_task.md                     l'incarico
│   ├── 02_reference_pack.md           testo delle norme e delle licenze utilizzabili
│   ├── 03_legal_sources.md            registro delle fonti, elenco chiuso, data di congelamento
│   ├── response_template.md           struttura attesa dei due file del deliverable
│   └── documents/                     i sette documenti del fascicolo
├── private/
│   ├── evaluation_criteria.md         rubrica in prosa, a livello di issue
│   ├── criteria_atomized.md           rubrica atomizzata, forma a campi
│   ├── rubric.json
│   ├── runtime_routing.json           instradamento + procedura di resa del redline per il judge
│   └── review_notes.md
├── source/
│   ├── authoring/
│   │   ├── challenge_map.json
│   │   ├── fonti_documentali.md       esemplare reale seguito per ciascun documento
│   │   ├── anagrafica.json
│   │   ├── date_e_valori_verificati.md
│   │   ├── verifica_wf2_036.py
│   │   ├── gold_standard.md           nota delle modifiche + verifica contro la rubrica
│   │   ├── gold_redline.docx          il redline gold, con sedici modifiche tracciate
│   │   ├── distractor.md
│   │   └── legal_validation.md
│   └── gen/
│       ├── comune_036.py              anagrafica condivisa
│       ├── contratto_036.py           testo della bozza: sorgente unica di .docx e .md
│       ├── build_contratto_docx.py    genera il documento 01
│       ├── build_contratto_md.py      genera la versione markdown canonica
│       ├── build_gold_redline.py      genera gold_redline.docx dal documento 01
│       ├── docs_036.py                genera i documenti 02-07
│       └── build_rubric_036.py        genera rubric.json + criteria_atomized.md
└── runs/README.md
```

## Come si rigenera

```bash
cd batch_WF2-035_037/WF2-036_licenza-software-titolarita-open-source
python3 source/authoring/verifica_wf2_036.py --md          # deve dare 0 errori
python3 source/gen/docs_036.py                             # documenti 02-07 (pdf + md)
python3 source/gen/build_contratto_md.py                    # documento 01, versione markdown
python3 source/gen/build_contratto_docx.py \
        public/documents/01_bozza_contratto_licenza_e_sviluppo_v2.docx
python3 source/gen/build_gold_redline.py \
        public/documents/01_bozza_contratto_licenza_e_sviluppo_v2.docx \
        source/authoring/gold_redline.docx
python3 source/gen/build_rubric_036.py
cd .. && python3 _tools/verifica_collisioni.py \
  WF2-036_licenza-software-titolarita-open-source/source/authoring/anagrafica.json
```

I generatori del `.docx` richiedono `python-docx`. La validazione del redline contro lo schema OOXML e
la resa in PDF per il controllo visivo delle revisioni sono state eseguite a parte con gli strumenti
della skill `docx`; non sono necessarie alla rigenerazione.

## Come è costruita la difficoltà

Sei meccanismi:

1. **Presenza contro adeguatezza.** Ogni clausola del perimetro esiste e sembra a posto. Il difetto è
   nel livello o nella definizione: la titolarità è concessa come licenza non esclusiva invece che
   trasferita; la garanzia sui componenti a codice aperto è tarata sulla sola distribuzione; il deposito
   c'è ma i suoi eventi di rilascio non comprendono l'inadempimento; la manleva c'è ma esclude proprio i
   componenti di terze parti.
2. **Gerarchia fra documenti.** L'articolo 8 rinvia all'Accordo di deposito per gli eventi di rilascio, e
   l'Accordo li restringe a due. Chi legge solo la bozza conclude che il deposito è presidiato.
3. **Ruolo formale contro ruolo sostanziale.** Un modulo qualificato nell'Allegato B come Componente
   Preesistente del Fornitore è stato in realtà commissionato a uno sviluppatore autonomo dopo l'avvio
   del Progetto. La qualificazione formale serve a sottrarlo alla titolarità del Cliente.
4. **Fatti distribuiti e aritmetica delle date.** La smentita di quella qualificazione emerge solo
   confrontando la Data di Inizio, che sta nelle premesse della bozza, con la data del contratto d'opera,
   che sta in un altro documento. Nessun documento lo dice.
5. **Dichiarazione di parte smentita dai documenti.** L'email del referente commerciale afferma che la
   titolarità del codice è del Cliente, che il sorgente è depositato e aggiornato e che i componenti a
   codice aperto sono tutti a licenza permissiva. Tutte e tre le affermazioni sono contraddette dagli
   allegati.
6. **Combinazione di condizioni, non licenza.** Fra i cinque componenti a codice aperto quello che
   genera l'obbligo è l'unico che è insieme **modificato** e **incluso** negli artefatti consegnati. Gli
   altri quattro sono neutralizzati da una combinazione diversa di licenza, collegamento, modifica e
   inclusione. È la combinazione, non il nome della licenza, a determinare l'effetto: chi ragiona per
   nome di licenza sovra-segnala, e quattro criteri di tipo `assenza` lo misurano.

## Che cosa il caso non misura

La convenienza economica del rinnovo. Il massimale generale dell'articolo 12, il collaudo con
accettazione tacita, la clausola compromissoria, la riservatezza, la durata e il trattamento dei dati
personali: sono fuori dal perimetro dell'incarico, e la loro modifica è penalizzata. La ragione è
duplice — non riusare le leve di un caso esistente sul verticale contiguo, e rendere verificabile il
test di sovra-intervento proprio dei redline circoscritti.

## Che cosa manca prima del freeze

1. Calibrazione del Passo 5: il gold ai tre judge, il fallimento del distrattore misurato.
2. Implementazione del controllo meccanico A.4 sulle revisioni fuori perimetro.
3. Collaudo della procedura di resa del redline in testo per il judge: quaranta criteri su cinquantotto
   ne dipendono.
4. Lettura blind di un professionista e risposta alle dieci domande di
   `source/authoring/legal_validation.md`, a partire dalla prima, che riguarda il soggetto su cui grava
   l'obbligo della sezione 13 della licenza del componente modificato.
