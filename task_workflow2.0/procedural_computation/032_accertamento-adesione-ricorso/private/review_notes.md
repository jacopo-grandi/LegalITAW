# WF2-032 - Note di revisione interna

## Che cosa il caso misura davvero

Un solo gesto: stabilire quanto tempo resta, e non sbagliarlo. Tutto il resto - le opzioni, le
attivita', la correzione della nota - dipende da quella data. Il caso e' costruito perche' esistano
cinque strade che portano a cinque date diverse e tutte plausibili, e perche' la piu' naturale sia
sbagliata.

Il secondo asse e' la fiducia nella parte. Chi scrive la nota e' un professionista, non un cliente
allarmato: il modello che si appoggia alla sua ricostruzione sbaglia sei volte in un colpo solo.

## Punti su cui il caso e' fragile, e perche' e' accettabile

1. **Il cumulo delle sospensioni non e' scritto in nessuna fonte del pack.** E' deliberato: le due
   sospensioni operano per ragioni distinte e il cumulo si deduce. Se la validazione professionale
   ritiene che serva un ancoraggio esplicito, la fonte va aggiunta al reference pack e il criterio
   B.6 va riformulato come `attribuzione`.

2. **La questione dell'art. 15 non ha una risposta unica.** Il caso non ne pretende una. Il rischio e'
   che un modello prudente si limiti a non parlarne: per questo il criterio B.11 chiede
   l'affermazione positiva della condizione di legge, che e' testuale, e il criterio B.12 vieta solo
   di dare la riduzione per acquisita.

3. **Nove criteri dipendono dalla data finale.** Un modello che sbaglia la sospensione li perde quasi
   tutti. E' la struttura della catena e va letta sull'`issue_rate`, non sul `criterion_rate`.

4. **La nota del consulente e' molto sbagliata.** Il rischio e' che diventi un bersaglio troppo facile
   e che il modello si limiti a contraddirla. Il presidio e' che tre degli errori della nota (novanta
   giorni, ripresa dal verbale, seconda istanza) coincidono con altrettante derivazioni che un modello
   produrrebbe da solo: contraddire la nota non basta, bisogna arrivare alla data giusta.

## Controlli eseguiti prima della consegna

- `source/authoring/verifica_wf2_032.py`: cronologia, sei termini, cinque derivazioni errate con
  verifica di non collisione, importi, divisibilita' per tre del totale delle imposte, codici a
  struttura calcolata. Esito: tutti i controlli superati.
- `_tools/check_gold.py`: limite di parole, sezioni obbligatorie, presenza nel gold delle stringhe
  dei criteri di tipo `valore`, assenza delle stringhe vietate. Esito: zero errori.
- `_tools/validate_case.py`: struttura, `task_spec.json`, prompt, copertura issue-atomi, criteri
  `assenza` nominati per ciascun controlled non-issue, chiusura, allineamento fra rubrica in prosa e
  challenge map, elenco chiuso delle fonti, codici nei documenti, nomi non ripresi.
- `batch_WF2-031_034/_batch_tools/nomi_liberi.py`: nessuna collisione con la lista riservata.

## Che cosa resta da fare

- Validazione professionale sulle sei domande di `source/authoring/legal_validation.md`, in
  particolare sulla durata della sospensione e sulla riduzione delle sanzioni.
- Somministrazione del distrattore al judge.
