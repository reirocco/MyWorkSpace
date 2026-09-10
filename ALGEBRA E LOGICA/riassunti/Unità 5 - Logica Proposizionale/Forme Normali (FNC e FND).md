---
tags:
  - forma-normale
  - fnc
  - fnd
  - logica-proposizionale
type: atomic
unit: 5
---

# Forme Normali (FNC e FND)

Ogni formula proposizionale, per quanto complessa, "annidata" o ricca di implicazioni, può essere convertita (tramite le regole di equivalenza) in un formato "standard" a due livelli, estremamente utile per gli algoritmi informatici: la Forma Normale.

Ci sono due varianti principali: la FNC e la FND.

## Concetti Preliminari
- **Letterale:** È una variabile proposizionale (es. $P$) oppure la sua negazione (es. $\neg P$).
- **Clausola Disgiuntiva (Maxtermine):** È una disgiunzione (OR, $\lor$) di letterali. Es. $(P \lor \neg Q \lor R)$.
- **Clausola Congiuntiva (Mintermine):** È una congiunzione (AND, $\land$) di letterali. Es. $(P \land Q \land \neg R)$.

---

## 1. Forma Normale Congiuntiva (FNC / CNF)

Una formula è in **FNC (Conjunctive Normal Form)** se è un grande $\text{AND}$ di $\text{OR}$.
Formalmente, è una congiunzione ($\land$) di clausole disgiuntive.
**Struttura visiva:** $(A \lor B) \land (C \lor \neg D) \land (\neg A \lor E)$

> [!IMPORTANT] Perché la FNC è cruciale?
> La FNC è il formato di input obbligatorio per tutti i moderni **SAT Solver** (i programmi che verificano la soddisfacibilità). Un grande AND è vero se e solo se *tutte* le clausole interne (gli OR) sono vere simultaneamente.

## 2. Forma Normale Disgiuntiva (FND / DNF)

Una formula è in **FND (Disjunctive Normal Form)** se è un grande $\text{OR}$ di $\text{AND}$.
Formalmente, è una disgiunzione ($\lor$) di clausole congiuntive.
**Struttura visiva:** $(A \land B) \lor (C \land \neg D) \lor (\neg A \land E)$

> L'utilità della FND sta nel fatto che, se una formula è scritta così, per sapere se è soddisfacibile (vera in almeno un caso) basta guardare se esiste almeno un blocco AND che non contenga una contraddizione ovvia (come $P \land \neg P$). Se c'è, la formula è soddisfacibile.

---

## Algoritmo di Conversione in FNC

Esiste una procedura meccanica (da sapere a memoria) per convertire QUALSIASI formula nella sua FNC equivalente:

1. **Elimina le doppie implicazioni ($\leftrightarrow$):** Sostituisci $A \leftrightarrow B$ con $(A \rightarrow B) \land (B \rightarrow A)$.
2. **Elimina le implicazioni ($\rightarrow$):** Sostituisci $A \rightarrow B$ con $\neg A \lor B$.
3. **Spingi in dentro le negazioni (De Morgan):** Usa le leggi di De Morgan e la doppia negazione per far arrivare i simboli "$\neg$" attaccati esclusivamente alle singole variabili.
   *(Es: $\neg(A \land B)$ diventa $\neg A \lor \neg B$).*
4. **Distribuisci gli OR sugli AND:** Usa la distributività $A \lor (B \land C) \equiv (A \lor B) \land (A \lor C)$ per far emergere gli AND come connettivi principali esterni.

> [!EXAMPLE] Conversione passo-passo
> Convertire in FNC: $\neg (P \rightarrow (Q \land R))$
> 1. Tolgo la freccia: $\neg (\neg P \lor (Q \land R))$
> 2. De Morgan verso l'interno: $\neg(\neg P) \land \neg(Q \land R)$
> 3. Doppia negazione e ancora De Morgan: $P \land (\neg Q \lor \neg R)$
> Finito! Questa è già una FNC (un AND tra due blocchi: il letterale $P$ e l'OR $\neg Q \lor \neg R$).

---

## Tip d'Esame

> [!TIP] Clausole singole
> Attenzione: un letterale isolato può fungere sia da "clausola disgiuntiva" che da "clausola congiuntiva".
> La formula $P \land Q$ è **già** sia in FNC che in FND!
> In FNC si vede come $(P) \land (Q)$.
> In FND si vede come un unico grande blocco: $(P \land Q)$.

---

## Note Correlate
- [[05.0 - MoC Logica|Unità 5 MoC]]
- [[Tautologie, Contraddizioni e Equivalenze Logiche]]
- [[Soddisfacibilità e Problema SAT]]
