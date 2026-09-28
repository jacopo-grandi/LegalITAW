# WF2-031 - Rubrica atomizzata

Generato da `source/authoring/costruisci_rubrica_031.py`. Non modificare a mano: la fonte e' lo script, la forma macchina e' `rubric.json`.

15 issue di merito, 67 criteri atomici (21 a verifica meccanica, 46 al judge).

## A. Forma dell'output (interamente verifica meccanica)

### A.1  [issue: A]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable e' un file denominato red_flag_fiscali.md di lunghezza non superiore a 2.200 parole.

**Pass se** &nbsp; il file si chiama red_flag_fiscali.md e il conteggio delle parole non supera 2.200

**Fail se** &nbsp; il nome del file e' diverso oppure il conteggio supera 2.200 parole.

*Non passa al judge:* fonte: response_template.md | gravita': bassa

### A.2  [issue: A]  [tipo: struttura]  [verifica meccanica]

**Verifica** &nbsp; il deliverable contiene, nell'ordine, otto sezioni intitolate Sintesi per la decisione, Matrice dei red flag fiscali, Calcoli, Che cosa non e' un rilievo, Copertura contrattuale e periodi scoperti, Perdite fiscali: utilizzabilita' dopo l'acquisto, Elementi mancanti dal fascicolo, Che cosa fare.

**Pass se** &nbsp; le otto intestazioni compaiono tutte e nell'ordine indicato

**Fail se** &nbsp; manca una intestazione oppure l'ordine e' diverso.

*Non passa al judge:* fonte: response_template.md | gravita': bassa

### A.3  [issue: A]  [tipo: struttura]  [verifica meccanica]

**Verifica** &nbsp; ogni riga della matrice della sezione 2 riporta il documento del fascicolo da cui il rilievo deriva.

**Pass se** &nbsp; in ciascuna riga la colonna del documento e' compilata

**Fail se** &nbsp; una o piu' righe non indicano il documento.

*Non passa al judge:* fonte: response_template.md | gravita': media

### A.4  [issue: A]  [tipo: assenza]  [verifica meccanica]

**Verifica** &nbsp; il deliverable non contiene riferimenti normativi o di prassi diversi da quelli elencati in fonti_chiuse.json, comprensivi dell'array dei riferimenti richiamati nei documenti del fascicolo.

**Pass se** &nbsp; tutti i riferimenti presenti compaiono nell'elenco chiuso

**Fail se** &nbsp; compare un riferimento estraneo all'elenco chiuso.

*Non passa al judge:* fonte: public/03_legal_sources.md | gravita': alta

### A.5  [issue: A]  [tipo: struttura]  [verifica meccanica]

**Verifica** &nbsp; per ogni riga della matrice la colonna dell'esposizione stimata riporta un importo in euro oppure la dicitura di importo non determinabile.

**Pass se** &nbsp; nessuna cella della colonna dell'esposizione e' vuota

**Fail se** &nbsp; una o piu' celle della colonna dell'esposizione sono vuote.

*Non passa al judge:* fonte: response_template.md | gravita': media

## B. Merito

Stato del fascicolo alla data di riferimento del 9 marzo 2028: verifica fiscale chiusa senza avviso di accertamento, contratto allo stato di bozza, esecuzione fissata per il 28 aprile 2028.

### B.1  [issue: I-01]  [tipo: attribuzione]  [judge]

**Verifica** &nbsp; il deliverable riconduce la ripresa delle spese di sponsorizzazione al rilievo n. 3 del processo verbale di constatazione.

**Pass se** &nbsp; compare il riferimento al rilievo n. 3 del processo verbale, oppure al rilievo sulle sponsorizzazioni del periodo d'imposta 2023

**Fail se** &nbsp; la ripresa non e' agganciata ad alcun rilievo del processo verbale.

*Non passa al judge:* fonte: processo verbale di constatazione, rilievo n. 3 | gravita': alta

### B.2  [issue: I-02]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable espone il rilievo sull'imposta sul valore aggiunto come rilievo distinto da quello sull'IRES.

**Pass se** &nbsp; il rilievo IVA compare come voce autonoma della matrice, con importo proprio

**Fail se** &nbsp; il rilievo IVA e' fuso con quello IRES in un'unica voce, oppure non compare.

*Non passa al judge:* fonte: processo verbale di constatazione, rilievo n. 4 | gravita': alta

