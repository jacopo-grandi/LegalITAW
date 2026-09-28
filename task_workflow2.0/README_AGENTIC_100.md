# LegalITA Workflow 2.0 — benchmark agentico, edizione da 100 task

> **Snapshot storico del 4 settembre 2026.** I file di authoring citati più avanti
> (`planning/`, `pilot/`, `tools/`, `MIGRATION_WF2_031_100.md`, `source/`) restano nel
> repository di authoring legal-ITA e non fanno parte di LegalITA-W. Le sezioni sul runtime descrivono
> `agentic_workspace` e servono alla riproducibilità delle run precedenti. La
> lane interna primaria è ora `generic_agent`; il contratto corrente è in
> [`../docs/generic_agent_harness.md`](../docs/generic_agent_harness.md).

> Documento di contesto per LLM che mantengono, integrano o eseguono il benchmark. Non includere
> questo file nel contesto del modello sottoposto a evaluation: contiene la descrizione della busta
> privata, del gold e dei meccanismi di scoring. Durante una run il modello valutato deve vedere
> soltanto gli input pubblici dichiarati dal singolo `task_spec.json`.

Versione del documento: `0.2`. Snapshot operativo: **4 settembre 2026**.

## 1. Che cos'è questo corpus

LegalITA Workflow 2.0 valuta se un sistema linguistico riesce a svolgere un incarico legale italiano
come un agente che lavora su un fascicolo chiuso. Il sistema deve aprire documenti, distinguere fatti
e allegazioni, seguire dipendenze, calcolare date o valori quando servono e consegnare un artefatto
professionale nel formato richiesto. La risposta libera a una domanda di diritto è soltanto una
piccola parte del problema.

L'edizione descritta qui comprende **100 task**, identificati da `WF2-001` a `WF2-100`. Il
portafoglio è bilanciato per operazione professionale:

| Famiglia | Task | Quota |
|---|---:|---:|
| Dossier analysis | 34 | 34% |
| Review and redline | 33 | 33% |
| Procedural timeline | 33 | 33% |
| **Totale** | **100** | **100%** |

Tutti i casi, da WF2-001 a WF2-100, sono ora materializzati nel corpus canonico
`task_workflow2.0/`. I settanta casi dell'espansione conservano in `source/authoring/` gli snapshot
pre-migrazione; la precedente area `task_workflow2.0.1/` rimane una sorgente storica e non viene letta
dal runner.

Lo snapshot eseguibile comprende **5.032 criteri atomizzati** e 683 allegati materializzati. Tutti i profili
sono `pilot_ready` per run diagnostiche: schema, input pubblici, deliverable, rubriche e routing sono
caricabili dal runtime comune. Questo stato non sostituisce il sign-off legale blind né la
calibrazione judge-human, che restano gate distinti per una release gold.

## 2. A chi serve questo README

Un LLM può incontrare il benchmark in tre ruoli distinti. Confonderli produce leakage.

| Ruolo | Può leggere | Compito |
|---|---|---|
| Modello valutato | soltanto `public_inputs` | analizzare il fascicolo e produrre il deliverable |
| Judge | submission, criterio assegnato ed evidenze ammesse | emettere PASS, FAIL o unresolved per il criterio |
| Maintainer / integratore | corpus pubblico e privato, codice e report | costruire, correggere, validare e versionare i task |

Questo file è scritto per il terzo ruolo e, in parte, per chi configura runner e judge. Se stai
generando una submission come modello sottoposto a test, non devi usare rubriche, challenge map,
gold, distrattori o note di validazione legale.

## 3. L'unità di valutazione

Un task è un piccolo mandato professionale completo. Contiene un committente, il lato assistito, una
data di riferimento, lo stato del fascicolo, un insieme chiuso di documenti e un prodotto atteso. Il
fascicolo può essere sintetico, ma non è decorativo: ogni allegato deve provare un fatto, cambiare una
conclusione, rendere visibile una lacuna o esercitare un controllo sui falsi positivi.

Il deliverable può essere un memo, una matrice, una timeline, una nota di review o un DOCX con
revisioni. Alcuni task richiedono più file in una submission atomica. Il formato fa parte
dell'incarico: una risposta giuridicamente plausibile consegnata nel file sbagliato resta un errore
operativo.

