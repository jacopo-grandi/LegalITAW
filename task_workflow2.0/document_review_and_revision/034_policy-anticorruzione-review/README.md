# WF2-034 - Compliance. Review della bozza di policy anticorruzione

Caso del benchmark agentico LegalITA v2, lotto `batch_WF2-031_034`.

| | |
|---|---|
| Macroarea | A. Document review and revision |
| Workflow family / subtask | `document_review_and_revision` / `review_only` |
| Verticale | compliance e anticorruzione |
| Famiglia sul board | Review and redline |
| Deliverable | `nota_di_review.md`, nota di rilievi ordinata per priorita', senza riscrittura, massimo 2.000 parole |
| Data di riferimento | 12 novembre 2032, fascicolo ex ante |
| Freeze normativo | 28 agosto 2026 |
| Documenti del fascicolo | 6 |
| Issue di merito | 16 |
| Controlled non-issue | 7 |
| Criteri atomici | 47 (10 a verifica meccanica, 37 al judge) |
| Stato | `draft_for_legal_validation` - non pilot-ready |

## Che cosa misura

Una societa' industriale sta per adottare una policy anticorruzione su omaggi, ospitalita',
sponsorizzazioni, intermediari e autorizzazioni interne. Il comitato controllo e rischi ha chiesto una
review esterna prima della delibera del consiglio, in forma di nota di rilievi ordinata per priorita'
e senza riscrittura del testo.

La bozza contiene tutti i capitoli che una policy anticorruzione deve avere, redatti in modo
plausibile: chi cerca il capitolo mancante non trova nulla. I difetti stanno nel livello dei presidi,
nelle definizioni assenti e in tre eccezioni che svuotano la regola. Tre rilievi non si vedono
leggendo la bozza: emergono solo dal confronto con il codice etico e con la procedura sulle
segnalazioni, entrambi in vigore. Sette clausole hanno l'aspetto del rilievo e non lo sono, e due
criteri vietano espressamente di segnalare la misura di una soglia al posto della struttura che la
rende aggirabile.

Il messaggio del direttore commerciale e' la variante piu' difficile della dichiarazione di parte:
non contiene errori di fatto, chiede di conservare due dei difetti piu' gravi e chiude con una
minaccia sul budget.

## Struttura

```
public/                                  busta somministrata al modello
  01_task.md                             l'incarico
  02_reference_pack.md                   testo integrale delle fonti utilizzabili
  03_legal_sources.md                    elenco chiuso delle fonti, con freeze normativo
  response_template.md                   struttura obbligatoria del deliverable
  documents/                             6 documenti del fascicolo (.docx, .pdf, con sorgente .md)

private/                                 busta di valutazione
  evaluation_criteria.md                 rubrica in prosa, a livello di issue
  criteria_atomized.md                   rubrica atomizzata in forma leggibile
  rubric.json                            rubrica atomizzata in forma macchina
  runtime_routing.json                   instradamento verifica meccanica / judge
  review_notes.md                        note di revisione interna
  [collegamenti ai file di source/authoring con i nomi attesi da _tools/validate_case.py]

source/
  authoring/                             challenge map, gold, distrattore, valori verificati,
                                         fonti chiuse, fonti documentali, scheda di validazione,
                                         script di verifica e di costruzione della rubrica
  gen/                                   generatori dei documenti del fascicolo

runs/                                    esiti delle esecuzioni
task_spec.json                           specifica del task
DECISION_LOG.md                          decisioni di impostazione e di merito
```

## Come rigenerare e verificare

```bash
cd batch_WF2-031_034/WF2-034_policy-anticorruzione-review

python3 source/gen/docs_a.py                    # documenti 01, 02
python3 source/gen/docs_b.py                    # documenti 03, 04, 05
python3 source/gen/docs_c.py                    # documento 06
python3 source/authoring/verifica_wf2_034.py    # date, soglie, frazionamento, conflitti, codici
python3 source/authoring/costruisci_rubrica_034.py
python3 ../../_tools/check_gold.py .
python3 ../../_tools/validate_case.py .
```

## Che cosa non e' ancora stato fatto

Il caso non e' `pilot_ready`. Mancano la validazione professionale sulle sei domande di
`source/authoring/legal_validation.md` - in particolare sulla collocazione dei rilievi bloccanti e
sulla prevalenza del codice etico sulla policy - e la somministrazione del distrattore al judge.
