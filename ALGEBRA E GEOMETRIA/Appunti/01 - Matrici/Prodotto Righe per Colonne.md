---
tags:
  - matematica
  - algebra/matrici
aliases:
  - Moltiplicazione tra matrici
  - Prodotto Righe per Colonne
---
# Prodotto Righe per Colonne

Siano $A \in M_{m,n}$ e $B \in M_{n,p}$. Il **prodotto righe per colonne** $C = AB$ è una matrice in $M_{m,p}$ il cui elemento in riga $i$ e colonna $j$ ($c_{ij}$) è ottenuto moltiplicando scalarmente la riga $i$-esima di $A$ con la colonna $j$-esima di $B$:

$$
c_{ij} = (A)_i \cdot (B)^j = \sum_{k=1}^{n} a_{ik} b_{kj}
$$

> [!danger] Condizione Necessaria (FONDAMENTALE)
> Il prodotto $AB$ è eseguibile **solo se** il numero di *colonnne* della prima matrice ($A$) è uguale al numero di *righe* della seconda matrice ($B$). 
> *Taglia:* $(m \times n) \times (n \times p) \implies (m \times p)$

## Proprietà del Prodotto
Per tutte le matrici per cui i prodotti sono definiti e per scalari $\lambda \in \mathbb{R}$:
1. **Associativa**: $(AB)C = A(BC)$
2. **Distributiva**: $(A+B)C = AC + BC$ e $A(B+C) = AB + AC$
3. **Molt. per scalare**: $\lambda(AB) = (\lambda A)B = A(\lambda B)$
4. **Elemento neutro**: $I_n$ (matrice identità) tale che $A I_n = A$ e $I_m A = A$
5. **Trasposta del prodotto**: $^t(AB) = ^tB ^tA$

> [!info]- Dimostrazione: Trasposta del Prodotto $^t(AB) = ^tB ^tA$
> Per definizione di matrice trasposta, l'elemento in posizione $(i,j)$ di $^tB$ è $b_{ji}$ e per $^tA$ è $a_{ji}$.
> Dalla definizione di prodotto tra matrici, l'elemento alla riga $i$ e colonna $j$ di $^tB ^tA$ è:
> $$ \sum_{r=1}^{n} (^tB)_{ir} (^tA)_{rj} = \sum_{r=1}^{n} b_{ri} a_{jr} $$
> Per la commutatività del prodotto tra numeri reali, questo è uguale a:
> $$ \sum_{r=1}^{n} a_{jr} b_{ri} $$
> Che è esattamente l'elemento in riga $j$ e colonna $i$ di $AB$, ovvero l'elemento in riga $i$ e colonna $j$ di $^t(AB)$.

> [!danger] Il Prodotto NON è Commutativo
> In generale, **$AB \neq BA$**.
> Esistono eccezioni in cui le matrici *commutano* (es. se una è multiplo della matrice identità, come $A(\lambda I) = (\lambda I)A$), ma la regola generale dice che l'ordine conta!

> [!question]- Esercizio Pratico
> Date:
> $A = \begin{pmatrix} -1 & 0 \\ 3 & 1 \end{pmatrix} \in M_{2,2}$ e $B = \begin{pmatrix} 0 & 1 & 2 \\ -1 & 0 & -2 \end{pmatrix} \in M_{2,3}$
> Calcolare se possibile $AB$ e $BA$.
> 
> **Soluzione passo-passo:**
> 1. Analisi Taglie: $A$ è $2 \times 2$, $B$ è $2 \times 3$.
>    - Prodotto $AB$: le taglie sono compatibili $(2 \times 2) \cdot (2 \times 3)$. Risultato in $2 \times 3$.
>    - Prodotto $BA$: taglie $(2 \times 3) \cdot (2 \times 2)$. Numero colonne di $B$ (3) diverso dalle righe di $A$ (2). Il prodotto **non è definito**.
> 2. Calcolo $AB$: 
>    - Riga 1 colonna 1: $(-1 \cdot 0) + (0 \cdot -1) = 0$
>    - Riga 1 colonna 2: $(-1 \cdot 1) + (0 \cdot 0) = -1$
>    - Riga 1 colonna 3: $(-1 \cdot 2) + (0 \cdot -2) = -2$
>    - Riga 2 colonna 1: $(3 \cdot 0) + (1 \cdot -1) = -1$
>    - Riga 2 colonna 2: $(3 \cdot 1) + (1 \cdot 0) = 3$
>    - Riga 2 colonna 3: $(3 \cdot 2) + (1 \cdot -2) = 6 - 2 = 4$
> $$
> AB = \begin{pmatrix} 0 & -1 & -2 \\ -1 & 3 & 4 \end{pmatrix}
> $$

## Collegamenti
- Back: [[01 - Matrici]]
- Previous: [[Tipologie di Matrici Quadrate]]
- Next: [[Matrici Invertibili]]
