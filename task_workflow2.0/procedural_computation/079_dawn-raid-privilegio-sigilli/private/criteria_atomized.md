# WF2-079 - Criteri atomizzati

Ogni riga valuta un solo fatto, valore, collegamento probatorio, effetto o azione.

## A.1

- Tipo: struttura
- Issue: A
- Verifica: la consegna usa i file dawn_raid_timeline.md.
- Pass (insieme chiuso): i nomi dei file coincidono con dawn_raid_timeline.md | il controllo deterministico sul requisito restituisce esito positivo
- Fail: manca un file o il nome diverge
- Fonte: response_template.md

## A.2

- Tipo: struttura
- Issue: A
- Verifica: la consegna contiene le sezioni obbligatorie nell'ordine indicato.
- Pass (insieme chiuso): tutte le intestazioni compaiono nell'ordine del template | il controllo deterministico sul requisito restituisce esito positivo
- Fail: manca un'intestazione o l'ordine diverge
- Fonte: response_template.md

## A.3

- Tipo: struttura
- Issue: A
- Verifica: la parte testuale non supera 1.700 parole.
- Pass (insieme chiuso): il conteggio non supera 1.700 | il controllo deterministico sul requisito restituisce esito positivo
- Fail: il conteggio supera il limite
- Fonte: task_spec.json

## A.4

- Tipo: struttura
- Issue: A
- Verifica: ogni conclusione di merito indica almeno un documento o una fonte del reference pack.
- Pass (insieme chiuso): ogni conclusione reca una traccia documentale o normativa | il controllo deterministico sul requisito restituisce esito positivo
- Fail: una conclusione è priva di traccia
- Fonte: 02_reference_pack.md; documenti

## B.1

- Tipo: presenza
- Issue: I-01
- Verifica: il deliverable enuncia il risultato: gli ispettori hanno consegnato una decisione che indica prodotti e periodo 2026-2029.
- Pass (insieme chiuso): afferma: gli ispettori hanno consegnato una decisione che indica prodotti e periodo 2026-2029 | conclude: gli ispettori hanno consegnato una decisione che indica prodotti e periodo 2026-2029
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_decisione_ispettiva_e_verbale_accesso.pdf, contenuto pertinente a decisione; art. 20 Reg. 1/2003; decisione

## B.2

- Tipo: attribuzione
- Issue: I-01
- Verifica: il deliverable collega il dato al documento: decisione ispettiva ore 08:12.
- Pass (insieme chiuso): cita 01_decisione_ispettiva_e_verbale_accesso.pdf, contenuto pertinente a decisione | indica come riscontro 01_decisione_ispettiva_e_verbale_accesso.pdf, contenuto pertinente a decisione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_decisione_ispettiva_e_verbale_accesso.pdf, contenuto pertinente a decisione; art. 20 Reg. 1/2003; decisione

## B.3

- Tipo: qualificazione
- Issue: I-01
- Verifica: il deliverable espone l'effetto: le ricerche vanno confrontate con oggetto e finalità.
- Pass (insieme chiuso): espone l'effetto: le ricerche vanno confrontate con oggetto e finalità | indica come conseguenza: le ricerche vanno confrontate con oggetto e finalità
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_decisione_ispettiva_e_verbale_accesso.pdf, contenuto pertinente a decisione; art. 20 Reg. 1/2003; decisione

## B.4

- Tipo: valore
- Issue: I-02
- Verifica: il deliverable riporta il valore documentato per identificazione.
- Pass (insieme chiuso): compare «08:18» | compare «ore 8:18»
- Fail: non compare ne «08:18» ne «ore 8:18» oppure compare un valore incompatibile
- Fonte: 01_decisione_ispettiva_e_verbale_accesso.pdf, contenuto pertinente a identificazione; log; art. 20 Reg. 1/2003

## B.5

- Tipo: attribuzione
- Issue: I-02
- Verifica: il deliverable collega il dato al documento: log reception.
- Pass (insieme chiuso): cita 01_decisione_ispettiva_e_verbale_accesso.pdf, contenuto pertinente a identificazione | indica come riscontro 01_decisione_ispettiva_e_verbale_accesso.pdf, contenuto pertinente a identificazione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_decisione_ispettiva_e_verbale_accesso.pdf, contenuto pertinente a identificazione; log; art. 20 Reg. 1/2003

