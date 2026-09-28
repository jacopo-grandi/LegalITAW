Convenzione atomo v1. required = gravità alta; media e bassa = optional.
Inquadramento: WF2-028; fascicolo fotografato al 2027-03-15.
La base normativa è congelata al 25 agosto 2026 e coincide con il reference pack chiuso.

A. FORMA DELL'OUTPUT

A.1 il deliverable e' un file denominato deadline_audit.md di lunghezza non superiore a 1.700 parole.
issue: A · tipo: valore · gravità: bassa · judge: no · fonte: response_template.md
Verifica: il deliverable e' un file denominato deadline_audit.md di lunghezza non superiore a 1.700 parole.
Pass se: il file si chiama deadline_audit.md e il conteggio delle parole non supera 1.700
Fail se: il nome del file e' diverso oppure il conteggio supera 1.700 parole.

A.2 il deliverable contiene, nell'ordine, sei sezioni intitolate Sintesi, Matrice degli adempimenti, Ancore e dipendenze, Che cosa non richiede rilievo, Che cosa manca dal fascicolo, Azioni residue.
issue: A · tipo: struttura · gravità: bassa · judge: no · fonte: response_template.md
Verifica: il deliverable contiene, nell'ordine, sei sezioni intitolate Sintesi, Matrice degli adempimenti, Ancore e dipendenze, Che cosa non richiede rilievo, Che cosa manca dal fascicolo, Azioni residue.
Pass se: le sei intestazioni compaiono tutte e nell'ordine indicato
Fail se: manca una intestazione oppure l'ordine e' diverso.

A.3 la matrice degli adempimenti riporta per ogni riga le colonne adempimento, fatto da cui decorre il termine, termine, compiuto il, qualificazione, documento di riferimento.
issue: A · tipo: struttura · gravità: media · judge: no · fonte: response_template.md
Verifica: la matrice degli adempimenti riporta per ogni riga le colonne adempimento, fatto da cui decorre il termine, termine, compiuto il, qualificazione, documento di riferimento.
Pass se: le sei colonne compaiono nell'intestazione della matrice
Fail se: manca una colonna.

A.4 il deliverable non contiene riferimenti normativi diversi da quelli elencati in fonti_chiuse.json.
issue: A · tipo: assenza · gravità: alta · judge: no · fonte: 02_reference_pack.md
Verifica: il deliverable non contiene riferimenti normativi diversi da quelli elencati in fonti_chiuse.json.
Pass se: tutti i riferimenti presenti compaiono nell'elenco chiuso
Fail se: compare un riferimento normativo estraneo all'elenco chiuso.

B. MERITO

B.1 designazione diretta della cliente
issue: I-01 · tipo: presenza · gravità: alta · judge: sì · fonte: report dei riscontri, alert AL-2027-0032
Verifica: il deliverable afferma che i fondi del rapporto n. 000000731204 sono soggetti a congelamento per la designazione diretta di Sernaglia Commodities S.r.l.
Pass se: compare la designazione diretta della societa' come presupposto del congelamento
Fail se: il congelamento e' escluso, non trattato o fondato soltanto sulle quote dei soci

B.2 designazione diretta della cliente
issue: I-01 · tipo: attribuzione · gravità: alta · judge: sì · fonte: report dei riscontri, alert AL-2027-0032
Verifica: il deliverable riconduce il congelamento alla designazione diretta della cliente efficace dal 13 gennaio 2027.
Pass se: la conclusione e' agganciata al report dei riscontri e alla data di efficacia
Fail se: la conclusione e' agganciata soltanto alla visura o all'assetto dei soci

B.3 designazione diretta della cliente
issue: I-02 · tipo: presenza · gravità: alta · judge: sì · fonte: report dei riscontri; visura, sezione 4
Verifica: il deliverable distingue la designazione diretta della societa' dal suo assetto proprietario.
Pass se: la visura e le quote sono trattate come informazioni di contesto e non come presupposto della misura
Fail se: il deliverable calcola una soglia di proprieta' per fondare il congelamento

B.4 designazione diretta della cliente
issue: I-03 · tipo: presenza · gravità: alta · judge: sì · fonte: report dei riscontri, alert AL-2027-0032
Verifica: il deliverable afferma che per il rapporto della societa' l'obbligo di comunicazione decorre dall'entrata in vigore della designazione diretta di Sernaglia Commodities S.r.l.
Pass se: la decorrenza e' agganciata all'entrata in vigore della designazione diretta della cliente, oppure alla data di efficacia del provvedimento che la include direttamente nell'elenco dei soggetti designati
Fail se: la decorrenza e' agganciata alla designazione di un socio, alla data del decreto oppure alla data della sua pubblicazione

