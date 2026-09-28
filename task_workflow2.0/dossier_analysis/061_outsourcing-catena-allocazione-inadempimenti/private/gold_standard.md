# WF2-061 - Gold standard

**Deliverable atteso:** multi_contract_memo.md.

## Testo sostanziale del deliverable

### Conclusione esecutiva

Alla data di riferimento il fascicolo richiede le decisioni indicate sotto. Sono stati esaminati doc. 01, doc. 02, doc. 03, doc. 04, doc. 05, doc. 06; fatti, inferenze e lacune restano distinti.

Nessun ulteriore punto autonomo; valgono le azioni e le lacune gia' documentate nelle sezioni precedenti.

### Mappa dei contratti

- **I-01 - responsabilita' del contraente principale.** Veltragno resta responsabile verso arcomera anche quando la causa si colloca a valle. Documento: doc. 01 clausola 12 e doc. 03. Azione: rifiutare ogni rinvio diretto del reclamo a Nembrosa. Conseguenza: la catena contrattuale non spezza il rapporto principale.

### SLA e incidenti

- **I-02 - SLA non trasferiti al primo subfornitore.** La soglia 99,50% e il ripristino a 240 minuti non coprono gli impegni 99,95% e 120 minuti. Documento: doc. 02 e doc. 03. Azione: imporre flow-down integrale o buffer misurabile. Conseguenza: Veltragno sopporta uno scoperto prestazionale.
- **I-04 - manutenzione non programmata.** Il preavviso di un giorno non soddisfa la finestra di cinque giorni. Documento: doc. 02 e doc. 05. Azione: conteggiare i 94 minuti nella disponibilita' di febbraio. Conseguenza: l'esclusione SLA non opera.

### Audit e subfornitura

- **I-03 - secondo livello privo di flow-down.** Quadir non assume tempi di ripristino ne' exit assistance. Documento: doc. 03 e doc. 04. Azione: estendere SLA, audit e uscita a Quadir. Conseguenza: un guasto del data center resta senza rimedio back-to-back.
- **I-06 - audit interrotto nella catena.** Arcomera non puo' verificare direttamente i log dei soggetti a valle. Documento: doc. 01, doc. 03 e doc. 06. Azione: introdurre accesso per Arcomera o audit indipendente su Nembrosa e Quadir. Conseguenza: manca la prova tecnica per allocare i due incidenti.
- **I-07 - cambio di localizzazione.** La comunicazione successiva sul data center non consente controllo preventivo. Documento: doc. 04. Azione: richiedere autorizzazione preventiva per trasferimenti fuori dal perimetro concordato. Conseguenza: la governance dei dati dipende da una notifica tardiva.
- **I-09 - exit assistance assente a valle.** Veltragno promette novanta giorni di assistenza ma quadir non e' vincolata. Documento: doc. 01 e doc. 04. Azione: replicare durata, formati e cooperazione nel contratto Quadir. Conseguenza: la migrazione puo' bloccarsi all'ultimo livello.

### Responsabilita' e rimedi

- **I-05 - service credit non esclusivi nel contratto principale.** L'esclusivita' pattuita a valle non limita i rimedi di arcomera. Documento: doc. 01 e doc. 03. Azione: preservare risarcimento e rimedi contrattuali principali. Conseguenza: Veltragno non puo' trasferire a monte il limite di Nembrosa.
- **I-10 - massimali disallineati.** Il massimale nembrosa di eur 300.000 e' inferiore a quello assunto da veltragno. Documento: doc. 01 e doc. 03. Azione: negoziare massimale e copertura assicurativa coerenti con l'esposizione. Conseguenza: resta una quota non recuperabile a valle.

### Dati mancanti

- **I-08 - sub-responsabile non autorizzato.** Il fascicolo non prova l'autorizzazione specifica o generale a quadir. Documento: doc. 01 e doc. 04. Azione: acquisire la catena di nomina e il registro delle opposizioni. Conseguenza: non e' dimostrata la regolarita' del sub-processing.
- **I-12 - causalita' ancora incompleta.** I log quadir non sono nel fascicolo. Documento: doc. 05 e doc. 06. Azione: sospendere l'attribuzione definitiva del primo incidente e acquisire i log. Conseguenza: la responsabilita' contrattuale e la causa tecnica vanno tenute distinte.

### Azioni entro trenta giorni

- **I-11 - sostituzione del subfornitore.** Il rinnovo proposto non disciplina preavviso e opposizione alla sostituzione. Documento: doc. 01 e doc. 06. Azione: inserire notifica preventiva e diritto di opposizione motivata. Conseguenza: Arcomera non governa la composizione della catena.

## Note private di controllo (non fanno parte del deliverable)

Controlled non-issue verificati come assenze:

- N-01 - cifratura a riposo: non e' elencato come rischio o criticita'; la mera menzione fattuale resta ammessa.
- N-02 - primo evento unico: non e' elencato come rischio o criticita'; la mera menzione fattuale resta ammessa.
- N-03 - hosting iniziale a Milano: non e' elencato come rischio o criticita'; la mera menzione fattuale resta ammessa.
- N-04 - rinnovo ancora non firmato: non e' elencato come rischio o criticita'; la mera menzione fattuale resta ammessa.

Il deliverable applica il criterio di simmetria nominato in rubrica e non presume l'esito di decisioni giudiziali, amministrative, assicurative o brevettuali.

## Verifica criterio per criterio

