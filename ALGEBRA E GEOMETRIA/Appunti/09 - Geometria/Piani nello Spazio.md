---
tags:
  - matematica
  - geometria
aliases:
  - Piano
  - Vettore normale
---

# Piani nello Spazio

Un piano $\alpha$ in $\mathbb{R}^3$ è un sottospazio affine di dimensione 2. È univocamente identificato da un punto di passaggio $P_0$ e da due direzioni indipendenti (i vettori direttori $v$ e $w$). 

In alternativa, un modo molto più potente per descriverlo è usare un punto di passaggio e una "direzione negata", ovvero il **Vettore Normale** ($\mathbf{n}$), che è perpendicolare al piano.

## Rappresentazioni

### 1. Equazione Cartesiana
È una singola equazione lineare in 3 variabili:
$$ \alpha: ax + by + cz + d = 0 $$
Il vettore normale del piano si estrae guardando i coefficienti di $x, y, z$:
$$ \mathbf{n}_\alpha = \begin{pmatrix} a \\ b \\ c \end{pmatrix} $$

### 2. Equazioni Parametriche
Usano due parametri (ad es. $t, s$) per descrivere l'intera superficie del piano partendo da $P_0$ e muovendosi lungo due vettori $v, w$:
$$ \begin{cases} x = x_0 + t v_x + s w_x \\ y = y_0 + t v_y + s w_y \\ z = z_0 + t v_z + s w_z \end{cases} $$

## Posizioni Reciproche
- **Piani Paralleli**: Due piani sono paralleli se i loro vettori normali sono proporzionali. L'equazione sarà uguale a meno del termine noto $d$.
- **Piani Perpendicolari**: Due piani sono ortogonali se i loro vettori normali lo sono ($\langle \mathbf{n}_\alpha, \mathbf{n}_\beta \rangle = 0$).
- **Retta e Piano Paralleli**: Una retta con vettore direttore $v$ è parallela al piano se non lo buca, cioè se scorre ortogonalmente al vettore normale del piano ($\langle v, \mathbf{n}_\alpha \rangle = 0$).
- **Retta e Piano Perpendicolari**: Una retta è perpendicolare al piano se "buca a piombo", ovvero il suo vettore direttore è proporzionale al vettore normale del piano.

## Fasci di Piani (Heuristics)
Se una retta è data come intersezione di due piani ($P_1 = 0, P_2 = 0$), qualsiasi piano che contenga quella retta avrà un'equazione che è combinazione lineare di $P_1$ e $P_2$:
$$ P_1 + k \cdot P_2 = 0 $$
Questa tecnica è formidabile per trovare il piano passante per una retta e per un altro punto $Q$ (basta sostituire $Q$ nel fascio per trovare $k$).

## Collegamenti
- Back: [[00_Geometria_MOC|MOC Geometria]]
- Previous: [[Rette nello Spazio]]
- Next: [[Circonferenze e Sfere]]
