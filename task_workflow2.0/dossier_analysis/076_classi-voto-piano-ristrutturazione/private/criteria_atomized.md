# WF2-076 - Criteri atomizzati

Ogni riga valuta un solo fatto, valore, collegamento probatorio, effetto o azione.

## A.1

- Tipo: struttura
- Issue: A
- Verifica: la consegna usa i file class_and_vote_matrix.md.
- Pass (insieme chiuso): i nomi dei file coincidono con class_and_vote_matrix.md | il controllo deterministico sul requisito restituisce esito positivo
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
- Verifica: il deliverable enuncia il risultato: la bozza dichiara un piano di ristrutturazione soggetto a omologazione.
- Pass (insieme chiuso): afferma: la bozza dichiara un piano di ristrutturazione soggetto a omologazione | conclude: la bozza dichiara un piano di ristrutturazione soggetto a omologazione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_term_sheet_piano_ristrutturazione.pdf, contenuto pertinente a strumento; art. 64-bis CCII

## B.2

- Tipo: attribuzione
- Issue: I-01
- Verifica: il deliverable collega il dato al documento: term sheet del 3 settembre.
- Pass (insieme chiuso): cita 01_term_sheet_piano_ristrutturazione.pdf, contenuto pertinente a strumento | indica come riscontro 01_term_sheet_piano_ristrutturazione.pdf, contenuto pertinente a strumento
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_term_sheet_piano_ristrutturazione.pdf, contenuto pertinente a strumento; art. 64-bis CCII

## B.3

- Tipo: qualificazione
- Issue: I-01
- Verifica: il deliverable espone l'effetto: il test di approvazione richiede il voto favorevole di tutte le classi.
- Pass (insieme chiuso): espone l'effetto: il test di approvazione richiede il voto favorevole di tutte le classi | indica come conseguenza: il test di approvazione richiede il voto favorevole di tutte le classi
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_term_sheet_piano_ristrutturazione.pdf, contenuto pertinente a strumento; art. 64-bis CCII

## B.4

- Tipo: presenza
- Issue: I-01
- Verifica: il deliverable indica l'azione: mantenere distinto il percorso alternativo di concordato.
- Pass (insieme chiuso): afferma: la bozza dichiara un piano di ristrutturazione soggetto a omologazione | conclude: la bozza dichiara un piano di ristrutturazione soggetto a omologazione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_term_sheet_piano_ristrutturazione.pdf, contenuto pertinente a strumento; art. 64-bis CCII

## B.5

- Tipo: qualificazione
- Issue: I-01
- Verifica: il deliverable tratta la lacuna come dato mancante: manca la versione definitiva della proposta.
- Pass (insieme chiuso): espone l'effetto: il test di approvazione richiede il voto favorevole di tutte le classi | indica come conseguenza: il test di approvazione richiede il voto favorevole di tutte le classi
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_term_sheet_piano_ristrutturazione.pdf, contenuto pertinente a strumento; art. 64-bis CCII

## B.6

- Tipo: assenza
- Issue: I-01
- Verifica: il deliverable esclude la conclusione bersaglio: applicare automaticamente la maggioranza per classi del concordato.
- Pass (insieme chiuso): indica l'azione: mantenere distinto il percorso alternativo di concordato | propone: mantenere distinto il percorso alternativo di concordato
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_term_sheet_piano_ristrutturazione.pdf, contenuto pertinente a strumento; art. 64-bis CCII

## B.7

- Tipo: attribuzione
- Issue: I-01
- Verifica: il deliverable usa la fonte indicata: art. 64-bis CCII.
- Pass (insieme chiuso): cita 01_term_sheet_piano_ristrutturazione.pdf, contenuto pertinente a strumento | indica come riscontro 01_term_sheet_piano_ristrutturazione.pdf, contenuto pertinente a strumento
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_term_sheet_piano_ristrutturazione.pdf, contenuto pertinente a strumento; art. 64-bis CCII

## B.8

