# WF2-074 - Remediation 231 dopo l'acquisizione

Caso sintetico LegalITA v2, batch `WF2-071_080`.

| Campo | Valore |
|---|---|
| Area | Compliance & Investigations |
| Famiglia | Procedural timeline |
| Deliverable | `remediation_timeline.md` |
| Difficoltà / fascicolo | high / medium |
| Documenti | 5 |
| Issue / criteri | 10 / 70 |
| Stato | `draft_for_legal_validation` |

Il fascicolo separa fatti, lacune e affermazioni di parte. La challenge map è stata chiusa prima della generazione documentale ed è conservata nella busta privata e nella sorgente di authoring.

## Rigenerazione e verifica

Eseguire dalla radice del repository:

```bash
python task_workflow2.0.1/batch_WF2-071_080/source/gen/build_batch.py
python task_workflow2.0.1/batch_WF2-071_080/source/authoring/verify_batch.py
```
