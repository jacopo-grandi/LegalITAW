```text
█     █████  ███   ███  █     ███ █████  ███       █   █   
█░    █░░░░░█ ░░░ █ ░░█ █░     █░░ ░█░░░█ ░░█      █░  █░  
█░░   ████░░█░ ██░█████░█░░    █░░░ █░░░█████░████ █░█ █░░ 
█░░   █░░░░ █░░ █░█░░░█░█░░    █░░  █░░ █░░░█░░░░░░██░██░░ 
█████ █████░ ███ ░█░░░█░█████ ███░  █░░ █░░░█░░ ░░░█░░ █░░ 
 ░░░░░ ░░░░░  ░░░ ░░░  ░░░░░░░ ░░░   ░░  ░░  ░░     ░░░ ░░ 
  ░░░░░ ░░░░░  ░░░  ░   ░ ░░░░░ ░░░   ░   ░   ░      ░   ░ 
```

# LegalITA-W

**Legal Italian Agentic Workflows.** È un benchmark agentico di workflow legali italiani: 100 incarichi
realistici (WF2-001…WF2-100) e 5.032 criteri binari. Il modello lavora in un workspace isolato con
sei tool generici e consegna i propri deliverable, che una terna di giudici valuta criterio per
criterio.

Il repository contiene solo ciò che serve a eseguire e valutare il benchmark. Il materiale di
authoring (snapshot Notion, generatori dei documenti, piani di espansione, script di manutenzione)
resta nel repository legal-ITA.

## Contenuto

```text
legalitaw/
├── legalitaw/            # package Python
│   ├── agentic/          # loader dei task, workspace, harness generic_agent, artefatti, copertura
│   ├── modeling/         # gateway verso i provider, tool calling, telemetria
│   ├── evaluation/       # giudici, contesto del giudice, scoring dei criteri
│   ├── benchmark/        # orchestrazione delle run: generazione, scoring, checkpoint, aggregati
│   └── cli/              # comando `legalitaw`
├── task_workflow2.0/     # i 100 task (busta pubblica e busta privata)
├── docs/                 # metodologia, audit della terna, harness, CLI
└── tests/
```

Ogni task ha questa struttura:

- `public/`: ciò che vede il modello. Contiene l'incarico (`01_task.md`), il reference pack, le
  fonti ammesse e il fascicolo in `documents/`.
- `private/`: rubrica, routing runtime, criteri atomizzati, controlli deterministici e note di
  valutazione. Serve solo ai giudici.
- `task_spec.json`: identità, perimetro, input pubblici ammessi e deliverable del task.

## Installazione

Serve Python 3.10 o superiore.

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[test]"
cp .env.example .env   # poi inserisci le chiavi
```

Installa il package in modalità editabile: i percorsi dei task e dei risultati si risolvono a
partire dalla root del repository.

## Uso

Per generare una run su tutti i task, con il profilo `bare` (modello, filesystem isolato e sei tool
generici):

```bash
legalitaw run --model gpt-5.6-luna
legalitaw run --model gpt-5.6-luna --tasks WF2-001 WF2-002 --max-agent-cost-usd 5
```

Per valutare una run interna, una cartella esterna o uno ZIP:

```bash
legalitaw score results/agentic/<run>
```

Senza opzioni lo scoring usa la terna di giudici validata: servono `TYPESAFE_API_KEY`,
`OPENAI_API_KEY` e `ANTHROPIC_API_KEY`. La terna funziona così:

- Jev (A) e Luna (B) giudicano tutti i criteri.
- Opus (C) arbitra i disaccordi, i PASS la cui citazione non si ritrova nella risposta e un
  campione di audit del 5%.
- Il giudice vede il contesto compatto: i file testuali della busta pubblica, non i documenti.

Ogni elemento si può cambiare con le opzioni `--judge-*` e `--judge-context` (vedi `docs/CLI.md`).

Opzioni utili:

- `--preflight-only`: risolve la run, controlla i checkpoint e stima il costo senza chiamare i
  giudici.
- `--expected all`: fissa il denominatore ai 100 task.

I checkpoint vengono riusati finché non cambiano la submission, la rubrica, la configurazione dei
giudici o il contratto di valutazione. Un task con errori dei giudici viene rigiudicato. Una run
completa costa circa 20-24 dollari di giudici e dura circa 2 ore.

I dettagli sono in [`docs/CLI.md`](docs/CLI.md) e [`docs/generic_agent_harness.md`](docs/generic_agent_harness.md).

## Test

```bash
python3 -m pytest
```

I test non chiamano provider esterni.

## Documentazione

- [`docs/METODOLOGIA_v2.md`](docs/METODOLOGIA_v2.md): metodologia completa. Copre task, buste,
  criteri, perimetro chiuso delle fonti, esplorazione autonoma, giudici e scoring.
- [`docs/AUDIT_TERNA_2026-09-26.md`](docs/AUDIT_TERNA_2026-09-26.md): audit della terna di giudici.
- [`docs/CONTROLLI_DETERMINISTICI.md`](docs/CONTROLLI_DETERMINISTICI.md): controlli deterministici
  sovrapposti al judge.
- [`docs/RESPONSE_TEMPLATE_RETIREMENT_2026-09-21.md`](docs/RESPONSE_TEMPLATE_RETIREMENT_2026-09-21.md):
  ritiro dei template di risposta.
- [`task_workflow2.0/README.md`](task_workflow2.0/README.md): stato del corpus.

## Licenza

Il codice è distribuito con licenza MIT (vedi `LICENSE` e `NOTICE`). Parte delle convenzioni di
schema e dello scoring all-pass è adattata da Harvey LAB.
