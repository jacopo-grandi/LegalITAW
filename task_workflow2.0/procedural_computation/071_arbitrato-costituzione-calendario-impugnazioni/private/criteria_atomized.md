# WF2-071 - Criteri atomizzati

Ogni riga valuta un solo fatto, valore, collegamento probatorio, effetto o azione.

## A.1

- Tipo: struttura
- Issue: A
- Verifica: la consegna usa i file arbitration_timeline.md.
- Pass (insieme chiuso): i nomi dei file coincidono con arbitration_timeline.md | il controllo deterministico sul requisito restituisce esito positivo
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
- Verifica: la parte testuale non supera 2.300 parole.
- Pass (insieme chiuso): il conteggio non supera 2.300 | il controllo deterministico sul requisito restituisce esito positivo
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
- Verifica: il deliverable enuncia il risultato: la clausola richiama il Regolamento CAM e fissa Milano come sede.
- Pass (insieme chiuso): afferma: la clausola richiama il Regolamento CAM e fissa Milano come sede | conclude: la clausola richiama il Regolamento CAM e fissa Milano come sede
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_estratto_contratto_e_ricevuta_cam.pdf, contenuto pertinente a regolamento e sede; contratto; Regolamento CAM

## B.2

- Tipo: attribuzione
- Issue: I-01
- Verifica: il deliverable collega il dato al documento: contratto quadro, clausola 18.
- Pass (insieme chiuso): cita 01_estratto_contratto_e_ricevuta_cam.pdf, contenuto pertinente a regolamento e sede | indica come riscontro 01_estratto_contratto_e_ricevuta_cam.pdf, contenuto pertinente a regolamento e sede
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_estratto_contratto_e_ricevuta_cam.pdf, contenuto pertinente a regolamento e sede; contratto; Regolamento CAM

## B.3

- Tipo: qualificazione
- Issue: I-01
- Verifica: il deliverable espone l'effetto: il procedimento e il computo dei termini seguono il regolamento richiamato.
- Pass (insieme chiuso): espone l'effetto: il procedimento e il computo dei termini seguono il regolamento richiamato | indica come conseguenza: il procedimento e il computo dei termini seguono il regolamento richiamato
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_estratto_contratto_e_ricevuta_cam.pdf, contenuto pertinente a regolamento e sede; contratto; Regolamento CAM

## B.4

- Tipo: presenza
- Issue: I-01
- Verifica: il deliverable indica l'azione: usare Milano e la disciplina CAM in ogni passaggio.
- Pass (insieme chiuso): afferma: la clausola richiama il Regolamento CAM e fissa Milano come sede | conclude: la clausola richiama il Regolamento CAM e fissa Milano come sede
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_estratto_contratto_e_ricevuta_cam.pdf, contenuto pertinente a regolamento e sede; contratto; Regolamento CAM

## B.5

- Tipo: qualificazione
- Issue: I-01
- Verifica: il deliverable tratta la lacuna come dato mancante: manca ogni successiva deroga delle parti.
- Pass (insieme chiuso): espone l'effetto: il procedimento e il computo dei termini seguono il regolamento richiamato | indica come conseguenza: il procedimento e il computo dei termini seguono il regolamento richiamato
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_estratto_contratto_e_ricevuta_cam.pdf, contenuto pertinente a regolamento e sede; contratto; Regolamento CAM

## B.6

- Tipo: valore
- Issue: I-02
- Verifica: il deliverable riporta il valore documentato per avvio.
- Pass (insieme chiuso): compare «9 gennaio 2029» | compare «2029-01-09»
- Fail: non compare ne «9 gennaio 2029» ne «2029-01-09» oppure compare un valore incompatibile
- Fonte: 01_estratto_contratto_e_ricevuta_cam.pdf, contenuto pertinente a avvio; ricevuta CAM; art. 10 Regolamento CAM

## B.7

