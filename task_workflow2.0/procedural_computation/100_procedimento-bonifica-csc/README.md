# WF2-100 - Procedimento di bonifica dopo il superamento delle soglie nel piazzale di Colderasso

`Procedural timeline` - Environmental, Energy & ESG - difficolta low - pack medium.

Il caso assiste Metalpiave S.p.A., responsabile dell'evento e gestore del sito alla data del 2026-10-27. Il fascicolo contiene 7 allegati; la busta
privata contiene 16 issue di merito, 4 controlled non-issue e 40 criteri atomici.

## Che cosa e pubblico e che cosa non lo e

Pubblico: `public/01_task.md`, `public/02_reference_pack.md`,
`public/03_legal_sources.md`, `public/response_template.md`, `public/documents/`.

Privato: challenge map, rubrica in prosa, criteri atomizzati, `rubric.json`,
`runtime_routing.json`, gold standard, distrattore, tabella delle date verificate,
elenco chiuso delle fonti, note di validazione.

## Deliverable atteso

`remediation_timeline.md`, markdown, entro 2400 parole.

## Verifiche

```
python3 source/gen/verifica_date_e_codici.py
python3 source/gen/valida_batch.py
python3 ../_tools/validate_case.py WF2-100_procedimento-bonifica-csc
python3 ../_tools/check_gold.py WF2-100_procedimento-bonifica-csc
```

**Stato: `draft_for_legal_validation`.** Nessun run eseguito, nessuna calibrazione
con judge, nessuna validazione giuridica professionale.
