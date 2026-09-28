# WF2-094 - Due diligence urbanistica sul compendio di strada dei Gerbidi

`Dossier analysis` - Real Estate & Construction - difficolta medium - pack medium.

Il caso assiste Immobiliare Cordevalle S.r.l., promissaria acquirente alla data del 2026-10-06. Il fascicolo contiene 7 allegati; la busta
privata contiene 15 issue di merito, 4 controlled non-issue e 58 criteri atomici.

## Che cosa e pubblico e che cosa non lo e

Pubblico: `public/01_task.md`, `public/02_reference_pack.md`,
`public/03_legal_sources.md`, `public/response_template.md`, `public/documents/`.

Privato: challenge map, rubrica in prosa, criteri atomizzati, `rubric.json`,
`runtime_routing.json`, gold standard, distrattore, tabella delle date verificate,
elenco chiuso delle fonti, note di validazione.

## Deliverable atteso

`real_estate_red_flag_matrix.md`, markdown, entro 2600 parole.

## Verifiche

```
python3 source/gen/verifica_date_e_codici.py
python3 source/gen/valida_batch.py
python3 ../_tools/validate_case.py WF2-094_due-diligence-urbanistica
python3 ../_tools/check_gold.py WF2-094_due-diligence-urbanistica
```

**Stato: `draft_for_legal_validation`.** Nessun run eseguito, nessuna calibrazione
con judge, nessuna validazione giuridica professionale.
