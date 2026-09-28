# WF2-073 - Criteri atomizzati

Ogni riga valuta un solo fatto, valore, collegamento probatorio, effetto o azione.

## A.1

- Tipo: struttura
- Issue: A
- Verifica: la consegna usa i file cross_border_investigation_memo.md.
- Pass (insieme chiuso): i nomi dei file coincidono con cross_border_investigation_memo.md | il controllo deterministico sul requisito restituisce esito positivo
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
- Verifica: il deliverable enuncia il risultato: l'identità della segnalante è contenuta solo nell'allegato cifrato del canale.
- Pass (insieme chiuso): afferma: l'identità della segnalante è contenuta solo nell'allegato cifrato del canale | conclude: l'identità della segnalante è contenuta solo nell'allegato cifrato del canale
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_registro_canale_wb_2029_44.pdf, contenuto pertinente a segnalante; D.Lgs. 24/2023; registro canale

## B.2

- Tipo: attribuzione
- Issue: I-01
- Verifica: il deliverable collega il dato al documento: registro del canale interno.
- Pass (insieme chiuso): cita 01_registro_canale_wb_2029_44.pdf, contenuto pertinente a segnalante | indica come riscontro 01_registro_canale_wb_2029_44.pdf, contenuto pertinente a segnalante
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_registro_canale_wb_2029_44.pdf, contenuto pertinente a segnalante; D.Lgs. 24/2023; registro canale

## B.3

- Tipo: qualificazione
- Issue: I-01
- Verifica: il deliverable espone l'effetto: l'accesso va limitato al team autorizzato.
- Pass (insieme chiuso): espone l'effetto: l'accesso va limitato al team autorizzato | indica come conseguenza: l'accesso va limitato al team autorizzato
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_registro_canale_wb_2029_44.pdf, contenuto pertinente a segnalante; D.Lgs. 24/2023; registro canale

## B.4

- Tipo: presenza
- Issue: I-01
- Verifica: il deliverable indica l'azione: separare identità e contenuto investigativo.
- Pass (insieme chiuso): afferma: l'identità della segnalante è contenuta solo nell'allegato cifrato del canale | conclude: l'identità della segnalante è contenuta solo nell'allegato cifrato del canale
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_registro_canale_wb_2029_44.pdf, contenuto pertinente a segnalante; D.Lgs. 24/2023; registro canale

## B.5

- Tipo: qualificazione
- Issue: I-01
- Verifica: il deliverable tratta la lacuna come dato mancante: manca il consenso alla divulgazione.
- Pass (insieme chiuso): espone l'effetto: l'accesso va limitato al team autorizzato | indica come conseguenza: l'accesso va limitato al team autorizzato
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_registro_canale_wb_2029_44.pdf, contenuto pertinente a segnalante; D.Lgs. 24/2023; registro canale

## B.6

- Tipo: valore
- Issue: I-02
- Verifica: il deliverable riporta il valore documentato per ritorsione.
- Pass (insieme chiuso): compare «tre giorni» | compare «3 giorni»
- Fail: non compare ne «tre giorni» ne «3 giorni» oppure compare un valore incompatibile
- Fonte: 01_registro_canale_wb_2029_44.pdf, contenuto pertinente a ritorsione; report HR; D.Lgs. 24/2023

## B.7

- Tipo: attribuzione
- Issue: I-02
- Verifica: il deliverable collega il dato al documento: report HR e timestamp del canale.
- Pass (insieme chiuso): cita 01_registro_canale_wb_2029_44.pdf, contenuto pertinente a ritorsione | indica come riscontro 01_registro_canale_wb_2029_44.pdf, contenuto pertinente a ritorsione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_registro_canale_wb_2029_44.pdf, contenuto pertinente a ritorsione; report HR; D.Lgs. 24/2023

## B.8

- Tipo: qualificazione
- Issue: I-02
- Verifica: il deliverable espone l'effetto: la prossimità temporale impone una verifica autonoma.
- Pass (insieme chiuso): espone l'effetto: la prossimità temporale impone una verifica autonoma | indica come conseguenza: la prossimità temporale impone una verifica autonoma
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_registro_canale_wb_2029_44.pdf, contenuto pertinente a ritorsione; report HR; D.Lgs. 24/2023

