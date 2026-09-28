# WF2-098 - Garanzie ambientali nella cessione del ramo d'azienda Praterno

`Review and redline` - Environmental, Energy & ESG - difficolta medium - pack medium.

Il caso assiste Nordovest Polimeri S.p.A., cessionaria del ramo d'azienda alla data del 2026-11-18. Il fascicolo contiene 7 allegati; la busta
privata contiene 14 issue di merito, 4 controlled non-issue e 56 criteri atomici.

## Che cosa e pubblico e che cosa non lo e

Pubblico: `public/01_task.md`, `public/02_reference_pack.md`,
`public/03_legal_sources.md`, `public/response_template.md`, `public/documents/`.

Privato: challenge map, rubrica in prosa, criteri atomizzati, `rubric.json`,
`runtime_routing.json`, gold standard, distrattore, tabella delle date verificate,
elenco chiuso delle fonti, note di validazione.

## Deliverable atteso

`environmental_schedule_redline.docx + note.md`, docx con revisioni tracciate e markdown, entro 2600 parole.

## Verifiche

```
python3 source/gen/verifica_date_e_codici.py
python3 source/gen/valida_batch.py
python3 ../_tools/validate_case.py WF2-098_garanzie-ambientali-asset-deal
python3 ../_tools/check_gold.py WF2-098_garanzie-ambientali-asset-deal
```

**Stato: `draft_for_legal_validation`.** Nessun run eseguito, nessuna calibrazione
con judge, nessuna validazione giuridica professionale.
