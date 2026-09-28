# WF2-077 - Criteri atomizzati

Ogni riga valuta un solo fatto, valore, collegamento probatorio, effetto o azione.

## A.1

- Tipo: struttura
- Issue: A
- Verifica: la consegna usa i file finance_amendment_redline.docx e note.md.
- Pass (insieme chiuso): i nomi dei file coincidono con finance_amendment_redline.docx e note.md | il controllo deterministico sul requisito restituisce esito positivo
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

- Tipo: valore
- Issue: I-01
- Verifica: il deliverable riporta il valore documentato per waiver circoscritto.
- Pass (insieme chiuso): compare «30 giugno 2029» | compare «2029-06-30»
- Fail: non compare ne «30 giugno 2029» ne «2029-06-30» oppure compare un valore incompatibile
- Fonte: 01_amendment_n2_finanziamento_salmura.docx, contenuto pertinente a waiver circoscritto; richiesta; amendment

## B.2

- Tipo: attribuzione
- Issue: I-01
- Verifica: il deliverable collega il dato al documento: richiesta del debitore.
- Pass (insieme chiuso): cita 01_amendment_n2_finanziamento_salmura.docx, contenuto pertinente a waiver circoscritto | indica come riscontro 01_amendment_n2_finanziamento_salmura.docx, contenuto pertinente a waiver circoscritto
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_amendment_n2_finanziamento_salmura.docx, contenuto pertinente a waiver circoscritto; richiesta; amendment

## B.3

- Tipo: qualificazione
- Issue: I-01
- Verifica: il deliverable espone l'effetto: una rinuncia generale cancellerebbe default non istruiti.
- Pass (insieme chiuso): espone l'effetto: una rinuncia generale cancellerebbe default non istruiti | indica come conseguenza: una rinuncia generale cancellerebbe default non istruiti
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_amendment_n2_finanziamento_salmura.docx, contenuto pertinente a waiver circoscritto; richiesta; amendment

## B.4

- Tipo: presenza
- Issue: I-01
- Verifica: il deliverable riporta il valore documentato per waiver circoscritto.
- Pass (insieme chiuso): afferma: il waiver richiesto riguarda solo il Leverage Ratio al 30 giugno 2029 | conclude: il waiver richiesto riguarda solo il Leverage Ratio al 30 giugno 2029
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_amendment_n2_finanziamento_salmura.docx, contenuto pertinente a waiver circoscritto; richiesta; amendment

## B.5

- Tipo: qualificazione
- Issue: I-01
- Verifica: il deliverable tratta la lacuna come dato mancante: manca conferma su default ulteriori.
- Pass (insieme chiuso): espone l'effetto: una rinuncia generale cancellerebbe default non istruiti | indica come conseguenza: una rinuncia generale cancellerebbe default non istruiti
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_amendment_n2_finanziamento_salmura.docx, contenuto pertinente a waiver circoscritto; richiesta; amendment

## B.6

- Tipo: presenza
- Issue: I-02
- Verifica: il deliverable enuncia il risultato: la bozza non preserva i diritti per inadempimenti diversi.
- Pass (insieme chiuso): afferma: la bozza non preserva i diritti per inadempimenti diversi | conclude: la bozza non preserva i diritti per inadempimenti diversi
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_amendment_n2_finanziamento_salmura.docx, contenuto pertinente a riserva diritti; amendment; contratto originario

## B.7

- Tipo: attribuzione
- Issue: I-02
- Verifica: il deliverable collega il dato al documento: clausola 2.
- Pass (insieme chiuso): cita 01_amendment_n2_finanziamento_salmura.docx, contenuto pertinente a riserva diritti | indica come riscontro 01_amendment_n2_finanziamento_salmura.docx, contenuto pertinente a riserva diritti
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_amendment_n2_finanziamento_salmura.docx, contenuto pertinente a riserva diritti; amendment; contratto originario

## B.8

- Tipo: qualificazione
- Issue: I-02
- Verifica: il deliverable espone l'effetto: serve una riserva espressa.
- Pass (insieme chiuso): espone l'effetto: serve una riserva espressa | indica come conseguenza: serve una riserva espressa
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_amendment_n2_finanziamento_salmura.docx, contenuto pertinente a riserva diritti; amendment; contratto originario

## B.9

