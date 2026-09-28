# WF2-078 - Criteri atomizzati

Ogni riga valuta un solo fatto, valore, collegamento probatorio, effetto o azione.

## A.1

- Tipo: struttura
- Issue: A
- Verifica: la consegna usa i file tax_position_memo.md.
- Pass (insieme chiuso): i nomi dei file coincidono con tax_position_memo.md | il controllo deterministico sul requisito restituisce esito positivo
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
- Verifica: la parte testuale non supera 3.000 parole.
- Pass (insieme chiuso): il conteggio non supera 3.000 | il controllo deterministico sul requisito restituisce esito positivo
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
- Verifica: il deliverable enuncia il risultato: la merce resta di proprietà di Lindevaart fino alla vendita al cliente italiano.
- Pass (insieme chiuso): afferma: la merce resta di proprietà di Lindevaart fino alla vendita al cliente italiano | conclude: la merce resta di proprietà di Lindevaart fino alla vendita al cliente italiano
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_contratto_distribuzione_logistica_italia.pdf, contenuto pertinente a flusso beni; contratto; registro

## B.2

- Tipo: attribuzione
- Issue: I-01
- Verifica: il deliverable collega il dato al documento: contratto e registro magazzino.
- Pass (insieme chiuso): cita 01_contratto_distribuzione_logistica_italia.pdf, contenuto pertinente a flusso beni | indica come riscontro 01_contratto_distribuzione_logistica_italia.pdf, contenuto pertinente a flusso beni
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_contratto_distribuzione_logistica_italia.pdf, contenuto pertinente a flusso beni; contratto; registro

## B.3

- Tipo: qualificazione
- Issue: I-01
- Verifica: il deliverable espone l'effetto: il distributore non opera come puro buy-sell sui beni in deposito.
- Pass (insieme chiuso): espone l'effetto: il distributore non opera come puro buy-sell sui beni in deposito | indica come conseguenza: il distributore non opera come puro buy-sell sui beni in deposito
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_contratto_distribuzione_logistica_italia.pdf, contenuto pertinente a flusso beni; contratto; registro

## B.4

- Tipo: presenza
- Issue: I-01
- Verifica: il deliverable indica l'azione: ricostruire passaggio proprietà e fatture.
- Pass (insieme chiuso): afferma: la merce resta di proprietà di Lindevaart fino alla vendita al cliente italiano | conclude: la merce resta di proprietà di Lindevaart fino alla vendita al cliente italiano
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_contratto_distribuzione_logistica_italia.pdf, contenuto pertinente a flusso beni; contratto; registro

## B.5

- Tipo: qualificazione
- Issue: I-01
- Verifica: il deliverable tratta la lacuna come dato mancante: mancano Incoterms per due clienti.
- Pass (insieme chiuso): espone l'effetto: il distributore non opera come puro buy-sell sui beni in deposito | indica come conseguenza: il distributore non opera come puro buy-sell sui beni in deposito
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_contratto_distribuzione_logistica_italia.pdf, contenuto pertinente a flusso beni; contratto; registro

## B.6

- Tipo: assenza
- Issue: I-01
- Verifica: il deliverable esclude la conclusione bersaglio: descrivere sempre una rivendita locale.
- Pass (insieme chiuso): indica l'azione: ricostruire passaggio proprietà e fatture | propone: ricostruire passaggio proprietà e fatture
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_contratto_distribuzione_logistica_italia.pdf, contenuto pertinente a flusso beni; contratto; registro

## B.7

- Tipo: attribuzione
- Issue: I-01
- Verifica: il deliverable usa la fonte indicata: contratto; registro.
- Pass (insieme chiuso): cita 01_contratto_distribuzione_logistica_italia.pdf, contenuto pertinente a flusso beni | indica come riscontro 01_contratto_distribuzione_logistica_italia.pdf, contenuto pertinente a flusso beni
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_contratto_distribuzione_logistica_italia.pdf, contenuto pertinente a flusso beni; contratto; registro

## B.8

