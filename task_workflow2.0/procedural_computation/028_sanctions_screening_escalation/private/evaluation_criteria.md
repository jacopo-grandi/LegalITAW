# WF2-028 — Rubrica in prosa, a livello di issue

Fascicolo in corso alla data di riferimento del 15 marzo 2027. Due posizioni sono aperte: il rapporto
di pagamento della societa' cliente e i fondi accreditati su conto di transito a favore di una entita'
designata. La misura di congelamento e' stata disposta su entrambe, ma con tempi e con efficacia
operativa diversi. I criteri riguardano lo stato degli adempimenti quale risulta agli atti, non un
giudizio sull'esito di un eventuale procedimento sanzionatorio.

Il prompt chiede la ricostruzione degli adempimenti con termine, decorrenza, stato e qualificazione,
l'ancoraggio documentale di ogni data, il calcolo seguito, le azioni residue e la risposta ai due
quesiti del consiglio. La rubrica non verifica passaggi che il prompt non chiede di esplicitare.

## Issue di merito

**I-01. Designazione diretta della cliente** — il report documenta che Sernaglia Commodities S.r.l. è direttamente inclusa nell'elenco nazionale dei soggetti designati con efficacia dal 13 gennaio 2027; da quella data i fondi del rapporto sono soggetti a congelamento. (report dei riscontri)

**I-02. Assetto proprietario non determinante** — le quote dei soci risultanti dalla visura non fondano la misura e non devono essere aggregate. La visura serve a identificare titolare del rapporto e assetto societario. (visura; report dei riscontri)

**I-03. Decorrenza della posizione A** — l'obbligo sorge il 13 gennaio 2027, data di entrata in vigore della designazione diretta di Sernaglia Commodities S.r.l., perché a quella data i fondi erano già detenuti. La data del decreto (11 gennaio) e quella della pubblicazione (12 gennaio) non sono decorrenze. (report dei riscontri, alert AL-2027-0032; art. 7, co. 1, D.Lgs. 109/2007)

**I-04. Termine e ritardo della comunicazione per la posizione A** — il termine di trenta giorni
scadeva il 12 febbraio 2027; la comunicazione risulta trasmessa il 26 febbraio 2027 e va qualificata
come tardiva. (comunicazione di congelamento, ricevuta di trasmissione)

**I-05. Decorrenza della posizione B** — per i fondi destinati all'entita' designata il termine
decorre dall'8 febbraio 2027, data in cui i fondi sono stati detenuti, successiva alla data di entrata
in vigore della designazione. (avviso di accredito; art. 7, co. 1, D.Lgs. 109/2007)

**I-06. Omissione della comunicazione per la posizione B** — il termine scadeva il 10 marzo 2027 e
alla data di riferimento non risulta trasmessa alcuna comunicazione riferita a quella posizione:
l'adempimento e' omesso e il termine e' gia' scaduto. (assenza di comunicazioni nel fascicolo)

**I-07. Ritardo del congelamento della posizione A** — la misura opera dal momento in cui il
presupposto e' conosciuto; l'alert e' del 14 gennaio 2027 e la nota che dispone il congelamento e' del
15 febbraio 2027. (nota interna AML/2027/0044; report dei riscontri)

**I-08. Misura disposta e non resa operativa** — il blocco tecnico sul rapporto risulta applicato
soltanto il 9 marzo 2027: fra il 15 febbraio e il 9 marzo la richiesta e' rimasta in lavorazione e il
rapporto e' rimasto operativo. (log del sistema dispositivo)

**I-09. Operazione eseguita in violazione del congelamento** — il bonifico di euro 48.200,00 eseguito
il 3 marzo 2027 costituisce trasferimento di fondi sottoposti a congelamento e l'atto e' nullo.
(disposizione DISP-2027-0009114; estratto conto; art. 5, co. 1 e 3, D.Lgs. 109/2007)

**I-10. Autonomia della segnalazione di operazione sospetta** — la segnalazione trasmessa il 18
febbraio 2027 non assolve l'obbligo di comunicazione delle misure di congelamento: i due obblighi sono
distinti e autonomi. (ricevuta SOS; comunicato UIF del 18 agosto 2022)

**I-11. Comunicazione dei dati su operazioni e rapporti** — la comunicazione tempestiva dei dati su
operazioni, rapporti e altre informazioni riconducibili ai soggetti designati e' dovuta, non risulta
effettuata e non ha un termine espresso in giorni. (art. 7, co. 2, D.Lgs. 109/2007)

**I-12. Richiesta di chiusura e trasferimento del saldo** — la richiesta della cliente non puo' essere
accolta: il trasferimento del saldo presso altro intermediario e' un atto di disposizione di fondi
congelati e ne comporta la messa a disposizione. (nota del gestore del 4 marzo 2027; art. 5, co. 1 e
4, D.Lgs. 109/2007)

**I-13. Lacune del fascicolo** — mancano la nota interna AML/2027/0031, richiamata dal log per la
posizione sul conto di transito, e la valutazione documentata dell'alert AL-2027-0032 sulla designazione diretta della cliente, rimasto in
stato aperto. (log del sistema; report dei riscontri)

## Controlled non-issue (da non segnalare come irregolarita')

**N-01. Riscontro su soggetto cancellato** — la cancellazione di Rutka dall'elenco e' efficace dal 21
gennaio 2027, anteriore alla disposizione del 2 marzo 2027: il riscontro non genera obblighi e la
posizione del beneficiario non va congelata per quella ragione.

**N-02. Quota del socio non designato** — Todeschin non e' un soggetto designato: la sua quota non si
somma e la sua posizione personale non e' interessata dalle misure.

**N-03. Comunicazione al Nucleo speciale di polizia valutaria** — e' prevista per le risorse
economiche; nel caso si tratta di soli fondi, quindi la sua assenza non e' un'irregolarita'.

**N-04. Rapporto rimasto aperto** — il congelamento non impone la chiusura del rapporto: mantenerlo
aperto con i fondi congelati e' la condotta dovuta.

**N-05. Segnalazione di operazione sospetta trasmessa** — l'invio e' un adempimento autonomo e dovuto:
presentarlo come duplicazione o come adempimento non dovuto e' sovra-segnalazione.

## Punti neutri, non valutati

Le commissioni di gestione addebitate il 23 febbraio e l'11 marzo 2027; l'intervallo di un giorno fra
l'efficacia della designazione e la generazione dell'alert. Nessun criterio li premia e nessuno
penalizza chi li segnala.

## Decisioni di build

1. La posizione A è fondata sulla designazione diretta della cliente; il criterio di ownership non è applicato.

2. **I-09.** Va confermato che la conseguenza da affermare sia la nullita' dell'atto e non altro, e
   fino a che punto il memo possa spingersi sulle conseguenze per l'istituto.
3. **I-11.** Va confermato che la comunicazione dell'art. 7, comma 2, sia dovuta anche quando e' gia'
   stata trasmessa quella del comma 1.
