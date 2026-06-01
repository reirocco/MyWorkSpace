---
tags:
  - matematica
  - algebra/determinante
aliases:
  - Sarrus
---
# Regola di Sarrus

La **Regola di Sarrus** è uno schema pratico e veloce per calcolare il determinante esclusivamente delle matrici di **ordine 3** ($3 \times 3$).

> [!danger] Attenzione!
> Questa regola **non** è applicabile a matrici di ordine superiore ($4 \times 4, 5 \times 5, \dots$). Per quelle è necessario usare Laplace o la riduzione di Gauss.

## Procedimento
Data una matrice $A = (a_{ij}) \in M_3$, si affiancano a destra della matrice le sue prime due colonne:

$$
\begin{vmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33} 
\end{vmatrix}
\begin{matrix}
a_{11} & a_{12} \\
a_{21} & a_{22} \\
a_{31} & a_{32} 
\end{matrix}
$$

Il determinante si ottiene sommando i prodotti delle tre diagonali principali (da sinistra a destra, scendendo) e sottraendo i prodotti delle tre diagonali secondarie (da destra a sinistra, scendendo):

$$
\det A = (a_{11}a_{22}a_{33} + a_{12}a_{23}a_{31} + a_{13}a_{21}a_{32}) - (a_{13}a_{22}a_{31} + a_{11}a_{23}a_{32} + a_{12}a_{21}a_{33})
$$

> [!question]- Esercizio Pratico
> Calcola il determinante di $A = \begin{pmatrix} 3 & 1 & -1 \\ 0 & 2 & 1 \\ -1 & 0 & -1 \end{pmatrix}$ usando Sarrus.
> 
> **Soluzione passo-passo:**
> 1. Affianchiamo le prime due colonne:
>    $3 \quad 1 \quad -1 \quad | \quad 3 \quad 1$
>    $0 \quad 2 \quad 1 \quad | \quad 0 \quad 2$
>    $-1 \quad 0 \quad -1 \quad | \quad -1 \quad 0$
> 2. Prodotti "positivi" (scendendo a destra):
>    - $3 \cdot 2 \cdot (-1) = -6$
>    - $1 \cdot 1 \cdot (-1) = -1$
>    - $(-1) \cdot 0 \cdot 0 = 0$
>    - Somma: $-6 - 1 + 0 = -7$
> 3. Prodotti "negativi" (scendendo a sinistra):
>    - $(-1) \cdot 2 \cdot (-1) = 2$
>    - $3 \cdot 1 \cdot 0 = 0$
>    - $1 \cdot 0 \cdot (-1) = 0$
>    - Somma: $2 + 0 + 0 = 2$
> 4. Risultato: $(-7) - (2) = -9$.

## Collegamenti
- Back: [[00_Determinante_Rango_MOC|MOC Determinante e Rango]]
- Previous: [[Definizione di Determinante e Sviluppo di Laplace]]
