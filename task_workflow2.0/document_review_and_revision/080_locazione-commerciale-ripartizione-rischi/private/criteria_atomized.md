# WF2-080 - Criteri atomizzati

Ogni riga valuta un solo fatto, valore, collegamento probatorio, effetto o azione.

## A.1

- Tipo: struttura
- Issue: A
- Verifica: la consegna usa i file lease_redline.docx e negotiation_note.md.
- Pass (insieme chiuso): i nomi dei file coincidono con lease_redline.docx e negotiation_note.md | il controllo deterministico sul requisito restituisce esito positivo
- Fail: manca un file o il nome diverge
- Fonte: response_template.md

## A.2

- Tipo: struttura
- Issue: A
- Verifica: la consegna contiene le sezioni obbligatorie nell'ordine indicato.
- Pass (insieme chiuso): tutte le intestazioni compaiono nell'ordine del template | il controllo deterministico sul requisito restituisce esito positivo
- Fail: manca un'intestazione o l'ordine diverge
- Fonte: response_template.md

## A.3

- Tipo: struttura
- Issue: A
- Verifica: la parte testuale non supera 1.700 parole.
- Pass (insieme chiuso): il conteggio non supera 1.700 | il controllo deterministico sul requisito restituisce esito positivo
- Fail: il conteggio supera il limite
- Fonte: task_spec.json

## A.4

- Tipo: struttura
- Issue: A
- Verifica: ogni conclusione di merito indica almeno un documento o una fonte del reference pack.
- Pass (insieme chiuso): ogni conclusione reca una traccia documentale o normativa | il controllo deterministico sul requisito restituisce esito positivo
- Fail: una conclusione è priva di traccia
- Fonte: 02_reference_pack.md; documenti

## B.1

- Tipo: valore
- Issue: I-01
- Verifica: il deliverable riporta il valore documentato per durata.
- Pass (insieme chiuso): compare «sei anni» | compare «6 anni»
- Fail: non compare ne «sei anni» ne «6 anni» oppure compare un valore incompatibile
- Fonte: 01_bozza_locazione_via_delle_vele_18.docx, contenuto pertinente a durata; art. 27 legge 392/1978

## B.2

- Tipo: attribuzione
- Issue: I-01
- Verifica: il deliverable collega il dato al documento: bozza, destinazione retail.
- Pass (insieme chiuso): cita 01_bozza_locazione_via_delle_vele_18.docx, contenuto pertinente a durata | indica come riscontro 01_bozza_locazione_via_delle_vele_18.docx, contenuto pertinente a durata
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_bozza_locazione_via_delle_vele_18.docx, contenuto pertinente a durata; art. 27 legge 392/1978

## B.3

- Tipo: qualificazione
- Issue: I-01
- Verifica: il deliverable espone l'effetto: la previsione quadriennale va sostituita.
- Pass (insieme chiuso): espone l'effetto: la previsione quadriennale va sostituita | indica come conseguenza: la previsione quadriennale va sostituita
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_bozza_locazione_via_delle_vele_18.docx, contenuto pertinente a durata; art. 27 legge 392/1978

## B.4

- Tipo: presenza
- Issue: I-02
- Verifica: il deliverable enuncia il risultato: la cessazione automatica senza rinnovo non riflette il regime applicabile.
- Pass (insieme chiuso): afferma: la cessazione automatica senza rinnovo non riflette il regime applicabile | conclude: la cessazione automatica senza rinnovo non riflette il regime applicabile
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_bozza_locazione_via_delle_vele_18.docx, contenuto pertinente a rinnovo; legge 392/1978

## B.5

- Tipo: attribuzione
- Issue: I-02
- Verifica: il deliverable collega il dato al documento: clausola 3.
- Pass (insieme chiuso): cita 01_bozza_locazione_via_delle_vele_18.docx, contenuto pertinente a rinnovo | indica come riscontro 01_bozza_locazione_via_delle_vele_18.docx, contenuto pertinente a rinnovo
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_bozza_locazione_via_delle_vele_18.docx, contenuto pertinente a rinnovo; legge 392/1978

## B.6

