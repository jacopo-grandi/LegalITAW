# Ritiro dei response template dal benchmark eseguibile

Il 21 settembre 2026 i `response_template.md` sono stati esclusi dal materiale visibile al modello. Il problema non era soltanto formale: in 57 task il template poteva entrare nel workspace e suggeriva in anticipo nomi, ordine delle sezioni, limiti di parole e, in alcuni casi, la stessa checklist che sarebbe poi stata valutata. Una run così misurava anche la capacità di seguire uno stampino fornito dal benchmark; non isolava bene la qualità del lavoro sul fascicolo.

I 70 file fisici non sono stati cancellati. Restano accanto ai task come reperti di authoring, necessari per capire e riprodurre le vecchie run, ma `public_envelope_paths()` li esclude in modo esplicito. La stessa esclusione vale per `generic_agent`, `text_bundle`, `agentic_workspace` e per il bundle consegnato ai judge. I `task_spec.json` non li dichiarano più fra gli input pubblici e riportano la policy `authoring_only_not_model_visible`.

La pulizia ha toccato anche le consegne: 37 riferimenti espliciti al template sono stati rimossi da `01_task.md`. Quando la frase conteneva pure un requisito autonomo — per esempio il nome del file o l'obbligo di ancorare ogni conclusione a un documento — quel requisito è rimasto. Non sono stati trasferiti nel prompt gli indici, i word cap o le tassonomie del vecchio template: farlo avrebbe conservato il vantaggio sotto un'altra forma.

## Effetto sulla rubrica

L'audit ha trovato 273 criteri che indicavano il template fra le fonti di authoring. Ne sono stati eliminati 146: nomi di file non richiesti nella consegna, limiti di parole, ordine obbligatorio delle sezioni e vincoli di tabella o classificazione che il modello non poteva ricavare dal prompt. Gli altri 127 sono rimasti perché la consegna li chiedeva già in modo indipendente — fra questi le revisioni tracciate, la distinzione fra fatti e lacune, alcuni nomi di file e campi sostanziali delle matrici — e la loro fonte è stata ricondotta a `public/01_task.md`.

Il corpus passa così da 5.178 a 5.032 criteri. `rubric.json`, `runtime_routing.json`, gli overlay dei controlli deterministici e `manifest.json` sono stati aggiornati insieme; il loader carica 100 task e 5.032 criteri senza drift.

## Comparabilità delle run

Le run precedenti restano valide per lo snapshot su cui sono state prodotte, ma il loro punteggio complessivo non è direttamente confrontabile con quello del corpus ripulito: cambia il denominatore e spariscono 146 controlli di forma. Un confronto serio deve conservare insieme a ciascun risultato l'hash di task spec e rubrica, oppure rivalutare le submission storiche con la rubrica da 5.032 criteri.

La migrazione è riproducibile con `scripts/retire_response_templates.py` del repository di authoring legal-ITA. Il test del generic agent attraversa tutti i cento task e verifica sia l'assenza del template dal public envelope sia la sua effettiva assenza nel filesystem montato per il modello.