Il singolo criterio atomizzato è l'unità minima di giudizio, ma **il task è l'unità statistica
principale**. Cinquanta criteri dello stesso caso condividono fascicolo, prompt e generazione; non
vanno trattati come cinquanta osservazioni indipendenti.

## 4. Cosa misuriamo

Il benchmark separa capacità che nei test question-answering tendono a confondersi.

| Dimensione | Domanda osservabile |
|---|---|
| Copertura documentale | Il modello ha aperto e usato tutte le fonti necessarie? |
| Fedeltà al fascicolo | Fatti, parti, date, importi e clausole corrispondono ai documenti? |
| Correttezza giuridica | La qualificazione applica la regola ammessa al fatto provato? |
| Sintesi cross-document | Il deliverable collega evidenze distribuite e conserva i conflitti? |
| Calcolo procedurale | Trigger, dies a quo, tipo di giorni, sospensioni e proroghe formano una catena corretta? |
| Disciplina dell'incertezza | Il modello distingue conclusioni, assunzioni, alternative e dati mancanti? |
| Controllo dei falsi positivi | Evita di trasformare un non-issue o un fatto non provato in una violazione? |
| Completezza | Copre tutte le issue che il fascicolo rende decidibili? |
| Scope discipline | Rispetta lato assistito, mandato, fonti chiuse e limiti del deliverable? |
| Qualità della revisione | Le modifiche proposte sono precise, coerenti e propagabili nel documento? |
| Conformità dell'artefatto | File, sezioni, tabelle, redline e submission rispettano il contratto? |
| Comportamento agentico | Il modello cerca, apre, registra decisioni operative, controlla e sottopone entro il budget? |

La qualità stilistica interessa solo quando incide sull'uso professionale: una matrice illeggibile,
una conclusione sepolta o una redline non applicabile sono errori; la distanza da una formula modello
non lo è.

### Cosa non misuriamo

- memoria libera di norme non presenti nel perimetro ammesso;
- abilità di indovinare il gold o imitare una frase di riferimento;
- chain-of-thought privata;
- successo ottenuto consultando la busta privata;
- certificazione della correttezza legale da parte del benchmark stesso;
- preferenza stilistica del judge non collegata a un criterio osservabile.

## 5. Le tre famiglie operative

La famiglia descrive il lavoro svolto, non la materia giuridica. Un caso privacy con calcolo di un
termine resta `procedural_computation`; una redline bancaria resta
`document_review_and_revision`.

### Dossier analysis — 34 task

Il modello ricostruisce un problema da più documenti e produce un memo, una matrice di rischi o una
evidence matrix. Qui pesano la provenienza delle affermazioni, la gestione dei conflitti, le lacune e
il controllo della sovra-segnalazione. Due diligence, investigazioni, coverage opinion e analisi di
responsabilità appartengono a questa famiglia quando il prodotto dominante è la sintesi del
fascicolo.

### Review and redline — 33 task

Il modello esamina una bozza, individua difetti o rischi e propone una revisione coerente con il lato
assistito. Il prodotto può essere una nota di review oppure una redline DOCX accompagnata da una
nota. Sono misurati perimetro, fedeltà documentale, precisione delle modifiche, assenza di falsi
positivi e coerenza fra clausole dipendenti.

### Procedural timeline — 33 task

Il modello costruisce una sequenza di adempimenti, scadenze o rimedi. La valutazione controlla
l'intera catena: evento iniziale, natura del termine, calendario, condizioni, rami alternativi,
conseguenze e azioni successive. Una data finale corretta ottenuta con un percorso sbagliato non
supera i criteri che verificano la derivazione.

## 6. Copertura giuridica: sedici aree

Ogni area compare almeno due volte in ciascuna famiglia. Quattro celle ricevono un caso aggiuntivo
per ospitare capstone o variazioni deliberate.

