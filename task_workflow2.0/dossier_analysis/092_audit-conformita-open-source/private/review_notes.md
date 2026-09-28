# WF2-092 - Decision log

## Vincoli dalla matrice master

- Famiglia: `Dossier analysis`
- Area primaria: IP & Technology
- Deliverable: `open_source_audit.md`
- Difficolta: medium; pack tier: medium
- Forchetta dei criteri: 45-58; criteri effettivi: 54

## Scelte assunte in fase di authoring

- Il prodotto è stato costruito con due canali di fornitura contemporanei, appliance e servizio in cloud, perché è la sola configurazione in cui l'obbligo dipende dal canale e non dal componente: lo stesso pacchetto Apache produce conseguenze diverse nei due canali.
- Le coppie modificato / non modificato e limitato a una versione / con opzione di versione successiva sono costruite su componenti distinti che condividono tutto il resto: è il modo per misurare se l'agente legge il presupposto della licenza o assimila per categoria.
- Il testo delle licenze non è allegato: le licenze sono la regola che l'agente deve applicare e stanno nel reference pack, non nel fascicolo. Nel fascicolo ci sono soltanto gli avvisi che il prodotto spedisce e le intestazioni dei file, che sono fatti.
- L'email del responsabile sviluppo contiene una valutazione di parte sul valore della logica scritta internamente: è una dichiarazione, non un fatto, e il prompt chiede espressamente di tenere separati i due piani.
- La nota finale del piano di rilascio afferma che le attività aperte non impediscono il rilascio. È una dichiarazione sulla procedura interna e la sua accettazione acritica è l'errore-bersaglio dell'ultimo issue.
- Sono stati inseriti cinque controlled non-issue: quattro riguardano assimilazioni fra componenti simili, il quinto una categoria giuridica che la licenza non contiene.

## Stato

`draft_for_legal_validation`; `pilot_ready: false`; nessun run eseguito.