## B.6

- Tipo: qualificazione
- Issue: I-02
- Verifica: il deliverable espone l'effetto: il controllo iniziale risulta completato.
- Pass (insieme chiuso): espone l'effetto: il controllo iniziale risulta completato | indica come conseguenza: il controllo iniziale risulta completato
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_decisione_ispettiva_e_verbale_accesso.pdf, contenuto pertinente a identificazione; log; art. 20 Reg. 1/2003

## B.7

- Tipo: valore
- Issue: I-03
- Verifica: il deliverable riporta il valore documentato per preservazione.
- Pass (insieme chiuso): compare «08:26» | compare «ore 8:26»
- Fail: non compare ne «08:26» ne «ore 8:26» oppure compare un valore incompatibile
- Fonte: 01_decisione_ispettiva_e_verbale_accesso.pdf, contenuto pertinente a preservazione; ticket; decisione

## B.8

- Tipo: attribuzione
- Issue: I-03
- Verifica: il deliverable collega il dato al documento: ticket IT.
- Pass (insieme chiuso): cita 01_decisione_ispettiva_e_verbale_accesso.pdf, contenuto pertinente a preservazione | indica come riscontro 01_decisione_ispettiva_e_verbale_accesso.pdf, contenuto pertinente a preservazione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_decisione_ispettiva_e_verbale_accesso.pdf, contenuto pertinente a preservazione; ticket; decisione

## B.9

- Tipo: qualificazione
- Issue: I-03
- Verifica: il deliverable espone l'effetto: la misura riduce il rischio di alterazione.
- Pass (insieme chiuso): espone l'effetto: la misura riduce il rischio di alterazione | indica come conseguenza: la misura riduce il rischio di alterazione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_decisione_ispettiva_e_verbale_accesso.pdf, contenuto pertinente a preservazione; ticket; decisione

## B.10

- Tipo: valore
- Issue: I-04
- Verifica: il deliverable riporta il valore documentato per copia forense.
- Pass (insieme chiuso): compare «09:04» | compare «ore 9:04»
- Fail: non compare ne «09:04» ne «ore 9:04» oppure compare un valore incompatibile
- Fonte: 02_log_operazioni_e_privilege_log.xlsx, contenuto pertinente a copia forense; art. 20 Reg. 1/2003

## B.11

- Tipo: attribuzione
- Issue: I-04
- Verifica: il deliverable collega il dato al documento: verbale operazioni.
- Pass (insieme chiuso): cita 02_log_operazioni_e_privilege_log.xlsx, contenuto pertinente a copia forense | indica come riscontro 02_log_operazioni_e_privilege_log.xlsx, contenuto pertinente a copia forense
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_log_operazioni_e_privilege_log.xlsx, contenuto pertinente a copia forense; art. 20 Reg. 1/2003

## B.12

- Tipo: qualificazione
- Issue: I-04
- Verifica: il deliverable espone l'effetto: la copia rientra nei poteri di acquisizione se pertinente.
- Pass (insieme chiuso): espone l'effetto: la copia rientra nei poteri di acquisizione se pertinente | indica come conseguenza: la copia rientra nei poteri di acquisizione se pertinente
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_log_operazioni_e_privilege_log.xlsx, contenuto pertinente a copia forense; art. 20 Reg. 1/2003

## B.13

- Tipo: presenza
- Issue: I-05
- Verifica: il deliverable enuncia il risultato: il memorandum dello studio esterno è preparato per la difesa ed è marcato separatamente.
- Pass (insieme chiuso): afferma: il memorandum dello studio esterno è preparato per la difesa ed è marcato separatamente | conclude: il memorandum dello studio esterno è preparato per la difesa ed è marcato separatamente
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_log_operazioni_e_privilege_log.xlsx, contenuto pertinente a documento esterno; Akzo; privilege log

## B.14

- Tipo: attribuzione
- Issue: I-05
- Verifica: il deliverable collega il dato al documento: privilege log riga 4.
- Pass (insieme chiuso): cita 02_log_operazioni_e_privilege_log.xlsx, contenuto pertinente a documento esterno | indica come riscontro 02_log_operazioni_e_privilege_log.xlsx, contenuto pertinente a documento esterno
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_log_operazioni_e_privilege_log.xlsx, contenuto pertinente a documento esterno; Akzo; privilege log

