# WF2-034 - Date, soglie e coerenza verificate

Prodotto da `source/authoring/verifica_wf2_034.py`; l'output integrale dell'ultima esecuzione e' in
`source/authoring/_output_verifica.txt`.

## Date

| Evento | Data | Giorno | Fonte |
|---|---|---|---|
| Approvazione del codice etico | 21/06/2029 | giovedi | documento 03 |
| Entrata in vigore della procedura sulle segnalazioni | 01/02/2024 | giovedi | documento 04 |
| Versione 3 della bozza di policy | 28/10/2032 | giovedi | documento 01 |
| Seduta del comitato controllo e rischi | 05/11/2032 | venerdi | documento 05 |
| Messaggio del direttore commerciale | 10/11/2032 | mercoledi | documento 06 |
| Data di riferimento del fascicolo | 12/11/2032 | venerdi | prompt |
| Consiglio di amministrazione previsto | 03/12/2032 | venerdi | documento 05 |
| Entrata in vigore prevista della policy | 01/01/2033 | sabato | documento 01, art. 15.1 |

Fra la data di riferimento e il consiglio corrono **21 giorni**: il fascicolo e' ex ante e la review
e' utilizzabile.

## Soglie e parametri della bozza

| Parametro | Valore nella bozza | Clausola | Rilievo |
|---|---|---|---|
| Omaggio a soggetto privato, limite per singola erogazione | euro 150,00 | art. 5.2 | la misura non e' un rilievo (N-02) |
| Omaggio a soggetto privato, limite cumulativo annuo per destinatario | non previsto | art. 5.2 | I-01 |
| Omaggio a pubblico ufficiale, definizione di modico valore | non prevista | artt. 3 e 5.3 | I-03 |
| Ospitalita', limite per pasto | euro 250,00 | art. 6.1 | nessuno |
| Ospitalita', limite per evento e per destinatario | euro 1.000,00 | art. 6.1 | nessuno sul limite; I-10 sull'autorizzazione |
| Sponsorizzazione, soglia della verifica sul beneficiario | euro 25.000,00 | art. 7.3 | I-06 |
| Intermediari, limite al compenso | cinque per cento | art. 9.3 | presidio, non rilievo (N-07) |
| Regolarizzazione successiva in caso di urgenza | trenta giorni | art. 10.2 | I-11 |
| Formazione | cadenza biennale con verifica | art. 12 | presidio, non rilievo (N-03) |
| Conservazione della documentazione | dieci anni | art. 14 | presidio, non rilievo (N-05) |

## Effetto del frazionamento, verificato con script

| Grandezza | Valore |
|---|---:|
| Numero di omaggi allo stesso destinatario nello stesso anno | 4 |
| Valore unitario di ciascun omaggio | 140,00 |
| Ciascun omaggio resta sotto il limite dell'articolo 5.2 | si' |
| Totale annuo per destinatario | 560,00 |
| Autorizzazioni richieste dalla bozza | nessuna |

Una sponsorizzazione di euro 24.000,00 resta sotto la soglia dell'articolo 7.3 e non attiva alcuna
verifica sul beneficiario.

## Conflitti fra la bozza e i documenti in vigore

| Tema | Documento in vigore | Bozza | Esito |
|---|---|---|---|
| Omaggi a pubblici ufficiali | codice etico, art. 4: divieto assoluto, senza eccezioni | art. 5.3: ammessi se di modico valore | conflitto: la bozza deroga a un divieto assoluto contenuto in un documento approvato dallo stesso organo |
| Canale di segnalazione | procedura sulle segnalazioni, artt. 3 e 4: canale gestito da un ufficio autonomo dedicato, riservatezza dell'identita' garantita anche verso i superiori gerarchici | art. 11.1: segnalazione al superiore gerarchico, identita' trasmessa al responsabile di funzione | conflitto: la bozza sostituisce un canale conforme con uno che non garantisce la riservatezza |
| Ambito soggettivo | codice etico, art. 2: dipendenti, amministratori, sindaci, consulenti, agenti, distributori, fornitori e partner | art. 2: soli dipendenti | conflitto: la bozza restringe l'ambito rispetto al documento sovraordinato |

Verificato con script che i conflitti sono tre e che ciascuno ha un criterio dedicato.

## Codici a struttura calcolata

| Codice | Valore | Verifica |
|---|---|---|
| P.IVA Ilcinara Automazione S.p.A. | 01864290133 | cifra di controllo valida |

## Coerenza relativa dei valori

- La soglia dell'ospitalita' autorizzata dal proponente (euro 1.000,00) e quella della
  sponsorizzazione autorizzata dal direttore commerciale (euro 25.000,00) sono **le due righe della
  matrice in cui proponente e autorizzante coincidono**: il difetto non e' isolato e va nominato su
  entrambe.
- La soglia della verifica sul beneficiario coincide con la soglia dell'autorizzazione della
  sponsorizzazione: **sotto i venticinquemila euro non c'e' ne' verifica ne' autorizzazione
  indipendente**. E' la relazione che rende grave il rilievo I-06.
- Il valore unitario del frazionamento (euro 140,00) e' **appena sotto** il limite: l'esempio e'
  realistico e non forzato.
- Il periodo che separa la data di riferimento dal consiglio (**21 giorni**) e' sufficiente a
  intervenire sul testo: il caso non chiede di scegliere fra approvare e rinviare.
