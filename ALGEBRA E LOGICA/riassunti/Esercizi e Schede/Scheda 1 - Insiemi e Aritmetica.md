---
tags:
  - esercizi
  - scheda1
  - insiemi
  - induzione
  - MCD
type: exercise_sheet
unit: 1
---

# Scheda 1: Insiemi, Funzioni, Induzione e Aritmetica

Questa nota sintetizza i principali tipi di esercizi contenuti nella **Scheda 1** e le relative metodologie risolutive.

---

## 1. Dimostrazioni Insiemistiche

### Esempio Tipo
> Dimostrare che $(A \cup B) \setminus C = (A \setminus C) \cup (B \setminus C)$.

### Procedura Risolutiva
1. **Doppia Inclusione:** Dimostrare sia $\subseteq$ sia $\supseteq$.
2. **Definizione Elementare:**
   $$x \in (A \cup B) \setminus C \iff (x \in A \lor x \in B) \land x \notin C$$
   Distribuisci $\land$ su $\lor$:
   $$\iff (x \in A \land x \notin C) \lor (x \in B \land x \notin C) \iff x \in (A \setminus C) \cup (B \setminus C)$$

---

## 2. Studio delle Proprietà di una Funzione

### Esempio Tipo
> Data la funzione $f: \mathbb{N} \rightarrow \mathbb{N}$ definita da $f(n) = 2n + 1$, stabilire se è iniettiva o suriettiva.

### Procedura Risolutiva
- **Iniettività:** Poni $f(n_1) = f(n_2) \implies 2n_1 + 1 = 2n_2 + 1 \implies n_1 = n_2$. *(Iniettiva!)*
- **Suriettività:** Cerca se esiste $n \in \mathbb{N}$ tale che $f(n) = 0$. $2n + 1 = 0 \implies n = -1/2 \notin \mathbb{N}$. *(Non suriettiva!)*

---

## 3. Calcolo MCD ed Identità di Bézout

### Esempio Tipo
> Calcolare $\text{MCD}(143, 65)$ ed esprimerlo nella forma $143x + 65y$.

### Procedura Risolutiva
1. **Algoritmo di Euclide:**
   - $143 = 65 \cdot 2 + 13$
   - $65 = 13 \cdot 5 + 0$
   - L'ultimo resto non nullo è **13**, quindi $\text{MCD}(143, 65) = 13$.
2. **Risalita per Bézout:**
   - $13 = 143 - 65 \cdot 2$.
   - Coefficienti: $x = 1, y = -2$.

---

## Note Correlate
- [[01.0 - MoC Insiemistica e Aritmetica|Unità 1 MoC]]
- [[Insiemi e Operazioni Insiemistiche]]
- [[Funzioni, Iniettività e Suriettività]]
- [[Divisibilità e Algoritmo di Euclide]]
