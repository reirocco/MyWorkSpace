---
tags:
  - matematica
  - algebra/spazi_vettoriali
  - algebra/sistemi
aliases:
  - Sottospazio Affine
  - Varietà Affine
  - Giacitura
---
# Sottospazi Affini

Finora abbiamo visto che i sottospazi vettoriali geometrici in $\mathbb{R}^n$ devono sempre passare per l'origine (poiché contengono il vettore nullo). Cosa succede se li trasliamo? Otteniamo i **Sottospazi Affini**.

## Definizione
Sia $W \subseteq \mathbb{R}^n$ un sottospazio vettoriale e $v_0 \in \mathbb{R}^n$ un vettore (punto) fissato. 
Un sottospazio affine $L$ è l'insieme ottenuto traslando tutti i vettori di $W$ tramite $v_0$:
$$ L = v_0 + W = \{ v_0 + w : w \in W \} $$
- $v_0$ è un **punto di passaggio**.
- $W$ prende il nome di **giacitura** (o direzione) del sottospazio affine.
- La dimensione di $L$ è definita pari alla dimensione della sua giacitura $W$.

## Struttura delle Soluzioni di un Sistema Lineare
Esiste un legame profondo tra sottospazi affini e sistemi lineari non omogenei.

> [!abstract] Teorema di Struttura
> L'insieme delle soluzioni di un sistema lineare $AX = B$ compatibile è sempre un **sottospazio affine**. 
> Precisamente, l'insieme delle soluzioni è $S = v_0 + W$, dove:
> - $v_0$ è una *soluzione particolare* del sistema $AX = B$.
> - $W$ è l'insieme delle soluzioni del *sistema omogeneo associato* $AX = \mathbf{0}$ (che sappiamo essere un sottospazio vettoriale).

> [!info]- Dimostrazione
> Se $v \in S$ (è soluzione di $AX=B$), allora $A(v - v_0) = Av - Av_0 = B - B = \mathbf{0}$. Quindi $(v - v_0) \in W$. Questo prova che ogni soluzione $v$ si scrive come $v_0 + w$.
> Viceversa, se prendiamo $v_0 + w$ con $w \in W$, si ha $A(v_0 + w) = Av_0 + Aw = B + \mathbf{0} = B$. Quindi $v_0+w$ è soluzione.

> [!tip] Visione Geometrica in $\mathbb{R}^2$ e $\mathbb{R}^3$
> - **Dimensione 0**: I punti. (Soluzione unica di un sistema).
> - **Dimensione 1**: Le rette. Se passano per l'origine, sono sottospazi vettoriali. Altrimenti affini.
> - **Dimensione 2**: I piani.

## Collegamenti
- Back: [[00_Spazi_Vettoriali_MOC|MOC Spazi Vettoriali]]
- Previous: [[Equazioni Parametriche e Cartesiane]]