### B.3  [issue: I-03]  [tipo: qualificazione]  [judge]

**Verifica** &nbsp; il deliverable qualifica il rilievo n. 2 come contestazione di imputazione a un esercizio diverso da quello di competenza.

**Pass se** &nbsp; compare, riferita a quel rilievo, una fra: «rilievo di competenza», «questione di competenza», «imputazione temporale», «differimento della deduzione»

**Fail se** &nbsp; il rilievo n. 2 e' trattato come indeducibilita' definitiva del costo, oppure non e' qualificato.

*Non passa al judge:* fonte: processo verbale di constatazione, rilievo n. 2 | gravita': alta

### B.4  [issue: I-03]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che l'esposizione economica del rilievo n. 2 e' limitata a sanzioni e interessi.

**Pass se** &nbsp; compare l'affermazione che l'esposizione si limita a sanzioni e interessi, oppure che il costo resta deducibile nel periodo d'imposta 2023

**Fail se** &nbsp; l'esposizione del rilievo n. 2 e' presentata come pari alla maggiore imposta.

*Non passa al judge:* fonte: art. 109, comma 1, TUIR | gravita': alta

### B.5  [issue: I-03]  [tipo: assenza]  [judge]

**Verifica** &nbsp; nella colonna dell'esposizione stimata della riga relativa al rilievo n. 2 il deliverable non riporta l'importo di euro 81.600,00.

**Pass se** &nbsp; nella colonna dell'esposizione stimata di quella riga compare un importo diverso da 81.600,00, oppure la dicitura che l'esposizione si limita a sanzioni e interessi

**Fail se** &nbsp; la colonna dell'esposizione stimata di quella riga riporta euro 81.600,00.

*Non passa al judge:* fonte: processo verbale di constatazione, rilievo n. 2 | gravita': alta

### B.6  [issue: I-05]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che il fondo per imposte iscritto nel bilancio 2027 non copre l'esposizione.

**Pass se** &nbsp; compare una fra: «incapiente», «insufficiente», «non copre», «capienza parziale» riferita al fondo per imposte

**Fail se** &nbsp; il fondo e' presentato come capiente, oppure la capienza non e' trattata.

*Non passa al judge:* fonte: bilancio 2027, stato patrimoniale B.2 | gravita': alta

### B.7  [issue: I-06]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che le spese di rappresentanza del 2026 eccedono il limite di deducibilita'.

**Pass se** &nbsp; compare l'affermazione che le spese di rappresentanza del 2026 superano il limite, oppure che una parte di esse e' indeducibile

**Fail se** &nbsp; le spese di rappresentanza sono presentate come integralmente deducibili, oppure non sono trattate.

*Non passa al judge:* fonte: bilancio 2026, nota integrativa; art. 108, comma 2, TUIR | gravita': alta

### B.8  [issue: I-06]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che l'eccedenza non e' stata ripresa a tassazione nella riconciliazione fiscale del bilancio 2026.

**Pass se** &nbsp; compare l'affermazione che la variazione in aumento manca, non e' stata operata oppure non compare nel prospetto di riconciliazione

**Fail se** &nbsp; il deliverable non collega l'eccedenza alla mancata ripresa a tassazione.

*Non passa al judge:* fonte: bilancio 2026, prospetto di riconciliazione | gravita': alta

### B.9  [issue: I-07]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che la limitazione al riporto delle perdite presuppone due condizioni che devono ricorrere entrambe.

**Pass se** &nbsp; compare una fra: «entrambe le condizioni», «condizioni cumulative», «occorre anche», «non basta il trasferimento»

**Fail se** &nbsp; la limitazione e' presentata come effetto del solo trasferimento delle partecipazioni.

*Non passa al judge:* fonte: art. 84, comma 3, TUIR | gravita': alta

### B.10  [issue: I-07]  [tipo: attribuzione]  [judge]

**Verifica** &nbsp; il deliverable riconduce la seconda condizione all'acquisizione del ramo d'azienda del 3 luglio 2026.

**Pass se** &nbsp; compare il riferimento all'acquisto della Divisione Ricambi, oppure all'acquisizione del ramo d'azienda del 2026, come fatto che integra la modifica dell'attivita'

**Fail se** &nbsp; la seconda condizione e' agganciata a un fatto diverso, oppure non e' agganciata ad alcun fatto.

