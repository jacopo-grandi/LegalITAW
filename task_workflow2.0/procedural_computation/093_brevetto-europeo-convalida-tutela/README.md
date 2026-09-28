# WF2-093 - Brevetto europeo EP 4 118 902: convalida in Italia, opposizione e tutela

`Procedural timeline` - IP & Technology - difficolta high - pack large.

Il caso assiste Nevalta Medical S.p.A., titolare del brevetto europeo EP 4 118 902 B1 alla data del 2026-11-10. Il fascicolo contiene 10 allegati; la busta
privata contiene 15 issue di merito, 4 controlled non-issue e 66 criteri atomici.

## Che cosa e pubblico e che cosa non lo e

Pubblico: `public/01_task.md`, `public/02_reference_pack.md`,
`public/03_legal_sources.md`, `public/response_template.md`, `public/documents/`.

Privato: challenge map, rubrica in prosa, criteri atomizzati, `rubric.json`,
`runtime_routing.json`, gold standard, distrattore, tabella delle date verificate,
elenco chiuso delle fonti, note di validazione.

## Deliverable atteso

`patent_timeline.md`, markdown, entro 3000 parole.

## Verifiche

```
python3 source/gen/verifica_date_e_codici.py
python3 source/gen/valida_batch.py
python3 ../_tools/validate_case.py WF2-093_brevetto-europeo-convalida-tutela
python3 ../_tools/check_gold.py WF2-093_brevetto-europeo-convalida-tutela
```

**Stato: `draft_for_legal_validation`.** Nessun run eseguito, nessuna calibrazione
con judge, nessuna validazione giuridica professionale.
