# WF2-040 — Matrice probatoria su una pretesa risarcitoria da inadempimento

`evidence_matrix` · Contenzioso commerciale · fase stragiudiziale · data di riferimento **giovedì 22 giugno 2034** · termine della diffida **12 luglio 2034**

Caso costruito secondo `procedura_nuovo_caso.md` e `metodo_e_convenzioni.md`.
**Stato: draft**, in attesa di validazione professionale. Nulla è stato caricato su Notion, nessun run è stato eseguito.

## Contenuto

```
batch_WF2-038_040/WF2-040_matrice-probatoria-inadempimento-fornitura/
├── README.md
├── task_spec.json
├── public/                                     ← materiale somministrabile
│   ├── 01_task.md                              prompt integrale ed elenco allegati
│   ├── 02_reference_pack.md                    elenco chiuso delle fonti normative
│   ├── 03_legal_sources.md                     fonti primarie e modelli reali, con URL e freeze
│   ├── response_template.md                    struttura attesa del deliverable
│   └── documents/                              13 documenti: 12 PDF e un XLSX
├── private/                                    ← busta privata, NON somministrabile
│   ├── evaluation_criteria.md                  rubrica in prosa, a livello di issue
│   ├── criteria_atomized.md                    rubrica atomizzata, 68 atomi
│   ├── rubric.json                             la stessa rubrica in forma eseguibile
│   ├── runtime_routing.json                    instradamento judge / verifica meccanica
│   └── review_notes.md                         bivi e scelte discrezionali della costruzione
├── source/authoring/
│   ├── challenge_map.md                        issue, non-issue, divieti, meccanismi, evidenze
│   ├── gold_standard.md                        deliverable di riferimento
│   ├── distractor.md                           versione sbagliata su tre gruppi di errori
│   ├── calibrazione.json                       ancore del surrogato deterministico
│   ├── date_e_valori_verificati.md             output dello script di verifica
│   ├── fonti_documentali.md                    esemplari reali seguiti e note sulla taratura dei numeri
│   ├── fonti_chiuse.json                       elenco chiuso in forma leggibile da script
│   ├── legal_validation.md                     scheda per chi firma la validazione
│   ├── verifica_wf2_040.py                     69 asserzioni su date, termini e importi
│   ├── build_prospetto_040.py                  generatore del prospetto dei maggiori costi .xlsx
│   └── build_rubric_040.py                     generatore delle tre forme della rubrica
└── runs/README.md
```

## Che cosa misura

Il caso misura la capacità di tenere separati **tre importi che quasi tutti collassano in uno**:
quello che la controparte chiede, quello che il fascicolo documenta e quello che è giuridicamente
recuperabile. Sono 3.240.000, 1.320.000 e 499.600 euro, che il massimale contrattuale riporta a
372.000. Il passaggio dal primo al quarto non è una sottrazione: è una ricostruzione voce per voce,
e il massimale si applica in coda, non come sconto sulla richiesta.

Il fascicolo è costruito su tre episodi con esiti diversi. Quello di novembre è indifendibile
nell'an, perché è il rapporto del tecnico del nostro stesso assistito a parlare di difetto di
progetto. Quello di gennaio è difendibile per decadenza — ventisei giorni fra scoperta e denuncia
scritta, contro i quindici pattuiti — ma la difesa poggia su un termine convenzionale più breve di
quello legale di sessanta giorni, e il caso misura se il deliverable lo solleva **senza darlo per
acquisito**. Quello di aprile è difendibile nel merito, perché il film impiegato dal committente
misurava 21,4-22,6 micron contro i 28 con tolleranza di ± 2 della specifica.

Il quarto asse è il documento che in ogni fascicolo di questo tipo qualcuno ha scritto: l'email del
direttore commerciale che offre 250.000 euro e ammette il difetto. È cordiale, è in buona fede, ed
è già citata dal legale della controparte. Ignorarla, o liquidarla per difetto di poteri, è
l'errore che il caso punisce più severamente.

Gli errori-bersaglio sono simmetrici e, a differenza di un caso costruito lato attore, il più
pericoloso è la **sovra-asserzione difensiva**: dare per acquisita la decadenza, dichiarare
inutilizzabile la relazione di controparte, eccepire la rinuncia per pagamento del saldo senza
riserve. Tre criteri di assenza li nominano uno per uno.

## Rapporto con WF2-025

È l'altro `evidence_matrix` del set. Il workflow e la famiglia del board coincidono: la diversità è
costruita sugli altri tre assi previsti dalla regola — verticale, lato assistito e forma del
deliverable — e nessuna trappola di WF2-025 è riusata. Il confronto per assi è in
`private/review_notes.md`; è il punto su cui conviene fermarsi per primo in sede di revisione.

## Verifiche eseguite

```
python3 source/authoring/verifica_wf2_040.py     69 asserzioni, 0 errori
python3 source/authoring/build_rubric_040.py     68 atomi, nessun atomo orfano, nessun issue scoperto
python3 ../_check_gold.py .                      gold 100%, distrattore fallisce esattamente 10 criteri
python3 ../_validate_case.py .                   struttura, instradamento, fonti, anagrafica
```

Lo script verifica anche la quadratura interna dei tre documenti contabili: il prospetto dei
maggiori costi, la nota di addebito del cliente finale e la fattura del terzo. I numeri non sono
solo corretti in assoluto: sono tarati nella relazione che fa scattare la trappola, e in
particolare l'esposizione ricostruita è sopra il massimale, perché il massimale morda.

La calibrazione del Passo 5 è eseguita come **surrogato deterministico**: il judge non è
disponibile in fase di build. Cinquantatré criteri su sessantotto sono verificabili per via
testuale; i restanti quindici restano affidati al judge.

## Come si carica sul board, quando dirai di procedere

| Proprietà | Valore |
|---|---|
| Caso d'uso | Contenzioso commerciale. Matrice probatoria sulla pretesa risarcitoria per inadempimento di un contratto di fornitura industriale |
| Use-case family | Dossier analysis |
| Macro area | Contenzioso, Contrattualistica |
| Prompt | contenuto di `public/01_task.md`, fra i separatori |
| Criteri di valutazione | contenuto di `private/evaluation_criteria.md` |
| Criteri atomizzati | contenuto di `private/criteria_atomized.md` |
| Allegati | i 13 file di `public/documents/` nella forma impaginata |
| Data | data del caricamento |