| Area primaria | Dossier | Review | Timeline | Totale |
|---|---:|---:|---:|---:|
| Corporate / M&A | 3 | 2 | 2 | 7 |
| Commercial Contracts | 2 | 3 | 2 | 7 |
| Litigation & Arbitration | 2 | 2 | 2 | 6 |
| Data Protection & Cyber | 2 | 2 | 3 | 7 |
| AML & Financial Crime | 2 | 2 | 2 | 6 |
| Employment | 2 | 2 | 2 | 6 |
| Compliance & Investigations | 3 | 2 | 2 | 7 |
| Insurance | 2 | 2 | 2 | 6 |
| Administrative & Public Procurement | 2 | 2 | 2 | 6 |
| Insolvency & Restructuring | 2 | 2 | 2 | 6 |
| Banking & Finance | 2 | 2 | 2 | 6 |
| Tax | 2 | 2 | 2 | 6 |
| Antitrust & Competition | 2 | 2 | 2 | 6 |
| IP & Technology | 2 | 2 | 2 | 6 |
| Real Estate & Construction | 2 | 2 | 2 | 6 |
| Environmental, Energy & ESG | 2 | 2 | 2 | 6 |
| **Totale** | **34** | **33** | **33** | **100** |

L'area primaria serve al bilanciamento. Le materie secondarie restano tag: un finanziamento usato in
una due diligence M&A non viene contato due volte.

## 7. Difficoltà e dimensione del fascicolo

La difficoltà descrive il numero e la qualità dei passaggi richiesti. Il numero di pagine, da solo,
non basta.

- `low`: percorso corto, pochi rami e valori direttamente verificabili;
- `medium`: evidenze distribuite, gerarchie documentali o più issue dipendenti;
- `high`: fonti in tensione, calcoli concatenati, molti rami, redline complesse o risposta
  correttamente condizionata dai dati mancanti.

Il `pack_tier` disciplina l'ampiezza del fascicolo:

| Tier | Indicazione progettuale |
|---|---|
| `small` | fascicolo essenziale; nei nuovi casi, tipicamente fino a 5 documenti |
| `medium` | più fonti con funzioni diverse; tipicamente 3–7 documenti |
| `large` | fascicolo esteso; tipicamente 8–12 documenti |

I valori sono guide di authoring, non un contratto universale per i primi trenta casi. Un allegato
inutile non rende il task più difficile: aggiunge rumore non governato.

## 8. Anatomia di un task

I casi nuovi convergono verso questa struttura. I primi trenta hanno alcuni nomi legacy, mappati nel
loro `task_spec.json`.

```text
WF2-NNN_slug/
├── README.md
├── DECISION_LOG.md
├── task_spec.json
├── public/
│   ├── 01_task.md
│   ├── 02_reference_pack.md
│   ├── 03_legal_sources.md
│   ├── response_template.md
│   └── documents/
├── private/
│   ├── evaluation_criteria.md
│   ├── criteria_atomized.md
│   ├── rubric.json
│   ├── runtime_routing.json
│   ├── review_notes.md
│   └── file di compatibilità per challenge map, gold e validazione
├── source/
│   ├── authoring/
│   │   ├── challenge_map.*
│   │   ├── gold_standard.md
│   │   ├── distractor.md
│   │   ├── legal_validation.md
│   │   └── registri di fonti, date e valori
│   └── gen/                  # eventuali generatori e renderer
└── runs/
    └── README.md
```

### Ordine delle fonti interne

1. `task_spec.json` governa identità, input pubblici, famiglia e output.
2. `public/01_task.md` governa l'incarico dato al modello.
3. `public/documents/` contiene il fascicolo somministrato.
4. `public/02_reference_pack.md` e `03_legal_sources.md` chiudono il perimetro informativo.
5. La challenge map privata governa issue, non-issue, dipendenze e funzione degli allegati.
6. Il gold descrive una soluzione sostanzialmente corretta, con i suoi limiti.
7. I criteri atomizzati traducono il caso in proposizioni decidibili.
8. `rubric.json` rende i criteri machine-readable.
9. `runtime_routing.json` assegna ogni criterio al meccanismo di verifica.
10. `legal_validation.md` registra fonti, assunzioni e questioni riservate al professionista.

Se due livelli divergono, non scegliere quello più comodo. Ricostruisci l'intenzione dal fascicolo,
correggi tutti i derivati e aggiungi un controllo che intercetti la stessa divergenza in futuro.

## 9. Separazione public/private

Il confine fra le due buste è parte del benchmark.

La busta `public/` contiene tutto ciò che il modello valutato può usare: incarico, documenti,
reference pack, fonti chiuse e template. Deve essere autosufficiente e non deve nominare gold,
challenge map, criteri, pass condition, distractor o percorsi privati.

