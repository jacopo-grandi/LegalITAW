# WF2-098 - Legal validation

**Stato: `draft_for_legal_validation`. Il caso non e `pilot_ready`.**

Questo file distingue tre cose che non vanno confuse: il self-check meccanico, che
e stato eseguito; la validazione giuridica professionale, che non lo e; la
calibrazione con judge reali, che non lo e.

## Domande per il sign-off

1. L'issue I-05 sposta la definizione di completamento sulla certificazione provinciale. Confermate che la certificazione sia l'atto cui ancorare il completamento, e confermate che il deliverable non debba attribuirle effetti ulteriori rispetto allo svincolo delle garanzie?

2. L'issue I-10 fa salvi gli obblighi che la legge pone al proprietario o gestore non responsabile. Confermate che quegli obblighi si limitino alla comunicazione e alle misure di prevenzione, e che il deliverable non debba affermare un obbligo di bonifica in capo al cessionario?

3. L'issue I-14 tratta il termine di avvio dei lavori come adempimento verso l'autorità che segue il sito. Confermate l'impostazione e confermate che il deliverable non debba qualificare le conseguenze del ritardo, che il reference pack non consente di verificare?

4. Il caso non tratta la sorte dei debiti dell'azienda ceduta né il regime della responsabilità solidale fra cedente e cessionario, perché le norme civilistiche sulla cessione di azienda non sono state verificate su fonte primaria in questa sessione. Volete integrarle, con l'estensione del reference pack e dei criteri che ne consegue?

5. Il gold propone una garanzia finanziaria commisurata all'esposizione stimata e svincolabile progressivamente. Confermate che sia la richiesta da avanzare, o preferite una ritenuta sul prezzo?

6. Il gold indica come posizione minima sul massimale l'esclusione delle voci documentate dal computo del massimale. Confermate che sia la posizione minima corretta?

## Punti che le fonti consultate non risolvono

Nessuno di questi e stato trasformato in criterio.

- Le norme civilistiche sulla cessione di azienda, sulla sorte dei debiti e sulla responsabilità solidale fra cedente e cessionario non sono state verificate su fonte primaria: non figurano nel reference pack e nessun criterio dipende da esse. Il caso è costruito sul solo profilo ambientale.
- Le norme sanzionatorie applicabili al ritardo nell'esecuzione degli interventi approvati non sono state verificate: nessun criterio richiede di qualificare le conseguenze del mancato avvio dei lavori.
- I valori tabellari delle concentrazioni soglia di contaminazione per le acque sotterranee non sono stati verificati su fonte primaria in questa sessione: i valori analitici che compaiono nella relazione di due diligence sono materiale sintetico e nessun criterio richiede di confrontarli con una soglia numerica. La relazione afferma il superamento senza indicare la soglia.
- Nessuna disciplina regionale in materia di bonifiche è stata verificata: il decreto regionale riprodotto nel fascicolo segue la struttura di un provvedimento reale ma non è ancorato ad alcuna disposizione regionale determinata.
- Nessuna pronuncia è stata verificata o citata, in particolare sulla posizione del proprietario non responsabile e sull'efficacia liberatoria della certificazione di avvenuta bonifica.
- La prassi di mercato sui livelli di massimale, franchigia, soglia di irrilevanza e durata della garanzia ambientale non è stata verificata su alcuna fonte: i valori della bozza sono coerenti con esemplari reali consultati, ma nessun criterio richiede di valutarli rispetto a uno standard di mercato.

## Effetto di una correzione

Una correzione che incida su una conclusione richiede l'aggiornamento coordinato di
challenge map, rubrica in prosa, criteri atomizzati, `rubric.json`,
`runtime_routing.json`, gold e distrattore: sono emessi da un'unica fonte
(`source/authoring/casi/wf2_098.py`), quindi si corregge la fonte e si riesegue
`source/gen/assembla_casi.py`.