B.5 il deliverable qualifica come tardiva la comunicazione trasmessa il 26 febbraio 2027.
issue: I-04 · tipo: qualificazione · gravità: alta · judge: sì · fonte: ricevuta di trasmissione del 26/02/2027
Verifica: il deliverable qualifica come tardiva la comunicazione trasmessa il 26 febbraio 2027.
Pass se: compare, riferita a quella comunicazione, una fra: «tardiva», «fuori termine», «oltre il termine», «in ritardo»
Fail se: la comunicazione e' qualificata come tempestiva, oppure la qualificazione non compare.

B.6 il deliverable afferma che per i fondi destinati a Vartex Metal Trading Ltd il termine decorre dalla data in cui i fondi sono stati detenuti.
issue: I-05 · tipo: presenza · gravità: alta · judge: sì · fonte: avviso di accredito
Verifica: il deliverable afferma che per i fondi destinati a Vartex Metal Trading Ltd il termine decorre dalla data in cui i fondi sono stati detenuti.
Pass se: la decorrenza e' agganciata all'accredito sul conto di transito, alla detenzione dei fondi oppure alla data di ricezione dei fondi
Fail se: la decorrenza e' agganciata alla data di entrata in vigore della designazione.

B.7 il deliverable qualifica come omessa la comunicazione relativa ai fondi destinati a Vartex Metal Trading Ltd.
issue: I-06 · tipo: qualificazione · gravità: alta · judge: sì · fonte: assenza di comunicazioni nel fascicolo
Verifica: il deliverable qualifica come omessa la comunicazione relativa ai fondi destinati a Vartex Metal Trading Ltd.
Pass se: compare, riferita a quella posizione, una fra: «omessa», «non effettuata», «non risulta trasmessa», «mancante»
Fail se: la comunicazione e' data per effettuata, oppure la posizione non e' trattata.

B.8 il deliverable afferma che il congelamento del rapporto della societa' e' stato disposto in ritardo rispetto al momento in cui l'obbligo e' sorto.
issue: I-07 · tipo: presenza · gravità: alta · judge: sì · fonte: nota interna AML/2027/0044
Verifica: il deliverable afferma che il congelamento del rapporto della societa' e' stato disposto in ritardo rispetto al momento in cui l'obbligo e' sorto.
Pass se: compare, riferita alla nota del 15 febbraio 2027, una fra: «in ritardo», «tardivo», «oltre un mese dopo», «con un mese di ritardo»
Fail se: la data della nota e' riportata senza alcuna qualificazione del ritardo.

B.9 il deliverable afferma che la misura di congelamento opera senza necessita' di un provvedimento dell'autorita'.
issue: I-07 · tipo: presenza · gravità: media · judge: sì · fonte: art. 5 D.Lgs. 109/2007
Verifica: il deliverable afferma che la misura di congelamento opera senza necessita' di un provvedimento dell'autorita'.
Pass se: compare una fra: «opera di diritto», «opera automaticamente», «non richiede un provvedimento dell'autorita'», «e' immediata»
Fail se: il deliverable subordina la misura a un provvedimento dell'autorita', oppure il passaggio non compare.

B.10 il deliverable afferma che fra la disposizione del congelamento e l'applicazione del blocco il rapporto e' rimasto operativo.
issue: I-08 · tipo: presenza · gravità: alta · judge: sì · fonte: log del sistema dispositivo
Verifica: il deliverable afferma che fra la disposizione del congelamento e l'applicazione del blocco il rapporto e' rimasto operativo.
Pass se: compare l'affermazione che il rapporto e' rimasto operativo, movimentabile o non bloccato in quel periodo
Fail se: il deliverable tratta il rapporto come bloccato dalla data della nota interna.

B.11 il deliverable riconduce al log del sistema dispositivo la data di applicazione del blocco.
issue: I-08 · tipo: attribuzione · gravità: media · judge: sì · fonte: log del sistema dispositivo
Verifica: il deliverable riconduce al log del sistema dispositivo la data di applicazione del blocco.
Pass se: la data e' agganciata al log, al sistema dispositivo oppure al registro degli stati di blocco
Fail se: la data non e' agganciata ad alcun documento.

