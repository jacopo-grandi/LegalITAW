# WF2-035 — Note di revisione interna

Registro dei bivi di costruzione, delle scelte discrezionali e delle fragilità note. Non è materiale
somministrato: serve a chi rilegge il caso prima del freeze.

## Ordine di lavoro effettivamente seguito

1. Lettura di `procedura_nuovo_caso.md` e `metodo_e_convenzioni.md` (fonte autoritativa del Progetto) e
   dei precedenti WF2-021 e WF2-027…WF2-030.
2. Verifica delle fonti primarie in rete, prima di qualunque scelta di merito: artt. 18, 35, 36, 90, 93
   e 220 d.lgs. 36/2023; artt. 45, 119, 120 e 122 c.p.a.; una pronuncia sul dies a quo. Nessuna norma è
   stata citata a memoria.
3. Challenge map (`source/authoring/challenge_map.json`), scritta **prima** dei documenti.
4. Ricerca degli esemplari reali per ciascun tipo di documento
   (`source/authoring/fonti_documentali.md`).
5. Fissazione del calendario con ricerca esaustiva su script, non a mano: vedi sotto.
6. Redazione dei dieci documenti (`source/gen/`), con generazione simultanea di .md e .pdf dalla
   stessa sorgente.
7. Rubrica in prosa a livello di issue (`private/evaluation_criteria.md`), **poi** rubrica atomizzata
   (`private/rubric.json` e `private/criteria_atomized.md`), generata da sorgente unica.
8. Gold standard e distrattore; verifica del gold contro la propria rubrica.

## Come è stato scelto il calendario

Le date non sono state scelte a mano. È stata eseguita una ricerca esaustiva sulle date candidate con
questi vincoli simultanei, tutti verificati da script:

- nessun termine del caso cade in sabato, in domenica o in giorno festivo nazionale (se un termine
  fosse prorogabile, i criteri di tipo `assenza` sulle derivazioni errate diventerebbero ambigui);
- nessuna delle tre derivazioni errate cade in sabato, in domenica o in festivo, per la stessa ragione:
  un modello che sbaglia il dies a quo e poi proroga la data sfuggirebbe al criterio;
- tutti i termini e tutte le derivazioni errate hanno valori-data distinti fra loro;
- il termine dell'art. 36, comma 4, è già scaduto alla data di riferimento; i due termini per il
  ricorso sono pendenti;
- il termine per il ricorso principale scade **prima** del termine dilatorio, perché la notificazione
  della domanda cautelare sia ancora utile a impedire la stipulazione;
- la comunicazione ex art. 90 è inviata entro cinque giorni dall'adozione della determina;
- la nomina della commissione è anteriore alla scadenza del termine di presentazione delle offerte;
- nessuna data, nessun nome, nessun importo e nessun codice collide con quelli usati nei casi esistenti
  del repository, compresi i batch WF2-031…WF2-034 e WF2-038…WF2-040.

Le combinazioni valide erano cinque; è stata scelta quella che non attraversa il periodo natalizio e
non richiede di discutere la sospensione feriale dei termini.

## Scelte discrezionali

1. **Il termine di trenta giorni non è dimezzato: quanto peso dargli.** È il punto in cui il caso
   distingue di più fra un modello che conosce il rito e uno che applica una regola generale. Ha due
   criteri di segno opposto (B.8 positivo, B.9 negativo) e non un criterio omnibus.
2. **La frase sui trenta giorni per ricorrere è stata rimossa dalla comunicazione di aggiudicazione.**
   Negli esemplari reali c'è. Toglierla costa realismo ma è imposto dal divieto di scrivere nel
   documento la regola che l'agente deve dedurre. Resta l'indicazione dell'organo competente, che è la
   formula degli avvisi di esito. È la sola divergenza deliberata dai modelli reali e va segnalata al
   validatore.
3. **La scadenza del termine dilatorio è indicata nella comunicazione.** Non è una concessione: l'art.
   90, comma 2, impone alla stazione appaltante di indicarla. Il discriminante non è quindi il calcolo
   della data ma il non contraddirla applicando trentacinque giorni, come fa la nota interna. Per questo
   l'issue I-08 ha un criterio sul numero di giorni (B.14), uno sul divieto (B.15) e uno sul valore-data
   (C.7).
4. **Nel documento 09 il legale rappresentante del cliente scrive che la comunicazione è stata
   «ricevuta in piattaforma nella medesima data».** È un'affermazione di parte che coincide con la
   risposta corretta, e in questo senso è un piccolo aiuto. È stata mantenuta perché è ciò che scriverebbe
   davvero un'istanza di accesso redatta il 28 ottobre, e perché entra in tensione con la nota interna
   che colloca la conoscenza al 26 ottobre: la tensione fra i due documenti di parte è essa stessa un
   fatto distribuito. Se in calibrazione risultasse troppo indulgente, la frase va sostituita con
   «ricevuta in piattaforma».
5. **Le due censure sono nominate dal cliente nella nota interna.** Il caso misura la costruzione della
   timeline, non l'individuazione dei vizi: chiedere entrambe le cose avrebbe reso il caso ibrido e i
   criteri non atomici. Il modello deve allocare le censure ai termini, non giudicarle.
6. **Dieci documenti.** Ciascuno ha una funzione dichiarata nella challenge map. Non è stato inserito
   alcun foglio di sintesi e nessun foglio di calcolo.
7. **La sospensione feriale dei termini non è toccata.** L'applicabilità della sospensione feriale al
   termine di trenta giorni nel rito degli appalti è discussa e non è stato possibile ancorarla a una
   fonte primaria univoca: il calendario è stato scelto perché nessun termine attraversi agosto. È una
   rinuncia deliberata a un meccanismo di difficoltà, non una dimenticanza.

## Fragilità note, da risolvere in calibrazione

1. **B.7 copre meno di quanto sembri.** È formulato come divieto di presentare il 24 novembre 2027 come
   scadenza anche della censura sul criterio B.2: un deliverable che presenti un termine unico con una
   data *diversa* passa B.7 pur essendo sbagliato. La copertura sostanziale resta su B.6 e B.24. Da
   valutare se riformulare B.7 senza la data.
2. **B.18 accumula due ipotesi.** Il criterio chiede che compaiano entrambe le ipotesi di cessazione
   dell'effetto sospensivo. Formalmente è un solo oggetto (l'elenco delle ipotesi), ma è al limite
   dell'atomicità: se in calibrazione il fail non è attribuibile, va spezzato in B.18a e B.18b.
3. **C.9 e C.10 sono divieti su valori-data che il gold nomina per respingerli.** Il testo del criterio
   vieta di indicarli come termine o come scadenza, non di menzionarli. Se un judge legge la menzione
   critica come violazione, la formula va irrigidita.
4. **Il numero di criteri sui controlled non-issue è basso per un caso di questa ampiezza.** Sono
   cinque. In un workflow di review ne servirebbero di più; qui la famiglia è procedurale e il rumore
   che conta è quello sulle date, coperto dalla sezione C. Da confermare.
5. **La calibrazione del Passo 5 non è stata eseguita.** Il gold è stato verificato contro la propria
   rubrica in forma tabellare, ma non è stato sottoposto ai tre judge; il distrattore è scritto e i
   criteri attesi sono elencati, ma il fallimento non è stato misurato. Il caso non è `pilot_ready`.
