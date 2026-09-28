# WF2-031 - Decision log

## Impostazione

1. **Perche' `due_diligence_memo` e non un caso di calcolo.** Il prodotto richiesto e' una matrice di
   rilievi con esposizione e copertura, cioe' un red-flag report: il calcolo c'e' ma e' strumentale.
   Il caso resta in macroarea B, dossier analysis.

2. **Distanza dal caso di due diligence esistente.** WF2-026 e' un `due_diligence_memo` in materia di
   protezione dei dati, su un pacchetto di valutazione. Qui variano il verticale (fiscale), i
   meccanismi portanti (metodo di calcolo controintuitivo e fatti distribuiti, invece di gerarchia
   fra documenti) e la forma del deliverable (matrice con esposizione stimata e colonna di copertura
   contrattuale, invece di rilievi bloccanti e non bloccanti per gravita').

3. **Un solo documento che alimenta due issue indipendenti.** L'atto di cessione del ramo d'azienda
   del 3 luglio 2026 e' insieme la fonte della responsabilita' solidale (I-11) e il fatto che integra
   la seconda condizione della limitazione al riporto delle perdite (I-07). Nessuno dei due profili e'
   leggibile da quel documento da solo: il primo richiede la disciplina sulla cessione d'azienda, il
   secondo richiede di collegarlo al trasferimento delle quote. E' la forma piu' economica di fatto
   distribuito.

4. **La catena dell'art. 84 TUIR e' il meccanismo portante.** Tre passaggi, ognuno con una risposta
   intuitiva sbagliata: il cambio di controllo non basta da solo, ma qui la seconda condizione
   ricorre; il test si supera confrontando con il quaranta per cento della media, non con la media;
   superato il test il riporto resta limitato al patrimonio netto contabile, al netto dei versamenti
   recenti. Ogni scorciatoia produce un numero plausibile e diverso, e ognuno di quei numeri e'
   presidiato da un criterio `assenza` nominato.

## Scelte di merito

5. **Il test di vitalita' passa, e passa stretto.** Cinque per cento di margine sui ricavi e nove per
   cento sulle spese di lavoro. Se il test fallisse, la catena si fermerebbe al secondo passaggio e
   il terzo non sarebbe misurabile. Il margine stretto rende discriminante il metodo senza rendere
   decisivo l'arrotondamento.

6. **Il rilievo di competenza e' l'unico rilievo del verbale che va sottratto all'esposizione.** Serve
   a misurare il failure mode opposto a quello consueto: non l'omissione, ma la sovra-quantificazione
   di un rilievo che c'e' ma non vale l'imposta piena. Il periodo 2021 decaduto misura la stessa cosa
   su un altro asse.

7. **La nota del direttore amministrativo dice quattro cose vere e tre conclusioni sbagliate.** Le
   date che fornisce (presentazione della dichiarazione, protocollo, casella del quadro RS) sono
   esatte e servono al modello; le conclusioni che ne trae (fondo capiente, tema del ramo chiuso,
   perdite integralmente riportabili, sanzioni disapplicate) sono smentite dai documenti. E' il
   meccanismo della dichiarazione di parte smentita dai documenti nella forma piu' insidiosa: la
   parte non mente sui fatti.

8. **La franchigia non e' una trappola.** L'articolo 9.7 la esclude per la materia fiscale: e'
   deliberatamente una clausola a favore dell'acquirente, ed e' il controlled non-issue che misura
   l'errore di lato. La trappola di adeguatezza sta altrove, nella durata della garanzia e nella
   deduzione degli accantonamenti.

9. **Il limite massimo di indennizzo e' capiente.** Anche questo e' deliberato: in un caso di
   acquisto e' l'oggetto piu' facile da segnalare come rischio, e qui non lo e'. Serve a misurare la
   sovra-segnalazione su un elemento che il modello e' addestrato a cercare.

10. **Le sanzioni non sono quantificate.** Vedi `source/authoring/legal_validation.md`, sezione
    "Punti dichiarati e non risolti". La misura applicabile dipende dal regime vigente al momento
    della violazione e la ricostruzione del regime previgente non ha raggiunto il grado di certezza
    che il progetto richiede per scrivere un riferimento in un criterio. Il caso e' costruito perche'
    quella lacuna non incida su alcun criterio, ed e' dichiarata.

## Scelte di costruzione

11. **Il fascicolo non contiene le dichiarazioni dei redditi.** Alla data di riferimento la
    dichiarazione del periodo 2027 non e' ancora dovuta, e le altre non sono state consegnate dai
    venditori: e' una situazione ordinaria in una data room. Gli elementi fiscali necessari passano
    dai prospetti di riconciliazione delle note integrative, che sono informativa di bilancio
    obbligatoria. La loro assenza diventa una voce dell'issue I-15.

12. **La voce A.5 del conto economico e' azzerata in tutti e tre gli esercizi.** Cosi' il perimetro
    dei ricavi della gestione caratteristica non e' opinabile e le due letture possibili del test non
    producono soglie diverse. E' una scelta di igiene del caso: l'ambiguita' avrebbe reso non
    verificabile un criterio di tipo `valore`.

13. **Il layout del lotto e i nomi canonici convivono.** I file richiesti dal lotto sono i file reali;
    i nomi attesi da `_tools/validate_case.py` sono collegamenti simbolici allo stesso contenuto. Non
    esistono due copie di nulla e non c'e' rischio di divergenza.
