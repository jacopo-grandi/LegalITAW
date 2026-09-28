# WF2-096 - Permesso di costruire e scadenze del cantiere di Sarezzana

`Procedural timeline` - Real Estate & Construction - difficolta medium - pack medium.

Il caso assiste Costruzioni Pratomagno S.p.A., titolare del permesso di costruire alla data del 2026-12-02. Il fascicolo contiene 7 allegati; la busta
privata contiene 15 issue di merito, 4 controlled non-issue e 50 criteri atomici.

## Che cosa e pubblico e che cosa non lo e

Pubblico: `public/01_task.md`, `public/02_reference_pack.md`,
`public/03_legal_sources.md`, `public/response_template.md`, `public/documents/`.

Privato: challenge map, rubrica in prosa, criteri atomizzati, `rubric.json`,
`runtime_routing.json`, gold standard, distrattore, tabella delle date verificate,
elenco chiuso delle fonti, note di validazione.

## Deliverable atteso

`construction_deadline_audit.md`, markdown, entro 2500 parole.

## Verifiche

```
python3 source/gen/verifica_date_e_codici.py
python3 source/gen/valida_batch.py
python3 ../_tools/validate_case.py WF2-096_permesso-di-costruire-cantiere
python3 ../_tools/check_gold.py WF2-096_permesso-di-costruire-cantiere
```

**Stato: `draft_for_legal_validation`.** Nessun run eseguito, nessuna calibrazione
con judge, nessuna validazione giuridica professionale.