- Tipo: presenza
- Issue: I-02
- Verifica: il deliverable indica l'azione: inserire no waiver generale.
- Pass (insieme chiuso): afferma: la bozza non preserva i diritti per inadempimenti diversi | conclude: la bozza non preserva i diritti per inadempimenti diversi
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_amendment_n2_finanziamento_salmura.docx, contenuto pertinente a riserva diritti; amendment; contratto originario

## B.10

- Tipo: qualificazione
- Issue: I-02
- Verifica: il deliverable tratta la lacuna come dato mancante: manca l'elenco delle reservation letters.
- Pass (insieme chiuso): espone l'effetto: serve una riserva espressa | indica come conseguenza: serve una riserva espressa
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_amendment_n2_finanziamento_salmura.docx, contenuto pertinente a riserva diritti; amendment; contratto originario

## B.11

- Tipo: presenza
- Issue: I-03
- Verifica: il deliverable enuncia il risultato: le conferme dei garanti sono condizioni di efficacia non ancora soddisfatte.
- Pass (insieme chiuso): afferma: le conferme dei garanti sono condizioni di efficacia non ancora soddisfatte | conclude: le conferme dei garanti sono condizioni di efficacia non ancora soddisfatte
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_closing_checklist_amendment_n2.xlsx, contenuto pertinente a condizioni efficacia; closing checklist

## B.12

- Tipo: attribuzione
- Issue: I-03
- Verifica: il deliverable collega il dato al documento: closing checklist.
- Pass (insieme chiuso): cita 02_closing_checklist_amendment_n2.xlsx, contenuto pertinente a condizioni efficacia | indica come riscontro 02_closing_checklist_amendment_n2.xlsx, contenuto pertinente a condizioni efficacia
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_closing_checklist_amendment_n2.xlsx, contenuto pertinente a condizioni efficacia; closing checklist

## B.13

- Tipo: qualificazione
- Issue: I-03
- Verifica: il deliverable espone l'effetto: l'amendment non deve operare alla sola firma del debitore.
- Pass (insieme chiuso): espone l'effetto: l'amendment non deve operare alla sola firma del debitore | indica come conseguenza: l'amendment non deve operare alla sola firma del debitore
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_closing_checklist_amendment_n2.xlsx, contenuto pertinente a condizioni efficacia; closing checklist

## B.14

- Tipo: presenza
- Issue: I-03
- Verifica: il deliverable indica l'azione: richiedere conferma scritta dell'Agent.
- Pass (insieme chiuso): afferma: le conferme dei garanti sono condizioni di efficacia non ancora soddisfatte | conclude: le conferme dei garanti sono condizioni di efficacia non ancora soddisfatte
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_closing_checklist_amendment_n2.xlsx, contenuto pertinente a condizioni efficacia; closing checklist

## B.15

- Tipo: qualificazione
- Issue: I-03
- Verifica: il deliverable tratta la lacuna come dato mancante: manca la firma di due garanti.
- Pass (insieme chiuso): espone l'effetto: l'amendment non deve operare alla sola firma del debitore | indica come conseguenza: l'amendment non deve operare alla sola firma del debitore
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_closing_checklist_amendment_n2.xlsx, contenuto pertinente a condizioni efficacia; closing checklist

## B.16

- Tipo: valore
- Issue: I-04
- Verifica: il deliverable riporta il valore documentato per delibere.
- Pass (insieme chiuso): compare «15 milioni» | compare «euro 15.000.000»
- Fail: non compare ne «15 milioni» ne «euro 15.000.000» oppure compare un valore incompatibile
- Fonte: 02_closing_checklist_amendment_n2.xlsx, contenuto pertinente a delibere; delibera; amendment

## B.17

- Tipo: attribuzione
- Issue: I-04
- Verifica: il deliverable collega il dato al documento: delibera del 18 ottobre.
- Pass (insieme chiuso): cita 02_closing_checklist_amendment_n2.xlsx, contenuto pertinente a delibere | indica come riscontro 02_closing_checklist_amendment_n2.xlsx, contenuto pertinente a delibere
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_closing_checklist_amendment_n2.xlsx, contenuto pertinente a delibere; delibera; amendment

## B.18

- Tipo: qualificazione
- Issue: I-04
- Verifica: il deliverable espone l'effetto: la capienza autorizzativa non coincide con l'operazione.
- Pass (insieme chiuso): espone l'effetto: la capienza autorizzativa non coincide con l'operazione | indica come conseguenza: la capienza autorizzativa non coincide con l'operazione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_closing_checklist_amendment_n2.xlsx, contenuto pertinente a delibere; delibera; amendment