- Tipo: attribuzione
- Issue: I-02
- Verifica: il deliverable collega il dato al documento: ricevuta CAM del 9 gennaio 2029.
- Pass (insieme chiuso): cita 01_estratto_contratto_e_ricevuta_cam.pdf, contenuto pertinente a avvio | indica come riscontro 01_estratto_contratto_e_ricevuta_cam.pdf, contenuto pertinente a avvio
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_estratto_contratto_e_ricevuta_cam.pdf, contenuto pertinente a avvio; ricevuta CAM; art. 10 Regolamento CAM

## B.8

- Tipo: qualificazione
- Issue: I-02
- Verifica: il deliverable espone l'effetto: questa è la data di avvio amministrativo da usare.
- Pass (insieme chiuso): espone l'effetto: questa è la data di avvio amministrativo da usare | indica come conseguenza: questa è la data di avvio amministrativo da usare
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_estratto_contratto_e_ricevuta_cam.pdf, contenuto pertinente a avvio; ricevuta CAM; art. 10 Regolamento CAM

## B.9

- Tipo: presenza
- Issue: I-02
- Verifica: il deliverable riporta il valore documentato per avvio.
- Pass (insieme chiuso): afferma: la domanda è stata ricevuta dalla Segreteria il 9 gennaio 2029 | conclude: la domanda è stata ricevuta dalla Segreteria il 9 gennaio 2029
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_estratto_contratto_e_ricevuta_cam.pdf, contenuto pertinente a avvio; ricevuta CAM; art. 10 Regolamento CAM

## B.10

- Tipo: qualificazione
- Issue: I-02
- Verifica: il deliverable tratta la lacuna come dato mancante: manca prova di un deposito anteriore.
- Pass (insieme chiuso): espone l'effetto: questa è la data di avvio amministrativo da usare | indica come conseguenza: questa è la data di avvio amministrativo da usare
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_estratto_contratto_e_ricevuta_cam.pdf, contenuto pertinente a avvio; ricevuta CAM; art. 10 Regolamento CAM

## B.11

- Tipo: valore
- Issue: I-03
- Verifica: il deliverable riporta il valore documentato per risposta.
- Pass (insieme chiuso): compare «8 febbraio 2029» | compare «2029-02-08»
- Fail: non compare ne «8 febbraio 2029» ne «2029-02-08» oppure compare un valore incompatibile
- Fonte: 02_registro_segreteria_cam.xlsx, contenuto pertinente a risposta; artt. 7 e 11 Regolamento CAM

## B.12

- Tipo: attribuzione
- Issue: I-03
- Verifica: il deliverable collega il dato al documento: trasmissione della domanda il 9 gennaio 2029.
- Pass (insieme chiuso): cita 02_registro_segreteria_cam.xlsx, contenuto pertinente a risposta | indica come riscontro 02_registro_segreteria_cam.xlsx, contenuto pertinente a risposta
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_segreteria_cam.xlsx, contenuto pertinente a risposta; artt. 7 e 11 Regolamento CAM

## B.13

- Tipo: qualificazione
- Issue: I-03
- Verifica: il deliverable espone l'effetto: la risposta del 1 febbraio è tempestiva.
- Pass (insieme chiuso): espone l'effetto: la risposta del 1 febbraio è tempestiva | indica come conseguenza: la risposta del 1 febbraio è tempestiva
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_segreteria_cam.xlsx, contenuto pertinente a risposta; artt. 7 e 11 Regolamento CAM

## B.14

- Tipo: presenza
- Issue: I-03
- Verifica: il deliverable riporta il valore documentato per risposta.
- Pass (insieme chiuso): afferma: il termine di trenta giorni per la risposta scade l'8 febbraio 2029 | conclude: il termine di trenta giorni per la risposta scade l'8 febbraio 2029
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_segreteria_cam.xlsx, contenuto pertinente a risposta; artt. 7 e 11 Regolamento CAM

