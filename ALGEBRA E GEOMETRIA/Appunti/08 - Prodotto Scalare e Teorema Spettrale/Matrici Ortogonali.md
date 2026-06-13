---
tags:
  - matematica
  - algebra/prodotto_scalare
aliases:
  - Matrice Ortogonale
  - Isometria
  - Gruppo O(n)
---
# Matrici Ortogonali e Isometrie

Mentre un isomorfismo generico è un'applicazione che conserva la struttura di spazio vettoriale, esiste una famiglia elitaria di applicazioni che va ben oltre: le **Isometrie**. Esse non solo preservano lo spazio, ma preservano fedelmente *l'intera geometria*, mantenendo inalterate lunghezze e angoli. Le matrici associate a queste trasformazioni (rispetto a basi ortonormali) sono le **Matrici Ortogonali**.

---

## 1. Definizione e Proprietà Fondamentali

> [!abstract] Definizione Analitica
> Una matrice quadrata $M \in M_n(\mathbb{R})$ si dice **ortogonale** se la sua trasposta coincide esattamente con la sua inversa.
> $$ M^T = M^{-1} \iff M^T \cdot M = I \iff M \cdot M^T = I $$

Questa definizione puramente algebrica nasconde un'incredibile potenza geometrica, formalizzata nel seguente teorema.

### Caratterizzazioni Equivalenti
Le seguenti affermazioni sono **totalmente equivalenti**. All'esame, provare una qualsiasi di esse significa averle provate tutte:
1. $M$ è una matrice ortogonale.
2. Le **colonne** di $M$ costituiscono una **base ortonormale** per $\mathbb{R}^n$. (Sono versori a due a due perpendicolari).
3. Le **righe** di $M$ costituiscono una **base ortonormale** per $\mathbb{R}^n$.
4. L'endomorfismo associato a $M$ è un'**Isometria**: esso conserva inalterato il prodotto scalare ($\langle Mx, My \rangle = \langle x, y \rangle$).

---

## 2. Invarianti e Determinante

Proprio perché queste matrici non possono "deformare" lo spazio, il loro determinante (che geometricamente rappresenta il fattore di scala dell'area/volume) è rigidamente vincolato.

> [!tip] Il Determinante di $M$
> Se $M$ è una matrice ortogonale, allora il suo determinante può assumere solo due valori:
> $$ \det(M) = \pm 1 $$
> 
> *Dimostrazione:* Sfruttando il Teorema di Binet:
> $M^T M = I \implies \det(M^T M) = \det(I)$
> $\det(M^T) \cdot \det(M) = 1$
> Ma poiché $\det(M^T) = \det(M)$, l'equazione diviene $[\det(M)]^2 = 1 \implies \det(M) = \pm 1$.

### Interpretazione Geometrica
La classificazione geometrica si basa proprio sul segno del determinante:
- **Se $\det(M) = +1$:** La matrice appartiene al gruppo $SO(n)$ (Gruppo Speciale Ortogonale). Rappresenta una trasformazione che conserva l'orientazione dello spazio. In $\mathbb{R}^2$ e $\mathbb{R}^3$, queste sono pure **Rotazioni**.
- **Se $\det(M) = -1$:** La matrice rappresenta una trasformazione che inverte l'orientazione dello spazio (come guardarsi allo specchio). L'esempio tipico è la **Riflessione** (eventualmente seguita da una rotazione).

---

## 3. Esempio Pratico: Rotazioni nel Piano

Nel piano $\mathbb{R}^2$, ogni matrice ortogonale con determinante $+1$ rappresenta una rotazione. La forma generale per una rotazione antioraria di angolo $\theta$ è:
$$ R_\theta = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} $$

**Verifichiamo le proprietà:**
1. *Colonne Ortonormali:* La norma della prima colonna è $\sqrt{\cos^2\theta + \sin^2\theta} = 1$. Idem per la seconda. Il loro prodotto scalare è $\cos\theta(-\sin\theta) + \sin\theta\cos\theta = 0$. Le colonne sono una base ortonormale!
2. *Trasposta uguale Inversa:* La trasposta $R_\theta^T$ inverte il segno del seno, il che geometricamente corrisponde a invertire la rotazione (ossia all'angolo $-\theta$). Essendo la rotazione inversa, coincide perfettamente con $R_\theta^{-1}$.
3. *Determinante:* $\cos^2\theta - (-\sin^2\theta) = \cos^2\theta + \sin^2\theta = 1$.

---
## Collegamenti
* **Back:** [[00_Prodotto_Scalare_MOC|MOC Prodotto Scalare]]
* **Previous:** [[Basi Ortogonali e Gram-Schmidt]]
* **Next:** [[Endomorfismi Simmetrici e Teorema Spettrale]]