- Tipo: presenza
- Issue: I-02
- Verifica: il deliverable enuncia il risultato: Lindevaart dispone in via continuativa di un'area esclusiva nel magazzino di Verona.
- Pass (insieme chiuso): afferma: Lindevaart dispone in via continuativa di un'area esclusiva nel magazzino di Verona | conclude: Lindevaart dispone in via continuativa di un'area esclusiva nel magazzino di Verona
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_contratto_distribuzione_logistica_italia.pdf, contenuto pertinente a luogo fisso; art. 162 TUIR

## B.9

- Tipo: attribuzione
- Issue: I-02
- Verifica: il deliverable collega il dato al documento: contratto logistico e planimetria.
- Pass (insieme chiuso): cita 01_contratto_distribuzione_logistica_italia.pdf, contenuto pertinente a luogo fisso | indica come riscontro 01_contratto_distribuzione_logistica_italia.pdf, contenuto pertinente a luogo fisso
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_contratto_distribuzione_logistica_italia.pdf, contenuto pertinente a luogo fisso; art. 162 TUIR

## B.10

- Tipo: qualificazione
- Issue: I-02
- Verifica: il deliverable espone l'effetto: il requisito di disponibilità materiale richiede analisi.
- Pass (insieme chiuso): espone l'effetto: il requisito di disponibilità materiale richiede analisi | indica come conseguenza: il requisito di disponibilità materiale richiede analisi
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_contratto_distribuzione_logistica_italia.pdf, contenuto pertinente a luogo fisso; art. 162 TUIR

## B.11

- Tipo: presenza
- Issue: I-02
- Verifica: il deliverable indica l'azione: verificare accessi, durata e poteri.
- Pass (insieme chiuso): afferma: Lindevaart dispone in via continuativa di un'area esclusiva nel magazzino di Verona | conclude: Lindevaart dispone in via continuativa di un'area esclusiva nel magazzino di Verona
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_contratto_distribuzione_logistica_italia.pdf, contenuto pertinente a luogo fisso; art. 162 TUIR

## B.12

- Tipo: qualificazione
- Issue: I-02
- Verifica: il deliverable tratta la lacuna come dato mancante: manca il registro accessi.
- Pass (insieme chiuso): espone l'effetto: il requisito di disponibilità materiale richiede analisi | indica come conseguenza: il requisito di disponibilità materiale richiede analisi
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_contratto_distribuzione_logistica_italia.pdf, contenuto pertinente a luogo fisso; art. 162 TUIR

## B.13

- Tipo: assenza
- Issue: I-02
- Verifica: il deliverable esclude la conclusione bersaglio: escludere il luogo perché intestato a Garrano.
- Pass (insieme chiuso): indica l'azione: verificare accessi, durata e poteri | propone: verificare accessi, durata e poteri
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_contratto_distribuzione_logistica_italia.pdf, contenuto pertinente a luogo fisso; art. 162 TUIR

## B.14

- Tipo: attribuzione
- Issue: I-02
- Verifica: il deliverable usa la fonte indicata: art. 162 TUIR.
- Pass (insieme chiuso): cita 01_contratto_distribuzione_logistica_italia.pdf, contenuto pertinente a luogo fisso | indica come riscontro 01_contratto_distribuzione_logistica_italia.pdf, contenuto pertinente a luogo fisso
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_contratto_distribuzione_logistica_italia.pdf, contenuto pertinente a luogo fisso; art. 162 TUIR

## B.15

- Tipo: presenza
- Issue: I-03
- Verifica: il deliverable enuncia il risultato: nel magazzino si svolgono anche configurazione e collaudo pre-consegna.
- Pass (insieme chiuso): afferma: nel magazzino si svolgono anche configurazione e collaudo pre-consegna | conclude: nel magazzino si svolgono anche configurazione e collaudo pre-consegna
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_operativo_centro_verona.xlsx, contenuto pertinente a attività ausiliaria; art. 162 TUIR

## B.16

- Tipo: attribuzione
- Issue: I-03
- Verifica: il deliverable collega il dato al documento: manuale operativo.
- Pass (insieme chiuso): cita 02_registro_operativo_centro_verona.xlsx, contenuto pertinente a attività ausiliaria | indica come riscontro 02_registro_operativo_centro_verona.xlsx, contenuto pertinente a attività ausiliaria
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_operativo_centro_verona.xlsx, contenuto pertinente a attività ausiliaria; art. 162 TUIR

