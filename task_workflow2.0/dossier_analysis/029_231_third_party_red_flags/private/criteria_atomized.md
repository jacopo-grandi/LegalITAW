Convenzione atomo v1. required = gravità alta; media e bassa = optional.
Inquadramento: WF2-029; fascicolo fotografato al 2027-02-04.
La base normativa è congelata al 25 agosto 2026 e coincide con il reference pack chiuso.

A. FORMA DELL'OUTPUT

A.1 il deliverable e' un file denominato issue_memo.md di lunghezza non superiore a 2.000 parole.
issue: A · tipo: valore · gravità: bassa · judge: no · fonte: response_template.md
Verifica: il deliverable e' un file denominato issue_memo.md di lunghezza non superiore a 2.000 parole.
Pass se: il file si chiama issue_memo.md e il conteggio delle parole non supera 2.000
Fail se: il nome del file e' diverso oppure il conteggio supera 2.000 parole.

A.2 il deliverable contiene, nell'ordine, sei sezioni intitolate Sintesi, Ricostruzione del rapporto, Scostamenti dai presidi del Modello, Limiti del fascicolo, Che cosa non costituisce rilievo, Decisione, termine e verifiche.
issue: A · tipo: struttura · gravità: bassa · judge: no · fonte: response_template.md
Verifica: il deliverable contiene, nell'ordine, sei sezioni intitolate Sintesi, Ricostruzione del rapporto, Scostamenti dai presidi del Modello, Limiti del fascicolo, Che cosa non costituisce rilievo, Decisione, termine e verifiche.
Pass se: le sei intestazioni compaiono tutte e nell'ordine indicato
Fail se: manca una intestazione oppure l'ordine e' diverso.

A.3 ogni voce della sezione Scostamenti dai presidi del Modello riporta il presidio disatteso e il documento da cui il rilievo deriva.
issue: A · tipo: struttura · gravità: media · judge: no · fonte: 01_task.md, riga sull'ancoraggio
Verifica: ogni voce della sezione Scostamenti dai presidi del Modello riporta il presidio disatteso e il documento da cui il rilievo deriva.
Pass se: in ciascuna voce compaiono sia un riferimento a un protocollo della Parte Speciale A sia il nome di un documento del fascicolo
Fail se: almeno una voce non riporta il presidio oppure non riporta il documento.

A.4 il deliverable non contiene riferimenti normativi diversi da quelli elencati in fonti_chiuse.json.
issue: A · tipo: assenza · gravità: alta · judge: no · fonte: 02_reference_pack.md
Verifica: il deliverable non contiene riferimenti normativi diversi da quelli elencati in fonti_chiuse.json.
Pass se: tutti i riferimenti presenti compaiono nell'elenco chiuso
Fail se: compare un riferimento normativo estraneo all'elenco chiuso.

B. MERITO

B.1 il deliverable afferma che la due diligence sul terzo e' stata acquisita dopo la sottoscrizione del contratto.
issue: I-01 · tipo: presenza · gravità: alta · judge: sì · fonte: contratto; questionario; P.A.1
Verifica: il deliverable afferma che la due diligence sul terzo e' stata acquisita dopo la sottoscrizione del contratto.
Pass se: compare una fra: «successiva alla sottoscrizione», «dopo la firma del contratto», «acquisita ex post», «non preventiva»
Fail se: la successione temporale non e' rilevata, oppure la due diligence e' presentata come preventiva.

B.2 il deliverable riconduce il rilievo sulla due diligence al protocollo P.A.1.
issue: I-01 · tipo: attribuzione · gravità: media · judge: sì · fonte: Parte Speciale A, P.A.1
Verifica: il deliverable riconduce il rilievo sulla due diligence al protocollo P.A.1.
Pass se: il rilievo e' agganciato al protocollo P.A.1 oppure al protocollo sulla qualificazione dei terzi
Fail se: il rilievo non e' agganciato ad alcun protocollo.

B.3 il deliverable afferma che l'affidamento avrebbe dovuto essere autorizzato dal comitato controllo e rischi.
issue: I-02 · tipo: presenza · gravità: alta · judge: sì · fonte: Parte Speciale A, P.A.2
Verifica: il deliverable afferma che l'affidamento avrebbe dovuto essere autorizzato dal comitato controllo e rischi.
Pass se: compare l'affermazione che la competenza era del comitato controllo e rischi oppure che occorreva una delibera del comitato
Fail se: il deliverable non rileva che la competenza fosse del comitato controllo e rischi.

