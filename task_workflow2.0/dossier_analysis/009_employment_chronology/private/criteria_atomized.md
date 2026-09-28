A. Forma dell'output (interamente verifica meccanica)

A.1 file e formato [tipo: valore]
Verifica: la risposta consegna un file documento scaricabile che contiene la cronologia in forma di tabella.
Pass se: è presente un file con estensione .docx, .pdf, .xlsx o .md e il file contiene almeno una tabella.
Fail se: la cronologia compare solo nel corpo della risposta, oppure il file non contiene alcuna tabella.

A.2 colonne obbligatorie [tipo: valore]
Verifica: la tabella ha sei colonne: formazione; invio/spedizione; ricezione/consegna; efficacia; fonte; conflitti.
Pass se: compaiono tutte e sei le intestazioni, nelle forme ammesse: «formazione», «data di formazione», «redazione»; «invio», «spedizione»; «ricezione», «consegna»; «efficacia», «decorrenza degli effetti»; «fonte», «documento»; «conflitti», «anomalie», «contraddizioni».
Fail se: manca almeno una delle sei colonne.

A.3 ordinamento [tipo: struttura]
Verifica: le righe della tabella sono ordinate per data di efficacia crescente.
Fail se: l'ordine delle righe non segue la colonna efficacia.
Indifferente: la posizione delle righe la cui efficacia è indicata come non determinabile.

A.4 ancoraggio al documento [tipo: struttura]
Verifica: ogni riga della tabella ha la cella «fonte» compilata con il nome o il numero di un documento del fascicolo.
Fail se: almeno una riga ha la cella fonte vuota.

B. Merito
Inquadramento: il fascicolo si chiude con la lettera di licenziamento; il deliverable ricostruisce le date che risultano dagli atti e non valuta la legittimità del licenziamento. Le date sono indicate giorno/mese come nel fascicolo.

B.1 contestazione, formazione [issue: I-01] [tipo: valore]
Verifica: il deliverable indica come data di formazione della contestazione disciplinare il 6 maggio.
Pass se: nella riga della contestazione la colonna formazione riporta il 6 maggio.
Fail se: riporta una data diversa, oppure la cella è vuota.
— Fonte: 02_contestazione_disciplinare.pdf. Gravità: alta.

B.2 contestazione, spedizione [issue: I-01] [tipo: valore]
Verifica: il deliverable indica come data di spedizione della contestazione disciplinare il 7 maggio.
Pass se: nella riga della contestazione la colonna invio/spedizione riporta il 7 maggio.
Fail se: riporta una data diversa, oppure la cella è vuota.
— Fonte: 03_avviso_ricevimento_raccomandata.pdf. Gravità: alta.

B.3 contestazione, consegna [issue: I-01] [tipo: valore]
Verifica: il deliverable indica come data di consegna della contestazione disciplinare l'11 maggio.
Pass se: nella riga della contestazione la colonna ricezione/consegna riporta l'11 maggio.
Fail se: riporta una data diversa, oppure la cella è vuota.
— Fonte: 03_avviso_ricevimento_raccomandata.pdf. Gravità: alta.

B.4 contestazione, date non collassate [issue: I-01] [tipo: assenza]
Verifica: il deliverable non indica la stessa data come data di formazione e come data di consegna della contestazione disciplinare.
Pass se: le celle formazione e ricezione/consegna della riga della contestazione portano date diverse.
Fail se: le due celle portano la stessa data, oppure per la contestazione è indicata una sola data complessiva.
— Fonte: 02 + 03. Gravità: alta.

B.5 contestazione, efficacia [issue: I-02] [tipo: valore]
Verifica: il deliverable indica come data di efficacia della contestazione disciplinare l'11 maggio.
Pass se: nella riga della contestazione la colonna efficacia riporta l'11 maggio.
Fail se: riporta una data diversa, oppure la cella è vuota.
— Fonte: 03_avviso_ricevimento_raccomandata.pdf. Gravità: alta.

B.6 contestazione, efficacia non dalla redazione [issue: I-02] [tipo: assenza]
Verifica: il deliverable non indica il 6 maggio come data di efficacia della contestazione disciplinare.
Pass se: il 6 maggio non compare nella colonna efficacia della riga della contestazione.
Fail se: la colonna efficacia della contestazione riporta il 6 maggio.
— Fonte: 02_contestazione_disciplinare.pdf, data in calce. Gravità: alta.

B.7 licenziamento, efficacia [issue: I-02] [tipo: valore]
Verifica: il deliverable indica come data di efficacia della lettera di licenziamento il 16 maggio.
Pass se: nella riga del licenziamento la colonna efficacia riporta il 16 maggio.
Fail se: riporta una data diversa, oppure la cella è vuota.
— Fonte: 09_ricevuta_PEC_licenziamento.pdf. Gravità: alta.