La busta `private/` e `source/authoring/` appartiene a maintainer e valutatori. Contiene risposte
attese, errori-bersaglio e istruzioni di scoring. Un modello che riceve questi file non sta più
svolgendo il task: sta leggendo la soluzione.

La separazione vale anche per log, demo, caching e preprocessing. Il testo estratto dagli allegati
pubblici può essere indicizzato; i file privati non devono entrare nello stesso indice accessibile al
modello.

## 10. Provenienza e tempo

Nomi di persone, società, operazioni, numeri di ruolo, importi e corrispondenza sono sintetici. Le
fonti normative o istituzionali devono invece essere ufficiali e tracciabili. La descrizione più
corretta dei casi nuovi è `source-grounded synthetic`: storia inventata, regole ancorate a fonti
primarie.

Ogni caso dichiara una data di riferimento e, quando necessario, un freeze normativo. Una storia può
essere ambientata nel futuro rispetto al freeze; in quel caso il task non può pretendere la
conoscenza di diritto sopravvenuto. L'assunzione temporale deve essere pubblica, coerente con il gold
e registrata per il legal sign-off.

Notion è la provenienza storica dei primi task, non il database operativo della nuova edizione. Il
corpus locale è autoritativo per le run; nessun processo di authoring deve scrivere su Notion senza
una richiesta esplicita e un passaggio di sincronizzazione separato.

## 11. Challenge map, gold e distractor

La challenge map viene progettata prima del fascicolo. Per ogni issue stabilisce fatto portante,
fonte, regola, conclusione accettabile, dati mancanti, documenti necessari ed errore che il caso vuole
rendere osservabile. I `controlled_non_issues` fanno il lavoro opposto: verificano se il modello evita
un rilievo plausibile ma non sostenuto.

Il gold non è un tema da copiare. È una submission di riferimento che deve superare ogni criterio,
mostrare le ancore documentali e conservare le cautele richieste. Risposte formulate diversamente
possono passare quando sono sostanzialmente equivalenti.

Il distractor è una risposta deliberatamente difettosa. Prima dell'esecuzione dichiara quali criteri
intende far fallire; serve a verificare che rubrica e judge riconoscano omissioni, inferenze non
sostenute e percorsi di calcolo errati.

## 12. Criteri atomizzati e routing

Un criterio valuta una sola proposizione osservabile. Gli ID usano la forma `A.n`, `B.n` o `C.n`,
senza livelli annidati.

- se il modello deve dire qualcosa, il criterio è di presenza o qualificazione;
- se deve evitare un'affermazione, il criterio nomina precisamente il contenuto vietato;
- se deve produrre un valore, il criterio indica valore, contesto e derivazione;
- se esistono più alternative corrette, `pass_se`, `fail_se` e l'eventuale campo indifferente devono
  coprire l'intero spazio rilevante.

Rubrica narrativa, `criteria_atomized.md`, `rubric.json` e `runtime_routing.json` devono contenere gli
stessi ID e lo stesso numero di criteri. Il routing distingue almeno:

| Classe | Meccanismo |
|---|---|
| Meccanica | provenienza del requisito formale; nel contratto output-free passa al judge |
| Esatta | date, valori, conteggi, percentuali o stringhe nel contesto stabilito |
| Span / attribuzione | judge ristretto a una proposizione e alla sua fonte |
| Scansione / assenza | controllo dell'intero scope e conferma semantica |
| Semantica | coerenza trasversale, priorità, adeguatezza o distinzione fra tesi |
| Condizionale | attivazione deterministica e successiva verifica nella classe propria |

Il tipo logico e il meccanismo di controllo sono assi distinti. Nel contratto
`prompt_only_free_artifacts_v1` tutti i 5.032 criteri sono valutati dal judge. I 97 check legacy
restano disponibili soltanto come diagnostica e non incidono sullo score.

## 13. Scoring e aggregazione

I criteri richiesti ricevono `PASS`, `FAIL` o `unresolved`. Errori di esecuzione e artefatti mancanti
restano categorie tecniche separate.

```text
criterion_rate = criteri required PASS / criteri required valutati
all_pass       = true  se tutti i required sono PASS
all_pass       = false se almeno un required è FAIL
all_pass       = null  se un required resta unresolved
```

