---
tags:
  - matematica
  - algebra/determinante
aliases:
  - Determinante Gauss
  - Riduzione triangolare
---
# Calcolo del Determinante con Metodo di Gauss

Il metodo di Gauss (o eliminazione di Gauss) permette di trasformare una matrice $A$ in una matrice **triangolare superiore** $T$ tramite operazioni elementari.

## Algoritmo
Poiché sappiamo che per una matrice triangolare il determinante è il prodotto degli elementi diagonali, l'obiettivo è azzerare gli elementi sotto la diagonale.

1. **Scambio di righe:** Ogni volta che scambi due righe, devi moltiplicare il determinante per $-1$.
2. **Sostituzione ($R_i \to R_i + \lambda R_j$):** Questa operazione **non cambia** il valore del determinante.
3. **Moltiplicazione per scalare ($R_i \to \lambda R_i$):** Questa operazione moltiplica il determinante per $\lambda$. (Di solito evitata se possibile, o se ne tiene traccia dividendo alla fine).

$$ \det A = (-1)^s \cdot \det T = (-1)^s \prod t_{ii} $$
Dove $s$ è il numero di scambi effettuati.

> [!abstract] Quale tecnica scegliere?
> | Matrice | Tecnica Consigliata |
> | --- | --- |
> | $2 \times 2$ | Formula diretta $ad-bc$ |
> | $3 \times 3$ | Sarrus o Laplace (se ci sono zeri) |
> | $n \times n$ (con $n \ge 4$) | **Metodo di Gauss** per creare zeri + Laplace |

> [!question]- Esercizio Pratico
> Calcola $\det \begin{pmatrix} 1 & 2 & 5 \\ 3 & 2 & 8 \\ -1 & 6 & 7 \end{pmatrix}$ usando Gauss.
> 
> **Soluzione passo-passo:**
> 1. Fissiamo la prima riga e azzeriamo sotto il pivot $a_{11}=1$:
>    - $R_2 \to R_2 - 3R_1: \begin{pmatrix} 1 & 2 & 5 \\ 0 & -4 & -7 \\ -1 & 6 & 7 \end{pmatrix}$
>    - $R_3 \to R_3 + R_1: \begin{pmatrix} 1 & 2 & 5 \\ 0 & -4 & -7 \\ 0 & 8 & 12 \end{pmatrix}$
> 2. Azzeriamo sotto il secondo pivot $a_{22}=-4$:
>    - $R_3 \to R_3 + 2R_2: \begin{pmatrix} 1 & 2 & 5 \\ 0 & -4 & -7 \\ 0 & 0 & -2 \end{pmatrix}$
> 3. La matrice è ora triangolare superiore. Il determinante è il prodotto della diagonale:
>    - $\det = 1 \cdot (-4) \cdot (-2) = 8$.

## Collegamenti
- Back: [[00_Determinante_Rango_MOC|MOC Determinante e Rango]]
- Previous: [[Proprietà del Determinante]]
