# task_workflow2.0

Corpus locale canonico dei task atomizzati Workflow 2.0. Notion è una fonte storica in sola lettura:
le correzioni e le run di questa cartella non modificano le pagine originali.

## Stato del corpus

Sono materializzati 100 task, 5.032 criteri atomizzati e 683 allegati; non risultano ID, route o
input pubblici mancanti.

Dal 21 settembre 2026 i `response_template.md` restano conservati come materiale storico di
authoring, ma non sono visibili al modello. La migrazione e il suo effetto sul denominatore sono
documentati in [`../docs/RESPONSE_TEMPLATE_RETIREMENT_2026-09-21.md`](../docs/RESPONSE_TEMPLATE_RETIREMENT_2026-09-21.md).

- `WF2-001`–`WF2-100` sono `pilot_ready` per test diagnostici.
- `WF2-011`–`WF2-020`, importati e revisionati il 24 agosto 2026, includono source pack ufficiali chiusi, routing completo e le otto decisioni di design confermate nel registro del pilot.
- `WF2-021`–`WF2-030`, normalizzati il 25 agosto 2026 dalla staging area `task_workflow2.0.1`, usano lo stesso confine public/private, prompt autosufficiente, reference pack chiuso, profilo runtime e routing dei primi venti.
- `WF2-031`–`WF2-100`, migrati il 4 settembre 2026, hanno profilo e rubrica normalizzati, routing
  completo; gli snapshot pre-migrazione restano nel repository di authoring legal-ITA.

`pilot_ready` significa pronto per il pilot comparativo, non gold legale definitivo: il campo `gold_legal_signoff` resta `pending` finché non viene svolto il sign-off blind.

## Struttura

I task sono raggruppati per famiglia operativa:

- `document_review_and_revision/`
- `procedural_computation/`
- `dossier_analysis/`

Ogni task contiene:

- `public/`: prompt, reference pack, documenti e altre note che il modello può vedere;
- `private/`: criteri, rubriche, valutazione narrativa e note di revisione;
- `task_spec.json`: metadati, input ammessi e stato di revisione.

Questa separazione è vincolante: durante la generazione il modello riceve soltanto gli input elencati in `public_inputs`; i contenuti `private/` entrano solo nella valutazione.

## Criteri e instradamento

`private/criteria_atomized.md` è la fonte canonica del task. `private/rubric.json` è la rappresentazione machine-readable e va rigenerata dopo ogni modifica ai criteri.

I due campi descrivono assi indipendenti:

- `tipo`: operazione logica richiesta, per esempio `presenza`, `assenza`, `qualificazione`, `attribuzione`, `valore`;
- `verifica`: meccanismo di controllo, con valori `esatta`, `span`, `scansione`, `judge`.

Significato di `verifica`:

| Valore | Controllo |
|---|---|
| `esatta` | stringa o valore determinato in un contesto identificato |
| `span` | proposizione affermata in un passaggio individuabile |
| `scansione` | ricerca completa nell'ambito dichiarato, che può essere l'intero output o una sezione |
| `judge` | trattamento complessivo o coerenza fra più parti del deliverable |

Nel profilo eseguibile l'operazione logica viene ulteriormente resa esplicita
come `required_presence`, `prohibited_presence` o
`conditional_if_mentioned`, separandola dalla classe di verifica e dallo scope.
Il file `private/runtime_routing.json` materializza per ogni criterio classe,
logica e scope effettivi. Non restano criteri senza route runtime.

## Policy sui dati mancanti

Un criterio non deve obbligare il modello a inventare fatti. Se il fascicolo non consente di concludere, scegliere e rendere pubblica una delle seguenti soluzioni:

1. integrare i dati mancanti;
2. accettare campi decisionali o alternative motivate;
3. premiare l'impossibilità motivata di concludere e l'indicazione dei documenti necessari.

Una conclusione corretta non basta quando può derivare da un percorso errato. Nei computi il criterio deve controllare evento iniziale, natura della data o del termine, numero e tipo di giorni, festività e coerenza del trattamento nell'intero deliverable.

## Rigenerazione e validazione

Gli script che ricostruiscono i `rubric.json` dai criteri Markdown e validano schema, conteggi, ID,
file, allegati e hash (`tools/rebuild_rubrics.py`, `tools/validate_corpus.py`) sono strumenti di
authoring e restano nel repository legal-ITA, insieme agli snapshot `source/` di ogni task. In
LegalITA-W la coerenza del corpus è verificata dai test:

```bash
python3 -m pytest tests/test_workflow2_corpus.py
```

## Prima run

Readiness, rapporto di migrazione e tassonomia degli errori del pilot restano nel repository di
authoring legal-ITA. Prima della matrice completa, eseguire uno smoke test su un caso per
famiglia e sottoporlo ad audit umano. Il passo seguente è un batch di dieci; soltanto dopo si allarga
l'esecuzione ai cento task e alle repliche previste.

Per ogni run conservare almeno:

- risposta e artefatti prodotti;
- trace dei tool, per le run interne agentiche;
- latenza e token, se disponibili;
- esito per criterio con evidenza testuale;
- classe di verifica usata;
- tag di errore secondo la tassonomia del pilot.

Nei cento profili la lane interna primaria è `generic_agent`: il modello riceve
il testo di `public/01_task.md`, i documenti pubblici in sola lettura e i sei
tool generici `bash`, `read`, `write`, `edit`, `glob` e `grep`. L'output mode
normalizzato è `prompt_only_free_artifacts`; il runtime non impone nomi, numero
o struttura della consegna. Le modalità storiche `text_bundle` e
`agentic_workspace` compaiono ancora nei profili dei task, ma LegalITA-W esegue
solo `generic_agent`.

Ogni risultato per criterio usa il contratto `response_span_v1`: il judge deve
indicare estratti esatti della risposta e il runtime li localizza nell'artifact
con offset e righe. Omissioni e controlli di assenza sono registrati con lo
scope effettivo, senza creare falsi estratti; un estratto fuori dalla sezione
dichiarata non è prova valida. Gli stati `invalid` e `unavailable` identificano
invece un problema di evidenza del judge.

La validazione ha livelli distinti. Il comando strutturale può risultare verde
anche quando restano criteri `unassigned`, allegati mancanti o il
`gold_legal_signoff` è `pending`. Per dichiarare un task gold servono insieme:
integrità del fascicolo, routing completo di tutti i criteri, calibrazione del
judge su annotazioni umane e sign-off legale blind. Tutti i cento task hanno un
profilo runtime completo; il sign-off legale resta intenzionalmente separato.

La prima esecuzione va sottoposta ad audit manuale completo: lo scopo non è soltanto misurare i modelli, ma individuare criteri ambigui, non documentati o instradati al motore sbagliato.
