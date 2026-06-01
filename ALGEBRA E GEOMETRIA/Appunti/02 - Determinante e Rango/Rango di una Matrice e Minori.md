---
tags:
  - matematica
  - algebra/rango
aliases:
  - Definizione di Rango
  - Rango
  - Minore di una matrice
---
# Rango di una Matrice e Minori

Il **rango** di una matrice $A \in M_{m,n}$ è un numero intero che misura la "qualità" dell'informazione contenuta nella matrice, ovvero il numero massimo di righe (o colonne) linearmente indipendenti.

## Definizione via Minori
Sia $A \in M_{m,n}$. 
- Un **minore** di ordine $k$ è il determinante di una sottomatrice quadrata $k \times k$ ottenuta intersecando $k$ righe e $k$ colonne di $A$.
- Il **Rango** di $A$, indicato con $\text{rk}(A)$ o $\text{rg}(A)$, è l'**ordine massimo** di un minore con determinante diverso da zero.

> [!abstract] Proprietà Fondamentali
> 1. **Range del Rango** - Se $A \in M_{m,n}$, allora $0 \le \text{rk}(A) \le \min(m, n)$.
> 2. **Matrice nulla** - $\text{rk}(A) = 0 \iff A = \mathbf{0}_{v}$.
> 3. **Invarianza della trasposta** - $\text{rk}(A) = \text{rk}(^tA)$.
> 4. **Rango massimo** - Per una matrice quadrata $A \in M_n$, $\text{rk}(A) = n \iff \det A \neq 0$. In questo caso la matrice si dice **a rango massimo** o non singolare.

> [!info]- Dimostrazione (Proprietà del Rango)
> - **(1)** Segue dal fatto che il più grande minore possibile per una matrice $m \times n$ è determinato dal lato più corto, quindi ha ordine al più $\min(m,n)$.
> - **(2)** Se $A=0$, il rango è 0 per definizione. Se $\text{rg}(A)=0$, significa che non esiste nemmeno un minore di ordine 1 (che è semplicemente un singolo elemento) diverso da zero. Quindi tutti gli elementi sono $0 \implies A=0$.
> - **(3)** Segue dalla proprietà $\det(^t M) = \det(M)$. I minori non nulli restano non nulli se si traspone la matrice.
> - **(4)** Se $\text{rg}(A)=n$, esiste un minore di ordine $n$ non nullo. Poiché l'unico minore di ordine $n$ di $A$ è $A$ stessa, $\det(A) \neq 0$. Viceversa, se $\det(A) \neq 0$, la definizione assicura $\text{rg}(A) \ge n$, e per la prop 1 è al più $n$, quindi $\text{rg}(A) = n$.

> [!question]- Esercizio Pratico (Calcolo tramite minori)
> Determina il rango di $A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix} \in M_{2,3}$.
> 
> **Soluzione passo-passo:**
> 1. Il rango massimo possibile è $\min(2, 3) = 2$.
> 2. Cerchiamo un minore di ordine 2 con $\det \neq 0$.
>    Consideriamo le prime due colonne: $\begin{vmatrix} 1 & 2 \\ 4 & 5 \end{vmatrix} = 1\cdot 5 - 2\cdot 4 = 5-8 = -3$.
> 3. Poiché abbiamo trovato almeno un minore $2 \times 2$ con determinante non nullo, $\text{rk}(A) = 2$.

## Collegamenti
- Back: [[00_Determinante_Rango_MOC|MOC Determinante e Rango]]
- Next: [[Teorema degli Orlati]]
