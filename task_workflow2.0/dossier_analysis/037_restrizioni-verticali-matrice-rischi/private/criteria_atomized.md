# WF2-037 — Rubrica atomizzata

Forma a campi somministrata al judge e alla verifica meccanica. Generato da `source/gen/build_rubric_037.py` insieme a `private/rubric.json`: non modificare a mano.

Issue di merito: 16. Criteri atomici: 58, di cui 13 a verifica meccanica e 45 al judge.

---

## A. Forma dell'output  (interamente verifica meccanica)

### A.1  [issue: A]  [tipo: valore]  [verifica meccanica]

**Verifica** — il deliverable è un file denominato matrice_rischi_antitrust.md di lunghezza non superiore a 2.800 parole.

**Pass se** — il file si chiama matrice_rischi_antitrust.md e il conteggio delle parole non supera 2.800

**Fail se** — il nome del file è diverso oppure il conteggio supera 2.800 parole.

<small>—— non passa al judge —— Fonte: response_template.md · Gravità: bassa</small>

### A.2  [issue: A]  [tipo: struttura]  [verifica meccanica]

**Verifica** — il deliverable contiene, nell'ordine, otto sezioni intitolate: Matrice dei rischi; Come ho qualificato ciascun elemento; Elementi che non costituiscono restrizione o che sono coperti dall'esenzione; Soglie e quote di mercato; Verifica della posizione della direzione commerciale; Azioni, in ordine di urgenza; Che cosa non è determinabile allo stato e che cosa serve; Questioni riservate al parere legale.

**Pass se** — le otto intestazioni compaiono tutte e nell'ordine indicato

**Fail se** — manca una intestazione oppure l'ordine è diverso.

<small>—— non passa al judge —— Fonte: response_template.md · Gravità: bassa</small>

### A.3  [issue: A]  [tipo: struttura]  [verifica meccanica]

**Verifica** — ogni riga della matrice riporta il documento e la clausola da cui l'elemento risulta.

**Pass se** — nessuna riga della matrice ha vuota la colonna del documento e della clausola

**Fail se** — almeno una riga non riporta il documento oppure non riporta la clausola.

<small>—— non passa al judge —— Fonte: response_template.md · Gravità: media</small>

### A.4  [issue: A]  [tipo: valore]  [verifica meccanica]

**Verifica** — in ogni riga della matrice la colonna della qualificazione riporta una sola fra le cinque etichette dell'elenco chiuso: restrizione fondamentale, restrizione esclusa, coperta dall'esenzione, fuori dall'esenzione da valutare, non restrittiva.

**Pass se** — ogni riga porta esattamente una delle cinque etichette e nessuna riga porta un'etichetta diversa

**Fail se** — compare un'etichetta estranea all'elenco chiuso, oppure una riga ne porta più di una, oppure una riga non ne porta alcuna.

<small>—— non passa al judge —— Fonte: response_template.md · Gravità: alta</small>

### A.5  [issue: A]  [tipo: struttura]  [verifica meccanica]

**Verifica** — ogni riga della matrice riporta la colonna dei presupposti da cui la qualificazione dipende.

**Pass se** — nessuna riga della matrice ha vuota la colonna dei presupposti

**Fail se** — almeno una riga non riporta i presupposti.

<small>—— non passa al judge —— Fonte: response_template.md · Gravità: media</small>

### A.6  [issue: A]  [tipo: struttura]  [verifica meccanica]

**Verifica** — ogni riga della matrice riporta un'azione.

**Pass se** — nessuna riga della matrice ha vuota la colonna dell'azione

**Fail se** — almeno una riga non riporta un'azione.

<small>—— non passa al judge —— Fonte: response_template.md · Gravità: media</small>

### A.7  [issue: A]  [tipo: assenza]  [verifica meccanica]

**Verifica** — il deliverable non contiene riferimenti normativi, di soft law o giurisprudenziali diversi da quelli elencati nella tabella dell'elenco chiuso di 03_legal_sources.md.

**Pass se** — tutti i riferimenti presenti compaiono nell'elenco chiuso

**Fail se** — compare un riferimento estraneo all'elenco chiuso.

<small>—— non passa al judge —— Fonte: 03_legal_sources.md · Gravità: alta</small>

### A.8  [issue: I-16]  [tipo: struttura]  [verifica meccanica]

**Verifica** — la sezione 8 del deliverable non è vuota.

**Pass se** — la sezione Questioni riservate al parere legale contiene almeno una voce

**Fail se** — la sezione è vuota oppure contiene la sola indicazione che non vi sono questioni riservate.