- Tipo: presenza
- Issue: I-02
- Verifica: il deliverable enuncia il risultato: la classe A comprende banca ipotecaria per la parte capiente e chirografaria per l'incapienza.
- Pass (insieme chiuso): afferma: la classe A comprende banca ipotecaria per la parte capiente e chirografaria per l'incapienza | conclude: la classe A comprende banca ipotecaria per la parte capiente e chirografaria per l'incapienza
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_term_sheet_piano_ristrutturazione.pdf, contenuto pertinente a ipotecari; artt. 64-bis e 85 CCII

## B.9

- Tipo: attribuzione
- Issue: I-02
- Verifica: il deliverable collega il dato al documento: perizia immobile e piano.
- Pass (insieme chiuso): cita 01_term_sheet_piano_ristrutturazione.pdf, contenuto pertinente a ipotecari | indica come riscontro 01_term_sheet_piano_ristrutturazione.pdf, contenuto pertinente a ipotecari
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_term_sheet_piano_ristrutturazione.pdf, contenuto pertinente a ipotecari; artt. 64-bis e 85 CCII

## B.10

- Tipo: qualificazione
- Issue: I-02
- Verifica: il deliverable espone l'effetto: le due porzioni hanno posizione giuridica diversa.
- Pass (insieme chiuso): espone l'effetto: le due porzioni hanno posizione giuridica diversa | indica come conseguenza: le due porzioni hanno posizione giuridica diversa
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_term_sheet_piano_ristrutturazione.pdf, contenuto pertinente a ipotecari; artt. 64-bis e 85 CCII

## B.11

- Tipo: presenza
- Issue: I-02
- Verifica: il deliverable indica l'azione: separare esposizione e trattamento.
- Pass (insieme chiuso): afferma: la classe A comprende banca ipotecaria per la parte capiente e chirografaria per l'incapienza | conclude: la classe A comprende banca ipotecaria per la parte capiente e chirografaria per l'incapienza
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_term_sheet_piano_ristrutturazione.pdf, contenuto pertinente a ipotecari; artt. 64-bis e 85 CCII

## B.12

- Tipo: qualificazione
- Issue: I-02
- Verifica: il deliverable tratta la lacuna come dato mancante: manca il valore di liquidazione definitivo.
- Pass (insieme chiuso): espone l'effetto: le due porzioni hanno posizione giuridica diversa | indica come conseguenza: le due porzioni hanno posizione giuridica diversa
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_term_sheet_piano_ristrutturazione.pdf, contenuto pertinente a ipotecari; artt. 64-bis e 85 CCII

## B.13

- Tipo: assenza
- Issue: I-02
- Verifica: il deliverable esclude la conclusione bersaglio: collocare tutto il credito in una sola classe.
- Pass (insieme chiuso): indica l'azione: separare esposizione e trattamento | propone: separare esposizione e trattamento
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_term_sheet_piano_ristrutturazione.pdf, contenuto pertinente a ipotecari; artt. 64-bis e 85 CCII

## B.14

- Tipo: attribuzione
- Issue: I-02
- Verifica: il deliverable usa la fonte indicata: artt. 64-bis e 85 CCII.
- Pass (insieme chiuso): cita 01_term_sheet_piano_ristrutturazione.pdf, contenuto pertinente a ipotecari | indica come riscontro 01_term_sheet_piano_ristrutturazione.pdf, contenuto pertinente a ipotecari
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_term_sheet_piano_ristrutturazione.pdf, contenuto pertinente a ipotecari; artt. 64-bis e 85 CCII

## B.15

- Tipo: presenza
- Issue: I-03
- Verifica: il deliverable enuncia il risultato: IVA e ritenute sono inserite nella stessa classe dei fornitori.
- Pass (insieme chiuso): afferma: IVA e ritenute sono inserite nella stessa classe dei fornitori | conclude: IVA e ritenute sono inserite nella stessa classe dei fornitori
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_elenco_creditori_riconciliato.xlsx, contenuto pertinente a erario; artt. 85 e 88 CCII

