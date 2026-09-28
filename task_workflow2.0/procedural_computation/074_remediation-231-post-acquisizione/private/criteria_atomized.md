# WF2-074 - Criteri atomizzati

Ogni riga valuta un solo fatto, valore, collegamento probatorio, effetto o azione.

## A.1

- Tipo: struttura
- Issue: A
- Verifica: la consegna usa i file remediation_timeline.md.
- Pass (insieme chiuso): i nomi dei file coincidono con remediation_timeline.md | il controllo deterministico sul requisito restituisce esito positivo
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
- Verifica: il deliverable enuncia il risultato: il legal hold del 5 febbraio 2029 non comprende l'account del direttore vendite.
- Pass (insieme chiuso): afferma: il legal hold del 5 febbraio 2029 non comprende l'account del direttore vendite | conclude: il legal hold del 5 febbraio 2029 non comprende l'account del direttore vendite
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_delibera_cda_e_legal_hold.pdf, contenuto pertinente a preservazione; legal hold; art. 6 D.Lgs. 231/2001

## B.2

- Tipo: attribuzione
- Issue: I-01
- Verifica: il deliverable collega il dato al documento: elenco destinatari del legal hold.
- Pass (insieme chiuso): cita 01_delibera_cda_e_legal_hold.pdf, contenuto pertinente a preservazione | indica come riscontro 01_delibera_cda_e_legal_hold.pdf, contenuto pertinente a preservazione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_delibera_cda_e_legal_hold.pdf, contenuto pertinente a preservazione; legal hold; art. 6 D.Lgs. 231/2001

## B.3

- Tipo: qualificazione
- Issue: I-01
- Verifica: il deliverable espone l'effetto: una fonte centrale resta esposta a cancellazione.
- Pass (insieme chiuso): espone l'effetto: una fonte centrale resta esposta a cancellazione | indica come conseguenza: una fonte centrale resta esposta a cancellazione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_delibera_cda_e_legal_hold.pdf, contenuto pertinente a preservazione; legal hold; art. 6 D.Lgs. 231/2001

## B.4

- Tipo: presenza
- Issue: I-01
- Verifica: il deliverable indica l'azione: estendere immediatamente il hold e bloccare l'autodeletion.
- Pass (insieme chiuso): afferma: il legal hold del 5 febbraio 2029 non comprende l'account del direttore vendite | conclude: il legal hold del 5 febbraio 2029 non comprende l'account del direttore vendite
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_delibera_cda_e_legal_hold.pdf, contenuto pertinente a preservazione; legal hold; art. 6 D.Lgs. 231/2001

## B.5

- Tipo: qualificazione
- Issue: I-01
- Verifica: il deliverable tratta la lacuna come dato mancante: manca l'immagine del telefono.
- Pass (insieme chiuso): espone l'effetto: una fonte centrale resta esposta a cancellazione | indica come conseguenza: una fonte centrale resta esposta a cancellazione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_delibera_cda_e_legal_hold.pdf, contenuto pertinente a preservazione; legal hold; art. 6 D.Lgs. 231/2001

## B.6

- Tipo: assenza
- Issue: I-01
- Verifica: il deliverable esclude la conclusione bersaglio: attendere la conclusione delle interviste.
- Pass (insieme chiuso): indica l'azione: estendere immediatamente il hold e bloccare l'autodeletion | propone: estendere immediatamente il hold e bloccare l'autodeletion
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_delibera_cda_e_legal_hold.pdf, contenuto pertinente a preservazione; legal hold; art. 6 D.Lgs. 231/2001

## B.7

- Tipo: attribuzione
- Issue: I-01
- Verifica: il deliverable usa la fonte indicata: legal hold; art. 6 D.Lgs. 231/2001.
- Pass (insieme chiuso): cita 01_delibera_cda_e_legal_hold.pdf, contenuto pertinente a preservazione | indica come riscontro 01_delibera_cda_e_legal_hold.pdf, contenuto pertinente a preservazione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_delibera_cda_e_legal_hold.pdf, contenuto pertinente a preservazione; legal hold; art. 6 D.Lgs. 231/2001

## B.8