## B.15

- Tipo: qualificazione
- Issue: I-05
- Verifica: il deliverable espone l'effetto: la rivendicazione deve essere documentata senza rivelare il merito.
- Pass (insieme chiuso): espone l'effetto: la rivendicazione deve essere documentata senza rivelare il merito | indica come conseguenza: la rivendicazione deve essere documentata senza rivelare il merito
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_log_operazioni_e_privilege_log.xlsx, contenuto pertinente a documento esterno; Akzo; privilege log

## B.16

- Tipo: presenza
- Issue: I-06
- Verifica: il deliverable enuncia il risultato: l'email del legale interno sul listino non beneficia automaticamente del privilegio UE.
- Pass (insieme chiuso): afferma: l'email del legale interno sul listino non beneficia automaticamente del privilegio UE | conclude: l'email del legale interno sul listino non beneficia automaticamente del privilegio UE
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_studio_ranieri_punto_giornata.eml, contenuto pertinente a legale interno; C-550/07 P Akzo

## B.17

- Tipo: attribuzione
- Issue: I-06
- Verifica: il deliverable collega il dato al documento: email riga 7 del log.
- Pass (insieme chiuso): cita 03_email_studio_ranieri_punto_giornata.eml, contenuto pertinente a legale interno | indica come riscontro 03_email_studio_ranieri_punto_giornata.eml, contenuto pertinente a legale interno
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_studio_ranieri_punto_giornata.eml, contenuto pertinente a legale interno; C-550/07 P Akzo

## B.18

- Tipo: qualificazione
- Issue: I-06
- Verifica: il deliverable espone l'effetto: lo status del mittente non basta nel procedimento unionale.
- Pass (insieme chiuso): espone l'effetto: lo status del mittente non basta nel procedimento unionale | indica come conseguenza: lo status del mittente non basta nel procedimento unionale
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_studio_ranieri_punto_giornata.eml, contenuto pertinente a legale interno; C-550/07 P Akzo

## B.19

- Tipo: valore
- Issue: I-07
- Verifica: il deliverable riporta il valore documentato per obiezione.
- Pass (insieme chiuso): compare «10:37» | compare «ore 10:37»
- Fail: non compare ne «10:37» ne «ore 10:37» oppure compare un valore incompatibile
- Fonte: 03_email_studio_ranieri_punto_giornata.eml, contenuto pertinente a obiezione; verbale

## B.20

- Tipo: attribuzione
- Issue: I-07
- Verifica: il deliverable collega il dato al documento: verbale ispettivo.
- Pass (insieme chiuso): cita 03_email_studio_ranieri_punto_giornata.eml, contenuto pertinente a obiezione | indica come riscontro 03_email_studio_ranieri_punto_giornata.eml, contenuto pertinente a obiezione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_studio_ranieri_punto_giornata.eml, contenuto pertinente a obiezione; verbale

## B.21

- Tipo: qualificazione
- Issue: I-07
- Verifica: il deliverable espone l'effetto: la traccia contemporanea preserva la posizione.
- Pass (insieme chiuso): espone l'effetto: la traccia contemporanea preserva la posizione | indica come conseguenza: la traccia contemporanea preserva la posizione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_studio_ranieri_punto_giornata.eml, contenuto pertinente a obiezione; verbale

## B.22

- Tipo: valore
- Issue: I-08
- Verifica: il deliverable riporta il valore documentato per intervista.
- Pass (insieme chiuso): compare «11:20» | compare «ore 11:20»
- Fail: non compare ne «11:20» ne «ore 11:20» oppure compare un valore incompatibile
- Fonte: 03_email_studio_ranieri_punto_giornata.eml, contenuto pertinente a intervista; art. 20 Reg. 1/2003

## B.23

- Tipo: attribuzione
- Issue: I-08
- Verifica: il deliverable collega il dato al documento: nota intervista.
- Pass (insieme chiuso): cita 03_email_studio_ranieri_punto_giornata.eml, contenuto pertinente a intervista | indica come riscontro 03_email_studio_ranieri_punto_giornata.eml, contenuto pertinente a intervista
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_studio_ranieri_punto_giornata.eml, contenuto pertinente a intervista; art. 20 Reg. 1/2003

## B.24

