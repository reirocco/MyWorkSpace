---
tags:
  - matematica
  - algebra/applicazioni_lineari
aliases:
  - Isomorfismo
  - Isomorfi
  - Applicazione Biiettiva
---
# Isomorfismi: Il "Trasporto Perfetto" in Algebra Lineare

In algebra lineare, non tutte le applicazioni lineari sono uguali. Alcune "schiacciano" lo spazio (perdendo informazioni), altre lo "espandono", e altre ancora lo conservano perfettamente. Un **Isomorfismo** è la forma più perfetta di applicazione lineare: esso conserva totalmente la struttura dello spazio di partenza in quello di arrivo.

---

## 1. Definizione Formale

Siano $V$ e $W$ due spazi vettoriali.
Un'applicazione lineare $T: V \to W$ si definice **Isomorfismo** se è **biiettiva**, ovvero contemporaneamente:
1. **Iniettiva:** Manda vettori distinti in immagini distinte ($\ker(T) = \{\mathbf{0}_V\}$).
2. **Suriettiva:** Ricopre interamente lo spazio di arrivo ($\text{Im}(T) = W$).

Se esiste almeno un isomorfismo tra due spazi $V$ e $W$, si dice che i due spazi sono **isomorfi** (scritto $V \cong W$). 
Dal punto di vista puramente algebrico, due spazi isomorfi sono **indistinguibili**: hanno identica struttura e dimensione, differiscono unicamente per la natura o il "nome" dei loro elementi (es. polinomi vs vettori di coordinate).

> [!important] Proprietà Inversa
> Se $T: V \to W$ è un isomorfismo, allora l'applicazione inversa $T^{-1}: W \to V$ è garantita esistere ed è **anch'essa un'applicazione lineare** (e quindi un isomorfismo).

---

## 2. Caratterizzazione e Basi (Il Teorema Fondamentale)

Gli isomorfismi mantengono intatte le proprietà di dipendenza e indipendenza lineare.

> [!abstract] Isomorfismi e Vettori
> Sia $T: V \to W$ un isomorfismo e siano $v_1, \dots, v_k \in V$. Allora:
> - $v_1, \dots, v_k$ sono **linearmente indipendenti** $\iff$ $T(v_1), \dots, T(v_k)$ sono **linearmente indipendenti**.
> - $v_1, \dots, v_k$ **generano** $V$ $\iff$ $T(v_1), \dots, T(v_k)$ **generano** $W$.
> - $\{v_1, \dots, v_k\}$ è una **base** di $V$ $\iff$ $\{T(v_1), \dots, T(v_k)\}$ è una **base** di $W$.

### Conseguenze Sulla Dimensione
Il corollario diretto è che **due spazi vettoriali (di dimensione finita) sono isomorfi se e solo se hanno la stessa dimensione**.
$$ V \cong W \iff \dim(V) = \dim(W) $$

Questo è il motivo per cui l'applicazione delle coordinate $F_\mathcal{B}: V \to \mathbb{R}^n$ è un isomorfismo: qualsiasi spazio vettoriale reale di dimensione $n$ è "una fotocopia" di $\mathbb{R}^n$.

---

## 3. Matrice Associata e Isomorfismi

Siano $V$ e $W$ spazi di dimensione finita $n$. Fissiamo una base $\mathcal{B}$ in $V$ e $\mathcal{B}'$ in $W$.
Sia $A = M_{\mathcal{B}', \mathcal{B}}(T)$ la matrice associata a un'applicazione lineare $T: V \to W$.

Essendo $\dim(V) = \dim(W) = n$, la matrice $A$ è una **matrice quadrata** di ordine $n$.

> [!tip] Criterio Pratico (Da Esame)
> L'applicazione lineare $T$ è un **Isomorfismo** se e solo se la sua matrice associata $A$ è **invertibile**.
> Operativamente, questo significa verificare che:
> $$ \det(A) \neq 0 $$
> Se $\det(A) = 0$, l'applicazione ha un nucleo non banale (non è iniettiva) e non ricopre tutto l'arrivo (non è suriettiva).

### Esempio Pratico

Consideriamo $T: \mathbb{R}^2 \to \mathbb{R}^2$ tale che $T(x,y) = (x+y, x-y)$.
La matrice associata rispetto alle basi canoniche è:
$$ A = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} $$
Calcoliamo il determinante: $\det(A) = (1)(-1) - (1)(1) = -1 - 1 = -2$.
Poiché $\det(A) = -2 \neq 0$, la matrice è invertibile, quindi $T$ è un **isomorfismo** (è una biiezione di $\mathbb{R}^2$ in sé).

---

## Collegamenti
* **Back:** [[00_Applicazioni_Lineari_MOC|MOC Applicazioni Lineari]]
* **Previous:** [[Definizione di Applicazione Lineare]]
* **Focus Successivo:** [[Matrice Associata]]
* **Algoritmi Relativi:** [[Matrice di Cambiamento di Base]]