- Tipo: presenza
- Issue: I-02
- Verifica: il deliverable enuncia il risultato: l'indagine è affidata al responsabile che approvava gli intermediari.
- Pass (insieme chiuso): afferma: l'indagine è affidata al responsabile che approvava gli intermediari | conclude: l'indagine è affidata al responsabile che approvava gli intermediari
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_delibera_cda_e_legal_hold.pdf, contenuto pertinente a indipendenza; delibera; art. 6 D.Lgs. 231/2001

## B.9

- Tipo: attribuzione
- Issue: I-02
- Verifica: il deliverable collega il dato al documento: delibera del 6 febbraio.
- Pass (insieme chiuso): cita 01_delibera_cda_e_legal_hold.pdf, contenuto pertinente a indipendenza | indica come riscontro 01_delibera_cda_e_legal_hold.pdf, contenuto pertinente a indipendenza
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_delibera_cda_e_legal_hold.pdf, contenuto pertinente a indipendenza; delibera; art. 6 D.Lgs. 231/2001

## B.10

- Tipo: qualificazione
- Issue: I-02
- Verifica: il deliverable espone l'effetto: il mandato presenta un conflitto operativo.
- Pass (insieme chiuso): espone l'effetto: il mandato presenta un conflitto operativo | indica come conseguenza: il mandato presenta un conflitto operativo
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_delibera_cda_e_legal_hold.pdf, contenuto pertinente a indipendenza; delibera; art. 6 D.Lgs. 231/2001

## B.11

- Tipo: presenza
- Issue: I-02
- Verifica: il deliverable indica l'azione: rimettere supervisione al comitato indipendente.
- Pass (insieme chiuso): afferma: l'indagine è affidata al responsabile che approvava gli intermediari | conclude: l'indagine è affidata al responsabile che approvava gli intermediari
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_delibera_cda_e_legal_hold.pdf, contenuto pertinente a indipendenza; delibera; art. 6 D.Lgs. 231/2001

## B.12

- Tipo: qualificazione
- Issue: I-02
- Verifica: il deliverable tratta la lacuna come dato mancante: manca una disclosure del conflitto.
- Pass (insieme chiuso): espone l'effetto: il mandato presenta un conflitto operativo | indica come conseguenza: il mandato presenta un conflitto operativo
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_delibera_cda_e_legal_hold.pdf, contenuto pertinente a indipendenza; delibera; art. 6 D.Lgs. 231/2001

## B.13

- Tipo: assenza
- Issue: I-02
- Verifica: il deliverable esclude la conclusione bersaglio: lasciare invariata la catena di riporto.
- Pass (insieme chiuso): indica l'azione: rimettere supervisione al comitato indipendente | propone: rimettere supervisione al comitato indipendente
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_delibera_cda_e_legal_hold.pdf, contenuto pertinente a indipendenza; delibera; art. 6 D.Lgs. 231/2001

## B.14

- Tipo: attribuzione
- Issue: I-02
- Verifica: il deliverable usa la fonte indicata: delibera; art. 6 D.Lgs. 231/2001.
- Pass (insieme chiuso): cita 01_delibera_cda_e_legal_hold.pdf, contenuto pertinente a indipendenza | indica come riscontro 01_delibera_cda_e_legal_hold.pdf, contenuto pertinente a indipendenza
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_delibera_cda_e_legal_hold.pdf, contenuto pertinente a indipendenza; delibera; art. 6 D.Lgs. 231/2001

## B.15

- Tipo: presenza
- Issue: I-03
- Verifica: il deliverable enuncia il risultato: l'OdV ha ricevuto solo una sintesi priva degli allegati contabili.
- Pass (insieme chiuso): afferma: l'OdV ha ricevuto solo una sintesi priva degli allegati contabili | conclude: l'OdV ha ricevuto solo una sintesi priva degli allegati contabili
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_odv_peverano.xlsx, contenuto pertinente a flussi all'odv; verbale OdV; art. 6 D.Lgs. 231/2001

## B.16

