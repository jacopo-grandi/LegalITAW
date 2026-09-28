# WF2-072 - Criteri atomizzati

Ogni riga valuta un solo fatto, valore, collegamento probatorio, effetto o azione.

## A.1

- Tipo: struttura
- Issue: A
- Verifica: la consegna usa i file employment_deadline_audit.md.
- Pass (insieme chiuso): i nomi dei file coincidono con employment_deadline_audit.md | il controllo deterministico sul requisito restituisce esito positivo
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

- Tipo: valore
- Issue: I-01
- Verifica: il deliverable riporta il valore documentato per conoscenza del fatto.
- Pass (insieme chiuso): compare «2 maggio 2029» | compare «2029-05-02»
- Fail: non compare ne «2 maggio 2029» ne «2029-05-02» oppure compare un valore incompatibile
- Fonte: 01_atti_procedimento_varisco.pdf, contenuto pertinente a conoscenza del fatto; rapporto audit

## B.2

- Tipo: attribuzione
- Issue: I-01
- Verifica: il deliverable collega il dato al documento: rapporto audit chiuso il 2 maggio.
- Pass (insieme chiuso): cita 01_atti_procedimento_varisco.pdf, contenuto pertinente a conoscenza del fatto | indica come riscontro 01_atti_procedimento_varisco.pdf, contenuto pertinente a conoscenza del fatto
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_atti_procedimento_varisco.pdf, contenuto pertinente a conoscenza del fatto; rapporto audit

## B.3

- Tipo: qualificazione
- Issue: I-01
- Verifica: il deliverable espone l'effetto: l'immediatezza si valuta da questa data e non dal fatto del 29 aprile.
- Pass (insieme chiuso): espone l'effetto: l'immediatezza va verificata dal completamento dell'audit, non dal solo fatto del 27 aprile | indica come conseguenza: l'immediatezza va verificata dal completamento dell'audit, non dal solo fatto del 27 aprile
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_atti_procedimento_varisco.pdf, contenuto pertinente a conoscenza del fatto; rapporto audit

## B.4

- Tipo: presenza
- Issue: I-02
- Verifica: il deliverable enuncia il risultato: la lettera del 3 maggio indica operazione, ora, cliente e regola contestata.
- Pass (insieme chiuso): afferma: la lettera del 3 maggio indica operazione, ora, cliente e regola contestata | conclude: la lettera del 3 maggio indica operazione, ora, cliente e regola contestata
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_atti_procedimento_varisco.pdf, contenuto pertinente a specificità; lettera di contestazione

## B.5

- Tipo: attribuzione
- Issue: I-02
- Verifica: il deliverable collega il dato al documento: contestazione consegnata il 3 maggio.
- Pass (insieme chiuso): cita 01_atti_procedimento_varisco.pdf, contenuto pertinente a specificità | indica come riscontro 01_atti_procedimento_varisco.pdf, contenuto pertinente a specificità
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_atti_procedimento_varisco.pdf, contenuto pertinente a specificità; lettera di contestazione

## B.6

- Tipo: qualificazione
- Issue: I-02
- Verifica: il deliverable espone l'effetto: l'addebito è individuato nei suoi elementi materiali.
- Pass (insieme chiuso): espone l'effetto: l'addebito è individuato nei suoi elementi materiali | indica come conseguenza: l'addebito è individuato nei suoi elementi materiali
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_atti_procedimento_varisco.pdf, contenuto pertinente a specificità; lettera di contestazione

## B.7

- Tipo: presenza
- Issue: I-03
- Verifica: il deliverable enuncia il risultato: il codice disciplinare risulta affisso dal 4 gennaio 2028.
- Pass (insieme chiuso): afferma: il codice disciplinare risulta affisso dal 4 gennaio 2028 | conclude: il codice disciplinare risulta affisso dal 4 gennaio 2028
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_atti_procedimento_varisco.pdf, contenuto pertinente a pubblicità del codice; art. 7 legge 300/1970; verbale

## B.8

