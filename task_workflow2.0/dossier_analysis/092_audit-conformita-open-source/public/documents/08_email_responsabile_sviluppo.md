Da: Amilcare Bozzetto <a.bozzetto@solmarino.it>
A: Ludovica Sperandini <l.sperandini@solmarino.it>
Cc: Delfina Cusumano <d.cusumano@solmarino.it>
Oggetto: pianificatore - stato patch e nota sul portale
Data: lunedì 2 novembre 2026, 09:14

Ludovica,

riassumo lo stato prima del congelamento di venerdì.

Pianificatore. La patch sulla coda e sulle priorità è chiusa e in produzione dal 14
settembre. Tocca tre file del pacchetto originale: la struttura della coda,
l'assegnazione della priorità e il ciclo di ripetizione. La logica che abbiamo
scritto noi vale, secondo me, il grosso del valore del componente: senza quella il
pianificatore non regge i carichi del cliente principale. Il pacchetto lo abbiamo
preso dal registro pubblico e non abbiamo pubblicato nulla.

Il pianificatore gira solo in cloud. Gli utenti del cliente lo raggiungono
dall'esterno: il portale chiama l'orchestratore, e l'orchestratore espone anche
un'interfaccia programmatica che due clienti usano direttamente dai loro sistemi
per accodare le esecuzioni notturne.

Coda di elaborazione secondaria. Per la coda secondaria abbiamo tenuto il pacchetto
tessitura-queue senza toccarlo, così com'è nel registro. Anche quello sta in cloud.

Portale. Il componente di compilazione guidata è quello approvato in giugno,
aurendo-forms, senza modifiche. È la parte con cui gli utenti del cliente
compilano i moduli di collaudo: è esattamente la funzione che vedono quando entrano
nel portale.

Strumenti interni. Il caricatore che usiamo in assistenza l'abbiamo modificato per
leggere i tracciati vecchi. Quello resta sui nostri sistemi, non esce da qui e non
lo installiamo da nessuna parte.

Report. Sul motore di impaginazione abbiamo cambiato il calcolo dei margini per
farci stare l'intestazione del cliente. Quello viaggia sull'appliance.

Cifratura. Ho toccato tre file del generatore di chiavi per allinearlo alla
lunghezza richiesta dalle specifiche del cliente. Non ho aggiunto intestazioni, ho
lasciato quelle originali.

Dimmi se serve altro per venerdì.

Amilcare Bozzetto
Responsabile sviluppo piattaforma