## B.15

- Tipo: qualificazione
- Issue: I-03
- Verifica: il deliverable tratta la lacuna come dato mancante: nessuna proroga risulta dal fascicolo.
- Pass (insieme chiuso): espone l'effetto: la risposta del 1 febbraio è tempestiva | indica come conseguenza: la risposta del 1 febbraio è tempestiva
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_segreteria_cam.xlsx, contenuto pertinente a risposta; artt. 7 e 11 Regolamento CAM

## B.16

- Tipo: presenza
- Issue: I-04
- Verifica: il deliverable enuncia il risultato: Livenza ha nominato l'arbitra nella risposta del 1 febbraio 2029.
- Pass (insieme chiuso): afferma: Livenza ha nominato l'arbitra nella risposta del 1 febbraio 2029 | conclude: Livenza ha nominato l'arbitra nella risposta del 1 febbraio 2029
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_segreteria_cam.xlsx, contenuto pertinente a nomina di parte; risposta; art. 11 Regolamento CAM

## B.17

- Tipo: attribuzione
- Issue: I-04
- Verifica: il deliverable collega il dato al documento: risposta della convenuta.
- Pass (insieme chiuso): cita 02_registro_segreteria_cam.xlsx, contenuto pertinente a nomina di parte | indica come riscontro 02_registro_segreteria_cam.xlsx, contenuto pertinente a nomina di parte
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_segreteria_cam.xlsx, contenuto pertinente a nomina di parte; risposta; art. 11 Regolamento CAM

## B.18

- Tipo: qualificazione
- Issue: I-04
- Verifica: il deliverable espone l'effetto: non occorre una nomina sostitutiva della Camera.
- Pass (insieme chiuso): espone l'effetto: non occorre una nomina sostitutiva della Camera | indica come conseguenza: non occorre una nomina sostitutiva della Camera
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_segreteria_cam.xlsx, contenuto pertinente a nomina di parte; risposta; art. 11 Regolamento CAM

## B.19

- Tipo: presenza
- Issue: I-04
- Verifica: il deliverable indica l'azione: preservare prova del deposito.
- Pass (insieme chiuso): afferma: Livenza ha nominato l'arbitra nella risposta del 1 febbraio 2029 | conclude: Livenza ha nominato l'arbitra nella risposta del 1 febbraio 2029
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_segreteria_cam.xlsx, contenuto pertinente a nomina di parte; risposta; art. 11 Regolamento CAM

## B.20

- Tipo: valore
- Issue: I-05
- Verifica: il deliverable riporta il valore documentato per presidente.
- Pass (insieme chiuso): compare «19 febbraio 2029» | compare «2029-02-19»
- Fail: non compare ne «19 febbraio 2029» ne «2029-02-19» oppure compare un valore incompatibile
- Fonte: 03_email_nomine_e_competenza.eml, contenuto pertinente a presidente; comunicazione CAM

## B.21

- Tipo: attribuzione
- Issue: I-05
- Verifica: il deliverable collega il dato al documento: comunicazione di costituzione CAM.
- Pass (insieme chiuso): cita 03_email_nomine_e_competenza.eml, contenuto pertinente a presidente | indica come riscontro 03_email_nomine_e_competenza.eml, contenuto pertinente a presidente
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_nomine_e_competenza.eml, contenuto pertinente a presidente; comunicazione CAM

## B.22

- Tipo: qualificazione
- Issue: I-05
- Verifica: il deliverable espone l'effetto: il collegio risulta costituito in quella data.
- Pass (insieme chiuso): espone l'effetto: il collegio risulta costituito in quella data | indica come conseguenza: il collegio risulta costituito in quella data
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_nomine_e_competenza.eml, contenuto pertinente a presidente; comunicazione CAM

## B.23

