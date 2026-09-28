# Decision log

- Area, famiglia, deliverable, difficolta' e pack derivano dalla matrice master.
- Data di riferimento: 2028-11-07.
- Fonti congelate al 2 settembre 2026.
- Il caso resta draft e richiede legal sign-off.

## Riparazione strutturale del 2 settembre 2026

Decisioni assunte in riparazione (script: `source/repair_batch.py`, idempotente).

- File canonici: rubrica atomizzata in `private/rubric.json`, rubrica narrativa in
  `private/evaluation_criteria.md`, busta di build in `source/authoring/`. I nomi attesi da
  `_tools/` esistono in `private/` come symlink relativi, non come copie (stessa strategia
  del batch WF2-031_034).
- `fonti_chiuse.json` creato dall'elenco chiuso pubblico, con url e data di verifica.
- Rubrica narrativa riscritta a livello di issue con il raccordo agli atomi: la forma
  atomizzata resta in `criteria_atomized.md`. Il controllo del validatore locale che
  pretendeva gli ID degli atomi *dentro* la rubrica in prosa e' stato corretto, perche'
  chiedeva l'anti-pattern vietato dal Passo 5 della procedura.
- Criteri di assenza dei controlled non-issue riscritti in forma nominata, con `issue_id`
  pari all'ID del non-issue e `criterio_assenza` popolato nella challenge map.
- Criteri di chiusura su simmetria e presunzione dell'esito riscritti nominando oggetti
  concreti; rimosso il criterio generico sulla sovra-segnalazione dei fatti neutri, che
  duplicava i criteri nominati e poggiava su un campo `punti_neutri` boilerplate.
- Criteri di merito ritipizzati (`presenza` invece di `qualificazione` dove la proposizione
  e' un'affermazione) e contenuto atteso portato dentro il campo `verifica`.
- Prompt: rimossa la riga che anticipava il criterio sulla presunzione dell'esito; data di
  riferimento in forma redazionale italiana.
- `task_spec.json`: aggiunti i campi obbligatori mancanti; `input_pubblici` riportato alla
  convenzione del corpus (soli documenti, percorso relativo a `public/`).
- Date, termini e quadrature ricalcolati da `source/verifica_date_valori.py`.

## Audit chirurgico di benchmark readiness del 3 settembre 2026

Gli allegati del caso sono stati riscritti conservando nomi e funzione probatoria; le ancore
mancanti sono state inserite nel documento pertinente. Fonti chiuse, rubrica narrativa,
criteri atomizzati, routing, gold e distrattore sono stati riallineati senza cambiare gli ID
degli issue. I gate locali, condivisi e di readiness hanno esito PASS. Restano aperti soltanto
il legal sign-off e la calibrazione con judge reali; lo stato resta
`draft_for_legal_validation`, `pilot_ready: false`.