B.12 il deliverable qualifica come nullo l'atto di trasferimento eseguito il 3 marzo 2027.
issue: I-09 · tipo: qualificazione · gravità: alta · judge: sì · fonte: art. 5, co. 1 e 3, D.Lgs. 109/2007
Verifica: il deliverable qualifica come nullo l'atto di trasferimento eseguito il 3 marzo 2027.
Pass se: compare, riferita a quell'operazione, una fra: «nullo», «nullita'», «privo di effetti in quanto nullo»
Fail se: l'operazione e' qualificata come annullabile, inefficace, irregolare, oppure la qualificazione non compare.

B.13 il deliverable afferma che l'operazione del 3 marzo 2027 e' stata eseguita in violazione del congelamento.
issue: I-09 · tipo: presenza · gravità: alta · judge: sì · fonte: estratto conto; disposizione DISP-2027-0009114
Verifica: il deliverable afferma che l'operazione del 3 marzo 2027 e' stata eseguita in violazione del congelamento.
Pass se: compare l'affermazione che l'operazione e' stata eseguita nonostante il congelamento, in violazione della misura oppure in contrasto con il divieto
Fail se: l'operazione e' riportata senza rilevare la violazione.

B.14 il deliverable afferma che la segnalazione di operazione sospetta non assolve l'obbligo di comunicazione delle misure di congelamento.
issue: I-10 · tipo: presenza · gravità: alta · judge: sì · fonte: comunicato UIF del 18 agosto 2022
Verifica: il deliverable afferma che la segnalazione di operazione sospetta non assolve l'obbligo di comunicazione delle misure di congelamento.
Pass se: compare una fra: «obblighi distinti e autonomi», «non sostituisce», «non assolve», «adempimenti autonomi», «obblighi separati»
Fail se: la segnalazione e' presentata come sostitutiva della comunicazione, oppure il rapporto fra i due adempimenti non e' trattato.

B.15 il deliverable afferma che la comunicazione dei dati su operazioni e rapporti riconducibili ai soggetti designati e' dovuta e non risulta effettuata.
issue: I-11 · tipo: presenza · gravità: media · judge: sì · fonte: art. 7, co. 2, D.Lgs. 109/2007
Verifica: il deliverable afferma che la comunicazione dei dati su operazioni e rapporti riconducibili ai soggetti designati e' dovuta e non risulta effettuata.
Pass se: compare l'affermazione che quella comunicazione e' dovuta e non e' stata effettuata
Fail se: l'adempimento non compare fra quelli dovuti.

B.16 il deliverable non attribuisce alla comunicazione dei dati su operazioni e rapporti un termine di trenta giorni.
issue: I-11 · tipo: assenza · gravità: media · judge: sì · fonte: art. 7, co. 2, D.Lgs. 109/2007
Verifica: il deliverable non attribuisce alla comunicazione dei dati su operazioni e rapporti un termine di trenta giorni.
Pass se: a quella comunicazione non e' associato un termine espresso in giorni
Fail se: a quella comunicazione e' associato il termine di trenta giorni o altro termine espresso in giorni.

B.17 il deliverable afferma che la richiesta della cliente di chiudere il rapporto e trasferire il saldo non puo' essere accolta.
issue: I-12 · tipo: presenza · gravità: alta · judge: sì · fonte: nota del gestore del 4 marzo 2027
Verifica: il deliverable afferma che la richiesta della cliente di chiudere il rapporto e trasferire il saldo non puo' essere accolta.
Pass se: compare una fra: «non puo' essere accolta», «non e' possibile dare seguito», «va rifiutata», «non e' eseguibile»
Fail se: la richiesta e' presentata come accoglibile, oppure non e' trattata.

B.18 il deliverable non afferma che il trasferimento del saldo sia possibile previa comunicazione all'autorita'.
issue: I-12 · tipo: assenza · gravità: media · judge: sì · fonte: art. 5, co. 1 e 4, D.Lgs. 109/2007
Verifica: il deliverable non afferma che il trasferimento del saldo sia possibile previa comunicazione all'autorita'.
Pass se: non compare l'affermazione che una comunicazione o un'informativa all'autorita' renda eseguibile il trasferimento
Fail se: il trasferimento e' presentato come eseguibile previa comunicazione.

B.19 il deliverable indica fra i documenti mancanti la nota interna AML/2027/0031.
issue: I-13 · tipo: presenza · gravità: media · judge: sì · fonte: log del sistema, riga dell'08/02/2027
Verifica: il deliverable indica fra i documenti mancanti la nota interna AML/2027/0031.
Pass se: compare la richiesta della nota AML/2027/0031 oppure della nota interna richiamata dal log per il conto di transito
Fail se: la lacuna non e' segnalata.

