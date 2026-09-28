# WF2-075 - Criteri atomizzati

Ogni riga valuta un solo fatto, valore, collegamento probatorio, effetto o azione.

## A.1

- Tipo: struttura
- Issue: A
- Verifica: la consegna usa i file public_works_review.md.
- Pass (insieme chiuso): i nomi dei file coincidono con public_works_review.md | il controllo deterministico sul requisito restituisce esito positivo
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
- Verifica: il deliverable enuncia il risultato: la clausola 12 consente varianti del RUP senza indicare presupposto né limite.
- Pass (insieme chiuso): afferma: la clausola 12 consente varianti del RUP senza indicare presupposto né limite | conclude: la clausola 12 consente varianti del RUP senza indicare presupposto né limite
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_schema_contratto_appalto_lavori_v3.pdf, contenuto pertinente a varianti; art. 120 D.Lgs. 36/2023

## B.2

- Tipo: attribuzione
- Issue: I-01
- Verifica: il deliverable collega il dato al documento: bozza contratto, clausola 12.
- Pass (insieme chiuso): cita 01_schema_contratto_appalto_lavori_v3.pdf, contenuto pertinente a varianti | indica come riscontro 01_schema_contratto_appalto_lavori_v3.pdf, contenuto pertinente a varianti
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_schema_contratto_appalto_lavori_v3.pdf, contenuto pertinente a varianti; art. 120 D.Lgs. 36/2023

## B.3

- Tipo: qualificazione
- Issue: I-01
- Verifica: il deliverable espone l'effetto: la modifica può uscire dai casi ammessi.
- Pass (insieme chiuso): espone l'effetto: la modifica può uscire dai casi ammessi | indica come conseguenza: la modifica può uscire dai casi ammessi
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_schema_contratto_appalto_lavori_v3.pdf, contenuto pertinente a varianti; art. 120 D.Lgs. 36/2023

## B.4

- Tipo: presenza
- Issue: I-01
- Verifica: il deliverable indica l'azione: legare ogni variante a presupposto, motivazione e soglia.
- Pass (insieme chiuso): afferma: la clausola 12 consente varianti del RUP senza indicare presupposto né limite | conclude: la clausola 12 consente varianti del RUP senza indicare presupposto né limite
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_schema_contratto_appalto_lavori_v3.pdf, contenuto pertinente a varianti; art. 120 D.Lgs. 36/2023

## B.5

- Tipo: qualificazione
- Issue: I-01
- Verifica: il deliverable tratta la lacuna come dato mancante: manca il quadro economico aggiornato.
- Pass (insieme chiuso): espone l'effetto: la modifica può uscire dai casi ammessi | indica come conseguenza: la modifica può uscire dai casi ammessi
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_schema_contratto_appalto_lavori_v3.pdf, contenuto pertinente a varianti; art. 120 D.Lgs. 36/2023

## B.6

- Tipo: presenza
- Issue: I-02
- Verifica: il deliverable enuncia il risultato: il richiamo al quinto d'obbligo non indica la previsione nei documenti iniziali.
- Pass (insieme chiuso): afferma: il richiamo al quinto d'obbligo non indica la previsione nei documenti iniziali | conclude: il richiamo al quinto d'obbligo non indica la previsione nei documenti iniziali
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_schema_contratto_appalto_lavori_v3.pdf, contenuto pertinente a quinto d'obbligo; art. 120 D.Lgs. 36/2023

## B.7

- Tipo: attribuzione
- Issue: I-02
- Verifica: il deliverable collega il dato al documento: bozza e disciplinare.
- Pass (insieme chiuso): cita 01_schema_contratto_appalto_lavori_v3.pdf, contenuto pertinente a quinto d'obbligo | indica come riscontro 01_schema_contratto_appalto_lavori_v3.pdf, contenuto pertinente a quinto d'obbligo
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_schema_contratto_appalto_lavori_v3.pdf, contenuto pertinente a quinto d'obbligo; art. 120 D.Lgs. 36/2023

## B.8

