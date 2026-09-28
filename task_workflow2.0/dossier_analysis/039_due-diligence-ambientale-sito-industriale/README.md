# WF2-039 — Due diligence ambientale: red flag e azioni pre-closing su un sito industriale

`due_diligence_memo` · Environmental / ESG · operazione non perfezionata · data di riferimento **martedì 5 aprile 2033** · closing previsto **30 giugno 2033**

Caso costruito secondo `procedura_nuovo_caso.md` e `metodo_e_convenzioni.md`.
**Stato: draft**, in attesa di validazione professionale. Nulla è stato caricato su Notion, nessun run è stato eseguito.

## Contenuto

```
batch_WF2-038_040/WF2-039_due-diligence-ambientale-sito-industriale/
├── README.md
├── task_spec.json
├── public/                                     ← materiale somministrabile
│   ├── 01_task.md                              prompt integrale ed elenco allegati
│   ├── 02_reference_pack.md                    elenco chiuso delle fonti normative
│   ├── 03_legal_sources.md                     fonti primarie e modelli reali, con URL e freeze
│   ├── response_template.md                    struttura attesa del deliverable
│   └── documents/                              11 documenti: 9 PDF, un DOCX, un XLSX
├── private/                                    ← busta privata, NON somministrabile
│   ├── evaluation_criteria.md                  rubrica in prosa, a livello di issue
│   ├── criteria_atomized.md                    rubrica atomizzata, 70 atomi
│   ├── rubric.json                             la stessa rubrica in forma eseguibile
│   ├── runtime_routing.json                    instradamento judge / verifica meccanica
│   └── review_notes.md                         bivi e scelte discrezionali della costruzione
├── source/authoring/
│   ├── challenge_map.md                        issue, non-issue, divieti, meccanismi, evidenze
│   ├── gold_standard.md                        deliverable di riferimento
│   ├── distractor.md                           versione sbagliata su tre gruppi di errori
│   ├── calibrazione.json                       ancore del surrogato deterministico
│   ├── date_e_valori_verificati.md             output dello script di verifica
│   ├── fonti_documentali.md                    esemplari reali seguiti e note di grounding
│   ├── fonti_chiuse.json                       elenco chiuso in forma leggibile da script
│   ├── legal_validation.md                     scheda per chi firma la validazione
│   ├── verifica_wf2_039.py                     53 asserzioni su date, quantità e importi
│   ├── build_registro_039.py                   generatore del registro rifiuti .xlsx
│   └── build_rubric_039.py                     generatore delle tre forme della rubrica
└── runs/README.md
```

## Che cosa misura

Il caso misura la capacità di **non dare per accertato** ciò che il fascicolo non accerta. Un sito
industriale in esercizio dal 1972, con superamenti delle concentrazioni soglia di contaminazione e
un procedimento di bonifica aperto, invita a due conclusioni che i modelli producono quasi
automaticamente: che il sito sia contaminato e che il venditore ne sia responsabile. Il fascicolo
non consente né l'una né l'altra.

Il sito è **potenzialmente contaminato**: la qualificazione come contaminato dipende dal
superamento delle concentrazioni soglia di rischio, che l'analisi di rischio deve determinare.
Per una delle due aree quell'analisi è stata approvata e ha escluso il superamento — quell'area
esce dal procedimento; per l'altra non è mai stata presentata e il termine è scaduto da 238 giorni.
La responsabilità della contaminazione la accerta la provincia, che ha aperto il procedimento e non
ha adottato alcun atto: la sola presenza storica dell'attività industriale non è un accertamento.

Il terzo passaggio è la posizione del compratore. Come proprietario non responsabile non erediterà
l'obbligo di bonificare; erediterà obblighi di comunicazione e di prevenzione, e un rischio
economico che passa dall'onere reale e dal privilegio speciale, i quali però presuppongono
l'esecuzione d'ufficio, richiedono un provvedimento motivato e sono contenuti nel limite del valore
di mercato dell'area dopo gli interventi.

Il quarto asse è contrattuale ed è quello che decide l'operazione: massimale dell'indennizzo al
51,72% della stima, durata di ventiquattro mesi contro un procedimento che dura anni, perimetro
ancorato alla sola contaminazione già descritta, garanzie ambientali rese nei limiti della
conoscenza del venditore.

I controlled non-issue sono sette e sono deliberatamente pesanti: l'area A già chiusa, il sito di
interesse nazionale confinante ma non applicabile, l'amianto in matrice compatta con programma di
manutenzione attivo, la diffida di ARPA già ottemperata, il piezometro a monte idrogeologico, il
riesame fisiologico dell'autorizzazione e la clausola scritta a favore del compratore.

Trattandosi di un fascicolo *ex ante*, cinque criteri misurano direttamente la presenza di azioni
pre-closing concrete: un deliverable che elenca rischi senza dire che cosa fare entro il 30 giugno
non è utilizzabile.

## Verifiche eseguite

```
python3 source/authoring/verifica_wf2_039.py     53 asserzioni, 0 errori
python3 source/authoring/build_rubric_039.py     70 atomi, nessun atomo orfano, nessun issue scoperto
python3 ../_check_gold.py .                      gold 100%, distrattore fallisce esattamente 10 criteri
python3 ../_validate_case.py .                   struttura, instradamento, fonti, anagrafica
```

I valori soglia usati nei documenti sono quelli reali delle tabelle dell'Allegato 5 al Titolo V
della Parte Quarta, verificati su fonte: i superamenti costruiti nel fascicolo sono tarati su
quei valori.

La calibrazione del Passo 5 è eseguita come **surrogato deterministico**: il judge non è
disponibile in fase di build. Cinquantaquattro criteri su settanta sono verificabili per via
testuale; i restanti sedici restano affidati al judge.

## Un punto che va letto prima di congelare il caso

`source/authoring/legal_validation.md`, § 1.2. La posizione del proprietario non responsabile è
esposta a un contenzioso pendente davanti alla Corte di giustizia, su rimessione dell'Adunanza
plenaria del Consiglio di Stato. Va verificato lo stato di quel contenzioso alla data della
validazione e va deciso se il caso possa poggiare su quella regola.

## Come si carica sul board, quando dirai di procedere

| Proprietà | Valore |
|---|---|
| Caso d'uso | Due diligence ambientale. Matrice dei red flag e delle azioni pre-closing sull'acquisizione di un sito industriale |
| Use-case family | Dossier analysis |
| Macro area | Compliance & Regulatory, Corporate / M&A |
| Prompt | contenuto di `public/01_task.md`, fra i separatori |
| Criteri di valutazione | contenuto di `private/evaluation_criteria.md` |
| Criteri atomizzati | contenuto di `private/criteria_atomized.md` |
| Allegati | gli 11 file di `public/documents/` nella forma impaginata |
| Data | data del caricamento |