<small>—— non passa al judge —— Fonte: response_template.md · Gravità: alta</small>

---

## B. Merito

Fascicolo in corso alla data di riferimento del 16 marzo 2029: la diffida è stata ricevuta, nessun procedimento è aperto, la politica di prezzo è in corso di applicazione e i contratti sono in vigore. Il deliverable è una matrice dei rischi con qualificazione e azioni. I criteri riguardano la qualificazione degli elementi del fascicolo, i presupposti da cui essa dipende e le azioni indicate; non riguardano l'esito di un eventuale procedimento né la quantificazione dell'esposizione. Le etichette di qualificazione sono un elenco chiuso di cinque voci, esposto al modello nel response_template: i criteri di tipo qualificazione verificano quale etichetta compare, non un giudizio del judge sulla gravità.

### B.1  [issue: I-01]  [tipo: qualificazione]  [judge]

**Verifica** — la matrice qualifica come restrizione fondamentale la politica di prezzo al pubblico risultante dalla circolare alla Rete e dall'email dell'Area Manager.

**Pass se** — nella riga relativa a quella politica compare l'etichetta «restrizione fondamentale»

**Fail se** — quella politica è qualificata con una delle altre quattro etichette, oppure non compare nella matrice.

**Indifferente** — l'uso dell'espressione «imposizione dei prezzi di rivendita» accanto all'etichetta.

<small>—— non passa al judge —— Fonte: documenti 04 e 05; art. 4, lett. a), reg. (UE) 2022/720 · Gravità: alta</small>

### B.2  [issue: I-01]  [tipo: attribuzione]  [judge]

**Verifica** — il deliverable riconduce la qualificazione della politica di prezzo alla combinazione fra la circolare e la minaccia contenuta nell'email dell'Area Manager.

**Pass se** — la qualificazione è agganciata a entrambi i documenti: la circolare alla Rete e l'email dell'Area Manager

**Fail se** — la qualificazione è agganciata a uno solo dei due documenti, oppure a nessuno.

**Indifferente** — il richiamo anche dell'obbligo di segnalazione degli scostamenti.

<small>—— non passa al judge —— Fonte: documenti 04 e 05 · Gravità: alta</small>

### B.3  [issue: I-01]  [tipo: assenza]  [judge]

**Verifica** — il deliverable non fonda la qualificazione della politica di prezzo sulla sola raccomandazione dei prezzi di rivendita.

**Pass se** — non compare l'affermazione che la raccomandazione dei prezzi sia, in sé, un'imposizione dei prezzi di rivendita

**Fail se** — la qualificazione è fondata sulla sola esistenza di prezzi raccomandati.

<small>—— non passa al judge —— Fonte: art. 4, lett. a), reg. (UE) 2022/720; Orientamenti, punto (188) · Gravità: alta</small>

### B.4  [issue: I-02]  [tipo: presenza]  [judge]

**Verifica** — il deliverable afferma che la qualificazione come restrizione fondamentale non dipende dalla quota di mercato.

**Pass se** — compare una fra le formulazioni seguenti:
- compare l'affermazione che la restrizione fondamentale elimina il beneficio dell'esenzione a prescindere dalla quota
- compare l'affermazione che la soglia del 30 per cento non rileva per le restrizioni fondamentali
- compare l'affermazione che la questione della definizione del mercato non incide su quella qualificazione

**Fail se** — il deliverable subordina la qualificazione alla verifica della soglia, oppure il punto non è trattato.

<small>—— non passa al judge —— Fonte: art. 4 reg. (UE) 2022/720 · Gravità: alta</small>

### B.5  [issue: I-02]  [tipo: presenza]  [judge]

**Verifica** — il deliverable afferma che la comunicazione sugli accordi di importanza minore non si applica agli accordi che hanno per oggetto di restringere la concorrenza.

**Pass se** — compare una fra le formulazioni seguenti:
- compare l'affermazione che il de minimis non copre le restrizioni per oggetto
- compare l'affermazione che la soglia del 15 per cento non è invocabile per le restrizioni fondamentali

**Fail se** — il punto non è trattato, oppure il deliverable ammette il de minimis per quella condotta.

<small>—— non passa al judge —— Fonte: comunicazione de minimis, punti 2 e 13 · Gravità: alta</small>

### B.6  [issue: I-03]  [tipo: qualificazione]  [judge]

**Verifica** — la matrice qualifica come restrizione fondamentale la clausola del contratto di distribuzione esclusiva che vieta al distributore di dare seguito agli ordini provenienti da fuori territorio.

