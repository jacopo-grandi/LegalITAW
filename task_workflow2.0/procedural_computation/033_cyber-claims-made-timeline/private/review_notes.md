# WF2-033 - Note di revisione interna

## Che cosa il caso misura davvero

La capacita' di tenere separati quattro istanti che appartengono allo stesso incidente e di agganciare
ciascun termine a quello giusto. Tutti e quattro stanno nello stesso documento e sono dichiarati con
l'ora: non c'e' nulla da cercare, c'e' solo da non confondere.

Il secondo asse e' la disciplina nel non trasformare ogni limite di polizza in un rilievo. Massimale,
sublimite, durata massima, retroattivita', scadenza: cinque oggetti che in un caso assicurativo un
modello e' addestrato a segnalare, e che qui non mordono. Il sesto - la condizione sui fornitori -
morde, e su un oggetto solo.

## Punti su cui il caso e' fragile, e perche' e' accettabile

1. **La denuncia e' stata trasmessa di domenica.** Il 16 marzo 2031 e' domenica, come lo e' la
   notifica all'autorita'. E' voluto e realistico: nella risposta a un incidente si lavora nel fine
   settimana, e nessun termine del caso e' processuale, quindi nessuna proroga opera. Se un modello
   applicasse una proroga per il giorno festivo arriverebbe comunque alla stessa conclusione sulla
   tempestivita', e nessun criterio ne risulta falsato.

2. **L'art. 1932 e' nel reference pack senza un criterio dedicato.** E' una scelta: serve a rendere
   possibile la discussione sulla derogabilita' della condizione sui fornitori, che un buon
   professionista solleverebbe, senza pretenderla. Il campo `Indifferente` del criterio B.14 lo
   dichiara. Se la validazione professionale ritenesse che la clausola e' inefficace, il caso andrebbe
   riscritto sul punto: e' segnalato in `legal_validation.md`.

3. **Sei criteri dipendono dal momento iniziale del termine di denuncia.** Un modello che segue il
   broker li perde tutti. E' la struttura del caso e va letta sull'`issue_rate`.

4. **Le durate sono espresse in ore e minuti.** La verifica meccanica deve accettare anche la forma
   decimale: 49,5 ore e 49 ore e 30 minuti sono lo stesso valore. E' indicato in
   `runtime_routing.json`.

## Controlli eseguiti prima della consegna

- `source/authoring/verifica_wf2_033.py`: cronologia con gli orari, termini a ore e a giorni, periodo
  di attesa e durate, derivazioni errate con verifica di non collisione, massimali e sublimiti,
  perimetro temporale della polizza, codici a struttura calcolata. Esito: tutti i controlli superati.
- `_tools/check_gold.py`: limite di parole, sezioni obbligatorie, stringhe dei criteri di tipo
  `valore`, stringhe vietate. Esito: zero errori.
- `_tools/validate_case.py`: struttura, `task_spec.json`, prompt, copertura issue-atomi, criteri
  `assenza` nominati, chiusura, allineamento fra le due rubriche, elenco chiuso delle fonti, codici
  nei documenti, nomi non ripresi.
- `batch_WF2-031_034/_batch_tools/nomi_liberi.py`: nessuna collisione con la lista riservata.
- Verifica aritmetica delle cinque voci della richiesta del terzo: sommano esattamente il totale.

## Che cosa resta da fare

- Validazione professionale sulle sei domande di `source/authoring/legal_validation.md`, in
  particolare sulla condizione relativa ai Fornitori Autorizzati alla luce delle norme inderogabili.
- Somministrazione del distrattore al judge.