## B.16

- Tipo: attribuzione
- Issue: I-03
- Verifica: il deliverable collega il dato al documento: matrice proposta.
- Pass (insieme chiuso): cita 02_elenco_creditori_riconciliato.xlsx, contenuto pertinente a erario | indica come riscontro 02_elenco_creditori_riconciliato.xlsx, contenuto pertinente a erario
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_elenco_creditori_riconciliato.xlsx, contenuto pertinente a erario; artt. 85 e 88 CCII

## B.17

- Tipo: qualificazione
- Issue: I-03
- Verifica: il deliverable espone l'effetto: la posizione pubblicistica e il trattamento proposto richiedono verifica separata.
- Pass (insieme chiuso): espone l'effetto: la posizione pubblicistica e il trattamento proposto richiedono verifica separata | indica come conseguenza: la posizione pubblicistica e il trattamento proposto richiedono verifica separata
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_elenco_creditori_riconciliato.xlsx, contenuto pertinente a erario; artt. 85 e 88 CCII

## B.18

- Tipo: presenza
- Issue: I-03
- Verifica: il deliverable indica l'azione: creare classe autonoma e quantificare voto.
- Pass (insieme chiuso): afferma: IVA e ritenute sono inserite nella stessa classe dei fornitori | conclude: IVA e ritenute sono inserite nella stessa classe dei fornitori
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_elenco_creditori_riconciliato.xlsx, contenuto pertinente a erario; artt. 85 e 88 CCII

## B.19

- Tipo: qualificazione
- Issue: I-03
- Verifica: il deliverable tratta la lacuna come dato mancante: manca attestazione sul trattamento.
- Pass (insieme chiuso): espone l'effetto: la posizione pubblicistica e il trattamento proposto richiedono verifica separata | indica come conseguenza: la posizione pubblicistica e il trattamento proposto richiedono verifica separata
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_elenco_creditori_riconciliato.xlsx, contenuto pertinente a erario; artt. 85 e 88 CCII

## B.20

- Tipo: assenza
- Issue: I-03
- Verifica: il deliverable esclude la conclusione bersaglio: assimilare il credito fiscale ai trade.
- Pass (insieme chiuso): indica l'azione: creare classe autonoma e quantificare voto | propone: creare classe autonoma e quantificare voto
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_elenco_creditori_riconciliato.xlsx, contenuto pertinente a erario; artt. 85 e 88 CCII

## B.21

- Tipo: attribuzione
- Issue: I-03
- Verifica: il deliverable usa la fonte indicata: artt. 85 e 88 CCII.
- Pass (insieme chiuso): cita 02_elenco_creditori_riconciliato.xlsx, contenuto pertinente a erario | indica come riscontro 02_elenco_creditori_riconciliato.xlsx, contenuto pertinente a erario
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_elenco_creditori_riconciliato.xlsx, contenuto pertinente a erario; artt. 85 e 88 CCII

## B.22

- Tipo: valore
- Issue: I-04
- Verifica: il deliverable riporta il valore documentato per fornitori strategici.
- Pass (insieme chiuso): compare «55 per cento» | compare «55%»
- Fail: non compare ne «55 per cento» ne «55%» oppure compare un valore incompatibile
- Fonte: 03_email_trattamenti_e_classamento.eml, contenuto pertinente a fornitori strategici; art. 85 CCII

## B.23

- Tipo: attribuzione
- Issue: I-04
- Verifica: il deliverable collega il dato al documento: piano industriale e matrice.
- Pass (insieme chiuso): cita 03_email_trattamenti_e_classamento.eml, contenuto pertinente a fornitori strategici | indica come riscontro 03_email_trattamenti_e_classamento.eml, contenuto pertinente a fornitori strategici
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_trattamenti_e_classamento.eml, contenuto pertinente a fornitori strategici; art. 85 CCII

## B.24

