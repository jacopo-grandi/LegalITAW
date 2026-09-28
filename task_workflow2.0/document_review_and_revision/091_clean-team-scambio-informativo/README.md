# WF2-091 - Clean team e scambio informativo nella joint venture Sinaldo

`Review and redline` - Antitrust & Competition - difficolta high - pack medium.

Il caso assiste Tramontina Azionamenti S.p.A., co-fondatrice della joint venture alla data del 2026-10-14. Il fascicolo contiene 7 allegati; la busta
privata contiene 16 issue di merito, 5 controlled non-issue e 69 criteri atomici.

## Che cosa e pubblico e che cosa non lo e

Pubblico: `public/01_task.md`, `public/02_reference_pack.md`,
`public/03_legal_sources.md`, `public/response_template.md`, `public/documents/`.

Privato: challenge map, rubrica in prosa, criteri atomizzati, `rubric.json`,
`runtime_routing.json`, gold standard, distrattore, tabella delle date verificate,
elenco chiuso delle fonti, note di validazione.

## Deliverable atteso

`clean_team_protocol_redline.docx + note.md`, docx con revisioni tracciate e markdown, entro 3000 parole.

## Verifiche

```
python3 source/gen/verifica_date_e_codici.py
python3 source/gen/valida_batch.py
python3 ../_tools/validate_case.py WF2-091_clean-team-scambio-informativo
python3 ../_tools/check_gold.py WF2-091_clean-team-scambio-informativo
```

**Stato: `draft_for_legal_validation`.** Nessun run eseguito, nessuna calibrazione
con judge, nessuna validazione giuridica professionale.
