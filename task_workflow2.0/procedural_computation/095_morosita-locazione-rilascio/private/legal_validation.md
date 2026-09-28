# WF2-095 - Legal validation

**Stato: `draft_for_legal_validation`. Il caso non e `pilot_ready`.**

Questo file distingue tre cose che non vanno confuse: il self-check meccanico, che
e stato eseguito; la validazione giuridica professionale, che non lo e; la
calibrazione con judge reali, che non lo e.

## Domande per il sign-off

1. L'issue I-03 poggia sul fatto che l'art. 5 della legge sulle locazioni non è fra le disposizioni estese ai contratti ad uso diverso dall'art. 41. Confermate che le soglie dei venti giorni e delle due mensilità non siano regole di legge per la locazione commerciale, e che la loro presenza nel contratto vada trattata come pattuizione?

2. L'issue I-12 tratta come controversa l'applicabilità del termine di grazia alle locazioni ad uso diverso. È il punto su cui vi chiedo una decisione: preferite che il caso resti su questa impostazione, che il tema esca dai criteri, o che il caso sia riportato a una locazione abitativa dove il problema non si pone?

3. L'issue I-05 conclude che la clausola 6.3 non è utilizzabile perché il canone annuo è inferiore alla soglia di derogabilità. Confermate la lettura dell'art. 79 per i contratti ad uso diverso, tenuto conto che l'abrogazione disposta dalla legge del 1998 riguarda le sole locazioni abitative?

4. L'issue I-07 rileva l'omissione dell'avviso sul patrocinio a spese dello Stato senza concludere per la nullità dell'atto. Confermate che, avendo la conduttrice annunciato di comparire, la rappresentazione corretta sia quella di un contenuto prescritto mancante di cui va valutata la conseguenza in udienza?

5. L'issue I-08 rileva l'assenza della ricevuta di spedizione dell'avviso di cui all'ultimo comma dell'art. 660. Confermate che il rilievo vada portato all'udienza e non sanato prima?

6. Il gold indica come somma non controversa 12.872,00 euro, sommando i canoni non contestati e la quota di oneri accessori residua dopo lo stralcio del portierato. Confermate il criterio di determinazione?

## Punti che le fonti consultate non risolvono

Nessuno di questi e stato trasformato in criterio.

- L'applicabilità del termine di grazia previsto dall'art. 55 della legge sulle locazioni ai contratti ad uso diverso da quello di abitazione non è risolta dal testo di legge e non è stata verificata su alcuna pronuncia. Nessun criterio richiede una conclusione su questo punto: i criteri chiedono di rappresentarlo come controverso e di chiedere istruzioni.
- L'ampiezza dell'esclusione dalla sospensione feriale, e in particolare se essa copra anche la fase a cognizione piena successiva al mutamento del rito, non è risolta dal testo. Il caso si arresta al termine di comparizione, che è coperto dall'esclusione.
- Nessuna pronuncia, di legittimità o di merito, è stata verificata o citata. Le conseguenze processuali dell'omissione dell'avviso sul patrocinio a spese dello Stato non sono state verificate su fonte primaria oltre al testo dell'art. 660: nessun criterio richiede di indicarne l'effetto.
- Nessun protocollo di tribunale è stato usato come fonte di alcun criterio.
- L'importo del contributo unificato indicato nell'atto non è stato verificato e non è oggetto di alcun criterio.

## Effetto di una correzione

Una correzione che incida su una conclusione richiede l'aggiornamento coordinato di
challenge map, rubrica in prosa, criteri atomizzati, `rubric.json`,
`runtime_routing.json`, gold e distrattore: sono emessi da un'unica fonte
(`source/authoring/casi/wf2_095.py`), quindi si corregge la fonte e si riesegue
`source/gen/assembla_casi.py`.
