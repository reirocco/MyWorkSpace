---
tags:
  - matematica
  - algebra/rango
  - algebra/gauss
aliases:
  - Matrice a scala
  - Pivot
---
# Matrici a Scala e Pivot

Le **matrici a scala** (o a gradini) sono una particolare forma di matrici che semplifica enormemente il calcolo del rango e la risoluzione di sistemi lineari.

## Definizione
Una matrice $A$ si dice **a scala** se:
1. Le eventuali righe nulle si trovano tutte in fondo alla matrice.
2. Sotto il primo elemento non nullo di ogni riga (e sotto tutti gli zeri che lo precedono), ci sono solo zeri.

> [!abstract] Cos'è un Pivot?
> Il **pivot** è il primo elemento diverso da zero di ogni riga non nulla in una matrice a scala.

## Teorema del Rango (Matrici a Scala)
Per una matrice a scala, il rango è estremamente facile da calcolare:
**Il rango di una matrice a scala è uguale al numero dei suoi pivot** (ovvero al numero delle sue righe non nulle).

> [!info]- Dimostrazione
> Si consideri il minore di $A$ individuato dalle colonne in cui cadono i pivot e dalle righe corrispondenti (le righe non nulle). Questa è una matrice quadrata di ordine pari al numero di pivot. Tale sottomatrice è triangolare superiore e i suoi elementi sulla diagonale sono proprio i pivot (che sono diversi da zero). Quindi il suo determinante, essendo il prodotto degli elementi diagonali, è diverso da zero.
> D'altro canto, tutti gli orlati di questo minore hanno determinante zero, perché qualsiasi riga che andremmo ad aggiungere sarebbe una riga nulla (essendo le righe sottostanti tutte nulle). 
> Per il Teorema degli Orlati, il rango di $A$ è esattamente l'ordine di questo minore, ovvero il numero di pivot.

> [!question]- Esercizio Pratico
> Determina il rango della seguente matrice:
> $$
> A = \begin{pmatrix} 1 & 2 & 3 & 0 \\ 0 & 0 & 5 & -1 \\ 0 & 0 & 0 & 0 \end{pmatrix}
> $$
> 
> **Soluzione passo-passo:**
> 1. Verifichiamo se è a scala:
>    - Riga 1: pivot 1 in colonna 1. Sotto il pivot ci sono solo zeri.
>    - Riga 2: pivot 5 in colonna 3. Sotto il pivot c'è uno zero.
>    - Riga 3: riga nulla.
>    La matrice è a scala.
> 2. Contiamo i pivot: ce ne sono 2 (il numero 1 e il numero 5).
> 3. Conclusione: $\text{rk} A = 2$.

## Collegamenti
- Back: [[00_Determinante_Rango_MOC|MOC Determinante e Rango]]
- Next: [[Algoritmo di Eliminazione di Gauss]]