- Tipo: qualificazione
- Issue: I-04
- Verifica: il deliverable espone l'effetto: la diversità economica può sostenere classi separate se documentata.
- Pass (insieme chiuso): espone l'effetto: la diversità economica può sostenere classi separate se documentata | indica come conseguenza: la diversità economica può sostenere classi separate se documentata
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_trattamenti_e_classamento.eml, contenuto pertinente a fornitori strategici; art. 85 CCII

## B.25

- Tipo: presenza
- Issue: I-04
- Verifica: il deliverable riporta il valore documentato per fornitori strategici.
- Pass (insieme chiuso): afferma: i fornitori strategici ricevono il 55 per cento e i fornitori ordinari il 28 per cento | conclude: i fornitori strategici ricevono il 55 per cento e i fornitori ordinari il 28 per cento
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_trattamenti_e_classamento.eml, contenuto pertinente a fornitori strategici; art. 85 CCII

## B.26

- Tipo: qualificazione
- Issue: I-04
- Verifica: il deliverable tratta la lacuna come dato mancante: manca l'elenco dei contratti essenziali.
- Pass (insieme chiuso): espone l'effetto: la diversità economica può sostenere classi separate se documentata | indica come conseguenza: la diversità economica può sostenere classi separate se documentata
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_trattamenti_e_classamento.eml, contenuto pertinente a fornitori strategici; art. 85 CCII

## B.27

- Tipo: assenza
- Issue: I-04
- Verifica: il deliverable esclude la conclusione bersaglio: dividere le classi solo per ottenere voti.
- Pass (insieme chiuso): indica l'azione: legare strategicità a continuità e sostituibilità | propone: legare strategicità a continuità e sostituibilità
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_trattamenti_e_classamento.eml, contenuto pertinente a fornitori strategici; art. 85 CCII

## B.28

- Tipo: presenza
- Issue: I-05
- Verifica: il deliverable enuncia il risultato: il credito del socio finanziatore è collocato con le banche chirografarie.
- Pass (insieme chiuso): afferma: il credito del socio finanziatore è collocato con le banche chirografarie | conclude: il credito del socio finanziatore è collocato con le banche chirografarie
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_trattamenti_e_classamento.eml, contenuto pertinente a correlati; art. 85 CCII; elenco

## B.29

- Tipo: attribuzione
- Issue: I-05
- Verifica: il deliverable collega il dato al documento: elenco creditori.
- Pass (insieme chiuso): cita 03_email_trattamenti_e_classamento.eml, contenuto pertinente a correlati | indica come riscontro 03_email_trattamenti_e_classamento.eml, contenuto pertinente a correlati
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_trattamenti_e_classamento.eml, contenuto pertinente a correlati; art. 85 CCII; elenco

## B.30

- Tipo: qualificazione
- Issue: I-05
- Verifica: il deliverable espone l'effetto: il rapporto di correlazione altera l'omogeneità degli interessi.
- Pass (insieme chiuso): espone l'effetto: il rapporto di correlazione altera l'omogeneità degli interessi | indica come conseguenza: il rapporto di correlazione altera l'omogeneità degli interessi
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_trattamenti_e_classamento.eml, contenuto pertinente a correlati; art. 85 CCII; elenco

## B.31

- Tipo: presenza
- Issue: I-05
- Verifica: il deliverable indica l'azione: isolare il socio e verificare postergazione.
- Pass (insieme chiuso): afferma: il credito del socio finanziatore è collocato con le banche chirografarie | conclude: il credito del socio finanziatore è collocato con le banche chirografarie
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_trattamenti_e_classamento.eml, contenuto pertinente a correlati; art. 85 CCII; elenco

## B.32

- Tipo: qualificazione
- Issue: I-05
- Verifica: il deliverable tratta la lacuna come dato mancante: manca la delibera del finanziamento.
- Pass (insieme chiuso): espone l'effetto: il rapporto di correlazione altera l'omogeneità degli interessi | indica come conseguenza: il rapporto di correlazione altera l'omogeneità degli interessi
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_trattamenti_e_classamento.eml, contenuto pertinente a correlati; art. 85 CCII; elenco