## B.17

- Tipo: qualificazione
- Issue: I-03
- Verifica: il deliverable espone l'effetto: le attività eccedono il solo deposito descritto dal contratto.
- Pass (insieme chiuso): espone l'effetto: le attività eccedono il solo deposito descritto dal contratto | indica come conseguenza: le attività eccedono il solo deposito descritto dal contratto
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_operativo_centro_verona.xlsx, contenuto pertinente a attività ausiliaria; art. 162 TUIR

## B.18

- Tipo: presenza
- Issue: I-03
- Verifica: il deliverable indica l'azione: valutare il complesso unitario delle funzioni.
- Pass (insieme chiuso): afferma: nel magazzino si svolgono anche configurazione e collaudo pre-consegna | conclude: nel magazzino si svolgono anche configurazione e collaudo pre-consegna
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_operativo_centro_verona.xlsx, contenuto pertinente a attività ausiliaria; art. 162 TUIR

## B.19

- Tipo: qualificazione
- Issue: I-03
- Verifica: il deliverable tratta la lacuna come dato mancante: manca il tempo-uomo per attività.
- Pass (insieme chiuso): espone l'effetto: le attività eccedono il solo deposito descritto dal contratto | indica come conseguenza: le attività eccedono il solo deposito descritto dal contratto
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_operativo_centro_verona.xlsx, contenuto pertinente a attività ausiliaria; art. 162 TUIR

## B.20

- Tipo: assenza
- Issue: I-03
- Verifica: il deliverable esclude la conclusione bersaglio: qualificare tutto come deposito.
- Pass (insieme chiuso): indica l'azione: valutare il complesso unitario delle funzioni | propone: valutare il complesso unitario delle funzioni
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_operativo_centro_verona.xlsx, contenuto pertinente a attività ausiliaria; art. 162 TUIR

## B.21

- Tipo: attribuzione
- Issue: I-03
- Verifica: il deliverable usa la fonte indicata: art. 162 TUIR.
- Pass (insieme chiuso): cita 02_registro_operativo_centro_verona.xlsx, contenuto pertinente a attività ausiliaria | indica come riscontro 02_registro_operativo_centro_verona.xlsx, contenuto pertinente a attività ausiliaria
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_operativo_centro_verona.xlsx, contenuto pertinente a attività ausiliaria; art. 162 TUIR

## B.22

- Tipo: presenza
- Issue: I-04
- Verifica: il deliverable enuncia il risultato: il country manager negozia prezzo e condizioni chiuse poi approvate senza modifiche nei Paesi Bassi.
- Pass (insieme chiuso): afferma: il country manager negozia prezzo e condizioni chiuse poi approvate senza modifiche nei Paesi Bassi | conclude: il country manager negozia prezzo e condizioni chiuse poi approvate senza modifiche nei Paesi Bassi
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_operativo_centro_verona.xlsx, contenuto pertinente a agente dipendente; art. 162 TUIR

## B.23

- Tipo: attribuzione
- Issue: I-04
- Verifica: il deliverable collega il dato al documento: email di approvazione.
- Pass (insieme chiuso): cita 02_registro_operativo_centro_verona.xlsx, contenuto pertinente a agente dipendente | indica come riscontro 02_registro_operativo_centro_verona.xlsx, contenuto pertinente a agente dipendente
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_operativo_centro_verona.xlsx, contenuto pertinente a agente dipendente; art. 162 TUIR

## B.24

- Tipo: qualificazione
- Issue: I-04
- Verifica: il deliverable espone l'effetto: la prassi è rilevante per la stabile personale.
- Pass (insieme chiuso): espone l'effetto: la prassi è rilevante per la stabile personale | indica come conseguenza: la prassi è rilevante per la stabile personale
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_operativo_centro_verona.xlsx, contenuto pertinente a agente dipendente; art. 162 TUIR

## B.25

