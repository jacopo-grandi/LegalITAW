# Audit della terna di giudici WF2 — 26 settembre 2026

Run giudicata: `results/agentic/v2-scores/luna-wf2-100-paired/20260926-080533-030797`, risposte di gpt-5.6-luna.
Perimetro: 65 task in cui la terna ha funzionato davvero (WF2-001…066 senza WF2-020), 3.300 criteri.
Giudici: Jev (A), Luna (B), Opus 5.5 (C, arbitro).

## Metodo

- 176 casi rivisti a mano alla cieca, senza vedere i voti dei giudici. Ogni revisore aveva il criterio, la risposta, i documenti del fascicolo e il gold standard.
- Campione 1 (104 casi, mirato ai punti deboli): 44 disaccordi Jev/Luna, stratificati per tipo di criterio; tutti i 15 accordi smentiti dall'audit di Opus; tutti i 21 FAIL decisi dal controllo sulle citazioni; 12 PASS confermati da quel controllo; 12 accordi unanimi A=B=C.
- Campione 2 (72 casi, casuale): accordi Jev=Luna che non sono passati da Opus. Sono il 68% di tutti i verdetti.
- I revisori erano agenti Claude, cioè la stessa famiglia di Opus. Questo può gonfiare l'accordo con Opus. Per una conferma indipendente conviene far vedere 15-20 casi al team legale.

## Risultati

| Gruppo | Casi | Verdetto finale giusto | Jev | Luna | Opus |
|---|---|---|---|---|---|
| Accordi non ricontrollati (casuale) | 72 | 68 (94%) | = | = | — |
| Disaccordi Jev/Luna | 44 | 39 (89%) | 30 | 14 | 39 |
| Accordi smentiti dall'audit | 15 | 3 | 3 | 3 | 12 |
| Controllo citazioni, FAIL di Opus | 21 | 20 | 1 | 1 | 20 |
| Controllo citazioni, PASS di Opus | 12 | 12 | 12 | 12 | 12 |
| Accordi unanimi A=B=C | 12 | 10 | 10 | 10 | 10 |

Stima pesata su 3.300 criteri: circa il 94% dei verdetti finali è corretto, cioè circa 200 sbagliati.
L'intervallo plausibile è 91-97%. Gli errori vanno in entrambe le direzioni (nel campione 1: 10 PASS sbagliati e 10 FAIL sbagliati), quindi lo score complessivo dovrebbe essere spostato di non più di 1-2 punti.

Gli errori stanno quasi tutti nei criteri scritti in modo ambiguo: 12 dei 24 errori sono su criteri che il revisore ha segnato come ambigui. Sui criteri chiari giudicati con sicurezza alta gli errori sono 3 su 97.

Nel campione casuale i criteri segnati come ambigui sono il 14% (10 su 72).

## Famiglie di criteri da sistemare (conteggi sulle 5.032 voci)

1. **Rinvio a un'etichetta del gold** ("la conclusione I-01 è attribuita al doc. …"): 138 criteri in WF2-041…050. Il giudice non vede il gold, quindi non sa quale conclusione cercare. Spiega perché i criteri di attribuzione hanno il tasso di disaccordo più alto (20%).
2. **Formula letterale** ("compare «…»", "compare una fra …"): 361 criteri. Non è chiaro se valga una parafrasi.
3. **"Il deliverable richiede [azione]"**: 96 criteri. Resta incerto il caso in cui il modello esegue l'azione invece di chiederla.
4. **Criteri senza condizioni PASS/FAIL** (vecchio formato): 136 criteri.
5. **Casi scoperti**: PASS e FAIL non coprono la risposta che non affronta il punto (casi visti in WF2-001, 003, 006, 049).
6. **"Ogni data / ogni importo ha la fonte"**: 17 criteri. Non è chiaro se valga anche per date calcolate e date di riferimento.
7. **Incoerenze puntuali**: il criterio parla della nota ma il campo deliverable indica la redline (WF2-053 B.27, B.37); tipo "assenza" con logica required_presence (WF2-019 A.2, B.4a).

Da controllare in modo deterministico: la presenza di revisioni tracciate. In WF2-001 A.2 tutti e tre i giudici hanno dato PASS a una redline fatta con barrati e senza vere revisioni tracciate.

## Controllo sulle citazioni

Nel campione 1 ha deciso 33 casi e Opus ne ha azzeccati 32. Sull'intera run corregge circa 20 PASS sbagliati su 3.300 criteri (0,6%) e costa circa il 40% della spesa di Opus.

## File

`audit_terna_176_casi.json` (casi uniti ai voti dei giudici). I casi ciechi e i verdetti grezzi dei revisori restano nel repository di authoring.
