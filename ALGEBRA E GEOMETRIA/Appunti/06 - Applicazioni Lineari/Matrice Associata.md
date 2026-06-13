---
tags:
  - matematica
  - algebra/applicazioni_lineari
  - algebra/matrici
aliases:
  - Matrice Associata
  - Matrice rappresentativa
  - Cambiamento di base
---
# Matrice Associata: Teoria Completa ed Esempi

L'idea fondamentale dell'Algebra Lineare è che ogni applicazione lineare tra spazi di dimensione finita può essere "tradotta" in una matrice, trasformando la geometria in puro calcolo numerico.

---

## 1. Trattazione Teorica (Calcoli Letterali per Esteso)

Sia $T: V \to W$ un'applicazione lineare.
* Sia $\mathcal{B} = (v_1, v_2, \dots, v_n)$ una base dello spazio di partenza $V$ ($\dim(V) = n$).
* Sia $\mathcal{B}' = (w_1, w_2, \dots, w_m)$ una base dello spazio di arrivo $W$ ($\dim(W) = m$).

Per costruire la matrice associata $M_{\mathcal{B}', \mathcal{B}}(T)$, calcoliamo l'immagine di ogni singolo vettore della base di partenza $\mathcal{B}$ e la esprimiamo come combinazione lineare dei vettori della base di arrivo $\mathcal{B}'$:

$$
\begin{aligned}
T(v_1) &= a_{11}w_1 + a_{21}w_2 + \dots + a_{m1}w_m \\
T(v_2) &= a_{12}w_1 + a_{22}w_2 + \dots + a_{m2}w_m \\
&\vdots \\
T(v_n) &= a_{1n}w_1 + a_{2n}w_2 + \dots + a_{mn}w_m 
\end{aligned}
$$

I coefficienti scalari $a_{ij}$ rappresentano le coordinate delle immagini. Per costruire la matrice $A$ di dimensione $m \times n$, prendiamo i coefficienti di $T(v_1)$ e li piazziamo nella **prima colonna**, quelli di $T(v_2)$ nella **seconda colonna**, e così via.

$$A = M_{\mathcal{B}', \mathcal{B}}(T) = \begin{pmatrix} 
a_{11} & a_{12} & \dots & a_{1n} \\ 
a_{21} & a_{22} & \dots & a_{2n} \\ 
\vdots & \vdots & \ddots & \vdots \\ 
a_{m1} & a_{m2} & \dots & a_{mn} 
\end{pmatrix}$$

> ⚠️ **Regola d'oro per l'esame:** Le coordinate delle immagini vanno disposte sempre in **COLONNA**.

---

## 2. Esempio 1: Da Base Canonica a Base Canonica

Consideriamo l'applicazione lineare $T: \mathbb{R}^3 \to \mathbb{R}^2$ definita da:
$$T(x, y, z) = (2x - y, x + 3z)$$

Usiamo le basi canoniche $\mathcal{E}_3 = (e_1, e_2, e_3)$ di $\mathbb{R}^3$ e $\mathcal{E}_2 = (e_1, e_2)$ di $\mathbb{R}^2$.

### Calcolo delle immagini:
* $T(e_1) = T(1, 0, 0) = (2(1) - 0, 1 + 3(0)) = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$
* $T(e_2) = T(0, 1, 0) = (2(0) - 1, 0 + 3(0)) = \begin{pmatrix} -1 \\ 0 \end{pmatrix}$
* $T(e_3) = T(0, 0, 1) = (2(0) - 0, 0 + 3(1)) = \begin{pmatrix} 0 \\ 3 \end{pmatrix}$

### Costruzione della matrice:
Disponendo i vettori ottenuti in colonna, otteniamo la matrice associata $A$:
$$A = M_{\mathcal{E}_2, \mathcal{E}_3}(T) = \begin{pmatrix} 2 & -1 & 0 \\ 1 & 0 & 3 \end{pmatrix}$$

> 💡 **Shortcut visivo:** Quando lavoriamo esclusivamente con le **basi canoniche**, la matrice si costruisce istantaneamente prendendo i coefficienti delle variabili e disponendoli **per riga**.
> * Prima riga: coefficienti di $2x - 1y + 0z \to (2, -1, 0)$
> * Seconda riga: coefficienti di $1x + 0y + 3z \to (1, 0, 3)$

---

## 3. Esempio 2: Cambio di Base (Basi non Canoniche)

Sia $T: \mathbb{R}^2 \to \mathbb{R}^2$ definita da:
$$T(x, y) = (x + y, 2x)$$

Scegliamo una base non canonica sia per la partenza che per l'arrivo: $\mathcal{B} = \mathcal{B}' = \left\{ \begin{pmatrix} 1 \\ 1 \end{pmatrix}, \begin{pmatrix} 1 \\ 0 \end{pmatrix} \right\}$. 
Chiamiamo questi vettori $v_1$ e $v_2$.

### Passo 1: Calcolare le immagini reali dei vettori di $\mathcal{B}$
* $T(v_1) = T(1, 1) = (1+1, 2(1)) = \begin{pmatrix} 2 \\ 2 \end{pmatrix}$
* $T(v_2) = T(1, 0) = (1+0, 2(1)) = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$

### Passo 2: Esprimere i risultati rispetto alla base di arrivo $\mathcal{B}'$
Dobbiamo trovare i coefficienti delle combinazioni lineari.

* **Per la prima colonna ($T(v_1)$):**
  $$\begin{pmatrix} 2 \\ 2 \end{pmatrix} = \alpha_1 \begin{pmatrix} 1 \\ 1 \end{pmatrix} + \alpha_2 \begin{pmatrix} 1 \\ 0 \end{pmatrix} \implies \begin{cases} \alpha_1 + \alpha_2 = 2 \\ \alpha_1 = 2 \end{cases} \implies \begin{cases} \alpha_1 = 2 \\ \alpha_2 = 0 \end{cases}$$
  La prima colonna è quindi: $\begin{pmatrix} 2 \\ 0 \end{pmatrix}$.

* **Per la seconda colonna ($T(v_2)$):**
  $$\begin{pmatrix} 1 \\ 2 \end{pmatrix} = \beta_1 \begin{pmatrix} 1 \\ 1 \end{pmatrix} + \beta_2 \begin{pmatrix} 1 \\ 0 \end{pmatrix} \implies \begin{cases} \beta_1 + \beta_2 = 1 \\ \beta_1 = 2 \end{cases} \implies \begin{cases} \beta_1 = 2 \\ \beta_2 = -1 \end{cases}$$
  La seconda colonna è quindi: $\begin{pmatrix} 2 \\ -1 \end{pmatrix}$.

### Matrice finale:
$$M_{\mathcal{B}, \mathcal{B}}(T) = \begin{pmatrix} 2 & 2 \\ 0 & -1 \end{pmatrix}$$

---

## 4. Teorema del Prodotto (Il "Ponte" dell'Algebra Lineare)

Il **Teorema del Prodotto** (o Teorema di Rappresentazione) è il risultato più importante di tutto l'argomento. Esso afferma che la matrice associata non è solo una tabella riassuntiva, ma un vero e proprio **motore di calcolo** che sostituisce l'applicazione lineare.

> [!abstract] Enunciato del Teorema
> Data un'applicazione lineare $T: V \to W$ e due basi $\mathcal{B}$ e $\mathcal{B}'$, per qualsiasi vettore $v \in V$ vale la formula:
> $$ [T(v)]_{\mathcal{B}'} = M_{\mathcal{B}', \mathcal{B}}(T) \cdot [v]_{\mathcal{B}} $$

**Come leggere questa formula:**
- $[v]_{\mathcal{B}}$ è il vettore colonna delle **coordinate** di $v$ nella base di partenza.
- $M_{\mathcal{B}', \mathcal{B}}(T)$ è la **matrice associata** (che agisce come operatore).
- Il simbolo $\cdot$ rappresenta l'ordinario **prodotto riga per colonna** tra matrici.
- Il risultato $[T(v)]_{\mathcal{B}'}$ è un nuovo vettore colonna, che contiene le **coordinate** dell'immagine $T(v)$ scritte rispetto alla base di arrivo.

Il teorema ci dice che possiamo "dimenticarci" dell'applicazione $T$ astratta: ci basta tradurre il vettore in coordinate, moltiplicarlo per la matrice, e tradurre il risultato indietro.

### La Verifica Numerica (su Esempio 2)

Facciamo una prova riprendendo l'**Esempio 2** con il vettore $v = \begin{pmatrix} 3 \\ 2 \end{pmatrix}$.

1. **Codifica in partenza (Troviamo $[v]_{\mathcal{B}}$):**
   Vogliamo le coordinate di $v$ rispetto alla base $\mathcal{B} = \left\{ \begin{pmatrix} 1 \\ 1 \end{pmatrix}, \begin{pmatrix} 1 \\ 0 \end{pmatrix} \right\}$:
   $$\begin{pmatrix} 3 \\ 2 \end{pmatrix} = 2\begin{pmatrix} 1 \\ 1 \end{pmatrix} + 1\begin{pmatrix} 1 \\ 0 \end{pmatrix} \implies [v]_{\mathcal{B}} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$$

2. **Il "Motore" (Prodotto riga per colonna):**
   Applichiamo il Teorema del Prodotto moltiplicando la matrice trovata per le coordinate:
   $$[T(v)]_{\mathcal{B}'} = \begin{pmatrix} 2 & 2 \\ 0 & -1 \end{pmatrix} \cdot \begin{pmatrix} 2 \\ 1 \end{pmatrix} = \begin{pmatrix} 2(2) + 2(1) \\ 0(2) + (-1)(1) \end{pmatrix} = \begin{pmatrix} 6 \\ -1 \end{pmatrix}$$

3. **Decodifica in arrivo:**
   Il risultato $\begin{pmatrix} 6 \\ -1 \end{pmatrix}$ sono le coordinate rispetto alla base di arrivo $\mathcal{B}'$. Ricostruiamo il vettore geometrico finale:
   $$6\begin{pmatrix} 1 \\ 1 \end{pmatrix} - 1\begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 6-1 \\ 6-0 \end{pmatrix} = \begin{pmatrix} 5 \\ 6 \end{pmatrix}$$

**Controprova (Verifica diretta con la formula analitica):**
Calcoliamo $T(3, 2)$ usando la regola originale della funzione $T(x, y) = (x+y, 2x)$:
$$T(3, 2) = (3+2, 2(3)) = \begin{pmatrix} 5 \\ 6 \end{pmatrix}$$

I due metodi portano allo stesso identico vettore geometrico. La struttura algebrica funziona perfettamente e il teorema è confermato!

---

## Matrice Associata e Isomorfismi (Il Significato Profondo)
La relazione tra applicazioni lineari e matrici non è solo una comodità di calcolo, ma un vero e proprio legame strutturale definito dal concetto di **Isomorfismo**.

Siano $V$ e $W$ due spazi vettoriali di dimensione finita, con $\dim(V) = n$ e $\dim(W) = m$. Fissate due basi $\mathcal{B}$ e $\mathcal{B}'$, l'operazione che associa a ogni applicazione lineare $T$ la sua matrice associata $A$ è essa stessa una funzione:

$$\Phi: \text{Hom}(V, W) \to M_{m \times n}(\mathbb{R})$$
$$\Phi(T) = M_{\mathcal{B}', \mathcal{B}}(T)$$

Questo legame $\Phi$ è un **Isomorfismo di spazi vettoriali**. Significa due cose cruciali:
1. **Conservazione delle operazioni:** Se sommi due applicazioni lineari o le moltiplichi per uno scalare, le rispettive matrici associate si sommano o si moltiplicano allo stesso modo:
   $$M_{\mathcal{B}', \mathcal{B}}(T_1 + T_2) = M_{\mathcal{B}', \mathcal{B}}(T_1) + M_{\mathcal{B}', \mathcal{B}}(T_2)$$
   $$M_{\mathcal{B}', \mathcal{B}}(k \cdot T) = k \cdot M_{\mathcal{B}', \mathcal{B}}(T)$$
2. **Identità strutturale:** Lo spazio di tutte le applicazioni lineari $\text{Hom}(V, W)$ e lo spazio delle matrici $M_{m \times n}(\mathbb{R})$ hanno la stessa identica struttura algebrica e la stessa dimensione:
   $$\dim(\text{Hom}(V, W)) = \dim(V) \cdot \dim(W) = n \cdot m$$

### Il caso delle matrici quadrate ($V = W$)
Se l'applicazione è un endomorfismo ($T: V \to V$) e usiamo la stessa base $\mathcal{B}$ in partenza e in arrivo, la matrice associata $A = M_{\mathcal{B}, \mathcal{B}}(T)$ sarà **quadrata** ($n \times n$). 

In questo contesto specifico:
* $T$ è un **Isomorfismo** (applicazione biettiva) $\iff$ La matrice associata $A$ è **[[Matrici Invertibili|Invertibile]]** ($\det(A) \neq 0$).
* In più, la composizione di applicazioni lineari corrisponde esattamente al prodotto tra matrici:
  $$M_{\mathcal{B}, \mathcal{B}}(F \circ G) = M_{\mathcal{B}, \mathcal{B}}(F) \cdot M_{\mathcal{B}, \mathcal{B}}(G)$$
---
## Collegamenti
* **Back:** [[MOC Applicazioni Lineari]]
* **Focus Successivo:** [[Matrice di Cambiamento di Base]]
* **Algoritmi Correlati:** [[Algoritmo di Eliminazione di Gauss]]