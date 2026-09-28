# Audit dello scoring output-free — Workflow 2.0

## Decisione

Il contratto ufficiale di esecuzione è `prompt_only_free_artifacts_v1`.
Il sistema valutato riceve soltanto il prompt, i documenti pubblici e, nelle run
interne, il protocollo tecnico neutrale necessario a usare il workspace. Nomi,
numero e struttura degli artifact non sono imposti dall'harness.

Tutti i 5.032 criteri sono sottoposti al judge. I 97 artifact check ereditati
dai profili WF2-001–020 restano inventariati come diagnostica
`diagnostic_only_not_applied`, senza sostituire il verdetto semantico.
Ogni risultato dichiara inoltre
`criterion_routing_contract: all_criteria_semantic_judge_v1`, così da non
confonderlo con gli score diagnostici precedenti.

## Motivo

I 97 check interessano 19 task e si dividono in:

- 64 regex di presenza;
- 10 verifiche di caratteristiche DOCX;
- 23 verifiche di heading, blocchi, etichette o allowlist.

Le verifiche strutturali codificano spesso la vecchia impaginazione suggerita
dall'harness. Le regex, anche quando cercano un valore corretto, non sempre
verificano il ruolo attribuito al valore. Alcuni criteri di assenza, per
esempio, erano implementati cercando soltanto la presenza della data corretta e
non l'assenza delle alternative vietate.

Applicarli a una consegna libera produrrebbe quindi falsi negativi per
intestazioni o sintassi diverse e possibili falsi positivi per valori presenti
nel contesto sbagliato.

## Regola del judge

Il prompt e i documenti pubblici sono l'unica fonte dei requisiti di output.
Quando il testo legacy di un criterio menziona un nome di file, un'estensione,
un'intestazione, un'etichetta o una sintassi più restrittivi, il judge non deve
penalizzare il mero scostamento formale. Deve verificare se la sostanza richiesta
pubblicamente è presente, corretta e utilizzabile.

I requisiti formali esplicitamente presenti nel prompt restano invece
vincolanti: per esempio una tabella richiesta dall'utente, una redline, due file
distinti o una struttura richiamata tramite `response_template.md`.

## Compatibilità

Gli score prodotti prima di questo contratto restano diagnostici e non sono
confrontabili direttamente con lo score output-free. Il vecchio comportamento
deterministico rimane invariato per il corpus legacy `tasks_agentic_workflow/`;
la modifica è limitata ai task Workflow 2.0 marcati con il nuovo contratto.

Una futura riattivazione di fast path deterministici richiederà una versione
successiva del contratto, controlli semanticamente equivalenti e una
calibrazione contro verdetti umani su output eterogenei.
