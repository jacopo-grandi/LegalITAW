# WF2-031 - Date, importi e soglie verificati

Prodotto da `source/authoring/verifica_wf2_031.py`; l'output integrale dell'ultima esecuzione e' in
`source/authoring/_output_verifica.txt`. Festivita' nazionali italiane incluse nel controllo. Nessun
valore di questa tabella e' stato calcolato a mano.

## Date

| Milestone | Data | Giorno | Calcolo | Fonte |
|---|---|---|---|---|
| Inizio delle operazioni di verifica | 09/02/2027 (2027-02-09) | martedi | - | documento 01 |
| Chiusura delle operazioni di verifica | 14/05/2027 (2027-05-14) | venerdi | - | documento 01 |
| Consegna del processo verbale di constatazione | 17/05/2027 (2027-05-17) | lunedi | - | documento 01 |
| Scadenza per le osservazioni al verbale | 16/07/2027 (2027-07-16) | venerdi | 60 giorni dalla consegna, giorno iniziale non computato; non prorogata | documento 01 |
| Acquisto del ramo d'azienda | 03/07/2026 (2026-07-03) | venerdi | - | documento 04 |
| Versamento dei soci in conto capitale | 18/09/2026 (2026-09-18) | venerdi | - | documento 03 |
| Comunicazione di irregolarita' | 21/06/2027 (2027-06-21) | lunedi | - | documento 07 |
| Quietanza del modello F24 | 15/07/2027 (2027-07-15) | giovedi | entro trenta giorni dalla comunicazione | documento 08 |
| Presentazione della dichiarazione 2026 | 29/10/2027 (2027-10-29) | venerdi | - | documento 09 |
| Marca temporale della Documentazione Nazionale | 12/11/2027 (2027-11-12) | venerdi | 14 giorni DOPO la presentazione: la disapplicazione non opera | documento 06 |
| Chiusura dell'esercizio di riferimento delle perdite | 31/12/2027 (2027-12-31) | venerdi | periodo precedente al trasferimento, che cade nella prima meta' del 2028 | documento 02 |
| Data di riferimento del fascicolo | 09/03/2028 (2028-03-09) | giovedi | - | prompt |
| Data di Esecuzione prevista | 28/04/2028 (2028-04-28) | venerdi | - | documento 05 |
| Scadenza della garanzia fiscale | 28/04/2030 (2030-04-28) | domenica | ventiquattro mesi dalla Data di Esecuzione | documento 05, art. 9.4 |

## Termini di decadenza (art. 43 d.P.R. 600/1973)

| Periodo d'imposta | Anno di presentazione | Termine di decadenza | Stato al 09/03/2028 | Coperto dalla garanzia |
|---|---|---|---|---|
| 2021 | 2022 | 31/12/2027 | DECADUTO | - |
| 2022 | 2023 | 31/12/2028 | aperto | si' |
| 2023 | 2024 | 31/12/2029 | aperto | si' |
| 2024 | 2025 | 31/12/2030 | aperto | NO |
| 2025 | 2026 | 31/12/2031 | aperto | NO |
| 2026 | 2027 | 31/12/2032 | aperto | NO |
| 2027 | 2028 | 31/12/2033 | aperto | NO |

Derivazione errata presidiata dal criterio C.6: computo dall'anno del periodo d'imposta anziche'
dall'anno di presentazione, che porterebbe al 31/12/2027 per il periodo 2022.

## Importi

| Voce | Importo (euro) | Calcolo | Fonte |
|---|---:|---|---|
| Rilievo n. 1 - imponibile 2021 | 210.000,00 | - | documento 01 |
| Rilievo n. 1 - maggiore IRES | 50.400,00 | 24% di 210.000,00 | art. 77 TUIR |
| Rilievo n. 2 - imponibile 2022 | 340.000,00 | - | documento 01 |
| Rilievo n. 2 - maggiore IRES | 81.600,00 | 24% di 340.000,00 | art. 77 TUIR |
| Rilievo n. 3 - imponibile 2023 | 620.000,00 | - | documento 01 |
| Rilievo n. 3 - maggiore IRES | 148.800,00 | 24% di 620.000,00 | art. 77 TUIR |
| Rilievo n. 4 - maggiore IVA 2023 | 136.400,00 | 22% di 620.000,00 | documento 01 |
| Totale maggiori imposte constatate | 417.200,00 | somma dei quattro rilievi | documento 01 |
| Ricavi 2026 | 8.800.000,00 | - | documento 03 |
| Limite spese di rappresentanza 2026 | 132.000,00 | 1,5% di 8.800.000,00 (ricavi sotto i 10 milioni) | art. 108, comma 2, TUIR |
| Spese di rappresentanza 2026 | 312.000,00 | - | documento 03 |
| Eccedenza indeducibile 2026 | 180.000,00 | 312.000,00 - 132.000,00 | art. 108, comma 2, TUIR |
| Maggiore IRES 2026 | 43.200,00 | 24% di 180.000,00 | art. 77 TUIR |
| Esposizione in imposta rilevante | 328.400,00 | 148.800,00 + 136.400,00 + 43.200,00 | build |
| Fondo per imposte 2027 | 150.000,00 | - | documento 02 |
| Scoperto del fondo | 178.400,00 | 328.400,00 - 150.000,00 | build |
| Prezzo | 6.200.000,00 | - | documento 05 |
| Limite massimo di indennizzo fiscale | 930.000,00 | 15% di 6.200.000,00 | documento 05, art. 9.6 |
| Importo indennizzabile al netto dell'accantonamento | 178.400,00 | 328.400,00 - 150.000,00 | documento 05, art. 9.5 |
| Valore del ramo d'azienda | 1.150.000,00 | corrispettivo pattuito | documento 04, art. 5 |

