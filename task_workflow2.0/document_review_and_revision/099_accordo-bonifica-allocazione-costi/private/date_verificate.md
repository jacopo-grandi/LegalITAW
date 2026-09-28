# WF2-099 - Date e valori verificati

Prodotta da `source/gen/verifica_date_e_codici.py`, non a mano. Le festivita
nazionali italiane sono incluse nel calcolo tramite
`_tools/util_verifica_codici_e_date.py`.

**Data di riferimento:** 2026-12-09

| Milestone | Valore | Calcolo | Fonte |
|---|---|---|---|
| data di riferimento | 9 dicembre 2026 | mercoledì | public/01_task.md |
| costo base degli interventi concordati | 740.000 euro | somma delle undici voci del computo metrico allegato | 03_computo_metrico.md |
| alea contrattuale a carico del proponente | 111.000 euro | quindici per cento di 740.000 euro | 01_bozza_accordo_bonifica.docx, clausole 2.4 e 4.2 |
| esposizione massima entro l'alea | 851.000 euro | 740.000 più 111.000 uguale 851.000; oltre tale somma la clausola 4.3 pone l'eccedenza a carico della proprietaria | quadratura fra clausole 2.4 e 4.2 e 03_computo_metrico.md |
| esposizione della proprietaria nella bozza | non determinabile | la clausola 4.3 pone a carico della proprietaria l'intera eccedenza oltre 851.000 euro, senza alcun limite di importo e senza obbligo di comunicazione preventiva | 01_bozza_accordo_bonifica.docx, clausole 4.3 e 4.4 |
| approvazione del progetto operativo | 22 luglio 2026 | mercoledì | 02_decreto_regionale_approvazione_progetto.md |
| notifica del decreto di approvazione | 29 luglio 2026 | mercoledì | 02_decreto_regionale_approvazione_progetto.md, relata di notifica |
| termine per l'avvio dei lavori fissato dal decreto | 27 ottobre 2026 | novanta giorni dalla notifica del decreto; alla data di riferimento il termine è decorso da 43 giorni e i lavori non risultano avviati | 02_decreto_regionale_approvazione_progetto.md, punto 5 |
| derivazione errata: novanta giorni dalla data del decreto | 20 ottobre 2026 | il termine decorre dalla notifica e non dall'adozione del provvedimento | derivazione da escludere |
| termine di esecuzione fissato dal decreto | 27 aprile 2028 | diciotto mesi dal termine di avvio dei lavori | 02_decreto_regionale_approvazione_progetto.md, punto 4 |
| data prevista di sottoscrizione dell'accordo | 15 dicembre 2026 | martedì; indicata nella corrispondenza fra le parti | 05_email_della_proprietaria.md |
| avvio dei lavori secondo la clausola 5.1 della bozza | 13 febbraio 2027 | sessanta giorni dalla sottoscrizione; è posteriore di 109 giorni al termine fissato dal decreto, già decorso | 01_bozza_accordo_bonifica.docx, clausola 5.1 |
| cessazione della locazione | 30 giugno 2021 | data del verbale di restituzione, che contiene la riserva sullo stato del suolo | 04_contratto_di_locazione_cessato.md |

## Codici a struttura calcolata

Generati con l'algoritmo ufficiale e verificati sul carattere di controllo.

| Soggetto | Tipo | Valore |
|---|---|---|
| Cerinelli Chimica S.p.A. | partita IVA | `03617482058` |
| Vetrerie Malaspino S.p.A. | partita IVA | `07831256040` |
| Anfibia Ambiente S.r.l. | partita IVA | `08502736146` |

## Derivazioni errate escluse

Compaiono come criteri di assenza in sezione C: portano al risultato giusto per la
strada sbagliata, oppure a un risultato sbagliato per una strada intuitiva.

- computare il termine di avvio dei lavori dalla data del decreto anziché dalla data della sua notifica
- presentare la somma di costo base e alea come limite dell'esposizione della proprietaria, quando la clausola 4.3 pone a suo carico l'intera eccedenza
- quantificare l'esposizione residua della proprietaria in una cifra determinata, che il fascicolo non consente di ricavare
- assumere che il costo base dell'accordo coincida con il costo stimato su cui il decreto calcola le garanzie finanziarie in favore della regione
