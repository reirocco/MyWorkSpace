---
tags:
  - matematica
  - algebra/matrici
aliases:
  - Matrice Trasposta
---
# Trasposta di una Matrice

## Definizione
Sia $A = (a_{ij})$ una matrice di dimensione $m \times n$. 
La **trasposta** di $A$ è la matrice $n \times m$ denotata con $^tA$ (o a volte $A^T$), ottenuta scambiando le righe con le colonne in maniera ordinata:
$$
^tA = (a_{ji})
$$

> [!abstract] Proprietà Fondamentali
> 1. **Involuzione**: Trasporre due volte riporta alla matrice originale:
>    $$
>    ^t(^t A) = A
>    $$
> 2. **Additività**: La trasposta della somma è la somma delle trasposte:
>    $$
>    ^t(A + B) = ^tA + ^tB
>    $$
> 3. Nelle **matrici triangolari** (vedi [[Tipologie di Matrici Quadrate]]):
>    - La trasposta di un triangolare superiore è triangolare inferiore (e viceversa). 
>    - La trasposta di una matrice diagonale è la matrice stessa.

> [!info]- Dimostrazione: Additività $^t(A+B) = ^tA + ^tB$
> Per definizione della somma di matrici, $(A+B) = (a_{ij} + b_{ij})$.
> Trasponendo questa somma invertiamo gli indici:
> $$
> ^t(A+B) = (a_{ji} + b_{ji})
> $$
> Per le proprietà di separazione dei termini reali: $(a_{ji} + b_{ji}) = (a_{ji}) + (b_{ji})$.
> Poiché $(a_{ji}) = ^tA$ e $(b_{ji}) = ^tB$, otteniamo $^t(A+B) = ^tA + ^tB$.

> [!question]- Esercizio Pratico
> Data la matrice $A = \begin{pmatrix} 1 & 2 \\ 0 & 3 \\ -5 & \pi \end{pmatrix} \in M_{3,2}$.
> Calcola la sua trasposta $^tA$.
> 
> **Soluzione passo-passo:**
> 1. La matrice iniziale $A$ è $3 \times 2$. La sua trasposta sarà $2 \times 3$.
> 2. Le righe di $A$ diventano le colonne di $^tA$:
>    - 1ª riga $(1 \quad 2)$ diventa la 1ª colonna.
>    - 2ª riga $(0 \quad 3)$ diventa la 2ª colonna.
>    - 3ª riga $(-5 \quad \pi)$ diventa la 3ª colonna.
> $$
> ^tA = \begin{pmatrix} 1 & 0 & -5 \\ 2 & 3 & \pi \end{pmatrix} \in M_{2,3}
> $$

## Collegamenti
- Back: [[01 - Matrici]]
- Previous: [[Dipendenza Lineare di Matrici]]
- Next: [[Tipologie di Matrici Quadrate]]
