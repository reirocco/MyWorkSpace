---
tags:
  - matematica
  - algebra/matrici
aliases:
  - Definizione di Matrice
  - Notazione matriciale
---
# Definizione e Notazione di Matrice

> [!abstract] Cos'è una matrice?
> Una matrice $m \times n$ è una tabella di numeri reali composta da $m$ righe ed $n$ colonne.
> L'insieme delle matrici $m \times n$ aventi elementi reali viene indicato con $M_{m,n}$.

## Notazione
Una generica matrice $A \in M_{m,n}$ viene rappresentata in forma compatta come $A = (a_{ij})$, dove l'elemento $a_{ij}$ (o $(A)_{ij}$) si trova all'incrocio della **riga $i$** e della **colonna $j$**:

$$
A = \begin{pmatrix}
a_{11} & a_{12} & \dots & a_{1n} \\
a_{21} & a_{22} & \dots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \dots & a_{mn} 
\end{pmatrix}
$$

- La **riga $i$-esima** di $A$ si denota $(A)_i$.
- La **colonna $j$-esima** di $A$ si denota $(A)^j$.

Se $m = n$, la matrice è detta **quadrata** e l'insieme delle matrici quadrate di ordine $n$ si denota $M_n$. Vedi [[Tipologie di Matrici Quadrate]].

> [!tip] Trovare l'elemento
> Il primo indice indica *sempre* la riga, il secondo la colonna (Ricorda l'acronimo **RC**: Riga, Colonna).

> [!question]- Esercizio Pratico
> Data la matrice:
> $$
> A = \begin{pmatrix}
> 1 & 2 & 3 \\
> 0 & \pi & -1
> \end{pmatrix} \in M_{2,3}
> $$
> Trova $a_{22}$, $(A)_1$ e $(A)^2$.
> 
> **Soluzione passo-passo:**
> 1. L'elemento $a_{22}$ si trova nella 2ª riga, 2ª colonna: è $\pi$.
> 2. La prima riga $(A)_1$ è formata dagli elementi letti orizzontalmente: $(1, 2, 3)$.
> 3. La seconda colonna $(A)^2$ è formata dagli elementi letti verticalmente:
> $$
> \begin{pmatrix} 2 \\ \pi \end{pmatrix}
> $$

## Collegamenti
- Back: [[01 - Matrici]]
- Next: [[Operazioni su Matrici]]
