# Alteforge Cyber Response S.r.l.

## RELAZIONE DI ANALISI FORENSE - VERSIONE PRELIMINARE

Riferimento incarico AF-2031-0117 - Cliente: Casaltino Retail S.p.A. - Data di emissione: 4 aprile 2031

### 1. Incarico e perimetro

Alteforge Cyber Response S.r.l. ha ricevuto incarico da Casaltino Retail S.p.A. in data 14 marzo 2031 per l'analisi tecnica dell'evento occorso ai sistemi informatici della società. Il perimetro comprende l'infrastruttura di data center di Sesto Fiorentino, la piattaforma di vendita e i sistemi di posta. La presente relazione ha carattere preliminare: l'analisi degli archivi copiati è in corso.

### 2. Sintesi

L'attacco è stato condotto da un gruppo che opera con schema a doppia estorsione: copia degli archivi, cifratura dei sistemi e richiesta di pagamento. L'accesso iniziale è avvenuto tramite credenziali valide di un'utenza di manutenzione, prive di secondo fattore. La piattaforma di vendita è rimasta indisponibile dalle 05:40 del 14 marzo 2031 alle 19:10 del 16 marzo 2031.

### 3. Cronologia ricostruita

| Data e ora (fuso Europa/Roma) | Evento | Fonte tecnica |
|---|---|---|
| 12 marzo 2031, 21:15 | primo accesso non autorizzato al concentratore VPN mediante credenziali valide di un'utenza di manutenzione | log di autenticazione del concentratore |
| 12 marzo 2031, 23:48 | creazione di un'utenza amministrativa locale sul controller di dominio | registro eventi di sicurezza del controller |
| 13 marzo 2031, 02:10 - 13 marzo 2031, 18:35 | ricognizione della rete interna e copia di archivi dal file server commerciale, per complessivi 214 GB | flussi di rete e log del file server |
| 13 marzo 2031, 22:02 | disattivazione dei servizi di copia di sicurezza | log della piattaforma di backup |
| 14 marzo 2031, 05:40 | avvio della cifratura dei volumi di produzione e arresto dei servizi applicativi: da questo momento la piattaforma di vendita non è raggiungibile | log dei sistemi di virtualizzazione; monitoraggio di disponibilità |
| 14 marzo 2031, 06:20 | la responsabile dei sistemi informativi apre l'incidente in seguito agli avvisi automatici e constata la cifratura dei volumi | ticket INC-2031-0392 del sistema di gestione degli incidenti |
| 14 marzo 2031, 07:05 | isolamento della rete e attivazione del presente fornitore | verbale interno di attivazione |
| 14 marzo 2031, 15:30 | ricezione della richiesta di pagamento in criptovaluta con minaccia di pubblicazione degli archivi copiati | messaggio depositato sui sistemi cifrati |
| 15 marzo 2031, 09:00 - 16 marzo 2031, 19:10 | ricostruzione dei sistemi da copie di sicurezza off-line e riavvio progressivo dei servizi | registro delle attività di ripristino |
| 16 marzo 2031, 19:10 | ripristino completo dell'operatività della piattaforma di vendita | monitoraggio di disponibilità |

### 4. Dati coinvolti

Gli archivi copiati contengono anagrafiche e storico ordini di clienti persone fisiche, per un numero stimato in 148.000 posizioni, e i dati di contatto dei referenti commerciali dei partner. Non risultano coinvolti dati di pagamento, conservati presso il gestore esterno. Alla data della presente relazione non risulta pubblicazione degli archivi.

### 5. Attività di contenimento

Isolamento perimetrale, revoca di tutte le credenziali privilegiate, ricostruzione del controller di dominio, ripristino da copie off-line non raggiunte dalla cifratura. Nessun pagamento è stato effettuato all'attaccante. Le attività di negoziazione sono state condotte da questo fornitore su incarico della società.

### 6. Attività in corso

Analisi dell'esfiltrazione per determinare l'esatto contenuto degli archivi copiati; monitoraggio delle piattaforme di pubblicazione; relazione definitiva prevista entro il 30 settembre 2031.

Il presente documento è riservato al destinatario. Firmato digitalmente dal responsabile del servizio di risposta agli incidenti.
