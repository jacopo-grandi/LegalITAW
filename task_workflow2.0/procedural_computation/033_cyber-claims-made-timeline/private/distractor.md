# WF2-033 - Distrattore

Versione del deliverable deliberatamente sbagliata su tre punti.

## Errori introdotti

1. **Denuncia dell'Evento dichiarata tardiva.** La timeline segue la tesi del broker, computa le
   settantadue ore dal primo accesso non autorizzato del 12 marzo 2031 e conclude che il termine e'
   scaduto il 15 marzo 2031.
2. **Intera durata dell'interruzione presentata come indennizzabile.** La timeline indica 61 ore e 30
   minuti come periodo indennizzabile e non applica il periodo di attesa.
3. **Sospensione feriale applicata al termine di denuncia della Richiesta.** La timeline indica il 22
   settembre 2031 come scadenza e colloca la denuncia della Richiesta fra le attivita' di settembre.

## Criteri che devono fallire

| Criterio | Issue | Ragione |
|---|---|---|
| B.2 | I-01 | fa decorrere il termine dal primo accesso non autorizzato |
| B.3 | I-02 | non afferma che la denuncia e' tempestiva |
| B.4 | I-02 | condivide la tesi del broker |
| B.24 | I-02 | segnala la tardivita' della denuncia come rilievo |
| C.2 | I-02 | non indica il 17 marzo 2031 come scadenza |
| C.3 | I-01 | indica il 15 marzo 2031 come scadenza |
| B.6 | I-04 | non afferma che il periodo di attesa decorre dall'inizio dell'interruzione |
| B.7 | I-05 | presenta come indennizzabile l'intera durata |
| C.4 | I-04 | non indica le ore 17:40 come inizio del periodo indennizzabile |
| C.7 | I-05 | non indica 49 ore e 30 minuti |
| B.22 | I-05 | non distingue le due durate |
| B.10 | I-07 | applica la sospensione feriale |
| C.8 | I-06 | non indica il 22 agosto 2031 |
| C.10 | I-07 | indica il 22 settembre 2031 |
| C.14 | I-06 | i giorni residui non sono quattordici |

## Criteri che devono continuare a passare

Tutti gli altri, in particolare B.1, B.5, B.8, B.9, B.11, B.12, B.13, B.14, B.15, B.16, B.17, B.18,
B.19, B.20, B.21, B.23, B.25, B.26, B.27, B.28, B.29, B.30, B.31 e i criteri C.1, C.5, C.6, C.9,
C.11, C.12, C.13.

Nota sull'accoppiamento voluto. L'errore 1 tocca sei criteri distribuiti su due issue: il momento
iniziale sbagliato si propaga alla scadenza e alla conclusione sulla tempestivita', e attiva il
criterio di sovra-segnalazione. Il criterio B.1, che chiede di individuare la Scoperta, continua a
passare: il distrattore la individua correttamente e poi non la usa. E' l'accoppiamento voluto fra
individuazione del fatto e sua applicazione al termine, tenuti separati proprio per distinguere i due
errori.

L'errore 2 tocca quattro criteri di due issue contigue. L'errore 3 tocca quattro criteri di due
issue. Nessuno dei tre tocca la sezione sulla copertura, che resta interamente valutabile.
