# CLI `legalitaw`

**Stato:** implementata
**Ambito:** generazione interna e valutazione di run interne o esterne  
**Fuori ambito:** revisione dello scaffolding e audit del leakage, da affrontare separatamente

I comandi `legalitaw` mostrati in questa pagina sono l'interfaccia operativa del benchmark.
La pagina nasce come nota di design della CLI v2 del repository legal-ITA: le sezioni 1 e 8
conservano quel contesto.

## 1. Il problema da risolvere

Il motore attuale sa già generare e valutare i task Workflow 2.0, ma espone la struttura interna del repository a chi lo usa. Una run interna viene salvata in cartelle per modello e timestamp; `evaluate-run`, invece, si aspetta una directory nella quale le cartelle `WF2-xxx` siano figlie dirette. Per valutare la run Luna del 9 settembre 2026 è stato quindi necessario costruire una directory temporanea di symlink. È un attrito artificiale: gli artifact esistono, i manifest identificano i task, eppure l'utente deve normalizzare a mano il layout.

La CLI v2 deve eliminare questo passaggio. Generazione e scoring restano operazioni distinte, ma condividono lo stesso formato logico di run e lo stesso resolver dei risultati. La provenienza — run interna, cartella esterna o ZIP — rimane nei metadati; non determina più un percorso di valutazione diverso.

## 2. Interfaccia proposta

L'entry point è `legalitaw`.

### 2.1 Generare una run interna

```bash
legalitaw run --model gpt-5.6-luna
```

Il comando usa automaticamente il corpus `task_workflow2.0`, la modalità `generic_agent` con profilo `bare` e tutti i task disponibili. La generazione, per impostazione predefinita, non avvia il judge.

Per limitare la run ai primi task nell'ordine canonico:

```bash
legalitaw run --model gpt-5.6-luna --limit 10
```

Per generare e avviare lo scoring al termine della run:

```bash
legalitaw run --model gpt-5.6-luna --limit 10 --score
```

`--score` non introduce un secondo percorso di valutazione: congela le submission prodotte e invoca internamente lo stesso servizio usato dal sottocomando `score`.

### 2.2 Valutare risultati esistenti

```bash
legalitaw score results/workflow2-agentic-100-luna-run1
```

Lo stesso comando accetta una run esterna o uno ZIP:

```bash
legalitaw score /percorso/risultati-next-os
legalitaw score /percorso/run-esterna.zip
```

Non sono richiesti symlink, estrazioni manuali o directory intermedie. `evaluate` può essere mantenuto come alias di `score`, ma la documentazione deve indicare un solo nome canonico.

## 3. Semantica di `run`

`legalitaw run` applica queste regole:

1. il corpus predefinito è `task_workflow2.0`;
2. la modalità predefinita è `generic_agent` con profilo `bare`; `production` aggiunge soltanto skill tecniche documentali standardizzate;
3. `--model` identifica un solo sistema per run;
4. senza selettori vengono richiesti tutti i task del corpus;
5. `--limit N` seleziona i primi `N` task dopo l'eventuale `--start-at`;
6. `--tasks WF2-001 WF2-017` permette una selezione esplicita;
7. `--tasks` e `--limit` non possono essere usati insieme;
8. il default è generation-only;
9. `--score` valuta soltanto dopo che la fase di generazione è terminata e le submission sono state congelate;
10. errori e retry vengono registrati senza cancellare i tentativi precedenti.

La run scrive un manifest di livello superiore che conserva almeno:

```json
{
  "schema_version": "legalita_v2_run_manifest_v1",
  "run_id": "...",
  "model": "gpt-5.6-luna",
  "corpus": "task_workflow2.0",
  "requested_task_ids": ["WF2-001", "WF2-002"],
  "completed_task_ids": ["WF2-001"],
  "failed_task_ids": ["WF2-002"],
  "attempts": {
    "WF2-001": ["percorso/del/tentativo"],
    "WF2-002": ["percorso/del/tentativo"]
  }
}
```

Il manifest non duplica gli artifact e non impone subito una migrazione del layout storico. Fornisce al resolver una mappa affidabile fra `task_id` e tentativi disponibili.

## 4. Semantica di `score`

Il comando ha una forma breve:

```bash
legalitaw score SOURCE
```

`SOURCE` può essere:

- una directory con cartelle `WF2-xxx` dirette;
- una run interna annidata per modello e timestamp;
- una directory esterna con deliverable;
- un file ZIP;
- una directory prodotta dalla nuova CLI e accompagnata dal manifest v2.

La configurazione diagnostica predefinita usa un solo judge:

```text
strategy: batched_single
provider: openai
model: gpt-5.6-luna
batch size: 10
reviewer: nessuno
```

Sonnet o un altro reviewer entra in gioco soltanto attraverso un'opzione esplicita. La scelta del judge, la strategia, i costi stimati e l'assenza di reviewer devono comparire nel manifest dello scoring.

## 5. Resolver universale dei risultati

Il resolver esplora ricorsivamente la sorgente e produce una mappa:

```text
task_id -> submission selezionata
```

Per ogni candidato legge, quando presenti, `submission.json`, `run_manifest.json`, `failure.json` e tutti gli artifact leggibili (`.md`, `.txt`, `.docx`, `.pdf`). I nomi di output privati non sono condizioni di ingestione. La selezione segue un ordine stabile:

