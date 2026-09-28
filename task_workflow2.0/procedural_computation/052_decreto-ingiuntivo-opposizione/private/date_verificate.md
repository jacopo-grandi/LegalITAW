# WF2-052 - Date e valori verificati

Prodotti da `_build/verifica_termini.py`, non a mano.
Data di riferimento: 2031-06-18.

## Date

| Milestone | Data | Giorno | Calcolo | Fonte |
|---|---|---|---|---|
| emissione del decreto ingiuntivo | 2031-05-12 | lunedi | intestazione del decreto | doc. 01 |
| notifica del decreto e del ricorso | 2031-05-20 | martedi | relata di notifica a mezzo PEC | doc. 02 |
| scadenza del termine per proporre opposizione (40 giorni) | 2031-06-30 | lunedi | 20 maggio + 40 giorni, dies a quo escluso | art. 641, co. 1 c.p.c. |
| notificazione dell'opposizione programmata dalla bozza | 2031-06-25 | mercoledi | bozza di citazione in opposizione | doc. 03 |
| prima udienza indicata nella bozza di citazione | 2031-10-20 | lunedi | bozza di citazione in opposizione | doc. 03 |
| termine per la costituzione dell'opponente (10 gg dalla notificazione) | 2031-07-07 | lunedi | notificazione programmata + 10 giorni | art. 165 c.p.c. |
| termine per la costituzione dell'opposto (70 gg prima dell'udienza) | 2031-08-11 | lunedi | udienza indicata meno 70 giorni | art. 166 c.p.c. |
| prima memoria integrativa (40 gg prima dell'udienza) | 2031-09-10 | mercoledi | udienza indicata meno 40 giorni | art. 171-ter, n. 1 c.p.c. |
| seconda memoria integrativa (20 gg prima dell'udienza) | 2031-09-30 | martedi | udienza indicata meno 20 giorni | art. 171-ter, n. 2 c.p.c. |
| terza memoria integrativa (10 gg prima dell'udienza) | 2031-10-10 | venerdi | udienza indicata meno 10 giorni | art. 171-ter, n. 3 c.p.c. |
| data di riferimento | 2031-06-18 | mercoledi | fissata dall'incarico | prompt |

## Proroghe applicate

- scadenza del termine per proporre opposizione (40 giorni): scadenza nominale 2031-06-29 (domenica), prorogata al primo giorno non festivo (regime processuale)
- termine per la costituzione dell'opponente (10 gg dalla notificazione): scadenza nominale 2031-07-05 (sabato), prorogata al primo giorno non festivo (regime processuale)

## Valori controllati

| Grandezza | Valore | Fonte |
|---|---|---|
| importo ingiunto in linea capitale, interessi e penale | euro 486.700,00 | decreto |
| fatture portate in ingiunzione | euro 420.000,00 | estratto delle partite |
| note di credito non contabilizzate | euro 84.000,00 | doc. 05 |
| acconti versati e non imputati | euro 60.000,00 | estratto delle partite |
| capitale non contestato | euro 276.000,00 | 420.000 - 84.000 - 60.000 |
| penale contestata | euro 42.000,00 | estratto delle partite |
| interessi conteggiati | euro 24.700,00 | estratto delle partite |
| importo contestabile in linea capitale sulla base dei documenti | euro 144.000,00 | 84.000 di note di credito piu' 60.000 di acconti |
| importo complessivamente contestabile | euro 210.700,00 | 144.000 di capitale piu' 42.000 di penale piu' 24.700 di interessi |
| importo effettivamente contestato dalla bozza di citazione | euro 126.000,00 | 84.000 di note di credito piu' 42.000 di penale |
| scostamento fra contestabile e contestato | euro 84.700,00 | 60.000 di acconti piu' 24.700 di interessi |
| giorni liberi fra notificazione programmata e udienza indicata | 116 | 25 giugno 2031 -> 20 ottobre 2031, esclusi entrambi gli estremi |
| termine minimo a comparire per notificazione in Italia | 120 giorni liberi | art. 163-bis, co. 1 c.p.c. |

## Codici a struttura calcolata

Generati con l'algoritmo ufficiale da `_build/anagrafica.py` e verificati
con il carattere di controllo.

| Soggetto | Codice |
|---|---|
| Teleria Monteluce S.r.l. | P.IVA 73000004116 |
| Teleria Monteluce S.r.l. | IBAN IT06P0392816604400000002973 |
| Polimeri Brancora S.p.A. | P.IVA 73000005485 |
| Polimeri Brancora S.p.A. | IBAN IT94W0517512280400000003964 |
| Studio Legale Ombrivalle | P.IVA 74000033766 |
| Studio Legale Ombrivalle | IBAN IT77T0621411970500000012368 |
| Silvio Terlizzone | C.F. TRLSLV74S03A944W |