## B.19

- Tipo: presenza
- Issue: I-04
- Verifica: il deliverable riporta il valore documentato per delibere.
- Pass (insieme chiuso): afferma: la delibera del debitore autorizza 12 milioni ma l'esposizione modificata è 15 milioni | conclude: la delibera del debitore autorizza 12 milioni ma l'esposizione modificata è 15 milioni
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_closing_checklist_amendment_n2.xlsx, contenuto pertinente a delibere; delibera; amendment

## B.20

- Tipo: presenza
- Issue: I-05
- Verifica: il deliverable enuncia il risultato: la proroga e l'aumento del margine richiedono conferma espressa dei garanti.
- Pass (insieme chiuso): afferma: la proroga e l'aumento del margine richiedono conferma espressa dei garanti | conclude: la proroga e l'aumento del margine richiedono conferma espressa dei garanti
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_garanzie_e_ispezione_ipotecaria.eml, contenuto pertinente a conferma garanzie; garanzie; art. 1232 c.c.

## B.21

- Tipo: attribuzione
- Issue: I-05
- Verifica: il deliverable collega il dato al documento: testi delle garanzie.
- Pass (insieme chiuso): cita 03_email_garanzie_e_ispezione_ipotecaria.eml, contenuto pertinente a conferma garanzie | indica come riscontro 03_email_garanzie_e_ispezione_ipotecaria.eml, contenuto pertinente a conferma garanzie
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_garanzie_e_ispezione_ipotecaria.eml, contenuto pertinente a conferma garanzie; garanzie; art. 1232 c.c.

## B.22

- Tipo: qualificazione
- Issue: I-05
- Verifica: il deliverable espone l'effetto: il package deve riferirsi alle obbligazioni come modificate.
- Pass (insieme chiuso): espone l'effetto: il package deve riferirsi alle obbligazioni come modificate | indica come conseguenza: il package deve riferirsi alle obbligazioni come modificate
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_garanzie_e_ispezione_ipotecaria.eml, contenuto pertinente a conferma garanzie; garanzie; art. 1232 c.c.

## B.23

- Tipo: presenza
- Issue: I-05
- Verifica: il deliverable indica l'azione: acquisire confirmations separate.
- Pass (insieme chiuso): afferma: la proroga e l'aumento del margine richiedono conferma espressa dei garanti | conclude: la proroga e l'aumento del margine richiedono conferma espressa dei garanti
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_garanzie_e_ispezione_ipotecaria.eml, contenuto pertinente a conferma garanzie; garanzie; art. 1232 c.c.

## B.24

- Tipo: valore
- Issue: I-06
- Verifica: il deliverable riporta il valore documentato per ipoteca.
- Pass (insieme chiuso): compare «18 milioni» | compare «euro 18.000.000»
- Fail: non compare ne «18 milioni» ne «euro 18.000.000» oppure compare un valore incompatibile
- Fonte: 03_email_garanzie_e_ispezione_ipotecaria.eml, contenuto pertinente a ipoteca; nota ipotecaria; codice civile

## B.25

- Tipo: attribuzione
- Issue: I-06
- Verifica: il deliverable collega il dato al documento: ispezione ipotecaria.
- Pass (insieme chiuso): cita 03_email_garanzie_e_ispezione_ipotecaria.eml, contenuto pertinente a ipoteca | indica come riscontro 03_email_garanzie_e_ispezione_ipotecaria.eml, contenuto pertinente a ipoteca
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_garanzie_e_ispezione_ipotecaria.eml, contenuto pertinente a ipoteca; nota ipotecaria; codice civile

## B.26

- Tipo: qualificazione
- Issue: I-06
- Verifica: il deliverable espone l'effetto: la capienza va confrontata con capitale, interessi e accessori.
- Pass (insieme chiuso): espone l'effetto: la capienza va confrontata con capitale, interessi e accessori | indica come conseguenza: la capienza va confrontata con capitale, interessi e accessori
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_garanzie_e_ispezione_ipotecaria.eml, contenuto pertinente a ipoteca; nota ipotecaria; codice civile

## B.27

- Tipo: presenza
- Issue: I-06
- Verifica: il deliverable riporta il valore documentato per ipoteca.
- Pass (insieme chiuso): afferma: la nota ipotecaria indica un importo massimo di 18 milioni | conclude: la nota ipotecaria indica un importo massimo di 18 milioni
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_garanzie_e_ispezione_ipotecaria.eml, contenuto pertinente a ipoteca; nota ipotecaria; codice civile