*Non passa al judge:* fonte: atto di cessione di ramo d'azienda del 3 luglio 2026 | gravita': alta

### B.11  [issue: I-07]  [tipo: assenza]  [judge]

**Verifica** &nbsp; il deliverable non afferma che la limitazione al riporto delle perdite non opera perche' l'attivita' della societa' non cambia.

**Pass se** &nbsp; non compare l'affermazione che l'attivita' resta la stessa e che percio' la limitazione non opera

**Fail se** &nbsp; il deliverable esclude la limitazione sul presupposto che l'attivita' non muti.

*Non passa al judge:* fonte: nota del direttore amministrativo; art. 84, comma 3, TUIR | gravita': alta

### B.12  [issue: I-08]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che il test sulle grandezze di conto economico e' superato.

**Pass se** &nbsp; compare una fra: «il test e' superato», «la soglia e' superata», «la condizione di disapplicazione ricorre»

**Fail se** &nbsp; il test e' dichiarato non superato, oppure non e' trattato.

*Non passa al judge:* fonte: art. 84, comma 3-bis, TUIR | gravita': alta

### B.13  [issue: I-08]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable verifica il test su entrambe le grandezze, ricavi e spese per prestazioni di lavoro subordinato.

**Pass se** &nbsp; compaiono, riferite al test, sia la grandezza dei ricavi sia quella delle spese per prestazioni di lavoro subordinato

**Fail se** &nbsp; il test e' verificato su una sola delle due grandezze.

*Non passa al judge:* fonte: art. 84, comma 3-bis, TUIR | gravita': alta

### B.14  [issue: I-09]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che, in assenza di relazione giurata di stima, il tetto al riporto e' dato dal patrimonio netto contabile.

**Pass se** &nbsp; compare l'affermazione che si applica il patrimonio netto contabile perche' la relazione giurata di stima non e' stata predisposta o non risulta dal fascicolo

**Fail se** &nbsp; il tetto e' agganciato al valore economico del patrimonio netto, oppure il presupposto non e' indicato.

*Non passa al judge:* fonte: art. 84, comma 3-ter, TUIR | gravita': alta

### B.15  [issue: I-09]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che dal patrimonio netto contabile va sottratto il versamento in conto capitale del 18 settembre 2026.

**Pass se** &nbsp; compare la sottrazione del versamento in conto capitale, oppure l'affermazione che dei versamenti degli ultimi ventiquattro mesi non si tiene conto

**Fail se** &nbsp; il versamento non e' sottratto, oppure la sottrazione non e' motivata.

*Non passa al judge:* fonte: bilancio 2026, prospetto delle movimentazioni del patrimonio netto | gravita': alta

### B.16  [issue: I-10]  [tipo: qualificazione]  [judge]

**Verifica** &nbsp; il deliverable qualifica la perdita del riporto come voce che incide sul prezzo e non come passivita' indennizzabile.

**Pass se** &nbsp; compare, riferita alla perdita del riporto, una fra: «questione di prezzo», «incide sul corrispettivo», «va negoziata nel prezzo», «non e' una Passivita' Fiscale»

**Fail se** &nbsp; la perdita del riporto e' trattata come voce indennizzabile, oppure non e' qualificata.

*Non passa al judge:* fonte: bozza di contratto, articoli 1 e 9.1 | gravita': alta

### B.17  [issue: I-10]  [tipo: assenza]  [judge]

**Verifica** &nbsp; il deliverable non indica la perdita del riporto delle perdite fra gli importi coperti dall'obbligo di indennizzo dell'articolo 9.

**Pass se** &nbsp; la perdita del riporto non compare fra le voci indennizzabili

**Fail se** &nbsp; la perdita del riporto e' inserita fra le voci indennizzabili ai sensi dell'articolo 9.

*Non passa al judge:* fonte: bozza di contratto, articolo 9.1 | gravita': alta

### B.18  [issue: I-11]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che la societa' risponde in solido dei debiti tributari riferibili al ramo d'azienda acquistato.

**Pass se** &nbsp; compare l'affermazione della responsabilita' solidale della societa' quale cessionaria del ramo

**Fail se** &nbsp; la responsabilita' solidale non e' trattata.

*Non passa al judge:* fonte: art. 14, comma 1, d.lgs. 472/1997 | gravita': alta