- Tipo: presenza
- Issue: I-04
- Verifica: il deliverable indica l'azione: campionare contratti e scostamenti.
- Pass (insieme chiuso): afferma: il country manager negozia prezzo e condizioni chiuse poi approvate senza modifiche nei Paesi Bassi | conclude: il country manager negozia prezzo e condizioni chiuse poi approvate senza modifiche nei Paesi Bassi
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_operativo_centro_verona.xlsx, contenuto pertinente a agente dipendente; art. 162 TUIR

## B.26

- Tipo: qualificazione
- Issue: I-04
- Verifica: il deliverable tratta la lacuna come dato mancante: mancano deleghe formali.
- Pass (insieme chiuso): espone l'effetto: la prassi è rilevante per la stabile personale | indica come conseguenza: la prassi è rilevante per la stabile personale
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_operativo_centro_verona.xlsx, contenuto pertinente a agente dipendente; art. 162 TUIR

## B.27

- Tipo: assenza
- Issue: I-04
- Verifica: il deliverable esclude la conclusione bersaglio: guardare solo alla firma finale.
- Pass (insieme chiuso): indica l'azione: campionare contratti e scostamenti | propone: campionare contratti e scostamenti
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_operativo_centro_verona.xlsx, contenuto pertinente a agente dipendente; art. 162 TUIR

## B.28

- Tipo: valore
- Issue: I-05
- Verifica: il deliverable riporta il valore documentato per indipendenza.
- Pass (insieme chiuso): compare «82 per cento» | compare «82%»
- Fail: non compare ne «82 per cento» ne «82%» oppure compare un valore incompatibile
- Fonte: 03_email_dati_gestionali_garrano.eml, contenuto pertinente a indipendenza; art. 162 TUIR; bilancio

## B.29

- Tipo: attribuzione
- Issue: I-05
- Verifica: il deliverable collega il dato al documento: bilancio gestionale.
- Pass (insieme chiuso): cita 03_email_dati_gestionali_garrano.eml, contenuto pertinente a indipendenza | indica come riscontro 03_email_dati_gestionali_garrano.eml, contenuto pertinente a indipendenza
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_dati_gestionali_garrano.eml, contenuto pertinente a indipendenza; art. 162 TUIR; bilancio

## B.30

- Tipo: qualificazione
- Issue: I-05
- Verifica: il deliverable espone l'effetto: dipendenza economica e istruzioni riducono il peso dell'etichetta contrattuale.
- Pass (insieme chiuso): espone l'effetto: dipendenza economica e istruzioni riducono il peso dell'etichetta contrattuale | indica come conseguenza: dipendenza economica e istruzioni riducono il peso dell'etichetta contrattuale
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_dati_gestionali_garrano.eml, contenuto pertinente a indipendenza; art. 162 TUIR; bilancio

## B.31

- Tipo: presenza
- Issue: I-05
- Verifica: il deliverable riporta il valore documentato per indipendenza.
- Pass (insieme chiuso): afferma: Garrano ricava l'82 per cento dei compensi dal gruppo Lindevaart | conclude: Garrano ricava l'82 per cento dei compensi dal gruppo Lindevaart
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_dati_gestionali_garrano.eml, contenuto pertinente a indipendenza; art. 162 TUIR; bilancio

## B.32

- Tipo: qualificazione
- Issue: I-05
- Verifica: il deliverable tratta la lacuna come dato mancante: mancano clienti alternativi aggiornati.
- Pass (insieme chiuso): espone l'effetto: dipendenza economica e istruzioni riducono il peso dell'etichetta contrattuale | indica come conseguenza: dipendenza economica e istruzioni riducono il peso dell'etichetta contrattuale
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_dati_gestionali_garrano.eml, contenuto pertinente a indipendenza; art. 162 TUIR; bilancio

## B.33

- Tipo: assenza
- Issue: I-05
- Verifica: il deliverable esclude la conclusione bersaglio: ritenere decisivo il nome distributore indipendente.
- Pass (insieme chiuso): indica l'azione: analizzare rischio e autonomia | propone: analizzare rischio e autonomia
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_dati_gestionali_garrano.eml, contenuto pertinente a indipendenza; art. 162 TUIR; bilancio

