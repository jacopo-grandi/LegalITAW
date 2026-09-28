# WF2-038 — Note di costruzione e scelte discrezionali

Registro dei bivi presi in fase di build. Serve a chi rivede il caso per capire che cosa è
stato deciso e che cosa può essere deciso diversamente senza rifare tutto.

## Perché questo caso non ripete WF2-023 e WF2-027

Sono i due `review_only` già costruiti. La regola di diversità chiede di variare almeno due
assi rispetto al caso esistente più vicino.

| Asse | WF2-023 (SaaS) | WF2-027 (transazione dirigente) | WF2-038 |
|---|---|---|---|
| verticale | contrattualistica commerciale / IT | employment | banking & finance, finanziamenti corporate |
| oggetto della review | bozza non ancora sottoscritta | bozza non ancora sottoscritta | **contratto in essere** e posizione del cliente alla data di riferimento |
| meccanismi portanti | gerarchia ordine/bozza, disponibilità sui minuti computati | presenza contro adeguatezza, data del documento contro data di efficacia | versioni incompatibili sul livello del covenant, definizione convenzionale che governa il perimetro di una posta, termine dipendente da più eventi |
| errore-bersaglio | rimedio presente con credito maturato pari a zero | rinuncia più ampia di quanto il cliente crede | **collasso dei tre livelli** violazione / evento di default / conseguenza |

La terza riga è la variazione più significativa: rivedere un contratto **in essere** contro i
fatti, invece di una bozza prima della firma, è una forma di `review_only` che il set non
conteneva.

## Scelte discrezionali

1. **Il cliente è la società finanziata, non le banche.** Ne discende che ogni issue deve essere
   contro di lei. Il controllo di lato è stato rifatto a valle: le clausole a favore del cliente
   — sostituzione della banca non consenziente, rimborso anticipato volontario senza compenso,
   rinuncia all'articolo 1957 nella fideiussione — sono controlled non-issue, non issue.
   La scopertura della fideiussione è un issue **perché** il contratto impone alla società di
   mantenere la garanzia a un livello determinato: senza quell'impegno sarebbe stata un
   vantaggio del cliente e quindi un errore di lato.

2. **Undici documenti, nessun foglio di sintesi.** La posizione sui covenant non è riassunta da
   nessuna parte: emerge incrociando il prospetto di calcolo, l'atto di postergazione e il
   verbale del consiglio. Per lo stesso motivo i certificati di conformità sono due e non uno:
   il precedente esercizio del rimedio è un fatto che il fascicolo deve contenere senza
   dichiararlo.

3. **Il certificato dichiara un limite sbagliato in senso conservativo.** Indica 3,50x invece di
   3,90x, e con l'indice dichiarato di 3,42x la conclusione non cambia. È una scelta: se il
   limite sbagliato avesse da solo prodotto una violazione, il caso sarebbe stato risolvibile
   correggendo il livello, senza toccare il calcolo. Così i due passaggi — il livello e la
   posta — vanno fatti entrambi, e sbagliarne uno solo non basta a sbagliare la conclusione
   qualitativa ma sposta lo scostamento da 0,06 a 0,46.

4. **La finestra di rimedio è aperta e il rimedio è precluso.** È il cuore del caso. La scelta
   alternativa — finestra già scaduta — avrebbe prodotto un caso più semplice e avrebbe reso
   inutile il secondo certificato di conformità.

5. **La diffida del locatore scade il giorno dopo la data di riferimento.** Serve a misurare
   l'ordinamento per priorità: il rilievo di gravità maggiore non è quello con la scadenza più
   vicina, e una nota che ordina per gravità invece che per urgenza sbaglia l'ordine.

6. **L'operazione societaria non è perfezionata.** La data di riferimento è *ex ante* rispetto
   al cambio di controllo (`metodo_e_convenzioni.md`, decisione #6): i criteri sono sul percorso
   e sul divieto di presumere l'esito, non sullo stato di avanzamento.

7. **Nessun codice fiscale di persona fisica nei documenti.** Non ne serviva alcuno, e la sua
   presenza avrebbe imposto la verifica su fonte del codice catastale, che non è calcolabile per
   algoritmo.

## Decisioni che spettano a chi rivede

- Se la definizione convenzionale di Cambio di Controllo per moltiplicazione sia realistica, o
  se convenga rinviare all'articolo 2359 del codice civile e costruire diversamente la soglia
  (vedi `source/authoring/legal_validation.md`, § 1.3).
- Se la scala di gravità assegnata ai rilievi sia quella giusta, e in particolare se la
  scopertura della fideiussione debba stare sopra o sotto la comunicazione omessa della
  dismissione.
- Se il limite di 2.600 parole sia adeguato a un deliverable che contiene una tabella di dieci
  righe: il gold sta a 2.428 parole.
- Se il caso vada somministrato anche in versione *human-in-the-loop*, dove la domanda al
  cliente — «esiste un atto di adesione alla postergazione?» — è esattamente il punto che
  decide il caso.