Non introdurre soglie arbitrarie per convertire il `criterion_rate` in successo del task. `all_pass`
è severo; il rate serve a diagnosticare dove e quanto il modello sbaglia. Gli unresolved vanno
riportati a parte, senza trasformarli in PASS o in zeri silenziosi.

Un report comparativo dovrebbe mostrare almeno:

- task success rate tramite `all_pass`;
- media e distribuzione del `criterion_rate` per task;
- risultati per famiglia, area, difficoltà e pack tier;
- errori per tassonomia;
- tool call, document coverage, latenza, token e fallimenti del protocollo;
- disaccordo judge-human e tasso di unresolved.

La media piatta dei criteri favorirebbe i task con rubriche più lunghe. Per la classifica principale
si aggrega prima dentro il task, poi fra task con peso uguale; eventuali macro-medie per famiglia o
area vanno pubblicate accanto al risultato complessivo.

## 14. Esecuzione agentica

In una run `agentic_workspace` il runtime crea un workspace temporaneo:

```text
matter/   copia read-only del prompt e dei documenti pubblici
work/     artefatti prodotti dal modello
```

Il modello non riceve accesso al filesystem host o alla rete. Opera attraverso un broker con
allowlist, attualmente fondato su:

- `list_files`;
- `search_documents`;
- `open_document`;
- `inspect_metadata`;
- `write_artifact`;
- `submit`.

Il runtime non impone nomi, numero o struttura degli artifact e non richiede un decision log. Le
indicazioni di output hanno valore soltanto se compaiono nel prompt o in un documento pubblico
espressamente richiamato. Lo schema privato e i nomi attesi restano dati di valutazione e non sono
esposti al modello.

Una parte finale del budget di step è riservata alla consegna. In quella fase il runtime può bloccare
nuove letture e chiedere al modello di controllare, scrivere e sottoporre. Questo evita che un agente
consumi tutti i turni esplorando il fascicolo e termini senza artefatto.

### Artefatti di run

Una run riuscita conserva almeno:

```text
submission.json
<artifact prodotti dal modello>
tool_trace.json
workspace_manifest.json
run_manifest.json
score.json                 # se il judge è stato eseguito
```

Timeout, errore del protocollo o esaurimento degli step devono comunque lasciare `failure.json`,
trace, manifest e gli eventuali artefatti parziali. Un fallimento operativo non va
rimosso dal campione: misura una proprietà dell'agente.

## 15. Tassonomia degli errori

La diagnosi distingue almeno:

| Classe | Significato |
|---|---|
| `MODEL_OMISSION` | requisito richiesto ma assente |
| `MODEL_WRONG_FACT` | fatto o valore contrario al fascicolo |
| `MODEL_WRONG_REASONING` | conclusione o computo derivati con passaggio errato |
| `MODEL_UNSUPPORTED_INVENTION` | dato, fonte o qualificazione inventati |
| `MODEL_FORMAT_FAILURE` | deliverable o submission non conformi |
| `CRITERION_AMBIGUOUS` | pass/fail non decidibili in modo univoco |
| `CRITERION_UNDOCUMENTED` | requisito non provabile dagli input pubblici |
| `CRITERION_WRONG` | criterio contrario al fascicolo o alla regola |
| `CRITERION_ROUTING` | meccanismo di verifica inadeguato |
| `JUDGE_ERROR` | il valutatore applica male un criterio corretto |
| `TOOL_OR_ARTIFACT_ERROR` | file, parser, renderer o broker falliscono |

Separare gli errori del modello da quelli del benchmark evita di premiare un sistema perché il judge
è permissivo o di penalizzarlo per una rubrica sbagliata.

## 16. Cosa significa “benchmark-usable”

`benchmark-usable` è un gate operativo, non ancora un valore uniforme in tutti i `task_spec.json`.
Un task soddisfa il gate quando:

1. il fascicolo pubblico è completo, apribile e privo di duplicati ingestibili;
2. il prompt è autosufficiente e non anticipa rubrica o soluzione;
3. nessun file privato, indizio di scoring o path autoriale compare nel pubblico;
4. challenge map, documenti, gold e rubrica descrivono lo stesso caso;
5. ogni criterio è atomico, decidibile e dimostrabile dagli input ammessi;
6. rubriche e routing hanno identità completa di ID e conteggi;
7. il gold supera tutti i criteri e il distractor fallisce quelli pre-dichiarati;
8. fonti, date, valori, festività e formule sono verificati;
9. PDF e contenitori Office si aprono; DOCX e redline sono stati renderizzati e ispezionati;
10. validatori locali e condivisi terminano senza errori strutturali;
11. nomi, identificativi, date portanti e valori non collidono involontariamente con altri casi;
12. un rapporto di readiness elenca controlli, correzioni e limiti residui.

Il gate autorizza run diagnostiche controllate. Non equivale a `gold_legal_signoff: approved`, né a
calibrazione riuscita del judge.

## 17. Stati e promozione

| Stato | Significato |
|---|---|
| `draft_for_legal_validation` | caso costruito o in revisione; vietata la promozione automatica |
| strutturalmente valido | layout del corpus e contratti macchina passano |
| benchmark-usable | eseguibile senza ambiguità tecnica secondo i dodici gate sopra |
| `pilot_ready` | ammesso a un pilot comparativo dopo decisione di release |
| gold approvato | legal sign-off blind e calibrazione del judge completati |

Questi livelli non si implicano automaticamente. Un task può essere strutturalmente verde e avere
un criterio giuridicamente sbagliato; può essere benchmark-usable per un test diagnostico mentre il
sign-off legale resta pending.

## 18. Catalogo dei 100 task

Le descrizioni seguenti sono indici, non prompt. Per i dettagli autoritativi leggere il
`task_spec.json` del caso; la matrice in `planning/WF2_031_100_MASTER_MATRIX.tsv` conserva il disegno
dell'espansione e non prevale sui profili migrati.

### WF2-001–010

| ID | Famiglia | Caso |
|---|---|---|
| WF2-001 | Review | Revisione di un DPA |
| WF2-002 | Timeline | Opposizione allo stato passivo e impugnazione del decreto |
| WF2-003 | Dossier | Check red flag di una data room M&A |
| WF2-004 | Review | Analisi di term sheet/SPA senza riscrittura |
| WF2-005 | Timeline | Termine per il ricorso al TAR contro un diniego |
| WF2-006 | Dossier | Istruttoria AML su operatività sospetta |
| WF2-007 | Dossier | Titolarità effettiva di una struttura KYC |
| WF2-008 | Review | Redline mirata di un patto di non concorrenza |
| WF2-009 | Dossier | Cronologia di una vicenda disciplinare |
| WF2-010 | Timeline | Signing-closing di una SPA con condizioni sospensive |

### WF2-011–020

| ID | Famiglia | Caso |
|---|---|---|
| WF2-011 | Timeline | Data breach: notifica al Garante e comunicazione agli interessati |
| WF2-012 | Dossier | Due diligence immobiliare prima del preliminare |
| WF2-013 | Review | Contratto di distribuzione lato fornitore |
| WF2-014 | Review | Redline circoscritta di un accordo quadro di subfornitura |
| WF2-015 | Timeline | Procedura di riduzione del personale |
| WF2-016 | Review | Riesame di un sistema di segnalazione interna |
| WF2-017 | Timeline | Opposizione a un decreto sanzionatorio AML |
| WF2-018 | Dossier | Cronologia di una delibera assembleare |
| WF2-019 | Dossier | Parere di copertura assicurativa |
| WF2-020 | Dossier | Riscontro istruttorio a una richiesta del Garante |

### WF2-021–030

| ID | Famiglia | Caso |
|---|---|---|
| WF2-021 | Review | Patti parasociali per l'ingresso di un socio di minoranza |
| WF2-022 | Dossier | Contestazione dell'earn-out dopo il closing |
| WF2-023 | Review | Condizioni SaaS: SLA, licenza e responsabilità |
| WF2-024 | Timeline | Revisione prezzi, forza maggiore e risoluzione |
| WF2-025 | Dossier | Sequestro conservativo: credito, periculum e beni |
| WF2-026 | Dossier | DPIA, scoring e trasferimento extra-SEE |
| WF2-027 | Review | Accordo transattivo con dirigente licenziato |
| WF2-028 | Timeline | Screening sanzionatorio ed escalation |
| WF2-029 | Dossier | Red flag 231 su un terzo verso la PA |
| WF2-030 | Timeline | Denuncia D&O in regime claims-made |