- Tipo: qualificazione
- Issue: I-02
- Verifica: il deliverable espone l'effetto: occorre disciplinare rinnovo e diniego.
- Pass (insieme chiuso): espone l'effetto: occorre disciplinare rinnovo e diniego | indica come conseguenza: occorre disciplinare rinnovo e diniego
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 01_bozza_locazione_via_delle_vele_18.docx, contenuto pertinente a rinnovo; legge 392/1978

## B.7

- Tipo: presenza
- Issue: I-03
- Verifica: il deliverable enuncia il risultato: la bozza esclude il recesso per gravi motivi.
- Pass (insieme chiuso): afferma: la bozza esclude il recesso per gravi motivi | conclude: la bozza esclude il recesso per gravi motivi
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_trattativa_e_term_sheet.xlsx, contenuto pertinente a recesso conduttore; art. 27 legge 392/1978

## B.8

- Tipo: attribuzione
- Issue: I-03
- Verifica: il deliverable collega il dato al documento: clausola 4.
- Pass (insieme chiuso): cita 02_registro_trattativa_e_term_sheet.xlsx, contenuto pertinente a recesso conduttore | indica come riscontro 02_registro_trattativa_e_term_sheet.xlsx, contenuto pertinente a recesso conduttore
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_trattativa_e_term_sheet.xlsx, contenuto pertinente a recesso conduttore; art. 27 legge 392/1978

## B.9

- Tipo: qualificazione
- Issue: I-03
- Verifica: il deliverable espone l'effetto: l'esclusione espone la clausola a inefficacia.
- Pass (insieme chiuso): espone l'effetto: l'esclusione espone la clausola a inefficacia | indica come conseguenza: l'esclusione espone la clausola a inefficacia
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_trattativa_e_term_sheet.xlsx, contenuto pertinente a recesso conduttore; art. 27 legge 392/1978

## B.10

- Tipo: valore
- Issue: I-04
- Verifica: il deliverable riporta il valore documentato per istat.
- Pass (insieme chiuso): compare «settantacinque per cento» | compare «75%»
- Fail: non compare ne «settantacinque per cento» ne «75%» oppure compare un valore incompatibile
- Fonte: 02_registro_trattativa_e_term_sheet.xlsx, contenuto pertinente a istat; art. 32 legge 392/1978

## B.11

- Tipo: attribuzione
- Issue: I-04
- Verifica: il deliverable collega il dato al documento: clausola 5.
- Pass (insieme chiuso): cita 02_registro_trattativa_e_term_sheet.xlsx, contenuto pertinente a istat | indica come riscontro 02_registro_trattativa_e_term_sheet.xlsx, contenuto pertinente a istat
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_trattativa_e_term_sheet.xlsx, contenuto pertinente a istat; art. 32 legge 392/1978

## B.12

- Tipo: qualificazione
- Issue: I-04
- Verifica: il deliverable espone l'effetto: la percentuale del cento per cento va ridotta.
- Pass (insieme chiuso): espone l'effetto: la percentuale del cento per cento va ridotta | indica come conseguenza: la percentuale del cento per cento va ridotta
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 02_registro_trattativa_e_term_sheet.xlsx, contenuto pertinente a istat; art. 32 legge 392/1978

## B.13

- Tipo: presenza
- Issue: I-05
- Verifica: il deliverable enuncia il risultato: il canone decorre dalla consegna con agibilità e impianti funzionanti.
- Pass (insieme chiuso): afferma: il canone decorre dalla consegna con agibilità e impianti funzionanti | conclude: il canone decorre dalla consegna con agibilità e impianti funzionanti
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_consegna_lavori_e_titoli.eml, contenuto pertinente a consegna; term sheet; bozza

## B.14

- Tipo: attribuzione
- Issue: I-05
- Verifica: il deliverable collega il dato al documento: term sheet e verbale tecnico.
- Pass (insieme chiuso): cita 03_email_consegna_lavori_e_titoli.eml, contenuto pertinente a consegna | indica come riscontro 03_email_consegna_lavori_e_titoli.eml, contenuto pertinente a consegna
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_consegna_lavori_e_titoli.eml, contenuto pertinente a consegna; term sheet; bozza

## B.15

- Tipo: qualificazione
- Issue: I-05
- Verifica: il deliverable espone l'effetto: la decorrenza non può restare agganciata alla firma.
- Pass (insieme chiuso): espone l'effetto: la decorrenza non può restare agganciata alla firma | indica come conseguenza: la decorrenza non può restare agganciata alla firma
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_consegna_lavori_e_titoli.eml, contenuto pertinente a consegna; term sheet; bozza

