# WF2-036 — Note di revisione interna

Registro dei bivi di costruzione, delle scelte discrezionali e delle fragilità note.

## Ordine di lavoro effettivamente seguito

1. Lettura di `procedura_nuovo_caso.md` e `metodo_e_convenzioni.md` e dei precedenti, in particolare del
   caso esistente sul verticale contiguo (condizioni generali SaaS), per verificare clausola per
   clausola che nessuna leva fosse riusata.
2. Verifica delle fonti primarie in rete: artt. 12-bis, 22, 64-bis, 64-ter, 64-quater e 110 l.
   633/1941; artt. 1341, 1342 e 2222 c.c.; testi delle cinque licenze, riprodotti verbatim dalle fonti
   ufficiali. Nessuna norma e nessuna clausola di licenza è stata citata a memoria.
3. Challenge map, scritta prima dei documenti.
4. Ricerca degli esemplari reali per ciascun tipo di documento e verifica che i difetti da inserire
   coincidessero con la prassi attestata anziché essere costruiti ad arte.
5. Fissazione del calendario e dei valori con script.
6. Redazione dei sette documenti, con il contratto generato da sorgente unica in `.docx` e `.md`.
7. Rubrica in prosa a livello di issue, poi rubrica atomizzata generata da sorgente unica.
8. Gold: nota delle modifiche più `gold_redline.docx` effettivamente prodotto, validato contro lo
   schema e reso in PDF per verificare la visibilità delle revisioni.

## Scelte discrezionali

1. **Contratto unico invece di due documenti separati.** Nella prassi italiana la licenza d'uso e lo
   sviluppo su commessa sono di regola due documenti (condizioni generali del fornitore più contratto
   o accordo quadro di sviluppo). Il caso li unifica perché il deliverable è un redline circoscritto e
   due documenti moltiplicherebbero il perimetro senza aggiungere difficoltà. La struttura resta quella
   attestata: le rubriche degli articoli e il loro ordine sono ripresi dagli esemplari reali. È la
   principale divergenza dalla prassi e va segnalata al validatore.
2. **Il difetto sulla titolarità non è costruito: è la prassi.** La clausola dell'articolo 6, commi 1 e
   2, riproduce l'impianto reale di un fornitore di servizi ICT, che non cede nulla e concede una
   licenza non esclusiva per uso interno. Questo è il punto di forza del caso rispetto all'anti-pattern
   dell'errore grossolano: il modello non trova la trappola per pattern-matching, perché non c'è nulla
   di anomalo da riconoscere. Deve leggere che cosa il cliente ha pagato e che cosa riceve.
3. **La garanzia no-copyleft è ristretta alla sola distribuzione.** Entrambe le formulazioni esistono
   nella pratica; la scelta della più stretta è deliberata e costituisce il difetto di livello.
4. **Il perimetro escluso è ampio e comprende il massimale.** Serve a due scopi: non riusare le leve del
   caso esistente sul verticale contiguo, e creare un test di sovra-intervento verificabile
   meccanicamente (criterio A.4) e nominato (B.42, B.43, B.44). Il costo è che il caso non misura il
   giudizio sulla proporzionalità del massimale.
5. **Le due censure sui componenti a codice aperto non sono anticipate dai documenti.** La nota interna
   del responsabile tecnologie dice che «le licenze indicate non sono tutte dello stesso tipo e uno dei
   componenti risulta modificato dal fornitore», e dichiara di non avere competenza per trarne
   conseguenze. È il massimo di segnalazione compatibile con il divieto di anticipare la soluzione:
   indica dove guardare, non che cosa concludere.
6. **Sette documenti.** Ciascuno ha una funzione dichiarata nella challenge map. Non è stato inserito
   alcun foglio di sintesi: l'Allegato B è l'elenco reale dei componenti, non un recap del fascicolo.
7. **Il limite di parole della nota è stato alzato da 1.500 a 2.200** dopo la scrittura del gold: la
   tabella di sintesi richiesta dal template occupa da sola circa settecento parole con sedici
   modifiche. Il limite iniziale rendeva il compito impossibile senza sacrificare le sezioni di merito.
8. **Il gold redline è prodotto da uno script e non scritto a mano.** In questo modo il testo delle
   modifiche attese è versionato, riproducibile e confrontabile, e la marcatura delle revisioni è
   verificabile contro lo schema.

## Fragilità note, da risolvere in calibrazione

1. **I criteri B.34, B.36 e B.37 vietano di segnalare tre componenti come rischio di contaminazione, e
   il gold li nomina per dire il contrario.** Se un judge legge la menzione critica come segnalazione,
   la formula va irrigidita. È la fragilità più seria del caso, perché quei tre criteri sono il cuore
   del test sulla sovra-segnalazione.
2. **La coppia sovra-segnalazione / rilevazione corretta sullo stesso issue I-05.** L'issue contiene sia
   criteri positivi (B.9, B.10) sia divieti nominati (B.11, B.34-B.37, B.39). Se in calibrazione il
   fallimento dei divieti si propaga ai positivi, l'issue va spezzato in due, distinguendo la
   rilevazione del componente AGPL dal trattamento degli altri quattro.
3. **La resa del redline in testo per il judge.** I criteri di merito sul redline parlano di «testo
   inserito» e «testo cancellato»: dipendono dalla procedura di conversione descritta in
   `private/runtime_routing.json`. Se quella conversione perde la marcatura, quaranta criteri su
   cinquantotto diventano inverificabili. È una dipendenza infrastrutturale, non giuridica, e va
   collaudata prima del primo run.
4. **A.4 è un criterio meccanico non banale.** Verificare che nessuna revisione ricada negli articoli
   esclusi richiede di individuare la posizione delle intestazioni degli articoli nel flusso dei
   paragrafi. Il metodo è descritto nel routing ma non è ancora implementato.
5. **I-04 e I-12 sono i due issue più debolmente ancorati.** Il primo riguarda una clausola diffusa
   nella prassi e discutibile ma non chiaramente patologica; il secondo chiede l'introduzione di un
   diritto che il contratto semplicemente non prevede. Sono i primi due da togliere se il validatore
   ritiene il caso troppo carico.
6. **La calibrazione del Passo 5 non è stata eseguita.** Il gold è verificato contro la propria rubrica
   in forma tabellare e il redline è stato prodotto e validato, ma il gold non è stato sottoposto ai
   tre judge e il fallimento del distrattore non è stato misurato. Il caso non è `pilot_ready`.