## B.9

- Tipo: presenza
- Issue: I-02
- Verifica: il deliverable riporta il valore documentato per ritorsione.
- Pass (insieme chiuso): afferma: il blocco del bonus della segnalante è successivo di tre giorni alla segnalazione | conclude: il blocco del bonus della segnalante è successivo di tre giorni alla segnalazione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_registro_canale_wb_2029_44.pdf, contenuto pertinente a ritorsione; report HR; D.Lgs. 24/2023

## B.10

- Tipo: qualificazione
- Issue: I-02
- Verifica: il deliverable tratta la lacuna come dato mancante: manca la motivazione anteriore del responsabile.
- Pass (insieme chiuso): espone l'effetto: la prossimità temporale impone una verifica autonoma | indica come conseguenza: la prossimità temporale impone una verifica autonoma
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_registro_canale_wb_2029_44.pdf, contenuto pertinente a ritorsione; report HR; D.Lgs. 24/2023

## B.11

- Tipo: presenza
- Issue: I-03
- Verifica: il deliverable enuncia il risultato: tre fatture di consulenza coincidono con pagamenti verso un subagente non dichiarato.
- Pass (insieme chiuso): afferma: tre fatture di consulenza coincidono con pagamenti verso un subagente non dichiarato | conclude: tre fatture di consulenza coincidono con pagamenti verso un subagente non dichiarato
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_istruttorio_kestrel.xlsx, contenuto pertinente a flusso sospetto; mastro; questionario due diligence

## B.12

- Tipo: attribuzione
- Issue: I-03
- Verifica: il deliverable collega il dato al documento: mastro fornitori e bonifici.
- Pass (insieme chiuso): cita 02_registro_istruttorio_kestrel.xlsx, contenuto pertinente a flusso sospetto | indica come riscontro 02_registro_istruttorio_kestrel.xlsx, contenuto pertinente a flusso sospetto
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_istruttorio_kestrel.xlsx, contenuto pertinente a flusso sospetto; mastro; questionario due diligence

## B.13

- Tipo: qualificazione
- Issue: I-03
- Verifica: il deliverable espone l'effetto: il conflitto fra questionario e contabilità richiede tracciamento dei beneficiari.
- Pass (insieme chiuso): espone l'effetto: il conflitto fra questionario e contabilità richiede tracciamento dei beneficiari | indica come conseguenza: il conflitto fra questionario e contabilità richiede tracciamento dei beneficiari
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_istruttorio_kestrel.xlsx, contenuto pertinente a flusso sospetto; mastro; questionario due diligence

## B.14

- Tipo: presenza
- Issue: I-03
- Verifica: il deliverable indica l'azione: acquisire contratti, conti e deliverable.
- Pass (insieme chiuso): afferma: tre fatture di consulenza coincidono con pagamenti verso un subagente non dichiarato | conclude: tre fatture di consulenza coincidono con pagamenti verso un subagente non dichiarato
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_istruttorio_kestrel.xlsx, contenuto pertinente a flusso sospetto; mastro; questionario due diligence

## B.15

- Tipo: qualificazione
- Issue: I-03
- Verifica: il deliverable tratta la lacuna come dato mancante: manca la titolarità effettiva del subagente.
- Pass (insieme chiuso): espone l'effetto: il conflitto fra questionario e contabilità richiede tracciamento dei beneficiari | indica come conseguenza: il conflitto fra questionario e contabilità richiede tracciamento dei beneficiari
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_istruttorio_kestrel.xlsx, contenuto pertinente a flusso sospetto; mastro; questionario due diligence

## B.16

