# WF2-031 - Scheda per la validazione professionale

Lettura blind: leggere prima la sola busta pubblica, registrare le proprie conclusioni, poi
confrontarle con `private/evaluation_criteria.md` e `source/authoring/gold_standard.md`.

## Dati del caso

| Campo | Valore |
|---|---|
| Workflow family | dossier_analysis |
| Subtask | due_diligence_memo |
| Verticale | fiscale / due diligence tributaria |
| Data di riferimento | 9 marzo 2028, fascicolo in corso |
| Freeze normativo | 28 agosto 2026 |
| Committente | la responsabile sviluppo dell'acquirente |
| Lato assistito | l'acquirente dell'intera partecipazione |
| Deliverable | dossier dei red flag fiscali in forma di matrice, massimo 2.200 parole |
| Issue di merito | 15 |
| Controlled non-issue | 6 |
| Criteri atomici | 67 (21 a verifica meccanica, 46 al judge) |

## Domande al validatore, in ordine di importanza

1. **Catena dell'art. 84 TUIR (I-07, I-08, I-09).** E' il cuore del caso. Confermare: (a) che
   l'acquisizione di un ramo d'azienda da parte della societa' che riporta le perdite integri la
   modifica dell'attivita' principale ai sensi del comma 3, anche quando l'attivita' produttiva
   prosegue immutata; (b) che la finestra di rilevanza comprenda il periodo d'imposta 2026 rispetto
   a un trasferimento che si perfeziona nel 2028; (c) che la data di riferimento delle perdite sia
   il 31 dicembre 2027, poiche' il trasferimento cade nella prima meta' del periodo d'imposta 2028;
   (d) che in assenza di relazione giurata di stima il tetto del comma 3-ter sia il patrimonio netto
   contabile ridotto dei versamenti degli ultimi ventiquattro mesi, e non del loro doppio.

2. **Grandezze del test di vitalita' (I-08).** Confermare che le grandezze da confrontare siano i
   ricavi e proventi della gestione caratteristica e le sole spese per prestazioni di lavoro
   subordinato e relativi contributi, cioe' le lettere a) e b) della voce B.9 dello schema di conto
   economico, e che il confronto vada fatto con il quaranta per cento della media dei due esercizi
   anteriori alla data di riferimento delle perdite. Il caso e' costruito in modo che l'inclusione
   delle lettere c) ed e) non muti l'esito: confermare che il punto possa restare neutro.

3. **Limite delle spese di rappresentanza (I-06).** Il limite dell'art. 108, comma 2, TUIR e'
   commisurato ai ricavi e proventi della gestione caratteristica "risultanti dalla dichiarazione dei
   redditi relativa allo stesso periodo". Il fascicolo non contiene la dichiarazione: il calcolo e'
   fondato sui ricavi del conto economico. Confermare che sia la base corretta per un lavoro di due
   diligence e che il criterio possa esigere l'importo di euro 132.000,00.

4. **Rilievo di competenza (I-03).** Confermare che l'esposizione economica di un rilievo di
   competenza, in una due diligence, vada rappresentata come limitata a sanzioni e interessi, e non
   come maggiore imposta definitiva, e che il criterio B.5 possa vietare l'inserimento di euro
   81.600,00 nella colonna dell'esposizione.

5. **Responsabilita' solidale sul ramo d'azienda (I-11).** Confermare che l'art. 14 d.lgs. 472/1997
   colpisca la societa' quale cessionaria del ramo nel 2026 e non l'acquirente delle quote nel 2028,
   e che la garanzia contrattuale rilasciata dalla cedente nell'atto notarile abbia effetto solo nei
   rapporti interni.

6. **Marca temporale (I-12).** Confermare che l'apposizione della marca temporale dopo la
   presentazione della dichiarazione faccia venire meno la disapplicazione della sanzione per il
   periodo d'imposta interessato, e che la comunicazione del possesso, regolarmente effettuata, non
   sani il difetto.

## Punti dichiarati e non risolti

- **Quantificazione delle sanzioni.** Il caso non chiede e non premia il calcolo delle sanzioni sui
  rilievi del processo verbale. La scelta e' deliberata: la misura applicabile dipende dal regime
  vigente al momento in cui la violazione e' stata commessa e la ricostruzione del regime previgente
  non e' stata verificata con il grado di certezza richiesto dal progetto. Nessun criterio la premia
  e nessuno la penalizza; il gold la tratta come non quantificabile dal fascicolo. **Se il validatore
  ritiene che una due diligence debba quantificarla, il caso va integrato con la disposizione
  sanzionatoria nel reference pack e con criteri dedicati.**
- **Importi della comunicazione di irregolarita'.** Imposta, sanzioni e interessi indicati nel
  documento 07 sono coerenti fra loro ma nessun criterio ne dipende: la comunicazione e' un
  controlled non-issue e rileva solo per essere stata pagata.
- **Macro-area del board.** Il board non ha oggi un'opzione fiscale. Il caso e' mappato su
  Corporate / M&A e Compliance & Regulatory; la mappatura corretta e' registrata nel `task_spec.json`
  come `board_macro_area_proposta`. Decisione rimessa a chi governa il board.

## Nota del costruttore

Il caso non riusa alcuna leva dei casi esistenti. Rispetto a WF2-026, che e' l'altro
`due_diligence_memo` del corpus, variano il verticale, i meccanismi e la forma del deliverable
(matrice con esposizione stimata invece che red-flag report per gravita'). Rispetto a WF2-022, che e'
l'altro caso M&A su dossier, variano il workflow e il lato assistito.
