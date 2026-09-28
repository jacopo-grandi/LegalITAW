# WF2-032 - Distrattore

Versione del deliverable deliberatamente sbagliata su tre punti.

## Errori introdotti

1. **Sospensione di novanta giorni.** L'audit segue la nota del consulente, applica la sospensione
   ordinaria e indica il 18 dicembre 2030 come termine per il ricorso.
2. **Reclamo indicato come passaggio obbligato.** L'audit inserisce fra le attivita' da compiere la
   presentazione del reclamo con proposta di mediazione, con scadenza anteriore al ricorso.
3. **Nessuna riscossione in pendenza di giudizio.** L'audit afferma che, proposto il ricorso, nessuna
   somma potra' essere richiesta fino alla sentenza, e non quantifica l'importo iscrivibile a titolo
   provvisorio.

## Criteri che devono fallire

| Criterio | Issue | Ragione |
|---|---|---|
| B.3 | I-02 | non indica la sospensione in trenta giorni |
| B.4 | I-02 | non riconduce la durata allo schema di atto |
| B.5 | I-02 | indica la sospensione in novanta giorni |
| C.3 | I-04 | non indica il 19 ottobre 2030 come scadenza nominale |
| C.4 | I-04 | non tratta la proroga per il sabato |
| C.5 | I-04 | non indica il 21 ottobre 2030 come termine ultimo |
| C.7 | I-11 | il termine di costituzione, calcolato sul termine sbagliato, non e' il 20 novembre 2030 |
| C.9 | I-02 | indica il 18 dicembre 2030 come termine |
| C.14 | I-05 | i giorni residui non sono trentacinque |
| B.24 | I-12 | indica il reclamo fra le attivita' da compiere |
| B.13 | I-09 | non afferma che l'Ufficio puo' iscrivere un terzo |
| B.14 | I-09 | afferma che nulla puo' essere iscritto a ruolo |
| C.8 | I-09 | non indica euro 166.000,00 |

## Criteri che devono continuare a passare

Tutti gli altri, in particolare B.1, B.2, B.6, B.7, B.8, B.9, B.10, B.11, B.12, B.15, B.16, B.17,
B.18, B.19, B.20, B.21, B.22, B.23, B.25, B.26, B.27, B.28, B.29, B.30 e i criteri C.1, C.2, C.6,
C.10, C.11, C.12, C.13.

Nota sull'accoppiamento voluto. L'errore 1 tocca nove criteri distribuiti su quattro issue (I-02,
I-04, I-05, I-11): il termine sbagliato si propaga a tutto cio' che da esso dipende, ed e' la
struttura della catena, non un difetto di atomizzazione. Il criterio B.7, sullo stato del termine,
continua a passare: anche con la data sbagliata il termine resta pendente, e l'audit lo dice. E' il
comportamento voluto, perche' B.7 misura lo stato e non il calcolo.

L'errore 2 tocca un solo criterio. L'errore 3 tocca tre criteri dello stesso issue I-09 e nessun
altro.