- Tipo: attribuzione
- Issue: I-03
- Verifica: il deliverable collega il dato al documento: verbale OdV dell'8 febbraio.
- Pass (insieme chiuso): cita 02_registro_odv_peverano.xlsx, contenuto pertinente a flussi all'odv | indica come riscontro 02_registro_odv_peverano.xlsx, contenuto pertinente a flussi all'odv
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_odv_peverano.xlsx, contenuto pertinente a flussi all'odv; verbale OdV; art. 6 D.Lgs. 231/2001

## B.17

- Tipo: qualificazione
- Issue: I-03
- Verifica: il deliverable espone l'effetto: la vigilanza non dispone delle evidenze sottostanti.
- Pass (insieme chiuso): espone l'effetto: la vigilanza non dispone delle evidenze sottostanti | indica come conseguenza: la vigilanza non dispone delle evidenze sottostanti
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_odv_peverano.xlsx, contenuto pertinente a flussi all'odv; verbale OdV; art. 6 D.Lgs. 231/2001

## B.18

- Tipo: presenza
- Issue: I-03
- Verifica: il deliverable indica l'azione: aprire accesso controllato al fascicolo.
- Pass (insieme chiuso): afferma: l'OdV ha ricevuto solo una sintesi priva degli allegati contabili | conclude: l'OdV ha ricevuto solo una sintesi priva degli allegati contabili
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_odv_peverano.xlsx, contenuto pertinente a flussi all'odv; verbale OdV; art. 6 D.Lgs. 231/2001

## B.19

- Tipo: qualificazione
- Issue: I-03
- Verifica: il deliverable tratta la lacuna come dato mancante: manca il protocollo dei flussi.
- Pass (insieme chiuso): espone l'effetto: la vigilanza non dispone delle evidenze sottostanti | indica come conseguenza: la vigilanza non dispone delle evidenze sottostanti
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_odv_peverano.xlsx, contenuto pertinente a flussi all'odv; verbale OdV; art. 6 D.Lgs. 231/2001

## B.20

- Tipo: assenza
- Issue: I-03
- Verifica: il deliverable esclude la conclusione bersaglio: rinviare gli allegati al report finale.
- Pass (insieme chiuso): indica l'azione: aprire accesso controllato al fascicolo | propone: aprire accesso controllato al fascicolo
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_odv_peverano.xlsx, contenuto pertinente a flussi all'odv; verbale OdV; art. 6 D.Lgs. 231/2001

## B.21

- Tipo: attribuzione
- Issue: I-03
- Verifica: il deliverable usa la fonte indicata: verbale OdV; art. 6 D.Lgs. 231/2001.
- Pass (insieme chiuso): cita 02_registro_odv_peverano.xlsx, contenuto pertinente a flussi all'odv | indica come riscontro 02_registro_odv_peverano.xlsx, contenuto pertinente a flussi all'odv
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_odv_peverano.xlsx, contenuto pertinente a flussi all'odv; verbale OdV; art. 6 D.Lgs. 231/2001

## B.22

- Tipo: presenza
- Issue: I-04
- Verifica: il deliverable enuncia il risultato: la mappa rischi della target non considera intermediari commerciali esteri.
- Pass (insieme chiuso): afferma: la mappa rischi della target non considera intermediari commerciali esteri | conclude: la mappa rischi della target non considera intermediari commerciali esteri
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_odv_peverano.xlsx, contenuto pertinente a risk assessment; risk assessment; art. 6 D.Lgs. 231/2001

## B.23

- Tipo: attribuzione
- Issue: I-04
- Verifica: il deliverable collega il dato al documento: risk assessment 2027.
- Pass (insieme chiuso): cita 02_registro_odv_peverano.xlsx, contenuto pertinente a risk assessment | indica come riscontro 02_registro_odv_peverano.xlsx, contenuto pertinente a risk assessment
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_odv_peverano.xlsx, contenuto pertinente a risk assessment; risk assessment; art. 6 D.Lgs. 231/2001

## B.24