- Tipo: presenza
- Issue: I-04
- Verifica: il deliverable enuncia il risultato: le interviste dirette dallo studio esterno sono separate dai colloqui HR.
- Pass (insieme chiuso): afferma: le interviste dirette dallo studio esterno sono separate dai colloqui HR | conclude: le interviste dirette dallo studio esterno sono separate dai colloqui HR
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_istruttorio_kestrel.xlsx, contenuto pertinente a privilegio esterno; lettera d'incarico; protocollo

## B.17

- Tipo: attribuzione
- Issue: I-04
- Verifica: il deliverable collega il dato al documento: lettera d'incarico e protocollo interviste.
- Pass (insieme chiuso): cita 02_registro_istruttorio_kestrel.xlsx, contenuto pertinente a privilegio esterno | indica come riscontro 02_registro_istruttorio_kestrel.xlsx, contenuto pertinente a privilegio esterno
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_istruttorio_kestrel.xlsx, contenuto pertinente a privilegio esterno; lettera d'incarico; protocollo

## B.18

- Tipo: qualificazione
- Issue: I-04
- Verifica: il deliverable espone l'effetto: la segregazione sostiene la rivendicazione di riservatezza difensiva.
- Pass (insieme chiuso): espone l'effetto: la segregazione sostiene la rivendicazione di riservatezza difensiva | indica come conseguenza: la segregazione sostiene la rivendicazione di riservatezza difensiva
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_istruttorio_kestrel.xlsx, contenuto pertinente a privilegio esterno; lettera d'incarico; protocollo

## B.19

- Tipo: presenza
- Issue: I-04
- Verifica: il deliverable indica l'azione: marcare e custodire separatamente i work product.
- Pass (insieme chiuso): afferma: le interviste dirette dallo studio esterno sono separate dai colloqui HR | conclude: le interviste dirette dallo studio esterno sono separate dai colloqui HR
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_istruttorio_kestrel.xlsx, contenuto pertinente a privilegio esterno; lettera d'incarico; protocollo

## B.20

- Tipo: qualificazione
- Issue: I-04
- Verifica: il deliverable tratta la lacuna come dato mancante: manca una valutazione per ciascun documento.
- Pass (insieme chiuso): espone l'effetto: la segregazione sostiene la rivendicazione di riservatezza difensiva | indica come conseguenza: la segregazione sostiene la rivendicazione di riservatezza difensiva
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_istruttorio_kestrel.xlsx, contenuto pertinente a privilegio esterno; lettera d'incarico; protocollo

## B.21

- Tipo: presenza
- Issue: I-05
- Verifica: il deliverable enuncia il risultato: l'email del legale interno contiene anche istruzioni commerciali.
- Pass (insieme chiuso): afferma: l'email del legale interno contiene anche istruzioni commerciali | conclude: l'email del legale interno contiene anche istruzioni commerciali
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_fermo_conservativo_mailbox.eml, contenuto pertinente a legale interno; email; disciplina applicabile al contesto

## B.22

- Tipo: attribuzione
- Issue: I-05
- Verifica: il deliverable collega il dato al documento: email del 22 ottobre 2029.
- Pass (insieme chiuso): cita 03_email_fermo_conservativo_mailbox.eml, contenuto pertinente a legale interno | indica come riscontro 03_email_fermo_conservativo_mailbox.eml, contenuto pertinente a legale interno
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_fermo_conservativo_mailbox.eml, contenuto pertinente a legale interno; email; disciplina applicabile al contesto

## B.23

- Tipo: qualificazione
- Issue: I-05
- Verifica: il deliverable espone l'effetto: il solo mittente non consente una rivendicazione indiscriminata.
- Pass (insieme chiuso): espone l'effetto: il solo mittente non consente una rivendicazione indiscriminata | indica come conseguenza: il solo mittente non consente una rivendicazione indiscriminata
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_fermo_conservativo_mailbox.eml, contenuto pertinente a legale interno; email; disciplina applicabile al contesto

## B.24

- Tipo: presenza
- Issue: I-05
- Verifica: il deliverable indica l'azione: separare consulenza legale e contenuto operativo.
- Pass (insieme chiuso): afferma: l'email del legale interno contiene anche istruzioni commerciali | conclude: l'email del legale interno contiene anche istruzioni commerciali
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_fermo_conservativo_mailbox.eml, contenuto pertinente a legale interno; email; disciplina applicabile al contesto

