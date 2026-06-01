---
tags:
  - matematica
  - algebra/prodotto_scalare
aliases:
  - V perp
  - Proiezione Ortogonale
---

# Complemento Ortogonale

Se $V$ è un sottospazio vettoriale di $\mathbb{R}^n$, il suo **complemento ortogonale** $V^\perp$ ("$V$ perp") è l'insieme di tutti i vettori di $\mathbb{R}^n$ che sono perpendicolari a *tutti* i vettori di $V$:
$$ V^\perp = \{ w \in \mathbb{R}^n : \langle v, w \rangle = 0 \quad \forall v \in V \} $$

## Proprietà Fondamentali
1. $V^\perp$ è sempre un sottospazio vettoriale.
2. $\dim(V) + \dim(V^\perp) = n$.
3. I due spazi si "spartiscono" in modo perfetto $\mathbb{R}^n$ (sono in **somma diretta**):
   $$ V \oplus V^\perp = \mathbb{R}^n $$
   *(Il che significa che ogni vettore dello spazio si può scomporre in modo UNICO come somma di un pezzo su $V$ e un pezzo su $V^\perp$).*
4. $(V^\perp)^\perp = V$.

## Calcolo di $V^\perp$
Se conosciamo una base di generatori di $V$ (es. $v_1, \dots, v_k$), per trovare i vettori $X \in V^\perp$ basta imporre che $X$ sia ortogonale a tutti i generatori:
$$ \begin{cases} \langle v_1, X \rangle = 0 \\ \dots \\ \langle v_k, X \rangle = 0 \end{cases} $$
Questo produce esattamente un sistema lineare omogeneo in cui **le righe della matrice dei coefficienti sono i generatori di $V$**.

> [!question]- Esercizio Pratico (Heuristic)
> Data la retta $V = \text{Span}( (1, 2, -1)^T )$ in $\mathbb{R}^3$, descrivi il suo complemento ortogonale $V^\perp$.
> 
> **Soluzione passo-passo:**
> 1. $\dim(V) = 1$. Nello spazio $\mathbb{R}^3$, $\dim(V^\perp) = 3 - 1 = 2$. $V^\perp$ sarà un piano.
> 2. Imponiamo l'ortogonalità al generatore: $\langle (1, 2, -1)^T, (x, y, z)^T \rangle = 0$.
> 3. Otteniamo l'equazione: $x + 2y - z = 0$.
> 4. Questo è un piano passante per l'origine, che rappresenta geometricamente $V^\perp$.

## Collegamenti
- Back: [[00_Prodotto_Scalare_MOC|MOC Prodotto Scalare]]
- Previous: [[Prodotto Scalare e Norma]]
- Next: [[Basi Ortogonali e Gram-Schmidt]]
