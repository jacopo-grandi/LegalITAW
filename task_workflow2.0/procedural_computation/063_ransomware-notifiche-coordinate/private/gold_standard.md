# WF2-063 - Gold standard

**Deliverable atteso:** incident_master_timeline.md.

## Testo sostanziale del deliverable

### Decisione immediata

Alla data di riferimento il fascicolo richiede le decisioni indicate sotto. Sono stati esaminati doc. 01, doc. 02, doc. 03, doc. 04, doc. 05, doc. 06, doc. 07, doc. 08, doc. 09, doc. 10; fatti, inferenze e lacune restano distinti.

- **I-16 - registro unico dei fatti, decisioni separate.** I medesimi fatti alimentano cinque flussi ma i test giuridici non coincidono. Documento: tutti i documenti. Azione: mantenere fonte fattuale unica con decisioni e versioni per destinatario. Conseguenza: coordinamento non significa fusione.

### Cronologia verificata

- **I-01 - momento di conoscenza del titolare.** Il dies a quo di saliceto e' il 16 febbraio alle 08:20, non il primo alert delle 06:42. Documento: doc. 01. Azione: ancorare tutti i termini del titolare alle 08:20. Conseguenza: il dies a quo dei termini di notifica e' il 16 febbraio 2027 alle 08:20.
- **I-02 - obbligo del responsabile.** Kairone doveva informare senza ritardo e comunque entro il limite contrattuale. Documento: doc. 02. Azione: registrare 05:55 e 07:48 come eventi distinti. Conseguenza: il termine del responsabile non sostituisce quello del titolare.

### Scadenze distinte

- **I-03 - pre-notifica NIS entro 24 ore.** La scadenza e' 17 febbraio 2027 alle 08:20. Documento: doc. 01 e doc. 04. Azione: inviare pre-notifica ACN con natura dolosa e possibile impatto. Conseguenza: il primo adempimento NIS precede la notifica completa.
- **I-04 - notifica NIS entro 72 ore.** La scadenza e' 19 febbraio 2027 alle 08:20. Documento: doc. 01 e fonti. Azione: trasmettere valutazione iniziale, gravita' e indicatori disponibili. Conseguenza: il secondo adempimento resta distinto dalla pre-notifica.
- **I-05 - relazione finale NIS.** La relazione finale va calendarizzata a un mese dalla notifica completa, con aggiornamenti se l'incidente perdura. Documento: fonti e registro evento. Azione: fissare presidio al 19 marzo 2027 e verificare lo stato. Conseguenza: la chiusura tecnica non cancella l'obbligo.
- **I-06 - notifica GDPR entro 72 ore.** La scadenza e' 19 febbraio 2027 alle 08:20 e il rischio non e' improbabile. Documento: doc. 01, doc. 03 e GDPR. Azione: notificare il Garante anche per fasi se mancano dettagli. Conseguenza: la notifica privacy ha destinatario e test diversi dalla NIS.
- **I-08 - avviso all'assicuratore.** Le 48 ore scadono il 18 febbraio 2027 alle 08:20. Documento: doc. 05. Azione: inviare avviso cautelativo e chiedere consenso alle spese non urgenti. Conseguenza: il termine di polizza e' autonomo.
- **I-09 - avviso al cliente Cerasia.** Le 24 ore scadono il 17 febbraio 2027 alle 08:20. Documento: doc. 06. Azione: inviare avviso contrattuale e aggiornamenti giornalieri. Conseguenza: il cliente non coincide con gli interessati.

### Dipendenze

- **I-10 - runbook con termini fusi.** La regola unica delle 72 ore omette nis 24h, polizza 48h e cliente 24h. Documento: doc. 07. Azione: sostituire la riga unica con scadenze e owner separati. Conseguenza: la semplificazione produce ritardi.
- **I-15 - riscatto non sospensivo.** La scadenza imposta dall'attaccante non sospende notifiche. Documento: doc. 10. Azione: procedere con gli adempimenti senza attendere il 18 febbraio. Conseguenza: la decisione sul pagamento resta separata.

### Contenuto delle comunicazioni

- **I-07 - comunicazione agli interessati.** Dati sanitari ed esfiltrazione sostengono un rischio elevato. Documento: doc. 03, doc. 08 e doc. 09. Azione: comunicare senza ingiustificato ritardo con natura, conseguenze, misure e contatto. Conseguenza: non esiste un termine fisso di 72 ore per l'art. 34.
- **I-12 - bozza interessati incompleta.** La bozza omette l'esfiltrazione e il recapito. Documento: doc. 09. Azione: correggere contenuto prima dell'invio. Conseguenza: un testo rassicurante ma incompleto non soddisfa il dovere informativo.

### Registro delle incertezze