- Tipo: qualificazione
- Issue: I-08
- Verifica: il deliverable espone l'effetto: le risposte vanno rese veritiere e delimitate alla conoscenza personale.
- Pass (insieme chiuso): espone l'effetto: le risposte vanno rese veritiere e delimitate alla conoscenza personale | indica come conseguenza: le risposte vanno rese veritiere e delimitate alla conoscenza personale
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_studio_ranieri_punto_giornata.eml, contenuto pertinente a intervista; art. 20 Reg. 1/2003

## B.25

- Tipo: valore
- Issue: I-09
- Verifica: il deliverable riporta il valore documentato per sigillo.
- Pass (insieme chiuso): compare «19:05» | compare «ore 19:05»
- Fail: non compare ne «19:05» ne «ore 19:05» oppure compare un valore incompatibile
- Fonte: 04_nota_interna_sigilli_e_seguito.pdf, contenuto pertinente a sigillo; artt. 20 e 23 Reg. 1/2003

## B.26

- Tipo: attribuzione
- Issue: I-09
- Verifica: il deliverable collega il dato al documento: verbale di apposizione.
- Pass (insieme chiuso): cita 04_nota_interna_sigilli_e_seguito.pdf, contenuto pertinente a sigillo | indica come riscontro 04_nota_interna_sigilli_e_seguito.pdf, contenuto pertinente a sigillo
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_nota_interna_sigilli_e_seguito.pdf, contenuto pertinente a sigillo; artt. 20 e 23 Reg. 1/2003

## B.27

- Tipo: qualificazione
- Issue: I-09
- Verifica: il deliverable espone l'effetto: nessuno deve accedere o alterare il sigillo.
- Pass (insieme chiuso): espone l'effetto: nessuno deve accedere o alterare il sigillo | indica come conseguenza: nessuno deve accedere o alterare il sigillo
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_nota_interna_sigilli_e_seguito.pdf, contenuto pertinente a sigillo; artt. 20 e 23 Reg. 1/2003

## B.28

- Tipo: valore
- Issue: I-10
- Verifica: il deliverable riporta il valore documentato per follow-up.
- Pass (insieme chiuso): compare «29 gennaio 2030» | compare «2030-01-29»
- Fail: non compare ne «29 gennaio 2030» ne «2030-01-29» oppure compare un valore incompatibile
- Fonte: 04_nota_interna_sigilli_e_seguito.pdf, contenuto pertinente a follow-up; richiesta della Commissione

## B.29

- Tipo: attribuzione
- Issue: I-10
- Verifica: il deliverable collega il dato al documento: allegato al verbale.
- Pass (insieme chiuso): cita 04_nota_interna_sigilli_e_seguito.pdf, contenuto pertinente a follow-up | indica come riscontro 04_nota_interna_sigilli_e_seguito.pdf, contenuto pertinente a follow-up
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_nota_interna_sigilli_e_seguito.pdf, contenuto pertinente a follow-up; richiesta della Commissione

## C.1

- Tipo: assenza
- Issue: N-01
- Verifica: chiusura simmetria sul falso positivo «attesa legale»: L'arrivo del legale esterno non è una condizione generale per consentire l'accesso ispettivo.
- Pass (insieme chiuso): non qualifica come criticita attesa legale | esclude espressamente il falso positivo attesa legale
- Fail: compare la conclusione vietata «attesa legale costituisce una criticita autonoma»
- Fonte: challenge_map.json; documenti pubblici

## C.2

- Tipo: assenza
- Issue: N-02
- Verifica: chiusura sovra-segnalazione sul falso positivo «formato elettronico»: Il formato elettronico non sottrae i documenti pertinenti ai poteri di copia.
- Pass (insieme chiuso): non qualifica come criticita formato elettronico | esclude espressamente il falso positivo formato elettronico
- Fail: compare la conclusione vietata «formato elettronico costituisce una criticita autonoma»
- Fonte: challenge_map.json; documenti pubblici

## C.3

- Tipo: assenza
- Issue: N-03
- Verifica: chiusura presunzione sul falso positivo «testimone sigillo»: La presenza di un testimone interno non autorizza l'apertura di un locale sigillato.
- Pass (insieme chiuso): non qualifica come criticita testimone sigillo | esclude espressamente il falso positivo testimone sigillo
- Fail: compare la conclusione vietata «testimone sigillo costituisce una criticita autonoma»
- Fonte: challenge_map.json; documenti pubblici