## Riporto delle perdite (art. 84 TUIR)

| Passaggio | Valore | Calcolo | Fonte |
|---|---:|---|---|
| Periodo d'imposta del trasferimento | 2028 | esecuzione il 28/04/2028 | documento 05 |
| Finestra di rilevanza della modifica di attivita' | 2026-2030 | periodo del trasferimento, due anteriori e due successivi | art. 84, comma 3 |
| Acquisizione del ramo d'azienda | 2026 | dentro la finestra | documento 04 |
| Ricavi 2025 | 9.200.000,00 | - | documento 03 |
| Ricavi 2026 | 8.800.000,00 | - | documento 03 |
| Media dei ricavi dei due esercizi anteriori | 9.000.000,00 | (8.800.000 + 9.200.000) / 2 | art. 84, comma 3-bis |
| Soglia dei ricavi | 3.600.000,00 | 40% di 9.000.000,00 | art. 84, comma 3-bis |
| Ricavi 2027 | 3.780.000,00 | soglia SUPERATA di 180.000,00 | documento 02 |
| Spese di lavoro subordinato 2025 (B.9 a + b) | 2.400.000,00 | 1.820.000 + 580.000 | documento 03 |
| Spese di lavoro subordinato 2026 (B.9 a + b) | 2.200.000,00 | 1.670.000 + 530.000 | documento 03 |
| Media delle spese di lavoro dei due esercizi anteriori | 2.300.000,00 | (2.200.000 + 2.400.000) / 2 | art. 84, comma 3-bis |
| Soglia delle spese di lavoro | 920.000,00 | 40% di 2.300.000,00 | art. 84, comma 3-bis |
| Spese di lavoro subordinato 2027 (B.9 a + b) | 1.010.000,00 | 772.000 + 238.000; soglia SUPERATA di 90.000,00 | documento 02 |
| Perdite fiscali al 31/12/2027 | 3.420.000,00 | - | documento 02 |
| Patrimonio netto contabile al 31/12/2027 | 1.310.000,00 | - | documento 02 |
| Versamenti dei soci negli ultimi ventiquattro mesi | 420.000,00 | versamento del 18/09/2026 | documento 03 |
| Tetto al riporto | 890.000,00 | 1.310.000,00 - 420.000,00 | art. 84, comma 3-ter |
| Perdite non riportabili | 2.530.000,00 | 3.420.000,00 - 890.000,00 | build |
| Mancato beneficio IRES | 607.200,00 | 24% di 2.530.000,00 | build |

Derivazioni errate presidiate dai criteri C.10, C.14, C.15, C.18, C.19 e C.20:

| Derivazione errata | Risultato | Criterio |
|---|---:|---|
| IRES sull'intero importo delle spese di rappresentanza | 74.880,00 | C.10 |
| confronto con la media anziche' con il 40% della media | test non superato | C.14 |
| media calcolata sugli esercizi 2027 e 2026 | 6.290.000,00 | C.15 |
| patrimonio netto senza deduzione dei versamenti | 1.310.000,00 | C.18 |
| patrimonio netto meno il doppio dei versamenti | 470.000,00 | C.19 |
| perdite integralmente riportabili | 3.420.000,00 | C.20 |

## Codici a struttura calcolata

| Codice | Valore | Verifica |
|---|---|---|
| P.IVA Miralbeno Componenti S.r.l. | 03672940164 | cifra di controllo valida |
| P.IVA Anselvieri Partecipazioni S.p.A. | 04128850171 | cifra di controllo valida |
| P.IVA Orbilene Ricambi S.r.l. | 02983710365 | cifra di controllo valida |
| C.F. Ludovico Trescanti | TRSLVC58D22F257D | algoritmo ufficiale; Belfiore F257 = Modena |
| C.F. Marta Ferronio | FRRMRT66S43F257X | algoritmo ufficiale; Belfiore F257 = Modena |

## Coerenza relativa dei valori

- Il fondo per imposte (150.000,00) e' **inferiore** all'esposizione (328.400,00): la trappola di
  capienza morde.
- Il limite massimo di indennizzo (930.000,00) e' **superiore** all'esposizione: l'incapienza del
  limite e' deliberatamente assente ed e' il controlled non-issue N-04.
- Il test sulle grandezze di conto economico passa con margine stretto su entrambe le grandezze
  (5,0 per cento sui ricavi, 9,8 per cento sulle spese di lavoro): un errore di metodo cambia
  l'esito, un errore di arrotondamento no.
- La scadenza della garanzia fiscale (28/04/2030) cade **fra** il termine di decadenza del 2023
  (31/12/2029) e quello del 2024 (31/12/2030): il confine fra periodi coperti e scoperti e' netto.
- La marca temporale della Documentazione Nazionale cade **quattordici giorni dopo** la
  presentazione della dichiarazione: lo scarto e' abbastanza breve da non essere evidente e
  abbastanza netto da non essere opinabile.