### WF2-031–040

| ID | Famiglia | Caso |
|---|---|---|
| WF2-031 | Dossier | Due diligence fiscale della target |
| WF2-032 | Timeline | Accertamento con adesione e ricorso |
| WF2-033 | Timeline | Polizza cyber claims-made e denuncia |
| WF2-034 | Review | Policy anticorruzione |
| WF2-035 | Timeline | Appalti: standstill, accesso e termini di impugnazione |
| WF2-036 | Review | Licenza software, titolarità e open source |
| WF2-037 | Dossier | Restrizioni verticali e matrice dei rischi |
| WF2-038 | Review | Finanziamento corporate, covenant e default |
| WF2-039 | Dossier | Due diligence ambientale di un sito industriale |
| WF2-040 | Dossier | Matrice probatoria su inadempimento di fornitura |

### WF2-041–050

| ID | Famiglia | Caso |
|---|---|---|
| WF2-041 | Timeline | Aumento di capitale riservato e iscrizioni |
| WF2-042 | Dossier | Portafoglio contratti e change of control |
| WF2-043 | Review | Atto di citazione: allegazioni, prove e quantificazione |
| WF2-044 | Timeline | Accesso ai dati del dipendente e dati di terzi |
| WF2-045 | Review | Procedura KYC ed enhanced due diligence per PEP |
| WF2-046 | Dossier | Qualificazione del rapporto e lavoro straordinario |
| WF2-047 | Timeline | Segnalazione whistleblowing e indagine interna |
| WF2-048 | Review | Polizza cyber: esclusioni e sublimiti |
| WF2-049 | Dossier | Modifica di concessione e interesse pubblico |
| WF2-050 | Review | Standstill agreement e protezioni dei creditori |

### WF2-051–060

| ID | Famiglia | Caso |
|---|---|---|
| WF2-051 | Timeline | Diffida, cure period e risoluzione |
| WF2-052 | Timeline | Decreto ingiuntivo, opposizione e provvisoria esecuzione |
| WF2-053 | Review | Monitoraggio dei dipendenti e informativa privacy |
| WF2-054 | Review | Clausole AML nel correspondent banking |
| WF2-055 | Dossier | Intermediari in una gara pubblica: indagine interna |
| WF2-056 | Dossier | Business interruption: copertura e nesso causale |
| WF2-057 | Review | Disciplinare di gara e schema di contratto |
| WF2-058 | Timeline | Composizione negoziata e misure protettive |
| WF2-059 | Dossier | Pagamenti non autorizzati e frode aziendale |
| WF2-060 | Timeline | Diniego di rimborso IVA e impugnazione |

### WF2-061–070

| ID | Famiglia | Caso |
|---|---|---|
| WF2-061 | Dossier | Outsourcing a catena e allocazione degli inadempimenti |
| WF2-062 | Review | Accordo transattivo e rinunce |
| WF2-063 | Timeline | Ransomware: notifiche coordinate e copertura |
| WF2-064 | Review | Polizza professional indemnity |
| WF2-065 | Dossier | Revoca di contributo pubblico |
| WF2-066 | Dossier | Pagamenti sospetti e azione revocatoria |
| WF2-067 | Timeline | Escussione delle garanzie ed enforcement |
| WF2-068 | Review | Tax covenant e indennizzo in una SPA |
| WF2-069 | Timeline | Controllo concentrazioni e closing |
| WF2-070 | Review | Accordo R&D e titolarità dei risultati |

### WF2-071–080

| ID | Famiglia | Caso |
|---|---|---|
| WF2-071 | Timeline | Arbitrato: domanda, tribunale e impugnazioni |
| WF2-072 | Timeline | Contestazione disciplinare e licenziamento |
| WF2-073 | Dossier | Indagine cross-border su terza parte e whistleblowing |
| WF2-074 | Timeline | Remediation 231 dopo acquisizione |
| WF2-075 | Review | Lavori pubblici: varianti e penali |
| WF2-076 | Dossier | Classi e voto nel piano di ristrutturazione |
| WF2-077 | Review | Amendment del finanziamento e security package |
| WF2-078 | Dossier | IVA e stabile organizzazione nel modello distributivo |
| WF2-079 | Timeline | Dawn raid e tutela del privilegio |
| WF2-080 | Review | Locazione commerciale e ripartizione dei rischi |

