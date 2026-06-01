---
tags:
  - matematica
  - geometria
aliases:
  - Punto Medio
  - Baricentro
  - Distanza punto retta
  - Distanza punto piano
---

# Punti e Distanze

In uno spazio $\mathbb{R}^n$ dotato di sistema di riferimento cartesiano ortonormale, un punto $P$ è identificato dalle sue coordinate vettoriali.

## Punti Notevoli
Siano $P_1, P_2, \dots, P_k$ punti in $\mathbb{R}^n$:
- **Punto Medio** (di un segmento $P_1P_2$): $M = \frac{P_1 + P_2}{2}$
- **Baricentro** (di un poligono con $k$ vertici): $G = \frac{P_1 + P_2 + \dots + P_k}{k}$

## Distanza tra Due Punti
Applicando il Teorema di Pitagora sulle coordinate, la distanza è la norma euclidea della differenza vettoriale:
$$ d(P_1, P_2) = \|P_2 - P_1\| = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2 + (z_2-z_1)^2} $$

## Distanza tra un Punto e un Iperpiano
Se abbiamo un iperpiano $\alpha: ax_1 + bx_2 + \dots + c = 0$ e un punto $P_0(x_0, y_0, \dots)$, la distanza minima dal punto all'iperpiano è:
$$ d(P_0, \alpha) = \frac{|a x_0 + b y_0 + \dots + c|}{\sqrt{a^2 + b^2 + \dots}} $$
> *Questa formula vale per la distanza **Punto-Retta in $\mathbb{R}^2$** e **Punto-Piano in $\mathbb{R}^3$**.*

> [!info]- Dimostrazione concettuale (Proiezione)
> La distanza è la lunghezza del segmento $P_0 H$, dove $H$ è la proiezione ortogonale di $P_0$ sull'iperpiano. Il vettore $\vec{P_0H}$ è parallelo al vettore normale dell'iperpiano $\mathbf{n} = (a,b,\dots)^T$.

## Distanze nello Spazio $\mathbb{R}^3$
- **Distanza Punto-Retta in $\mathbb{R}^3$**: Non c'è una formuletta semplice. Bisogna prendere il punto $P_0$, costruire il piano $\alpha$ perpendicolare alla retta $r$ passante per $P_0$. Trovare l'intersezione $H = r \cap \alpha$. Infine calcolare $d(P_0, H)$. In alternativa, usando il prodotto vettoriale: $d(P_0, r) = \frac{\|(P_1-P_0) \wedge v\|}{\|v\|}$ dove $P_1 \in r$ e $v$ è il vettore direttore.
- **Distanza tra Rette Sghembe**: Trova un piano $\alpha$ che contiene una retta ed è parallelo all'altra. Calcola la distanza tra la seconda retta e il piano $\alpha$.

## Collegamenti
- Back: [[00_Geometria_MOC|MOC Geometria]]
- Next: [[Prodotto Vettoriale]]