- Tipo: qualificazione
- Issue: I-02
- Verifica: il deliverable espone l'effetto: l'esigibilità della prestazione aggiuntiva resta esposta.
- Pass (insieme chiuso): espone l'effetto: l'esigibilità della prestazione aggiuntiva resta esposta | indica come conseguenza: l'esigibilità della prestazione aggiuntiva resta esposta
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_schema_contratto_appalto_lavori_v3.pdf, contenuto pertinente a quinto d'obbligo; art. 120 D.Lgs. 36/2023

## B.9

- Tipo: presenza
- Issue: I-02
- Verifica: il deliverable indica l'azione: coordinare contratto e lex specialis.
- Pass (insieme chiuso): afferma: il richiamo al quinto d'obbligo non indica la previsione nei documenti iniziali | conclude: il richiamo al quinto d'obbligo non indica la previsione nei documenti iniziali
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_schema_contratto_appalto_lavori_v3.pdf, contenuto pertinente a quinto d'obbligo; art. 120 D.Lgs. 36/2023

## B.10

- Tipo: qualificazione
- Issue: I-02
- Verifica: il deliverable tratta la lacuna come dato mancante: manca l'allegato opzioni.
- Pass (insieme chiuso): espone l'effetto: l'esigibilità della prestazione aggiuntiva resta esposta | indica come conseguenza: l'esigibilità della prestazione aggiuntiva resta esposta
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_schema_contratto_appalto_lavori_v3.pdf, contenuto pertinente a quinto d'obbligo; art. 120 D.Lgs. 36/2023

## B.11

- Tipo: valore
- Issue: I-03
- Verifica: il deliverable riporta il valore documentato per revisione prezzi.
- Pass (insieme chiuso): compare «10 per cento» | compare «10%»
- Fail: non compare ne «10 per cento» ne «10%» oppure compare un valore incompatibile
- Fonte: 02_disciplinare_estratto_coordinamento_contrattuale.xlsx, contenuto pertinente a revisione prezzi; art. 60 D.Lgs. 36/2023; Allegato II.2-bis

## B.12

- Tipo: attribuzione
- Issue: I-03
- Verifica: il deliverable collega il dato al documento: clausola 15.
- Pass (insieme chiuso): cita 02_disciplinare_estratto_coordinamento_contrattuale.xlsx, contenuto pertinente a revisione prezzi | indica come riscontro 02_disciplinare_estratto_coordinamento_contrattuale.xlsx, contenuto pertinente a revisione prezzi
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_disciplinare_estratto_coordinamento_contrattuale.xlsx, contenuto pertinente a revisione prezzi; art. 60 D.Lgs. 36/2023; Allegato II.2-bis

## B.13

- Tipo: qualificazione
- Issue: I-03
- Verifica: il deliverable espone l'effetto: la formula deve essere sostituita con rinvio e indice pertinenti.
- Pass (insieme chiuso): espone l'effetto: la formula deve essere sostituita con rinvio e indice pertinenti | indica come conseguenza: la formula deve essere sostituita con rinvio e indice pertinenti
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_disciplinare_estratto_coordinamento_contrattuale.xlsx, contenuto pertinente a revisione prezzi; art. 60 D.Lgs. 36/2023; Allegato II.2-bis

## B.14

- Tipo: presenza
- Issue: I-03
- Verifica: il deliverable riporta il valore documentato per revisione prezzi.
- Pass (insieme chiuso): afferma: la soglia contrattuale del 10 per cento contrasta con la clausola legale applicabile | conclude: la soglia contrattuale del 10 per cento contrasta con la clausola legale applicabile
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_disciplinare_estratto_coordinamento_contrattuale.xlsx, contenuto pertinente a revisione prezzi; art. 60 D.Lgs. 36/2023; Allegato II.2-bis

## B.15

- Tipo: qualificazione
- Issue: I-03
- Verifica: il deliverable tratta la lacuna come dato mancante: manca l'indice di settore.
- Pass (insieme chiuso): espone l'effetto: la formula deve essere sostituita con rinvio e indice pertinenti | indica come conseguenza: la formula deve essere sostituita con rinvio e indice pertinenti
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_disciplinare_estratto_coordinamento_contrattuale.xlsx, contenuto pertinente a revisione prezzi; art. 60 D.Lgs. 36/2023; Allegato II.2-bis

