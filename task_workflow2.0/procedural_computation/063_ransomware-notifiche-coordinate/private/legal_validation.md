# WF2-063 - Scheda per legal validation

Stato: `draft_for_legal_validation`. `pilot_ready`: false.

## Domande che richiedono giudizio professionale

1. Confermare l'applicazione dell'art. 25 del D.Lgs. 138/2024 al soggetto e all'incidente descritti, inclusa la relazione sui progressi se l'incidente perdura oltre il mese.
2. Qualificazione del rischio elevato per gli interessati in presenza di dati relativi alla salute ed esfiltrazione, e conseguente obbligo di comunicazione.
3. Se il momento di conoscenza rilevante sia l'acquisizione di certezza ragionevole e non il primo alert tecnico.
4. Se il termine di 24 ore verso il cliente sia contrattuale e non normativo, e come si coordini con i termini di legge.

## Issue da confermare uno per uno

| Issue | Etichetta | Gravita' | Affermazione richiesta |
|---|---|---|---|
| I-01 | momento di conoscenza del titolare | alta | il dies a quo di Saliceto e' il 16 febbraio alle 08:20, non il primo alert delle 06:42 |
| I-02 | obbligo del responsabile | alta | Kairone doveva informare senza ritardo e comunque entro il limite contrattuale |
| I-03 | pre-notifica NIS entro 24 ore | alta | la scadenza e' 17 febbraio 2027 alle 08:20 |
| I-04 | notifica NIS entro 72 ore | alta | la scadenza e' 19 febbraio 2027 alle 08:20 |
| I-05 | relazione finale NIS | alta | la relazione finale va calendarizzata a un mese dalla notifica completa, con aggiornamenti se l'incidente perdura |
| I-06 | notifica GDPR entro 72 ore | alta | la scadenza e' 19 febbraio 2027 alle 08:20 e il rischio non e' improbabile |
| I-07 | comunicazione agli interessati | alta | dati sanitari ed esfiltrazione sostengono un rischio elevato |
| I-08 | avviso all'assicuratore | alta | le 48 ore scadono il 18 febbraio 2027 alle 08:20 |
| I-09 | avviso al cliente Cerasia | media | le 24 ore scadono il 17 febbraio 2027 alle 08:20 |
| I-10 | runbook con termini fusi | media | la regola unica delle 72 ore omette NIS 24h, polizza 48h e cliente 24h |
| I-11 | owner NIS errato | media | il punto di contatto NIS e' direzione sicurezza, non DPO |
| I-12 | bozza interessati incompleta | media | la bozza omette l'esfiltrazione e il recapito |
| I-13 | notifica per fasi | media | l'incertezza sulla composizione dei 62 GB non giustifica attendere |
| I-14 | conservazione probatoria | media | immagini, log e indicatori devono restare integri mentre si ripristina |
| I-15 | riscatto non sospensivo | media | la scadenza imposta dall'attaccante non sospende notifiche |
| I-16 | registro unico dei fatti, decisioni separate | media | i medesimi fatti alimentano cinque flussi ma i test giuridici non coincidono |
| I-17 | lacuna sull'estensione | media | non e' noto quali record compongano tutti i 62 GB |

## Controlled non-issue da confermare

| Non-issue | Perche' non e' un issue | Criterio di assenza |
|---|---|---|
| N-01 - primo alert non qualificato | alle 06:42 mancava ragionevole certezza | B.59 |
| N-02 - backup clinici integri | l'integrita' dei backup mitiga disponibilita' ma non elimina l'esfiltrazione | B.60 |
| N-03 - scadenza del riscatto | e' un fatto operativo e non un termine normativo | B.61 |
| N-04 - festivita' e fine settimana | i termini in ore non slittano al giorno lavorativo | B.62 |
| N-05 - DPO consultato | la consultazione privacy e' utile; e' errata solo l'attribuzione del flusso NIS | B.63 |

## Limiti residui

- Validazione legale professionale non eseguita.
- Calibrazione con judge reali non eseguita; il caso resta un draft benchmark-usable.
- Applicabilita' delle fonti congelate alla data futura del caso da confermare in legal sign-off.
- Per i casi di redline, confermare che la revisione mirata copra il perimetro negoziale desiderato senza trasformarsi in riscrittura integrale.
