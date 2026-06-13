---
tags:
  - matematica
  - algebra/prodotto_scalare
aliases:
  - V perp
  - Proiezione Ortogonale
  - Ortogonale di un Sottospazio
---
# Complemento Ortogonale ($V^\perp$)

Nello studio della geometria lineare, quando si definisce un "pavimento" (un sottospazio), sorge spontaneamente l'esigenza di definire una "verticale" che sia perfettamente perpendicolare a tutto il pavimento. Questo è il ruolo del **Complemento Ortogonale**.

---

## 1. Definizione Formale

Sia $V$ un sottospazio vettoriale di $\mathbb{R}^n$.
Il **Complemento Ortogonale** di $V$, denotato con $V^\perp$ ("$V$ perp"), è l'insieme di tutti i vettori di $\mathbb{R}^n$ che risultano ortogonali a **tutti** i vettori di $V$.

> [!abstract] Definizione Analitica
> $$ V^\perp = \{ w \in \mathbb{R}^n : \langle v, w \rangle = 0 \quad \forall v \in V \} $$

* **Esempio Intuitivo:** Nello spazio tridimensionale $\mathbb{R}^3$, se $V$ è un piano passante per l'origine, il suo complemento ortogonale $V^\perp$ è l'unica retta perpendicolare al piano e passante per l'origine.

---

## 2. Proprietà Fondamentali (Teoremi Strutturali)

Il complemento ortogonale possiede proprietà geometriche formidabili che dividono in modo perfetto lo spazio euclideo.

1. **Struttura di Sottospazio:** $V^\perp$ è sempre, garantitamente, un sottospazio vettoriale di $\mathbb{R}^n$.
2. **Equazione Dimensionale:** Le dimensioni dei due spazi si integrano per formare lo spazio intero:
   $$ \dim(V) + \dim(V^\perp) = n $$
3. **Somma Diretta Ortogonale (Decomposizione):**
   I due spazi hanno in comune *solo e soltanto* il vettore nullo ($V \cap V^\perp = \{\mathbf{0}\}$). Insieme, essi formano l'intero spazio euclideo.
   $$ \mathbb{R}^n = V \oplus V^\perp $$
   *Significato Pratico:* Qualsiasi vettore $x \in \mathbb{R}^n$ può essere smontato e scritto in modo **UNICO** come la somma di due pezzi: $x = x_V + x_{V^\perp}$, dove $x_V$ è la **proiezione ortogonale** di $x$ su $V$.
4. **Riflessività:** L'ortogonale dell'ortogonale ci riporta al punto di partenza.
   $$ (V^\perp)^\perp = V $$

---

## 3. Calcolo Pratico (L'Algoritmo da Esame)

Per calcolare il complemento ortogonale di uno spazio, la definizione richiede che il vettore incognito sia ortogonale a *infiniti* vettori. Per nostra fortuna, l'algebra lineare semplifica il tutto grazie al concetto di base.

> [!tip] Teorema Operativo
> Affinché un vettore $w$ sia ortogonale a tutto lo spazio $V$, è sufficiente e necessario che esso sia ortogonale ai **soli generatori** di $V$.

**Procedura Step-by-Step:**
Supponiamo di avere $V = \text{Span}(v_1, v_2, \dots, v_k)$.
Vogliamo trovare l'equazione (o la base) di $V^\perp$.
1. Prendiamo un generico vettore $X = (x_1, x_2, \dots, x_n)^T$.
2. Imponiamo che il prodotto scalare di $X$ con ciascuno dei generatori sia zero:
   $$ \begin{cases} \langle v_1, X \rangle = 0 \\ \langle v_2, X \rangle = 0 \\ \dots \\ \langle v_k, X \rangle = 0 \end{cases} $$
3. Questo costruisce automaticamente un **Sistema Lineare Omogeneo** dove i coefficienti delle equazioni sono esattamente le componenti dei vettori $v_i$. In forma matriciale: $A \cdot X = \mathbf{0}$, dove le righe di $A$ sono i vettori generatori di $V$.
4. Le soluzioni di questo sistema (il Ker della matrice $A$) costituiscono l'autospazio $V^\perp$. Risolvendo il sistema si ottiene una base del complemento ortogonale.

---

### Esercizio Esempio
Data la retta $V = \text{Span}\left( \begin{pmatrix} 1 \\ 2 \\ -1 \end{pmatrix} \right)$ in $\mathbb{R}^3$, descrivi il suo complemento ortogonale $V^\perp$.

**Soluzione:**
1. Dimensione: $\dim(V) = 1$. Nello spazio $\mathbb{R}^3$, avremo $\dim(V^\perp) = 3 - 1 = 2$. Ci aspettiamo un piano.
2. Impostiamo il sistema: $\langle (1, 2, -1)^T, (x, y, z)^T \rangle = 0$.
3. Espandiamo il prodotto scalare: $1x + 2y - 1z = 0$.
4. **L'equazione cartesiana di $V^\perp$** è esattamente $x + 2y - z = 0$, che rappresenta un piano passante per l'origine.

---
## Collegamenti
* **Back:** [[00_Prodotto_Scalare_MOC|MOC Prodotto Scalare]]
* **Previous:** [[Prodotto Scalare e Norma]]
* **Next:** [[Basi Ortogonali e Gram-Schmidt]]
