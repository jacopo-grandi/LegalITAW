# WF2-038 — Finanziamento corporate: covenant, eventi di default, cambio di controllo e garanzie

`review_only` · Banking & Finance, finanziamenti corporate · contratto in essere · data di riferimento **giovedì 15 aprile 2032**

Caso costruito secondo `procedura_nuovo_caso.md` e `metodo_e_convenzioni.md`.
**Stato: draft**, in attesa di validazione professionale. Nulla è stato caricato su Notion, nessun run è stato eseguito.

## Contenuto

```
batch_WF2-038_040/WF2-038_finanziamento-corporate-covenant-default/
├── README.md
├── task_spec.json
├── public/                                     ← materiale somministrabile
│   ├── 01_task.md                              prompt integrale ed elenco allegati
│   ├── 02_reference_pack.md                    elenco chiuso delle fonti normative
│   ├── 03_legal_sources.md                     fonti primarie e modelli reali, con URL e freeze
│   ├── response_template.md                    struttura attesa del deliverable
│   └── documents/                              11 documenti del fascicolo, .md e .pdf, più un .xlsx
├── private/                                    ← busta privata, NON somministrabile
│   ├── evaluation_criteria.md                  rubrica in prosa, a livello di issue
│   ├── criteria_atomized.md                    rubrica atomizzata, 72 atomi, forma a campi
│   ├── rubric.json                             la stessa rubrica in forma eseguibile
│   ├── runtime_routing.json                    instradamento judge / verifica meccanica
│   └── review_notes.md                         bivi e scelte discrezionali della costruzione
├── source/authoring/                           ← materiale di costruzione
│   ├── challenge_map.md                        issue, non-issue, divieti, meccanismi, evidenze
│   ├── gold_standard.md                        deliverable di riferimento
│   ├── distractor.md                           versione sbagliata su tre gruppi di errori
│   ├── calibrazione.json                       ancore del surrogato deterministico
│   ├── date_e_valori_verificati.md             output dello script di verifica
│   ├── fonti_documentali.md                    esemplari reali seguiti e note di grounding
│   ├── fonti_chiuse.json                       elenco chiuso in forma leggibile da script
│   ├── legal_validation.md                     scheda per chi firma la validazione
│   ├── verifica_wf2_038.py                     75 asserzioni su date, importi e rapporti
│   ├── build_prospetto_038.py                  generatore del prospetto covenant .xlsx
│   └── build_rubric_038.py                     generatore delle tre forme della rubrica
└── runs/README.md                              come si eseguono e si valutano i run
```

## Che cosa misura

Il caso misura la capacità di distinguere tre livelli che i modelli tendono a collassare in uno:
**la violazione di un impegno**, **l'evento di default** e **la conseguenza che il creditore può
attivare**. Alla data di riferimento l'impegno sulla Leva Finanziaria è violato, l'evento di
default non è ancora maturato, e nessuna conseguenza opera senza la dichiarazione dell'agente su
istruzione della maggioranza delle banche. Rispondere «siamo in default, le banche possono
revocare» è l'errore-bersaglio.

Per arrivare alla violazione servono due passaggi indipendenti, entrambi necessari. Il primo è il
livello applicabile: l'atto modificativo del 2031 ha derogato alla scaletta del contratto per le
sole Date di Verifica di quell'anno, e il certificato di conformità indica il livello sbagliato.
Il secondo è il perimetro dell'indebitamento: un finanziamento soci di 7.830.000 euro è
dichiarato postergato nel prospetto di calcolo, ma l'atto di postergazione copre i soli crediti
del proprio allegato e sottopone i crediti successivi alla propria disciplina solo con un atto di
adesione che nel fascicolo non c'è. Incluso quel credito, l'indice passa da 3,42x a 3,96x.

Il terzo asse è il rimedio. La clausola di *equity cure* esiste, la finestra di venti Giorni
Lavorativi è ancora aperta, e la facoltà è preclusa perché è già stata esercitata alla Data di
Verifica immediatamente precedente. È presenza contro adeguatezza nella forma più pura: la
clausola c'è e non serve.

Il quarto asse è il cambio di controllo, che la definizione contrattuale misura moltiplicando le
partecipazioni lungo la catena: il permanere del controllo della capogruppo non salva la soglia,
e l'esenzione per le riorganizzazioni infragruppo non si applica perché la newco non è
interamente controllata.

I due errori-bersaglio simmetrici sono la **sovra-segnalazione** (trattare come violato il DSCR
che è esattamente sulla soglia, contestare la validità della fideiussione che l'importo massimo
garantito ce l'ha, presentare come rischio una clausola scritta a favore del cliente) e la
**prudenza paralizzante** (concludere che senza il bilancio certificato la posizione non è
determinabile).

Sulla priorità c'è una trappola a sé: il rilievo più grave non è quello con la scadenza più
vicina. La diffida del locatore finanziario scade il giorno successivo alla data di riferimento.

## Verifiche eseguite

```
python3 source/authoring/verifica_wf2_038.py     75 asserzioni, 0 errori
python3 source/authoring/build_rubric_038.py     72 atomi, nessun atomo orfano, nessun issue scoperto
python3 ../_check_gold.py .                      gold 100%, distrattore fallisce esattamente 11 criteri
python3 ../_validate_case.py .                   struttura, instradamento, fonti, anagrafica
```

La calibrazione del Passo 5 è eseguita come **surrogato deterministico**: il judge non è
disponibile in fase di build. Cinquantadue criteri su settantadue sono verificabili per via
testuale; i restanti venti restano affidati al judge e non sono stati calibrati.

## Come si carica sul board, quando dirai di procedere

| Proprietà | Valore |
|---|---|
| Caso d'uso | Finanziamento corporate. Rassegna della posizione del gruppo su covenant, eventi di default, cambio di controllo e garanzie |
| Use-case family | Review and redline |
| Macro area | Contrattualistica, Corporate / M&A |
| Prompt | contenuto di `public/01_task.md`, fra i separatori |
| Criteri di valutazione | contenuto di `private/evaluation_criteria.md` |
| Criteri atomizzati | contenuto di `private/criteria_atomized.md` |
| Allegati | gli 11 file di `public/documents/` nella forma impaginata |
| Data | data del caricamento |
