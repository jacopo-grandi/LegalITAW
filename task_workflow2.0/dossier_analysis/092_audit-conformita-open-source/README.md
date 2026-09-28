# WF2-092 - Audit di conformità open source sulla piattaforma Solmarino

`Dossier analysis` - IP & Technology - difficolta medium - pack medium.

Il caso assiste Solmarino Software S.r.l., che fornisce il prodotto come apparecchiatura installata presso il cliente e come servizio erogato in cloud alla data del 2026-11-05. Il fascicolo contiene 8 allegati; la busta
privata contiene 12 issue di merito, 5 controlled non-issue e 54 criteri atomici.

## Che cosa e pubblico e che cosa non lo e

Pubblico: `public/01_task.md`, `public/02_reference_pack.md`,
`public/03_legal_sources.md`, `public/response_template.md`, `public/documents/`.

Privato: challenge map, rubrica in prosa, criteri atomizzati, `rubric.json`,
`runtime_routing.json`, gold standard, distrattore, tabella delle date verificate,
elenco chiuso delle fonti, note di validazione.

## Deliverable atteso

`open_source_audit.md`, markdown, entro 2400 parole.

## Verifiche

```
python3 source/gen/verifica_date_e_codici.py
python3 source/gen/valida_batch.py
python3 ../_tools/validate_case.py WF2-092_audit-conformita-open-source
python3 ../_tools/check_gold.py WF2-092_audit-conformita-open-source
```

**Stato: `draft_for_legal_validation`.** Nessun run eseguito, nessuna calibrazione
con judge, nessuna validazione giuridica professionale.