**Pass se** — nella riga relativa a quella clausola compare l'etichetta «restrizione fondamentale»

**Fail se** — quella clausola è qualificata con una delle altre quattro etichette, oppure non compare nella matrice.

**Indifferente** — l'uso dell'espressione «vendite passive» accanto all'etichetta.

<small>—— non passa al judge —— Fonte: documento 02, art. 4, comma 3; art. 4, lett. b), reg. (UE) 2022/720 · Gravità: alta</small>

### B.7  [issue: I-03]  [tipo: presenza]  [judge]

**Verifica** — il deliverable afferma che l'eccezione prevista per la distribuzione esclusiva copre le sole vendite attive.

**Pass se** — compare una fra le formulazioni seguenti:
- compare l'affermazione che l'eccezione riguarda le vendite attive e non le passive
- compare l'affermazione che le vendite passive non possono essere restrette

**Fail se** — il punto non è trattato.

<small>—— non passa al judge —— Fonte: art. 4, lett. b), punto i), reg. (UE) 2022/720 · Gravità: alta</small>

### B.8  [issue: I-04]  [tipo: qualificazione]  [judge]

**Verifica** — la matrice qualifica come restrizione fondamentale la clausola del contratto di distribuzione selettiva che vieta ai Rivenditori Autorizzati di cedere i Prodotti ad altri Rivenditori Autorizzati.

**Pass se** — nella riga relativa a quella clausola compare l'etichetta «restrizione fondamentale»

**Fail se** — quella clausola è qualificata con una delle altre quattro etichette, oppure non compare nella matrice.

**Indifferente** — l'uso dell'espressione «forniture incrociate» accanto all'etichetta.

<small>—— non passa al judge —— Fonte: documento 01, art. 7, comma 2; art. 4, lett. c), punto ii), reg. (UE) 2022/720 · Gravità: alta</small>

### B.9  [issue: I-04]  [tipo: attribuzione]  [judge]

**Verifica** — il deliverable riconduce quella qualificazione all'articolo 7, comma 2, del contratto di distribuzione selettiva.

**Pass se** — compare una fra le formulazioni seguenti:
- la qualificazione è agganciata all'articolo 7, comma 2, del contratto di distribuzione selettiva
- la qualificazione è agganciata alla clausola del documento 01 che vieta le cessioni fra Rivenditori Autorizzati

**Fail se** — la qualificazione non è agganciata ad alcuna clausola determinata.

<small>—— non passa al judge —— Fonte: documento 01, art. 7, comma 2 · Gravità: media</small>

### B.10  [issue: I-05]  [tipo: qualificazione]  [judge]

**Verifica** — la matrice qualifica la maggiorazione del prezzo all'ingrosso per le unità destinate al canale online con una delle due etichette «coperta dall'esenzione» o «fuori dall'esenzione, da valutare».

**Pass se** — nella riga relativa alla maggiorazione compare una fra le etichette «coperta dall'esenzione» e «fuori dall'esenzione, da valutare»

**Fail se** — la maggiorazione è qualificata come «restrizione fondamentale», come «restrizione esclusa» o come «non restrittiva», oppure non compare nella matrice.

**Indifferente** — quale delle due etichette ammesse è stata scelta.

<small>—— non passa al judge —— Fonte: documento 03, art. 5; Orientamenti, punto (209) · Gravità: alta</small>

### B.11  [issue: I-05]  [tipo: presenza]  [judge]

**Verifica** — il deliverable afferma che la qualificazione della maggiorazione dipende dalla connessione fra la differenza di prezzo e le differenze di investimenti e costi sostenuti per ciascun canale.

**Pass se** — compare una fra le formulazioni seguenti:
- compare il riferimento alla connessione fra la differenza di prezzo e gli investimenti o i costi di canale
- compare l'affermazione che occorre verificare se la differenza sia ragionevolmente connessa ai costi
- compare l'affermazione che occorre verificare se la vendita online resti redditizia

**Fail se** — il punto non è trattato.

<small>—— non passa al judge —— Fonte: Orientamenti, punto (209) · Gravità: alta</small>

### B.12  [issue: I-05]  [tipo: assenza]  [judge]

**Verifica** — il deliverable non afferma che la maggiorazione del prezzo all'ingrosso per il canale online è una restrizione fondamentale.

**Pass se** — non compare l'affermazione che quella maggiorazione sia di per sé vietata o fondamentale

**Fail se** — la maggiorazione è presentata come restrizione fondamentale o come violazione.