- Tipo: presenza
- Issue: I-05
- Verifica: il deliverable riporta il valore documentato per presidente.
- Pass (insieme chiuso): afferma: la Camera ha confermato la presidente e comunicato la costituzione il 19 febbraio 2029 | conclude: la Camera ha confermato la presidente e comunicato la costituzione il 19 febbraio 2029
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_nomine_e_competenza.eml, contenuto pertinente a presidente; comunicazione CAM

## B.24

- Tipo: presenza
- Issue: I-06
- Verifica: il deliverable enuncia il risultato: l'eccezione di competenza deve essere formulata nella prima difesa utile.
- Pass (insieme chiuso): afferma: l'eccezione di competenza deve essere formulata nella prima difesa utile | conclude: l'eccezione di competenza deve essere formulata nella prima difesa utile
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_nomine_e_competenza.eml, contenuto pertinente a eccezione di competenza; art. 817 c.p.c.

## B.25

- Tipo: attribuzione
- Issue: I-06
- Verifica: il deliverable collega il dato al documento: bozza di risposta che la riserva senza svolgerla.
- Pass (insieme chiuso): cita 03_email_nomine_e_competenza.eml, contenuto pertinente a eccezione di competenza | indica come riscontro 03_email_nomine_e_competenza.eml, contenuto pertinente a eccezione di competenza
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_nomine_e_competenza.eml, contenuto pertinente a eccezione di competenza; art. 817 c.p.c.

## B.26

- Tipo: qualificazione
- Issue: I-06
- Verifica: il deliverable espone l'effetto: una riserva generica espone alla tardività.
- Pass (insieme chiuso): espone l'effetto: una riserva generica espone alla tardività | indica come conseguenza: una riserva generica espone alla tardività
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_nomine_e_competenza.eml, contenuto pertinente a eccezione di competenza; art. 817 c.p.c.

## B.27

- Tipo: presenza
- Issue: I-06
- Verifica: il deliverable indica l'azione: formulare subito oggetto e fondamento dell'eccezione.
- Pass (insieme chiuso): afferma: l'eccezione di competenza deve essere formulata nella prima difesa utile | conclude: l'eccezione di competenza deve essere formulata nella prima difesa utile
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_nomine_e_competenza.eml, contenuto pertinente a eccezione di competenza; art. 817 c.p.c.

## B.28

- Tipo: valore
- Issue: I-07
- Verifica: il deliverable riporta il valore documentato per calendario.
- Pass (insieme chiuso): compare «19 marzo 2029» | compare «2029-03-19»
- Fail: non compare ne «19 marzo 2029» ne «2029-03-19» oppure compare un valore incompatibile
- Fonte: 04_ordine_procedurale_n1.pdf, contenuto pertinente a calendario; ordine procedurale n. 1

## B.29

- Tipo: attribuzione
- Issue: I-07
- Verifica: il deliverable collega il dato al documento: ordine procedurale n. 1.
- Pass (insieme chiuso): cita 04_ordine_procedurale_n1.pdf, contenuto pertinente a calendario | indica come riscontro 04_ordine_procedurale_n1.pdf, contenuto pertinente a calendario
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_ordine_procedurale_n1.pdf, contenuto pertinente a calendario; ordine procedurale n. 1

## B.30

- Tipo: qualificazione
- Issue: I-07
- Verifica: il deliverable espone l'effetto: le due date governano la fase scritta.
- Pass (insieme chiuso): espone l'effetto: le due date governano la fase scritta | indica come conseguenza: le due date governano la fase scritta
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_ordine_procedurale_n1.pdf, contenuto pertinente a calendario; ordine procedurale n. 1

## B.31

- Tipo: presenza
- Issue: I-07
- Verifica: il deliverable riporta il valore documentato per calendario.
- Pass (insieme chiuso): afferma: l'ordine procedurale del 19 febbraio prevede memoria il 19 marzo 2029 e replica il 9 aprile 2029 | conclude: l'ordine procedurale del 19 febbraio prevede memoria il 19 marzo 2029 e replica il 9 aprile 2029
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_ordine_procedurale_n1.pdf, contenuto pertinente a calendario; ordine procedurale n. 1