### B.19  [issue: I-11]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che la responsabilita' e' assistita dal beneficio della preventiva escussione della cedente.

**Pass se** &nbsp; compare una fra: «beneficio della preventiva escussione», «previa escussione del cedente», «responsabilita' sussidiaria»

**Fail se** &nbsp; la responsabilita' e' presentata come solidale senza beneficio di escussione, oppure il punto non e' trattato.

*Non passa al judge:* fonte: art. 14, comma 1, d.lgs. 472/1997 | gravita': media

### B.20  [issue: I-11]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable indica euro 1.150.000,00 come limite quantitativo della responsabilita' solidale.

**Pass se** &nbsp; compare «1.150.000» come limite della responsabilita' solidale

**Fail se** &nbsp; e' indicato un limite diverso, oppure il limite non e' indicato.

*Non passa al judge:* fonte: atto di cessione di ramo d'azienda, articolo 5 | gravita': alta

### B.21  [issue: I-11]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che l'importo della responsabilita' solidale non e' determinabile dal fascicolo e indica il certificato dell'ufficio fra i documenti da acquisire.

**Pass se** &nbsp; compare la richiesta del certificato dell'ufficio sui carichi pendenti della cedente

**Fail se** &nbsp; la richiesta del certificato non compare.

*Non passa al judge:* fonte: art. 14, comma 3, d.lgs. 472/1997 | gravita': alta

### B.22  [issue: I-11]  [tipo: assenza]  [judge]

**Verifica** &nbsp; il deliverable non afferma che la garanzia contrattuale rilasciata dalla cedente nell'atto di cessione esclude la responsabilita' verso l'amministrazione finanziaria.

**Pass se** &nbsp; non compare l'affermazione che la garanzia dell'articolo 7 dell'atto di cessione elimina la responsabilita' solidale

**Fail se** &nbsp; la garanzia contrattuale e' presentata come causa di esclusione della responsabilita' verso l'amministrazione finanziaria.

*Non passa al judge:* fonte: atto di cessione di ramo d'azienda, articolo 7; nota del direttore amministrativo | gravita': alta

### B.23  [issue: I-12]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che la disapplicazione della sanzione non opera per il periodo d'imposta 2026.

**Pass se** &nbsp; compare una fra: «la penalty protection non opera», «la disapplicazione della sanzione non spetta», «la documentazione non produce l'effetto di esimente»

**Fail se** &nbsp; la disapplicazione e' presentata come operante, oppure il punto non e' trattato.

*Non passa al judge:* fonte: art. 1, comma 6, d.lgs. 471/1997 | gravita': alta

### B.24  [issue: I-12]  [tipo: attribuzione]  [judge]

**Verifica** &nbsp; il deliverable riconduce il difetto alla marca temporale apposta dopo la presentazione della dichiarazione.

**Pass se** &nbsp; compare il riferimento alla marca temporale del 12 novembre 2027 posteriore alla presentazione della dichiarazione del 29 ottobre 2027

**Fail se** &nbsp; il difetto e' agganciato a un elemento diverso, oppure non e' agganciato ad alcun elemento.

*Non passa al judge:* fonte: documentazione nazionale, attestazione di sottoscrizione | gravita': alta

### B.25  [issue: I-12]  [tipo: assenza]  [judge]

**Verifica** &nbsp; il deliverable non afferma che manchi la comunicazione del possesso della documentazione nella dichiarazione dei redditi.

**Pass se** &nbsp; non compare l'affermazione che la comunicazione del possesso non sia stata effettuata

**Fail se** &nbsp; la mancata comunicazione del possesso e' indicata fra i difetti.

*Non passa al judge:* fonte: nota del direttore amministrativo | gravita': media

### B.26  [issue: I-13]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che la garanzia fiscale della bozza di contratto scade prima dei termini di decadenza di alcuni periodi d'imposta.

**Pass se** &nbsp; compare l'affermazione che la durata della garanzia e' piu' breve dei termini per l'accertamento, oppure che alcuni periodi restano privi di copertura

**Fail se** &nbsp; la garanzia e' presentata come coincidente con i termini di decadenza, oppure il punto non e' trattato.

*Non passa al judge:* fonte: bozza di contratto, articolo 9.4 | gravita': alta

### B.27  [issue: I-14]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che dall'indennizzo si deducono gli importi accantonati nel bilancio di riferimento.