- Tipo: attribuzione
- Issue: I-03
- Verifica: il deliverable collega il dato al documento: verbale di affissione.
- Pass (insieme chiuso): cita 01_atti_procedimento_varisco.pdf, contenuto pertinente a pubblicità del codice | indica come riscontro 01_atti_procedimento_varisco.pdf, contenuto pertinente a pubblicità del codice
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_atti_procedimento_varisco.pdf, contenuto pertinente a pubblicità del codice; art. 7 legge 300/1970; verbale

## B.9

- Tipo: qualificazione
- Issue: I-03
- Verifica: il deliverable espone l'effetto: il fascicolo prova la conoscibilità delle regole aziendali.
- Pass (insieme chiuso): espone l'effetto: il fascicolo prova la conoscibilità delle regole aziendali | indica come conseguenza: il fascicolo prova la conoscibilità delle regole aziendali
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_atti_procedimento_varisco.pdf, contenuto pertinente a pubblicità del codice; art. 7 legge 300/1970; verbale

## B.10

- Tipo: valore
- Issue: I-04
- Verifica: il deliverable riporta il valore documentato per termine difensivo.
- Pass (insieme chiuso): compare «11 maggio 2029» | compare «2029-05-11»
- Fail: non compare ne «11 maggio 2029» ne «2029-05-11» oppure compare un valore incompatibile
- Fonte: 02_registro_procedimento_varisco.xlsx, contenuto pertinente a termine difensivo; art. 7 legge 300/1970

## B.11

- Tipo: attribuzione
- Issue: I-04
- Verifica: il deliverable collega il dato al documento: contestazione del 3 maggio e licenziamento del 13 maggio.
- Pass (insieme chiuso): cita 02_registro_procedimento_varisco.xlsx, contenuto pertinente a termine difensivo | indica come riscontro 02_registro_procedimento_varisco.xlsx, contenuto pertinente a termine difensivo
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_procedimento_varisco.xlsx, contenuto pertinente a termine difensivo; art. 7 legge 300/1970

## B.12

- Tipo: qualificazione
- Issue: I-04
- Verifica: il deliverable espone l'effetto: la decisione non è prematura per il solo decorso temporale.
- Pass (insieme chiuso): espone l'effetto: la decisione non e prematura per il solo intervallo temporale | indica come conseguenza: la decisione non e prematura per il solo intervallo temporale
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_procedimento_varisco.xlsx, contenuto pertinente a termine difensivo; art. 7 legge 300/1970

## B.13

- Tipo: valore
- Issue: I-05
- Verifica: il deliverable riporta il valore documentato per difese scritte.
- Pass (insieme chiuso): compare «7 maggio 2029» | compare «2029-05-07»
- Fail: non compare ne «7 maggio 2029» ne «2029-05-07» oppure compare un valore incompatibile
- Fonte: 02_registro_procedimento_varisco.xlsx, contenuto pertinente a difese scritte; PEC del 7 maggio

## B.14

- Tipo: attribuzione
- Issue: I-05
- Verifica: il deliverable collega il dato al documento: PEC della lavoratrice.
- Pass (insieme chiuso): cita 02_registro_procedimento_varisco.xlsx, contenuto pertinente a difese scritte | indica come riscontro 02_registro_procedimento_varisco.xlsx, contenuto pertinente a difese scritte
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_procedimento_varisco.xlsx, contenuto pertinente a difese scritte; PEC del 7 maggio

## B.15

- Tipo: qualificazione
- Issue: I-05
- Verifica: il deliverable espone l'effetto: devono essere valutate nella motivazione.
- Pass (insieme chiuso): espone l'effetto: devono essere valutate nella motivazione | indica come conseguenza: devono essere valutate nella motivazione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_procedimento_varisco.xlsx, contenuto pertinente a difese scritte; PEC del 7 maggio

## B.16

