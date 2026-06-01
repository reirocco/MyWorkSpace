---
tags:
  - matematica
  - algebra/prodotto_scalare
aliases:
  - Prodotto Scalare
  - Norma Euclidea
  - Ortogonali
---

# Prodotto Scalare e Norma

Il prodotto scalare in $\mathbb{R}^n$ è l'operazione che permette di misurare lunghezze e angoli. 

## Definizione e Proprietà
Dati $v, w \in \mathbb{R}^n$, il **prodotto scalare standard** è:
$$ \langle v, w \rangle = v^T w = v_1 w_1 + v_2 w_2 + \dots + v_n w_n $$
(Notare che il risultato è un *numero scalare*, non un vettore).

Godé di 4 proprietà fondamentali:
1. **Bilineare**: È lineare rispetto a entrambi i vettori.
2. **Simmetrico**: $\langle v, w \rangle = \langle w, v \rangle$.
3. **Definito Positivo**: $\langle v, v \rangle \ge 0$ e fa $0 \iff v = \mathbf{0}$.
4. **Non Degenere**: L'unico vettore ortogonale a tutti è lo zero.

## Norma (Lunghezza)
La lunghezza di un vettore è data dalla radice del suo prodotto scalare con se stesso:
$$ \|v\| = \sqrt{\langle v, v \rangle} = \sqrt{v_1^2 + \dots + v_n^2} $$
- Un vettore si dice **Versore** se ha norma $1$.
- Per "normalizzare" un vettore (portarlo a norma 1 mantenendo la direzione), lo si divide per la sua norma: $\frac{v}{\|v\|}$.

> [!abstract] Disuguaglianze Notevoli
> - **Cauchy-Schwarz**: $|\langle v, w \rangle| \le \|v\| \cdot \|w\|$
> - **Triangolare**: $\|v + w\| \le \|v\| + \|w\|$ (in un triangolo, un lato è minore della somma degli altri due).

## Ortogonalità e Angolo
Due vettori sono **ortogonali (o perpendicolari)** ($v \perp w$) se e solo se:
$$ \langle v, w \rangle = 0 $$
In generale, l'angolo $\theta$ tra due vettori non nulli si calcola con:
$$ \cos(\theta) = \frac{\langle v, w \rangle}{\|v\| \cdot \|w\|} $$

## Collegamenti
- Back: [[00_Prodotto_Scalare_MOC|MOC Prodotto Scalare]]
- Next: [[Complemento Ortogonale]]