## B.25

- Tipo: qualificazione
- Issue: I-05
- Verifica: il deliverable tratta la lacuna come dato mancante: manca il thread precedente.
- Pass (insieme chiuso): espone l'effetto: il solo mittente non consente una rivendicazione indiscriminata | indica come conseguenza: il solo mittente non consente una rivendicazione indiscriminata
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_fermo_conservativo_mailbox.eml, contenuto pertinente a legale interno; email; disciplina applicabile al contesto

## B.26

- Tipo: presenza
- Issue: I-06
- Verifica: il deliverable enuncia il risultato: il legal hold del 24 ottobre copre mailbox ma non telefoni aziendali.
- Pass (insieme chiuso): afferma: il legal hold del 24 ottobre copre mailbox ma non telefoni aziendali | conclude: il legal hold del 24 ottobre copre mailbox ma non telefoni aziendali
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_fermo_conservativo_mailbox.eml, contenuto pertinente a legal hold; legal hold; art. 5 GDPR

## B.27

- Tipo: attribuzione
- Issue: I-06
- Verifica: il deliverable collega il dato al documento: avviso di conservazione.
- Pass (insieme chiuso): cita 03_email_fermo_conservativo_mailbox.eml, contenuto pertinente a legal hold | indica come riscontro 03_email_fermo_conservativo_mailbox.eml, contenuto pertinente a legal hold
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_fermo_conservativo_mailbox.eml, contenuto pertinente a legal hold; legal hold; art. 5 GDPR

## B.28

- Tipo: qualificazione
- Issue: I-06
- Verifica: il deliverable espone l'effetto: la conservazione è incompleta per i messaggi mobili indicati nella segnalazione.
- Pass (insieme chiuso): espone l'effetto: la conservazione è incompleta per i messaggi mobili indicati nella segnalazione | indica come conseguenza: la conservazione è incompleta per i messaggi mobili indicati nella segnalazione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_fermo_conservativo_mailbox.eml, contenuto pertinente a legal hold; legal hold; art. 5 GDPR

## B.29

- Tipo: presenza
- Issue: I-06
- Verifica: il deliverable indica l'azione: estendere il hold a telefoni, chat e backup.
- Pass (insieme chiuso): afferma: il legal hold del 24 ottobre copre mailbox ma non telefoni aziendali | conclude: il legal hold del 24 ottobre copre mailbox ma non telefoni aziendali
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_fermo_conservativo_mailbox.eml, contenuto pertinente a legal hold; legal hold; art. 5 GDPR

## B.30

- Tipo: presenza
- Issue: I-07
- Verifica: il deliverable enuncia il risultato: l'esportazione del portatile non registra hash né operatore.
- Pass (insieme chiuso): afferma: l'esportazione del portatile non registra hash né operatore | conclude: l'esportazione del portatile non registra hash né operatore
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_verbale_acquisizione_forense.pdf, contenuto pertinente a catena di custodia; verbale forense

## B.31

- Tipo: attribuzione
- Issue: I-07
- Verifica: il deliverable collega il dato al documento: verbale forense del 29 ottobre.
- Pass (insieme chiuso): cita 04_verbale_acquisizione_forense.pdf, contenuto pertinente a catena di custodia | indica come riscontro 04_verbale_acquisizione_forense.pdf, contenuto pertinente a catena di custodia
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_verbale_acquisizione_forense.pdf, contenuto pertinente a catena di custodia; verbale forense

## B.32

- Tipo: qualificazione
- Issue: I-07
- Verifica: il deliverable espone l'effetto: l'autenticità della copia resta contestabile.
- Pass (insieme chiuso): espone l'effetto: l'autenticità della copia resta contestabile | indica come conseguenza: l'autenticità della copia resta contestabile
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_verbale_acquisizione_forense.pdf, contenuto pertinente a catena di custodia; verbale forense

## B.33