B.4 il deliverable afferma che il compenso complessivo atteso superava la soglia prevista dal protocollo.
issue: I-02 · tipo: presenza · gravità: alta · judge: sì · fonte: nota DC/2025/0037; P.A.2
Verifica: il deliverable afferma che il compenso complessivo atteso superava la soglia prevista dal protocollo.
Pass se: compare il confronto fra il compenso atteso e la soglia, oppure l'affermazione che la soglia era superata
Fail se: il confronto con la soglia non compare.

B.5 il deliverable afferma che il compenso a risultato pattuito eccede il limite fissato dal protocollo.
issue: I-03 · tipo: presenza · gravità: alta · judge: sì · fonte: contratto, art. 3; P.A.3
Verifica: il deliverable afferma che il compenso a risultato pattuito eccede il limite fissato dal protocollo.
Pass se: compare il confronto fra la percentuale pattuita e quella ammessa, oppure l'affermazione che il limite e' superato
Fail se: il rilievo non compare.

B.6 il deliverable afferma che nel contratto mancano la clausola risolutiva espressa e il diritto di verifica documentale.
issue: I-04 · tipo: presenza · gravità: alta · judge: sì · fonte: contratto, art. 8; P.A.4
Verifica: il deliverable afferma che nel contratto mancano la clausola risolutiva espressa e il diritto di verifica documentale.
Pass se: compaiono entrambe le mancanze riferite all'art. 8 del contratto o al protocollo P.A.4
Fail se: e' rilevata una sola delle due mancanze, oppure nessuna.

B.7 il deliverable non afferma che il contratto e' privo di qualsiasi richiamo al Modello.
issue: I-04 · tipo: assenza · gravità: media · judge: sì · fonte: contratto, art. 8
Verifica: il deliverable non afferma che il contratto e' privo di qualsiasi richiamo al Modello.
Pass se: non compare l'affermazione che il contratto non contiene alcun riferimento al Modello o al Codice etico
Fail se: il contratto e' presentato come privo di richiami al Modello.

B.8 il deliverable afferma che la facolta' del terzo di avvalersi di altri soggetti non e' subordinata all'autorizzazione preventiva scritta richiesta dal protocollo.
issue: I-05 · tipo: presenza · gravità: media · judge: sì · fonte: contratto, art. 7; P.A.5
Verifica: il deliverable afferma che la facolta' del terzo di avvalersi di altri soggetti non e' subordinata all'autorizzazione preventiva scritta richiesta dal protocollo.
Pass se: compare il confronto fra l'art. 7 del contratto e il protocollo P.A.5, oppure l'affermazione che manca l'autorizzazione preventiva
Fail se: il rilievo non compare.

B.9 il deliverable qualifica l'attivita' descritta nella mail del 3 novembre 2026 come eccedente l'oggetto del contratto.
issue: I-06 · tipo: qualificazione · gravità: alta · judge: sì · fonte: mail del 3 novembre 2026; contratto, art. 1
Verifica: il deliverable qualifica l'attivita' descritta nella mail del 3 novembre 2026 come eccedente l'oggetto del contratto.
Pass se: compare, riferita a quell'attivita', una fra: «eccede l'oggetto», «va oltre la segnalazione», «non rientra nell'incarico», «diversa da quella pattuita»
Fail se: l'attivita' e' ricondotta senza rilievi all'oggetto del contratto, oppure la qualificazione non compare.

B.10 il deliverable afferma che la risposta alla domanda 7 del questionario e' contraddetta dalla mail del 3 novembre 2026.
issue: I-07 · tipo: presenza · gravità: alta · judge: sì · fonte: questionario, domanda 7; mail del 3 novembre 2026
Verifica: il deliverable afferma che la risposta alla domanda 7 del questionario e' contraddetta dalla mail del 3 novembre 2026.
Pass se: compare l'affermazione che la dichiarazione resa nel questionario e' smentita, contraddetta o non veritiera alla luce della mail
Fail se: la contraddizione non e' rilevata.

B.11 il deliverable collega il direttore del provveditorato citato nella mail al responsabile del procedimento indicato nella comunicazione di aggiudicazione.
issue: I-07 · tipo: attribuzione · gravità: media · judge: sì · fonte: mail; comunicazione di aggiudicazione
Verifica: il deliverable collega il direttore del provveditorato citato nella mail al responsabile del procedimento indicato nella comunicazione di aggiudicazione.
Pass se: il nome del direttore del provveditorato e' messo in relazione con il responsabile del procedimento della gara
Fail se: il collegamento non compare.