## B.34

- Tipo: presenza
- Issue: I-06
- Verifica: il deliverable enuncia il risultato: logistica, marketing e negoziazione sono divisi fra entità correlate nello stesso modello.
- Pass (insieme chiuso): afferma: logistica, marketing e negoziazione sono divisi fra entità correlate nello stesso modello | conclude: logistica, marketing e negoziazione sono divisi fra entità correlate nello stesso modello
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_dati_gestionali_garrano.eml, contenuto pertinente a anti-frammentazione; art. 162 TUIR

## B.35

- Tipo: attribuzione
- Issue: I-06
- Verifica: il deliverable collega il dato al documento: organigramma e contratti infragruppo.
- Pass (insieme chiuso): cita 03_email_dati_gestionali_garrano.eml, contenuto pertinente a anti-frammentazione | indica come riscontro 03_email_dati_gestionali_garrano.eml, contenuto pertinente a anti-frammentazione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_dati_gestionali_garrano.eml, contenuto pertinente a anti-frammentazione; art. 162 TUIR

## B.36

- Tipo: qualificazione
- Issue: I-06
- Verifica: il deliverable espone l'effetto: le attività combinate vanno considerate insieme.
- Pass (insieme chiuso): espone l'effetto: le attività combinate vanno considerate insieme | indica come conseguenza: le attività combinate vanno considerate insieme
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_dati_gestionali_garrano.eml, contenuto pertinente a anti-frammentazione; art. 162 TUIR

## B.37

- Tipo: presenza
- Issue: I-06
- Verifica: il deliverable indica l'azione: mappare funzioni complementari.
- Pass (insieme chiuso): afferma: logistica, marketing e negoziazione sono divisi fra entità correlate nello stesso modello | conclude: logistica, marketing e negoziazione sono divisi fra entità correlate nello stesso modello
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_dati_gestionali_garrano.eml, contenuto pertinente a anti-frammentazione; art. 162 TUIR

## B.38

- Tipo: qualificazione
- Issue: I-06
- Verifica: il deliverable tratta la lacuna come dato mancante: manca il contratto marketing.
- Pass (insieme chiuso): espone l'effetto: le attività combinate vanno considerate insieme | indica come conseguenza: le attività combinate vanno considerate insieme
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_dati_gestionali_garrano.eml, contenuto pertinente a anti-frammentazione; art. 162 TUIR

## B.39

- Tipo: assenza
- Issue: I-06
- Verifica: il deliverable esclude la conclusione bersaglio: valutare ogni funzione isolatamente.
- Pass (insieme chiuso): indica l'azione: mappare funzioni complementari | propone: mappare funzioni complementari
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_dati_gestionali_garrano.eml, contenuto pertinente a anti-frammentazione; art. 162 TUIR

## B.40

- Tipo: valore
- Issue: I-07
- Verifica: il deliverable riporta il valore documentato per stabile iva.
- Pass (insieme chiuso): compare «sei tecnici» | compare «6 tecnici»
- Fail: non compare ne «sei tecnici» ne «6 tecnici» oppure compare un valore incompatibile
- Fonte: 04_relazione_tecnico_organizzativa_verona.pdf, contenuto pertinente a stabile iva; art. 11 Reg. UE 282/2011

## B.41

- Tipo: attribuzione
- Issue: I-07
- Verifica: il deliverable collega il dato al documento: roster e inventario IT.
- Pass (insieme chiuso): cita 04_relazione_tecnico_organizzativa_verona.pdf, contenuto pertinente a stabile iva | indica come riscontro 04_relazione_tecnico_organizzativa_verona.pdf, contenuto pertinente a stabile iva
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_tecnico_organizzativa_verona.pdf, contenuto pertinente a stabile iva; art. 11 Reg. UE 282/2011

## B.42

- Tipo: qualificazione
- Issue: I-07
- Verifica: il deliverable espone l'effetto: mezzi umani e tecnici possono integrare una struttura IVA.
- Pass (insieme chiuso): espone l'effetto: mezzi umani e tecnici possono integrare una struttura IVA | indica come conseguenza: mezzi umani e tecnici possono integrare una struttura IVA
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_tecnico_organizzativa_verona.pdf, contenuto pertinente a stabile iva; art. 11 Reg. UE 282/2011

