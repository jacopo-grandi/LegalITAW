# WF2-099 - Accordo di bonifica e allocazione dei costi sul sito di Rovasenda Ligure

`Review and redline` - Environmental, Energy & ESG - difficolta low - pack medium.

Il caso assiste Vetrerie Malaspino S.p.A., proprietaria del sito e non responsabile della contaminazione alla data del 2026-12-09. Il fascicolo contiene 6 allegati; la busta
privata contiene 14 issue di merito, 3 controlled non-issue e 37 criteri atomici.

## Che cosa e pubblico e che cosa non lo e

Pubblico: `public/01_task.md`, `public/02_reference_pack.md`,
`public/03_legal_sources.md`, `public/response_template.md`, `public/documents/`.

Privato: challenge map, rubrica in prosa, criteri atomizzati, `rubric.json`,
`runtime_routing.json`, gold standard, distrattore, tabella delle date verificate,
elenco chiuso delle fonti, note di validazione.

## Deliverable atteso

`remediation_agreement_redline.docx + issue_note.md`, docx con revisioni tracciate e markdown, entro 2100 parole.

## Verifiche

```
python3 source/gen/verifica_date_e_codici.py
python3 source/gen/valida_batch.py
python3 ../_tools/validate_case.py WF2-099_accordo-bonifica-allocazione-costi
python3 ../_tools/check_gold.py WF2-099_accordo-bonifica-allocazione-costi
```

**Stato: `draft_for_legal_validation`.** Nessun run eseguito, nessuna calibrazione
con judge, nessuna validazione giuridica professionale.