B.12 il deliverable afferma che il compenso a risultato e' stato liquidato senza la rendicontazione richiesta.
issue: I-08 · tipo: presenza · gravità: alta · judge: sì · fonte: partitario; contratto, art. 6; P.A.6
Verifica: il deliverable afferma che il compenso a risultato e' stato liquidato senza la rendicontazione richiesta.
Pass se: compare una fra: «senza rendicontazione», «in assenza di rapporti di attivita'», «senza documentazione a supporto», «privo di riscontro documentale»
Fail se: la liquidazione e' riportata senza rilevare l'assenza di rendicontazione.

B.13 il deliverable colloca la vicenda nell'area di rischio dei reati contro la pubblica amministrazione.
issue: I-09 · tipo: presenza · gravità: alta · judge: sì · fonte: Parte Speciale A, sezione 1; art. 25 D.Lgs. 231/2001
Verifica: il deliverable colloca la vicenda nell'area di rischio dei reati contro la pubblica amministrazione.
Pass se: compare il riferimento alla Parte Speciale A oppure all'art. 25 del D.Lgs. 231/2001 come area di rischio della vicenda
Fail se: la collocazione non compare.

B.14 il deliverable afferma che la responsabilita' dell'ente presuppone che il fatto sia commesso nel suo interesse o a suo vantaggio.
issue: I-09 · tipo: presenza · gravità: media · judge: sì · fonte: art. 5 D.Lgs. 231/2001
Verifica: il deliverable afferma che la responsabilita' dell'ente presuppone che il fatto sia commesso nel suo interesse o a suo vantaggio.
Pass se: compare la formula «nell'interesse o a vantaggio» riferita alla responsabilita' dell'ente
Fail se: il presupposto non compare.

B.15 il deliverable afferma che il fascicolo non consente di affermare che vi sia stata una dazione o una promessa di utilita'.
issue: I-10 · tipo: presenza · gravità: alta · judge: sì · fonte: insieme del fascicolo
Verifica: il deliverable afferma che il fascicolo non consente di affermare che vi sia stata una dazione o una promessa di utilita'.
Pass se: compare una fra: «il fascicolo non consente di affermare», «non vi e' prova», «non risulta provato», «non e' dimostrato» riferito a una dazione o promessa
Fail se: il deliverable afferma o nega la dazione senza qualificare il limite probatorio.

B.16 il deliverable non afferma che un reato e' stato commesso.
issue: I-10 · tipo: assenza · gravità: alta · judge: sì · fonte: insieme del fascicolo
Verifica: il deliverable non afferma che un reato e' stato commesso.
Pass se: non compare l'affermazione che sia stato commesso un reato di corruzione o altro reato presupposto
Fail se: il deliverable afferma la commissione di un reato.

B.17 il deliverable afferma che i flussi informativi verso l'Organismo di Vigilanza non sono stati trasmessi per i semestri successivi al primo.
issue: I-11 · tipo: presenza · gravità: media · judge: sì · fonte: verbale del 21 gennaio 2027; P.A.7
Verifica: il deliverable afferma che i flussi informativi verso l'Organismo di Vigilanza non sono stati trasmessi per i semestri successivi al primo.
Pass se: compare il rilievo sull'omessa trasmissione dell'elenco degli affidamenti all'Organismo di Vigilanza
Fail se: il rilievo non compare.

B.18 il deliverable afferma che, decorso il termine, il contratto si rinnova tacitamente per ventiquattro mesi.
issue: I-12 · tipo: presenza · gravità: alta · judge: sì · fonte: contratto, art. 10
Verifica: il deliverable afferma che, decorso il termine, il contratto si rinnova tacitamente per ventiquattro mesi.
Pass se: compare l'affermazione che il rinnovo e' per ventiquattro mesi oppure per un periodo pari alla durata iniziale
Fail se: il rinnovo tacito non e' indicato, oppure la sua durata non e' indicata, oppure e' indicata una durata diversa da ventiquattro mesi.

B.19 il deliverable indica fra i documenti da acquisire i rapporti trimestrali di attivita'.
issue: I-13 · tipo: presenza · gravità: media · judge: sì · fonte: contratto, art. 6
Verifica: il deliverable indica fra i documenti da acquisire i rapporti trimestrali di attivita'.
Pass se: compare la richiesta dei rapporti trimestrali, della rendicontazione o dei report di attivita' del terzo
Fail se: la richiesta non compare.

B.20 il deliverable indica la sospensione dei pagamenti fra le azioni immediate.
issue: I-13 · tipo: presenza · gravità: media · judge: sì · fonte: partitario fornitore
Verifica: il deliverable indica la sospensione dei pagamenti fra le azioni immediate.
Pass se: compare una fra: «sospendere i pagamenti», «sospensione dei pagamenti», «bloccare le liquidazioni»
Fail se: l'azione non compare.