- Tipo: valore
- Issue: I-06
- Verifica: il deliverable riporta il valore documentato per audizione.
- Pass (insieme chiuso): compare «10 maggio 2029» | compare «2029-05-10»
- Fail: non compare ne «10 maggio 2029» ne «2029-05-10» oppure compare un valore incompatibile
- Fonte: 03_scambi_audizione_e_recesso.eml, contenuto pertinente a audizione; verbale di audizione

## B.17

- Tipo: attribuzione
- Issue: I-06
- Verifica: il deliverable collega il dato al documento: verbale di audizione.
- Pass (insieme chiuso): cita 03_scambi_audizione_e_recesso.eml, contenuto pertinente a audizione | indica come riscontro 03_scambi_audizione_e_recesso.eml, contenuto pertinente a audizione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_scambi_audizione_e_recesso.eml, contenuto pertinente a audizione; verbale di audizione

## B.18

- Tipo: qualificazione
- Issue: I-06
- Verifica: il deliverable espone l'effetto: il passaggio difensivo richiesto risulta eseguito.
- Pass (insieme chiuso): espone l'effetto: il passaggio difensivo richiesto risulta eseguito | indica come conseguenza: il passaggio difensivo richiesto risulta eseguito
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_scambi_audizione_e_recesso.eml, contenuto pertinente a audizione; verbale di audizione

## B.19

- Tipo: presenza
- Issue: I-07
- Verifica: il deliverable enuncia il risultato: la lettera di licenziamento usa gli stessi fatti della contestazione.
- Pass (insieme chiuso): afferma: la lettera di licenziamento usa gli stessi fatti della contestazione | conclude: la lettera di licenziamento usa gli stessi fatti della contestazione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_scambi_audizione_e_recesso.eml, contenuto pertinente a decisione; lettere del 3 e 13 maggio

## B.20

- Tipo: attribuzione
- Issue: I-07
- Verifica: il deliverable collega il dato al documento: raffronto fra lettere.
- Pass (insieme chiuso): cita 03_scambi_audizione_e_recesso.eml, contenuto pertinente a decisione | indica come riscontro 03_scambi_audizione_e_recesso.eml, contenuto pertinente a decisione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_scambi_audizione_e_recesso.eml, contenuto pertinente a decisione; lettere del 3 e 13 maggio

## B.21

- Tipo: qualificazione
- Issue: I-07
- Verifica: il deliverable espone l'effetto: non emerge una mutazione dell'addebito.
- Pass (insieme chiuso): espone l'effetto: non emerge una mutazione dell'addebito | indica come conseguenza: non emerge una mutazione dell'addebito
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_scambi_audizione_e_recesso.eml, contenuto pertinente a decisione; lettere del 3 e 13 maggio

## B.22

- Tipo: valore
- Issue: I-08
- Verifica: il deliverable riporta il valore documentato per ricezione.
- Pass (insieme chiuso): compare «11 maggio 2029» | compare «2029-05-11»
- Fail: non compare ne «11 maggio 2029» ne «2029-05-11» oppure compare un valore incompatibile
- Fonte: 03_scambi_audizione_e_recesso.eml, contenuto pertinente a ricezione; ricevuta; art. 6 legge 604/1966

## B.23

- Tipo: attribuzione
- Issue: I-08
- Verifica: il deliverable collega il dato al documento: ricevuta di consegna.
- Pass (insieme chiuso): cita 03_scambi_audizione_e_recesso.eml, contenuto pertinente a ricezione | indica come riscontro 03_scambi_audizione_e_recesso.eml, contenuto pertinente a ricezione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_scambi_audizione_e_recesso.eml, contenuto pertinente a ricezione; ricevuta; art. 6 legge 604/1966

## B.24

- Tipo: qualificazione
- Issue: I-08
- Verifica: il deliverable espone l'effetto: da questa data decorre il termine di impugnazione.
- Pass (insieme chiuso): espone l'effetto: da questa data decorre il termine di impugnazione | indica come conseguenza: da questa data decorre il termine di impugnazione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_scambi_audizione_e_recesso.eml, contenuto pertinente a ricezione; ricevuta; art. 6 legge 604/1966

## B.25

