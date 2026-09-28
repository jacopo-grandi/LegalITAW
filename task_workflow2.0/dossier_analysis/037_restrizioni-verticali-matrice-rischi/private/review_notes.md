# WF2-037 — Note di revisione interna

## Ordine di lavoro effettivamente seguito

1. Lettura di `procedura_nuovo_caso.md` e `metodo_e_convenzioni.md`; verifica che il verticale antitrust
   non fosse rappresentato sul benchmark e che la leva della soglia esatta, già usata nei casi KYC, non
   fosse riproposta con lo stesso oggetto e lo stesso metodo.
2. Verifica delle fonti primarie: reperimento dei testi **verbatim** del reg. (UE) 2022/720 (artt. 1, 2,
   3, 4, 5, 8, 10 e 11), degli Orientamenti 2022/C 248/01 (punti 96, 99, 100, 185, 187, 188, 189, 190,
   191, 198, 208 e 209), della comunicazione de minimis (punti 2, 8 e 13), della l. 287/1990 (artt. 1,
   comma 4, e 2), del reg. (CE) n. 1/2003 (art. 5) e dell'art. 101 TFUE, da EUR-Lex e Normattiva.
   Nessuna norma, nessuna soglia e nessun punto degli Orientamenti è stato citato a memoria.
3. Challenge map, scritta prima dei documenti, con l'elenco chiuso delle cinque etichette di
   qualificazione deciso in questa fase: è la decisione che ha reso judgeable l'intero caso.
4. Ricerca degli esemplari reali per ciascun tipo di documento.
5. Fissazione delle date, delle quote e dei valori con script, compresa la verifica che la soglia sia
   superata su un perimetro e non sull'altro e che entrambi i perimetri restino sopra il de minimis.
6. Redazione dei nove documenti.
7. Rubrica in prosa, poi rubrica atomizzata da sorgente unica.
8. Gold e distrattore; verifica del gold contro la propria rubrica.

## La decisione centrale: l'elenco chiuso delle etichette

Il problema di un deliverable di qualificazione è che «rischio alto» o «clausola problematica» non sono
verificabili da un judge che non conosce il diritto. La soluzione adottata è un **elenco chiuso di
cinque etichette**, esposto al modello nel `response_template.md`: `restrizione fondamentale`,
`restrizione esclusa`, `coperta dall'esenzione`, `fuori dall'esenzione da valutare`, `non restrittiva`.

Le conseguenze sono tre, tutte volute:

1. i criteri di tipo `qualificazione` diventano confronti fra due stringhe e non richiedono al judge
   alcun giudizio di gravità;
2. il criterio A.4 diventa meccanico: si verifica che ogni riga porti una sola etichetta dell'elenco;
3. i sette divieti sui controlled non-issue diventano il controllo più solido dei tre casi del batch,
   perché non chiedono al judge se un elemento «è segnalato come rischio» ma quale etichetta compare
   nella riga.

Il costo è che l'elenco è nel materiale somministrato. Non è un anticipo della soluzione: è il
vocabolario dell'output, come le sezioni obbligatorie. La distinzione fra le cinque etichette
corrisponde però all'architettura del regolamento, e questo va detto: chi legge l'elenco sa che esiste
una categoria «restrizione esclusa» distinta da «restrizione fondamentale». È un aiuto strutturale, che
riduce la difficoltà dell'issue I-06 e I-07 in cambio della verificabilità. La scelta va confermata dal
validatore.

## Scelte discrezionali

1. **La proporzione fra elementi problematici e non problematici è deliberatamente sbilanciata**: su
   quattordici righe della matrice, tre sono restrizioni fondamentali, una è restrizione esclusa, due
   sono fuori dall'esenzione da valutare, cinque sono coperte dall'esenzione e due non sono restrittive.
   È la risposta alla richiesta di non trasformare automaticamente ogni clausola restrittiva in
   violazione.
