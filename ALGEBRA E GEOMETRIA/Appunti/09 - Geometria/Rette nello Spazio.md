---
tags:
  - matematica
  - geometria
aliases:
  - Retta
  - Rette sghembe
  - Rette parallele
---

# Rette nello Spazio

Una retta $r$ nello spazio $\mathbb{R}^n$ è un sottospazio affine di dimensione 1. Geometricamente, è identificata in modo univoco da un **Punto di Passaggio** ($P_0$) e da una direzione, data dal **Vettore Direttore** ($v$).

## Rappresentazioni in $\mathbb{R}^3$

### 1. Equazioni Parametriche
Esprimono i punti della retta al variare di un singolo parametro $t \in \mathbb{R}$:
$$ \begin{cases} x = x_0 + t v_x \\ y = y_0 + t v_y \\ z = z_0 + t v_z \end{cases} \iff P = P_0 + t \cdot v $$

### 2. Equazioni Cartesiane (Intersezione di Piani)
Nello spazio 3D, non esiste una singola equazione per descrivere una retta (un'equazione definisce un piano). Una retta è sempre data dall'**intersezione di due piani non paralleli**:
$$ \begin{cases} ax + by + cz + d = 0 \\ a'x + b'y + c'z + d' = 0 \end{cases} $$
Il vettore direttore di questa retta si può trovare agilmente calcolando il prodotto vettoriale tra i vettori normali dei due piani:
$$ v_r = \begin{pmatrix} a \\ b \\ c \end{pmatrix} \wedge \begin{pmatrix} a' \\ b' \\ c' \end{pmatrix} $$

## Posizione Reciproca tra Due Rette
In $\mathbb{R}^3$, due rette $r$ ed $s$ possono comportarsi in quattro modi:
1. **Incidenti**: Si intersecano in un unico punto (formano un piano).
2. **Parallele coincidenti**: Sono la stessa retta ($r=s$). Hanno lo stesso vettore direttore e punti in comune.
3. **Parallele distinte**: Hanno lo stesso vettore direttore, ma nessun punto in comune (non si intersecano, definiscono un piano).
4. **Sghembe**: L'unico caso non possibile nel piano 2D. Non hanno lo stesso vettore direttore e **non si intersecano**. (Non esiste nessun piano che le contenga entrambe).

> [!important] Rette Complanari
> Le prime 3 categorie sono **Rette Complanari**. Le rette sghembe sono l'unica categoria **Non Complanari**.

> [!tip] Da Cartesiane a Parametriche
> Per passare da cartesiane a parametriche, basta "risolvere il sistema" scegliendo una delle variabili (spesso $z$) come parametro $t$ e ricavando le altre.

## Collegamenti
- Back: [[00_Geometria_MOC|MOC Geometria]]
- Previous: [[Prodotto Vettoriale]]
- Next: [[Piani nello Spazio]]