## B.32

- Tipo: presenza
- Issue: I-08
- Verifica: il deliverable enuncia il risultato: la clausola attribuisce espressamente poteri cautelari agli arbitri.
- Pass (insieme chiuso): afferma: la clausola attribuisce espressamente poteri cautelari agli arbitri | conclude: la clausola attribuisce espressamente poteri cautelari agli arbitri
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_ordine_procedurale_n1.pdf, contenuto pertinente a cautelare; artt. 818 e 818-bis c.p.c.; contratto

## B.33

- Tipo: attribuzione
- Issue: I-08
- Verifica: il deliverable collega il dato al documento: clausola 18.6 del contratto.
- Pass (insieme chiuso): cita 04_ordine_procedurale_n1.pdf, contenuto pertinente a cautelare | indica come riscontro 04_ordine_procedurale_n1.pdf, contenuto pertinente a cautelare
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_ordine_procedurale_n1.pdf, contenuto pertinente a cautelare; artt. 818 e 818-bis c.p.c.; contratto

## B.34

- Tipo: qualificazione
- Issue: I-08
- Verifica: il deliverable espone l'effetto: dopo l'accettazione la competenza cautelare arbitrale è esclusiva.
- Pass (insieme chiuso): espone l'effetto: dopo l'accettazione la competenza cautelare arbitrale è esclusiva | indica come conseguenza: dopo l'accettazione la competenza cautelare arbitrale è esclusiva
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_ordine_procedurale_n1.pdf, contenuto pertinente a cautelare; artt. 818 e 818-bis c.p.c.; contratto

## B.35

- Tipo: presenza
- Issue: I-08
- Verifica: il deliverable indica l'azione: valutare l'istanza davanti al collegio.
- Pass (insieme chiuso): afferma: la clausola attribuisce espressamente poteri cautelari agli arbitri | conclude: la clausola attribuisce espressamente poteri cautelari agli arbitri
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_ordine_procedurale_n1.pdf, contenuto pertinente a cautelare; artt. 818 e 818-bis c.p.c.; contratto

## B.36

- Tipo: valore
- Issue: I-09
- Verifica: il deliverable riporta il valore documentato per termine del lodo.
- Pass (insieme chiuso): compare «20 agosto 2029» | compare «2029-08-20»
- Fail: non compare ne «20 agosto 2029» ne «2029-08-20» oppure compare un valore incompatibile
- Fonte: 05_nota_scadenze_studio_eridano.pdf, contenuto pertinente a termine del lodo; artt. 7 e 36 Regolamento CAM

## B.37

- Tipo: attribuzione
- Issue: I-09
- Verifica: il deliverable collega il dato al documento: costituzione il 18 febbraio 2029 e scadenza semestrale di sabato 18 agosto.
- Pass (insieme chiuso): cita 05_nota_scadenze_studio_eridano.pdf, contenuto pertinente a termine del lodo | indica come riscontro 05_nota_scadenze_studio_eridano.pdf, contenuto pertinente a termine del lodo
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_scadenze_studio_eridano.pdf, contenuto pertinente a termine del lodo; artt. 7 e 36 Regolamento CAM

## B.38

- Tipo: qualificazione
- Issue: I-09
- Verifica: il deliverable espone l'effetto: il primo giorno lavorativo seguente governa in assenza di proroga.
- Pass (insieme chiuso): espone l'effetto: il primo giorno lavorativo seguente governa in assenza di proroga | indica come conseguenza: il primo giorno lavorativo seguente governa in assenza di proroga
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_scadenze_studio_eridano.pdf, contenuto pertinente a termine del lodo; artt. 7 e 36 Regolamento CAM

## B.39