## B.28

- Tipo: presenza
- Issue: I-07
- Verifica: il deliverable enuncia il risultato: il patto di pegno vieta modifiche al finanziamento senza consenso del datore.
- Pass (insieme chiuso): afferma: il patto di pegno vieta modifiche al finanziamento senza consenso del datore | conclude: il patto di pegno vieta modifiche al finanziamento senza consenso del datore
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_pegno_e_intercreditor.pdf, contenuto pertinente a pegno quote; pegno

## B.29

- Tipo: attribuzione
- Issue: I-07
- Verifica: il deliverable collega il dato al documento: pegno del 2027.
- Pass (insieme chiuso): cita 04_relazione_pegno_e_intercreditor.pdf, contenuto pertinente a pegno quote | indica come riscontro 04_relazione_pegno_e_intercreditor.pdf, contenuto pertinente a pegno quote
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_pegno_e_intercreditor.pdf, contenuto pertinente a pegno quote; pegno

## B.30

- Tipo: qualificazione
- Issue: I-07
- Verifica: il deliverable espone l'effetto: il consenso è un documento di closing.
- Pass (insieme chiuso): espone l'effetto: il consenso è un documento di closing | indica come conseguenza: il consenso è un documento di closing
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_pegno_e_intercreditor.pdf, contenuto pertinente a pegno quote; pegno

## B.31

- Tipo: presenza
- Issue: I-07
- Verifica: il deliverable indica l'azione: inserirlo tra le condizioni.
- Pass (insieme chiuso): afferma: il patto di pegno vieta modifiche al finanziamento senza consenso del datore | conclude: il patto di pegno vieta modifiche al finanziamento senza consenso del datore
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_pegno_e_intercreditor.pdf, contenuto pertinente a pegno quote; pegno

## B.32

- Tipo: presenza
- Issue: I-08
- Verifica: il deliverable enuncia il risultato: l'estensione della scadenza richiede Majority Senior Creditors e notifica ai subordinati.
- Pass (insieme chiuso): afferma: l'estensione della scadenza richiede Majority Senior Creditors e notifica ai subordinati | conclude: l'estensione della scadenza richiede Majority Senior Creditors e notifica ai subordinati
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_pegno_e_intercreditor.pdf, contenuto pertinente a intercreditor; intercreditor

## B.33

- Tipo: attribuzione
- Issue: I-08
- Verifica: il deliverable collega il dato al documento: accordo intercreditor.
- Pass (insieme chiuso): cita 04_relazione_pegno_e_intercreditor.pdf, contenuto pertinente a intercreditor | indica come riscontro 04_relazione_pegno_e_intercreditor.pdf, contenuto pertinente a intercreditor
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_pegno_e_intercreditor.pdf, contenuto pertinente a intercreditor; intercreditor

## B.34

- Tipo: qualificazione
- Issue: I-08
- Verifica: il deliverable espone l'effetto: la bozza non può rendere il consenso implicito.
- Pass (insieme chiuso): espone l'effetto: la bozza non può rendere il consenso implicito | indica come conseguenza: la bozza non può rendere il consenso implicito
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_pegno_e_intercreditor.pdf, contenuto pertinente a intercreditor; intercreditor

## B.35

- Tipo: presenza
- Issue: I-08
- Verifica: il deliverable indica l'azione: ottenere decisione e inviare notifica.
- Pass (insieme chiuso): afferma: l'estensione della scadenza richiede Majority Senior Creditors e notifica ai subordinati | conclude: l'estensione della scadenza richiede Majority Senior Creditors e notifica ai subordinati
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_pegno_e_intercreditor.pdf, contenuto pertinente a intercreditor; intercreditor

## B.36

- Tipo: presenza
- Issue: I-09
- Verifica: il deliverable enuncia il risultato: le parti intendono modificare e non novare il finanziamento.
- Pass (insieme chiuso): afferma: le parti intendono modificare e non novare il finanziamento | conclude: le parti intendono modificare e non novare il finanziamento
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_studio_bertelli_per_il_debitore.pdf, contenuto pertinente a novazione; term sheet; art. 1232 c.c.

## B.37

