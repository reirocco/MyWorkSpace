---
tags:
  - matematica
  - algebra/determinante
aliases:
  - Teoremi del determinante
---
# Proprietà del Determinante

Il determinante gode di numerose proprietà che permettono di semplificarne il calcolo drasticamente. Sia $A \in M_n$:

## Le 8 Proprietà Fondamentali

1. **Matrici Triangolari:** Se $A$ è triangolare (sup. o inf.) o diagonale, il determinante è il **prodotto degli elementi sulla diagonale**: $\det A = \prod a_{ii}$.
2. **Identità:** $\det I_n = 1$.
3. **Trasposta:** $\det A = \det(^tA)$.
4. **Righe/Colonne Nulle:** Se $A$ ha una riga o una colonna interamente nulla, $\det A = 0$.
5. **Linearità (per riga):** Se moltiplichiamo una riga per $\lambda$, il determinante risulta moltiplicato per $\lambda$. $\det(A') = \lambda \det A$.
   > [!danger] Errore Tipico
   > $\det(\lambda A) = \lambda^n \det A$, perché moltiplicare la matrice per $\lambda$ significa moltiplicare *tutte* le $n$ righe per $\lambda$.
6. **Invarianza per Somma:** Il determinante **non cambia** se sommiamo a una riga il multiplo di un'altra riga ($R_i \to R_i + \lambda R_j$).
7. **Righe/Colonne Dipendenti:** Se $A$ ha due righe (o colonne) uguali o proporzionali (L.D.), allora $\det A = 0$.
8. **Scambio di Righe:** Se scambiamo due righe (o due colonne), il determinante **cambia segno**.

> [!tip] Heuristics d'Esame
> Usa la proprietà (6) per creare degli zeri in una riga/colonna e poi applica lo [[Definizione di Determinante e Sviluppo di Laplace|Sviluppo di Laplace]]. Questa è la strategia standard per matrici $4 \times 4$ o superiori.

> [!info]- Dimostrazione: Proprietà (1) - Matrici Triangolari
> Sviluppiamo il determinante rispetto alla prima colonna (dove c'è solo $a_{11}$ e poi zeri).
> Otteniamo $a_{11} \cdot \det(A_{11})$. Ma $A_{11}$ è anch'essa triangolare! Sviluppando di nuovo otteniamo $a_{11} \cdot a_{22} \cdot \det(A_{11,22})$ e così via, fino a esaurire la matrice. Il risultato è il prodotto sulla diagonale.

> [!info]- Dimostrazione: Proprietà (8) - Scambio di due righe
> Si dimostra per induzione che se scambiamo due righe, la matrice $J$ di scambio ha $\det = -1$.
> Per $2 \times 2$, se scambiamo le due righe di $I_2$ otteniamo $\det \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = (0\cdot 0) - (1\cdot 1) = -1$.
> Per $n>2$, espandendo rispetto a una riga non scambiata, il minore ricade nel caso $n-1$, preservando il $-1$. Essendo $B = JA$, per Binet $\det(B) = \det(J)\det(A) = -1 \cdot \det(A) = -\det(A)$.

> [!info]- Dimostrazione: Proprietà (6) - Invarianza per somma
> Supponiamo che $B$ sia ottenuta da $A$ sommando alla riga $r$ un multiplo della riga $s$.
> Sviluppiamo $\det B$ lungo la riga $r$: gli elementi sono $a_{rk} + c \cdot a_{sk}$.
> $\det B = \sum (-1)^{r+k} (a_{rk} + c \cdot a_{sk}) \det(A_{rk})$.
> Separando la somma in due, la prima parte ridà $\det A$. La seconda parte è $c \cdot \det(\text{matrice con due righe } s \text{ uguali})$. Poiché una matrice con due righe uguali ha det nullo, la seconda parte è $0$. Quindi $\det B = \det A$.

## Collegamenti
- Back: [[00_Determinante_Rango_MOC|MOC Determinante e Rango]]
- Next: [[Calcolo del Determinante con Metodo di Gauss]]