<small>—— non passa al judge —— Fonte: Orientamenti, punto (209) · Gravità: alta</small>

### B.13  [issue: I-06]  [tipo: qualificazione]  [judge]

**Verifica** — la matrice qualifica come restrizione esclusa l'obbligo di non concorrenza di sette anni previsto dal contratto di distribuzione selettiva.

**Pass se** — nella riga relativa a quell'obbligo compare l'etichetta «restrizione esclusa»

**Fail se** — quell'obbligo è qualificato con una delle altre quattro etichette, oppure non compare nella matrice.

**Indifferente** — il richiamo del limite di cinque anni.

<small>—— non passa al judge —— Fonte: documento 01, art. 12; art. 5, par. 1, lett. a), reg. (UE) 2022/720 · Gravità: alta</small>

### B.14  [issue: I-06]  [tipo: assenza]  [judge]

**Verifica** — il deliverable non qualifica l'obbligo di non concorrenza come restrizione fondamentale.

**Pass se** — l'etichetta «restrizione fondamentale» non compare nella riga relativa all'obbligo di non concorrenza

**Fail se** — l'obbligo di non concorrenza è qualificato come restrizione fondamentale.

<small>—— non passa al judge —— Fonte: art. 5, par. 1, lett. a), reg. (UE) 2022/720 · Gravità: alta</small>

### B.15  [issue: I-07]  [tipo: presenza]  [judge]

**Verifica** — il deliverable afferma che una restrizione fondamentale elimina il beneficio dell'esenzione per l'intero accordo che la contiene.

**Pass se** — compare una fra le formulazioni seguenti:
- compare l'affermazione che l'esenzione non si applica all'accordo nel suo complesso
- compare l'affermazione che l'intero accordo perde il beneficio dell'esenzione

**Fail se** — il punto non è trattato.

<small>—— non passa al judge —— Fonte: art. 4 reg. (UE) 2022/720 · Gravità: alta</small>

### B.16  [issue: I-07]  [tipo: presenza]  [judge]

**Verifica** — il deliverable afferma che una restrizione esclusa non è esentata ma le altre clausole del medesimo accordo conservano l'esenzione.

**Pass se** — compare una fra le formulazioni seguenti:
- compare l'affermazione che la restrizione esclusa è scindibile
- compare l'affermazione che l'esenzione non si applica al solo obbligo e resta per il resto dell'accordo
- compare l'affermazione che le altre clausole restano esentate

**Fail se** — il punto non è trattato, oppure il deliverable afferma che l'intero contratto selettivo perde l'esenzione per effetto dell'obbligo di non concorrenza.

<small>—— non passa al judge —— Fonte: art. 5 reg. (UE) 2022/720 · Gravità: alta</small>

### B.17  [issue: I-08]  [tipo: qualificazione]  [judge]

**Verifica** — la matrice qualifica come «fuori dall'esenzione, da valutare» lo scambio di informazioni avvenuto nel comitato commerciale.

**Pass se** — nella riga relativa allo scambio di informazioni compare l'etichetta «fuori dall'esenzione, da valutare»

**Fail se** — lo scambio è qualificato con una delle altre quattro etichette, oppure non compare nella matrice.

<small>—— non passa al judge —— Fonte: documento 06; art. 2, par. 5, reg. (UE) 2022/720 · Gravità: alta</small>

### B.18  [issue: I-08]  [tipo: attribuzione]  [judge]

**Verifica** — il deliverable riconduce quella qualificazione alla comunicazione, da parte dei rivenditori, dei prezzi che intendono praticare nel trimestre successivo.

**Pass se** — la qualificazione è agganciata allo scambio dei prezzi futuri o dei prezzi del trimestre successivo

**Fail se** — quel contenuto dello scambio non è richiamato.

<small>—— non passa al judge —— Fonte: documento 06, punto 3; Orientamenti, punto (100), lett. a) · Gravità: alta</small>

### B.19  [issue: I-08]  [tipo: attribuzione]  [judge]

**Verifica** — il deliverable riconduce quella qualificazione anche alla distribuzione dell'elenco nominativo dei clienti professionali.

**Pass se** — la qualificazione è agganciata anche allo scambio di dati relativi a utenti finali identificati o all'elenco nominativo dei clienti

**Fail se** — quel contenuto dello scambio non è richiamato.

<small>—— non passa al judge —— Fonte: documento 06, punto 5; Orientamenti, punto (100), lett. b) · Gravità: alta</small>

### B.20  [issue: I-09]  [tipo: presenza]  [judge]

