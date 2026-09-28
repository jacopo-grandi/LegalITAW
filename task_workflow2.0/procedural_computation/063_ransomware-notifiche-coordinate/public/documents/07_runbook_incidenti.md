# Runbook IR-04 — Gestione degli incidenti di sicurezza

**Documento interno — SAL/SEC/IR-04 rev. 3 — pubblicato il 10 gennaio 2027**
Proprietario del documento: Direzione sicurezza delle informazioni
Approvazione rev. 3: comitato sicurezza dell'8 gennaio 2027, verbale CS/2027/01
Destinatari: turno SOC, Direzione sicurezza, Affari legali, Responsabile della protezione dei dati, Direzione comunicazione, referenti di reparto
Revisione successiva prevista: gennaio 2028

## 1. Scopo e ambito

Il presente runbook descrive le attività da svolgere quando un evento di sicurezza sui sistemi del gruppo viene classificato come incidente. Si applica a tutti gli ambienti di produzione, compresi quelli amministrati da fornitori. Non sostituisce le procedure di continuità operativa (BC-02) né il piano di disaster recovery (DR-01), ai quali rinvia per il ripristino dei servizi essenziali.

## 2. Ruoli

| Ruolo | Funzione | Attività principali |
|---|---|---|
| Turno SOC | Direzione sicurezza | rilevazione, triage, prima informativa, aggiornamenti tecnici |
| Incident manager | Direzione sicurezza | coordinamento del contenimento e delle attività forensi, cabina di regia |
| Affari legali | funzione consultata | supporto sui profili contrattuali e sui rapporti con le autorità |
| Responsabile della protezione dei dati | funzione consultata e responsabile delle notifiche | valutazione dei profili privacy, approvazione e invio delle notifiche |
| Direzione comunicazione | funzione consultata | predisposizione dei testi verso l'esterno |
| Referente di reparto | struttura interessata | rilevazione dell'impatto clinico e organizzativo |

## 3. Classificazione

| Severità | Presupposto | Escalation |
|---|---|---|
| S3 — bassa | evento circoscritto, nessun impatto sui servizi | gestione a cura del turno |
| S2 — media | impatto su un servizio non clinico o su un singolo reparto | incident manager entro 1 ora |
| S1 — alta | impatto su servizi clinici, sospetto accesso non autorizzato a dati, cifratura di sistemi | incident manager immediato, cabina di regia entro 2 ore, informativa alla Direzione generale |

## 4. Fasi operative

### 4.1 Rilevazione e triage

Il turno verifica l'allarme, esclude le attività pianificate consultando il calendario cambi, raccoglie i primi indicatori e apre l'evento nel registro degli eventi di sicurezza. Ogni evento riceve un identificativo nella forma IR-AA-MMGG e mantiene quell'identificativo per tutta la gestione, compresi gli aggiornamenti successivi alla chiusura tecnica.

### 4.2 Qualificazione

L'incident manager qualifica l'evento come incidente quando gli elementi raccolti consentono un giudizio ragionevolmente fondato sull'accaduto. L'ora della qualificazione è annotata nel registro insieme al nome di chi l'ha effettuata.

### 4.3 Contenimento

Isolamento dei sistemi interessati, revoca e rotazione delle credenziali privilegiate, blocco delle destinazioni ostili, sospensione delle integrazioni con i fornitori. Il contenimento ha precedenza sull'analisi, salvo che l'attività di contenimento comporti la perdita di elementi non altrimenti recuperabili: in tal caso l'incident manager dispone la preventiva acquisizione delle copie.

### 4.4 Analisi e attività forensi

L'incident manager attiva il fornitore forense accreditato e ne coordina le attività con quelle di ripristino. Le acquisizioni sono registrate nella catena di custodia. Le immagini dei sistemi, gli hash e i log sono conservati sul volume di raccolta e non sono modificati.

### 4.5 Ripristino

Il ripristino segue il piano DR-01, previa verifica dell'integrità dei punti di ripristino e conferma dell'avvenuto contenimento. Il rientro in produzione è autorizzato dall'incident manager sentiti i referenti di reparto; per i servizi clinici l'autorizzazione è sempre scritta.

### 4.6 Chiusura e lezioni apprese

L'evento è chiuso quando i servizi sono ripristinati e le attività di analisi sono concluse. Entro trenta giorni dalla chiusura si tiene la riunione di lezioni apprese e si aggiorna il registro.

## 5. Notifiche

| Adempimento | Termine | Approvazione | Invio |
|---|---|---|---|
| Notifiche esterne relative all'incidente | entro 72 ore dalla qualificazione dell'incidente | Responsabile della protezione dei dati | Responsabile della protezione dei dati |

Il Responsabile della protezione dei dati approva e trasmette sia la notifica all'autorità di protezione dei dati sia la comunicazione all'Agenzia per la cybersicurezza nazionale, utilizzando i canali previsti per ciascun destinatario. Affari legali e Direzione comunicazione forniscono i contributi di competenza entro dodici ore dalla richiesta. La Direzione sicurezza mette a disposizione gli elementi tecnici e i dati dell'evento.

Prima dell'invio, il testo è condiviso in cabina di regia con Direzione sicurezza, Affari legali e Direzione generale. Copia di ogni comunicazione trasmessa è conservata nel registro degli eventi di sicurezza insieme alla ricevuta.

## 6. Checklist del turno per gli eventi S1

- [ ] Evento aperto nel registro con identificativo e ora di rilevazione
- [ ] Attività pianificate escluse tramite calendario cambi
- [ ] Incident manager allertato e cabina di regia convocata
- [ ] Prima informativa scritta emessa e distribuita
- [ ] Ora di qualificazione annotata nel registro
- [ ] Credenziali privilegiate revocate e ruotate
- [ ] Destinazioni ostili bloccate in uscita
- [ ] Fornitore forense attivato
- [ ] Copie acquisite prima di ogni intervento distruttivo
- [ ] Responsabile della protezione dei dati informato per gli adempimenti di cui al § 5
- [ ] Aggiornamenti periodici trasmessi ai destinatari della prima informativa

## 7. Recapiti operativi

Turno SOC: int. 4400 — soc@saliceto.example
Incident manager di guardia: +39 051 4400118
Responsabile della protezione dei dati: dpo@saliceto.example
Affari legali: legale@saliceto.example
Fornitore forense accreditato: Ostiglia Digital Forensics S.r.l., pronto intervento 800 552 118
Fornitore di gestione infrastrutturale: Kairone S.r.l., service desk 24/7

## 8. Storico delle revisioni

| Rev. | Data | Modifiche | Approvazione |
|---|---|---|---|
| 1 | 14 marzo 2025 | prima emissione | CS/2025/03 |
| 2 | 22 giugno 2026 | inserimento della fase forense e della catena di custodia; aggiornamento recapiti | CS/2026/05 |
| 3 | 10 gennaio 2027 | semplificazione del capitolo notifiche: le scadenze precedentemente distinte per destinatario sono state ricondotte a un'unica soglia e a un unico responsabile, su richiesta del turno che segnalava difficoltà di applicazione; aggiornamento della tabella dei ruoli | CS/2027/01 |