B.20 il deliverable indica fra i documenti mancanti la valutazione dell'alert AL-2027-0032.
issue: I-13 · tipo: presenza · gravità: media · judge: sì · fonte: report dei riscontri
Verifica: il deliverable indica fra i documenti mancanti la valutazione dell'alert AL-2027-0032.
Pass se: compare la richiesta della valutazione, dell'istruttoria o dell'esito dell'alert AL-2027-0032
Fail se: la lacuna non e' segnalata.

B.21 designazione diretta della cliente
issue: I-01 · tipo: presenza · gravità: alta · judge: sì · fonte: report dei riscontri
Verifica: il deliverable afferma che Sernaglia Commodities S.r.l. e' direttamente inclusa nell'elenco dei soggetti designati.
Pass se: la designazione diretta della societa' compare
Fail se: la societa' e' descritta soltanto come posseduta o controllata da soggetti designati

B.22 designazione diretta della cliente
issue: I-02 · tipo: assenza · gravità: alta · judge: sì · fonte: visura, sezione 4; report dei riscontri
Verifica: il deliverable non fonda il congelamento sulla quota singola del 30 per cento.
Pass se: la quota non e' usata come presupposto della misura
Fail se: la quota del 30 per cento e' indicata come ragione del congelamento

B.23 il deliverable non indica la data del decreto di designazione come decorrenza del termine per il rapporto della societa'.
issue: I-03 · tipo: assenza · gravità: alta · judge: sì · fonte: art. 7, co. 1, D.Lgs. 109/2007
Verifica: il deliverable non indica la data del decreto di designazione come decorrenza del termine per il rapporto della societa'.
Pass se: la decorrenza non e' fissata alla data del decreto ne' alla data della sua pubblicazione
Fail se: la decorrenza e' fissata all'11 gennaio 2027 o al 12 gennaio 2027.

B.24 il deliverable non indica la data di entrata in vigore della designazione di Vartex Metal Trading Ltd come decorrenza del termine per quella posizione.
issue: I-05 · tipo: assenza · gravità: alta · judge: sì · fonte: art. 7, co. 1, D.Lgs. 109/2007
Verifica: il deliverable non indica la data di entrata in vigore della designazione di Vartex Metal Trading Ltd come decorrenza del termine per quella posizione.
Pass se: la decorrenza della posizione sul conto di transito non e' fissata al 3 novembre 2026
Fail se: la decorrenza e' fissata al 3 novembre 2026.

B.25 il deliverable non afferma che il congelamento richiede un provvedimento dell'autorita' per operare.
issue: I-07 · tipo: assenza · gravità: media · judge: sì · fonte: art. 5 D.Lgs. 109/2007
Verifica: il deliverable non afferma che il congelamento richiede un provvedimento dell'autorita' per operare.
Pass se: non compare l'affermazione che occorra un provvedimento, un'autorizzazione o un'istruzione dell'autorita'
Fail se: il congelamento e' subordinato a un provvedimento dell'autorita'.

B.26 il deliverable non afferma che il rapporto era bloccato dal 15 febbraio 2027.
issue: I-08 · tipo: assenza · gravità: alta · judge: sì · fonte: log del sistema dispositivo
Verifica: il deliverable non afferma che il rapporto era bloccato dal 15 febbraio 2027.
Pass se: non compare l'affermazione che il blocco fosse operativo dalla data della nota interna
Fail se: il rapporto e' presentato come bloccato dal 15 febbraio 2027.

B.27 simmetria del controllo: il deliverable non presenta come ancora pendente il termine relativo ai fondi destinati a Vartex Metal Trading Ltd.
issue: I-06 · tipo: assenza · gravità: alta · judge: sì · fonte: art. 7, co. 1, D.Lgs. 109/2007
Verifica: simmetria del controllo: il deliverable non presenta come ancora pendente il termine relativo ai fondi destinati a Vartex Metal Trading Ltd.
Pass se: non compare l'affermazione che quel termine e' in corso o non ancora scaduto
Fail se: il termine e' presentato come pendente alla data di riferimento.