## B.33

- Tipo: assenza
- Issue: I-05
- Verifica: il deliverable esclude la conclusione bersaglio: contare il socio come banca indipendente.
- Pass (insieme chiuso): indica l'azione: isolare il socio e verificare postergazione | propone: isolare il socio e verificare postergazione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_trattamenti_e_classamento.eml, contenuto pertinente a correlati; art. 85 CCII; elenco

## B.34

- Tipo: valore
- Issue: I-06
- Verifica: il deliverable riporta il valore documentato per voto per classe.
- Pass (insieme chiuso): compare «62 per cento» | compare «62%»
- Fail: non compare ne «62 per cento» ne «62%» oppure compare un valore incompatibile
- Fonte: 04_relazione_computo_adesioni.pdf, contenuto pertinente a voto per classe; art. 109 CCII

## B.35

- Tipo: attribuzione
- Issue: I-06
- Verifica: il deliverable collega il dato al documento: tabella voti.
- Pass (insieme chiuso): cita 04_relazione_computo_adesioni.pdf, contenuto pertinente a voto per classe | indica come riscontro 04_relazione_computo_adesioni.pdf, contenuto pertinente a voto per classe
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_computo_adesioni.pdf, contenuto pertinente a voto per classe; art. 109 CCII

## B.36

- Tipo: qualificazione
- Issue: I-06
- Verifica: il deliverable espone l'effetto: va verificata anche la regola alternativa dei due terzi dei votanti quando rilevante.
- Pass (insieme chiuso): espone l'effetto: va verificata anche la regola alternativa dei due terzi dei votanti quando rilevante | indica come conseguenza: va verificata anche la regola alternativa dei due terzi dei votanti quando rilevante
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_computo_adesioni.pdf, contenuto pertinente a voto per classe; art. 109 CCII

## B.37

- Tipo: presenza
- Issue: I-06
- Verifica: il deliverable riporta il valore documentato per voto per classe.
- Pass (insieme chiuso): afferma: il foglio calcola il 62 per cento sul totale della classe C | conclude: il foglio calcola il 62 per cento sul totale della classe C
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_computo_adesioni.pdf, contenuto pertinente a voto per classe; art. 109 CCII

## B.38

- Tipo: qualificazione
- Issue: I-06
- Verifica: il deliverable tratta la lacuna come dato mancante: mancano tre schede di voto.
- Pass (insieme chiuso): espone l'effetto: va verificata anche la regola alternativa dei due terzi dei votanti quando rilevante | indica come conseguenza: va verificata anche la regola alternativa dei due terzi dei votanti quando rilevante
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_computo_adesioni.pdf, contenuto pertinente a voto per classe; art. 109 CCII

## B.39

- Tipo: assenza
- Issue: I-06
- Verifica: il deliverable esclude la conclusione bersaglio: usare il numero dei creditori.
- Pass (insieme chiuso): indica l'azione: esporre denominatore, votanti e favorevoli | propone: esporre denominatore, votanti e favorevoli
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_computo_adesioni.pdf, contenuto pertinente a voto per classe; art. 109 CCII

## B.40

- Tipo: valore
- Issue: I-07
- Verifica: il deliverable riporta il valore documentato per classe dissenziente.
- Pass (insieme chiuso): compare «71 per cento» | compare «71%»
- Fail: non compare ne «71 per cento» ne «71%» oppure compare un valore incompatibile
- Fonte: 05_nota_advisor_classi_chirografarie.pdf, contenuto pertinente a classe dissenziente; artt. 64-bis e 112 CCII

## B.41

- Tipo: attribuzione
- Issue: I-07
- Verifica: il deliverable collega il dato al documento: verbale provvisorio.
- Pass (insieme chiuso): cita 05_nota_advisor_classi_chirografarie.pdf, contenuto pertinente a classe dissenziente | indica come riscontro 05_nota_advisor_classi_chirografarie.pdf, contenuto pertinente a classe dissenziente
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_advisor_classi_chirografarie.pdf, contenuto pertinente a classe dissenziente; artt. 64-bis e 112 CCII