**Verifica** — il deliverable afferma che il fornitore vende anche direttamente agli utilizzatori finali e che si è quindi in una situazione di duplice distribuzione.

**Pass se** — compare una fra le formulazioni seguenti:
- compare una fra: «duplice distribuzione»
- «distribuzione duale»
- «il fornitore opera anche a valle»
- «il fornitore è anche concorrente dei rivenditori a valle»

**Fail se** — il punto non è trattato.

<small>—— non passa al judge —— Fonte: documento 03, art. 2; art. 2, par. 4, reg. (UE) 2022/720 · Gravità: media</small>

### B.21  [issue: I-09]  [tipo: assenza]  [judge]

**Verifica** — il deliverable non afferma che la vendita diretta del fornitore agli utilizzatori finali fa venire meno l'esenzione per l'intero rapporto con la Rete.

**Pass se** — non compare l'affermazione che la vendita diretta escluda l'esenzione per il rapporto verticale

**Fail se** — il deliverable conclude che l'esenzione non si applica perché il fornitore vende anche direttamente.

<small>—— non passa al judge —— Fonte: art. 2, par. 4, lett. a), reg. (UE) 2022/720 · Gravità: alta</small>

### B.22  [issue: I-10]  [tipo: presenza]  [judge]

**Verifica** — il deliverable afferma che la quota del fornitore supera il 30 per cento su una delle due definizioni del mercato e resta sotto sull'altra, e che il fascicolo non risolve quale sia il mercato rilevante.

**Pass se** — compaiono entrambe le quote e l'affermazione che la definizione del mercato non è risolta dal fascicolo

**Fail se** — è indicata una sola quota come se fosse quella rilevante, oppure il punto non è trattato.

<small>—— non passa al judge —— Fonte: documento 07; art. 3, par. 1, reg. (UE) 2022/720 · Gravità: alta</small>

### B.23  [issue: I-10]  [tipo: assenza]  [judge]

**Verifica** — il deliverable non afferma che la quota del fornitore è inferiore al 30 per cento senza indicare la definizione del mercato da cui la conclusione dipende.

**Pass se** — ogni affermazione sulla quota è accompagnata dall'indicazione del perimetro o della definizione del mercato

**Fail se** — compare un'affermazione sulla quota priva dell'indicazione del perimetro.

<small>—— non passa al judge —— Fonte: documento 07 · Gravità: alta</small>

### B.24  [issue: I-11]  [tipo: presenza]  [judge]

**Verifica** — il deliverable afferma che l'esenzione richiede anche che la quota dell'acquirente non superi il 30 per cento e che il fascicolo non contiene quel dato.

**Pass se** — compaiono entrambi gli elementi: il requisito relativo alla quota dell'acquirente e l'assenza del dato nel fascicolo

**Fail se** — il requisito relativo alla quota dell'acquirente non è richiamato, oppure è richiamato senza rilevare l'assenza del dato.

<small>—— non passa al judge —— Fonte: art. 3, par. 1, reg. (UE) 2022/720; documento 07 · Gravità: media</small>

### B.25  [issue: I-12]  [tipo: presenza]  [judge]

**Verifica** — il deliverable afferma che le quote si calcolano sui dati dell'anno civile precedente.

**Pass se** — compare il riferimento all'anno civile precedente come base di calcolo delle quote

**Fail se** — il punto non è trattato.

<small>—— non passa al judge —— Fonte: art. 8, lett. b), reg. (UE) 2022/720 · Gravità: media</small>

### B.26  [issue: I-12]  [tipo: presenza]  [judge]

**Verifica** — il deliverable afferma che, quando la soglia del 30 per cento viene superata dopo esserne stata sotto, l'esenzione continua ad applicarsi per un periodo di due anni civili.

**Pass se** — compare il riferimento al periodo di due anni civili successivo al primo superamento della soglia

**Fail se** — il punto non è trattato.

<small>—— non passa al judge —— Fonte: art. 8, lett. d), reg. (UE) 2022/720 · Gravità: alta</small>

### B.27  [issue: I-13]  [tipo: presenza]  [judge]

**Verifica** — il deliverable afferma che le intese vietate sono nulle.

**Pass se** — compare una fra le formulazioni seguenti:
- compare una fra: «nulle ad ogni effetto»
- «nullità dell'intesa»
- «nulla di diritto»
- «nullità delle clausole»

**Fail se** — la conseguenza civilistica non è indicata.

<small>—— non passa al judge —— Fonte: art. 2, comma 3, l. 287/1990; art. 101, par. 2, TFUE · Gravità: media</small>