B.28 sovra-segnalazione: il deliverable non indica la posizione riferita a Rutka Silvano fra quelle che generano obblighi.
issue: I-09 · tipo: assenza · gravità: alta · judge: sì · fonte: report dei riscontri, alert AL-2027-0034
Verifica: sovra-segnalazione: il deliverable non indica la posizione riferita a Rutka Silvano fra quelle che generano obblighi.
Pass se: il riscontro su Rutka non e' presentato come posizione da congelare o da comunicare
Fail se: il riscontro su Rutka e' trattato come posizione attiva.

B.29 designazione diretta della cliente
issue: I-02 · tipo: assenza · gravità: alta · judge: sì · fonte: visura, sezione 4; report dei riscontri
Verifica: il deliverable non somma le quote dei soci per fondare il congelamento.
Pass se: non compare alcun calcolo aggregato delle quote come presupposto della misura
Fail se: il congelamento e' fondato sulla somma 30 + 22 o sull'inclusione della quota di Todeschin

B.30 sovra-segnalazione: il deliverable non segnala come irregolarita' la mancata comunicazione al Nucleo speciale di polizia valutaria.
issue: I-11 · tipo: assenza · gravità: media · judge: sì · fonte: art. 7, co. 3, D.Lgs. 109/2007
Verifica: sovra-segnalazione: il deliverable non segnala come irregolarita' la mancata comunicazione al Nucleo speciale di polizia valutaria.
Pass se: la mancata comunicazione al Nucleo speciale di polizia valutaria non compare fra le irregolarita'
Fail se: la mancata comunicazione al Nucleo speciale di polizia valutaria e' segnalata come irregolarita'.

B.31 sovra-segnalazione: il deliverable non segnala come irregolarita' la mancata chiusura del rapporto.
issue: I-12 · tipo: assenza · gravità: media · judge: sì · fonte: art. 5 D.Lgs. 109/2007
Verifica: sovra-segnalazione: il deliverable non segnala come irregolarita' la mancata chiusura del rapporto.
Pass se: la chiusura del rapporto non compare fra gli adempimenti dovuti o fra le irregolarita'
Fail se: la mancata chiusura del rapporto e' segnalata come irregolarita' o come adempimento dovuto.

B.32 sovra-segnalazione: il deliverable non presenta la segnalazione di operazione sospetta del 18 febbraio 2027 come duplicazione o come adempimento non dovuto.
issue: I-10 · tipo: assenza · gravità: media · judge: sì · fonte: art. 35 D.Lgs. 231/2007
Verifica: sovra-segnalazione: il deliverable non presenta la segnalazione di operazione sospetta del 18 febbraio 2027 come duplicazione o come adempimento non dovuto.
Pass se: la segnalazione non e' qualificata come duplicazione, come superflua o come non dovuta
Fail se: la segnalazione e' presentata come duplicazione o come adempimento non dovuto.

B.33 divieto di presunzione dell'esito: il deliverable non afferma che l'istituto sara' sanzionato.
issue: I-09 · tipo: assenza · gravità: media · judge: sì · fonte: -
Verifica: divieto di presunzione dell'esito: il deliverable non afferma che l'istituto sara' sanzionato.
Pass se: non compare l'affermazione che una sanzione sara' irrogata o che l'autorita' adottera' un provvedimento sanzionatorio
Fail se: il deliverable presuppone l'irrogazione di una sanzione.

C. DATE E VALORI

C.1 il deliverable indica il 13 gennaio 2027 come fatto da cui decorre il termine per il rapporto della societa'.
issue: I-03 · tipo: valore · gravità: alta · judge: no · fonte: report dei riscontri, alert AL-2027-0032
Verifica: il deliverable indica il 13 gennaio 2027 come fatto da cui decorre il termine per il rapporto della societa'.
Pass se: compare «13 gennaio 2027» oppure «13/01/2027» come decorrenza
Fail se: e' indicata una data diversa.

C.2 il deliverable indica il 12 febbraio 2027 come termine della comunicazione per il rapporto della societa'.
issue: I-04 · tipo: valore · gravità: alta · judge: no · fonte: art. 7, co. 1, D.Lgs. 109/2007
Verifica: il deliverable indica il 12 febbraio 2027 come termine della comunicazione per il rapporto della societa'.
Pass se: compare «12 febbraio 2027» oppure «12/02/2027» come termine
Fail se: e' indicata una data diversa.

C.3 il deliverable afferma che il giorno da cui il termine decorre non si computa.
issue: I-04 · tipo: presenza · gravità: media · judge: sì · fonte: computo dei termini a giorni
Verifica: il deliverable afferma che il giorno da cui il termine decorre non si computa.
Pass se: compare una fra: «il giorno iniziale non si computa», «a decorrere dal giorno successivo», «escluso il giorno di decorrenza», «dal 14 gennaio 2027»
Fail se: il passaggio non compare, oppure il termine e' contato includendo il giorno iniziale.

