# WF2-056 - Distrattore controllato

## Criteri che questa versione intende far fallire, dichiarati prima dell'esecuzione

- `B.31` - qualifica la rettifica per l'andamento come operante in aumento
- `B.32` - non fonda il segno della rettifica sui dati di portafoglio ordini
- `B.33` - indica una misura della rettifica diversa dal 6 per cento
- `B.34` - non indica euro 2.258.643,75 come perdita rettificata
- `B.35` - indica euro 2.498.925,00 come perdita rettificata
- `B.36` - non rileva la rettifica in aumento applicata dalla perizia di parte
- `B.37` - non rileva il contrasto fra la motivazione della perizia e i dati di portafoglio
- `B.43` - propagazione voluta: l'indennizzo sulla perdita di margine non è euro 1.806.915,00
- `B.49` - propagazione voluta: l'indennizzo complessivo non è euro 1.966.915,00
- `B.51` - propagazione voluta: lo scostamento non è euro 872.010,00
- `B.52` - indica due cause dello scostamento e non tre: il segno della rettifica manca

Nessun altro criterio deve fallire. Se il fallimento si propaga a criteri
limitrofi, l'atomizzazione non ha funzionato e va rivista.

## Criteri che devono restare superati

- B.1, B.2 e B.3: operatività della garanzia
- B.4 e B.5: tesi dell'assicuratore sull'elencazione del bene
- B.6, B.7 e B.8: tesi dell'assicuratore sul provvedimento dell'autorità
- B.9 e B.10: decorrenza e scadenza del periodo di indennizzo
- B.11 e B.12: divieto di proroga della scadenza
- B.13 e B.14: stato del periodo alla data di riferimento
- B.15, B.16 e B.17: margine di riferimento
- B.18 e B.19: margine giornaliero e base convenzionale
- B.20 e B.21: durata dei due periodi e date delle riprese
- B.22 e B.23: metodo per il periodo di capacità ridotta
- B.24, B.25 e B.26: perdita lorda
- B.27, B.28, B.29 e B.30: franchigia
- B.38, B.39 e B.40: sottoassicurazione e regola proporzionale
- B.41 e B.42: errore della perizia sulla regola proporzionale
- B.44, B.45 e B.46: maggiori costi e sublimite
- B.47 e B.48: condizione di indennizzabilità dei maggiori costi
- B.50: limite della somma assicurata
- B.53 e B.54: valore della perizia di parte
- B.55, B.56 e B.57: acconto
- B.58, B.59 e B.60: dati mancanti
- C.1, C.2, C.3, C.4, C.5, C.6, C.7 e C.8: nessuna sovra-segnalazione sugli otto controlled non-issue
- C.9, C.10 e C.11: nessuna asimmetria, nessuna presunzione

## Limite dichiarato

La verifica che il fallimento colpisca esattamente i criteri elencati e nessun
altro richiede un'esecuzione con judge reali, che questa sessione non ha svolto.
Il controllo meccanico eseguito riguarda le sole stringhe verificabili: le
varianti dei criteri `valore` restano presenti nel distrattore e le stringhe
vietate dai criteri `assenza` non mirati restano assenti.

## Testo

## 1. Operativita della garanzia

**La garanzia della sezione B opera.** Il presupposto è che il danno materiale sia
**indennizzabile ai sensi della sezione A, indipendentemente dall'importo liquidato**. Il
bene danneggiato è **ricompreso nella partita macchinario, attrezzature e impianti**.

## 2. Periodo di indennizzo

**Decorrenza: 11 gennaio 2031**, giorno del sinistro.

**Scadenza: 11 gennaio 2032.** Cade di domenica, ma **non si proroga**: è un **termine
convenzionale di durata della copertura**, non un termine per l'adempimento.

Al **30 settembre 2031 il periodo di indennizzo è ancora aperto**.

## 3. Parametri della quantificazione

**Margine di contribuzione di riferimento: euro 6.750.000,00**, differenza fra valore della
produzione e costi variabili di produzione dell'esercizio 2030.

**Base convenzionale di computo: trecentosessanta giorni.**

**Margine giornaliero: euro 18.750,00.**

**Periodi di riduzione: 72 giorni** di fermo totale; **147 giorni** di capacità ridotta, dal
**24 marzo 2031** al **17 agosto 2031**; ripresa a regime dal **18 agosto 2031**.

Nel periodo di capacità ridotta la perdita si determina **applicando al margine giornaliero
la percentuale di riduzione della capacità**, pari al **45 per cento**.

## 4. Quantificazione per passaggi

