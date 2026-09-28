# WF2-053 - Distrattore controllato

## Criteri che questa versione intende far fallire, dichiarati prima dell'esecuzione

- `B.6` - afferma che l'esenzione per gli strumenti di lavoro copre la finalità della lettera c)
- `B.9` - non qualifica come non integrato il presupposto procedurale
- `B.10` - afferma che l'illustrazione alle rappresentanze integra l'accordo richiesto
- `C.2` - segnala le statistiche aggregate come controllo individuale

Nessun altro criterio deve fallire. Se il fallimento si propaga a criteri
limitrofi, l'atomizzazione non ha funzionato e va rivista.

## Criteri che devono restare superati

- B.1, B.2, B.3 e B.4: base giuridica, clausola 3.2 e divieto di negare ogni base
- B.5 e B.7: qualificazione della finalità e soppressione nel redline
- B.8: rilievo sulla dichiarazione delle rappresentanze
- B.11, B.12, B.13 e B.14: conservazione dei metadati
- B.15, B.16 e B.17: affermazione tecnica dell'articolo 7.3
- B.18 e B.19: log di navigazione
- B.20, B.21 e B.22: qualificazione del fornitore
- B.23, B.24, B.25 e B.26: procedura di accesso alle caselle
- B.27, B.28 e B.29: informativa specifica
- B.30: utilizzabilità dei dati
- B.31, B.32 e B.33: valutazione preliminare
- B.34 e B.35: cessazione del rapporto
- B.36, B.37 e B.38: disattivazione e riscontro alle osservazioni
- C.1, C.3, C.4 e C.5: nessuna sovra-segnalazione sugli altri controlled non-issue
- C.6, C.7 e C.8: nessuna asimmetria, nessuna presunzione di intervento dell'autorità

## Limite dichiarato

La verifica che il fallimento colpisca esattamente i criteri elencati e nessun
altro richiede un'esecuzione con judge reali, che questa sessione non ha svolto.
Il controllo meccanico eseguito riguarda le sole stringhe verificabili: le
varianti dei criteri `valore` restano presenti nel distrattore e le stringhe
vietate dai criteri `assenza` non mirati restano assenti.

## Testo

## 1. Sintesi dei rilievi

La bozza PL-07 richiede interventi su base giuridica, periodi di conservazione,
qualificazione del fornitore, procedura di accesso, informativa e cessazione del rapporto.
La finalità di verifica della produttività è invece assistita dal presupposto
procedurale.

## 2. Base giuridica e perimetro lavoristico

**Base giuridica (art. 3.1).** Il **consenso del lavoratore non è la base giuridica
applicabile**: la clausola 3.2, che subordina l'assegnazione degli strumenti al consenso,
**incide sulla libera prestazione del consenso**. Le finalità delle lettere a) e b) vanno
ricondotte all'interesse legittimo alla sicurezza della rete e delle informazioni; quella
della lettera d) all'interesse legittimo alla tutela dei diritti del titolare.

**Finalità della lettera c) (art. 2.2).** La verifica della produttività è **controllo a
distanza dell'attività lavorativa**. Il redline la **sopprime** in via prudenziale.

**Presupposto procedurale.** Il verbale del 5 febbraio 2031 documenta l'illustrazione alle
rappresentanze sindacali: **l'informativa resa alle rappresentanze integra l'accordo
richiesto** e il presupposto risulta soddisfatto. Le rappresentanze hanno dichiarato di
**non sottoscrivere alcun accordo**, ma la procedura di consultazione è stata comunque
espletata.

**Utilizzabilità.** In assenza di informazione adeguata sulle modalità d'uso e sui
controlli, **i dati raccolti non sono utilizzabili a tutti i fini connessi al rapporto di
lavoro**.

## 3. Conservazione e configurazione tecnica

**Metadati (art. 7.2).** La bozza prevede **180 giorni**. Il termine orientativo indicato
dall'autorità di controllo è di **21 giorni**, e la bozza **non documenta condizioni
particolari** che ne rendano necessaria l'estensione.

**Affermazione dell'art. 7.3.** È **contraddetta dalla scheda tecnica**, che indica il
periodo come configurabile **da 7 a 365 giorni** e i 180 giorni come valore preimpostato di
fabbrica.

**Disattivazione.** La raccolta del campo oggetto e quella dei record **sono
disattivabili**: la scelta va documentata e motivata.

**Log di navigazione (art. 8.1).** I **12 mesi** previsti **non sono correlati ad alcuna
finalità determinata**.

## 4. Ruoli, accessi e trasparenza

**Fornitore (art. 4.3).** Va qualificato come **responsabile del trattamento**. Va
stipulato o verificato l'atto che disciplina il trattamento.

**Accesso alle caselle (art. 6.1).** La **sola richiesta del responsabile di funzione non
basta**. Il redline introduce autorizzazione congiunta, parere del responsabile della
protezione dei dati, **registrazione dell'accesso** e informazione all'interessato: misure
che **la piattaforma rende disponibili**. Va dato riscontro all'osservazione del
coordinatore sindacale.

**Informativa (art. 10.1).** L'**informativa vigente non contempla i metadati né i
controlli**. Il redline impone un'informativa specifica **prima dell'entrata in vigore**.

**Cessazione del rapporto (art. 9).** La bozza **non disciplina la sorte della casella alla
cessazione**.

**Valutazione preliminare d'impatto.** La conclusione è **contraddetta dal contenuto della
bozza** e **va riesaminata**.

**Statistiche (art. 5).** Le statistiche aggregate consentono comunque di ricostruire i
comportamenti individuali dei lavoratori e vanno considerate una forma di **controllo
individuale**: la clausola va soppressa.

## 5. Elementi che non richiedono modifica

**Sub-responsabile di assistenza.** Ha sede in un **paese con decisione di adeguatezza**.

**Designazione del responsabile della protezione dei dati (art. 11).** Adempimento assolto.

**Conservazione per la durata del rapporto (art. 9.1).** Non è di per sé eccedente.

**Rinvio al contratto collettivo (art. 12.1).** Formulazione corrente.

**Certificazione del fornitore.** Informazione sul fornitore, non profilo di rischio.

## 6. Azioni

1. Adottare il testo con le revisioni proposte.
2. Aggiornare l'informativa e renderla **prima** dell'entrata in vigore.
3. Configurare il periodo di conservazione ridotto e documentare la scelta.
4. Stipulare o verificare l'atto sul trattamento da parte del fornitore.
5. Riesaminare la valutazione preliminare VP-2031-004.
6. Sopprimere la clausola sulle statistiche.
