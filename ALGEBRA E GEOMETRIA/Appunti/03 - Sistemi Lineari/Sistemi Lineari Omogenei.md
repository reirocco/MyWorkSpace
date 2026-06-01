---
tags:
  - matematica
  - algebra/sistemi
aliases:
  - Sistema omogeneo
---
# Sistemi Lineari Omogenei

Un sistema lineare si dice **omogeneo** se tutti i termini noti sono nulli. La sua forma matriciale è:
$$ AX = \mathbf{0} $$

## Proprietà Fondamentali
1. **Sempre compatibile:** Un sistema omogeneo ammette sempre almeno la **soluzione banale** $X = (0, 0, \dots, 0)^T$. Infatti $\text{rk } A = \text{rk } (A|0)$ è sempre vero.
2. **Spazio delle soluzioni:** L'insieme delle soluzioni di un sistema omogeneo forma un sottospazio vettoriale (vedrai in [[04 - Spazi Vettoriali]]).
3. **Soluzioni non banali:** Il sistema ammette soluzioni diverse da quella nulla se e solo se $\text{rk } A < n$ (dove $n$ è il numero di incognite). Se il sistema è quadrato, questo equivale a dire $\det A = 0$.

> [!question]- Esercizio Pratico
> Per quali valori di $k$ il sistema omogeneo ha soluzioni non banali?
> $$ \begin{pmatrix} 2 & 1 \\ k & 2 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} $$
> 
> **Soluzione passo-passo:**
> 1. Il sistema ha soluzioni non banali se e solo se il determinante della matrice incompleta è zero.
> 2. $\det A = 2\cdot 2 - 1\cdot k = 4 - k$.
> 3. Poniamo $4 - k = 0 \implies k = 4$.
> 4. Se $k=4$, il sistema ha $\infty^{2-1} = \infty^1$ soluzioni del tipo $2x + y = 0 \implies y = -2x$.

## Collegamenti
- Back: [[00_Sistemi_Lineari_MOC|MOC Sistemi Lineari]]
- Previous: [[Teorema di Rouché-Capelli]]