| Passaggio | Importo |
|---|---|
| Perdita del periodo di fermo totale (72 giorni) | **euro 1.350.000,00** |
| Perdita del periodo di capacita ridotta (147 giorni al 45 per cento) | **euro 1.240.312,50** |
| **Perdita lorda** | **euro 2.590.312,50** |
| Franchigia (10 giorni per il margine giornaliero) | **euro 187.500,00** |
| **Perdita al netto della franchigia** | **euro 2.402.812,50** |
| Rettifica per l'andamento dell'attivita, in aumento del **4 per cento** | |
| **Perdita rettificata** | **euro 2.498.925,00** |
| Quota indennizzabile per la regola proporzionale: **80 per cento** | |
| **Indennizzo sulla perdita di margine** | **euro 1.999.140,00** |
| Maggiori costi richiesti euro 340.000,00, sublimite **euro 200.000,00**, ridotto all'80 per cento | |
| **Maggiori costi indennizzabili** | **euro 160.000,00** |
| **Indennizzo complessivo** | **euro 2.159.140,00** |

L'indennizzo è **contenuto entro la somma assicurata** di euro 6.000.000,00.

La franchigia si detrae **moltiplicando i giorni di franchigia per il margine giornaliero**.
La perdita lorda si determina con il **margine giornaliero convenzionale**.

## 5. Rettifica per l'andamento e sottoassicurazione

**Segno della rettifica: in aumento.** Il settore della carta per uso industriale ha
registrato nel 2031 una ripresa della domanda, come riferito dal perito incaricato: si
applica pertanto una rettifica in aumento del **4 per cento**, conforme a quella della
perizia di parte, che sul punto non presenta rilievi.

**Sottoassicurazione.** Il margine dichiarato in polizza, **euro 5.400.000,00**, è
inferiore a quello effettivo, **euro 6.750.000,00**: il grado di sottoassicurazione è del
**20 per cento** e la quota indennizzabile dell'**80 per cento**. È **assicurazione
parziale** con **riduzione proporzionale dell'indennizzo**, e le condizioni **non prevedono
alcuna deroga**.

**Errore della perizia sul punto.** L'osservazione del paragrafo 8, secondo cui lo
scostamento non incide perché l'importo è contenuto entro la somma assicurata, **non
regge**: la **somma assicurata opera come limite massimo di indennizzo**, il **margine
dichiarato come parametro su cui si calcola la proporzione**.

**Maggiori costi.** Il sublimite è **a sua volta soggetto alla riduzione proporzionale**. I
maggiori costi sono indennizzabili **nella misura in cui hanno evitato una perdita di margine
di importo non inferiore**, e il **raffronto non risulta dagli atti**.

## 6. Posizioni dell'assicuratore

**Punto 1, operatività.** **Non regge**: la scheda assicura per **partite** e non elenca i
singoli beni.

**Punto 2, perizia di parte.** La posizione è **conforme alle condizioni**: la perizia
**non vincola l'assicuratore**. In caso di mancato accordo le condizioni prevedono la
**nomina di due periti** e l'**eventuale terzo perito**.

**Punto 3, rettifica.** Il rilievo non è fondato: la rettifica in aumento è sostenuta
dall'andamento del settore.

**Punto 4, sublimite.** Il rilievo è fondato.

**Punto 5, margine dichiarato.** Il rilievo è fondato e conduce alla riduzione
proporzionale.

**Punto 6, acconto.** Le condizioni prevedono un **acconto fino al 50 per cento dell'importo
non contestato**: il rifiuto va contestato. **L'acconto non presuppone la determinazione
definitiva del danno**.

**Punto 7, provvedimento dell'autorità.** **Non regge**: il rapporto dei vigili del fuoco
riferisce l'interdizione **all'area del reparto**, e l'esclusione riguarda i **provvedimenti
non connessi al danno materiale**.

## 7. Scostamento, dati mancanti e azioni

**Scostamento.** La perizia di parte quantifica **euro 2.838.925,00**: lo scostamento
rispetto all'indennizzo qui determinato deriva dalla **mancata applicazione della riduzione
proporzionale** e dal **superamento del sublimite** per i maggiori costi.

**La quantificazione non è definitiva.** Mancano i **dati gestionali dei mesi da settembre
a dicembre 2031**, la **rilevazione analitica dei costi variabili non sostenuti** e la
**documentazione di dettaglio dei maggiori costi**. I dati mancanti **non impediscono ogni
quantificazione**.

**Azioni.**

1. Contestare i punti 1, 3 e 7 della lettera di riserva.
2. **Chiedere l'acconto** sull'importo non contestato.
3. Prendere posizione sui punti 4 e 5, che sono fondati.
4. Acquisire la documentazione di dettaglio dei maggiori costi con il raffronto.
5. Completare i dati gestionali fino alla scadenza del periodo di indennizzo.
6. In mancanza di accordo, attivare la procedura di nomina dei periti.

**Elementi che non costituiscono profili di rischio.** La denuncia è tempestiva. L'ora del
sinistro e il fermo programmato di fine settimana non incidono. La procedura di nomina dei
periti è l'assetto ordinario. Le somme assicurate delle due sezioni sono autonome.
L'affidamento in lavorazione esterna è una misura di contenimento. Le franchigie della
sezione A operano sui danni diretti. Il fermo programmato di luglio 2031 rientra nella
rettifica per l'andamento. Il premio è quietanzato. La facoltà di recesso dopo il sinistro
è una previsione contrattuale applicabile.

Non si afferma che l'assicuratore corrisponderà l'indennizzo determinato.