1. un tentativo `completed` prevale su un tentativo `failed`;
2. fra più tentativi completati viene scelto quello con timestamp più recente;
3. un `submission.json` valido prevale sull'inferenza basata soltanto sui nomi dei file;
4. ogni duplicato e la relativa decisione vengono registrati nel preflight;
5. se due candidati restano indistinguibili, il resolver si ferma e chiede una selezione esplicita invece di scegliere arbitrariamente.

Questa logica avrebbe gestito direttamente il doppio WF2-011 della run Luna: il tentativo completato delle 14:21 avrebbe prevalso su quello fallito delle 14:11.

## 6. Denominatore, task mancanti e run parziali

Il denominatore non può essere dedotto sempre dal numero di cartelle trovate. Una run richiesta su cento task e terminata con sette fallimenti è diversa da una run deliberatamente limitata a novantatré task.

Si applicano quindi queste regole:

- se esiste un manifest, `requested_task_ids` definisce il denominatore;
- i task richiesti ma falliti o mancanti valgono zero nello score completo e restano visibili come errori tecnici;
- se il manifest manca, il resolver usa i task scoperti e marca il risultato come `partial/inferred`;
- `--expected all` forza il denominatore all'intero corpus;
- `--completed-only` produce una diagnostica sui soli output validi, senza presentarla come score completo della run;
- `--expected all` e `--completed-only` sono incompatibili.

Esempi:

```bash
# Score end-to-end: gli output mancanti pesano zero
legalitaw score results/run-luna --expected all

# Diagnostica dei soli task completati
legalitaw score results/run-luna --completed-only
```

Ogni riepilogo deve mostrare insieme `overall_score`, task richiesti, task completati, fallimenti tecnici, task mancanti, coverage e numero di criteri unresolved. Un punteggio privo del suo denominatore non è un risultato interpretabile.

## 7. Output e ripresa

Lo scoring salva:

```text
score-run/
├── run_manifest.json
├── preflight.json
├── cost_estimate.json
├── summary.json
├── scores/
│   └── WF2-xxx.json
└── errors/
    └── WF2-xxx.json
```

La ripresa è attiva per impostazione predefinita: uno score valido e coerente con hash della submission, versione della rubrica e configurazione del judge viene riutilizzato. Se uno di questi elementi cambia, il task viene rivalutato. `--fresh` crea una nuova valutazione senza riusare checkpoint precedenti.

Il semplice fatto che `scores/WF2-001.json` esista non basta per il resume: devono coincidere almeno hash dell'artifact, `rubric_version`, `methodology_version`, judge model, strategia e batch size.

## 8. Compatibilità

La nuova CLI deve delegare ai componenti esistenti per caricamento del corpus, import delle submission, judge, cost guard e aggregazione. Non conviene duplicare il motore dentro un wrapper più gradevole.

L'entry point viene aggiunto a `pyproject.toml`:

```toml
[project.scripts]
legalitaw = "legalitaw.cli.v2:main"
```

I risultati storici restano valutabili grazie al resolver ricorsivo; nessuna migrazione distruttiva delle cartelle è necessaria.

## 9. Errori e messaggi operativi

La CLI deve fallire con messaggi brevi e azionabili. Alcuni esempi:

```text
93/100 submission completate; 7 fallimenti di generazione.
Valutazione completa: i 7 fallimenti peseranno zero.
Usa --completed-only per una diagnostica dei soli output validi.
```

```text
WF2-011: trovati 2 tentativi; selezionato il tentativo completed più recente.
Dettagli: preflight.json
```

```text
Configurazione judge: gpt-5.6-luna, batched_single, nessun reviewer.
Costo stimato: $X.XX. Checkpoint riutilizzabili: 61/93.
```

## 10. Criteri di accettazione

L'implementazione è pronta quando:

1. `legalitaw run --model MODEL --limit 3` genera esattamente tre task e non chiama alcun judge;
2. aggiungendo `--score`, le tre submission vengono valutate dallo stesso servizio di `legalitaw score`;
3. `legalitaw score results/workflow2-agentic-100-luna-run1` scopre la struttura annidata senza symlink;
4. il resolver preferisce il tentativo completato di WF2-011 a quello fallito;
5. directory piatte, directory annidate e ZIP producono lo stesso score a parità di artifact;
6. una run parziale non viene presentata come completa;
7. `--expected all` conta correttamente task mancanti e fallimenti nel denominatore;
8. `--completed-only` dichiara esplicitamente che lo score è parziale;
9. il resume invalida un checkpoint quando cambia artifact, rubrica o configurazione del judge;
10. la configurazione predefinita non effettua chiamate a Sonnet;
11. preflight, stima dei costi e manifest vengono scritti prima della prima chiamata al judge;
12. la CLI storica continua a superare i test esistenti.

## 11. Sequenza di implementazione

Il lavoro può procedere in quattro passaggi. Prima si introduce il resolver universale, coperto da fixture per layout piatto, annidato, ZIP, duplicati e tentativi falliti. Poi si aggiunge il manifest complessivo alle run interne. Il terzo passaggio costruisce `legalitaw` come facciata dei servizi esistenti; l'ultimo chiude resume, messaggi operativi e test end-to-end.

L'audit del leakage resta volutamente fuori da questa modifica. Mescolarlo alla nuova CLI renderebbe difficile capire se un cambiamento di score dipende dall'ingestione dei risultati o dalla riscrittura dei task. Prima si stabilizza il percorso `run -> results -> score`; subito dopo si può intervenire sugli indizi pubblici con un'ablazione controllata.