### B.28  [issue: I-14]  [tipo: presenza]  [judge]

**Verifica** — il deliverable indica fra le azioni immediate la cessazione delle pressioni sui prezzi e il ritiro dell'invito ai rivenditori a segnalare gli scostamenti degli altri membri della Rete.

**Pass se** — compaiono entrambe le azioni: la cessazione delle pressioni e il ritiro dell'invito alla segnalazione

**Fail se** — compare una sola delle due azioni, oppure nessuna.

**Indifferente** — l'ordine reciproco fra le due azioni.

<small>—— non passa al judge —— Fonte: documenti 04 e 05 · Gravità: alta</small>

### B.29  [issue: I-14]  [tipo: presenza]  [judge]

**Verifica** — il deliverable indica fra le azioni una comunicazione correttiva alla Rete.

**Pass se** — compare l'indicazione di una comunicazione, circolare o lettera alla Rete che rettifichi la politica di prezzo

**Fail se** — la comunicazione correttiva non compare fra le azioni.

<small>—— non passa al judge —— Fonte: documento 04 · Gravità: alta</small>

### B.30  [issue: I-03]  [tipo: assenza]  [judge]

**Verifica** — sovra-segnalazione: il deliverable non qualifica come restrizione fondamentale la clausola che vieta al distributore esclusivo le vendite attive fuori dal Territorio Sud.

**Pass se** — l'etichetta «restrizione fondamentale» non compare nella riga relativa alla restrizione delle vendite attive

**Fail se** — la restrizione delle vendite attive è qualificata come restrizione fondamentale.

**Indifferente** — la sua qualificazione come «coperta dall'esenzione».

<small>—— non passa al judge —— Fonte: documento 02, art. 4, commi 1 e 2; art. 4, lett. b), punto i), reg. (UE) 2022/720 · Gravità: alta</small>

### B.31  [issue: I-04]  [tipo: assenza]  [judge]

**Verifica** — sovra-segnalazione: il deliverable non qualifica come restrizione fondamentale la clausola che vieta ai Rivenditori Autorizzati di vendere a distributori non autorizzati.

**Pass se** — l'etichetta «restrizione fondamentale» non compare nella riga relativa al divieto di vendere a distributori non autorizzati

**Fail se** — quel divieto è qualificato come restrizione fondamentale.

**Indifferente** — la sua qualificazione come «coperta dall'esenzione».

<small>—— non passa al judge —— Fonte: documento 01, art. 7, comma 1; art. 4, lett. c), punto i), 2), reg. (UE) 2022/720 · Gravità: alta</small>

### B.32  [issue: I-05]  [tipo: assenza]  [judge]

**Verifica** — sovra-segnalazione: il deliverable non qualifica come restrizione fondamentale il divieto di vendere i Prodotti attraverso mercati online gestiti da terzi.

**Pass se** — l'etichetta «restrizione fondamentale» non compare nella riga relativa al divieto di utilizzare i mercati online

**Fail se** — il divieto di utilizzare i mercati online è qualificato come restrizione fondamentale.

**Indifferente** — la sua qualificazione come «coperta dall'esenzione».

<small>—— non passa al judge —— Fonte: documento 01, art. 9, comma 3; Orientamenti, punto (208), lett. c) · Gravità: alta</small>

### B.33  [issue: I-05]  [tipo: assenza]  [judge]

**Verifica** — sovra-segnalazione: il deliverable non segnala come restrizione l'obbligo di gestire almeno un punto vendita o showroom non virtuale.

**Pass se** — l'obbligo di showroom non compare fra gli elementi qualificati come restrittivi

**Fail se** — l'obbligo di showroom è qualificato come «restrizione fondamentale», come «restrizione esclusa» o come «fuori dall'esenzione, da valutare».

**Indifferente** — la sua qualificazione come «coperta dall'esenzione» o come «non restrittiva».

<small>—— non passa al judge —— Fonte: documento 01, art. 4, comma 1, lett. b); Orientamenti, punto (208), lett. d) · Gravità: alta</small>

### B.34  [issue: I-01]  [tipo: assenza]  [judge]

**Verifica** — sovra-segnalazione: il deliverable non qualifica come restrizione fondamentale autonoma il servizio di rilevazione automatica dei prezzi al pubblico.

**Pass se** — l'etichetta «restrizione fondamentale» non compare nella riga relativa al servizio di rilevazione dei prezzi, considerato in sé

**Fail se** — il servizio di rilevazione dei prezzi è qualificato di per sé come restrizione fondamentale.

