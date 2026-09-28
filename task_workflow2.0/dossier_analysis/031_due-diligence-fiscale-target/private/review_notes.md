# WF2-031 - Note di revisione interna

Note del costruttore per chi rilegge il caso prima della validazione professionale. Non fanno parte
del materiale somministrato e non sono viste dal judge.

## Che cosa il caso misura davvero

Il caso e' costruito attorno a un unico gesto professionale: distinguere, in un fascicolo fiscale,
cio' che e' una passivita' da cio' che le assomiglia. Le tre direzioni dell'errore sono presidiate
separatamente.

- **Omissione.** Un rilievo che non e' ancora stato contestato da nessuno (le spese di
  rappresentanza del 2026) e un profilo che nessun documento nomina come problema (la marca
  temporale) devono emergere dal confronto fra documenti.
- **Sovra-quantificazione.** Un rilievo di competenza vale sanzioni e interessi, non l'imposta
  piena; un periodo decaduto non vale nulla.
- **Sovra-segnalazione.** Sei elementi del fascicolo hanno l'aspetto del rilievo e non lo sono, e
  ciascuno ha un criterio `assenza` che lo nomina.

## Punti su cui il caso e' fragile, e perche' e' accettabile

1. **Il gold e' lungo.** 1.788 parole su un limite di 2.200. Il margine e' del 19 per cento: una
   risposta che aggiunga una sezione discorsiva sfora. E' voluto: la matrice ha nove righe e il
   deliverable ha otto sezioni, e il limite serve a impedire il memo-fiume. Se in calibrazione il
   criterio A.1 fallisse sistematicamente per risposte per il resto valide, il limite va alzato a
   2.600, non abbassata la richiesta.

2. **Molti criteri di tipo `valore`.** Ventuno criteri su sessantasette escono dal judge. E' una
   conseguenza del verticale: una due diligence fiscale e' fatta di numeri. La verifica meccanica
   deve normalizzare il separatore delle migliaia prima del confronto, come indicato in
   `runtime_routing.json`.

3. **La catena dell'art. 84 concentra ventuno criteri su tre issue.** Un modello che sbaglia il primo
   passaggio li perde quasi tutti. L'`issue_rate` lo rappresenta correttamente (tre issue su
   quindici); il `criterion_rate` lo sovrarappresenta. E' il motivo per cui il confronto fra modelli
   va letto sull'`issue_rate`, come prescrive il metodo.

4. **Il documento 09 e' l'unica fonte della data di presentazione della dichiarazione.** E' una
   dichiarazione di parte, ma su un fatto verificabile e con protocollo. Il criterio B.24 chiede il
   confronto fra due date, non la fiducia nella parte. Se il validatore lo ritiene insufficiente, la
   soluzione e' aggiungere la ricevuta di presentazione telematica come decimo documento, non
   riscrivere il criterio.

## Controlli eseguiti prima della consegna

- `source/authoring/verifica_wf2_031.py`: tutte le date, i termini di decadenza, le soglie dell'art.
  84, gli importi, le derivazioni errate e i codici a struttura calcolata. Esito: tutti i controlli
  superati.
- `_tools/check_gold.py`: limite di parole, sezioni obbligatorie, presenza nel gold delle stringhe
  di tutti i criteri di tipo `valore`, assenza delle stringhe vietate. Esito: zero errori.
- `_tools/validate_case.py`: struttura, `task_spec.json`, prompt senza norme e senza rubrica,
  copertura issue-atomi, criteri `assenza` nominati per ciascun controlled non-issue, chiusura su
  simmetria, sovra-segnalazione e presunzione, allineamento fra rubrica in prosa e challenge map,
  elenco chiuso delle fonti, date dei criteri `valore` presenti nella tabella verificata, validita'
  dei codici nei documenti, assenza di nomi ripresi da casi esistenti.
- `batch_WF2-031_034/_batch_tools/nomi_liberi.py`: tutti i nomi propri del caso confrontati con la
  lista riservata condivisa. Esito: nessuna collisione.

## Che cosa resta da fare

- Validazione professionale sulle sei domande di `source/authoring/legal_validation.md`.
- Somministrazione del distrattore al judge, per verificare che il fallimento resti nei venti criteri
  elencati in `source/authoring/distractor.md`.
- Decisione sulla macro-area del board.