## B.43

- Tipo: presenza
- Issue: I-07
- Verifica: il deliverable riporta il valore documentato per stabile iva.
- Pass (insieme chiuso): afferma: sei tecnici e il sistema locale sono usati stabilmente per configurare le forniture | conclude: sei tecnici e il sistema locale sono usati stabilmente per configurare le forniture
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_tecnico_organizzativa_verona.pdf, contenuto pertinente a stabile iva; art. 11 Reg. UE 282/2011

## B.44

- Tipo: qualificazione
- Issue: I-07
- Verifica: il deliverable tratta la lacuna come dato mancante: manca l'allocazione delle ore.
- Pass (insieme chiuso): espone l'effetto: mezzi umani e tecnici possono integrare una struttura IVA | indica come conseguenza: mezzi umani e tecnici possono integrare una struttura IVA
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_tecnico_organizzativa_verona.pdf, contenuto pertinente a stabile iva; art. 11 Reg. UE 282/2011

## B.45

- Tipo: assenza
- Issue: I-07
- Verifica: il deliverable esclude la conclusione bersaglio: dedurre la stabile IVA dalla sola partita IVA.
- Pass (insieme chiuso): indica l'azione: distinguere ricezione di servizi e intervento nelle vendite | propone: distinguere ricezione di servizi e intervento nelle vendite
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_tecnico_organizzativa_verona.pdf, contenuto pertinente a stabile iva; art. 11 Reg. UE 282/2011

## B.46

- Tipo: presenza
- Issue: I-08
- Verifica: il deliverable enuncia il risultato: il personale italiano prepara i beni prima della consegna ma la fatturazione resta olandese.
- Pass (insieme chiuso): afferma: il personale italiano prepara i beni prima della consegna ma la fatturazione resta olandese | conclude: il personale italiano prepara i beni prima della consegna ma la fatturazione resta olandese
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_tecnico_organizzativa_verona.pdf, contenuto pertinente a intervento; art. 53 Reg. UE 282/2011

## B.47

- Tipo: attribuzione
- Issue: I-08
- Verifica: il deliverable collega il dato al documento: workflow ordini.
- Pass (insieme chiuso): cita 04_relazione_tecnico_organizzativa_verona.pdf, contenuto pertinente a intervento | indica come riscontro 04_relazione_tecnico_organizzativa_verona.pdf, contenuto pertinente a intervento
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_tecnico_organizzativa_verona.pdf, contenuto pertinente a intervento; art. 53 Reg. UE 282/2011

## B.48

- Tipo: qualificazione
- Issue: I-08
- Verifica: il deliverable espone l'effetto: occorre stabilire se le risorse intervengono nella specifica operazione.
- Pass (insieme chiuso): espone l'effetto: occorre stabilire se le risorse intervengono nella specifica operazione | indica come conseguenza: occorre stabilire se le risorse intervengono nella specifica operazione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_tecnico_organizzativa_verona.pdf, contenuto pertinente a intervento; art. 53 Reg. UE 282/2011

## B.49

- Tipo: presenza
- Issue: I-08
- Verifica: il deliverable indica l'azione: tracciare attività prima e durante la fornitura.
- Pass (insieme chiuso): afferma: il personale italiano prepara i beni prima della consegna ma la fatturazione resta olandese | conclude: il personale italiano prepara i beni prima della consegna ma la fatturazione resta olandese
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_tecnico_organizzativa_verona.pdf, contenuto pertinente a intervento; art. 53 Reg. UE 282/2011

## B.50

- Tipo: qualificazione
- Issue: I-08
- Verifica: il deliverable tratta la lacuna come dato mancante: mancano log per ordine.
- Pass (insieme chiuso): espone l'effetto: occorre stabilire se le risorse intervengono nella specifica operazione | indica come conseguenza: occorre stabilire se le risorse intervengono nella specifica operazione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_tecnico_organizzativa_verona.pdf, contenuto pertinente a intervento; art. 53 Reg. UE 282/2011