- Tipo: valore
- Issue: I-09
- Verifica: il deliverable riporta il valore documentato per prima decadenza.
- Pass (insieme chiuso): compare «10 luglio 2029» | compare «2029-07-10»
- Fail: non compare ne «10 luglio 2029» ne «2029-07-10» oppure compare un valore incompatibile
- Fonte: 04_nota_studio_termini_impugnazione.pdf, contenuto pertinente a prima decadenza; art. 6 legge 604/1966

## B.26

- Tipo: attribuzione
- Issue: I-09
- Verifica: il deliverable collega il dato al documento: ricezione del 13 maggio 2029.
- Pass (insieme chiuso): cita 04_nota_studio_termini_impugnazione.pdf, contenuto pertinente a prima decadenza | indica come riscontro 04_nota_studio_termini_impugnazione.pdf, contenuto pertinente a prima decadenza
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_nota_studio_termini_impugnazione.pdf, contenuto pertinente a prima decadenza; art. 6 legge 604/1966

## B.27

- Tipo: qualificazione
- Issue: I-09
- Verifica: il deliverable espone l'effetto: l'impugnazione stragiudiziale deve pervenire entro quella data.
- Pass (insieme chiuso): espone l'effetto: l'impugnazione stragiudiziale deve pervenire entro il 10 luglio 2029 | indica come conseguenza: l'impugnazione stragiudiziale deve pervenire entro il 10 luglio 2029
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_nota_studio_termini_impugnazione.pdf, contenuto pertinente a prima decadenza; art. 6 legge 604/1966

## B.28

- Tipo: presenza
- Issue: I-10
- Verifica: il deliverable enuncia il risultato: il successivo termine di centottanta giorni non è ancora databile.
- Pass (insieme chiuso): afferma: il successivo termine di centottanta giorni non è ancora databile | conclude: il successivo termine di centottanta giorni non è ancora databile
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_nota_studio_termini_impugnazione.pdf, contenuto pertinente a seconda decadenza; art. 6 legge 604/1966

## B.29

- Tipo: attribuzione
- Issue: I-10
- Verifica: il deliverable collega il dato al documento: assenza di impugnazione nel fascicolo.
- Pass (insieme chiuso): cita 04_nota_studio_termini_impugnazione.pdf, contenuto pertinente a seconda decadenza | indica come riscontro 04_nota_studio_termini_impugnazione.pdf, contenuto pertinente a seconda decadenza
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_nota_studio_termini_impugnazione.pdf, contenuto pertinente a seconda decadenza; art. 6 legge 604/1966

## C.1

- Tipo: assenza
- Issue: N-01
- Verifica: chiusura simmetria sul falso positivo «copia intranet»: La presenza di una copia in intranet non cancella la prova dell'affissione fisica.
- Pass (insieme chiuso): non qualifica come criticita copia intranet | esclude espressamente il falso positivo copia intranet
- Fail: compare la conclusione vietata «copia intranet costituisce una criticita autonoma»
- Fonte: challenge_map.json; documenti pubblici

## C.2

- Tipo: assenza
- Issue: N-02
- Verifica: chiusura sovra-segnalazione sul falso positivo «registrazione audio»: L'assenza di audio non smentisce da sola il verbale di audizione firmato.
- Pass (insieme chiuso): non qualifica come criticita registrazione audio | esclude espressamente il falso positivo registrazione audio
- Fail: compare la conclusione vietata «registrazione audio costituisce una criticita autonoma»
- Fonte: challenge_map.json; documenti pubblici

## C.3

- Tipo: assenza
- Issue: N-03
- Verifica: chiusura presunzione sul falso positivo «seconda consegna»: L'assenza di una seconda modalità non invalida la ricevuta di consegna disponibile.
- Pass (insieme chiuso): non qualifica come criticita seconda consegna | esclude espressamente il falso positivo seconda consegna
- Fail: compare la conclusione vietata «seconda consegna costituisce una criticita autonoma»
- Fonte: challenge_map.json; documenti pubblici