## B.42

- Tipo: qualificazione
- Issue: I-07
- Verifica: il deliverable espone l'effetto: il piano non è approvato da tutte le classi.
- Pass (insieme chiuso): espone l'effetto: il piano non è approvato da tutte le classi | indica come conseguenza: il piano non è approvato da tutte le classi
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_advisor_classi_chirografarie.pdf, contenuto pertinente a classe dissenziente; artt. 64-bis e 112 CCII

## B.43

- Tipo: presenza
- Issue: I-07
- Verifica: il deliverable riporta il valore documentato per classe dissenziente.
- Pass (insieme chiuso): afferma: la classe E vota contro con il 71 per cento dei crediti | conclude: la classe E vota contro con il 71 per cento dei crediti
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_advisor_classi_chirografarie.pdf, contenuto pertinente a classe dissenziente; artt. 64-bis e 112 CCII

## B.44

- Tipo: qualificazione
- Issue: I-07
- Verifica: il deliverable tratta la lacuna come dato mancante: manca il voto definitivo.
- Pass (insieme chiuso): espone l'effetto: il piano non è approvato da tutte le classi | indica come conseguenza: il piano non è approvato da tutte le classi
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_advisor_classi_chirografarie.pdf, contenuto pertinente a classe dissenziente; artt. 64-bis e 112 CCII

## B.45

- Tipo: assenza
- Issue: I-07
- Verifica: il deliverable esclude la conclusione bersaglio: ignorare la classe perché di piccolo importo.
- Pass (insieme chiuso): indica l'azione: preparare il test di ristrutturazione trasversale | propone: preparare il test di ristrutturazione trasversale
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_advisor_classi_chirografarie.pdf, contenuto pertinente a classe dissenziente; artt. 64-bis e 112 CCII

## B.46

- Tipo: presenza
- Issue: I-08
- Verifica: il deliverable enuncia il risultato: il piano attribuisce alla classe dissenziente meno della stima di liquidazione allegata.
- Pass (insieme chiuso): afferma: il piano attribuisce alla classe dissenziente meno della stima di liquidazione allegata | conclude: il piano attribuisce alla classe dissenziente meno della stima di liquidazione allegata
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_advisor_classi_chirografarie.pdf, contenuto pertinente a valore di liquidazione; art. 112 CCII

## B.47

- Tipo: attribuzione
- Issue: I-08
- Verifica: il deliverable collega il dato al documento: raffronto perizia e waterfall.
- Pass (insieme chiuso): cita 05_nota_advisor_classi_chirografarie.pdf, contenuto pertinente a valore di liquidazione | indica come riscontro 05_nota_advisor_classi_chirografarie.pdf, contenuto pertinente a valore di liquidazione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_advisor_classi_chirografarie.pdf, contenuto pertinente a valore di liquidazione; art. 112 CCII

## B.48

- Tipo: qualificazione
- Issue: I-08
- Verifica: il deliverable espone l'effetto: il test del miglior soddisfacimento non risulta superato.
- Pass (insieme chiuso): espone l'effetto: il test del miglior soddisfacimento non risulta superato | indica come conseguenza: il test del miglior soddisfacimento non risulta superato
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_advisor_classi_chirografarie.pdf, contenuto pertinente a valore di liquidazione; art. 112 CCII

## B.49

- Tipo: presenza
- Issue: I-08
- Verifica: il deliverable indica l'azione: correggere distribuzione o perizia con attestazione.
- Pass (insieme chiuso): afferma: il piano attribuisce alla classe dissenziente meno della stima di liquidazione allegata | conclude: il piano attribuisce alla classe dissenziente meno della stima di liquidazione allegata
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_advisor_classi_chirografarie.pdf, contenuto pertinente a valore di liquidazione; art. 112 CCII

## B.50