## B.51

- Tipo: assenza
- Issue: I-08
- Verifica: il deliverable esclude la conclusione bersaglio: ritenere decisiva la contabilità locale.
- Pass (insieme chiuso): indica l'azione: tracciare attività prima e durante la fornitura | propone: tracciare attività prima e durante la fornitura
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_tecnico_organizzativa_verona.pdf, contenuto pertinente a intervento; art. 53 Reg. UE 282/2011

## B.52

- Tipo: presenza
- Issue: I-09
- Verifica: il deliverable enuncia il risultato: il contratto cloud indica la sede olandese ma gli utenti principali sono a Verona.
- Pass (insieme chiuso): afferma: il contratto cloud indica la sede olandese ma gli utenti principali sono a Verona | conclude: il contratto cloud indica la sede olandese ma gli utenti principali sono a Verona
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_studio_bissoli_posizione_italiana.pdf, contenuto pertinente a servizi ricevuti; artt. 21-22 Reg. UE 282/2011

## B.53

- Tipo: attribuzione
- Issue: I-09
- Verifica: il deliverable collega il dato al documento: ordine cloud e utenze.
- Pass (insieme chiuso): cita 05_nota_studio_bissoli_posizione_italiana.pdf, contenuto pertinente a servizi ricevuti | indica come riscontro 05_nota_studio_bissoli_posizione_italiana.pdf, contenuto pertinente a servizi ricevuti
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_studio_bissoli_posizione_italiana.pdf, contenuto pertinente a servizi ricevuti; artt. 21-22 Reg. UE 282/2011

## B.54

- Tipo: qualificazione
- Issue: I-09
- Verifica: il deliverable espone l'effetto: destinazione e uso richiedono il test degli artt. 21 e 22.
- Pass (insieme chiuso): espone l'effetto: destinazione e uso richiedono il test degli artt. 21 e 22 | indica come conseguenza: destinazione e uso richiedono il test degli artt. 21 e 22
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_studio_bissoli_posizione_italiana.pdf, contenuto pertinente a servizi ricevuti; artt. 21-22 Reg. UE 282/2011

## B.55

- Tipo: presenza
- Issue: I-09
- Verifica: il deliverable indica l'azione: documentare natura, ordine, pagamento e uso.
- Pass (insieme chiuso): afferma: il contratto cloud indica la sede olandese ma gli utenti principali sono a Verona | conclude: il contratto cloud indica la sede olandese ma gli utenti principali sono a Verona
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_studio_bissoli_posizione_italiana.pdf, contenuto pertinente a servizi ricevuti; artt. 21-22 Reg. UE 282/2011

## B.56

- Tipo: qualificazione
- Issue: I-09
- Verifica: il deliverable tratta la lacuna come dato mancante: manca la fattura del fornitore.
- Pass (insieme chiuso): espone l'effetto: destinazione e uso richiedono il test degli artt. 21 e 22 | indica come conseguenza: destinazione e uso richiedono il test degli artt. 21 e 22
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_studio_bissoli_posizione_italiana.pdf, contenuto pertinente a servizi ricevuti; artt. 21-22 Reg. UE 282/2011

## B.57

- Tipo: assenza
- Issue: I-09
- Verifica: il deliverable esclude la conclusione bersaglio: usare solo l'indirizzo contrattuale.
- Pass (insieme chiuso): indica l'azione: documentare natura, ordine, pagamento e uso | propone: documentare natura, ordine, pagamento e uso
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_studio_bissoli_posizione_italiana.pdf, contenuto pertinente a servizi ricevuti; artt. 21-22 Reg. UE 282/2011

## B.58

- Tipo: presenza
- Issue: I-10
- Verifica: il deliverable enuncia il risultato: l'identificazione IVA italiana non prova da sola una stabile organizzazione IVA.
- Pass (insieme chiuso): afferma: l'identificazione IVA italiana non prova da sola una stabile organizzazione IVA | conclude: l'identificazione IVA italiana non prova da sola una stabile organizzazione IVA
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_studio_bissoli_posizione_italiana.pdf, contenuto pertinente a assenza di automatismo; art. 11 Reg. UE 282/2011