## B.16

- Tipo: presenza
- Issue: I-04
- Verifica: il deliverable enuncia il risultato: la clausola 18 rinvia le riserve alla sola comunicazione PEC.
- Pass (insieme chiuso): afferma: la clausola 18 rinvia le riserve alla sola comunicazione PEC | conclude: la clausola 18 rinvia le riserve alla sola comunicazione PEC
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_disciplinare_estratto_coordinamento_contrattuale.xlsx, contenuto pertinente a riserve; art. 115 D.Lgs. 36/2023

## B.17

- Tipo: attribuzione
- Issue: I-04
- Verifica: il deliverable collega il dato al documento: bozza e capitolato.
- Pass (insieme chiuso): cita 02_disciplinare_estratto_coordinamento_contrattuale.xlsx, contenuto pertinente a riserve | indica come riscontro 02_disciplinare_estratto_coordinamento_contrattuale.xlsx, contenuto pertinente a riserve
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_disciplinare_estratto_coordinamento_contrattuale.xlsx, contenuto pertinente a riserve; art. 115 D.Lgs. 36/2023

## B.18

- Tipo: qualificazione
- Issue: I-04
- Verifica: il deliverable espone l'effetto: il testo non presidia iscrizione negli atti contabili.
- Pass (insieme chiuso): espone l'effetto: il testo non presidia iscrizione negli atti contabili | indica come conseguenza: il testo non presidia iscrizione negli atti contabili
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_disciplinare_estratto_coordinamento_contrattuale.xlsx, contenuto pertinente a riserve; art. 115 D.Lgs. 36/2023

## B.19

- Tipo: presenza
- Issue: I-04
- Verifica: il deliverable indica l'azione: richiamare modalità e termini dell'Allegato II.14.
- Pass (insieme chiuso): afferma: la clausola 18 rinvia le riserve alla sola comunicazione PEC | conclude: la clausola 18 rinvia le riserve alla sola comunicazione PEC
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_disciplinare_estratto_coordinamento_contrattuale.xlsx, contenuto pertinente a riserve; art. 115 D.Lgs. 36/2023

## B.20

- Tipo: presenza
- Issue: I-05
- Verifica: il deliverable enuncia il risultato: la clausola 20 attribuisce all'esecutore un diritto unilaterale di sospendere.
- Pass (insieme chiuso): afferma: la clausola 20 attribuisce all'esecutore un diritto unilaterale di sospendere | conclude: la clausola 20 attribuisce all'esecutore un diritto unilaterale di sospendere
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_dl_osservazioni_schema_contratto.eml, contenuto pertinente a sospensione; D.Lgs. 36/2023; Allegato II.14

## B.21

- Tipo: attribuzione
- Issue: I-05
- Verifica: il deliverable collega il dato al documento: bozza contratto.
- Pass (insieme chiuso): cita 03_email_dl_osservazioni_schema_contratto.eml, contenuto pertinente a sospensione | indica come riscontro 03_email_dl_osservazioni_schema_contratto.eml, contenuto pertinente a sospensione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_dl_osservazioni_schema_contratto.eml, contenuto pertinente a sospensione; D.Lgs. 36/2023; Allegato II.14

## B.22

- Tipo: qualificazione
- Issue: I-05
- Verifica: il deliverable espone l'effetto: la previsione può interrompere l'esecuzione fuori dal procedimento.
- Pass (insieme chiuso): espone l'effetto: la previsione può interrompere l'esecuzione fuori dal procedimento | indica come conseguenza: la previsione può interrompere l'esecuzione fuori dal procedimento
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_dl_osservazioni_schema_contratto.eml, contenuto pertinente a sospensione; D.Lgs. 36/2023; Allegato II.14

## B.23