- Tipo: qualificazione
- Issue: I-08
- Verifica: il deliverable tratta la lacuna come dato mancante: mancano costi e tempi di liquidazione.
- Pass (insieme chiuso): espone l'effetto: il test del miglior soddisfacimento non risulta superato | indica come conseguenza: il test del miglior soddisfacimento non risulta superato
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_advisor_classi_chirografarie.pdf, contenuto pertinente a valore di liquidazione; art. 112 CCII

## B.51

- Tipo: assenza
- Issue: I-08
- Verifica: il deliverable esclude la conclusione bersaglio: usare il solo valore contabile.
- Pass (insieme chiuso): indica l'azione: correggere distribuzione o perizia con attestazione | propone: correggere distribuzione o perizia con attestazione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_advisor_classi_chirografarie.pdf, contenuto pertinente a valore di liquidazione; art. 112 CCII

## B.52

- Tipo: valore
- Issue: I-09
- Verifica: il deliverable riporta il valore documentato per priorità.
- Pass (insieme chiuso): compare «900.000 euro» | compare «euro 900.000»
- Fail: non compare ne «900.000 euro» ne «euro 900.000» oppure compare un valore incompatibile
- Fonte: 06_prospetto_ripartizione_valore.xlsx, contenuto pertinente a priorità; art. 112 CCII

## B.53

- Tipo: attribuzione
- Issue: I-09
- Verifica: il deliverable collega il dato al documento: waterfall del piano.
- Pass (insieme chiuso): cita 06_prospetto_ripartizione_valore.xlsx, contenuto pertinente a priorità | indica come riscontro 06_prospetto_ripartizione_valore.xlsx, contenuto pertinente a priorità
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 06_prospetto_ripartizione_valore.xlsx, contenuto pertinente a priorità; art. 112 CCII

## B.54

- Tipo: qualificazione
- Issue: I-09
- Verifica: il deliverable espone l'effetto: serve verificare la regola di priorità applicabile e i consensi.
- Pass (insieme chiuso): espone l'effetto: serve verificare la regola di priorità applicabile e i consensi | indica come conseguenza: serve verificare la regola di priorità applicabile e i consensi
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 06_prospetto_ripartizione_valore.xlsx, contenuto pertinente a priorità; art. 112 CCII

## B.55

- Tipo: presenza
- Issue: I-09
- Verifica: il deliverable riporta il valore documentato per priorità.
- Pass (insieme chiuso): afferma: la waterfall distribuisce 900.000 euro ai soci mentre una classe dissenziente non è pagata integralmente | conclude: la waterfall distribuisce 900.000 euro ai soci mentre una classe dissenziente non è pagata integralmente
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 06_prospetto_ripartizione_valore.xlsx, contenuto pertinente a priorità; art. 112 CCII

## B.56

- Tipo: qualificazione
- Issue: I-09
- Verifica: il deliverable tratta la lacuna come dato mancante: manca una classe favorevole in-the-money.
- Pass (insieme chiuso): espone l'effetto: serve verificare la regola di priorità applicabile e i consensi | indica come conseguenza: serve verificare la regola di priorità applicabile e i consensi
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 06_prospetto_ripartizione_valore.xlsx, contenuto pertinente a priorità; art. 112 CCII

## B.57

- Tipo: assenza
- Issue: I-09
- Verifica: il deliverable esclude la conclusione bersaglio: assumere libertà distributiva assoluta.
- Pass (insieme chiuso): indica l'azione: produrre scenari senza distribuzione ai soci | propone: produrre scenari senza distribuzione ai soci
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 06_prospetto_ripartizione_valore.xlsx, contenuto pertinente a priorità; art. 112 CCII

## B.58

- Tipo: presenza
- Issue: I-10
- Verifica: il deliverable enuncia il risultato: l'aumento di capitale modifica i diritti dei soci senza separare il loro trattamento.
- Pass (insieme chiuso): afferma: l'aumento di capitale modifica i diritti dei soci senza separare il loro trattamento | conclude: l'aumento di capitale modifica i diritti dei soci senza separare il loro trattamento
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 07_verbale_cda_17_settembre.pdf, contenuto pertinente a soci; art. 120-ter CCII