B.8 licenziamento, efficacia non dalla data in calce [issue: I-02] [tipo: assenza]
Verifica: il deliverable non indica il 15 maggio come data di efficacia della lettera di licenziamento.
Pass se: il 15 maggio non compare nella colonna efficacia della riga del licenziamento.
Fail se: la colonna efficacia del licenziamento riporta il 15 maggio.
— Fonte: 08_lettera_licenziamento.pdf, data in calce. Gravità: alta.

B.9 colloquio, discordanza segnalata [issue: I-03] [tipo: presenza]
Verifica: il deliverable riporta come discordante la data del colloquio indicata nell'email di convocazione, il 12 maggio, rispetto alla data del verbale del colloquio, il 13 maggio.
Pass se: compaiono entrambe le date riferite al colloquio e, riferita ad esse, una fra: «discordanza», «discrepanza», «contraddizione», «conflitto», «le due date non coincidono».
Fail se: compare una sola delle due date, oppure compaiono entrambe senza alcuna delle formulazioni elencate.
— Fonte: 04_email_convocazione_colloquio.pdf + 05_verbale_colloquio.pdf. Gravità: alta.

B.10 colloquio, nessuna scelta d'ufficio [issue: I-03] [tipo: assenza]
Verifica: il deliverable non indica come data del colloquio una sola delle due date, 12 o 13 maggio, in assenza dell'indicazione della discordanza.
Pass se: dove è indicata una sola data del colloquio, nella stessa riga compare l'indicazione della discordanza.
Fail se: una delle due date è indicata come data del colloquio e l'altra non compare in alcuna cella.
— Fonte: 04 + 05. Gravità: alta.

B.11 evento contestato [issue: I-04] [tipo: valore]
Verifica: il deliverable indica come collocazione temporale del fatto contestato la settimana del 27 aprile.
Pass se: compare, riferito al fatto contestato, il 27 aprile o la settimana del 27 aprile.
Fail se: al fatto contestato è associata una data diversa, oppure il fatto contestato non compare nella cronologia.
— Fonte: 02_contestazione_disciplinare.pdf. Gravità: media.

B.12 segnalazione interna [issue: I-04] [tipo: valore]
Verifica: il deliverable indica il 4 maggio come data della segnalazione interna del fatto.
Pass se: il 4 maggio compare riferito all'email interna HR.
Fail se: riporta una data diversa, oppure l'email interna non compare nella cronologia.
— Fonte: 01_email_interna_HR.pdf. Gravità: media.

B.13 evento e scoperta distinti [issue: I-04] [tipo: assenza]
Verifica: il deliverable non indica il 4 maggio come data del fatto contestato.
Pass se: il 4 maggio compare solo come data della segnalazione interna.
Fail se: il 4 maggio è indicato come data in cui il fatto contestato si è verificato.
— Fonte: 01 + 02. Gravità: alta.

B.14 decorrenza del termine a difesa [issue: I-05] [tipo: presenza]
Verifica: il deliverable afferma che il termine per presentare le giustificazioni decorre dalla consegna della contestazione dell'11 maggio.
Pass se: compare, riferito al termine per le giustificazioni, la decorrenza dall'11 maggio o dalla consegna/ricezione della contestazione.
Fail se: la decorrenza è ancorata al 6 maggio o al 7 maggio, oppure la decorrenza non compare.
— Fonte: 03 + 02. Gravità: alta.

B.15 prossimità fra termine e licenziamento [issue: I-05] [tipo: presenza]
Verifica: il deliverable segnala la prossimità temporale fra la scadenza del termine per le giustificazioni e la data del licenziamento.
Pass se: compare una fra: «ravvicinate», «prossime», «a distanza di pochi giorni», «intervallo ristretto», riferita ai due momenti.
Fail se: i due momenti sono riportati senza alcuna delle formulazioni elencate.
Indifferente: l'indicazione del numero di giorni di intervallo.
— Fonte: 03 + 06 + 08. Gravità: media.

B.16 nessun giudizio sul termine a difesa [issue: I-05] [tipo: assenza]
Verifica: il deliverable non afferma che il termine per le giustificazioni non è stato rispettato.
Pass se: non compare l'affermazione che il termine è stato violato, compresso o non rispettato.
Fail se: compare una fra: «termine non rispettato», «termine violato», «giustificazioni non attese».
— Fonte: prompt, oggetto del deliverable. Gravità: alta.

B.17 PEC, accettazione e consegna distinte [issue: I-06] [tipo: presenza]
Verifica: per la lettera di licenziamento il deliverable riporta separatamente la ricevuta di accettazione e la ricevuta di consegna della PEC.
Pass se: compaiono, riferite alla PEC del licenziamento, sia «accettazione» sia «consegna», con i rispettivi momenti.
Fail se: compare un solo momento della PEC, oppure i due momenti non sono distinti.
— Fonte: 09_ricevuta_PEC_licenziamento.pdf. Gravità: alta.