### WF2-081–090

| ID | Famiglia | Caso |
|---|---|---|
| WF2-081 | Review | Accordo di ristrutturazione e intercreditor |
| WF2-082 | Dossier | Derivati: adeguatezza informativa e quantificazione |
| WF2-083 | Timeline | Reclamo MiFID, ABF e azione civile |
| WF2-084 | Review | Transfer pricing policy e ruling package |
| WF2-085 | Dossier | Valutazione sostanziale di una concentrazione |
| WF2-086 | Review | Distribuzione online, MFN e restrizioni territoriali |
| WF2-087 | Timeline | Opposizione a domanda di marchio |
| WF2-088 | Dossier | Contraffazione di marchio e matrice probatoria |
| WF2-089 | Review | Contratto di sviluppo immobiliare |
| WF2-090 | Timeline | Rinnovo dell'autorizzazione ambientale e ricorso |

### WF2-091–100

| ID | Famiglia | Caso |
|---|---|---|
| WF2-091 | Review | Clean team e scambio informativo in una joint venture |
| WF2-092 | Dossier | Audit di conformità open source |
| WF2-093 | Timeline | Brevetto europeo: convalida, opposizione e tutela |
| WF2-094 | Dossier | Due diligence urbanistica su immobile commerciale |
| WF2-095 | Timeline | Morosità nella locazione e rilascio |
| WF2-096 | Timeline | Permesso di costruire e scadenze del cantiere |
| WF2-097 | Dossier | Rifiuti, emissioni e responsabilità nel sito produttivo |
| WF2-098 | Review | Garanzie ambientali in un asset deal |
| WF2-099 | Review | Accordo di bonifica e allocazione dei costi |
| WF2-100 | Timeline | Bonifica dopo il superamento delle CSC |

## 19. Regole per un LLM maintainer

Prima di modificare un caso:

1. leggi `task_spec.json`, l'intera busta pubblica e tutti i file privati del task;
2. esegui i validatori prima della modifica e conserva l'esito iniziale;
3. modifica per primi i file canonici, non il DOCX generato;
4. propaga ogni variazione a challenge map, gold, criteri, JSON, routing e test;
5. renderizza e ispeziona ogni Office modificato;
6. riesegui controlli locali e condivisi;
7. registra difetto, correzione, comando ed esito nel report di readiness;
8. non promuovere lo stato, scrivere su Notion o migrare nel corpus canonico senza mandato esplicito.

Non “correggere” un caso rendendo il validatore più permissivo. Se il test è sbagliato, dimostralo
con un esempio minimo; poi correggi test e dato mantenendo visibile la decisione.

## 20. File di riferimento

- `README.md`: stato operativo e comandi del corpus canonico WF2-001–100;
- `MIGRATION_WF2_031_100.md`: metodo, controlli ed esito della migrazione;
- `planning/WF2_031_100_MASTER_PLAN.md`: disegno dell'espansione a 100;
- `planning/WF2_031_100_MASTER_MATRIX.tsv`: anagrafica autoritativa WF2-031–100;
- `planning/COMMON_AUTHORING_CONTRACT.md`: regole comuni di authoring;
- `pilot/READINESS.md`: significato operativo di pilot readiness;
- `pilot/ERROR_TAXONOMY.md`: classificazione degli errori;
- `../docs/workflow2_agentic_pilot.md`: runtime agentico, smoke test e artefatti;
- `../docs/workflow2_pilot_readiness_matrix.md`: profili e capacità del bench;
- `../task_workflow2.0.1/`: sorgente storica pre-migrazione, esclusa dalle run;
- `../legalitaw/agentic/`: implementazione del runtime;
- `../legalitaw/cli/v2.py`: ingresso CLI (`legalitaw run`, `legalitaw score`).

Il manifest e i cento `task_spec.json` definiscono il corpus eseguibile. Matrici e sorgenti di
authoring spiegano come ci si è arrivati; non fanno parte della busta pubblica e non vanno usati per
costruire una submission.
