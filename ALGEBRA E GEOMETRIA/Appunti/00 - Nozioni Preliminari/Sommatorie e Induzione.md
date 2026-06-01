---
tags:
  - matematica
  - algebra/preliminari
aliases:
  - Sommatoria
  - Principio di Induzione
---
# Sommatorie e Principio di Induzione

## Sommatorie
Il simbolo $\sum$ viene utilizzato per abbreviare una somma di molti (o infiniti) termini:
$$ \sum_{i=1}^{n} a_i = a_1 + a_2 + \dots + a_n $$
La variabile $i$ è "muta" (scompare a somma calcolata).

## Principio di Induzione
È uno strumento potentissimo per dimostrare che una certa proprietà $P(n)$ è vera **per tutti** i numeri naturali $n \in \mathbb{N}$.

> [!abstract] Come applicare l'Induzione
> 1. **Passo Base**: Dimostrare che $P(0)$ (o $P(1)$) è vera.
> 2. **Passo Induttivo**: Assumere che $P(n)$ sia vera (Ipotesi Induttiva) e **dimostrare** che da questo consegue necessariamente che $P(n+1)$ è vera.
> Se si completano entrambi i passi, il principio garantisce che $P(n)$ vale per ogni $n$.

> [!info]- Dimostrazione per Induzione (Somma dei primi $n$ numeri)
> Dimostriamo che $\sum_{i=0}^{n} i = \frac{n(n+1)}{2}$.
> **Passo Base ($n=0$):** $0 = \frac{0(1)}{2} = 0$. (Vero)
> **Passo Induttivo:** Assumiamo vero per $n$. Calcoliamo per $n+1$:
> $$ \sum_{i=0}^{n+1} i = \left(\sum_{i=0}^{n} i\right) + (n+1) $$
> Usando l'ipotesi induttiva, sostituiamo la sommatoria:
> $$ = \frac{n(n+1)}{2} + (n+1) = \frac{n(n+1) + 2(n+1)}{2} = \frac{(n+1)(n+2)}{2} $$
> Che è esattamente la formula cercata valutata in $n+1$. La tesi è dimostrata!

## Collegamenti
- Back: [[00_Nozioni_Preliminari_MOC|MOC Nozioni Preliminari]]
- Previous: [[Polinomi e Radici]]
- Next: [[Combinatoria]]