- Tipo: presenza
- Issue: I-05
- Verifica: il deliverable indica l'azione: subordinare sospensione a ordine e verbalizzazione.
- Pass (insieme chiuso): afferma: la clausola 20 attribuisce all'esecutore un diritto unilaterale di sospendere | conclude: la clausola 20 attribuisce all'esecutore un diritto unilaterale di sospendere
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_dl_osservazioni_schema_contratto.eml, contenuto pertinente a sospensione; D.Lgs. 36/2023; Allegato II.14

## B.24

- Tipo: presenza
- Issue: I-06
- Verifica: il deliverable enuncia il risultato: la penale giornaliera è fissata senza tetto complessivo.
- Pass (insieme chiuso): afferma: la penale giornaliera è fissata senza tetto complessivo | conclude: la penale giornaliera è fissata senza tetto complessivo
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_dl_osservazioni_schema_contratto.eml, contenuto pertinente a penali; art. 126 D.Lgs. 36/2023

## B.25

- Tipo: attribuzione
- Issue: I-06
- Verifica: il deliverable collega il dato al documento: clausola 22.
- Pass (insieme chiuso): cita 03_email_dl_osservazioni_schema_contratto.eml, contenuto pertinente a penali | indica come riscontro 03_email_dl_osservazioni_schema_contratto.eml, contenuto pertinente a penali
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_dl_osservazioni_schema_contratto.eml, contenuto pertinente a penali; art. 126 D.Lgs. 36/2023

## B.26

- Tipo: qualificazione
- Issue: I-06
- Verifica: il deliverable espone l'effetto: manca il limite previsto dalla disciplina di gara.
- Pass (insieme chiuso): espone l'effetto: manca il limite previsto dalla disciplina di gara | indica come conseguenza: manca il limite previsto dalla disciplina di gara
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_dl_osservazioni_schema_contratto.eml, contenuto pertinente a penali; art. 126 D.Lgs. 36/2023

## B.27

- Tipo: presenza
- Issue: I-06
- Verifica: il deliverable indica l'azione: inserire aliquota, base, contestazione e tetto.
- Pass (insieme chiuso): afferma: la penale giornaliera è fissata senza tetto complessivo | conclude: la penale giornaliera è fissata senza tetto complessivo
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_dl_osservazioni_schema_contratto.eml, contenuto pertinente a penali; art. 126 D.Lgs. 36/2023

## B.28

- Tipo: presenza
- Issue: I-07
- Verifica: il deliverable enuncia il risultato: la clausola 25 rende definitivo il collaudo alla firma del certificato.
- Pass (insieme chiuso): afferma: la clausola 25 rende definitivo il collaudo alla firma del certificato | conclude: la clausola 25 rende definitivo il collaudo alla firma del certificato
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_prospetto_garanzie_collaudo_supporto_rup.pdf, contenuto pertinente a collaudo; art. 116 D.Lgs. 36/2023

## B.29

- Tipo: attribuzione
- Issue: I-07
- Verifica: il deliverable collega il dato al documento: bozza contratto.
- Pass (insieme chiuso): cita 04_prospetto_garanzie_collaudo_supporto_rup.pdf, contenuto pertinente a collaudo | indica come riscontro 04_prospetto_garanzie_collaudo_supporto_rup.pdf, contenuto pertinente a collaudo
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_prospetto_garanzie_collaudo_supporto_rup.pdf, contenuto pertinente a collaudo; art. 116 D.Lgs. 36/2023

## B.30

- Tipo: qualificazione
- Issue: I-07
- Verifica: il deliverable espone l'effetto: il testo anticipa gli effetti definitivi.
- Pass (insieme chiuso): espone l'effetto: il testo anticipa gli effetti definitivi | indica come conseguenza: il testo anticipa gli effetti definitivi
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_prospetto_garanzie_collaudo_supporto_rup.pdf, contenuto pertinente a collaudo; art. 116 D.Lgs. 36/2023

## B.31