C.4 il deliverable indica l'8 febbraio 2027 come fatto da cui decorre il termine per i fondi destinati a Vartex Metal Trading Ltd.
issue: I-05 · tipo: valore · gravità: alta · judge: no · fonte: avviso di accredito su conto di transito
Verifica: il deliverable indica l'8 febbraio 2027 come fatto da cui decorre il termine per i fondi destinati a Vartex Metal Trading Ltd.
Pass se: compare «8 febbraio 2027» oppure «08/02/2027» come decorrenza
Fail se: e' indicata una data diversa.

C.5 il deliverable indica il 10 marzo 2027 come termine della comunicazione per i fondi destinati a Vartex Metal Trading Ltd.
issue: I-06 · tipo: valore · gravità: alta · judge: no · fonte: art. 7, co. 1, D.Lgs. 109/2007
Verifica: il deliverable indica il 10 marzo 2027 come termine della comunicazione per i fondi destinati a Vartex Metal Trading Ltd.
Pass se: compare «10 marzo 2027» oppure «10/03/2027» come termine
Fail se: e' indicata una data diversa.

C.6 il deliverable indica il 26 febbraio 2027 come data di trasmissione della comunicazione relativa al rapporto della societa'.
issue: I-04 · tipo: valore · gravità: media · judge: no · fonte: ricevuta di trasmissione
Verifica: il deliverable indica il 26 febbraio 2027 come data di trasmissione della comunicazione relativa al rapporto della societa'.
Pass se: compare «26 febbraio 2027» oppure «26/02/2027» come data di trasmissione
Fail se: e' indicata una data diversa.

C.7 il deliverable indica il 9 marzo 2027 come data di applicazione del blocco sul rapporto.
issue: I-08 · tipo: valore · gravità: alta · judge: no · fonte: log del sistema dispositivo
Verifica: il deliverable indica il 9 marzo 2027 come data di applicazione del blocco sul rapporto.
Pass se: compare «9 marzo 2027» oppure «09/03/2027» come data di applicazione del blocco
Fail se: e' indicata una data diversa.

C.8 il deliverable indica in euro 48.200,00 l'importo dell'operazione eseguita in violazione del congelamento.
issue: I-09 · tipo: valore · gravità: alta · judge: no · fonte: estratto conto, movimento del 03/03/2027
Verifica: il deliverable indica in euro 48.200,00 l'importo dell'operazione eseguita in violazione del congelamento.
Pass se: compare «48.200,00» oppure «48.200»
Fail se: e' indicato un importo diverso.

C.9 il deliverable non indica il 10 febbraio 2027 come termine della comunicazione per il rapporto della societa'.
issue: I-04 · tipo: assenza · gravità: alta · judge: sì · fonte: derivazione errata ricostruita in fase di build
Verifica: il deliverable non indica il 10 febbraio 2027 come termine della comunicazione per il rapporto della societa'.
Pass se: non compare «10 febbraio 2027» ne' «10/02/2027» come termine
Fail se: e' indicato come termine il risultato di trenta giorni dalla data del decreto.

C.10 il deliverable non indica l'11 febbraio 2027 come termine della comunicazione per il rapporto della societa'.
issue: I-04 · tipo: assenza · gravità: alta · judge: sì · fonte: derivazione errata ricostruita in fase di build
Verifica: il deliverable non indica l'11 febbraio 2027 come termine della comunicazione per il rapporto della societa'.
Pass se: non compare «11 febbraio 2027» ne' «11/02/2027» come termine
Fail se: e' indicato come termine il risultato di trenta giorni dalla data di pubblicazione del decreto.

C.11 il deliverable non indica il 3 dicembre 2026 come termine della comunicazione per i fondi destinati a Vartex Metal Trading Ltd.
issue: I-05 · tipo: assenza · gravità: alta · judge: sì · fonte: derivazione errata ricostruita in fase di build
Verifica: il deliverable non indica il 3 dicembre 2026 come termine della comunicazione per i fondi destinati a Vartex Metal Trading Ltd.
Pass se: non compare «3 dicembre 2026» ne' «03/12/2026» come termine
Fail se: e' indicato come termine il risultato di trenta giorni dalla data di entrata in vigore della designazione.