2. **La diffida del rivenditore è stata riscritta.** La prima stesura conteneva la qualificazione
   antitrust («non è una raccomandazione ma l'imposizione di un prezzo minimo di rivendita») e l'osservazione
   che l'invito alla segnalazione è uno strumento di controllo. Consegnava l'issue I-01. La versione
   attuale argomenta sul piano contrattuale, invocando la clausola che riconosce al rivenditore la
   libera determinazione del prezzo, e riferisce fatti — di essere stato oggetto di segnalazione, il
   danno da sospensione degli ordini — senza qualificarli.
3. **Nessun provvedimento dell'AGCM o della Commissione è citato.** Il caso poggia su regolamento,
   Orientamenti e comunicazioni, che sono testi verificabili verbatim. Citare un precedente decisorio
   avrebbe richiesto una verifica che non è stata fatta, e l'elenco chiuso lo esclude espressamente.
4. **Il profilo orizzontale del comitato commerciale non è qualificato.** Sarebbe stato il rilievo più
   grave del fascicolo, e per questo è stato lasciato fuori: qualificarlo avrebbe spostato il caso dalle
   restrizioni verticali agli accordi orizzontali e avrebbe richiesto un altro reference pack. Resta
   come questione riservata al parere legale, che è la collocazione onesta.
5. **La quantificazione dell'esposizione è fuori perimetro e non è penalizzata in sé**: è penalizzato
   il pronostico sull'esito. La distinzione è nei punti neutri e nel criterio B.38.
6. **Il documento 07 è un foglio di calcolo con formule, non con valori digitati.** È il formato reale, e
   rende il calcolo verificabile da chi rilegge il caso.
7. **Nove documenti.** È il fascicolo più ampio dei tre casi del batch, ed è coerente con la famiglia:
   un'analisi di dossier misura anche la capacità di incrociare documenti. Nessuno è un foglio di
   sintesi.

## Fragilità note, da risolvere in calibrazione

1. **C.3 e C.4 si risolvono sulla stessa stringa «2028»** su porzioni diverse del deliverable: l'anno
   dei dati e l'anno del primo superamento. Il controllo meccanico deve distinguere il contesto. Se
   l'implementazione non ci riesce, i due criteri vanno unificati oppure C.4 va spostato al judge. È
   annotato anche nel routing.
2. **B.15 e B.16 sono un accoppiamento delicato.** B.15 chiede l'affermazione generale sulle restrizioni
   fondamentali, B.16 quella sulle restrizioni escluse. Il distrattore afferma la prima e sbaglia la
   seconda: se in calibrazione fallisce anche B.15, i due criteri vanno riformulati per separare
   l'enunciato dalla sua applicazione.
3. **C.5 nel distrattore è di esito incerto.** Il distrattore non tratta il periodo di due anni civili:
   C.5 potrebbe fallire pur non essendo nell'elenco atteso. Va risolto in calibrazione, non prima.
4. **L'elenco chiuso delle etichette riduce la difficoltà di I-06 e I-07.** Vedi sopra: è un aiuto
   strutturale consapevole, in cambio della verificabilità. Se il validatore preferisce non darlo, i
   criteri di tipo `qualificazione` vanno riscritti come `presenza` sull'affermazione, con una perdita
   secca di judgeability.
5. **Sette controlled non-issue su sedici issue è una proporzione alta.** È voluta, e la procedura la
   raccomanda per i workflow di review. Va però verificato che non renda il caso «facile a segnalare
   poco»: la contromisura è che i criteri positivi sulle tre restrizioni fondamentali e sullo scambio di
   informazioni sono nove, e un deliverable prudente li perde tutti.
6. **La calibrazione del Passo 5 non è stata eseguita.** Il gold è verificato contro la propria rubrica
   in forma tabellare; il distrattore è scritto con l'elenco dei criteri attesi, ma il fallimento non è
   stato misurato. Il caso non è `pilot_ready`.