- Tipo: presenza
- Issue: I-07
- Verifica: il deliverable indica l'azione: distinguere emissione provvisoria e consolidamento.
- Pass (insieme chiuso): afferma: la clausola 25 rende definitivo il collaudo alla firma del certificato | conclude: la clausola 25 rende definitivo il collaudo alla firma del certificato
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_prospetto_garanzie_collaudo_supporto_rup.pdf, contenuto pertinente a collaudo; art. 116 D.Lgs. 36/2023

## B.32

- Tipo: presenza
- Issue: I-08
- Verifica: il deliverable enuncia il risultato: la rinuncia preventiva alle contestazioni per vizi riconoscibili è incompatibile con il periodo di provvisorietà.
- Pass (insieme chiuso): afferma: la rinuncia preventiva alle contestazioni per vizi riconoscibili è incompatibile con il periodo di provvisorietà | conclude: la rinuncia preventiva alle contestazioni per vizi riconoscibili è incompatibile con il periodo di provvisorietà
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_prospetto_garanzie_collaudo_supporto_rup.pdf, contenuto pertinente a vizi; art. 116 D.Lgs. 36/2023

## B.33

- Tipo: attribuzione
- Issue: I-08
- Verifica: il deliverable collega il dato al documento: clausola 25.7.
- Pass (insieme chiuso): cita 04_prospetto_garanzie_collaudo_supporto_rup.pdf, contenuto pertinente a vizi | indica come riscontro 04_prospetto_garanzie_collaudo_supporto_rup.pdf, contenuto pertinente a vizi
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_prospetto_garanzie_collaudo_supporto_rup.pdf, contenuto pertinente a vizi; art. 116 D.Lgs. 36/2023

## B.34

- Tipo: qualificazione
- Issue: I-08
- Verifica: il deliverable espone l'effetto: la stazione appaltante perderebbe una tutela prevista.
- Pass (insieme chiuso): espone l'effetto: la stazione appaltante perderebbe una tutela prevista | indica come conseguenza: la stazione appaltante perderebbe una tutela prevista
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_prospetto_garanzie_collaudo_supporto_rup.pdf, contenuto pertinente a vizi; art. 116 D.Lgs. 36/2023

## B.35

- Tipo: presenza
- Issue: I-08
- Verifica: il deliverable indica l'azione: eliminare la rinuncia.
- Pass (insieme chiuso): afferma: la rinuncia preventiva alle contestazioni per vizi riconoscibili è incompatibile con il periodo di provvisorietà | conclude: la rinuncia preventiva alle contestazioni per vizi riconoscibili è incompatibile con il periodo di provvisorietà
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_prospetto_garanzie_collaudo_supporto_rup.pdf, contenuto pertinente a vizi; art. 116 D.Lgs. 36/2023

## B.36

- Tipo: presenza
- Issue: I-09
- Verifica: il deliverable enuncia il risultato: la clausola 27 confonde recesso e risoluzione.
- Pass (insieme chiuso): afferma: la clausola 27 confonde recesso e risoluzione | conclude: la clausola 27 confonde recesso e risoluzione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_osservazioni_edil_quarneto_schema_contratto.pdf, contenuto pertinente a risoluzione; art. 122 D.Lgs. 36/2023

## B.37

- Tipo: attribuzione
- Issue: I-09
- Verifica: il deliverable collega il dato al documento: bozza contratto.
- Pass (insieme chiuso): cita 05_osservazioni_edil_quarneto_schema_contratto.pdf, contenuto pertinente a risoluzione | indica come riscontro 05_osservazioni_edil_quarneto_schema_contratto.pdf, contenuto pertinente a risoluzione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_osservazioni_edil_quarneto_schema_contratto.pdf, contenuto pertinente a risoluzione; art. 122 D.Lgs. 36/2023

## B.38

- Tipo: qualificazione
- Issue: I-09
- Verifica: il deliverable espone l'effetto: presupposti e conseguenze economiche risultano indistinti.
- Pass (insieme chiuso): espone l'effetto: presupposti e conseguenze economiche risultano indistinti | indica come conseguenza: presupposti e conseguenze economiche risultano indistinti
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_osservazioni_edil_quarneto_schema_contratto.pdf, contenuto pertinente a risoluzione; art. 122 D.Lgs. 36/2023

