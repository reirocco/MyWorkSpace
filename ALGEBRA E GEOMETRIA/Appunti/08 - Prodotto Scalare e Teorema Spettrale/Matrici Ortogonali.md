---
tags:
  - matematica
  - algebra/prodotto_scalare
aliases:
  - Matrice Ortogonale
  - Gruppo O(n)
---

# Matrici Ortogonali

Le **matrici ortogonali** sono le matrici associate ai cambiamenti tra basi ortonormali. Rappresentano trasformazioni rigide dello spazio che non deformano gli oggetti, non ne cambiano la lunghezza e non alterano gli angoli (come rotazioni e riflessioni).

## Definizione e Caratterizzazioni
Una matrice quadrata $M \in M_n$ si dice **ortogonale** se la sua inversa coincide con la sua trasposta:
$$ M^{-1} = M^T \iff M^T M = I $$

Questa definizione algebrica ha conseguenze geometriche fortissime. Le seguenti affermazioni sono del tutto **equivalenti**:
1. $M$ è una matrice ortogonale.
2. Le **colonne** di $M$ formano una base **ortonormale** di $\mathbb{R}^n$ (hanno norma 1 e sono a due a due perpendicolari).
3. Le **righe** di $M$ formano una base **ortonormale** di $\mathbb{R}^n$.

## Proprietà
1. **Determinante**: Se $M$ è ortogonale, $\det(M) = \pm 1$. (Perché $\det(M^T M) = \det(M)\det(M) = \det(I) = 1$).
   - Se $\det=1$, la matrice rappresenta una **rotazione**.
   - Se $\det=-1$, la matrice rappresenta una **riflessione** (unita a un'eventuale rotazione).
2. Il prodotto di due matrici ortogonali è ancora una matrice ortogonale.

> [!question]- Esercizio Pratico
> Come appare la generica matrice ortogonale $2 \times 2$ di rotazione?
> 
> **Soluzione:**
> Le matrici $2 \times 2$ con determinante 1 che sono ortogonali hanno sempre la forma:
> $$ R_\theta = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} $$
> Questo ruota il piano in senso antiorario di un angolo $\theta$.

## Collegamenti
- Back: [[00_Prodotto_Scalare_MOC|MOC Prodotto Scalare]]
- Previous: [[Basi Ortogonali e Gram-Schmidt]]
- Next: [[Endomorfismi Simmetrici e Teorema Spettrale]]