**Indifferente** — il suo richiamo fra gli elementi che rendono più efficace la pressione documentata nell'email.

<small>—— non passa al judge —— Fonte: documento 04, punto 3; Orientamenti, punto (191) · Gravità: alta</small>

### B.35  [issue: I-01]  [tipo: assenza]  [judge]

**Verifica** — sovra-segnalazione: il deliverable non qualifica come restrizione fondamentale la comunicazione del prezzo massimo di rivendita.

**Pass se** — l'etichetta «restrizione fondamentale» non compare nella riga relativa al prezzo massimo di rivendita

**Fail se** — il prezzo massimo di rivendita è qualificato come restrizione fondamentale.

<small>—— non passa al judge —— Fonte: documento 04, punto 1; art. 4, lett. a), reg. (UE) 2022/720 · Gravità: alta</small>

### B.36  [issue: I-04]  [tipo: assenza]  [judge]

**Verifica** — sovra-segnalazione: il deliverable non qualifica come restrizione fondamentale la clausola che subordina il trasferimento e l'apertura di punti vendita all'approvazione del fornitore.

**Pass se** — l'etichetta «restrizione fondamentale» non compare nella riga relativa al luogo di stabilimento

**Fail se** — quella clausola è qualificata come restrizione fondamentale o come ripartizione del mercato.

**Indifferente** — la sua qualificazione come «coperta dall'esenzione».

<small>—— non passa al judge —— Fonte: documento 01, art. 5, comma 2; art. 4, lett. c), punto i), 3), reg. (UE) 2022/720 · Gravità: media</small>

### B.37  [issue: I-01]  [tipo: assenza]  [judge]

**Verifica** — simmetria del controllo: il deliverable non afferma che la politica di prezzo al pubblico non presenta profili di rischio.

**Pass se** — non compare l'affermazione che sulla politica di prezzo non vi siano rilievi

**Fail se** — il deliverable conclude che la politica di prezzo è conforme.

<small>—— non passa al judge —— Fonte: documenti 04 e 05 · Gravità: alta</small>

### B.38  [issue: I-16]  [tipo: assenza]  [judge]

**Verifica** — divieto di presunzione dell'esito: il deliverable non pronostica l'esito di un eventuale procedimento dell'autorità garante.

**Pass se** — non compare un pronostico sull'esito di un procedimento, né sull'entità di una sanzione

**Fail se** — il deliverable afferma che un procedimento sarebbe vinto o perso, oppure quantifica la sanzione come esito atteso.

**Indifferente** — l'indicazione che una sanzione è possibile e che la sua entità non è determinabile allo stato.

<small>—— non passa al judge —— Fonte: 01_task.md · Gravità: alta</small>

### B.39  [issue: I-15]  [tipo: presenza]  [judge]

**Verifica** — il deliverable afferma che il fascicolo non consente di stabilire se le forniture al rivenditore siano state effettivamente sospese.

**Pass se** — compare una fra le formulazioni seguenti:
- compare una fra: «non risulta»
- «non è documentato»
- «non è possibile stabilire»
- «resta da verificare»
- riferita alla sospensione delle forniture

**Fail se** — il punto non è trattato, oppure il deliverable afferma che le forniture sono state sospese.

<small>—— non passa al judge —— Fonte: documenti 05 e 08 · Gravità: media</small>

### B.40  [issue: I-15]  [tipo: presenza]  [judge]

**Verifica** — il deliverable indica fra le informazioni da acquisire i dati di costo relativi ai due canali di vendita.

**Pass se** — compare la richiesta dei dati di costo o di investimento per canale

**Fail se** — la richiesta non compare.

<small>—— non passa al judge —— Fonte: documento 07, sezione dei dati non disponibili · Gravità: media</small>

### B.41  [issue: I-16]  [tipo: presenza]  [judge]

**Verifica** — il deliverable indica fra le questioni riservate al parere legale la definizione del mercato rilevante.

**Pass se** — la definizione del mercato rilevante compare nella sezione delle questioni riservate al parere legale

**Fail se** — la definizione del mercato non compare fra quelle questioni.

<small>—— non passa al judge —— Fonte: documento 07, nota metodologica · Gravità: alta</small>

### B.42  [issue: I-16]  [tipo: presenza]  [judge]

**Verifica** — il deliverable indica fra le questioni riservate al parere legale la valutazione dello scambio di informazioni fra i rivenditori presenti al comitato commerciale.

**Pass se** — il rilievo dello scambio fra rivenditori concorrenti compare nella sezione delle questioni riservate al parere legale