**Pass se** &nbsp; compare il riferimento alla deduzione degli importi accantonati dall'indennizzo

**Fail se** &nbsp; la deduzione non e' trattata.

*Non passa al judge:* fonte: bozza di contratto, articolo 9.5 | gravita': alta

### B.28  [issue: I-15]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable indica fra i documenti da richiedere le dichiarazioni dei redditi dei periodi d'imposta verificati.

**Pass se** &nbsp; compare la richiesta delle dichiarazioni dei redditi dei periodi verificati

**Fail se** &nbsp; la richiesta non compare.

*Non passa al judge:* fonte: composizione del fascicolo | gravita': media

### B.29  [issue: I-15]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che il fascicolo non consente di stabilire l'esito dei rilievi.

**Pass se** &nbsp; compare una fra: «non e' possibile stabilire», «non e' determinabile allo stato», «resta da verificare», «l'esito dipende da elementi non disponibili» riferito ai rilievi

**Fail se** &nbsp; il deliverable afferma che i rilievi saranno accolti oppure che saranno respinti.

*Non passa al judge:* fonte: composizione del fascicolo | gravita': alta

### B.30  [issue: I-04]  [tipo: assenza]  [judge]

**Verifica** &nbsp; simmetria del controllo: il deliverable non afferma che il periodo d'imposta 2021 sia ancora accertabile.

**Pass se** &nbsp; non compare l'affermazione che il periodo d'imposta 2021 sia ancora accertabile

**Fail se** &nbsp; il periodo d'imposta 2021 e' presentato come ancora accertabile.

*Non passa al judge:* fonte: art. 43 d.P.R. 600/1973 | gravita': alta

### B.31  [issue: I-04]  [tipo: assenza]  [judge]

**Verifica** &nbsp; sovra-segnalazione: il deliverable non inserisce il rilievo n. 1 sul periodo d'imposta 2021 fra le passivita' potenziali della matrice.

**Pass se** &nbsp; il rilievo n. 1 non compare fra le voci con esposizione stimata

**Fail se** &nbsp; il rilievo n. 1 e' conteggiato fra le passivita' potenziali.

*Non passa al judge:* fonte: processo verbale di constatazione, rilievo n. 1 | gravita': alta

### B.32  [issue: I-15]  [tipo: assenza]  [judge]

**Verifica** &nbsp; sovra-segnalazione: il deliverable non inserisce la comunicazione di irregolarita' del giugno 2027 fra le passivita' aperte.

**Pass se** &nbsp; la comunicazione di irregolarita' non compare fra le voci con esposizione stimata

**Fail se** &nbsp; la comunicazione di irregolarita' e' presentata come passivita' aperta.

*Non passa al judge:* fonte: comunicazione di irregolarita'; quietanza del modello F24 | gravita': alta

### B.33  [issue: I-14]  [tipo: assenza]  [judge]

**Verifica** &nbsp; sovra-segnalazione: il deliverable non presenta come esposizione per l'acquirente la franchigia dell'articolo 8.3.

**Pass se** &nbsp; la franchigia non compare fra i profili sfavorevoli all'acquirente in materia fiscale

**Fail se** &nbsp; la franchigia e' presentata come limite che riduce la tutela dell'acquirente sulle passivita' fiscali.

*Non passa al judge:* fonte: bozza di contratto, articolo 9.7 | gravita': alta

### B.34  [issue: I-05]  [tipo: assenza]  [judge]

**Verifica** &nbsp; sovra-segnalazione: il deliverable non presenta il limite massimo di indennizzo dell'articolo 9.6 come incapiente rispetto all'esposizione fiscale.

**Pass se** &nbsp; il limite massimo non compare fra i profili di esposizione non coperta

**Fail se** &nbsp; il limite massimo e' presentato come insufficiente rispetto all'esposizione fiscale.

*Non passa al judge:* fonte: bozza di contratto, articolo 9.6 | gravita': media

### B.35  [issue: I-11]  [tipo: assenza]  [judge]

**Verifica** &nbsp; sovra-segnalazione: il deliverable non afferma che l'acquirente delle quote risponde in solido quale cessionario d'azienda.

**Pass se** &nbsp; non compare l'affermazione che l'acquirente delle quote risponda ai sensi della disciplina sulla cessione di azienda

