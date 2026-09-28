# WF2-033 - Scheda per la validazione professionale

Lettura blind: leggere prima la sola busta pubblica, registrare le proprie conclusioni, poi
confrontarle con `private/evaluation_criteria.md` e `source/authoring/gold_standard.md`.

## Dati del caso

| Campo | Valore |
|---|---|
| Workflow family | procedural_computation |
| Subtask | procedural_timeline |
| Verticale | assicurativo, rischi informatici |
| Data di riferimento | 8 agosto 2031, fascicolo in corso |
| Freeze normativo | 28 agosto 2026 |
| Committente | il direttore operativo dell'Assicurata |
| Deliverable | linea del tempo, quadro dei termini e checklist, massimo 1.900 parole |
| Issue di merito | 13 |
| Controlled non-issue | 6 |
| Criteri atomici | 50 (15 a verifica meccanica, 35 al judge) |

## Domande al validatore, in ordine di importanza

1. **Momento da cui decorre il termine di denuncia (I-01, I-02).** La polizza aggancia il termine
   alla Scoperta, definita come il momento in cui il responsabile dei sistemi informativi viene a
   conoscenza di fatti che indicano l'Evento. Confermare che la denuncia sia tempestiva e che la
   tesi del broker, che computa dal primo accesso non autorizzato, sia infondata.

2. **Decorrenza del periodo di attesa (I-04).** La definizione di polizza lo fa decorrere dall'inizio
   dell'Interruzione di Attivita'. Confermare che sia questa la lettura corretta e che i quaranta
   minuti che separano l'inizio dell'interruzione dalla Scoperta non siano opinabili.

3. **Inapplicabilita' della sospensione feriale (I-07).** Confermare che la sospensione dei termini
   nel periodo feriale non si applichi a un termine contrattuale di denuncia del sinistro e che il
   criterio B.10 possa vietarne l'applicazione senza ulteriori distinzioni. Il reference pack non
   contiene la disciplina sulla sospensione feriale: la sua estraneita' e' cio' che il modello deve
   riconoscere.

4. **Condizione sui Fornitori Autorizzati e spese di resistenza (I-08, I-09).** La polizza subordina
   l'indennizzabilita' delle spese legali alla scelta di un fornitore in elenco o al consenso scritto
   dell'Assicuratore. **Il reference pack contiene l'art. 1917, comma 3, e l'art. 1932 del codice
   civile: se il validatore ritiene che la clausola costituisca deroga in senso meno favorevole
   all'assicurato, la conseguenza sarebbe la sostituzione di diritto e il caso andrebbe riscritto su
   questo punto.** Il caso non risolve la questione: chiede al modello di rilevare che la condizione
   non e' soddisfatta e di indicare come azione la richiesta del consenso, e con il campo
   `Indifferente` del criterio B.14 non premia ne' penalizza la discussione sulla derogabilita'.
   Confermare che questa impostazione sia sostenibile.

5. **Esclusione delle sanzioni amministrative (I-10).** Confermare che una clausola che escluda le
   sanzioni amministrative pecuniarie, comprese quelle irrogate a terzi e le somme dovute a titolo di
   rivalsa, sia valida e che l'esposizione riferibile alla copertura vada calcolata al netto di
   quella voce.

6. **Realismo della polizza.** Le condizioni sono verosimili per un prodotto cyber di mercato
   italiano? Il periodo di attesa di dodici ore, il massimo di trenta giorni per l'interruzione, il
   sublimite per l'estorsione e la struttura a tre Sezioni sono assetti plausibili?

## Punti dichiarati e non risolti

- **Comunicazione agli interessati.** Il fascicolo non dice se sia stata effettuata: la notifica
  all'autorita' riporta che era in corso di valutazione. Nessun criterio la premia o la penalizza. Se
  il validatore ritiene che una linea del tempo debba occuparsene, va aggiunto un documento e un
  issue dedicato.
- **Qualificazione della pretesa del terzo.** Il caso non chiede di valutarne la fondatezza e nessun
  criterio la misura.
- **Regime della Sezione B.** La Richiesta e' stata presentata durante il periodo di assicurazione e
  l'Evento e' successivo alla Data di Retroattivita': la garanzia opera senza che occorra alcuna
  ulteriore verifica. Il caso non usa il regime claims made come trappola, per non ripetere la leva
  del caso assicurativo esistente sul corpus.

## Nota del costruttore

Il corpus contiene gia' un caso assicurativo in regime claims made su polizza per la responsabilita'
degli amministratori. La distanza e' costruita su tre assi: il workflow, che qui e' una linea del
tempo e non il calcolo di un singolo termine; la forma del deliverable; le leve, integralmente
diverse. In particolare non sono riusate: il periodo di osservazione per mancato rinnovo,
l'esclusione assicurato contro assicurato, la permanenza della qualita' di assicurato dopo la
cessazione dalla carica, la franchigia operante su una sola copertura, il divieto di transigere, la
prescrizione biennale, il contenuto e la forma della denuncia. La decadenza per denuncia tardiva, che
e' la leva di un caso gia' presente sul board, compare qui in senso opposto: e' un controlled
non-issue, perche' la denuncia e' tempestiva e affermarne la tardivita' e' l'errore.
