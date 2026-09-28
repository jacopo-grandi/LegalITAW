# WF2-032 - Scheda per la validazione professionale

Lettura blind: leggere prima la sola busta pubblica, registrare le proprie conclusioni, poi
confrontarle con `private/evaluation_criteria.md` e `source/authoring/gold_standard.md`.

## Dati del caso

| Campo | Valore |
|---|---|
| Workflow family | procedural_computation |
| Subtask | deadline_chain |
| Verticale | tributario / contenzioso fiscale |
| Data di riferimento | 16 settembre 2030, fascicolo in corso |
| Freeze normativo | 28 agosto 2026 |
| Committente | l'amministratrice unica della societa' accertata |
| Deliverable | audit dei termini, massimo 1.800 parole |
| Issue di merito | 13 |
| Controlled non-issue | 5 |
| Criteri atomici | 49 (12 a verifica meccanica, 37 al judge) |

## Domande al validatore, in ordine di importanza

1. **Durata della sospensione (I-02).** E' il perno del caso. Confermare che, quando l'avviso e'
   stato preceduto dalla comunicazione dello schema di atto e l'istanza di adesione e' presentata nei
   quindici giorni successivi alla notifica, la sospensione del termine di impugnazione sia di trenta
   giorni e non di novanta.

2. **Cumulo con la sospensione feriale (I-03).** Confermare che la sospensione da adesione e quella
   feriale si sommino e che il computo corretto porti al 19 ottobre 2030 prima della proroga. Se il
   validatore ritiene che il cumulo vada sostenuto con una pronuncia, indicare quale: il reference
   pack contiene oggi le sole disposizioni, e l'agente deve dedurre il cumulo dal fatto che le due
   sospensioni operano per ragioni distinte.

3. **Proroga per il sabato (I-04).** Confermare che la proroga dell'art. 155, comma 5, del codice di
   procedura civile si applichi al termine per la proposizione del ricorso tributario e che la
   scadenza sia percio' il 21 ottobre 2030.

4. **Riduzione delle sanzioni per omessa impugnazione (I-08).** L'art. 15, comma 1, del d.lgs.
   218/1997 richiede la rinuncia a impugnare **e** a formulare istanza di accertamento con adesione.
   La societa' l'istanza l'ha presentata. Il caso non risolve la questione: chiede al modello di
   segnalarla come da verificare e gli vieta di dare la riduzione per acquisita. **Confermare che
   questa sia la posizione professionalmente corretta e che il caso non debba invece pretendere una
   conclusione in un senso o nell'altro.**

5. **Perimetro dell'iscrizione a titolo provvisorio (I-09).** Confermare che l'art. 15, comma 1, del
   d.P.R. 602/1973 consenta l'iscrizione di un terzo delle sole imposte e dei relativi interessi, e
   che le sanzioni non entrino in quella base. Confermare inoltre che il criterio B.15 possa vietarne
   l'inclusione.

6. **Chiusura del procedimento di adesione (I-12).** Confermare che, chiuso il contraddittorio con
   verbale di mancato accordo, la societa' non possa riaprire il procedimento con una nuova istanza,
   e che il deliverable debba dirlo senza ulteriori distinzioni.

## Punti dichiarati e non risolti

- **Misura delle sanzioni nell'avviso.** L'atto applica il settanta per cento della maggiore imposta
  per dichiarazione infedele, misura riferita a violazioni del periodo d'imposta 2026. Nessun
  criterio dipende da quella percentuale: e' un dato dell'atto, non un passaggio da ricostruire.
- **Interessi.** Il fascicolo non li quantifica e nessun criterio li richiede. La loro assenza e' una
  voce dell'issue I-13.
- **Macro-area del board.** Il board non ha oggi un'opzione fiscale; la mappatura corretta e'
  registrata nel `task_spec.json` come `board_macro_area_proposta`.

## Nota del costruttore

Sul corpus esistono gia' due casi `deadline_chain`, in materia di somministrazione e di sanzioni
internazionali. La distanza e' costruita su due assi: il verticale, interamente nuovo, e il
meccanismo portante, che qui non e' la concatenazione di eventi contrattuali ma la qualificazione
dell'atto che ha sospeso il termine. Le leve di quei casi - decadenza da diritti contrattuali,
escalation interna, termini di segnalazione - non sono riusate.
