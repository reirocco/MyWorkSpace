---
tags:
  - matematica
  - algebra/determinante
aliases:
  - Binet
  - Inversa con cofattori
  - Matrice aggiunta
---
# Teorema di Binet e Inversa con Cofattori

Questi teoremi collegano il determinante al prodotto di matrici e al calcolo esplicito dell'inversa.

## Teorema di Binet
Siano $A, B \in M_n$ matrici quadrate dello stesso ordine. Allora il determinante del prodotto è uguale al prodotto dei determinanti:
$$ \det(AB) = \det(A) \cdot \det(B) $$

> [!tip] Conseguenza per l'Inversa
> Se $A$ è invertibile, allora $AA^{-1} = I$. Applicando Binet:
> $\det(A) \cdot \det(A^{-1}) = \det(I) = 1 \implies \det(A^{-1}) = \frac{1}{\det A}$
> Questo conferma che una matrice è invertibile **se e solo se** $\det A \neq 0$.

## Formula dell'Inversa (tramite Cofattori)
Se $\det A \neq 0$, la matrice inversa $A^{-1}$ può essere calcolata tramite la **matrice dei cofattori** (o aggiunta):
$$ A^{-1} = \frac{1}{\det A} \cdot ^t(\text{Cof } A) $$
Dove $(\text{Cof } A)$ è la matrice formata dai cofattori $C_{ij} = (-1)^{i+j} \det A_{ij}$.

> [!important] Caso $2 \times 2$ (Formula Rapida)
> Se $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, allora $A^{-1} = \frac{1}{ad-bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$.

> [!info]- Dimostrazione: $\det(A^{-1}) = 1/\det A$
> 1. Partiamo dalla definizione di inversa: $A \cdot A^{-1} = I_n$.
> 2. Applichiamo il determinante a entrambi i membri: $\det(A \cdot A^{-1}) = \det(I_n)$.
> 3. Per il Teorema di Binet: $\det(A) \cdot \det(A^{-1}) = 1$.
> 4. Poiché $1 \neq 0$, deve essere $\det A \neq 0$ e possiamo dividere: $\det(A^{-1}) = \frac{1}{\det A}$.

> [!info]- Dimostrazione: Formula per l'Inversa
> Supponiamo che $A$ sia invertibile, allora $\det A \neq 0$. Sarà sufficiente esibire che la matrice dichiarata moltiplicata per $A = (a_{ij})$ restituisce la matrice identità.
> L'elemento in posizione $(i, j)$ del prodotto di $A$ per la matrice dell'inversa $B = \frac{1}{\det(A)} \, ^t(\text{Cof } A)$ è dato da:
> $$ \frac{1}{\det A} \sum_{r=1}^{n} a_{ir} (-1)^{j+r} \det(A_{jr}) $$
> Se $i = j$, la somma corrisponde esattamente allo sviluppo di Laplace per calcolare il $\det A$ rispetto alla riga $i$-esima, quindi il numeratore è $\det A$. Diviso per $\det A$ restituisce $1$.
> Se $i \neq j$, la somma corrisponde allo sviluppo di Laplace del determinante di una matrice in cui la riga $j$-esima è stata sostituita con la riga $i$-esima (due righe uguali). Il risultato è quindi $0$ (per le proprietà del determinante).
> Pertanto, il prodotto è esattamente la matrice Identità.

## Collegamenti
- Back: [[00_Determinante_Rango_MOC|MOC Determinante e Rango]]
- Previous: [[Calcolo del Determinante con Metodo di Gauss]]