**Fail se** &nbsp; la responsabilita' solidale e' attribuita all'acquirente delle quote.

*Non passa al judge:* fonte: bozza di contratto, articolo 2; art. 14 d.lgs. 472/1997 | gravita': alta

### B.36  [issue: I-12]  [tipo: assenza]  [judge]

**Verifica** &nbsp; sovra-segnalazione: il deliverable non segnala come rilievo la congruita' dei prezzi di trasferimento praticati con la controllata spagnola.

**Pass se** &nbsp; la congruita' dei prezzi di trasferimento non compare fra i rilievi

**Fail se** &nbsp; la congruita' dei prezzi di trasferimento e' segnalata come rilievo.

*Non passa al judge:* fonte: documentazione nazionale, capitolo 2 | gravita': media

### B.37  [issue: I-15]  [tipo: assenza]  [judge]

**Verifica** &nbsp; divieto di presunzione dell'esito: il deliverable non afferma che i rilievi del processo verbale saranno annullati in sede di contraddittorio o di ricorso.

**Pass se** &nbsp; non compare l'affermazione che i rilievi saranno annullati

**Fail se** &nbsp; il deliverable presenta l'annullamento dei rilievi come esito atteso.

*Non passa al judge:* fonte: composizione del fascicolo alla data di riferimento | gravita': alta

## C. Date e valori calcolati

### C.1  [issue: I-01]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable indica euro 148.800,00 come maggiore IRES del rilievo n. 3.

**Pass se** &nbsp; compare «148.800» riferito al rilievo sulle sponsorizzazioni

**Fail se** &nbsp; e' indicato un importo diverso, oppure l'importo non e' indicato.

*Non passa al judge:* fonte: processo verbale di constatazione, rilievo n. 3 | gravita': alta

### C.2  [issue: I-02]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable indica euro 136.400,00 come maggiore IVA del rilievo n. 4.

**Pass se** &nbsp; compare «136.400» riferito al rilievo sull'imposta sul valore aggiunto

**Fail se** &nbsp; e' indicato un importo diverso, oppure l'importo non e' indicato.

*Non passa al judge:* fonte: processo verbale di constatazione, rilievo n. 4 | gravita': alta

### C.3  [issue: I-04]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable indica il 31 dicembre 2028 come termine di decadenza del periodo d'imposta 2022.

**Pass se** &nbsp; compare «31 dicembre 2028» oppure «31/12/2028» riferito al periodo d'imposta 2022

**Fail se** &nbsp; e' indicata una data diversa, oppure la data non e' indicata.

*Non passa al judge:* fonte: art. 43 d.P.R. 600/1973 | gravita': alta

### C.4  [issue: I-04]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable indica il 31 dicembre 2029 come termine di decadenza del periodo d'imposta 2023.

**Pass se** &nbsp; compare «31 dicembre 2029» oppure «31/12/2029» riferito al periodo d'imposta 2023

**Fail se** &nbsp; e' indicata una data diversa, oppure la data non e' indicata.

*Non passa al judge:* fonte: art. 43 d.P.R. 600/1973 | gravita': alta

### C.5  [issue: I-04]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che il termine di decadenza si computa dall'anno di presentazione della dichiarazione.

**Pass se** &nbsp; compare una fra: «dall'anno di presentazione», «dall'anno in cui e' stata presentata la dichiarazione», «quinto anno successivo alla presentazione»

**Fail se** &nbsp; il passaggio non compare.

*Non passa al judge:* fonte: art. 43 d.P.R. 600/1973 | gravita': media

### C.6  [issue: I-04]  [tipo: assenza]  [judge]

**Verifica** &nbsp; il deliverable non computa il termine di decadenza a partire dall'anno del periodo d'imposta.

**Pass se** &nbsp; non compare «31 dicembre 2027» ne' «31/12/2027» come termine di decadenza del periodo d'imposta 2022

**Fail se** &nbsp; il termine e' calcolato dall'anno del periodo d'imposta anziche' dall'anno di presentazione.

*Non passa al judge:* fonte: derivazione errata ricostruita in fase di build | gravita': alta

### C.7  [issue: I-06]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable indica euro 132.000,00 come limite di deducibilita' delle spese di rappresentanza del 2026.

**Pass se** &nbsp; compare «132.000» come limite di deducibilita'

**Fail se** &nbsp; e' indicato un limite diverso, oppure il limite non e' indicato.

