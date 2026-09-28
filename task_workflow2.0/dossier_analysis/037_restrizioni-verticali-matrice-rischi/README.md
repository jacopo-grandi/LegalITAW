# WF2-037 — Antitrust: restrizioni verticali in una rete di distribuzione selettiva ed esclusiva

**Stato: draft, in attesa di validazione professionale. Non `pilot_ready`. Nulla è stato caricato su
Notion, nessun commit è stato eseguito.**

## In una riga

Un produttore di utensili professionali riceve la diffida di un rivenditore sulla politica di prezzo. La
responsabile compliance chiede una matrice dei rischi. Sette dei quattordici elementi della matrice sono
clausole restrittive **ammesse**: il caso è costruito perché la sovra-qualificazione costi più della
sotto-qualificazione.

## Coordinate

| Campo | Valore |
|---|---|
| Macro-area | Antitrust & Competition |
| Verticale | restrizioni verticali |
| Use-case family (board) | Dossier analysis |
| Workflow family / subtask | `dossier_analysis` / `cross_document_issue_analysis` |
| Data di riferimento | venerdì 16 marzo 2029, fascicolo *in corso* |
| Committente | responsabile compliance e affari legali del fornitore |
| Deliverable | `matrice_rischi_antitrust.md`, otto sezioni, massimo 2.800 parole |
| Documenti | 9 — otto PDF e un foglio di calcolo |
| Issue di merito | 16 |
| Controlled non-issue | 7 |
| Criteri atomici | 58 — 13 a verifica meccanica, 45 al judge |
| Fonti ammesse | 14, elenco chiuso, tutte riprodotte verbatim, congelate al 28 agosto 2026 |

## Struttura

```
WF2-037_restrizioni-verticali-matrice-rischi/
├── README.md
├── task_spec.json
├── public/
│   ├── 01_task.md
│   ├── 02_reference_pack.md      testi verbatim del reg. 2022/720, degli Orientamenti 2022,
│   │                             della comunicazione de minimis, della l. 287/1990,
│   │                             del reg. 1/2003 e dell'art. 101 TFUE
│   ├── 03_legal_sources.md       registro delle fonti, elenco chiuso, data di congelamento
│   ├── response_template.md      struttura attesa e ELENCO CHIUSO delle etichette
│   └── documents/                i nove documenti del fascicolo
├── private/
│   ├── evaluation_criteria.md
│   ├── criteria_atomized.md
│   ├── rubric.json
│   ├── runtime_routing.json
│   └── review_notes.md
├── source/
│   ├── authoring/
│   │   ├── challenge_map.json
│   │   ├── fonti_documentali.md
│   │   ├── anagrafica.json
│   │   ├── date_e_valori_verificati.md
│   │   ├── verifica_wf2_037.py
│   │   ├── gold_standard.md
│   │   ├── distractor.md
│   │   └── legal_validation.md
│   └── gen/
│       ├── comune_037.py
│       ├── docs_037_a.py          documenti 01-03
│       ├── docs_037_b.py          documenti 04, 05, 06, 08, 09
│       ├── build_dati_mercato.py  documento 07 (xlsx + md)
│       └── build_rubric_037.py
└── runs/README.md
```

## Come si rigenera

```bash
cd batch_WF2-035_037/WF2-037_restrizioni-verticali-matrice-rischi
python3 source/authoring/verifica_wf2_037.py --md    # deve dare 0 errori
python3 source/gen/docs_037_a.py
python3 source/gen/docs_037_b.py
python3 source/gen/build_dati_mercato.py             # richiede openpyxl
python3 source/gen/build_rubric_037.py
cd .. && python3 _tools/verifica_collisioni.py \
  WF2-037_restrizioni-verticali-matrice-rischi/source/authoring/anagrafica.json
```

## La decisione che rende il caso valutabile

Un deliverable di qualificazione è normalmente invalutabile da un judge che non conosce il diritto:
«rischio alto» e «clausola problematica» non si confrontano. La soluzione adottata è un **elenco chiuso
di cinque etichette**, esposto al modello nel `response_template.md`:

`restrizione fondamentale` · `restrizione esclusa` · `coperta dall'esenzione` ·
`fuori dall'esenzione, da valutare` · `non restrittiva`

I criteri di qualificazione diventano confronti fra stringhe; il criterio sull'uso corretto delle
etichette diventa meccanico; e i sette divieti sui controlled non-issue diventano il controllo più solido
dei tre casi del batch, perché non chiedono al judge se un elemento «è segnalato come rischio» ma quale
etichetta compare nella riga. Il costo — l'elenco rivela che esiste una categoria «restrizione esclusa»
distinta da «restrizione fondamentale» — è dichiarato in `private/review_notes.md` e sottoposto al
validatore.

## Come è costruita la difficoltà

1. **Soglia esatta e metodo di calcolo.** La quota del fornitore è il 34,1 per cento su un perimetro di
   mercato e il 22,4 per cento sull'altro; il prospetto dell'ufficio studi dichiara di non prendere
   posizione. Il metodo impone di usare i dati dell'anno civile precedente e prevede un periodo di due
   anni civili quando la soglia viene superata dopo esserne stata sotto: nel caso la soglia è superata
   per la prima volta proprio nell'anno dei dati, e l'esenzione **non è ancora venuta meno**. Una
   qualificazione per intuizione sbaglia in entrambe le direzioni.
2. **Fatti distribuiti.** La restrizione fondamentale sui prezzi non è in nessun documento preso da
   solo: la circolare raccomanda i prezzi, cosa consentita; il monitoraggio non è imposizione;
   l'obbligo di segnalazione da solo non basta. È l'email dell'area manager, tre mesi più tardi e in un
   altro documento, che aggiunge la minaccia di sospendere le forniture.
3. **Presenza contro adeguatezza, applicata alla qualificazione.** Cinque clausole restrittive del
   fascicolo sono coperte dall'esenzione e due non sono restrittive. Il modello che qualifica come
   violazione ogni clausola che limita la libertà del rivenditore perde sette criteri di tipo `assenza`
   senza guadagnarne nessuno.
4. **Due regimi che si somigliano.** La restrizione fondamentale elimina l'esenzione per l'intero
   accordo; la restrizione esclusa non è esentata ma è scindibile. Il fascicolo contiene entrambe.
5. **Dichiarazione di parte smentita.** La nota del direttore commerciale afferma quattro cose: di
   essere sotto il 30 per cento, che i prezzi sono soltanto raccomandati, che il divieto di marketplace
   è vietato dal 2022 e che il de minimis mette al riparo. Nessuna delle quattro regge, e la terza è un
   errore di segno opposto: sovra-segnala una clausola ammessa.
6. **Evidenze incomplete.** La doppia tariffazione non è qualificabile senza i dati di costo, che il
   fascicolo dichiara di non contenere; la quota dell'acquirente, che la norma richiede accanto a
   quella del fornitore, non è documentata.

## Che cosa il caso non misura

L'individuazione dell'autorità competente. La quantificazione dell'esposizione sanzionatoria. La scelta
fra presentare impegni, avvalersi di un programma di clemenza o non rappresentare nulla. Il profilo
orizzontale del comitato commerciale, che sarebbe il rilievo più grave del fascicolo e che è
deliberatamente collocato fra le questioni riservate al parere legale: qualificarlo avrebbe spostato il
caso dalle restrizioni verticali agli accordi orizzontali.

## Che cosa manca prima del freeze

1. Calibrazione del Passo 5: il gold ai tre judge, il fallimento del distrattore misurato. Il punto più
   importante è verificare che i sette divieti sui controlled non-issue e i criteri positivi che
   condividono con essi l'`issue_id` siano indipendenti.
2. Implementazione dei controlli meccanici A.4 e della distinzione di contesto fra C.3 e C.4.
3. Lettura blind di un professionista e risposta alle dieci domande di
   `source/authoring/legal_validation.md`, a partire dalla prima sulla combinazione che integra
   l'imposizione del prezzo di rivendita e dalla seconda sull'ambiguità del termine iniziale del periodo
   di due anni civili.
