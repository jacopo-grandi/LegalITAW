# Controlli deterministici sui criteri Workflow 2.0

> **Snapshot precedente al ritiro dei template.** I conteggi 5.081/5.178 qui sotto
> descrivono il corpus prima della migrazione del 21 settembre 2026. Il corpus
> eseguibile corrente contiene 5.032 criteri; si veda
> [`RESPONSE_TEMPLATE_RETIREMENT_2026-09-21.md`](RESPONSE_TEMPLATE_RETIREMENT_2026-09-21.md).

## Perche'

Prima di questo lavoro 5.081 criteri su 5.178 passavano dal judge LLM. Le
classi `span`, `scansione`, `esatta` e `judge` in `runtime_routing.json` non
sono esecutori diversi: sono varianti dello stesso prompt allo stesso modello
(`legalitaw/agentic/models.py`, `normalized_match_criteria`). Solo
`evaluation_mode == "deterministic"` salta l'LLM, e copriva 97 criteri
scritti a mano in `TASK_PROFILES`.

Alcuni criteri non sono materia da giudizio: un limite di parole e' un
conteggio, non una valutazione. Farli decidere a un LLM costa e sbaglia.

## Come

Tre pezzi, tutti a sola libreria standard. Sono strumenti di authoring e restano nel repository legal-ITA; in LegalITA-W arrivano solo i `deterministic_checks.json` dei task e l'overlay che li applica:

| file | ruolo |
|---|---|
| `scripts/value_patterns.py` | riconosce il tipo di un valore citato in un criterio (data, importo, durata, percentuale, file, norma) e genera la regex che ne copre le forme di superficie equivalenti |
| `scripts/build_deterministic_checks.py` | genera `<task>/private/deterministic_checks.json` con le proposte |
| `scripts/shadow_deterministic_checks.py` | esegue le proposte su run gia' giudicate e le confronta col judge, senza toccare il runtime |

`legalitaw/agentic/deterministic_overlay.py` applica al task caricato le sole
proposte con `status: "validated"`. Le altre restano inerti nel file.

```
python3 scripts/build_deterministic_checks.py --write
python3 scripts/shadow_deterministic_checks.py --report tmp/shadow.json
```

## Le due modalita', e perche'

**`decisive`** — il controllo esaurisce il criterio, verdetto autoritativo in
entrambe le direzioni. Oggi solo `max_words`.

**`necessary`** — condizione necessaria ma non sufficiente. Un controllo
letterale puo' provare l'ASSENZA di un valore (se la cifra non compare da
nessuna parte, nessun criterio che la richiede puo' passare) ma non la sua
corretta ATTRIBUZIONE. Nel corpus ricorrono risposte che riportano il valore
giusto riferito alla cosa sbagliata:

> WF2-052 B.2 — "La risposta indica il 20 maggio 2031 come data della
> notificazione, ma individua il 21 maggio come decorrenza del termine"

Per questo i controlli su valore non sono autoritativi in direzione PASS. Il
motore non ha ancora un gate solo-FAIL: sono generati e validati ma non
collegati.

## Cosa NON e' riducibile a un controllo

- **Criteri di assenza / divieto** (`prohibited_presence`): la logica si
  inverte, un controllo letterale ingenuo li romperebbe. Esclusi dal round 1.
- **Token che sono parafrasi, non valori.** Molte `pass_condition` elencano
  formulazioni a titolo di esempio (`«resta impugnabile»`, `«non trova
  riscontro»`): non sono una allowlist esaustiva. Una prima versione le
  trattava alla lettera e produceva 253 falsi FAIL. `value_patterns` accetta
  solo token che hanno la forma di un valore.
- **Decimali arrotondati.** Il criterio cita `22,4`, la risposta calcola
  `22,3988`. Il confronto letterale non rappresenta l'arrotondamento: esclusi.

## Stato

| | |
|---|---|
| proposte totali | 185 su 42 task |
| `decisive` validate e attive | 8 |
| `decisive` bloccate | 2 (limite complessivo su piu' deliverable: il motore conta un artifact per volta) |
| `necessary` in attesa del gate solo-FAIL | 175 |
| criteri deterministici nel corpus | 97 -> 105 |

Accordo col judge in shadow su 169 criteri `necessary`: 91,7%.

## Errori del judge emersi

Lo shadow non serve solo a validare i controlli: misura il judge.

**Conteggio parole.** Su 5 criteri A.2 verificabili, il judge ha sbagliato 4
volte, sempre dichiarando superato un limite rispettato:

| task | limite | parole reali | judge |
|---|---|---|---|
| WF2-045 | 2.300 | 1.947 | "supera il limite; ampiamente piu' lunga" |
| WF2-048 | 2.400 | 1.740 | "supera il limite" |
| WF2-047 | 3.000 | 2.906 | "supera il limite" |
| WF2-049 | 3.800 | 2.844 | "supera verosimilmente" |
| WF2-043 | 3.800 | 3.855 | "supera verosimilmente" (corretto) |

Il lessico ("verosimilmente", "ampiamente") mostra che il modello stima
invece di contare. Sono criteri di gravita' alta: ogni falso FAIL azzera
`all_pass` per quel task.

**Evidenza inventata.** Due falsi PASS con citazione inesistente, confermati
in modo indipendente da `evidence_status`:

- WF2-052 B.8 — judge: "Il tempo residuo e' indicato in dodici giorni".
  Ne' "dodici" ne' "12 giorni" compaiono nella submission. `evidence_status:
  invalid`.
- WF2-098 C.7 — judge: "Non viene quantificato il costo annuo di 43.000
  euro". Verdetto: PASS. `evidence_status: not_found`.

## Prossimi passi

1. Gate solo-FAIL nel motore, per attivare i 175 controlli `necessary`.
2. `max_words` sommato su piu' deliverable, per sbloccare le 2 proposte ferme.
3. Estendere ai criteri di assenza con una logica dedicata.
4. Normalizzare il formato di `criteria_atomized.md` (sei varianti sui 100
   file): senza, il flag `judge: no` non e' incrociabile con il routing.
