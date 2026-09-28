# WF2-032 - Decision log

## Impostazione

1. **Perche' `deadline_chain` e non `single_deadline`.** Il deliverable non e' una data ma un audit:
   sei termini, tre gia' scaduti e rispettati, uno aperto, uno futuro e uno eventuale a carico
   dell'Ufficio. La domanda del cliente e' che cosa fare e quando, non soltanto entro quando.

2. **Distanza dai due `deadline_chain` esistenti.** Sul corpus ci sono gia' un caso in materia di
   somministrazione e uno in materia di sanzioni internazionali. Qui variano il verticale, che e'
   nuovo, e il meccanismo portante: non la concatenazione di eventi contrattuali, ma la
   qualificazione dell'atto che ha sospeso il termine.

3. **Il perno e' una regola speciale che ribalta quella generale.** Chiunque conosca la materia sa
   che l'istanza di accertamento con adesione sospende i termini per novanta giorni. Qui la
   sospensione e' di trenta, perche' l'avviso e' stato preceduto dallo schema di atto e l'istanza e'
   stata presentata dopo la notifica. E' il meccanismo del termine dipendente dalla qualificazione:
   la risposta intuitiva e' quella sbagliata, e la differenza fra le due letture e' di sessanta
   giorni.

## Scelte di merito

4. **Quattro variabili indipendenti sullo stesso termine.** Data di notificazione contro data
   dell'atto; durata della sospensione da adesione; sospensione feriale; giorno della settimana in cui
   cade la scadenza. Ognuna produce una data diversa e ognuna ha un criterio `assenza` che nomina la
   data sbagliata. Nessuna delle cinque derivazioni errate coincide con il termine effettivo: e'
   verificato con script.

5. **La scadenza cade di sabato.** Non e' un dettaglio: e' l'unico modo per misurare se il modello
   conosce la proroga dell'art. 155, comma 5, invece di quella del comma 4. La differenza e' di due
   giorni, non di uno.

6. **La nota del consulente sbaglia sei volte e si contraddice una.** Afferma insieme che il termine
   scade in dicembre per effetto della sospensione di novanta giorni e che il decorso e' ripreso dal
   verbale di settembre. Le due affermazioni non stanno insieme, e il caso non lo segnala: e' compito
   dell'agente accorgersene. E' la forma piu' netta del meccanismo della dichiarazione di parte
   smentita dai documenti, perche' qui la parte e' un professionista.

7. **La riduzione delle sanzioni non e' risolta.** L'art. 15 richiede la rinuncia anche all'istanza
   di adesione, che la societa' ha presentato. La questione ha soluzioni argomentabili e il caso non
   ne impone una: chiede di segnalarla e vieta di darla per acquisita. E' l'applicazione della regola
   di progetto per cui le questioni che richiedono sign-off vanno dichiarate, non risolte fingendo
   certezza.

8. **Il reclamo e' il controlled non-issue piu' insidioso.** E' stato per anni il passaggio obbligato
   per le liti di valore contenuto ed e' presente in tutto il materiale su cui i modelli sono
   addestrati. Qui e' abrogato, e la nota del consulente lo suggerisce: chi lo inserisce nell'audit
   fa perdere al cliente il termine per il ricorso.

## Scelte di costruzione

9. **La ricevuta di accettazione e quella di consegna sono dello stesso giorno.** Nella posta
   elettronica certificata lo sono davvero, a un minuto di distanza. Il caso non costruisce una
   trappola artificiale sulla differenza fra le due ricevute: la trappola sulla decorrenza e' fra la
   data dell'atto, il 17 giugno, e la data della notificazione, il 20 giugno.

10. **Il totale delle maggiori imposte e' divisibile per tre.** L'importo iscrivibile a titolo
    provvisorio e' quindi un numero esatto: il criterio di tipo `valore` non dipende
    dall'arrotondamento.

11. **Il fascicolo ha sette documenti.** Meno di quelli del caso di due diligence dello stesso lotto,
    e di natura diversa: qui contano le date e i protocolli, non i numeri. La lunghezza non ha
    funzione oltre quella.
