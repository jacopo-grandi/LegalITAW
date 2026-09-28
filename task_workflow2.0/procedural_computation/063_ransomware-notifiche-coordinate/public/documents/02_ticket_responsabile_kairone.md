# KAI-SEC-7781 — Attività ostile su ambiente cliente SAL

Export del ticket dal service desk Kairone (kairone.service-now.example) — estratto il 16/02/2027 alle 09:22 da N. Fiorenzi
Condiviso con: soc@saliceto.example, sicurezza@saliceto.example (allegato al messaggio KAI/2027/0216-02)

## Campi del ticket

| Campo | Valore |
|---|---|
| Numero | KAI-SEC-7781 |
| Coda | SEC — Incident Response |
| Cliente | Saliceto Salute Digitale S.p.A. (codice cliente SAL) |
| Contratto | Servizi gestiti KAI/SAL-2024-09 — Addendum sul trattamento dei dati personali del 12/09/2024 |
| Aperto il | 16/02/2027 05:55 (fuso Europe/Rome) |
| Aperto da | monitoraggio automatico — regola KSEC-EDR-441 |
| Presa in carico | 16/02/2027 06:04 — M. Rovere (turno notte) |
| Duty manager | N. Fiorenzi |
| Priorità | P1 (elevata da P2 alle 07:12) |
| Categoria | Malware / esecuzione non autorizzata |
| Stato | In lavorazione |
| Sistemi in perimetro Kairone | 41 host: dominio, ipervisori, backup appliance, VPN fornitori, file server amministrativi |

## Diario attività

**16/02/2027 05:55 — sistema (KSEC-EDR-441)**
Rilevate esecuzioni anomale su tre host del segmento infrastrutturale del cliente SAL: catena di processi non riconducibile a pacchetti distribuiti, uso di utilità di sistema per l'enumerazione delle condivisioni, tentativi di accesso a percorsi amministrativi. Apertura automatica del ticket.

**16/02/2027 06:04 — M. Rovere**
Preso in carico. Verificati i tre host: la catena non corrisponde a nessuna attività pianificata sul calendario cambi. Estratti i primi indicatori (hash, nomi processo, account utilizzati). Avviata raccolta log.

**16/02/2027 06:40 — M. Rovere**
Riscontrato uso di due account di servizio con privilegi elevati fuori dagli orari abituali. Un terzo host mostra la stessa catena. Richiesta escalation al duty manager.

**16/02/2027 07:12 — N. Fiorenzi**
Priorità elevata a P1. Il quadro è compatibile con un'intrusione attiva sull'ambiente del cliente. Attivata la procedura di notifica al titolare prevista dall'addendum. Preparo la comunicazione preliminare con quanto disponibile: non attendiamo il completamento dell'analisi, come previsto dal contratto.

**16/02/2027 07:48 — N. Fiorenzi**
Inviato avviso preliminare al cliente SAL (soc@saliceto.example e sicurezza@saliceto.example), messaggio KAI/2027/0216-01, oggetto «Segnalazione preliminare di sicurezza — ambiente SAL». Contenuto: rilevazione delle 05:55, tre host interessati, uso di credenziali privilegiate, indicatori disponibili in allegato, invito a verificare i sistemi non amministrati da Kairone. Confermata ricezione dal turno SOC del cliente.

**16/02/2027 08:35 — M. Rovere**
Su richiesta del cliente sono stati disabilitati gli account di servizio compromessi e revocate le sessioni VPN dei profili fornitore. Il backup appliance non risulta interessato dalle catene di esecuzione rilevate; verifica in corso sui punti di ripristino.

**16/02/2027 09:05 — N. Fiorenzi**
Trasmessa integrazione (messaggio KAI/2027/0216-02): elenco completo degli indicatori di compromissione, tracciato delle esecuzioni per host, elenco dei 41 sistemi amministrati da Kairone con stato al momento della verifica, export del presente ticket. Comunicazione al titolare effettuata alle 07:48, entro il termine di dodici ore previsto dall'art. 7.3 dell'addendum. Le ulteriori informazioni saranno fornite progressivamente man mano che l'analisi procede.

## Riferimento contrattuale richiamato nel ticket

Art. 7.3 dell'Addendum sul trattamento dei dati personali: «Il responsabile informa il titolare senza ingiustificato ritardo e comunque entro dodici ore dal momento in cui viene a conoscenza di una violazione dei dati personali o di un incidente di sicurezza che possa determinarla, fornendo le informazioni disponibili al momento dell'avviso e integrandole progressivamente.»

## Prossime attività a carico di Kairone

- Consegna del tracciato completo delle autenticazioni dei due account di servizio (attesa entro le 13:00).
- Verifica dei punti di ripristino sul backup appliance e riscontro scritto al cliente.
- Supporto al team forense incaricato dal cliente per l'acquisizione delle immagini degli ipervisori.
- Aggiornamento del ticket a ogni nuovo elemento; il cliente riceve copia degli aggiornamenti sulla stessa catena di messaggi.