- Tipo: presenza
- Issue: I-09
- Verifica: il deliverable riporta il valore documentato per termine del lodo.
- Pass (insieme chiuso): afferma: il termine regolamentare del lodo cade domenica 19 agosto e slitta al 20 agosto 2029 | conclude: il termine regolamentare del lodo cade domenica 19 agosto e slitta al 20 agosto 2029
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_scadenze_studio_eridano.pdf, contenuto pertinente a termine del lodo; artt. 7 e 36 Regolamento CAM

## B.40

- Tipo: presenza
- Issue: I-10
- Verifica: il deliverable enuncia il risultato: il termine breve di impugnazione dipende dalla notificazione del lodo.
- Pass (insieme chiuso): afferma: il termine breve di impugnazione dipende dalla notificazione del lodo | conclude: il termine breve di impugnazione dipende dalla notificazione del lodo
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_scadenze_studio_eridano.pdf, contenuto pertinente a impugnazione; art. 828 c.p.c.

## B.41

- Tipo: attribuzione
- Issue: I-10
- Verifica: il deliverable collega il dato al documento: il fascicolo non contiene ancora un lodo notificato.
- Pass (insieme chiuso): cita 05_nota_scadenze_studio_eridano.pdf, contenuto pertinente a impugnazione | indica come riscontro 05_nota_scadenze_studio_eridano.pdf, contenuto pertinente a impugnazione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_scadenze_studio_eridano.pdf, contenuto pertinente a impugnazione; art. 828 c.p.c.

## B.42

- Tipo: qualificazione
- Issue: I-10
- Verifica: il deliverable espone l'effetto: alla data di riferimento non è calcolabile una scadenza breve.
- Pass (insieme chiuso): espone l'effetto: alla data di riferimento non è calcolabile una scadenza breve | indica come conseguenza: alla data di riferimento non è calcolabile una scadenza breve
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_scadenze_studio_eridano.pdf, contenuto pertinente a impugnazione; art. 828 c.p.c.

## B.43

- Tipo: presenza
- Issue: I-10
- Verifica: il deliverable indica l'azione: aprire un controllo alla futura notificazione.
- Pass (insieme chiuso): afferma: il termine breve di impugnazione dipende dalla notificazione del lodo | conclude: il termine breve di impugnazione dipende dalla notificazione del lodo
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_scadenze_studio_eridano.pdf, contenuto pertinente a impugnazione; art. 828 c.p.c.

## C.1

- Tipo: assenza
- Issue: N-01
- Verifica: chiusura simmetria sul falso positivo «forma digitale»: La sottoscrizione digitale del contratto non rende inefficace la clausola arbitrale.
- Pass (insieme chiuso): non qualifica come criticita forma digitale | esclude espressamente il falso positivo forma digitale
- Fail: compare la conclusione vietata «forma digitale costituisce una criticita autonoma»
- Fonte: challenge_map.json; documenti pubblici

## C.2

- Tipo: assenza
- Issue: N-02
- Verifica: chiusura sovra-segnalazione sul falso positivo «nazionalita arbitra»: La cittadinanza estera di un'arbitra non determina una sostituzione automatica.
- Pass (insieme chiuso): non qualifica come criticita nazionalita arbitra | esclude espressamente il falso positivo nazionalita arbitra
- Fail: compare la conclusione vietata «nazionalita arbitra costituisce una criticita autonoma»
- Fonte: challenge_map.json; documenti pubblici

## C.3

- Tipo: assenza
- Issue: N-03
- Verifica: chiusura presunzione sul falso positivo «udienza remota»: La previsione di una possibile udienza da remoto non modifica la sede giuridica di Milano.
- Pass (insieme chiuso): non qualifica come criticita udienza remota | esclude espressamente il falso positivo udienza remota
- Fail: compare la conclusione vietata «udienza remota costituisce una criticita autonoma»
- Fonte: challenge_map.json; documenti pubblici