- Tipo: attribuzione
- Issue: I-09
- Verifica: il deliverable collega il dato al documento: term sheet.
- Pass (insieme chiuso): cita 05_nota_studio_bertelli_per_il_debitore.pdf, contenuto pertinente a novazione | indica come riscontro 05_nota_studio_bertelli_per_il_debitore.pdf, contenuto pertinente a novazione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_studio_bertelli_per_il_debitore.pdf, contenuto pertinente a novazione; term sheet; art. 1232 c.c.

## B.38

- Tipo: qualificazione
- Issue: I-09
- Verifica: il deliverable espone l'effetto: il testo deve preservare continuità di debito e garanzie.
- Pass (insieme chiuso): espone l'effetto: il testo deve preservare continuità di debito e garanzie | indica come conseguenza: il testo deve preservare continuità di debito e garanzie
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_studio_bertelli_per_il_debitore.pdf, contenuto pertinente a novazione; term sheet; art. 1232 c.c.

## B.39

- Tipo: presenza
- Issue: I-09
- Verifica: il deliverable indica l'azione: inserire clausola di non novazione.
- Pass (insieme chiuso): afferma: le parti intendono modificare e non novare il finanziamento | conclude: le parti intendono modificare e non novare il finanziamento
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_studio_bertelli_per_il_debitore.pdf, contenuto pertinente a novazione; term sheet; art. 1232 c.c.

## B.40

- Tipo: presenza
- Issue: I-10
- Verifica: il deliverable enuncia il risultato: la fee è dovuta solo alla data di efficacia.
- Pass (insieme chiuso): afferma: la fee è dovuta solo alla data di efficacia | conclude: la fee è dovuta solo alla data di efficacia
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_studio_bertelli_per_il_debitore.pdf, contenuto pertinente a closing; fee letter; checklist

## B.41

- Tipo: attribuzione
- Issue: I-10
- Verifica: il deliverable collega il dato al documento: fee letter.
- Pass (insieme chiuso): cita 05_nota_studio_bertelli_per_il_debitore.pdf, contenuto pertinente a closing | indica come riscontro 05_nota_studio_bertelli_per_il_debitore.pdf, contenuto pertinente a closing
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_studio_bertelli_per_il_debitore.pdf, contenuto pertinente a closing; fee letter; checklist

## B.42

- Tipo: qualificazione
- Issue: I-10
- Verifica: il deliverable espone l'effetto: firma ed efficacia devono restare distinte.
- Pass (insieme chiuso): espone l'effetto: firma ed efficacia devono restare distinte | indica come conseguenza: firma ed efficacia devono restare distinte
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_studio_bertelli_per_il_debitore.pdf, contenuto pertinente a closing; fee letter; checklist

## B.43

- Tipo: presenza
- Issue: I-10
- Verifica: il deliverable indica l'azione: allineare pagamento e notice dell'Agent.
- Pass (insieme chiuso): afferma: la fee è dovuta solo alla data di efficacia | conclude: la fee è dovuta solo alla data di efficacia
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_studio_bertelli_per_il_debitore.pdf, contenuto pertinente a closing; fee letter; checklist

## C.1

- Tipo: assenza
- Issue: N-01
- Verifica: chiusura simmetria sul falso positivo «firma agent»: La sola firma dell'Agent non prova il raggiungimento delle maggioranze intercreditor.
- Pass (insieme chiuso): non qualifica come criticita firma agent | esclude espressamente il falso positivo firma agent
- Fail: compare la conclusione vietata «firma agent costituisce una criticita autonoma»
- Fonte: challenge_map.json; documenti pubblici

## C.2

- Tipo: assenza
- Issue: N-02
- Verifica: chiusura sovra-segnalazione sul falso positivo «importo ipoteca»: Il massimale ipotecario non coincide automaticamente con la copertura economica disponibile.
- Pass (insieme chiuso): non qualifica come criticita importo ipoteca | esclude espressamente il falso positivo importo ipoteca
- Fail: compare la conclusione vietata «importo ipoteca costituisce una criticita autonoma»
- Fonte: challenge_map.json; documenti pubblici

## C.3

- Tipo: assenza
- Issue: N-03
- Verifica: chiusura presunzione sul falso positivo «circolazione bozza»: La circolazione della bozza non fa maturare la fee collegata all'efficacia.
- Pass (insieme chiuso): non qualifica come criticita circolazione bozza | esclude espressamente il falso positivo circolazione bozza
- Fail: compare la conclusione vietata «circolazione bozza costituisce una criticita autonoma»
- Fonte: challenge_map.json; documenti pubblici
