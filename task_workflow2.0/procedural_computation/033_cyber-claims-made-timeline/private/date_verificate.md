# WF2-033 - Cronologia, termini e valori verificati

Prodotto da `source/authoring/verifica_wf2_033.py`; l'output integrale dell'ultima esecuzione e' in
`source/authoring/_output_verifica.txt`. Nessun valore di questa tabella e' stato calcolato a mano.

## Cronologia (fuso Europa/Roma)

| Momento | Data e ora | Giorno | Fonte |
|---|---|---|---|
| Primo accesso non autorizzato | 12/03/2031 ore 21:15 | mercoledi | documento 03 |
| Inizio dell'Interruzione di Attivita' | 14/03/2031 ore 05:40 | venerdi | documento 03 |
| SCOPERTA dell'Evento | 14/03/2031 ore 06:20 | venerdi | documento 03; documento 05 |
| Richiesta estorsiva | 14/03/2031 ore 15:30 | venerdi | documento 03 |
| Notifica all'autorita' di controllo | 16/03/2031 ore 11:05 | domenica | documento 04 |
| Denuncia all'Assicuratore | 16/03/2031 ore 15:42 | domenica | documento 05 |
| Fine dell'Interruzione di Attivita' | 16/03/2031 ore 19:10 | domenica | documento 03 |
| Data della lettera del terzo | 21/07/2031 | lunedi | documento 06 |
| RICEZIONE della richiesta del terzo | 23/07/2031 ore 09:14 | mercoledi | documento 06 |
| Incarico allo studio legale | 28/07/2031 | lunedi | documento 07 |
| Richiesta di documentazione dell'Assicuratore | 30/07/2031 | mercoledi | documento 08 |
| Messaggio del direttore operativo | 06/08/2031 | mercoledi | documento 09 |
| Data di riferimento del fascicolo | 08/08/2031 | venerdi | prompt |

## Termini

| Termine | Regola | Scadenza | Stato all'08/08/2031 | Margine |
|---|---|---|---|---|
| Denuncia dell'Evento | 72 ore dalla Scoperta | 17/03/2031 ore 06:20 | rispettato | 14 ore e 38 minuti |
| Notifica all'autorita' di controllo | 72 ore dalla conoscenza | 17/03/2031 ore 06:20 | rispettato | 19 ore e 15 minuti |
| Denuncia della Richiesta di Risarcimento | 30 giorni dalla ricezione | 22/08/2031 (venerdi) | aperto | 14 giorni |
| Consegna della documentazione | 15 giorni dalla richiesta | 14/08/2031 (giovedi) | aperto | 6 giorni |

Il termine di denuncia dell'Evento e quello di notifica all'autorita' coincidono perche' entrambi
decorrono dallo stesso momento: le ore 06:20 del 14 marzo 2031.

## Interruzione di attivita' e periodo di attesa

| Grandezza | Valore | Calcolo |
|---|---|---|
| Durata complessiva dell'interruzione | 61 ore e 30 minuti | dalle 05:40 del 14/03 alle 19:10 del 16/03 |
| Periodo di attesa | 12 ore | scheda di polizza |
| Inizio del periodo indennizzabile | 14/03/2031 ore 17:40 | inizio dell'interruzione piu' 12 ore |
| Durata indennizzabile | 49 ore e 30 minuti | dalle 17:40 del 14/03 alle 19:10 del 16/03 |
| Massimo indennizzabile previsto dalla polizza | 30 giorni consecutivi | la durata e' ampiamente inferiore |

## Derivazioni errate presidiate da criteri `assenza`

| Derivazione errata | Risultato | Criterio |
|---|---|---|
| 72 ore dal primo accesso non autorizzato | scadenza 15/03/2031 ore 21:15: la denuncia risulterebbe tardiva | C.3 |
| periodo di attesa computato dalla Scoperta | inizio dell'indennizzo alle 18:20 del 14/03, durata 48 ore e 50 minuti | C.5 |
| nessun periodo di attesa | durata indennizzabile 61 ore e 30 minuti | B.7 |
| 30 giorni dalla data della lettera del terzo | 20/08/2031 | C.9 |
| sospensione feriale applicata al termine contrattuale | 22/09/2031 | C.10 |

Verificato con script che nessuna delle derivazioni errate coincide con il risultato corretto.

## Importi

| Voce | Importo (euro) | Fonte |
|---|---:|---|
| Massimale Sezione A | 3.000.000,00 | documento 02 |
| Massimale Sezione B | 2.000.000,00 | documento 02 |
| Massimale Sezione C | 500.000,00 | documento 02 |
| Sublimite per l'estorsione informatica | 250.000,00 | documento 02 |
| Franchigia per Evento, cumulativa sulle tre Sezioni | 50.000,00 | documento 02 |
| Limite delle spese di resistenza | 500.000,00 | un quarto del massimale di Sezione B |
| Costi di negoziazione dell'estorsione sostenuti | 96.000,00 | documento 09 |
| Richiesta del terzo, totale | 1.450.000,00 | documento 06 |
| di cui voce esclusa per sanzioni amministrative | 320.000,00 | documento 06; documento 01, art. 6 |
| Richiesta riferibile alla copertura | 1.130.000,00 | 1.450.000 - 320.000 |
| Compenso pattuito con lo studio legale, fase stragiudiziale | 120.000,00 | documento 07 |
| di cui acconto gia' versato | 40.000,00 | documento 07; documento 09 |

Le cinque voci della richiesta del terzo sommano esattamente 1.450.000,00.

## Codici a struttura calcolata

| Codice | Valore | Verifica |
|---|---|---|
| P.IVA Casaltino Retail S.p.A. | 03182640122 | cifra di controllo valida |
| P.IVA Perlasca Assicurazioni S.p.A. | 07529130150 | cifra di controllo valida |
| P.IVA Quintilia Marketplace S.r.l. | 04981720131 | cifra di controllo valida |
| IBAN Casaltino Retail S.p.A. | IT98Z0538711200000042719305 | carattere di controllo valido |

## Coerenza relativa dei valori

- Fra l'inizio dell'interruzione e la Scoperta corrono **quaranta minuti**: abbastanza pochi da
  rendere naturale confonderli, abbastanza da spostare di quaranta minuti l'inizio del periodo
  indennizzabile.
- Il margine della denuncia sul termine e' di **circa quindici ore**: la denuncia e' tempestiva senza
  che il fatto sia evidente, e diventa tardiva se si sposta il momento iniziale.
- Il sublimite per l'estorsione e' **piu' del doppio** dei costi sostenuti: l'incapienza e'
  deliberatamente assente.
- La richiesta del terzo e' **inferiore al massimale** di Sezione B anche al lordo della voce
  esclusa: il problema di incapienza del massimale e' deliberatamente assente.
- La durata indennizzabile e' **ampiamente inferiore** al massimo di trenta giorni: il limite
  temporale non morde ed e' un ulteriore elemento che non va segnalato come problema.