**Fail se** — quel rilievo non compare fra quelle questioni.

<small>—— non passa al judge —— Fonte: documento 06 · Gravità: media</small>

---

## C. Valori e soglie

### C.1  [issue: I-10]  [tipo: valore]  [verifica meccanica]

**Verifica** — il deliverable indica il 34,1 per cento come quota del fornitore sul perimetro dei soli utensili elettrici professionali a batteria nell'anno civile 2028.

**Pass se** — compare «34,1» oppure «34,1 %» riferito a quel perimetro

**Fail se** — è indicato un valore diverso.

**Indifferente** — l'arrotondamento a 34 per cento.

<small>—— non passa al judge —— Fonte: documento 07, perimetro A · Gravità: alta</small>

### C.2  [issue: I-10]  [tipo: valore]  [verifica meccanica]

**Verifica** — il deliverable indica il 22,4 per cento come quota del fornitore sul perimetro di tutti gli utensili elettrici portatili nell'anno civile 2028.

**Pass se** — compare «22,4» oppure «22,4 %» riferito a quel perimetro

**Fail se** — è indicato un valore diverso.

**Indifferente** — l'arrotondamento a 22 per cento.

<small>—— non passa al judge —— Fonte: documento 07, perimetro B · Gravità: alta</small>

### C.3  [issue: I-12]  [tipo: valore]  [verifica meccanica]

**Verifica** — il deliverable indica il 2028 come anno civile dei dati utilizzati per il calcolo delle quote.

**Pass se** — compare «2028» come anno dei dati rilevanti

**Fail se** — è indicato un anno diverso, oppure l'anno non è indicato.

<small>—— non passa al judge —— Fonte: art. 8, lett. b), reg. (UE) 2022/720 · Gravità: alta</small>

### C.4  [issue: I-12]  [tipo: valore]  [verifica meccanica]

**Verifica** — il deliverable indica il 2028 come primo anno in cui la soglia del 30 per cento è stata superata sul perimetro dei soli utensili professionali a batteria.

**Pass se** — compare «2028» come anno del primo superamento della soglia

**Fail se** — è indicato un anno diverso, oppure il primo superamento non è datato.

<small>—— non passa al judge —— Fonte: documento 07, serie 2026-2028 · Gravità: alta</small>

### C.5  [issue: I-12]  [tipo: presenza]  [judge]

**Verifica** — il deliverable afferma che alla data di riferimento l'esenzione non è venuta meno per effetto del superamento della soglia.

**Pass se** — compare una fra le formulazioni seguenti:
- compare una fra: «l'esenzione continua ad applicarsi»
- «l'esenzione non è ancora venuta meno»
- «il periodo di due anni civili è ancora in corso»

**Fail se** — il punto non è trattato.

<small>—— non passa al judge —— Fonte: art. 8, lett. d), reg. (UE) 2022/720 · Gravità: alta</small>

### C.6  [issue: I-12]  [tipo: assenza]  [judge]

**Verifica** — il deliverable non afferma che l'esenzione è già venuta meno per effetto del superamento della soglia nel 2028.

**Pass se** — non compare l'affermazione che l'esenzione sia venuta meno con il superamento della soglia

**Fail se** — il deliverable conclude che l'esenzione non si applica più perché la quota ha superato il 30 per cento.

<small>—— non passa al judge —— Fonte: art. 8, lett. d), reg. (UE) 2022/720 · Gravità: alta</small>

### C.7  [issue: I-05]  [tipo: valore]  [verifica meccanica]

**Verifica** — il deliverable indica nel 5 per cento la maggiorazione del prezzo all'ingrosso applicata alle unità destinate al canale online.

**Pass se** — compare «5 per cento» oppure «5 %» riferito a quella maggiorazione

**Fail se** — è indicato un valore diverso, oppure la maggiorazione non è quantificata.

**Indifferente** — l'indicazione anche degli importi in euro.

<small>—— non passa al judge —— Fonte: documento 03, art. 5 · Gravità: media</small>

### C.8  [issue: I-02]  [tipo: assenza]  [judge]

**Verifica** — il deliverable non afferma che la quota del fornitore è inferiore al 15 per cento su alcuno dei due perimetri.

**Pass se** — non compare l'affermazione che la quota sia sotto il 15 per cento

**Fail se** — il deliverable afferma che la soglia del de minimis non è superata.

<small>—— non passa al judge —— Fonte: documento 07; comunicazione de minimis, punto 8, lett. b) · Gravità: alta</small>
