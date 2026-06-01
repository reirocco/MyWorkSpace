# Il Ruolo della Matrice Associata come Operatore

In algebra lineare, la **matrice associata** a un'applicazione lineare $T: V \to W$ non è solo una rappresentazione statica, ma un vero e proprio strumento di calcolo. Una volta determinata rispetto a due basi (o alla stessa base in caso di endomorfismi), permette di calcolare l'immagine di qualsiasi vettore tramite una semplice operazione algebrica.

[[6. APPLICAZIONI LINEARI.pdf#page=14]]
---

## 1. La Formula Fondamentale

Sia $T: V \to W$ un'applicazione lineare, $\mathcal{B}$ una base di $V$ e $\mathcal{C}$ una base di $W$. Se $A$ è la matrice associata a $T$ rispetto alle basi $\mathcal{B}$ e $\mathcal{C}$, allora per ogni vettore $v \in V$ vale la relazione:

$$[T(v)]_{\mathcal{C}} = A \cdot [v]_{\mathcal{B}}$$

### Legenda:
* $[v]_{\mathcal{B}}$: Vettore colonna delle **coordinate** di $v$ rispetto alla base di partenza $\mathcal{B}$.
* $A$: Matrice associata (dimensioni $m \times n$).
* $[T(v)]_{\mathcal{C}}$: Vettore colonna delle **coordinate** del risultato rispetto alla base di arrivo $\mathcal{C}$.

---

## 2. Flusso di Lavoro (Workflow)

Per ricavare $T(v)$ per un nuovo vettore $v$ utilizzando la matrice, segui questi passaggi:

1.  **Coordinate di input:** Esprimi $v$ come combinazione lineare della base di partenza $\mathcal{B}$ per trovare i coefficienti (le coordinate).
2.  **Moltiplicazione:** Esegui il prodotto matrice-vettore $A \times \text{coordinate}$.
3.  **Interpretazione:** Il risultato ottenuto sono coefficienti. Per ottenere il "vettore finale", moltiplica questi coefficienti per i vettori della base di arrivo $\mathcal{C}$.



---

## 3. Esempio Pratico

Supponiamo di avere un endomorfismo $T: \mathbb{R}^2 \to \mathbb{R}^2$ con matrice associata rispetto alla base $\mathcal{B} = \{v_1, v_2\}$:
$$A = \begin{pmatrix} 2 & 1 \\ 0 & -1 \end{pmatrix}$$

Se vogliamo calcolare $T(v)$ per un vettore che ha coordinate $[v]_{\mathcal{B}} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$:

1.  Moltiplichiamo: 
    $$\begin{pmatrix} 2 & 1 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} 3 \\ 4 \end{pmatrix} = \begin{pmatrix} (2\cdot3 + 1\cdot4) \\ (0\cdot3 + (-1)\cdot4) \end{pmatrix} = \begin{pmatrix} 10 \\ -4 \end{pmatrix}$$
2.  Il risultato $[T(v)]_{\mathcal{B}} = \begin{pmatrix} 10 \\ -4 \end{pmatrix}$ significa che:
    $$T(v) = 10v_1 - 4v_2$$

---

## 4. Perché è così importante?

* **Efficienza:** Non serve ricalcolare la funzione $T$ da zero. La matrice "contiene" già tutta l'informazione necessaria.
* **Astrazione:** Permette di trattare oggetti complessi (polinomi, matrici, funzioni) come semplici colonne di numeri.
* **Isomorfismo:** Conferma che ogni applicazione lineare tra spazi di dimensione finita è essenzialmente una moltiplicazione matrice-vettore.

> **Nota Bene:** Ricorda sempre che la matrice lavora sulle **coordinate**, non direttamente sui componenti dei vettori, a meno che tu non stia lavorando esclusivamente con le **basi canoniche**.