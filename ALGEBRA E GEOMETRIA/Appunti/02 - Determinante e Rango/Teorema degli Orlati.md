---
tags:
  - matematica
  - algebra/rango
aliases:
  - Orlati
  - Criterio di Kronecker
---
# Teorema degli Orlati

Il **Teorema degli Orlati** (o Criterio di Kronecker) fornisce un metodo efficiente per calcolare il rango evitando di dover controllare tutti i possibili minori della matrice.

## Definizione di Orlato
Dato un minore $M$ di ordine $k$ di una matrice $A$, un **orlato** di $M$ è un minore di ordine $k+1$ ottenuto aggiungendo a $M$ una riga e una colonna di $A$ che non erano già in $M$.

## Il Teorema
Sia $A \in M_{m,n}$. Il rango di $A$ è pari a $k$ **se e solo se**:
1. Esiste un minore $M$ di ordine $k$ con $\det M \neq 0$.
2. **Tutti** i possibili orlati di $M$ di ordine $k+1$ hanno determinante nullo (o non esistono).

> [!tip] Vantaggio Algoritmico
> Se trovi un minore $k \times k$ non nullo, non devi controllare *tutti* i minori di ordine $k+1$, ma solo quelli che contengono quel minore specifico. Se sono tutti zero, hai finito: il rango è $k$.

> [!question]- Esercizio Pratico
> Calcola il rango di $A = \begin{pmatrix} -1 & 0 & 2 & 3 \\ 1 & 0 & -2 & -3 \end{pmatrix}$.
> 
> **Soluzione passo-passo:**
> 1. Cerchiamo un minore $1 \times 1$ non nullo: $M = (-1) \implies \det M = -1 \neq 0$. Quindi $\text{rk} A \ge 1$.
> 2. Controlliamo gli orlati di ordine 2 che includono $(-1)$:
>    - Orlato con colonna 2: $\begin{vmatrix} -1 & 0 \\ 1 & 0 \end{vmatrix} = 0$.
>    - Orlato con colonna 3: $\begin{vmatrix} -1 & 2 \\ 1 & -2 \end{vmatrix} = 2 - 2 = 0$.
>    - Orlato con colonna 4: $\begin{vmatrix} -1 & 3 \\ 1 & -3 \end{vmatrix} = 3 - 3 = 0$.
> 3. Poiché tutti gli orlati del minore $M$ sono nulli, per il Teorema degli Orlati, $\text{rk} A = 1$.

## Collegamenti
- Back: [[00_Determinante_Rango_MOC|MOC Determinante e Rango]]
- Previous: [[Rango di una Matrice e Minori]]
