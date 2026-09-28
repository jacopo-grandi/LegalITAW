# `generic_agent`: harness ufficiale di LegalITA v2

Il vecchio runtime interveniva proprio dove il benchmark avrebbe dovuto
osservare il modello: scandiva il lavoro in esplorazione e finalizzazione,
cambiava i tool disponibili, mostrava il budget residuo e pretendeva una
chiamata `submit`. `generic_agent` rimuove questa regia. Il suo compito è più
sobrio: prepara un ambiente isolato, inoltra i messaggi, esegue le azioni e
registra ciò che è accaduto.

## Contratto della run

Il contenuto esatto di `public/01_task.md` diventa il messaggio utente. Il
system prompt descrive soltanto il workspace: fonti in `documents/`, appunti in
`scratch/`, deliverable in `output/` e, con il profilo `production`, istruzioni
tecniche in `skills/`. Tutti questi percorsi sono relativi alla radice che
`bash` riceve come directory corrente. Nessun campo di `task_spec.json`, nessun
filename privato e nessun criterio della rubrica entra nella conversazione.

Nel profilo normalizzato dei cento task, `generic_agent` è dichiarato fra le
modalità supportate e `output_mode` vale `prompt_only_free_artifacts`. I campi
`tool_allowlist`, `agentic_instructions` e `agentic_output_format` restano nel
corpus esclusivamente per riprodurre il runtime storico `agentic_workspace` e
non vengono inoltrati al modello nella lane ufficiale.

I sei tool — `bash`, `read`, `write`, `edit`, `glob`, `grep` — sono esposti con
lo schema nativo del provider e restano disponibili a ogni turno. Il transcript
normalizzato viene tradotto per Anthropic, OpenAI e gli endpoint
OpenAI-compatibili di Gemini e Novita; il modello riceve le osservazioni dei
tool nella forma prevista dalla propria API. Se una risposta contiene più tool
call, l'harness le esegue tutte prima di proseguire.

Il loop si arresta alla prima risposta priva di tool call. Non esistono
`record_decision`, coverage obbligatoria, fase finale o `submit`; il modello può
leggere ancora una fonte dopo aver iniziato a scrivere, correggere un file o
produrre più deliverable. I limiti di turni, tempo e costo rimangono esterni alla
conversazione. Se il modello termina senza lasciare file in `output/`, la run è
un fallimento operativo e viene conservata come tale.

## Isolamento

La copia dei documenti pubblici è read-only e la directory privata non viene
montata. `read`, `write`, `edit`, `glob` e `grep` risolvono ogni percorso dentro
la radice temporanea; i tentativi di attraversamento e le scritture fuori da
`scratch/` o `output/` vengono respinti.

Una shell cambia il livello del problema: un controllo applicativo sui path non
basta. Per questo `bash` viene avviato soltanto se il preflight riesce ad
applicare un sandbox OS. L'implementazione corrente usa `sandbox-exec` su macOS,
con ambiente ripulito, rete negata, lettura limitata al workspace e ai runtime
di sistema, scrittura limitata alle due directory previste. La semplice
presenza dell'eseguibile non è considerata sufficiente: il preflight applica un
profilo di prova prima di chiamare il modello. Su una macchina priva di backend
compatibile la run si ferma; non esiste un fallback silenzioso alla shell host.

## Profili

`bare` è la configurazione principale del benchmark. Misura modello più
filesystem isolato e tool generici. `production` mantiene lo stesso system
prompt di base e lo stesso toolset, ma monta istruzioni tecniche, identiche per
tutti i modelli, sulla creazione e verifica di DOCX, XLSX e PPTX. Il profilo e
l'hash del prompt sono registrati nel manifest: risultati ottenuti con profili
diversi non vanno mescolati nella stessa classifica. Il manifest conserva anche
l'inventario e gli hash delle singole skill, oltre all'hash degli schemi dei sei
tool.

## Uso

```bash
# Score principale: generic_agent + bare
legalitaw run \
  --model gpt-5.6-luna \
  --tasks WF2-001 WF2-002 \
  --profile bare \
  --max-agent-steps 40 \
  --timeout-seconds 900 \
  --max-agent-cost-usd 5

# Capacità operativa con skill documentali
legalitaw run \
  --model claude-sonnet-4-6 \
  --tasks WF2-001 \
  --profile production
```

La valutazione parte soltanto dopo che il workspace è stato chiuso. Tutti i
file di `output/` vengono acquisiti: per PDF, DOCX, XLSX e PPTX il runtime
conserva il binario e un'estrazione testuale giudicabile; per gli altri formati
mantiene almeno contenuto o metadati, hash e dimensione. Trace, uso token, costo,
latenza, motivo di arresto e configurazione del sandbox restano nel bundle di
audit. `agent_transcript.json` conserva la conversazione normalizzata; non
contiene il reasoning nascosto che i provider non restituiscono.

## Verifica offline

```bash
env PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m unittest \
  checks.test_generic_agent_harness \
  checks.test_workflow2_agentic_workspace \
  checks.test_agentic_workflow_runtime
```

I test coprono la parità del toolset, l'identità del messaggio utente, il
confine public/private, la libertà dei nomi di output, l'arresto naturale e la
compatibilità con il runtime precedente. La prova effettiva di `sandbox-exec`
resta un controllo di preflight della macchina di run: ambienti già confinati,
come alcuni runner CI, possono vietare correttamente l'annidamento di un secondo
sandbox.
