# WF2-059 - Distrattore controllato

## Criteri che questa versione intende far fallire, dichiarati prima dell'esecuzione

- `B.8` - non identifica le due operazioni che eccedono la soglia di doppia firma
- `B.9` - non riferisce alle due operazioni oltre soglia il rilievo della firma singola
- `B.10` - estende a tutte e sei le operazioni la difformità dal mandato
- `B.11` - non indica in quattro le operazioni disconosciute sotto soglia
- `B.12` - afferma che l'esecuzione a firma singola delle quattro operazioni sotto soglia viola il mandato
- `C.6` - afferma che la Banca sarà tenuta a rimborsare l'importo contestato

Nessun altro criterio deve fallire. Se il fallimento si propaga a criteri
limitrofi, l'atomizzazione non ha funzionato e va rivista.

## Criteri che devono restare superati

- B.1, B.2 e B.3: qualificazione del cliente e ammissibilità della deroga
- B.4, B.5 e B.6: perimetro chiuso della deroga e onere della prova
- B.7: eccesso della tesi della banca sull'esonero integrale
- B.13 e B.14: numero e attribuzione delle operazioni senza autenticazione forte
- B.15: la registrazione non prova l'autorizzazione
- B.16, B.17 e B.18: avviso, data della variazione e divieto di addebitare l'omissione
- B.19, B.20, B.21 e B.22: condotta del cliente e misura non determinabile
- B.23, B.24, B.25 e B.26: documentazione non trasmessa, autore ignoto, totale
- C.1, C.2, C.3 e C.4: nessuna sovra-segnalazione sui tre controlled non-issue
- C.5 e C.7: nessuna asimmetria e nessuna sovra-segnalazione sull'estero

## Limite dichiarato

La verifica che il fallimento colpisca esattamente i criteri elencati e nessun
altro richiede un'esecuzione con judge reali, che questa sessione non ha svolto.
Il controllo meccanico eseguito riguarda le sole stringhe verificabili: le
varianti dei criteri `valore` restano presenti nel distrattore e le stringhe
vietate dai criteri `assenza` non mirati restano assenti.

## Testo

## 1. Regime applicabile al rapporto

Officine Pratosolco S.r.l. stipula nell'esercizio dell'attività imprenditoriale e **non
è microimpresa**: la sezione II dichiara **34 dipendenti** e un **fatturato di euro
9.840.000,00**. La **deroga è ammessa** e, per effetto della clausola 18.3, **l'onere di
provare la mancata autorizzazione grava sul cliente**. La deroga non copre però
l'**obbligo di rimborso** né il **termine massimo per la comunicazione**: la clausola
18.4 lo riconosce.

## 2. Matrice delle evidenze

| Operazione | Importo | Firme | Autenticazione forte | Utenza e dispositivo | Fonte |
|---|---|---|---|---|---|
| 5 marzo, ORBITEC LP | 24.500,00 | 1 | non applicata | vertegno.a, DEV-019 non censito | doc. 02 |
| 5 marzo, ORBITEC LP | 18.000,00 | 1 | non applicata | vertegno.a, DEV-019 non censito | doc. 02 |
| 6 marzo, KESTRA TRADE OU | 39.000,00 | 1 | applicata | baldiselva.r, DEV-004 censito | doc. 02 |
| 6 marzo, ORBITEC LP | 22.000,00 | 1 | non applicata | vertegno.a, DEV-019 non censito | doc. 02 |
| 7 marzo, KESTRA TRADE OU | 16.000,00 | 1 | non applicata | vertegno.a, DEV-019 non censito | doc. 02 |
| 7 marzo, KESTRA TRADE OU | 29.000,00 | 1 | applicata | baldiselva.r, DEV-004 censito | doc. 02 |

Totale disconosciuto: **euro 148.500,00** [doc. 03].

## 3. Difformita rilevate

**Soglia di doppia firma.** Tutte e sei le operazioni sono state disposte con **una sola
firma**, in violazione della clausola 5.3, che impone la disposizione congiunta. Non vi
sono operazioni disconosciute conformi al mandato: la difformità è generale e riguarda
l'intero importo di euro 148.500,00. La clausola 5.4 vietava alla Banca di eseguirle.

**Autenticazione forte.** **Quattro** operazioni risultano eseguite **senza autenticazione
forte**, tutte disposte con l'utenza **vertegno.a** da **DEV-019, dispositivo non
censito**.

**Avviso e numero censito.** L'avviso via SMS della clausola 8.1, lettera a), **non è
stato ricevuto**. La variazione del numero censito era stata comunicata per iscritto il
**4 febbraio 2031**, prima delle operazioni.

## 4. Posizione della Banca

**Punto 1.** L'affermazione secondo cui nessun obbligo di rimborso grava sulla Banca
**eccede il contenuto della deroga**.

**Punto 2.** La tesi non regge: **la registrazione non prova l'autorizzazione**. La
circostanza che le operazioni risultino registrate e contabilizzate nei sistemi non
dimostra da sé che siano state autorizzate.

**Punto 3.** La comunicazione a terzi delle credenziali del **27 febbraio 2031** e il
fatto che **la Banca non sia stata informata** sono provati dagli atti. Rilevano come
concorso nella produzione del danno, ma la **misura dell'incidenza non è determinabile
con i dati disponibili**.

**Punto 4.** Il rilievo **non è fondato**: il disconoscimento è del 12 marzo 2031, lo
stesso giorno del rilievo in riconciliazione.

**Punto 5.** La documentazione tecnica **non è stata trasmessa**.

## 5. Dati mancanti e azioni

**Dati mancanti.** Il fascicolo **non prova chi abbia materialmente impartito** le
disposizioni: mancano i log di sessione, gli indirizzi di collegamento e il tracciato dei
codici temporanei. Non risulta agli atti **alcun rientro** delle somme.

Poiché la difformità dal mandato copre l'intero importo, **la Banca sarà tenuta a
rimborsare** euro 148.500,00 e il ripristino del saldo è dovuto.

**Azioni.**

1. Richiedere la documentazione tecnica e l'elenco dei dispositivi abilitati.
2. Allegare la ricevuta di ritorno della raccomandata del 4 febbraio 2031.
3. Acquisire il tracciato delle configurazioni della soglia nei sistemi della Banca.

**Elementi che non costituiscono profili di rischio.** Il bonifico stipendi di euro
96.420,00 del 3 marzo 2031 è conforme al mandato e non è fra le operazioni
disconosciute. Il termine di risposta al reclamo rientra in quello pattuito. La
destinazione estera dei conti è un elemento descrittivo.