- Tipo: qualificazione
- Issue: I-04
- Verifica: il deliverable espone l'effetto: il modello non copre il processo da cui nasce la segnalazione.
- Pass (insieme chiuso): espone l'effetto: il modello non copre il processo da cui nasce la segnalazione | indica come conseguenza: il modello non copre il processo da cui nasce la segnalazione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_odv_peverano.xlsx, contenuto pertinente a risk assessment; risk assessment; art. 6 D.Lgs. 231/2001

## B.25

- Tipo: presenza
- Issue: I-04
- Verifica: il deliverable indica l'azione: eseguire gap analysis per processo e paese.
- Pass (insieme chiuso): afferma: la mappa rischi della target non considera intermediari commerciali esteri | conclude: la mappa rischi della target non considera intermediari commerciali esteri
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_odv_peverano.xlsx, contenuto pertinente a risk assessment; risk assessment; art. 6 D.Lgs. 231/2001

## B.26

- Tipo: qualificazione
- Issue: I-04
- Verifica: il deliverable tratta la lacuna come dato mancante: manca il censimento degli agenti.
- Pass (insieme chiuso): espone l'effetto: il modello non copre il processo da cui nasce la segnalazione | indica come conseguenza: il modello non copre il processo da cui nasce la segnalazione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_odv_peverano.xlsx, contenuto pertinente a risk assessment; risk assessment; art. 6 D.Lgs. 231/2001

## B.27

- Tipo: assenza
- Issue: I-04
- Verifica: il deliverable esclude la conclusione bersaglio: aggiornare solo l'organigramma.
- Pass (insieme chiuso): indica l'azione: eseguire gap analysis per processo e paese | propone: eseguire gap analysis per processo e paese
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_odv_peverano.xlsx, contenuto pertinente a risk assessment; risk assessment; art. 6 D.Lgs. 231/2001

## B.28

- Tipo: valore
- Issue: I-05
- Verifica: il deliverable riporta il valore documentato per poteri e spesa.
- Pass (insieme chiuso): compare «180.000 euro» | compare «euro 180.000»
- Fail: non compare ne «180.000 euro» ne «euro 180.000» oppure compare un valore incompatibile
- Fonte: 03_email_imo_procure_e_intermediari.eml, contenuto pertinente a poteri e spesa; matrice procure; art. 6 D.Lgs. 231/2001

## B.29

- Tipo: attribuzione
- Issue: I-05
- Verifica: il deliverable collega il dato al documento: matrice procure.
- Pass (insieme chiuso): cita 03_email_imo_procure_e_intermediari.eml, contenuto pertinente a poteri e spesa | indica come riscontro 03_email_imo_procure_e_intermediari.eml, contenuto pertinente a poteri e spesa
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_imo_procure_e_intermediari.eml, contenuto pertinente a poteri e spesa; matrice procure; art. 6 D.Lgs. 231/2001

## B.30

- Tipo: qualificazione
- Issue: I-05
- Verifica: il deliverable espone l'effetto: il controllo autorizzativo è disallineato dal rischio.
- Pass (insieme chiuso): espone l'effetto: il controllo autorizzativo è disallineato dal rischio | indica come conseguenza: il controllo autorizzativo è disallineato dal rischio
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_imo_procure_e_intermediari.eml, contenuto pertinente a poteri e spesa; matrice procure; art. 6 D.Lgs. 231/2001

## B.31

- Tipo: presenza
- Issue: I-05
- Verifica: il deliverable riporta il valore documentato per poteri e spesa.
- Pass (insieme chiuso): afferma: le procure consentono pagamenti a consulenti senza doppia firma fino a 180.000 euro | conclude: le procure consentono pagamenti a consulenti senza doppia firma fino a 180.000 euro
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_imo_procure_e_intermediari.eml, contenuto pertinente a poteri e spesa; matrice procure; art. 6 D.Lgs. 231/2001

## B.32

- Tipo: qualificazione
- Issue: I-05
- Verifica: il deliverable tratta la lacuna come dato mancante: manca l'elenco dei delegati attivi.
- Pass (insieme chiuso): espone l'effetto: il controllo autorizzativo è disallineato dal rischio | indica come conseguenza: il controllo autorizzativo è disallineato dal rischio
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_imo_procure_e_intermediari.eml, contenuto pertinente a poteri e spesa; matrice procure; art. 6 D.Lgs. 231/2001

