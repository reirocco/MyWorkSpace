---
tags:
  - matematica
  - geometria
aliases:
  - Prodotto Vettore
  - Regola della Mano Destra
---

# Prodotto Vettoriale

Mentre il prodotto scalare restituisce un numero, in $\mathbb{R}^3$ esiste un'operazione speciale che prende due vettori e ne restituisce un **terzo vettore**: il prodotto vettoriale ($v \wedge w$ o $v \times w$).

## Definizione e Calcolo
Si definisce tramite un finto determinante (sviluppato lungo la prima riga) che ha come prima riga i versori fondamentali $\vec{i}, \vec{j}, \vec{k}$:
$$ v \wedge w = \det \begin{pmatrix} \vec{i} & \vec{j} & \vec{k} \\ v_x & v_y & v_z \\ w_x & w_y & w_z \end{pmatrix} = \begin{pmatrix} v_y w_z - v_z w_y \\ - (v_x w_z - v_z w_x) \\ v_x w_y - v_y w_x \end{pmatrix} $$

## Proprietà Fondamentali
1. **Ortogonalità**: Il vettore risultante $v \wedge w$ è **perpendicolare** sia a $v$ che a $w$.
2. **Modulo e Aree**: La lunghezza del vettore risultante è pari all'**area del parallelogramma** formato da $v$ e $w$:
   $$ \| v \wedge w \| = \|v\| \cdot \|w\| \cdot |\sin\theta| $$
   *(Conseguenza: l'area del triangolo individuato dai vettori è $\frac{1}{2} \| v \wedge w \|$)*.
3. **Antisimmetria**: $v \wedge w = - (w \wedge v)$.
4. **Vettori Paralleli**: $v \wedge w = \mathbf{0} \iff v, w$ sono proporzionali (paralleli).
5. **Regola della Mano Destra**: Pollice su $v$, indice su $w$, il medio indica il verso di $v \wedge w$.

> [!tip] Trovare il Vettore Normale
> Il prodotto vettoriale è il metodo più rapido per trovare l'equazione di un piano passante per 3 punti. 
> 1. Crea i due vettori lati $\vec{AB}$ e $\vec{AC}$.
> 2. Calcola $\vec{AB} \wedge \vec{AC}$. Questo ti dà direttamente $(a,b,c)$, il vettore normale del piano.
> 3. Scrivi l'equazione $ax + by + cz + d = 0$ e trova $d$ imponendo il passaggio per $A$.

> [!question]- Esercizio Pratico
> Trova l'area del triangolo di vertici $A(1,0,0)$, $B(0,1,0)$, $C(0,0,1)$.
> 
> **Soluzione passo-passo:**
> 1. Vettori lati: $\vec{AB} = (-1, 1, 0)^T$, $\vec{AC} = (-1, 0, 1)^T$.
> 2. Prodotto vettoriale $\vec{AB} \wedge \vec{AC} = \det \begin{pmatrix} i & j & k \\ -1 & 1 & 0 \\ -1 & 0 & 1 \end{pmatrix} = (1, 1, 1)^T$.
> 3. Norma del prodotto: $\| (1,1,1)^T \| = \sqrt{1^2 + 1^2 + 1^2} = \sqrt{3}$.
> 4. Area triangolo = $\frac{1}{2} \sqrt{3}$.

## Collegamenti
- Back: [[00_Geometria_MOC|MOC Geometria]]
- Previous: [[Punti e Distanze]]
- Next: [[Rette nello Spazio]]
