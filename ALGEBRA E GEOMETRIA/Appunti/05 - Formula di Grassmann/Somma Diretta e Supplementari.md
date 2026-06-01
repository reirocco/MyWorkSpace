---
tags:
  - matematica
  - algebra/spazi_vettoriali
aliases:
  - Somma Diretta
  - Sottospazi Supplementari
---
# Somma Diretta e Supplementari

## Somma Diretta
Due sottospazi $U$ e $W$ di $V$ sono in **somma diretta** se la loro intersezione contiene solo il vettore nullo:
$$ U \cap W = \{ \mathbf{0}_V \} $$
In questo caso, la somma si denota con $U \oplus W$.

> [!tip] Conseguenza per Grassmann
> Se $U \oplus W$, la dimensione dell'intersezione è 0, quindi Grassmann si riduce a:
> $\dim(U \oplus W) = \dim(U) + \dim(W)$.

## Sottospazi Supplementari
Se inoltre $U \oplus W = V$ (cioè la loro somma diretta genera tutto lo spazio), allora $U$ e $W$ si dicono **sottospazi supplementari**. In tal caso:
$$ \dim(U) + \dim(W) = \dim(V) $$

Un supplementare di un dato sottospazio esiste sempre, ma **non è mai unico** (esistono infiniti piani che sono supplementari a una determinata retta in $\mathbb{R}^3$).
Per trovare un supplementare, basta prendere una base di $U$ e "completarla" a base di $V$. I vettori aggiunti genereranno un supplementare di $U$.

> [!info]- Dimostrazione: Unicità della scomposizione in somma diretta
> **Teorema**: $U, W$ sono supplementari $\iff$ ogni vettore $v \in V$ si scrive in modo **unico** come $v = u + w$ con $u \in U$ e $w \in W$.
> **Dimostrazione**: L'esistenza della scrittura è garantita da $U+W=V$. Per l'unicità, supponiamo di avere $v = u_1 + w_1$ e $v = u_2 + w_2$. 
> Uguagliando: $u_1 + w_1 = u_2 + w_2 \implies u_1 - u_2 = w_2 - w_1$.
> Il termine a sinistra sta in $U$, quello a destra sta in $W$. Essendo uguali, questo elemento sta in $U \cap W$.
> Ma $U \cap W = \{\mathbf{0}_V\}$. Dunque $u_1 - u_2 = \mathbf{0} \implies u_1 = u_2$ e $w_2 - w_1 = \mathbf{0} \implies w_1 = w_2$. La scrittura è unica.

## Collegamenti
- Back: [[00_Grassmann_MOC|MOC Formula di Grassmann]]
- Previous: [[Formula di Grassmann]]