## B.33

- Tipo: assenza
- Issue: I-05
- Verifica: il deliverable esclude la conclusione bersaglio: lasciare la soglia invariata.
- Pass (insieme chiuso): indica l'azione: introdurre doppia approvazione e verifica beneficiario | propone: introdurre doppia approvazione e verifica beneficiario
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_imo_procure_e_intermediari.eml, contenuto pertinente a poteri e spesa; matrice procure; art. 6 D.Lgs. 231/2001

## B.34

- Tipo: presenza
- Issue: I-06
- Verifica: il deliverable enuncia il risultato: due agenti non hanno due diligence né clausola di audit.
- Pass (insieme chiuso): afferma: due agenti non hanno due diligence né clausola di audit | conclude: due agenti non hanno due diligence né clausola di audit
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_imo_procure_e_intermediari.eml, contenuto pertinente a terze parti; registro; modello 231

## B.35

- Tipo: attribuzione
- Issue: I-06
- Verifica: il deliverable collega il dato al documento: registro intermediari.
- Pass (insieme chiuso): cita 03_email_imo_procure_e_intermediari.eml, contenuto pertinente a terze parti | indica come riscontro 03_email_imo_procure_e_intermediari.eml, contenuto pertinente a terze parti
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_imo_procure_e_intermediari.eml, contenuto pertinente a terze parti; registro; modello 231

## B.36

- Tipo: qualificazione
- Issue: I-06
- Verifica: il deliverable espone l'effetto: il rapporto va sospeso o sottoposto a misure rafforzate.
- Pass (insieme chiuso): espone l'effetto: il rapporto va sospeso o sottoposto a misure rafforzate | indica come conseguenza: il rapporto va sospeso o sottoposto a misure rafforzate
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_imo_procure_e_intermediari.eml, contenuto pertinente a terze parti; registro; modello 231

## B.37

- Tipo: presenza
- Issue: I-06
- Verifica: il deliverable indica l'azione: bloccare nuovi pagamenti e completare la verifica.
- Pass (insieme chiuso): afferma: due agenti non hanno due diligence né clausola di audit | conclude: due agenti non hanno due diligence né clausola di audit
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_imo_procure_e_intermediari.eml, contenuto pertinente a terze parti; registro; modello 231

## B.38

- Tipo: qualificazione
- Issue: I-06
- Verifica: il deliverable tratta la lacuna come dato mancante: mancano titolari effettivi e referenze.
- Pass (insieme chiuso): espone l'effetto: il rapporto va sospeso o sottoposto a misure rafforzate | indica come conseguenza: il rapporto va sospeso o sottoposto a misure rafforzate
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_imo_procure_e_intermediari.eml, contenuto pertinente a terze parti; registro; modello 231

## B.39

- Tipo: assenza
- Issue: I-06
- Verifica: il deliverable esclude la conclusione bersaglio: rinnovare automaticamente gli incarichi.
- Pass (insieme chiuso): indica l'azione: bloccare nuovi pagamenti e completare la verifica | propone: bloccare nuovi pagamenti e completare la verifica
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_imo_procure_e_intermediari.eml, contenuto pertinente a terze parti; registro; modello 231

## B.40

- Tipo: presenza
- Issue: I-07
- Verifica: il deliverable enuncia il risultato: il regolamento della target non sanziona l'elusione dei controlli 231.
- Pass (insieme chiuso): afferma: il regolamento della target non sanziona l'elusione dei controlli 231 | conclude: il regolamento della target non sanziona l'elusione dei controlli 231
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_hr_disciplina_e_formazione.pdf, contenuto pertinente a sistema disciplinare; art. 6 D.Lgs. 231/2001

## B.41

- Tipo: attribuzione
- Issue: I-07
- Verifica: il deliverable collega il dato al documento: regolamento personale.
- Pass (insieme chiuso): cita 04_relazione_hr_disciplina_e_formazione.pdf, contenuto pertinente a sistema disciplinare | indica come riscontro 04_relazione_hr_disciplina_e_formazione.pdf, contenuto pertinente a sistema disciplinare
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_hr_disciplina_e_formazione.pdf, contenuto pertinente a sistema disciplinare; art. 6 D.Lgs. 231/2001

