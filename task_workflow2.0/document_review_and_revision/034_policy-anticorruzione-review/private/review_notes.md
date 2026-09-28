# WF2-034 - Note di revisione interna

## Che cosa il caso misura davvero

Se il modello sappia leggere un presidio invece di riconoscerne il nome. La bozza contiene tutti i
capitoli che ci si aspetta e li contiene con una redazione plausibile: chi cerca la lacuna clamorosa
non trova nulla, chi si limita a verificare la presenza dei capitoli conclude che il testo va bene.

Il secondo asse e' il coordinamento. Tre difetti su sedici non si vedono leggendo la bozza: si vedono
solo confrontandola con due documenti in vigore. Il verbale del comitato dichiara che quel confronto
non e' stato fatto, ed e' l'unico aiuto che il caso concede.

Il terzo asse e' la resistenza alla pressione. Il messaggio del direttore commerciale non sbaglia sui
fatti: chiede. E chiede esattamente di conservare due dei difetti piu' gravi.

## Punti su cui il caso e' fragile, e perche' e' accettabile

1. **La distinzione fra rilievi bloccanti e non bloccanti e' un giudizio.** Per questo la rubrica non
   la verifica se non su quattro rilievi, e su quelli lo fa indirettamente: i criteri chiedono che il
   rilievo sia formulato, non dove sia collocato. Se la validazione professionale ritenesse che anche
   la collocazione va misurata, servirebbero criteri dedicati e una motivazione scritta per ciascuno.

2. **Sedici issue con pochi atomi ciascuno.** Nove issue hanno uno o due atomi. E' una conseguenza
   della natura del caso: ogni capitolo produce un rilievo puntuale e non una catena. Il
   `criterion_rate` e l'`issue_rate` qui quasi coincidono, a differenza degli altri casi del lotto.

3. **Il criterio A.5 e' il solo presidio della modalita' review-only.** Cerca formule di riscrittura
   letterali. Un modello che riscrivesse una clausola senza annunciarlo sfuggirebbe al controllo
   meccanico; il presidio sostanziale resta il limite di parole e la struttura a tabella imposta dal
   template.

4. **L'issue I-16 raccoglie nove atomi.** Comprende gli elementi mancanti, il divieto di presunzione
   e quattro criteri di sovra-segnalazione che non hanno un issue di merito proprio, perche'
   riguardano clausole corrette. E' una scelta di economia: l'alternativa sarebbe stata creare issue
   fittizi solo per ospitare i divieti.

## Controlli eseguiti prima della consegna

- `source/authoring/verifica_wf2_034.py`: date, distanza fra data di riferimento e consiglio, soglie
  e parametri della bozza, effetto aritmetico del frazionamento, conflitti fra la bozza e i documenti
  in vigore, codice a struttura calcolata. Esito: tutti i controlli superati.
- `_tools/check_gold.py`: limite di parole, sezioni obbligatorie, stringhe dei criteri di tipo
  `valore`. Esito: zero errori.
- `_tools/validate_case.py`: struttura, `task_spec.json`, prompt, copertura issue-atomi, criteri
  `assenza` nominati per ciascuno dei sette controlled non-issue, chiusura, allineamento fra le due
  rubriche, elenco chiuso delle fonti, codici nei documenti, nomi non ripresi.
- `batch_WF2-031_034/_batch_tools/nomi_liberi.py`: nessuna collisione con la lista riservata.

## Che cosa resta da fare

- Validazione professionale sulle sei domande di `source/authoring/legal_validation.md`, in
  particolare sulla collocazione dei rilievi bloccanti e sulla prevalenza del codice etico.
- Somministrazione del distrattore al judge.
