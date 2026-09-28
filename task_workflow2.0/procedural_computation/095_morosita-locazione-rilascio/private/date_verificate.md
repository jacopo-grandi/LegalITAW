# WF2-095 - Date e valori verificati

Prodotta da `source/gen/verifica_date_e_codici.py`, non a mano. Le festivita
nazionali italiane sono incluse nel calcolo tramite
`_tools/util_verifica_codici_e_date.py`.

**Data di riferimento:** 2026-08-06

| Milestone | Valore | Calcolo | Fonte |
|---|---|---|---|
| data di riferimento | 6 agosto 2026 | giovedì; anteriore di 14 giorni all'udienza di comparizione | public/01_task.md |
| canone mensile pattuito | 3.150,00 euro | 37.800,00 euro annui in dodici rate anticipate | 01_contratto_locazione.md, art. 4.1 |
| canoni scaduti e intimati | 12.600,00 euro | quattro mensilità da 3.150,00 euro, scadute il 5 aprile, il 5 maggio, il 5 giugno e il 5 luglio 2026 | 03_intimazione_sfratto.md e 05_estratto_partitario.csv |
| oneri accessori intimati | 486,00 euro | esercizio 2025, richiesti il 14 aprile 2026 con il rendiconto approvato il 28 marzo 2026 | 05_estratto_partitario.csv |
| totale intimato | 13.086,00 euro | 12.600,00 + 486,00 = 13.086,00 | 03_intimazione_sfratto.md, punto 12 |
| partite aperte alla data di estrazione del partitario | 16.236,00 euro | cinque mensilità da 3.150,00 euro, compresa quella di agosto 2026 scaduta dopo l'atto, più 486,00 euro di oneri accessori; non è l'importo intimato | 05_estratto_partitario.csv |
| quota di oneri accessori contestata dalla conduttrice | 214,00 euro | quota per il servizio di portierato, istituito con delibera del 28 marzo 2026 e attivato dal 1 maggio 2026, addebitata sull'esercizio 2025 | 06_email_conduttrice.md |
| somma non controversa | 12.872,00 euro | 12.600,00 euro di canoni non contestati più 272,00 euro di oneri accessori residui dopo lo stralcio della quota di portierato | 06_email_conduttrice.md e 05_estratto_partitario.csv |
| confronto fra oneri non pagati e due mensilità di canone | 486,00 euro contro 6.300,00 euro | la soglia richiamata dalla clausola 6.2 non è raggiunta | 01_contratto_locazione.md, art. 6.2 |
| canone annuo e soglia di derogabilità | 37.800,00 euro contro 250.000,00 euro | il canone annuo è inferiore alla soglia oltre la quale le parti possono concordare termini e condizioni in deroga alle disposizioni di legge | 01_contratto_locazione.md, art. 4.1 |
| notificazione dell'intimazione | 30 luglio 2026 | giovedì; consegna a mani di addetta alla ricezione, non in mani proprie del legale rappresentante | 04_relazione_di_notificazione.md |
| udienza di comparizione fissata | 20 agosto 2026 | giovedì | 03_intimazione_sfratto.md, punto 15 |
| giorni liberi fra notificazione e udienza | venti giorni liberi | si escludono il giorno della notificazione e il giorno dell'udienza: dal 31 luglio al 19 agosto 2026 compresi sono venti giorni, pari al minimo di legge | art. 660, comma 4, del codice di procedura civile |
| esito del computo del termine di comparizione | termine rispettato | nessuna abbreviazione risulta richiesta né autorizzata con decreto motivato | art. 660, comma 4, del codice di procedura civile |
| derivazione errata con sospensione feriale applicata | 21 settembre 2026 | venti giorni liberi computati dal 1 settembre 2026; la sospensione feriale non si applica alle cause di sfratto | derivazione da escludere |
| termine massimo per il pagamento della somma non controversa | venti giorni dall'ordinanza | alla data di riferimento l'ordinanza non è stata emessa e la scadenza non è determinabile | art. 666 del codice di procedura civile |
| termine massimo di grazia in sede giudiziale | novanta giorni | con rinvio dell'udienza a non oltre dieci giorni dalla scadenza; l'applicabilità alle locazioni ad uso diverso non è risolta dal testo di legge | art. 55, commi 2 e 3, della legge sulle locazioni |

## Codici a struttura calcolata

Generati con l'algoritmo ufficiale e verificati sul carattere di controllo.

| Soggetto | Tipo | Valore |
|---|---|---|
| Sartiglia Immobiliare S.r.l. | partita IVA | `07452189033` |
| Vernasca Ottica S.r.l. | partita IVA | `04227915602` |
| Sartiglia Immobiliare S.r.l. | IBAN | `IT08N0312712800000000451207` |

## Derivazioni errate escluse

Compaiono come criteri di assenza in sezione C: portano al risultato giusto per la
strada sbagliata, oppure a un risultato sbagliato per una strada intuitiva.

- computare il termine di comparizione applicando la sospensione feriale, ottenendo che la prima udienza utile sarebbe il 21 settembre 2026
- computare i venti giorni includendo il giorno della notificazione o quello dell'udienza, e concludere che il termine è di diciotto o diciannove giorni
- usare come importo della morosità le partite aperte del partitario alla data di estrazione, pari a 16.236,00 euro, anziché l'importo intimato
