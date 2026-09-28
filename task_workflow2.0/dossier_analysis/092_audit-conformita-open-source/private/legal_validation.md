# WF2-092 - Legal validation

**Stato: `draft_for_legal_validation`. Il caso non e `pilot_ready`.**

Questo file distingue tre cose che non vanno confuse: il self-check meccanico, che
e stato eseguito; la validazione giuridica professionale, che non lo e; la
calibrazione con judge reali, che non lo e.

## Domande per il sign-off

1. L'issue I-07 poggia sulla definizione di distribuzione o comunicazione dell'EUPL v1.2, che comprende il fornire accesso alle funzionalità essenziali online. Confermate che la messa a disposizione del portale integri quella nozione anche in assenza di modifiche al componente?

2. L'issue I-04 e il controlled non-issue N-02 poggiano sulla posizione della Free Software Foundation sulla compatibilità fra Apache-2.0 e GPL. La distinzione fra GPL-2.0-only e GPL-2.0-or-later non è enunciata dalla Fondazione con riferimento alla Apache: è una deduzione dal meccanismo della versione successiva. Il criterio è formulato come ragionamento richiesto e non come citazione: confermate l'impostazione?

3. L'issue I-06 chiede di verificare il perimetro dell'opera distribuita senza affermare che il modulo costituisca un'opera unica o un aggregato. È il livello di prudenza che ritenete corretto, o preferite una conclusione più netta?

4. L'issue I-09 esclude l'applicazione al collaboratore esterno della regola sul lavoratore dipendente. Confermate che il fascicolo, così com'è, non consenta di affermare il titolo di Solmarino sul componente?

5. La posizione proposta sull'articolo 4.2 del contratto è di gestire la dichiarazione con il cliente. In uno scenario reale procedereste con una comunicazione preventiva o attendereste una contestazione?

6. L'issue I-12 subordina il rilascio del 26 novembre 2026 alla chiusura dei rimedi che incidono sulla distribuzione. Confermate quali rimedi rientrino in quel perimetro e quali possano seguire il rilascio?

## Punti che le fonti consultate non risolvono

Nessuno di questi e stato trasformato in criterio.

- Non è stata verificata alcuna pronuncia, italiana o europea, sul perimetro dell'opera nelle combinazioni di codice sotto licenze diverse. Nessun criterio poggia su giurisprudenza e nessun criterio chiede una conclusione sul perimetro dell'opera.
- La posizione della Free Software Foundation sulla compatibilità fra Apache-2.0 e GPL-2.0-or-later non è enunciata come tale nelle fonti consultate: la distinzione è una deduzione dal meccanismo della versione successiva ed è trattata come tale.
- Non è stato verificato se l'appendice delle licenze compatibili dell'EUPL v1.2 sia stata aggiornata dopo il 2017: la Commissione può aggiornarla senza produrre una nuova versione della licenza. Nessun criterio dipende dal contenuto dell'appendice.
- Non è stato verificato l'atto che ha introdotto nell'art. 1 della legge n. 633/1941 il riferimento alle opere create con l'ausilio di strumenti di intelligenza artificiale, che non rileva per il caso.
- La conversione in euro delle sanzioni pecuniarie dell'art. 171-bis della legge n. 633/1941 non è stata verificata: il profilo sanzionatorio penale non entra in alcun criterio.

## Effetto di una correzione

Una correzione che incida su una conclusione richiede l'aggiornamento coordinato di
challenge map, rubrica in prosa, criteri atomizzati, `rubric.json`,
`runtime_routing.json`, gold e distrattore: sono emessi da un'unica fonte
(`source/authoring/casi/wf2_092.py`), quindi si corregge la fonte e si riesegue
`source/gen/assembla_casi.py`.