- Tipo: presenza
- Issue: I-07
- Verifica: il deliverable indica l'azione: ripetere l'acquisizione con hash e registro.
- Pass (insieme chiuso): afferma: l'esportazione del portatile non registra hash né operatore | conclude: l'esportazione del portatile non registra hash né operatore
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_verbale_acquisizione_forense.pdf, contenuto pertinente a catena di custodia; verbale forense

## B.34

- Tipo: presenza
- Issue: I-08
- Verifica: il deliverable enuncia il risultato: il dataset include dati sanitari estranei all'ipotesi investigativa.
- Pass (insieme chiuso): afferma: il dataset include dati sanitari estranei all'ipotesi investigativa | conclude: il dataset include dati sanitari estranei all'ipotesi investigativa
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_verbale_acquisizione_forense.pdf, contenuto pertinente a base giuridica; artt. 5, 6 e 9 GDPR

## B.35

- Tipo: attribuzione
- Issue: I-08
- Verifica: il deliverable collega il dato al documento: indice dei file esportati.
- Pass (insieme chiuso): cita 04_verbale_acquisizione_forense.pdf, contenuto pertinente a base giuridica | indica come riscontro 04_verbale_acquisizione_forense.pdf, contenuto pertinente a base giuridica
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_verbale_acquisizione_forense.pdf, contenuto pertinente a base giuridica; artt. 5, 6 e 9 GDPR

## B.36

- Tipo: qualificazione
- Issue: I-08
- Verifica: il deliverable espone l'effetto: la raccolta richiede minimizzazione e una base distinta per le categorie particolari.
- Pass (insieme chiuso): espone l'effetto: la raccolta richiede minimizzazione e una base distinta per le categorie particolari | indica come conseguenza: la raccolta richiede minimizzazione e una base distinta per le categorie particolari
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_verbale_acquisizione_forense.pdf, contenuto pertinente a base giuridica; artt. 5, 6 e 9 GDPR

## B.37

- Tipo: presenza
- Issue: I-08
- Verifica: il deliverable indica l'azione: escludere o isolare i file sanitari.
- Pass (insieme chiuso): afferma: il dataset include dati sanitari estranei all'ipotesi investigativa | conclude: il dataset include dati sanitari estranei all'ipotesi investigativa
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_verbale_acquisizione_forense.pdf, contenuto pertinente a base giuridica; artt. 5, 6 e 9 GDPR

## B.38

- Tipo: presenza
- Issue: I-09
- Verifica: il deliverable enuncia il risultato: il caricamento verso la capogruppo statunitense è iniziato prima della firma delle SCC.
- Pass (insieme chiuso): afferma: il caricamento verso la capogruppo statunitense è iniziato prima della firma delle SCC | conclude: il caricamento verso la capogruppo statunitense è iniziato prima della firma delle SCC
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_ufficio_privacy_trasferimenti.pdf, contenuto pertinente a trasferimento usa; artt. 44-49 GDPR; log

## B.39

- Tipo: attribuzione
- Issue: I-09
- Verifica: il deliverable collega il dato al documento: log di esportazione e data package SCC.
- Pass (insieme chiuso): cita 05_nota_ufficio_privacy_trasferimenti.pdf, contenuto pertinente a trasferimento usa | indica come riscontro 05_nota_ufficio_privacy_trasferimenti.pdf, contenuto pertinente a trasferimento usa
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_ufficio_privacy_trasferimenti.pdf, contenuto pertinente a trasferimento usa; artt. 44-49 GDPR; log

## B.40

- Tipo: qualificazione
- Issue: I-09
- Verifica: il deliverable espone l'effetto: il trasferimento va sospeso e ricostruito.
- Pass (insieme chiuso): espone l'effetto: il trasferimento va sospeso e ricostruito | indica come conseguenza: il trasferimento va sospeso e ricostruito
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_ufficio_privacy_trasferimenti.pdf, contenuto pertinente a trasferimento usa; artt. 44-49 GDPR; log

## B.41

