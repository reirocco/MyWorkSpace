---
tags:
  - insiemistica
  - teoria-degli-insiemi
  - algebra
type: atomic
unit: 1
---
# Insiemi e Operazioni Insiemistiche

Un **insieme** è una collezione ben definita di oggetti distinti, detti *elementi*. Se $x$ è un elemento dell'insieme $A$, si scrive $x \in A$. L'assenza di elementi è rappresentata dall'**insieme vuoto** $\emptyset$.

---

## Operazioni Fondamentali

Dati due insiemi $A$ e $B$ appartenenti a un insieme universo $U$:

### 1. Unione ($A \cup B$)
L'unione di $A$ e $B$ è l'insieme degli elementi che appartengono ad $A$, a $B$ o a entrambi:
$$A \cup B = \{ x \in U \mid x \in A \lor x \in B \}$$

### 2. Intersezione ($A \cap B$)
L'intersezione di $A$ e $B$ è l'insieme degli elementi che appartengono sia ad $A$ sia a $B$:
$$A \cap B = \{ x \in U \mid x \in A \land x \in B \}$$
Se $A \cap B = \emptyset$, i due insiemi si dicono **disgiunti**.

### 3. Differenza ($A \setminus B$)
La differenza tra $A$ e $B$ è l'insieme degli elementi di $A$ che non appartengono a $B$:
$$A \setminus B = \{ x \in U \mid x \in A \land x \notin B \}$$

### 4. Complementare ($A^c$ o $\bar{A}$)
Il complementare di $A$ rispetto all'universo $U$ è $U \setminus A$:
$$A^c = \{ x \in U \mid x \notin A \}$$

---

## Leggi di De Morgan

Le Leggi di De Morgan permettono di distribuire il complementare rispetto alle operazioni di unione e intersezione:
1. $(A \cup B)^c = A^c \cap B^c$
2. $(A \cap B)^c = A^c \cup B^c$

> [!EXAMPLE] Esempio pratico
> Sia $U = \{1, 2, 3, 4, 5\}$, $A = \{1, 2\}$ e $B = \{2, 3\}$.
> Calcoliamo $(A \cup B)^c$:
> - $A \cup B = \{1, 2, 3\}$.
> - $(A \cup B)^c = \{4, 5\}$.
> Calcoliamo $A^c \cap B^c$:
> - $A^c = \{3, 4, 5\}$.
> - $B^c = \{1, 4, 5\}$.
> - L'intersezione $A^c \cap B^c = \{4, 5\}$. L'uguaglianza è verificata.

---

## Insieme delle Parti $\mathcal{P}(A)$ e Prodotto Cartesiano

> [!NOTE] Insieme delle Parti (Power Set)
> L'**insieme delle parti** di $A$, indicato con $\mathcal{P}(A)$ o $2^A$, è l'insieme di tutti i sottoinsiemi di $A$, compreso l'insieme vuoto $\emptyset$ e $A$ stesso:
> $$\mathcal{P}(A) = \{ X \mid X \subseteq A \}$$
> Se la cardinalità di $A$ è $|A| = n$, allora la cardinalità dell'insieme delle parti è $|\mathcal{P}(A)| = 2^n$.

> [!NOTE] Prodotto Cartesiano
> Il **prodotto cartesiano** $A \times B$ è l'insieme di tutte le coppie ordinate $(a, b)$ formate da un elemento di $A$ e uno di $B$:
> $$A \times B = \{ (a, b) \mid a \in A \land b \in B \}$$
> La cardinalità è $|A \times B| = |A| \cdot |B|$.
> *Attenzione:* Il prodotto cartesiano non è commutativo: $A \times B \neq B \times A$.

---

## Tip d'Esame

> [!TIP] Errori Comuni da Evitare
> - **$\in$ vs $\subseteq$:** Non confondere l'appartenenza ($\in$) con l'inclusione ($\subseteq$). Un elemento $x$ appartiene ad $A$ ($x \in A$), ma un sottoinsieme $X$ è incluso in $A$ ($X \subseteq A$). Ad esempio: $1 \in \{1, 2\}$, ma $\{1\} \subseteq \{1, 2\}$.
> - **Doppia inclusione:** Nelle dimostrazioni teoriche in sede d'esame, per dimostrare che l'insieme $X = Y$, il metodo infallibile (e richiesto) è dimostrare separatamente $X \subseteq Y$ e $Y \subseteq X$.

---

## Note Correlate
- [[01.0 - MoC Insiemistica e Aritmetica|Unità 1 MoC]]
- [[Funzioni, Iniettività e Suriettività]]
- [[Relazioni Binarie e Proprietà]]