## B.39

- Tipo: presenza
- Issue: I-09
- Verifica: il deliverable indica l'azione: separare le due fattispecie.
- Pass (insieme chiuso): afferma: la clausola 27 confonde recesso e risoluzione | conclude: la clausola 27 confonde recesso e risoluzione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_osservazioni_edil_quarneto_schema_contratto.pdf, contenuto pertinente a risoluzione; art. 122 D.Lgs. 36/2023

## B.40

- Tipo: presenza
- Issue: I-10
- Verifica: il deliverable enuncia il risultato: lo svincolo integrale della cauzione è previsto prima del collaudo provvisorio.
- Pass (insieme chiuso): afferma: lo svincolo integrale della cauzione è previsto prima del collaudo provvisorio | conclude: lo svincolo integrale della cauzione è previsto prima del collaudo provvisorio
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_osservazioni_edil_quarneto_schema_contratto.pdf, contenuto pertinente a garanzia; art. 117 D.Lgs. 36/2023

## B.41

- Tipo: attribuzione
- Issue: I-10
- Verifica: il deliverable collega il dato al documento: clausola 29.
- Pass (insieme chiuso): cita 05_osservazioni_edil_quarneto_schema_contratto.pdf, contenuto pertinente a garanzia | indica come riscontro 05_osservazioni_edil_quarneto_schema_contratto.pdf, contenuto pertinente a garanzia
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_osservazioni_edil_quarneto_schema_contratto.pdf, contenuto pertinente a garanzia; art. 117 D.Lgs. 36/2023

## B.42

- Tipo: qualificazione
- Issue: I-10
- Verifica: il deliverable espone l'effetto: lo svincolo anticipato lascia scoperta l'esecuzione.
- Pass (insieme chiuso): espone l'effetto: lo svincolo anticipato lascia scoperta l'esecuzione | indica come conseguenza: lo svincolo anticipato lascia scoperta l'esecuzione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_osservazioni_edil_quarneto_schema_contratto.pdf, contenuto pertinente a garanzia; art. 117 D.Lgs. 36/2023

## B.43

- Tipo: presenza
- Issue: I-10
- Verifica: il deliverable indica l'azione: allineare svincolo e certificati.
- Pass (insieme chiuso): afferma: lo svincolo integrale della cauzione è previsto prima del collaudo provvisorio | conclude: lo svincolo integrale della cauzione è previsto prima del collaudo provvisorio
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_osservazioni_edil_quarneto_schema_contratto.pdf, contenuto pertinente a garanzia; art. 117 D.Lgs. 36/2023

## C.1

- Tipo: assenza
- Issue: N-01
- Verifica: chiusura simmetria sul falso positivo «giorni naturali»: La durata espressa in giorni naturali non è di per sé una variante contrattuale.
- Pass (insieme chiuso): non qualifica come criticita giorni naturali | esclude espressamente il falso positivo giorni naturali
- Fail: compare la conclusione vietata «giorni naturali costituisce una criticita autonoma»
- Fonte: challenge_map.json; documenti pubblici

## C.2

- Tipo: assenza
- Issue: N-02
- Verifica: chiusura sovra-segnalazione sul falso positivo «bozza polizza»: Una bozza di garanzia non dimostra l'avvenuta costituzione della garanzia definitiva.
- Pass (insieme chiuso): non qualifica come criticita bozza polizza | esclude espressamente il falso positivo bozza polizza
- Fail: compare la conclusione vietata «bozza polizza costituisce una criticita autonoma»
- Fonte: challenge_map.json; documenti pubblici

## C.3

- Tipo: assenza
- Issue: N-03
- Verifica: chiusura presunzione sul falso positivo «pec informativa»: Una PEC informativa non sostituisce automaticamente gli adempimenti della contabilità lavori.
- Pass (insieme chiuso): non qualifica come criticita pec informativa | esclude espressamente il falso positivo pec informativa
- Fail: compare la conclusione vietata «pec informativa costituisce una criticita autonoma»
- Fonte: challenge_map.json; documenti pubblici