- Tipo: presenza
- Issue: I-09
- Verifica: il deliverable indica l'azione: chiudere SCC, valutazione del trasferimento e misure supplementari.
- Pass (insieme chiuso): afferma: il caricamento verso la capogruppo statunitense è iniziato prima della firma delle SCC | conclude: il caricamento verso la capogruppo statunitense è iniziato prima della firma delle SCC
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_ufficio_privacy_trasferimenti.pdf, contenuto pertinente a trasferimento usa; artt. 44-49 GDPR; log

## B.42

- Tipo: presenza
- Issue: I-10
- Verifica: il deliverable enuncia il risultato: l'accesso del consulente di Singapore è un trasferimento ulteriore distinto.
- Pass (insieme chiuso): afferma: l'accesso del consulente di Singapore è un trasferimento ulteriore distinto | conclude: l'accesso del consulente di Singapore è un trasferimento ulteriore distinto
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_ufficio_privacy_trasferimenti.pdf, contenuto pertinente a onward transfer singapore; artt. 44-49 GDPR; ACL

## B.43

- Tipo: attribuzione
- Issue: I-10
- Verifica: il deliverable collega il dato al documento: ACL della data room.
- Pass (insieme chiuso): cita 05_nota_ufficio_privacy_trasferimenti.pdf, contenuto pertinente a onward transfer singapore | indica come riscontro 05_nota_ufficio_privacy_trasferimenti.pdf, contenuto pertinente a onward transfer singapore
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_ufficio_privacy_trasferimenti.pdf, contenuto pertinente a onward transfer singapore; artt. 44-49 GDPR; ACL

## B.44

- Tipo: qualificazione
- Issue: I-10
- Verifica: il deliverable espone l'effetto: serve una base del capo V riferita anche a quell'accesso.
- Pass (insieme chiuso): espone l'effetto: serve una base del capo V riferita anche a quell'accesso | indica come conseguenza: serve una base del capo V riferita anche a quell'accesso
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_ufficio_privacy_trasferimenti.pdf, contenuto pertinente a onward transfer singapore; artt. 44-49 GDPR; ACL

## B.45

- Tipo: presenza
- Issue: I-10
- Verifica: il deliverable indica l'azione: revocare l'accesso finché la catena non è documentata.
- Pass (insieme chiuso): afferma: l'accesso del consulente di Singapore è un trasferimento ulteriore distinto | conclude: l'accesso del consulente di Singapore è un trasferimento ulteriore distinto
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_ufficio_privacy_trasferimenti.pdf, contenuto pertinente a onward transfer singapore; artt. 44-49 GDPR; ACL

## C.1

- Tipo: assenza
- Issue: N-01
- Verifica: chiusura simmetria sul falso positivo «pseudonimo contabile»: Il codice usato nel mastro non coincide con l'identità protetta della segnalante.
- Pass (insieme chiuso): non qualifica come criticita pseudonimo contabile | esclude espressamente il falso positivo pseudonimo contabile
- Fail: compare la conclusione vietata «pseudonimo contabile costituisce una criticita autonoma»
- Fonte: challenge_map.json; documenti pubblici

## C.2

- Tipo: assenza
- Issue: N-02
- Verifica: chiusura sovra-segnalazione sul falso positivo «link scaduto»: La scadenza del link di caricamento non prova la cancellazione dei file già acquisiti.
- Pass (insieme chiuso): non qualifica come criticita link scaduto | esclude espressamente il falso positivo link scaduto
- Fail: compare la conclusione vietata «link scaduto costituisce una criticita autonoma»
- Fonte: challenge_map.json; documenti pubblici

## C.3

- Tipo: assenza
- Issue: N-03
- Verifica: chiusura presunzione sul falso positivo «importi arrotondati»: L'arrotondamento degli importi nel report non dimostra da solo una manipolazione contabile.
- Pass (insieme chiuso): non qualifica come criticita importi arrotondati | esclude espressamente il falso positivo importi arrotondati
- Fail: compare la conclusione vietata «importi arrotondati costituisce una criticita autonoma»
- Fonte: challenge_map.json; documenti pubblici