| Criterio | Esito | Ancora nel gold |
|---|---|---|
| A.1 | PASS | ogni file atteso esiste con il nome indicato |
| A.2 | PASS | il conteggio e' al massimo 3.200 |
| A.3 | PASS | tutte le sezioni compaiono nell'ordine |
| A.4 | PASS | tutti gli allegati sono richiamati |
| A.5 | PASS | ogni fonte citata compare in 03_legal_sources.md |
| A.6 | PASS | le tre categorie sono distinguibili |
| B.1 | PASS | la proposizione compare in una frase autonoma: Veltragno resta responsabile verso Arcomera anche quando la causa si colloca a valle |
| B.2 | PASS | nel deliverable compare «la soglia 99,50% e il ripristino a 240 minuti non coprono gli impegni 99,95% e 120 minuti» |
| B.3 | PASS | la proposizione compare in una frase autonoma: Quadir non assume tempi di ripristino ne' exit assistance |
| B.4 | PASS | nel deliverable compare «il preavviso di un giorno non soddisfa la finestra di cinque giorni» |
| B.5 | PASS | la proposizione compare in una frase autonoma: l'esclusivita' pattuita a valle non limita i rimedi di Arcomera |
| B.6 | PASS | la proposizione compare in una frase autonoma: Arcomera non puo' verificare direttamente i log dei soggetti a valle |
| B.7 | PASS | la proposizione compare in una frase autonoma: la comunicazione successiva sul data center non consente controllo preventivo |
| B.8 | PASS | la proposizione compare in una frase autonoma: il fascicolo non prova l'autorizzazione specifica o generale a Quadir |
| B.9 | PASS | la proposizione compare in una frase autonoma: Veltragno promette novanta giorni di assistenza ma Quadir non e' vincolata |
| B.10 | PASS | nel deliverable compare «il massimale Nembrosa di EUR 300.000 e' inferiore a quello assunto da Veltragno» |
| B.11 | PASS | la proposizione compare in una frase autonoma: il rinnovo proposto non disciplina preavviso e opposizione alla sostituzione |
| B.12 | PASS | la proposizione compare in una frase autonoma: i log Quadir non sono nel fascicolo |
| B.13 | PASS | la stessa frase, riga di tabella o nota collega il punto a doc. 01 clausola 12 e doc. 03 |
| B.14 | PASS | la stessa frase, riga di tabella o nota collega il punto a doc. 02 e doc. 03 |
| B.15 | PASS | la stessa frase, riga di tabella o nota collega il punto a doc. 03 e doc. 04 |
| B.16 | PASS | la stessa frase, riga di tabella o nota collega il punto a doc. 02 e doc. 05 |
| B.17 | PASS | la stessa frase, riga di tabella o nota collega il punto a doc. 01 e doc. 03 |
| B.18 | PASS | la stessa frase, riga di tabella o nota collega il punto a doc. 01, doc. 03 e doc. 06 |
| B.19 | PASS | la stessa frase, riga di tabella o nota collega il punto a doc. 04 |
| B.20 | PASS | la stessa frase, riga di tabella o nota collega il punto a doc. 01 e doc. 04 |
| B.21 | PASS | la stessa frase, riga di tabella o nota collega il punto a doc. 01 e doc. 04 |
| B.22 | PASS | la stessa frase, riga di tabella o nota collega il punto a doc. 01 e doc. 03 |
| B.23 | PASS | la stessa frase, riga di tabella o nota collega il punto a doc. 01 e doc. 06 |
| B.24 | PASS | la stessa frase, riga di tabella o nota collega il punto a doc. 05 e doc. 06 |
| B.25 | PASS | l'azione e' formulata come richiesta: rifiutare ogni rinvio diretto del reclamo a Nembrosa |
| B.26 | PASS | l'azione e' formulata come richiesta: imporre flow-down integrale o buffer misurabile |
| B.27 | PASS | l'azione e' formulata come richiesta: estendere SLA, audit e uscita a Quadir |
| B.28 | PASS | l'azione e' formulata come richiesta: conteggiare i 94 minuti nella disponibilita' di febbraio |
| B.29 | PASS | l'azione e' formulata come richiesta: preservare risarcimento e rimedi contrattuali principali |
| B.30 | PASS | l'azione e' formulata come richiesta: introdurre accesso per Arcomera o audit indipendente su Nembrosa e Quadir |
| B.31 | PASS | l'azione e' formulata come richiesta: richiedere autorizzazione preventiva per trasferimenti fuori dal perimetro concordato |
| B.32 | PASS | l'azione e' formulata come richiesta: acquisire la catena di nomina e il registro delle opposizioni |
| B.33 | PASS | l'azione e' formulata come richiesta: replicare durata, formati e cooperazione nel contratto Quadir |
| B.34 | PASS | l'azione e' formulata come richiesta: negoziare massimale e copertura assicurativa coerenti con l'esposizione |
| B.35 | PASS | l'azione e' formulata come richiesta: inserire notifica preventiva e diritto di opposizione motivata |
| B.36 | PASS | l'azione e' formulata come richiesta: sospendere l'attribuzione definitiva del primo incidente e acquisire i log |
| B.37 | PASS | la conseguenza e' espressa nel testo: la catena contrattuale non spezza il rapporto principale |
| B.38 | PASS | sovra-segnalazione - cifratura a riposo non e' presentato come rischio, criticita', inadempimento o conclusione negativa |
| B.39 | PASS | sovra-segnalazione - primo evento unico non e' presentato come rischio, criticita', inadempimento o conclusione negativa |
| B.40 | PASS | sovra-segnalazione - hosting iniziale a Milano non e' presentato come rischio, criticita', inadempimento o conclusione negativa |
| B.41 | PASS | sovra-segnalazione - rinnovo ancora non firmato non e' presentato come rischio, criticita', inadempimento o conclusione negativa |
| B.42 | PASS | simmetria del controllo non e' presentato come rischio, criticita', inadempimento o conclusione negativa |
| B.43 | PASS | presunzione dell'esito non e' presentato come rischio, criticita', inadempimento o conclusione negativa |
