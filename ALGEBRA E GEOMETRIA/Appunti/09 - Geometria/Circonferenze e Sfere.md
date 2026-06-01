---
tags:
  - matematica
  - geometria
aliases:
  - Ipersfera
  - Sfera
  - Circonferenza
---

# Circonferenze e Sfere

La Geometria Analitica non si ferma alle entità piatte (rette e piani). L'oggetto non lineare più semplice è il luogo dei punti equidistanti da un centro.

## La Sfera in $\mathbb{R}^3$
Una sfera (o superficie sferica) $\mathcal{S}$ di centro $C(x_c, y_c, z_c)$ e raggio $r \ge 0$ ha equazione cartesiana base derivante dal teorema di Pitagora:
$$ (x - x_c)^2 + (y - y_c)^2 + (z - z_c)^2 = r^2 $$

Svolgendo i quadrati, l'equazione generica assume la forma:
$$ x^2 + y^2 + z^2 + ax + by + cz + d = 0 $$
Da questa forma sviluppata possiamo estrarre centro e raggio:
- **Centro**: $C = (-\frac{a}{2}, -\frac{b}{2}, -\frac{c}{2})$
- **Raggio**: $r = \sqrt{\frac{a^2}{4} + \frac{b^2}{4} + \frac{c^2}{4} - d}$
> *Affinché rappresenti una sfera reale, il contenuto della radice deve essere $\ge 0$.*

## La Circonferenza in $\mathbb{R}^2$ e $\mathbb{R}^3$
In $\mathbb{R}^2$, la formula è identica, basta rimuovere la variabile $z$. 
In $\mathbb{R}^3$, una **circonferenza** non ha una sua equazione indipendente. Geometricamente, una circonferenza nello spazio è l'intersezione tra una Sfera e un Piano. La sua equazione è un sistema:
$$ \begin{cases} x^2 + y^2 + z^2 + ax + by + cz + d = 0 & \text{(Sfera)} \\ \alpha x + \beta y + \gamma z + \delta = 0 & \text{(Piano)} \end{cases} $$

## Intersezione Sfera - Piano
Sia $\mathcal{S}$ una sfera di centro $C$ e raggio $r$, e $\alpha$ un piano. Chiamiamo $d = \text{dist}(C, \alpha)$.
1. Se $d > r$: L'intersezione è vuota (piano esterno).
2. Se $d = r$: L'intersezione è un singolo punto (piano tangente).
3. Se $d < r$: L'intersezione è una circonferenza.

> [!tip] Raggio e Centro della Circonferenza
> Se il piano taglia la sfera individuando una circonferenza, il centro di tale circonferenza è la proiezione ortogonale del centro della sfera $C$ sul piano. Il raggio $R_{circ}$ si trova col Teorema di Pitagora: $R_{circ} = \sqrt{r^2 - d^2}$.

## Collegamenti
- Back: [[00_Geometria_MOC|MOC Geometria]]
- Previous: [[Piani nello Spazio]]
