# WF2-033 - Assicurativo. Linea del tempo della copertura e della denuncia su polizza rischi informatici

Caso del benchmark agentico LegalITA v2, lotto `batch_WF2-031_034`.

| | |
|---|---|
| Macroarea | C. Procedural computation |
| Workflow family / subtask | `procedural_computation` / `procedural_timeline` |
| Verticale | assicurativo, rischi informatici |
| Famiglia sul board | Procedural timeline |
| Deliverable | `timeline_copertura_denuncia.md`, massimo 1.900 parole |
| Data di riferimento | 8 agosto 2031, fascicolo in corso |
| Freeze normativo | 28 agosto 2026 |
| Documenti del fascicolo | 9 |
| Issue di merito | 13 |
| Controlled non-issue | 6 |
| Criteri atomici | 50 (15 a verifica meccanica, 35 al judge) |
| Stato | `draft_for_legal_validation` - non pilot-ready |

## Che cosa misura

Una societa' di commercio elettronico ha subito un attacco informatico a marzo, lo ha denunciato alla
compagnia, ha notificato la violazione all'autorita' di controllo e a luglio ha ricevuto una richiesta
di risarcimento da un partner commerciale. Al direttore operativo serve la linea del tempo, il quadro
dei termini e la checklist di quello che va fatto ed entro quando.

Il fascicolo offre quattro istanti diversi per lo stesso incidente - primo accesso non autorizzato,
inizio dell'interruzione, scoperta, ripristino - e ogni termine e ogni durata decorre da uno soltanto
di essi. Quaranta minuti separano l'inizio dell'interruzione dalla scoperta, e da quei quaranta minuti
dipendono l'inizio del periodo indennizzabile e la durata dell'indennizzo. I termini sono a ore e a
giorni insieme: il caso misura anche il non applicare a un termine contrattuale in giorni le regole
dei termini processuali.

Il secondo asse e' la disciplina nel non trasformare ogni limite di polizza in un rilievo. Massimale,
sublimite, durata massima, retroattivita' e scadenza sono tutti capienti e ciascuno ha un criterio che
ne vieta la segnalazione. La sola condizione che non e' soddisfatta riguarda il professionista
incaricato dell'assistenza legale.

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
  authoring/                             challenge map, gold, distrattore, cronologia verificata,
                                         fonti chiuse, fonti documentali, scheda di validazione,
                                         script di verifica e di costruzione della rubrica
  gen/                                   generatori dei documenti del fascicolo

runs/                                    esiti delle esecuzioni
task_spec.json                           specifica del task
DECISION_LOG.md                          decisioni di impostazione e di merito
```

## Come rigenerare e verificare

```bash
cd batch_WF2-031_034/WF2-033_cyber-claims-made-timeline

python3 source/gen/docs_a.py                    # documenti 01, 02
python3 source/gen/docs_b.py                    # documenti 03, 04, 05
python3 source/gen/docs_c.py                    # documenti 06, 07, 08
python3 source/gen/docs_d.py                    # documento 09
python3 source/authoring/verifica_wf2_033.py    # cronologia, termini, durate, importi, codici
python3 source/authoring/costruisci_rubrica_033.py
python3 ../../_tools/check_gold.py .
python3 ../../_tools/validate_case.py .
```

## Che cosa non e' ancora stato fatto

Il caso non e' `pilot_ready`. Mancano la validazione professionale sulle sei domande di
`source/authoring/legal_validation.md` - in particolare sulla condizione relativa ai Fornitori
Autorizzati alla luce delle norme inderogabili in materia di assicurazione - e la somministrazione
del distrattore al judge.