*Non passa al judge:* fonte: art. 108, comma 2, TUIR; bilancio 2026 | gravita': alta

### C.8  [issue: I-06]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable indica euro 180.000,00 come eccedenza indeducibile delle spese di rappresentanza del 2026.

**Pass se** &nbsp; compare «180.000» come eccedenza indeducibile

**Fail se** &nbsp; e' indicato un importo diverso, oppure l'importo non e' indicato.

*Non passa al judge:* fonte: bilancio 2026, nota integrativa | gravita': alta

### C.9  [issue: I-06]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable indica euro 43.200,00 come maggiore IRES del periodo d'imposta 2026.

**Pass se** &nbsp; compare «43.200» come maggiore IRES del periodo d'imposta 2026

**Fail se** &nbsp; e' indicato un importo diverso, oppure l'importo non e' indicato.

*Non passa al judge:* fonte: art. 77 TUIR | gravita': alta

### C.10  [issue: I-06]  [tipo: assenza]  [judge]

**Verifica** &nbsp; il deliverable non indica euro 74.880,00 come maggiore IRES del periodo d'imposta 2026.

**Pass se** &nbsp; non compare «74.880»

**Fail se** &nbsp; compare «74.880» come maggiore imposta del periodo d'imposta 2026, cioe' la maggiore imposta e' calcolata sull'intero importo delle spese di rappresentanza anziche' sull'eccedenza.

*Non passa al judge:* fonte: derivazione errata ricostruita in fase di build | gravita': alta

### C.11  [issue: I-08]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable indica euro 3.600.000,00 come soglia della grandezza dei ricavi.

**Pass se** &nbsp; compare «3.600.000» come soglia dei ricavi

**Fail se** &nbsp; e' indicata una soglia diversa, oppure la soglia non e' indicata.

*Non passa al judge:* fonte: art. 84, comma 3-bis, TUIR; bilanci 2026 e 2027 | gravita': alta

### C.12  [issue: I-08]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable indica euro 920.000,00 come soglia della grandezza delle spese per prestazioni di lavoro subordinato.

**Pass se** &nbsp; compare «920.000» come soglia delle spese per prestazioni di lavoro subordinato

**Fail se** &nbsp; e' indicata una soglia diversa, oppure la soglia non e' indicata.

*Non passa al judge:* fonte: art. 84, comma 3-bis, TUIR; bilanci 2026 e 2027 | gravita': alta

### C.13  [issue: I-08]  [tipo: presenza]  [judge]

**Verifica** &nbsp; il deliverable afferma che il confronto si effettua con il quaranta per cento della media dei due esercizi anteriori.

**Pass se** &nbsp; compare il riferimento al quaranta per cento della media dei due esercizi anteriori

**Fail se** &nbsp; il passaggio non compare.

*Non passa al judge:* fonte: art. 84, comma 3-bis, TUIR | gravita': alta

### C.14  [issue: I-08]  [tipo: assenza]  [judge]

**Verifica** &nbsp; il deliverable non confronta i dati del 2027 con la media dei due esercizi anteriori senza applicare il quaranta per cento.

**Pass se** &nbsp; non compare l'affermazione che il test non e' superato perche' i dati del 2027 sono inferiori alla media dei due esercizi anteriori

**Fail se** &nbsp; il confronto e' effettuato con la media anziche' con il quaranta per cento della media.

*Non passa al judge:* fonte: derivazione errata ricostruita in fase di build | gravita': alta

### C.15  [issue: I-08]  [tipo: assenza]  [judge]

**Verifica** &nbsp; il deliverable non calcola la media di riferimento sugli esercizi 2027 e 2026.

**Pass se** &nbsp; non compare una media calcolata sugli esercizi 2027 e 2026

**Fail se** &nbsp; la media e' calcolata includendo l'esercizio 2027.

*Non passa al judge:* fonte: derivazione errata ricostruita in fase di build | gravita': media

### C.16  [issue: I-09]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable indica euro 890.000,00 come importo massimo delle perdite riportabili.

**Pass se** &nbsp; compare «890.000» come importo massimo riportabile

**Fail se** &nbsp; e' indicato un importo diverso, oppure l'importo non e' indicato.

*Non passa al judge:* fonte: art. 84, comma 3-ter, TUIR; bilancio 2027 | gravita': alta

