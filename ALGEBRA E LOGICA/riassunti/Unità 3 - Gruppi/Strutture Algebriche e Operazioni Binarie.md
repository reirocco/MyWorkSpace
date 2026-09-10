---
tags:
  - strutture-algebriche
  - operazioni-binarie
  - algebra
type: atomic
unit: 3
---

# Strutture Algebriche e Operazioni Binarie

Un'**operazione binaria** su un insieme $A$ è una funzione $\ast: A \times A \to A$.
In termini semplici, è una regola che prende due elementi dell'insieme $A$, li combina, e restituisce un *terzo elemento che deve anch'esso appartenere ad $A$*.

> [!IMPORTANT] Chiusura dell'Operazione
> Il fatto che il risultato debba appartenere all'insieme $A$ si chiama **proprietà di chiusura**. Se un'operazione porta "fuori" dall'insieme, NON è un'operazione binaria interna ben definita.
> *Esempio:* La sottrazione su $\mathbb{N}$ non è chiusa, perché $3 - 5 = -2 \notin \mathbb{N}$. La sottrazione su $\mathbb{Z}$ invece sì.

---

## Proprietà delle Operazioni Binarie

Data un'operazione $\ast$ su un insieme $A$, essa può godere delle seguenti proprietà:

1. **Associatività:** $\forall a, b, c \in A, \quad (a \ast b) \ast c = a \ast (b \ast c)$
   *Permette di omettere le parentesi.*
2. **Commutatività:** $\forall a, b \in A, \quad a \ast b = b \ast a$
3. **Esistenza dell'Elemento Neutro:** $\exists e \in A$ tale che $\forall a \in A, \quad a \ast e = e \ast a = a$
   *Se esiste, è unico. (Es: lo 0 per la somma, l'1 per il prodotto).*
4. **Esistenza dell'Elemento Inverso (o Simmetrico):** Dato un elemento neutro $e$, per ogni $a \in A$ esiste un $a^{-1} \in A$ tale che $a \ast a^{-1} = a^{-1} \ast a = e$.

---

## Classificazione delle Strutture Algebriche

Una **struttura algebrica** è semplicemente una coppia formata da un insieme e da una (o più) operazioni binarie definite su di esso: $(A, \ast)$.

A seconda di quante proprietà della lista precedente vengono soddisfatte, la struttura prende nomi via via più "forti":

- **Magma (o Gruppoide):** Solo la chiusura.
- **Semigruppo:** Chiusura + Associatività. (Es. $(\mathbb{N}^+, +)$)
- **Monoide:** Semigruppo + Esistenza dell'Elemento Neutro. (Es. $(\mathbb{N}, +)$ con lo 0)
- **Gruppo:** Monoide + Esistenza dell'Inverso per *ogni* elemento. (Es. $(\mathbb{Z}, +)$)
- **Gruppo Abeliano (o Commutativo):** Gruppo + Commutatività.

> [!EXAMPLE] Analisi di un Monoide
> Consideriamo l'insieme delle matrici quadrate $M_{n \times n}(\mathbb{R})$ con l'operazione di moltiplicazione righe per colonne.
> - È associativa? Sì.
> - Ha l'elemento neutro? Sì, la matrice identità $I_n$.
> - È commutativa? No, $A \times B \neq B \times A$.
> - Ha gli inversi per *tutti*? No, le matrici con determinante nullo non sono invertibili.
> Dunque $(M_{n \times n}, \times)$ è un **Monoide non commutativo**.

---

## Tip d'Esame

> [!TIP] Come dimostrare l'unicità dell'Elemento Neutro
> È una tipica domanda di teoria da esame orale. Per dimostrare che se esiste un elemento neutro questo è unico, supponi per assurdo che ce ne siano due, $e_1$ ed $e_2$.
> Calcola $e_1 \ast e_2$.
> - Visto che $e_1$ è neutro, il risultato è $e_2$.
> - Visto che $e_2$ è neutro, il risultato è $e_1$.
> Quindi $e_1 = e_2$. Fine!

---

## Note Correlate
- [[03.0 - MoC Teoria dei Gruppi|Unità 3 MoC]]
- [[Definizione di Gruppo ed Esempi Fondamentali]]