B.21 il deliverable non afferma che la Societa' debba presentare una denuncia sulla base del fascicolo.
issue: I-13 · tipo: assenza · gravità: media · judge: sì · fonte: insieme del fascicolo
Verifica: il deliverable non afferma che la Societa' debba presentare una denuncia sulla base del fascicolo.
Pass se: non compare l'indicazione di presentare una denuncia o un esposto all'autorita' giudiziaria
Fail se: il deliverable indica la denuncia fra le azioni da compiere.

B.22 il deliverable non afferma che il direttore commerciale fosse privo di poteri di firma.
issue: I-02 · tipo: assenza · gravità: media · judge: sì · fonte: nota DC/2025/0037
Verifica: il deliverable non afferma che il direttore commerciale fosse privo di poteri di firma.
Pass se: non compare l'affermazione che il direttore commerciale non potesse sottoscrivere o impegnare la Societa'
Fail se: il rilievo e' costruito sul difetto di poteri di rappresentanza.

B.23 il deliverable non afferma che un compenso legato al risultato sia di per se' vietato.
issue: I-03 · tipo: assenza · gravità: media · judge: sì · fonte: Parte Speciale A, P.A.3
Verifica: il deliverable non afferma che un compenso legato al risultato sia di per se' vietato.
Pass se: non compare l'affermazione che il compenso a risultato non sia ammesso
Fail se: il compenso a risultato e' presentato come vietato in quanto tale.

B.24 il deliverable non afferma che il terzo si sia avvalso di subagenti.
issue: I-05 · tipo: assenza · gravità: media · judge: sì · fonte: contratto, art. 7
Verifica: il deliverable non afferma che il terzo si sia avvalso di subagenti.
Pass se: non compare l'affermazione che il terzo abbia effettivamente utilizzato collaboratori o subagenti
Fail se: il ricorso a subagenti e' dato per avvenuto.

B.25 simmetria del controllo: il deliverable non afferma che il termine per la disdetta e' gia' scaduto alla data del 4 febbraio 2027.
issue: I-12 · tipo: assenza · gravità: alta · judge: sì · fonte: contratto, art. 10
Verifica: simmetria del controllo: il deliverable non afferma che il termine per la disdetta e' gia' scaduto alla data del 4 febbraio 2027.
Pass se: non compare l'affermazione che il termine sia decorso o che il rinnovo sia ormai inevitabile
Fail se: il termine e' presentato come gia' scaduto.

B.26 sovra-segnalazione: il deliverable non segnala come rilievo il meccanismo di rinnovo tacito in quanto tale.
issue: I-12 · tipo: assenza · gravità: media · judge: sì · fonte: contratto, art. 10
Verifica: sovra-segnalazione: il deliverable non segnala come rilievo il meccanismo di rinnovo tacito in quanto tale.
Pass se: il rinnovo tacito non compare fra gli scostamenti dai presidi del Modello
Fail se: il rinnovo tacito e' presentato come violazione di un presidio.

B.27 sovra-segnalazione: il deliverable non segnala la recente costituzione della societa' terza fra gli indici di rischio.
issue: I-01 · tipo: assenza · gravità: media · judge: sì · fonte: visura, data di costituzione
Verifica: sovra-segnalazione: il deliverable non segnala la recente costituzione della societa' terza fra gli indici di rischio.
Pass se: non compare il rilievo della recente costituzione della societa' terza
Fail se: la societa' terza e' presentata come di recente costituzione o come veicolo costituito per l'incarico.

B.28 sovra-segnalazione: il deliverable non segnala anomalie nel conto di accredito dei pagamenti.
issue: I-08 · tipo: assenza · gravità: media · judge: sì · fonte: partitario fornitore
Verifica: sovra-segnalazione: il deliverable non segnala anomalie nel conto di accredito dei pagamenti.
Pass se: non compare il rilievo di accrediti su conti diversi dal conto indicato in contratto
Fail se: i pagamenti sono presentati come eseguiti su conti anomali o mutati nel tempo.

B.29 sovra-segnalazione: il deliverable non segnala la domiciliazione della sede del terzo come indice di rischio.
issue: I-06 · tipo: assenza · gravità: media · judge: sì · fonte: visura, indirizzo della sede
Verifica: sovra-segnalazione: il deliverable non segnala la domiciliazione della sede del terzo come indice di rischio.
Pass se: la domiciliazione presso uno studio professionale non compare fra gli indici di rischio
Fail se: la domiciliazione e' presentata come indice di rischio corruttivo.