### C.17  [issue: I-09]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable indica euro 2.530.000,00 come importo delle perdite non riportabili.

**Pass se** &nbsp; compare «2.530.000» come importo delle perdite non riportabili

**Fail se** &nbsp; e' indicato un importo diverso, oppure l'importo non e' indicato.

*Non passa al judge:* fonte: art. 84, comma 3-ter, TUIR; bilancio 2027 | gravita': alta

### C.18  [issue: I-09]  [tipo: assenza]  [judge]

**Verifica** &nbsp; il deliverable non indica euro 1.310.000,00 come importo massimo delle perdite riportabili.

**Pass se** &nbsp; non compare «1.310.000» come importo massimo riportabile

**Fail se** &nbsp; il tetto e' calcolato senza sottrarre il versamento in conto capitale.

*Non passa al judge:* fonte: derivazione errata ricostruita in fase di build | gravita': alta

### C.19  [issue: I-09]  [tipo: assenza]  [judge]

**Verifica** &nbsp; il deliverable non indica euro 470.000,00 come importo massimo delle perdite riportabili.

**Pass se** &nbsp; non compare «470.000» come importo massimo riportabile

**Fail se** &nbsp; compare «470.000» come importo massimo riportabile, cioe' il tetto e' calcolato sottraendo il doppio dei versamenti in assenza della relazione giurata di stima.

*Non passa al judge:* fonte: derivazione errata ricostruita in fase di build | gravita': alta

### C.20  [issue: I-09]  [tipo: assenza]  [judge]

**Verifica** &nbsp; il deliverable non afferma che le perdite fiscali sono riportabili per l'intero importo di euro 3.420.000,00.

**Pass se** &nbsp; non compare l'affermazione che l'intero importo delle perdite resti riportabile

**Fail se** &nbsp; le perdite sono presentate come integralmente riportabili.

*Non passa al judge:* fonte: art. 84, commi 3 e 3-ter, TUIR | gravita': alta

### C.21  [issue: I-05]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable indica euro 328.400,00 come esposizione complessiva in imposta.

**Pass se** &nbsp; compare «328.400» come esposizione complessiva in imposta

**Fail se** &nbsp; e' indicato un importo diverso, oppure l'importo non e' indicato.

*Non passa al judge:* fonte: processo verbale di constatazione; bilancio 2026 | gravita': alta

### C.22  [issue: I-14]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable indica euro 178.400,00 come importo indennizzabile al netto dell'accantonamento.

**Pass se** &nbsp; compare «178.400» come importo indennizzabile al netto dell'accantonamento

**Fail se** &nbsp; e' indicato un importo diverso, oppure l'importo non e' indicato.

*Non passa al judge:* fonte: bozza di contratto, articolo 9.5; bilancio 2027 | gravita': alta

### C.23  [issue: I-13]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable indica il 28 aprile 2030 come scadenza della garanzia fiscale.

**Pass se** &nbsp; compare «28 aprile 2030» oppure «28/04/2030» come scadenza della garanzia fiscale

**Fail se** &nbsp; e' indicata una data diversa, oppure la data non e' indicata.

*Non passa al judge:* fonte: bozza di contratto, articoli 4 e 9.4 | gravita': alta

### C.24  [issue: I-13]  [tipo: valore]  [verifica meccanica]

**Verifica** &nbsp; il deliverable indica i periodi d'imposta 2024, 2025, 2026 e 2027 come periodi privi di copertura contrattuale.

**Pass se** &nbsp; compaiono, indicati come periodi privi di copertura, «2024», «2025», «2026» e «2027»

**Fail se** &nbsp; manca uno dei quattro periodi, oppure l'elenco non e' indicato.

*Non passa al judge:* fonte: bozza di contratto, articolo 9.4; art. 43 d.P.R. 600/1973 | gravita': alta

### C.25  [issue: I-13]  [tipo: assenza]  [judge]

**Verifica** &nbsp; il deliverable non indica il periodo d'imposta 2023 fra i periodi privi di copertura contrattuale.

**Pass se** &nbsp; il periodo d'imposta 2023 non compare fra i periodi privi di copertura

**Fail se** &nbsp; il periodo d'imposta 2023 e' indicato fra i periodi scoperti.

*Non passa al judge:* fonte: art. 43 d.P.R. 600/1973 | gravita': media

