# WF2-061 - Scheda per legal validation

Stato: `draft_for_legal_validation`. `pilot_ready`: false.

## Domande che richiedono giudizio professionale

1. Se il trasferimento degli impegni di livello di servizio lungo la catena richieda pattuizione specifica scritta con ciascun subfornitore o sia sufficiente l'obbligo di risultato del contraente principale.
2. Se l'esclusivita' dei service credit pattuita a valle possa essere opposta al cliente finale.
3. Se l'interruzione della catena di audit costituisca inadempimento attuale o soltanto rischio da regolare nel rinnovo.

## Issue da confermare uno per uno

| Issue | Etichetta | Gravita' | Affermazione richiesta |
|---|---|---|---|
| I-01 | responsabilita' del contraente principale | alta | Veltragno resta responsabile verso Arcomera anche quando la causa si colloca a valle |
| I-02 | SLA non trasferiti al primo subfornitore | alta | la soglia 99,50% e il ripristino a 240 minuti non coprono gli impegni 99,95% e 120 minuti |
| I-03 | secondo livello privo di flow-down | alta | Quadir non assume tempi di ripristino ne' exit assistance |
| I-04 | manutenzione non programmata | alta | il preavviso di un giorno non soddisfa la finestra di cinque giorni |
| I-05 | service credit non esclusivi nel contratto principale | alta | l'esclusivita' pattuita a valle non limita i rimedi di Arcomera |
| I-06 | audit interrotto nella catena | alta | Arcomera non puo' verificare direttamente i log dei soggetti a valle |
| I-07 | cambio di localizzazione | media | la comunicazione successiva sul data center non consente controllo preventivo |
| I-08 | sub-responsabile non autorizzato | media | il fascicolo non prova l'autorizzazione specifica o generale a Quadir |
| I-09 | exit assistance assente a valle | media | Veltragno promette novanta giorni di assistenza ma Quadir non e' vincolata |
| I-10 | massimali disallineati | media | il massimale Nembrosa di EUR 300.000 e' inferiore a quello assunto da Veltragno |
| I-11 | sostituzione del subfornitore | media | il rinnovo proposto non disciplina preavviso e opposizione alla sostituzione |
| I-12 | causalita' ancora incompleta | media | i log Quadir non sono nel fascicolo |

## Controlled non-issue da confermare

| Non-issue | Perche' non e' un issue | Criterio di assenza |
|---|---|---|
| N-01 - cifratura a riposo | AES-256 e' una misura dichiarata, non il difetto del caso | B.38 |
| N-02 - primo evento unico | le segnalazioni delle filiali descrivono la stessa indisponibilita' e non tre incidenti | B.39 |
| N-03 - hosting iniziale a Milano | la localizzazione iniziale coincide con il perimetro comunicato | B.40 |
| N-04 - rinnovo ancora non firmato | la proposta non ha ancora modificato il contratto | B.41 |

## Limiti residui

- Validazione legale professionale non eseguita.
- Calibrazione con judge reali non eseguita; il caso resta un draft benchmark-usable.
- Applicabilita' delle fonti congelate alla data futura del caso da confermare in legal sign-off.
- Per i casi di redline, confermare che la revisione mirata copra il perimetro negoziale desiderato senza trasformarsi in riscrittura integrale.
