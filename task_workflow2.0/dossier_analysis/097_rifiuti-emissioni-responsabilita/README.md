# WF2-097 - Rifiuti, emissioni e responsabilità nel sito produttivo di Vellamonte

`Dossier analysis` - Environmental, Energy & ESG - difficolta high - pack large.

Il caso assiste Fonderia Alsemio S.p.A., destinataria del verbale di prescrizioni alla data del 2026-09-10. Il fascicolo contiene 9 allegati; la busta
privata contiene 16 issue di merito, 6 controlled non-issue e 72 criteri atomici.

## Che cosa e pubblico e che cosa non lo e

Pubblico: `public/01_task.md`, `public/02_reference_pack.md`,
`public/03_legal_sources.md`, `public/response_template.md`, `public/documents/`.

Privato: challenge map, rubrica in prosa, criteri atomizzati, `rubric.json`,
`runtime_routing.json`, gold standard, distrattore, tabella delle date verificate,
elenco chiuso delle fonti, note di validazione.

## Deliverable atteso

`environmental_compliance_memo.md`, markdown, entro 3200 parole.

## Verifiche

```
python3 source/gen/verifica_date_e_codici.py
python3 source/gen/valida_batch.py
python3 ../_tools/validate_case.py WF2-097_rifiuti-emissioni-responsabilita
python3 ../_tools/check_gold.py WF2-097_rifiuti-emissioni-responsabilita
```

**Stato: `draft_for_legal_validation`.** Nessun run eseguito, nessuna calibrazione
con judge, nessuna validazione giuridica professionale.
