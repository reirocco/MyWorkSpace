---
tags:
  - tautologie
  - equivalenza-logica
  - de-morgan
  - logica-proposizionale
type: atomic
unit: 5
---

# Tautologie, Contraddizioni e Equivalenze Logiche

Ogni formula proposizionale, in base all'esito della sua tavola di verità (cioè in base al valore che assume per tutte le possibili combinazioni delle variabili), ricade in una di tre categorie.

## Classificazione delle Formule

1. **Tautologia (Validità):** Una formula è una tautologia se risulta **SEMPRE VERA** per qualsiasi assegnazione di verità alle sue variabili (la sua colonna finale ha solo "1").
   *Esempio: $P \lor \neg P$ (Principio del Terzo Escluso).*
2. **Contraddizione (Insoddisfacibile):** Una formula è una contraddizione se risulta **SEMPRE FALSA** per qualsiasi assegnazione (la colonna finale ha solo "0").
   *Esempio: $P \land \neg P$ (Principio di Non Contraddizione).*
3. **Contingenza (Soddisfacibile ma non valida):** Una formula è contingente se in alcuni casi è vera e in altri è falsa.

> [!NOTE] Relazione Cruciale
> - $F$ è una Tautologia $\iff \neg F$ è una Contraddizione.
> - Per verificare se una formula è una tautologia, l'approccio "brute force" è costruire la tabella di verità completa. Per $n$ variabili, la tabella ha $2^n$ righe.

---

## Equivalenza Logica ($\equiv$)

Due formule $F$ e $G$ si dicono **Logicamente Equivalenti** ($F \equiv G$) se assumono lo stesso valore di verità per ogni possibile assegnazione.
In altre parole, $F \equiv G$ se e solo se la doppia implicazione $(F \leftrightarrow G)$ è una Tautologia.

### Le Leggi (Equivalenze) Fondamentali da Memorizzare
Queste equivalenze funzionano come l'algebra tradizionale, permettendo di semplificare le formule:

- **Idempotenza:** $P \land P \equiv P \quad \text{e} \quad P \lor P \equiv P$
- **Doppia Negazione:** $\neg(\neg P) \equiv P$
- **Distributività:**
  - $P \land (Q \lor R) \equiv (P \land Q) \lor (P \land R)$
  - $P \lor (Q \land R) \equiv (P \lor Q) \land (P \lor R)$
- **Leggi di De Morgan (Fondamentali!):**
  - $\neg(P \land Q) \equiv \neg P \lor \neg Q$ *(Nega tutto e gira il connettivo)*
  - $\neg(P \lor Q) \equiv \neg P \land \neg Q$
- **Leggi di Assorbimento:**
  - $P \land (P \lor Q) \equiv P$
  - $P \lor (P \land Q) \equiv P$
- **Sostituzione dell'Implicazione:**
  - $P \rightarrow Q \equiv \neg P \lor Q$
  - $P \leftrightarrow Q \equiv (P \rightarrow Q) \land (Q \rightarrow P)$
- **Contrapposizione (o Modus Tollens):**
  - $P \rightarrow Q \equiv \neg Q \rightarrow \neg P$

> [!EXAMPLE] Dimostrazione Algebrica
> Dimostriamo che $P \rightarrow (Q \lor R)$ è equivalente a $(P \land \neg Q) \rightarrow R$.
> 1. Sostituisco l'implicazione a sinistra: $\neg P \lor (Q \lor R)$.
> 2. Sostituisco l'implicazione a destra: $\neg(P \land \neg Q) \lor R$.
> 3. Applico De Morgan a destra: $(\neg P \lor \neg(\neg Q)) \lor R$.
> 4. Applico la doppia negazione a destra: $(\neg P \lor Q) \lor R$.
> 5. Le due formule ottenute sono identiche a meno delle parentesi (che per associatività si possono togliere). Dimostrato!

---

## Tip d'Esame

> [!TIP] Come usare la Contrapposizione
> Nelle dimostrazioni matematiche, se devi provare $A \implies B$ ma è troppo difficile in avanti, il teorema della Contrapposizione ti autorizza a provare invece $\neg B \implies \neg A$.
> *Esempio:* Dimostrare "Se $n^2$ è pari, allora $n$ è pari".
> Proviamo la contrappositiva: "Se $n$ è dispari (non pari), allora $n^2$ è dispari". Questo si fa in due righe: $n=2k+1 \implies n^2 = 4k^2+4k+1 = 2(2k^2+2k)+1$, che è dispari. Fine!

---

## Note Correlate
- [[05.0 - MoC Logica|Unità 5 MoC]]
- [[Connettivi Logici e Tavole di Verità]]
- [[Soddisfacibilità e Problema SAT]]