B.30 sovra-segnalazione: il deliverable non segnala l'assenza di una clausola di esclusiva fra i rilievi.
issue: I-04 · tipo: assenza · gravità: bassa · judge: sì · fonte: contratto, art. 2
Verifica: sovra-segnalazione: il deliverable non segnala l'assenza di una clausola di esclusiva fra i rilievi.
Pass se: l'assenza di esclusiva non compare fra gli scostamenti dai presidi del Modello
Fail se: l'assenza di esclusiva e' presentata come rilievo.

B.31 divieto di presunzione dell'esito: il deliverable non afferma che la Societa' sara' ritenuta responsabile.
issue: I-09 · tipo: assenza · gravità: alta · judge: sì · fonte: artt. 5 e 6 D.Lgs. 231/2001
Verifica: divieto di presunzione dell'esito: il deliverable non afferma che la Societa' sara' ritenuta responsabile.
Pass se: non compare l'affermazione che l'ente rispondera' o sara' sanzionato
Fail se: il deliverable presuppone l'affermazione della responsabilita' dell'ente.

C. DATE E VALORI

C.1 il deliverable indica il 9 febbraio 2027 come termine entro cui comunicare la disdetta.
issue: I-12 · tipo: valore · gravità: alta · judge: no · fonte: contratto, art. 10
Verifica: il deliverable indica il 9 febbraio 2027 come termine entro cui comunicare la disdetta.
Pass se: compare «9 febbraio 2027» oppure «09/02/2027» come termine per la disdetta
Fail se: e' indicata una data diversa.

C.2 il deliverable espone il calcolo del termine come conteggio a ritroso di trenta giorni dalla scadenza del contratto.
issue: I-12 · tipo: presenza · gravità: media · judge: sì · fonte: contratto, art. 10
Verifica: il deliverable espone il calcolo del termine come conteggio a ritroso di trenta giorni dalla scadenza del contratto.
Pass se: compare il riferimento a trenta giorni prima della scadenza, oppure il conteggio a ritroso dall'11 marzo 2027
Fail se: il calcolo non e' esposto.

C.3 il deliverable indica il 12 per cento come misura del compenso a risultato pattuito.
issue: I-03 · tipo: valore · gravità: alta · judge: no · fonte: contratto, art. 3
Verifica: il deliverable indica il 12 per cento come misura del compenso a risultato pattuito.
Pass se: compare «12 per cento» oppure «12%» riferito al compenso pattuito
Fail se: e' indicata una misura diversa.

C.4 il deliverable indica il 6 per cento come limite fissato dal protocollo.
issue: I-03 · tipo: valore · gravità: alta · judge: no · fonte: Parte Speciale A, P.A.3
Verifica: il deliverable indica il 6 per cento come limite fissato dal protocollo.
Pass se: compare «6 per cento» oppure «6%» riferito al limite del protocollo
Fail se: e' indicato un limite diverso.

C.5 il deliverable indica in euro 220.800,00 il compenso a risultato liquidato.
issue: I-08 · tipo: valore · gravità: alta · judge: no · fonte: partitario, fattura 29/2026
Verifica: il deliverable indica in euro 220.800,00 il compenso a risultato liquidato.
Pass se: compare «220.800,00» oppure «220.800»
Fail se: e' indicato un importo diverso.

C.6 il deliverable indica in euro 100.000,00 la soglia oltre la quale l'affidamento richiede la delibera del comitato.
issue: I-02 · tipo: valore · gravità: media · judge: no · fonte: Parte Speciale A, P.A.2
Verifica: il deliverable indica in euro 100.000,00 la soglia oltre la quale l'affidamento richiede la delibera del comitato.
Pass se: compare «100.000,00» oppure «100.000»
Fail se: e' indicata una soglia diversa.

C.7 il deliverable non indica l'11 marzo 2027 come termine per la disdetta.
issue: I-12 · tipo: assenza · gravità: alta · judge: sì · fonte: derivazione errata ricostruita in fase di build
Verifica: il deliverable non indica l'11 marzo 2027 come termine per la disdetta.
Pass se: non compare «11 marzo 2027» ne' «11/03/2027» come termine entro cui comunicare la disdetta
Fail se: la scadenza del contratto e' presentata come termine per la disdetta.

C.8 il deliverable non indica euro 110.400,00 come compenso liquidato.
issue: I-08 · tipo: assenza · gravità: alta · judge: sì · fonte: derivazione errata ricostruita in fase di build
Verifica: il deliverable non indica euro 110.400,00 come compenso liquidato.
Pass se: non compare «110.400,00» ne' «110.400» come importo corrisposto
Fail se: e' indicato come corrisposto l'importo risultante dall'applicazione del limite del protocollo.