## B.59

- Tipo: attribuzione
- Issue: I-10
- Verifica: il deliverable collega il dato al documento: certificato di identificazione.
- Pass (insieme chiuso): cita 05_nota_studio_bissoli_posizione_italiana.pdf, contenuto pertinente a assenza di automatismo | indica come riscontro 05_nota_studio_bissoli_posizione_italiana.pdf, contenuto pertinente a assenza di automatismo
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_studio_bissoli_posizione_italiana.pdf, contenuto pertinente a assenza di automatismo; art. 11 Reg. UE 282/2011

## B.60

- Tipo: qualificazione
- Issue: I-10
- Verifica: il deliverable espone l'effetto: le conclusioni sulle imposte dirette e IVA restano autonome.
- Pass (insieme chiuso): espone l'effetto: le conclusioni sulle imposte dirette e IVA restano autonome | indica come conseguenza: le conclusioni sulle imposte dirette e IVA restano autonome
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_studio_bissoli_posizione_italiana.pdf, contenuto pertinente a assenza di automatismo; art. 11 Reg. UE 282/2011

## B.61

- Tipo: presenza
- Issue: I-10
- Verifica: il deliverable indica l'azione: esporre due test separati.
- Pass (insieme chiuso): afferma: l'identificazione IVA italiana non prova da sola una stabile organizzazione IVA | conclude: l'identificazione IVA italiana non prova da sola una stabile organizzazione IVA
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_studio_bissoli_posizione_italiana.pdf, contenuto pertinente a assenza di automatismo; art. 11 Reg. UE 282/2011

## B.62

- Tipo: qualificazione
- Issue: I-10
- Verifica: il deliverable tratta la lacuna come dato mancante: manca il motivo storico dell'identificazione.
- Pass (insieme chiuso): espone l'effetto: le conclusioni sulle imposte dirette e IVA restano autonome | indica come conseguenza: le conclusioni sulle imposte dirette e IVA restano autonome
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_studio_bissoli_posizione_italiana.pdf, contenuto pertinente a assenza di automatismo; art. 11 Reg. UE 282/2011

## B.63

- Tipo: assenza
- Issue: I-10
- Verifica: il deliverable esclude la conclusione bersaglio: far coincidere identificazione, stabile IVA e stabile reddituale.
- Pass (insieme chiuso): indica l'azione: esporre due test separati | propone: esporre due test separati
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_studio_bissoli_posizione_italiana.pdf, contenuto pertinente a assenza di automatismo; art. 11 Reg. UE 282/2011

## C.1

- Tipo: assenza
- Issue: N-01
- Verifica: chiusura simmetria sul falso positivo «partita iva»: La partita IVA italiana non prova da sola una struttura stabile ai fini IVA o reddituali.
- Pass (insieme chiuso): non qualifica come criticita partita iva | esclude espressamente il falso positivo partita iva
- Fail: compare la conclusione vietata «partita iva costituisce una criticita autonoma»
- Fonte: challenge_map.json; documenti pubblici

## C.2

- Tipo: assenza
- Issue: N-02
- Verifica: chiusura sovra-segnalazione sul falso positivo «intestazione magazzino»: L'intestazione del contratto a Garrano non esclude da sola la disponibilità dell'area per Lindevaart.
- Pass (insieme chiuso): non qualifica come criticita intestazione magazzino | esclude espressamente il falso positivo intestazione magazzino
- Fail: compare la conclusione vietata «intestazione magazzino costituisce una criticita autonoma»
- Fonte: challenge_map.json; documenti pubblici

## C.3

- Tipo: assenza
- Issue: N-03
- Verifica: chiusura presunzione sul falso positivo «firma olandese»: La firma finale nei Paesi Bassi non esaurisce l'esame della prassi negoziale italiana.
- Pass (insieme chiuso): non qualifica come criticita firma olandese | esclude espressamente il falso positivo firma olandese
- Fail: compare la conclusione vietata «firma olandese costituisce una criticita autonoma»
- Fonte: challenge_map.json; documenti pubblici