## B.42

- Tipo: qualificazione
- Issue: I-07
- Verifica: il deliverable espone l'effetto: l'aggiornamento del modello richiede una leva disciplinare espressa.
- Pass (insieme chiuso): espone l'effetto: l'aggiornamento del modello richiede una leva disciplinare espressa | indica come conseguenza: l'aggiornamento del modello richiede una leva disciplinare espressa
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_hr_disciplina_e_formazione.pdf, contenuto pertinente a sistema disciplinare; art. 6 D.Lgs. 231/2001

## B.43

- Tipo: presenza
- Issue: I-07
- Verifica: il deliverable indica l'azione: coordinare modifica, informativa e formazione.
- Pass (insieme chiuso): afferma: il regolamento della target non sanziona l'elusione dei controlli 231 | conclude: il regolamento della target non sanziona l'elusione dei controlli 231
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_hr_disciplina_e_formazione.pdf, contenuto pertinente a sistema disciplinare; art. 6 D.Lgs. 231/2001

## B.44

- Tipo: qualificazione
- Issue: I-07
- Verifica: il deliverable tratta la lacuna come dato mancante: manca il testo del CCNL applicato.
- Pass (insieme chiuso): espone l'effetto: l'aggiornamento del modello richiede una leva disciplinare espressa | indica come conseguenza: l'aggiornamento del modello richiede una leva disciplinare espressa
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_hr_disciplina_e_formazione.pdf, contenuto pertinente a sistema disciplinare; art. 6 D.Lgs. 231/2001

## B.45

- Tipo: assenza
- Issue: I-07
- Verifica: il deliverable esclude la conclusione bersaglio: limitarsi a una comunicazione etica.
- Pass (insieme chiuso): indica l'azione: coordinare modifica, informativa e formazione | propone: coordinare modifica, informativa e formazione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_hr_disciplina_e_formazione.pdf, contenuto pertinente a sistema disciplinare; art. 6 D.Lgs. 231/2001

## B.46

- Tipo: valore
- Issue: I-08
- Verifica: il deliverable riporta il valore documentato per formazione.
- Pass (insieme chiuso): compare «41 per cento» | compare «41%»
- Fail: non compare ne «41 per cento» ne «41%» oppure compare un valore incompatibile
- Fonte: 04_relazione_hr_disciplina_e_formazione.pdf, contenuto pertinente a formazione; report LMS; art. 7 D.Lgs. 231/2001

## B.47

- Tipo: attribuzione
- Issue: I-08
- Verifica: il deliverable collega il dato al documento: report LMS del 28 febbraio.
- Pass (insieme chiuso): cita 04_relazione_hr_disciplina_e_formazione.pdf, contenuto pertinente a formazione | indica come riscontro 04_relazione_hr_disciplina_e_formazione.pdf, contenuto pertinente a formazione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_hr_disciplina_e_formazione.pdf, contenuto pertinente a formazione; report LMS; art. 7 D.Lgs. 231/2001

## B.48

- Tipo: qualificazione
- Issue: I-08
- Verifica: il deliverable espone l'effetto: la misura non risulta attuata per il gruppo esposto.
- Pass (insieme chiuso): espone l'effetto: la misura non risulta attuata per il gruppo esposto | indica come conseguenza: la misura non risulta attuata per il gruppo esposto
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_hr_disciplina_e_formazione.pdf, contenuto pertinente a formazione; report LMS; art. 7 D.Lgs. 231/2001

## B.49

- Tipo: presenza
- Issue: I-08
- Verifica: il deliverable riporta il valore documentato per formazione.
- Pass (insieme chiuso): afferma: il 41 per cento della forza vendita non ha completato il corso | conclude: il 41 per cento della forza vendita non ha completato il corso
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_hr_disciplina_e_formazione.pdf, contenuto pertinente a formazione; report LMS; art. 7 D.Lgs. 231/2001

## B.50