- **I-13 - notifica per fasi.** L'incertezza sulla composizione dei 62 gb non giustifica attendere. Documento: doc. 08 e GDPR. Azione: inviare dati disponibili e integrare senza ritardo. Conseguenza: la completezza finale non e' condizione iniziale.
- **I-17 - lacuna sull'estensione.** Non e' noto quali record compongano tutti i 62 gb. Documento: doc. 08. Azione: aprire workstream forense con checkpoint alle 18:00. Conseguenza: non quantificare definitivamente prima della verifica.

### Owner e prove

- **I-11 - owner NIS errato.** Il punto di contatto nis e' direzione sicurezza, non dpo. Documento: doc. 04 e doc. 07. Azione: assegnare approvazione aziendale e invio al punto registrato. Conseguenza: il DPO resta consultato sul flusso privacy.
- **I-14 - conservazione probatoria.** Immagini, log e indicatori devono restare integri mentre si ripristina. Documento: doc. 08 e doc. 10. Azione: preservare copie, catena di custodia e decision log. Conseguenza: ripristino e prova hanno owner coordinati.

### Prossimo aggiornamento

Nessun ulteriore punto autonomo; valgono le azioni e le lacune gia' documentate nelle sezioni precedenti.

## Note private di controllo (non fanno parte del deliverable)

Controlled non-issue verificati come assenze:

- N-01 - primo alert non qualificato: non e' elencato come rischio o criticita'; la mera menzione fattuale resta ammessa.
- N-02 - backup clinici integri: non e' elencato come rischio o criticita'; la mera menzione fattuale resta ammessa.
- N-03 - scadenza del riscatto: non e' elencato come rischio o criticita'; la mera menzione fattuale resta ammessa.
- N-04 - festivita' e fine settimana: non e' elencato come rischio o criticita'; la mera menzione fattuale resta ammessa.
- N-05 - DPO consultato: non e' elencato come rischio o criticita'; la mera menzione fattuale resta ammessa.

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
| B.1 | PASS | nel deliverable compare «il dies a quo di Saliceto e' il 16 febbraio alle 08:20, non il primo alert delle 06:42» |
| B.2 | PASS | la proposizione compare in una frase autonoma: Kairone doveva informare senza ritardo e comunque entro il limite contrattuale |
| B.3 | PASS | nel deliverable compare «la scadenza e' 17 febbraio 2027 alle 08:20» |
| B.4 | PASS | nel deliverable compare «la scadenza e' 19 febbraio 2027 alle 08:20» |
| B.5 | PASS | nel deliverable compare «la relazione finale va calendarizzata a un mese dalla notifica completa, con aggiornamenti se l'incidente perdura» |
| B.6 | PASS | nel deliverable compare «la scadenza e' 19 febbraio 2027 alle 08:20 e il rischio non e' improbabile» |
| B.7 | PASS | la proposizione compare in una frase autonoma: dati sanitari ed esfiltrazione sostengono un rischio elevato |
| B.8 | PASS | nel deliverable compare «le 48 ore scadono il 18 febbraio 2027 alle 08:20» |
| B.9 | PASS | nel deliverable compare «le 24 ore scadono il 17 febbraio 2027 alle 08:20» |
| B.10 | PASS | nel deliverable compare «la regola unica delle 72 ore omette NIS 24h, polizza 48h e cliente 24h» |
| B.11 | PASS | la proposizione compare in una frase autonoma: il punto di contatto NIS e' direzione sicurezza, non DPO |
| B.12 | PASS | la proposizione compare in una frase autonoma: la bozza omette l'esfiltrazione e il recapito |
| B.13 | PASS | la proposizione compare in una frase autonoma: l'incertezza sulla composizione dei 62 GB non giustifica attendere |
| B.14 | PASS | la proposizione compare in una frase autonoma: immagini, log e indicatori devono restare integri mentre si ripristina |
| B.15 | PASS | la proposizione compare in una frase autonoma: la scadenza imposta dall'attaccante non sospende notifiche |
| B.16 | PASS | la proposizione compare in una frase autonoma: i medesimi fatti alimentano cinque flussi ma i test giuridici non coincidono |
| B.17 | PASS | la proposizione compare in una frase autonoma: non e' noto quali record compongano tutti i 62 GB |
| B.18 | PASS | la stessa frase, riga di tabella o nota collega il punto a doc. 01 |
| B.19 | PASS | la stessa frase, riga di tabella o nota collega il punto a doc. 02 |
| B.20 | PASS | la stessa frase, riga di tabella o nota collega il punto a doc. 01 e doc. 04 |
| B.21 | PASS | la stessa frase, riga di tabella o nota collega il punto a doc. 01 e fonti |
| B.22 | PASS | la stessa frase, riga di tabella o nota collega il punto a fonti e registro evento |
| B.23 | PASS | la stessa frase, riga di tabella o nota collega il punto a doc. 01, doc. 03 e GDPR |
| B.24 | PASS | la stessa frase, riga di tabella o nota collega il punto a doc. 03, doc. 08 e doc. 09 |
| B.25 | PASS | la stessa frase, riga di tabella o nota collega il punto a doc. 05 |
| B.26 | PASS | la stessa frase, riga di tabella o nota collega il punto a doc. 06 |
| B.27 | PASS | la stessa frase, riga di tabella o nota collega il punto a doc. 07 |
| B.28 | PASS | la stessa frase, riga di tabella o nota collega il punto a doc. 04 e doc. 07 |
| B.29 | PASS | la stessa frase, riga di tabella o nota collega il punto a doc. 09 |
| B.30 | PASS | la stessa frase, riga di tabella o nota collega il punto a doc. 08 e GDPR |
| B.31 | PASS | la stessa frase, riga di tabella o nota collega il punto a doc. 08 e doc. 10 |
| B.32 | PASS | la stessa frase, riga di tabella o nota collega il punto a doc. 10 |
| B.33 | PASS | la stessa frase, riga di tabella o nota collega il punto a tutti i documenti |
| B.34 | PASS | la stessa frase, riga di tabella o nota collega il punto a doc. 08 |
| B.35 | PASS | l'azione e' formulata come richiesta: ancorare tutti i termini del titolare alle 08:20 |
| B.36 | PASS | l'azione e' formulata come richiesta: registrare 05:55 e 07:48 come eventi distinti |
| B.37 | PASS | l'azione e' formulata come richiesta: inviare pre-notifica ACN con natura dolosa e possibile impatto |
| B.38 | PASS | l'azione e' formulata come richiesta: trasmettere valutazione iniziale, gravita' e indicatori disponibili |
| B.39 | PASS | l'azione e' formulata come richiesta: fissare presidio al 19 marzo 2027 e verificare lo stato |
| B.40 | PASS | l'azione e' formulata come richiesta: notificare il Garante anche per fasi se mancano dettagli |
| B.41 | PASS | l'azione e' formulata come richiesta: comunicare senza ingiustificato ritardo con natura, conseguenze, misure e contatto |
| B.42 | PASS | l'azione e' formulata come richiesta: inviare avviso cautelativo e chiedere consenso alle spese non urgenti |
| B.43 | PASS | l'azione e' formulata come richiesta: inviare avviso contrattuale e aggiornamenti giornalieri |
| B.44 | PASS | l'azione e' formulata come richiesta: sostituire la riga unica con scadenze e owner separati |
| B.45 | PASS | l'azione e' formulata come richiesta: assegnare approvazione aziendale e invio al punto registrato |
| B.46 | PASS | l'azione e' formulata come richiesta: correggere contenuto prima dell'invio |
| B.47 | PASS | l'azione e' formulata come richiesta: inviare dati disponibili e integrare senza ritardo |
| B.48 | PASS | l'azione e' formulata come richiesta: preservare copie, catena di custodia e decision log |
| B.49 | PASS | l'azione e' formulata come richiesta: procedere con gli adempimenti senza attendere il 18 febbraio |
| B.50 | PASS | l'azione e' formulata come richiesta: mantenere fonte fattuale unica con decisioni e versioni per destinatario |
| B.51 | PASS | l'azione e' formulata come richiesta: aprire workstream forense con checkpoint alle 18:00 |
| B.52 | PASS | la conseguenza e' espressa nel testo: il dies a quo dei termini di notifica e' il 16 febbraio 2027 alle 08:20 |
| B.53 | PASS | la conseguenza e' espressa nel testo: il termine del responsabile non sostituisce quello del titolare |
| B.54 | PASS | la conseguenza e' espressa nel testo: il primo adempimento NIS precede la notifica completa |
| B.55 | PASS | la conseguenza e' espressa nel testo: il secondo adempimento resta distinto dalla pre-notifica |
| B.56 | PASS | la conseguenza e' espressa nel testo: la chiusura tecnica non cancella l'obbligo |
| B.57 | PASS | la conseguenza e' espressa nel testo: la notifica privacy ha destinatario e test diversi dalla NIS |
| B.58 | PASS | la conseguenza e' espressa nel testo: non esiste un termine fisso di 72 ore per l'art. 34 |
| B.59 | PASS | sovra-segnalazione - primo alert non qualificato non e' presentato come rischio, criticita', inadempimento o conclusione negativa |
| B.60 | PASS | sovra-segnalazione - backup clinici integri non e' presentato come rischio, criticita', inadempimento o conclusione negativa |
| B.61 | PASS | sovra-segnalazione - scadenza del riscatto non e' presentato come rischio, criticita', inadempimento o conclusione negativa |
| B.62 | PASS | sovra-segnalazione - festivita' e fine settimana non e' presentato come rischio, criticita', inadempimento o conclusione negativa |
| B.63 | PASS | sovra-segnalazione - DPO consultato non e' presentato come rischio, criticita', inadempimento o conclusione negativa |
| B.64 | PASS | simmetria del controllo non e' presentato come rischio, criticita', inadempimento o conclusione negativa |
| B.65 | PASS | presunzione dell'esito non e' presentato come rischio, criticita', inadempimento o conclusione negativa |
