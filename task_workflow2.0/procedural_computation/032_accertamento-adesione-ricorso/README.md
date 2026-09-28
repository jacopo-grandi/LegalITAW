# WF2-032 - Tributario. Audit dei termini fra accertamento, adesione, pagamento e ricorso

Caso del benchmark agentico LegalITA v2, lotto `batch_WF2-031_034`.

| | |
|---|---|
| Macroarea | C. Procedural computation |
| Workflow family / subtask | `procedural_computation` / `deadline_chain` |
| Verticale | tributario, contenzioso fiscale |
| Famiglia sul board | Procedural timeline |
| Deliverable | `audit_dei_termini.md`, massimo 1.800 parole |
| Data di riferimento | 16 settembre 2030, fascicolo in corso |
| Freeze normativo | 28 agosto 2026 |
| Documenti del fascicolo | 7 |
| Issue di merito | 13 |
| Controlled non-issue | 5 |
| Criteri atomici | 49 (12 a verifica meccanica, 37 al judge) |
| Stato | `draft_for_legal_validation` - non pilot-ready |

## Che cosa misura

Una societa' ha ricevuto un avviso di accertamento preceduto dallo schema di atto, ha chiesto
l'accertamento con adesione e il contraddittorio si e' chiuso senza accordo. All'amministratrice
serve sapere entro quando decidere, che cosa puo' ancora fare e che cosa succede al pagamento se
propone ricorso.

Il perno e' una regola speciale che ribalta quella generale: l'istanza di adesione sospende i termini
per novanta giorni nell'ipotesi ordinaria, ma per trenta quando l'avviso e' stato preceduto dallo
schema di atto e l'istanza e' presentata dopo la notifica. Quattro variabili indipendenti agiscono
sullo stesso termine - data di notificazione contro data dell'atto, durata della sospensione,
sospensione feriale, giorno della settimana della scadenza - e producono cinque date diverse e tutte
plausibili. Nessuna delle cinque derivazioni errate coincide con la data corretta: e' verificato con
script.

Il secondo asse e' la nota del consulente fiscale, che sbaglia sei volte e si contraddice una: il
modello che vi si appoggia perde l'intera catena.

## Struttura

```
public/                                  busta somministrata al modello
  01_task.md                             l'incarico
  02_reference_pack.md                   testo integrale delle fonti utilizzabili
  03_legal_sources.md                    elenco chiuso delle fonti, con freeze normativo
  response_template.md                   struttura obbligatoria del deliverable
  documents/                             7 documenti del fascicolo (.pdf, .docx, con sorgente .md)

private/                                 busta di valutazione
  evaluation_criteria.md                 rubrica in prosa, a livello di issue
  criteria_atomized.md                   rubrica atomizzata in forma leggibile
  rubric.json                            rubrica atomizzata in forma macchina
  runtime_routing.json                   instradamento verifica meccanica / judge
  review_notes.md                        note di revisione interna
  [collegamenti ai file di source/authoring con i nomi attesi da _tools/validate_case.py]

source/
  authoring/                             challenge map, gold, distrattore, date verificate,
                                         fonti chiuse, fonti documentali, scheda di validazione,
                                         script di verifica e di costruzione della rubrica
  gen/                                   generatori dei documenti del fascicolo

runs/                                    esiti delle esecuzioni
task_spec.json                           specifica del task
DECISION_LOG.md                          decisioni di impostazione e di merito
```

## Come rigenerare e verificare

```bash
cd batch_WF2-031_034/WF2-032_accertamento-adesione-ricorso

python3 source/gen/docs_a.py                    # documenti 01, 02, 03
python3 source/gen/docs_b.py                    # documenti 04, 05, 06
python3 source/gen/docs_c.py                    # documento 07
python3 source/authoring/verifica_wf2_032.py    # cronologia, termini, derivazioni errate, importi
python3 source/authoring/costruisci_rubrica_032.py
python3 ../../_tools/check_gold.py .
python3 ../../_tools/validate_case.py .
```

## Che cosa non e' ancora stato fatto

Il caso non e' `pilot_ready`. Mancano la validazione professionale sulle sei domande di
`source/authoring/legal_validation.md` - in particolare sulla durata della sospensione e sulla
riduzione delle sanzioni per omessa impugnazione - e la somministrazione del distrattore al judge.
