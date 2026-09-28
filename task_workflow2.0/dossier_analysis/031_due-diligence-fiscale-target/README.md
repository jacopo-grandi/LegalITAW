# WF2-031 - Fiscale. Dossier dei red flag su una target in acquisizione

Caso del benchmark agentico LegalITA v2, lotto `batch_WF2-031_034`.

| | |
|---|---|
| Macroarea | B. Dossier analysis |
| Workflow family / subtask | `dossier_analysis` / `due_diligence_memo` |
| Verticale | fiscale, due diligence tributaria |
| Famiglia sul board | Dossier analysis |
| Deliverable | `red_flag_fiscali.md`, matrice dei red flag fiscali, massimo 2.200 parole |
| Data di riferimento | 9 marzo 2028, fascicolo in corso |
| Freeze normativo | 28 agosto 2026 |
| Documenti del fascicolo | 9 |
| Issue di merito | 15 |
| Controlled non-issue | 6 |
| Criteri atomici | 67 (21 a verifica meccanica, 46 al judge) |
| Stato | `draft_for_legal_validation` - non pilot-ready |

## Che cosa misura

Un'acquisizione del cento per cento delle quote di una societa' manifatturiera. All'acquirente serve
il dossier dei red flag fiscali, con l'esposizione stimata di ciascuno, il documento da cui deriva e
il grado di copertura offerto dalla bozza di contratto. Il caso misura tre direzioni dell'errore
tenute separate: l'omissione di rilievi che nessun documento nomina come tali, la
sovra-quantificazione di rilievi che valgono meno di quanto sembrano, e la sovra-segnalazione di sei
elementi che hanno l'aspetto del rilievo e non lo sono.

Il meccanismo portante e' la catena a tre passaggi sul riporto delle perdite fiscali dopo il cambio
di controllo: ogni scorciatoia produce un numero plausibile e diverso, e ognuno di quei numeri e'
presidiato da un criterio che lo vieta per nome.

## Struttura

```
public/                                  busta somministrata al modello
  01_task.md                             l'incarico
  02_reference_pack.md                   testo integrale delle fonti utilizzabili
  03_legal_sources.md                    elenco chiuso delle fonti, con freeze normativo
  response_template.md                   struttura obbligatoria del deliverable
  documents/                             9 documenti del fascicolo (.pdf, .docx, con sorgente .md)

private/                                 busta di valutazione
  evaluation_criteria.md                 rubrica in prosa, a livello di issue
  criteria_atomized.md                   rubrica atomizzata in forma leggibile
  rubric.json                            rubrica atomizzata in forma macchina
  runtime_routing.json                   instradamento verifica meccanica / judge
  review_notes.md                        note di revisione interna
  [collegamenti ai file di source/authoring con i nomi attesi da _tools/validate_case.py]

source/
  authoring/                             materiale di costruzione
    challenge_map.json                   issue, controlled non-issue, meccanismi, punti neutri
    gold_standard.md                     cio' che una buona risposta deve riconoscere
    distractor.md                        versione sbagliata e criteri che devono fallire
    date_e_valori_verificati.md          tabella prodotta dallo script di verifica
    fonti_chiuse.json                    elenco chiuso in forma macchina
    fonti_documentali.md                 modelli reali seguiti per ciascun documento
    legal_validation.md                  scheda per la validazione professionale
    verifica_wf2_031.py                  script di verifica di date, importi, soglie e codici
    costruisci_rubrica_031.py            genera rubric.json, criteria_atomized.md, runtime_routing.json
  gen/                                   generatori dei documenti del fascicolo

runs/                                    esiti delle esecuzioni
task_spec.json                           specifica del task
DECISION_LOG.md                          decisioni di impostazione e di merito
```

## Come rigenerare e verificare

```bash
cd batch_WF2-031_034/WF2-031_due-diligence-fiscale-target

python3 source/gen/docs_a.py                    # documenti 01, 07, 08
python3 source/gen/docs_b.py                    # documenti 02, 03
python3 source/gen/docs_c.py                    # documenti 04, 06
python3 source/gen/docs_d.py                    # documenti 05, 09
python3 source/authoring/verifica_wf2_031.py    # date, importi, soglie, codici
python3 source/authoring/costruisci_rubrica_031.py
python3 ../../_tools/check_gold.py .
python3 ../../_tools/validate_case.py .
```

Gli script di `source/gen/` sono deterministici: rieseguirli riscrive i documenti identici.

## Che cosa non e' ancora stato fatto

Il caso non e' `pilot_ready`. Mancano la validazione professionale sulle sei domande di
`source/authoring/legal_validation.md`, la somministrazione del distrattore al judge e la decisione
sulla macro-area del board, che oggi non ha un'opzione fiscale.
