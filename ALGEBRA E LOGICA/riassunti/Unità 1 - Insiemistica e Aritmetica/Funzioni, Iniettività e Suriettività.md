---
tags:
  - funzioni
  - iniettivita
  - suriettivita
  - biettivita
  - algebra
type: atomic
unit: 1
---
# Funzioni, Iniettività e Suriettività

Una **funzione** (o applicazione) $f$ da un insieme $A$ (dominio) a un insieme $B$ (codominio), indicata con $f: A \rightarrow B$, è una relazione che ad ogni elemento $x \in A$ associa uno ed un solo elemento $y = f(x) \in B$.

---

## Proprietà Fondamentali delle Funzioni

### 1. Iniettività (Nessuna sovrapposizione)
Una funzione $f: A \rightarrow B$ si dice **iniettiva** se elementi distinti del dominio hanno immagini distinte nel codominio:
$$\forall x_1, x_2 \in A, \quad f(x_1) = f(x_2) \implies x_1 = x_2$$
*(Equivalentemente: $x_1 \neq x_2 \implies f(x_1) \neq f(x_2)$)*.

### 2. Suriettività (Copertura totale)
Una funzione $f: A \rightarrow B$ si dice **suriettiva** se ogni elemento del codominio $B$ è immagine di almeno un elemento del dominio $A$:
$$\forall y \in B, \quad \exists x \in A \text{ tale che } f(x) = y$$
ovvero l'immagine della funzione coincide con l'intero codominio: $\text{Im}(f) = B$.

### 3. Biettività (Corrispondenza Biunivoca)
Una funzione $f: A \rightarrow B$ si dice **biettiva** (o **biunivoca**) se è sia iniettiva che suriettiva:
$$\forall y \in B, \quad \exists! x \in A \text{ tale che } f(x) = y$$

> [!EXAMPLE] Esempio Analitico
> Sia $f: \mathbb{R} \rightarrow \mathbb{R}$ con $f(x) = x^2$.
> - **Iniettiva?** No, perché $f(2) = f(-2) = 4$, ma $2 \neq -2$.
> - **Suriettiva?** No, perché non esiste $x \in \mathbb{R}$ tale che $x^2 = -1$ (cioè $\text{Im}(f) \neq \mathbb{R}$).
> Tuttavia, definendo $g: [0, +\infty) \rightarrow [0, +\infty)$ con $g(x) = x^2$, la funzione diventa **biettiva**.

---

## Composizione di Funzioni e Inversa

> [!NOTE] Composizione di Funzioni
> Date due funzioni $f: A \rightarrow B$ e $g: B \rightarrow C$, la **funzione composta** $(g \circ f): A \rightarrow C$ è definita da:
> $$(g \circ f)(x) = g(f(x)) \quad \forall x \in A$$

**Proprietà della composizione:**
- L'operazione non è commutativa: $(f \circ g) \neq (g \circ f)$.
- Se $f$ e $g$ sono iniettive $\implies (g \circ f)$ è iniettiva.
- Se $f$ e $g$ sono suriettive $\implies (g \circ f)$ è suriettiva.

> [!NOTE] Funzione Inversa
> Una funzione $f: A \rightarrow B$ ammette una **funzione inversa** $f^{-1}: B \rightarrow A$ se e solo se $f$ è **biettiva**.
> La funzione inversa soddisfa le relazioni identiche:
> $$(f^{-1} \circ f) = \text{id}_A \quad \text{e} \quad (f \circ f^{-1}) = \text{id}_B$$

---

## Tip d'Esame

> [!TIP] Strategia di Risoluzione
> - **Per dimostrare l'Iniettività:** Imponi sempre $f(x_1) = f(x_2)$ in forma algebrica e risolvi i passaggi matematici finché non ottieni l'unica soluzione possibile $x_1 = x_2$.
> - **Per dimostrare la Suriettività:** Scrivi l'equazione $y = f(x)$, assumi $y$ come parametro generico del codominio e cerca di ricavare $x$. Se trovi un $x$ (appartenente al dominio!) dipendente da $y$ per cui la relazione sussiste senza limitazioni per alcun $y$, la funzione è suriettiva.

---

## Note Correlate
- [[01.0 - MoC Insiemistica e Aritmetica|Unità 1 MoC]]
- [[Insiemi e Operazioni Insiemistiche]]
- [[Omomorfismi ed Isomorfismi di Gruppi]]