- Tipo: qualificazione
- Issue: I-08
- Verifica: il deliverable tratta la lacuna come dato mancante: mancano dati sui neoassunti.
- Pass (insieme chiuso): espone l'effetto: la misura non risulta attuata per il gruppo esposto | indica come conseguenza: la misura non risulta attuata per il gruppo esposto
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_hr_disciplina_e_formazione.pdf, contenuto pertinente a formazione; report LMS; art. 7 D.Lgs. 231/2001

## B.51

- Tipo: assenza
- Issue: I-08
- Verifica: il deliverable esclude la conclusione bersaglio: chiudere l'azione alla pubblicazione del corso.
- Pass (insieme chiuso): indica l'azione: assegnare recupero e test con escalation | propone: assegnare recupero e test con escalation
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_hr_disciplina_e_formazione.pdf, contenuto pertinente a formazione; report LMS; art. 7 D.Lgs. 231/2001

## B.52

- Tipo: presenza
- Issue: I-09
- Verifica: il deliverable enuncia il risultato: il piano non prevede ristoro del danno né messa a disposizione del profitto.
- Pass (insieme chiuso): afferma: il piano non prevede ristoro del danno né messa a disposizione del profitto | conclude: il piano non prevede ristoro del danno né messa a disposizione del profitto
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_comitato_controllo_rischi.pdf, contenuto pertinente a riparazione; art. 17 D.Lgs. 231/2001

## B.53

- Tipo: attribuzione
- Issue: I-09
- Verifica: il deliverable collega il dato al documento: bozza remediation del 7 marzo.
- Pass (insieme chiuso): cita 05_nota_comitato_controllo_rischi.pdf, contenuto pertinente a riparazione | indica come riscontro 05_nota_comitato_controllo_rischi.pdf, contenuto pertinente a riparazione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_comitato_controllo_rischi.pdf, contenuto pertinente a riparazione; art. 17 D.Lgs. 231/2001

## B.54

- Tipo: qualificazione
- Issue: I-09
- Verifica: il deliverable espone l'effetto: mancano due elementi da valutare ai fini delle condizioni riparatorie.
- Pass (insieme chiuso): espone l'effetto: mancano due elementi da valutare ai fini delle condizioni riparatorie | indica come conseguenza: mancano due elementi da valutare ai fini delle condizioni riparatorie
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_comitato_controllo_rischi.pdf, contenuto pertinente a riparazione; art. 17 D.Lgs. 231/2001

## B.55

- Tipo: presenza
- Issue: I-09
- Verifica: il deliverable indica l'azione: quantificare danno, restituzioni e profitto.
- Pass (insieme chiuso): afferma: il piano non prevede ristoro del danno né messa a disposizione del profitto | conclude: il piano non prevede ristoro del danno né messa a disposizione del profitto
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_comitato_controllo_rischi.pdf, contenuto pertinente a riparazione; art. 17 D.Lgs. 231/2001

## B.56

- Tipo: qualificazione
- Issue: I-09
- Verifica: il deliverable tratta la lacuna come dato mancante: manca la stima finanziaria.
- Pass (insieme chiuso): espone l'effetto: mancano due elementi da valutare ai fini delle condizioni riparatorie | indica come conseguenza: mancano due elementi da valutare ai fini delle condizioni riparatorie
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_comitato_controllo_rischi.pdf, contenuto pertinente a riparazione; art. 17 D.Lgs. 231/2001

## B.57

- Tipo: assenza
- Issue: I-09
- Verifica: il deliverable esclude la conclusione bersaglio: confondere l'aggiornamento del modello con tutte le condotte riparatorie.
- Pass (insieme chiuso): indica l'azione: quantificare danno, restituzioni e profitto | propone: quantificare danno, restituzioni e profitto
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_comitato_controllo_rischi.pdf, contenuto pertinente a riparazione; art. 17 D.Lgs. 231/2001

## B.58

- Tipo: presenza
- Issue: I-10
- Verifica: il deliverable enuncia il risultato: la chiusura è subordinata a test dei controlli e report al consiglio.
- Pass (insieme chiuso): afferma: la chiusura è subordinata a test dei controlli e report al consiglio | conclude: la chiusura è subordinata a test dei controlli e report al consiglio
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_comitato_controllo_rischi.pdf, contenuto pertinente a chiusura; mandato; artt. 6 e 7 D.Lgs. 231/2001

