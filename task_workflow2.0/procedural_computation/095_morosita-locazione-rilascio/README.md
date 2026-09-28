# WF2-095 - Morosità nella locazione di corso del Popolo e rilascio dell'immobile

`Procedural timeline` - Real Estate & Construction - difficolta low - pack small.

Il caso assiste Sartiglia Immobiliare S.r.l., locatrice intimante alla data del 2026-08-06. Il fascicolo contiene 6 allegati; la busta
privata contiene 12 issue di merito, 3 controlled non-issue e 40 criteri atomici.

## Che cosa e pubblico e che cosa non lo e

Pubblico: `public/01_task.md`, `public/02_reference_pack.md`,
`public/03_legal_sources.md`, `public/response_template.md`, `public/documents/`.

Privato: challenge map, rubrica in prosa, criteri atomizzati, `rubric.json`,
`runtime_routing.json`, gold standard, distrattore, tabella delle date verificate,
elenco chiuso delle fonti, note di validazione.

## Deliverable atteso

`lease_enforcement_timeline.md`, markdown, entro 1900 parole.

## Verifiche

```
python3 source/gen/verifica_date_e_codici.py
python3 source/gen/valida_batch.py
python3 ../_tools/validate_case.py WF2-095_morosita-locazione-rilascio
python3 ../_tools/check_gold.py WF2-095_morosita-locazione-rilascio
```

**Stato: `draft_for_legal_validation`.** Nessun run eseguito, nessuna calibrazione
con judge, nessuna validazione giuridica professionale.