## B.16

- Tipo: presenza
- Issue: I-06
- Verifica: il deliverable enuncia il risultato: le opere strutturali non causate dalla conduttrice restano al locatore.
- Pass (insieme chiuso): afferma: le opere strutturali non causate dalla conduttrice restano al locatore | conclude: le opere strutturali non causate dalla conduttrice restano al locatore
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_consegna_lavori_e_titoli.eml, contenuto pertinente a riparazioni; codice civile; relazione

## B.17

- Tipo: attribuzione
- Issue: I-06
- Verifica: il deliverable collega il dato al documento: relazione tecnica.
- Pass (insieme chiuso): cita 03_email_consegna_lavori_e_titoli.eml, contenuto pertinente a riparazioni | indica come riscontro 03_email_consegna_lavori_e_titoli.eml, contenuto pertinente a riparazioni
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_consegna_lavori_e_titoli.eml, contenuto pertinente a riparazioni; codice civile; relazione

## B.18

- Tipo: qualificazione
- Issue: I-06
- Verifica: il deliverable espone l'effetto: il trasferimento totale altera la ripartizione del rischio.
- Pass (insieme chiuso): espone l'effetto: il trasferimento totale altera la ripartizione del rischio | indica come conseguenza: il trasferimento totale altera la ripartizione del rischio
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 03_email_consegna_lavori_e_titoli.eml, contenuto pertinente a riparazioni; codice civile; relazione

## B.19

- Tipo: presenza
- Issue: I-07
- Verifica: il deliverable enuncia il risultato: il locatore deve consegnare documenti e prestare cooperazione per i titoli.
- Pass (insieme chiuso): afferma: il locatore deve consegnare documenti e prestare cooperazione per i titoli | conclude: il locatore deve consegnare documenti e prestare cooperazione per i titoli
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_verifica_precontrattuale_elvi.pdf, contenuto pertinente a autorizzazioni; allegato tecnico

## B.20

- Tipo: attribuzione
- Issue: I-07
- Verifica: il deliverable collega il dato al documento: allegato tecnico.
- Pass (insieme chiuso): cita 04_relazione_verifica_precontrattuale_elvi.pdf, contenuto pertinente a autorizzazioni | indica come riscontro 04_relazione_verifica_precontrattuale_elvi.pdf, contenuto pertinente a autorizzazioni
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_verifica_precontrattuale_elvi.pdf, contenuto pertinente a autorizzazioni; allegato tecnico

## B.21

- Tipo: qualificazione
- Issue: I-07
- Verifica: il deliverable espone l'effetto: la conduttrice non controlla documenti proprietari.
- Pass (insieme chiuso): espone l'effetto: la conduttrice non controlla documenti proprietari | indica come conseguenza: la conduttrice non controlla documenti proprietari
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_verifica_precontrattuale_elvi.pdf, contenuto pertinente a autorizzazioni; allegato tecnico

## B.22

- Tipo: valore
- Issue: I-08
- Verifica: il deliverable riporta il valore documentato per deposito.
- Pass (insieme chiuso): compare «tre mensilita» | compare «3 mensilita»
- Fail: non compare ne «tre mensilita» ne «3 mensilita» oppure compare un valore incompatibile
- Fonte: 04_relazione_verifica_precontrattuale_elvi.pdf, contenuto pertinente a deposito; term sheet; legge 392/1978

## B.23

- Tipo: attribuzione
- Issue: I-08
- Verifica: il deliverable collega il dato al documento: bozza e term sheet.
- Pass (insieme chiuso): cita 04_relazione_verifica_precontrattuale_elvi.pdf, contenuto pertinente a deposito | indica come riscontro 04_relazione_verifica_precontrattuale_elvi.pdf, contenuto pertinente a deposito
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_verifica_precontrattuale_elvi.pdf, contenuto pertinente a deposito; term sheet; legge 392/1978

## B.24