B.18 PEC, efficacia dalla consegna [issue: I-06] [tipo: assenza]
Verifica: il deliverable non indica l'accettazione della PEC come momento di efficacia della lettera di licenziamento.
Pass se: nella colonna efficacia del licenziamento compare la consegna, non l'accettazione.
Fail se: la colonna efficacia riporta la data o l'ora dell'accettazione.
— Fonte: 09_ricevuta_PEC_licenziamento.pdf. Gravità: alta.

B.19 simmetria del controllo — giustificazioni [issue: I-07] [tipo: presenza]
Verifica: il deliverable applica anche alle giustificazioni della lavoratrice la distinzione fra formazione, invio e consegna.
Pass se: per le giustificazioni sono compilate le celle formazione e ricezione/consegna con i momenti risultanti dalla ricevuta PEC.
Fail se: per le giustificazioni compare una sola data, oppure le celle formazione o consegna sono vuote.
— Fonte: 06_giustificazioni_lavoratrice.pdf + 07_ricevuta_PEC_giustificazioni.pdf. Gravità: alta.

B.20 non-issue — distanza formazione/spedizione [issue: I-08] [tipo: assenza]
Verifica: il deliverable non qualifica come retrodatazione o come vizio la distanza fra la data della contestazione, 6 maggio, e la data della sua spedizione, 7 maggio.
Pass se: riferito a quelle due date non compare nessuna fra: «retrodatazione», «retrodatata», «vizio», «irregolarità», «anomalia».
Fail se: compare una di quelle qualificazioni.
Indifferente: la semplice indicazione delle due date in celle diverse.
— Fonte: 02 + 03. Gravità: alta.

B.21 non-issue — sfasamento data in calce/consegna PEC [issue: I-08] [tipo: assenza]
Verifica: il deliverable non qualifica come anomalia lo sfasamento fra la data in calce alla lettera di licenziamento, 15 maggio, e la consegna della PEC, 16 maggio.
Pass se: riferito a quelle due date non compare nessuna fra: «anomalia», «irregolarità», «vizio», «incongruenza».
Fail se: compare una di quelle qualificazioni.
— Fonte: 08 + 09. Gravità: media.

B.22 non-issue — intervallo spedizione/consegna raccomandata [issue: I-08] [tipo: assenza]
Verifica: il deliverable non qualifica come anomalia l'intervallo fra la spedizione della raccomandata, 7 maggio, e la sua consegna, 11 maggio.
Pass se: riferito a quell'intervallo non compare nessuna fra: «anomalia», «irregolarità», «ritardo anomalo», «vizio della notifica».
Fail se: compare una di quelle qualificazioni.
— Fonte: 03_avviso_ricevimento_raccomandata.pdf. Gravità: media.

B.23 nessun giudizio di invalidità [issue: I-09] [tipo: assenza]
Verifica: il deliverable non afferma che il licenziamento è nullo, illegittimo, inefficace o annullabile.
Pass se: nessuna di quelle qualificazioni compare riferita al licenziamento.
Fail se: compare una fra: «nullo», «illegittimo», «inefficace», «annullabile», riferita al licenziamento.
Indifferente: la segnalazione delle discordanze di data richiesta da B.9.
— Fonte: prompt, oggetto del deliverable. Gravità: alta.

B.24 nessun giudizio di legittimità [issue: I-09] [tipo: assenza]
Verifica: il deliverable non afferma che il licenziamento è valido o legittimo.
Pass se: nessuna di quelle qualificazioni compare riferita al licenziamento.
Fail se: compare una fra: «valido», «legittimo», «regolare», riferita al licenziamento.
— Fonte: prompt, oggetto del deliverable. Gravità: alta.

B.25 divieto di presunzione dell'esito [issue: I-09] [tipo: assenza]
Verifica: il deliverable non afferma che l'impugnazione del licenziamento sarà accolta.
Pass se: non compare alcuna previsione sull'esito dell'impugnazione.
Fail se: compare una fra: «l'impugnazione sarà accolta», «il licenziamento verrà annullato», «la lavoratrice otterrà la reintegrazione».
— Fonte: prompt, oggetto del deliverable. Gravità: alta.

C. Date e valori calcolati — non applicabile
Il workflow non computa termini: nessuna data del deliverable è il risultato di un calcolo. Le date esatte sono verificate meccanicamente nei criteri B di tipo valore (B.1, B.2, B.3, B.5, B.7, B.11, B.12).

Raccordo issue → atomi: I-01 date distinte sullo stesso atto (B.1-B.4) · I-02 recettizietà (B.5-B.8) · I-03 conflitto sulla data del colloquio (B.9-B.10) · I-04 evento contestato e scoperta (B.11-B.13) · I-05 dipendenza del termine a difesa (B.14-B.16) · I-06 PEC accettazione/consegna (B.17-B.18) · I-07 simmetria del controllo (B.19) · I-08 sovra-segnalazione degli sfasamenti fisiologici (B.20-B.22) · I-09 nessun giudizio di merito e divieto di presunzione (B.23-B.25).