## B.59

- Tipo: attribuzione
- Issue: I-10
- Verifica: il deliverable collega il dato al documento: term sheet equity.
- Pass (insieme chiuso): cita 07_verbale_cda_17_settembre.pdf, contenuto pertinente a soci | indica come riscontro 07_verbale_cda_17_settembre.pdf, contenuto pertinente a soci
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 07_verbale_cda_17_settembre.pdf, contenuto pertinente a soci; art. 120-ter CCII

## B.60

- Tipo: qualificazione
- Issue: I-10
- Verifica: il deliverable espone l'effetto: la posizione dei soci deve entrare nell'analisi delle parti interessate.
- Pass (insieme chiuso): espone l'effetto: la posizione dei soci deve entrare nell'analisi delle parti interessate | indica come conseguenza: la posizione dei soci deve entrare nell'analisi delle parti interessate
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 07_verbale_cda_17_settembre.pdf, contenuto pertinente a soci; art. 120-ter CCII

## B.61

- Tipo: presenza
- Issue: I-10
- Verifica: il deliverable indica l'azione: mappare diritti, valore e voto.
- Pass (insieme chiuso): afferma: l'aumento di capitale modifica i diritti dei soci senza separare il loro trattamento | conclude: l'aumento di capitale modifica i diritti dei soci senza separare il loro trattamento
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 07_verbale_cda_17_settembre.pdf, contenuto pertinente a soci; art. 120-ter CCII

## B.62

- Tipo: qualificazione
- Issue: I-10
- Verifica: il deliverable tratta la lacuna come dato mancante: manca lo statuto vigente.
- Pass (insieme chiuso): espone l'effetto: la posizione dei soci deve entrare nell'analisi delle parti interessate | indica come conseguenza: la posizione dei soci deve entrare nell'analisi delle parti interessate
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 07_verbale_cda_17_settembre.pdf, contenuto pertinente a soci; art. 120-ter CCII

## B.63

- Tipo: assenza
- Issue: I-10
- Verifica: il deliverable esclude la conclusione bersaglio: trattare l'equity come estraneo.
- Pass (insieme chiuso): indica l'azione: mappare diritti, valore e voto | propone: mappare diritti, valore e voto
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 07_verbale_cda_17_settembre.pdf, contenuto pertinente a soci; art. 120-ter CCII

## C.1

- Tipo: assenza
- Issue: N-01
- Verifica: chiusura simmetria sul falso positivo «numero creditori»: Il numero delle teste non sostituisce gli importi ammessi nel test di voto.
- Pass (insieme chiuso): non qualifica come criticita numero creditori | esclude espressamente il falso positivo numero creditori
- Fail: compare la conclusione vietata «numero creditori costituisce una criticita autonoma»
- Fonte: challenge_map.json; documenti pubblici

## C.2

- Tipo: assenza
- Issue: N-02
- Verifica: chiusura sovra-segnalazione sul falso positivo «etichetta strategico»: La sola etichetta strategico non giustifica una classe senza dati di continuità e sostituibilità.
- Pass (insieme chiuso): non qualifica come criticita etichetta strategico | esclude espressamente il falso positivo etichetta strategico
- Fail: compare la conclusione vietata «etichetta strategico costituisce una criticita autonoma»
- Fonte: challenge_map.json; documenti pubblici

## C.3

- Tipo: assenza
- Issue: N-03
- Verifica: chiusura presunzione sul falso positivo «valore contabile»: Il valore contabile dell'immobile non sostituisce lo scenario di liquidazione.
- Pass (insieme chiuso): non qualifica come criticita valore contabile | esclude espressamente il falso positivo valore contabile
- Fail: compare la conclusione vietata «valore contabile costituisce una criticita autonoma»
- Fonte: challenge_map.json; documenti pubblici