- Tipo: qualificazione
- Issue: I-08
- Verifica: il deliverable espone l'effetto: la deviazione va negoziata e resa fruttifera secondo disciplina.
- Pass (insieme chiuso): espone l'effetto: la deviazione va negoziata e resa fruttifera secondo disciplina | indica come conseguenza: la deviazione va negoziata e resa fruttifera secondo disciplina
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 04_relazione_verifica_precontrattuale_elvi.pdf, contenuto pertinente a deposito; term sheet; legge 392/1978

## B.25

- Tipo: presenza
- Issue: I-09
- Verifica: il deliverable enuncia il risultato: la clausola non salva il trasferimento insieme all'azienda.
- Pass (insieme chiuso): afferma: la clausola non salva il trasferimento insieme all'azienda | conclude: la clausola non salva il trasferimento insieme all'azienda
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_negoziale_borgoluce.pdf, contenuto pertinente a cessione; art. 36 legge 392/1978

## B.26

- Tipo: attribuzione
- Issue: I-09
- Verifica: il deliverable collega il dato al documento: clausola 14.
- Pass (insieme chiuso): cita 05_nota_negoziale_borgoluce.pdf, contenuto pertinente a cessione | indica come riscontro 05_nota_negoziale_borgoluce.pdf, contenuto pertinente a cessione
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_negoziale_borgoluce.pdf, contenuto pertinente a cessione; art. 36 legge 392/1978

## B.27

- Tipo: qualificazione
- Issue: I-09
- Verifica: il deliverable espone l'effetto: il divieto assoluto confligge con il regime speciale.
- Pass (insieme chiuso): espone l'effetto: il divieto assoluto confligge con il regime speciale | indica come conseguenza: il divieto assoluto confligge con il regime speciale
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_negoziale_borgoluce.pdf, contenuto pertinente a cessione; art. 36 legge 392/1978

## B.28

- Tipo: presenza
- Issue: I-10
- Verifica: il deliverable enuncia il risultato: la rinuncia preventiva all'indennità per perdita di avviamento va eliminata.
- Pass (insieme chiuso): afferma: la rinuncia preventiva all'indennità per perdita di avviamento va eliminata | conclude: la rinuncia preventiva all'indennità per perdita di avviamento va eliminata
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_negoziale_borgoluce.pdf, contenuto pertinente a indennità; artt. 34 e 79 legge 392/1978

## B.29

- Tipo: attribuzione
- Issue: I-10
- Verifica: il deliverable collega il dato al documento: clausola 17.
- Pass (insieme chiuso): cita 05_nota_negoziale_borgoluce.pdf, contenuto pertinente a indennità | indica come riscontro 05_nota_negoziale_borgoluce.pdf, contenuto pertinente a indennità
- Fail: omette l'elemento verificato oppure afferma il contrario
- Fonte: 05_nota_negoziale_borgoluce.pdf, contenuto pertinente a indennità; artt. 34 e 79 legge 392/1978

## C.1

- Tipo: assenza
- Issue: N-01
- Verifica: chiusura simmetria sul falso positivo «uso retail»: La destinazione retail non basta, senza dati sull'attività, a provare il diritto all'indennità finale.
- Pass (insieme chiuso): non qualifica come criticita uso retail | esclude espressamente il falso positivo uso retail
- Fail: compare la conclusione vietata «uso retail costituisce una criticita autonoma»
- Fonte: challenge_map.json; documenti pubblici

## C.2

- Tipo: assenza
- Issue: N-02
- Verifica: chiusura sovra-segnalazione sul falso positivo «lavori allestimento»: I lavori di allestimento della conduttrice non trasferiscono automaticamente i difetti strutturali.
- Pass (insieme chiuso): non qualifica come criticita lavori allestimento | esclude espressamente il falso positivo lavori allestimento
- Fail: compare la conclusione vietata «lavori allestimento costituisce una criticita autonoma»
- Fonte: challenge_map.json; documenti pubblici

## C.3

- Tipo: assenza
- Issue: N-03
- Verifica: chiusura presunzione sul falso positivo «fideiussione futura»: Il richiamo a una futura fideiussione non documenta termini e oneri della garanzia.
- Pass (insieme chiuso): non qualifica come criticita fideiussione futura | esclude espressamente il falso positivo fideiussione futura
- Fail: compare la conclusione vietata «fideiussione futura costituisce una criticita autonoma»
- Fonte: challenge_map.json; documenti pubblici