## B.59

- Tipo: attribuzione
- Issue: I-10
- Verifica: il deliverable collega il dato al documento: mandato del comitato controllo.
- Pass (insieme chiuso): cita 05_nota_comitato_controllo_rischi.pdf, contenuto pertinente a chiusura | indica come riscontro 05_nota_comitato_controllo_rischi.pdf, contenuto pertinente a chiusura
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_comitato_controllo_rischi.pdf, contenuto pertinente a chiusura; mandato; artt. 6 e 7 D.Lgs. 231/2001

## B.60

- Tipo: qualificazione
- Issue: I-10
- Verifica: il deliverable espone l'effetto: la sola approvazione documentale non chiude la remediation.
- Pass (insieme chiuso): espone l'effetto: la sola approvazione documentale non chiude la remediation | indica come conseguenza: la sola approvazione documentale non chiude la remediation
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_comitato_controllo_rischi.pdf, contenuto pertinente a chiusura; mandato; artt. 6 e 7 D.Lgs. 231/2001

## B.61

- Tipo: presenza
- Issue: I-10
- Verifica: il deliverable indica l'azione: eseguire test a 30 e 90 giorni.
- Pass (insieme chiuso): afferma: la chiusura è subordinata a test dei controlli e report al consiglio | conclude: la chiusura è subordinata a test dei controlli e report al consiglio
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_comitato_controllo_rischi.pdf, contenuto pertinente a chiusura; mandato; artt. 6 e 7 D.Lgs. 231/2001

## B.62

- Tipo: qualificazione
- Issue: I-10
- Verifica: il deliverable tratta la lacuna come dato mancante: manca il proprietario di due controlli.
- Pass (insieme chiuso): espone l'effetto: la sola approvazione documentale non chiude la remediation | indica come conseguenza: la sola approvazione documentale non chiude la remediation
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_comitato_controllo_rischi.pdf, contenuto pertinente a chiusura; mandato; artt. 6 e 7 D.Lgs. 231/2001

## B.63

- Tipo: assenza
- Issue: I-10
- Verifica: il deliverable esclude la conclusione bersaglio: dichiarare chiuso il piano alla delibera.
- Pass (insieme chiuso): indica l'azione: eseguire test a 30 e 90 giorni | propone: eseguire test a 30 e 90 giorni
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_comitato_controllo_rischi.pdf, contenuto pertinente a chiusura; mandato; artt. 6 e 7 D.Lgs. 231/2001

## C.1

- Tipo: assenza
- Issue: N-01
- Verifica: chiusura simmetria sul falso positivo «brand policy»: Il cambio di intestazione della policy non prova l'attuazione dei controlli.
- Pass (insieme chiuso): non qualifica come criticita brand policy | esclude espressamente il falso positivo brand policy
- Fail: compare la conclusione vietata «brand policy costituisce una criticita autonoma»
- Fonte: challenge_map.json; documenti pubblici

## C.2

- Tipo: assenza
- Issue: N-02
- Verifica: chiusura sovra-segnalazione sul falso positivo «corso pubblicato»: La pubblicazione del corso non equivale al completamento da parte degli addetti.
- Pass (insieme chiuso): non qualifica come criticita corso pubblicato | esclude espressamente il falso positivo corso pubblicato
- Fail: compare la conclusione vietata «corso pubblicato costituisce una criticita autonoma»
- Fonte: challenge_map.json; documenti pubblici

## C.3

- Tipo: assenza
- Issue: N-03
- Verifica: chiusura presunzione sul falso positivo «verbale senza allegati»: La ricezione di una sintesi non dimostra che l'OdV abbia avuto accesso agli allegati.
- Pass (insieme chiuso): non qualifica come criticita verbale senza allegati | esclude espressamente il falso positivo verbale senza allegati
- Fail: compare la conclusione vietata «verbale senza allegati costituisce una criticita autonoma»
- Fonte: challenge_map.json; documenti pubblici
