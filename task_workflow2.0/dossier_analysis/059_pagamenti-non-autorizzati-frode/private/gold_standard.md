# WF2-059 - evidence_and_liability_memo.md - Gold standard

> Rappresentazione strutturata di ciò che una buona risposta deve riconoscere.
> Non è un testo da imitare.

## 1. Regime applicabile al rapporto

Officine Pratosolco S.r.l. stipula nell'esercizio dell'attività imprenditoriale e **non
è microimpresa**: la sezione II delle condizioni di conto dichiara **34 dipendenti** e un
**fatturato di euro 9.840.000,00**, valori che superano i requisiti dimensionali della
nozione [fatto documentato: doc. 01, sezione II]. La **deroga è ammessa**: la clausola
18.2 può quindi escludere l'onere della prova dell'autenticazione a carico della Banca e
la disciplina della responsabilità per l'utilizzo non autorizzato dello strumento. Per
effetto della clausola 18.3, **l'onere di provare la mancata autorizzazione grava sul
cliente**.

La deroga ha però un **perimetro chiuso**. Restano fuori, e non sono disponibili alle
parti, l'**obbligo di rimborso** del prestatore di servizi di pagamento e il **termine
massimo per la comunicazione** dell'operazione non autorizzata; la clausola 18.4 lo
riconosce espressamente [inferenza dal combinato delle clausole 18.2 e 18.4].

## 2. Matrice delle evidenze

| Operazione | Importo | Soglia 25.000 | Firme | Autenticazione forte | Utenza e dispositivo | Fonte |
|---|---|---|---|---|---|---|
| 5 marzo, ORBITEC LP | 24.500,00 | sotto | 1 | non applicata | vertegno.a, DEV-019 non censito | doc. 02 |
| 5 marzo, ORBITEC LP | 18.000,00 | sotto | 1 | non applicata | vertegno.a, DEV-019 non censito | doc. 02 |
| 6 marzo, KESTRA TRADE OU | **39.000,00** | **oltre** | **1** | applicata | baldiselva.r, DEV-004 censito | doc. 02 |
| 6 marzo, ORBITEC LP | 22.000,00 | sotto | 1 | non applicata | vertegno.a, DEV-019 non censito | doc. 02 |
| 7 marzo, KESTRA TRADE OU | 16.000,00 | sotto | 1 | non applicata | vertegno.a, DEV-019 non censito | doc. 02 |
| 7 marzo, KESTRA TRADE OU | **29.000,00** | **oltre** | **1** | applicata | baldiselva.r, DEV-004 censito | doc. 02 |

Totale disconosciuto: **euro 148.500,00** [doc. 03].

## 3. Difformita rilevate

**Soglia di doppia firma.** Due operazioni superano la soglia della clausola 5.3: quella
di **euro 39.000,00** del 6 marzo e quella di **euro 29.000,00** del 7 marzo. Per entrambe
la colonna delle firme riporta una firma sola: la loro esecuzione è in **difformita dal
mandato**, che la clausola 5.4 vietava di eseguire.

Le altre **quattro** operazioni - 24.500,00, 18.000,00, 22.000,00 e 16.000,00 - sono di
importo inferiore alla soglia: la loro esecuzione a firma singola è conforme alla
clausola 5.2. Il vizio, per esse, sta altrove.

**Autenticazione forte.** **Quattro** operazioni risultano eseguite **senza autenticazione
forte**, tutte disposte con l'utenza **vertegno.a** da **DEV-019, dispositivo non
censito**.

**Avviso e numero censito.** L'avviso via SMS della clausola 8.1, lettera a), **non è
stato ricevuto**. La variazione del numero censito era stata comunicata per iscritto il
**4 febbraio 2031**, prima delle operazioni: non è sostenibile che il cliente avesse
omesso quella comunicazione [doc. 03].

## 4. Posizione della Banca

**Punto 1, esonero integrale.** L'affermazione secondo cui nessun obbligo di rimborso
grava sulla Banca **eccede il contenuto della deroga**: la clausola 18.2 non nomina
l'obbligo di rimborso e la clausola 18.4 fa salve le disposizioni indisponibili.

**Punto 2, registrazione.** La tesi non regge: **la registrazione non prova
l'autorizzazione**. La circostanza che le operazioni risultino registrate e
contabilizzate nei sistemi non dimostra da sé che siano state autorizzate.

**Punto 3, condotta del cliente.** La comunicazione a terzi di identificativo, codice
segreto e codice temporaneo del **27 febbraio 2031** e il fatto che **la Banca non sia
stata informata** sono provati dagli atti [doc. 03]. Rilevano come concorso nella
produzione del danno, ma la **misura dell'incidenza non è determinabile con i dati
disponibili**: servirebbe la documentazione tecnica che la Banca non ha trasmesso. Non è
sostenibile che quella condotta escluda ogni pretesa.

**Punto 4, tempestivita.** Il rilievo **non è fondato**: il disconoscimento è del
12 marzo 2031, lo stesso giorno in cui il cliente ha rilevato i movimenti in
riconciliazione e cinque giorni dopo l'ultima operazione, entro il termine indisponibile.

**Punto 5, documentazione.** La documentazione tecnica sull'autenticazione delle singole
operazioni e l'elenco dei dispositivi abilitati **non sono stati trasmessi**.

## 5. Dati mancanti e azioni

**Dati mancanti.** Il fascicolo **non prova chi abbia materialmente impartito** le
disposizioni: mancano i log di sessione, gli indirizzi di collegamento, l'identificativo
completo del dispositivo e il tracciato dei codici temporanei. Non risulta agli atti
**alcun rientro** delle somme: la riga del 13 marzo 2031 riporta un importo pari a zero.
La ricevuta di ritorno della raccomandata del 4 febbraio 2031 è annunciata e non allegata.

**Azioni.**

1. Richiedere formalmente alla Banca la documentazione tecnica sull'autenticazione di
   ciascuna operazione e l'elenco dei dispositivi abilitati al 5 marzo 2031.
2. Allegare la ricevuta di ritorno della raccomandata del 4 febbraio 2031.
3. Impostare la pretesa sulle due operazioni oltre soglia sul piano della difformita dal
   mandato, distinta dal piano dell'autenticazione per le quattro sotto soglia.
4. Acquisire il tracciato interno delle configurazioni della soglia di doppia firma nei
   sistemi della Banca alla data del 6 marzo 2031.
5. Ricostruire la cronologia dell'episodio del 27 febbraio 2031 con la documentazione
   interna del cliente.

**Elementi che non costituiscono profili di rischio.** Il bonifico stipendi di euro
96.420,00 del 3 marzo 2031 supera la soglia ma risulta disposto con due firme e con
autenticazione forte da dispositivo censito: è conforme al mandato e non è fra le
operazioni disconosciute. Il termine di risposta al reclamo osservato dalla Banca rientra
in quello pattuito. La destinazione estera dei conti dei beneficiari è un elemento della
descrizione delle operazioni, non un profilo autonomo imputabile alla Banca.
