# WF2-061 - Distrattore controllato

## Testo del deliverable distrattore

Questa risposta e' completa nel formato ma adotta tre letture rassicuranti incompatibili con il fascicolo. Gli errori sono confinati agli issue indicati nella tabella privata finale.

### Conclusione esecutiva

Nessun ulteriore punto autonomo.

### Mappa dei contratti

- **responsabilita' del contraente principale.** La documentazione non richiede interventi su questo profilo e il punto puo' essere chiuso senza ulteriori verifiche.

### SLA e incidenti

- **SLA non trasferiti al primo subfornitore.** La documentazione non richiede interventi su questo profilo e il punto puo' essere chiuso senza ulteriori verifiche.
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

- **sub-responsabile non autorizzato.** La documentazione non richiede interventi su questo profilo e il punto puo' essere chiuso senza ulteriori verifiche.
- **I-12 - causalita' ancora incompleta.** I log quadir non sono nel fascicolo. Documento: doc. 05 e doc. 06. Azione: sospendere l'attribuzione definitiva del primo incidente e acquisire i log. Conseguenza: la responsabilita' contrattuale e la causa tecnica vanno tenute distinte.

### Azioni entro trenta giorni

- **I-11 - sostituzione del subfornitore.** Il rinnovo proposto non disciplina preavviso e opposizione alla sostituzione. Documento: doc. 01 e doc. 06. Azione: inserire notifica preventiva e diritto di opposizione motivata. Conseguenza: Arcomera non governa la composizione della catena.

## Esiti privati attesi

Issue bersaglio: I-01, I-02, I-08.

| Criterio | Issue | Esito atteso |
|---|---|---|
| B.1 | I-01 | FAIL |
| B.2 | I-02 | FAIL |
| B.8 | I-08 | FAIL |
| B.13 | I-01 | FAIL |
| B.14 | I-02 | FAIL |
| B.20 | I-08 | FAIL |
| B.25 | I-01 | FAIL |
| B.26 | I-02 | FAIL |
| B.32 | I-08 | FAIL |
| B.37 | I-01 | FAIL |

Tutti gli altri 39 criteri restano attesi in PASS. La calibrazione con judge reali non e' stata eseguita.
