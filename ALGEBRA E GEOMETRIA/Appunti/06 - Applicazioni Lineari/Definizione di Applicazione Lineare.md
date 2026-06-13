---
tags:
  - matematica
  - algebra/applicazioni_lineari
aliases:
  - Funzione Lineare
  - Omomorfismo
  - Linearità
  - Applicazione Lineare
---
# Definizione di Applicazione Lineare: Teoria ed Esempi

Le applicazioni lineari (o trasformazioni lineari) sono il cuore pulsante dell'Algebra Lineare. Esse sono funzioni tra spazi vettoriali che preservano la struttura fondamentale degli spazi stessi: la somma tra vettori e il prodotto per uno scalare.

---

## 1. Trattazione Teorica (Definizione Formale)

Siano $V$ e $W$ due spazi vettoriali costruiti sullo stesso campo (ad esempio, $\mathbb{R}$).
Una funzione $T: V \to W$ si dice **applicazione lineare** se e solo se soddisfa i seguenti due assiomi fondamentali per ogni scelta di vettori e scalari:

1. **Additività (o conservazione della somma):** 
   $$T(v_1 + v_2) = T(v_1) + T(v_2) \quad \forall v_1, v_2 \in V$$
2. **Omogeneità (o conservazione del prodotto per scalare):** 
   $$T(\lambda \cdot v) = \lambda \cdot T(v) \quad \forall v \in V, \forall \lambda \in \mathbb{R}$$

Queste due proprietà possono essere unificate in un'unica equazione che rappresenta il **principio di conservazione delle combinazioni lineari**:
$$ T(\lambda_1 v_1 + \lambda_2 v_2) = \lambda_1 T(v_1) + \lambda_2 T(v_2) $$

> [!important] Conseguenza Diretta: L'origine va nell'origine
> Un'applicazione lineare mappa **sempre** il vettore nullo del dominio nel vettore nullo del codominio:
> $$ T(\mathbf{0}_V) = \mathbf{0}_W $$
> **Dimostrazione:** Sfruttando l'omogeneità con $\lambda = 0$, otteniamo $T(\mathbf{0}_V) = T(0 \cdot v) = 0 \cdot T(v) = \mathbf{0}_W$.
> Se un esercizio ti presenta una funzione (come $T(x) = x + 3$) dove $T(\mathbf{0}) \neq \mathbf{0}$, puoi concludere *immediatamente* che **non è lineare**.

---

## 2. Determinazione di un'Applicazione Lineare

Un principio straordinario dell'Algebra Lineare afferma che un'applicazione lineare è **univocamente determinata** dai valori che assume su una base del dominio. 

> [!abstract] Teorema di Esistenza e Unicità
> Siano $V$ e $W$ spazi vettoriali. Fissata una base $\mathcal{B} = \{v_1, v_2, \dots, v_n\}$ di $V$ e scelti $n$ vettori **qualsiasi** $\{w_1, w_2, \dots, w_n\}$ in $W$, **esiste un'unica** applicazione lineare $T: V \to W$ tale che:
> $$ T(v_i) = w_i \quad \forall i = 1, \dots, n $$
> 
> **Dimostrazione:** Dato un qualunque $v \in V$, esso si scrive in modo unico come $v = \alpha_1 v_1 + \dots + \alpha_n v_n$. Per la linearità, l'unica definizione possibile di $T(v)$ è $\alpha_1 w_1 + \dots + \alpha_n w_n$. Questo dimostra sia l'esistenza che l'unicità della funzione.

---

## 3. Esempi e Controesempi

### Esempio 1: Applicazione Lineare Standard in $\mathbb{R}^n$
Consideriamo $T: \mathbb{R}^3 \to \mathbb{R}^2$ definita da:
$$ T \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} x_1 - x_2 \\ 2x_2 + x_3 \end{pmatrix} $$
Questa è un'applicazione lineare. Le sue componenti sono polinomi omogenei di primo grado nelle variabili del dominio.

### Esempio 2 (Controesempio): Fallimento della linearità
La funzione $T: \mathbb{R}^2 \to \mathbb{R}^2$ definita da $T \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x^2 \\ y \end{pmatrix}$ **non è lineare**.
Verifica formale: 
* $T \left( 2 \begin{pmatrix} 1 \\ 1 \end{pmatrix} \right) = T \begin{pmatrix} 2 \\ 2 \end{pmatrix} = \begin{pmatrix} 4 \\ 2 \end{pmatrix}$.
* Ma $2 \cdot T \begin{pmatrix} 1 \\ 1 \end{pmatrix} = 2 \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 2 \\ 2 \end{pmatrix}$.
* Poiché $T(2v) \neq 2T(v)$, l'omogeneità fallisce.

---

## 4. Esercizio Tipico d'Esame: Sfruttare la Linearità

**Testo:** Sia $T: \mathbb{R}^2 \to \mathbb{R}^2$ un'applicazione lineare tale che $T \begin{pmatrix} 1 \\ 3 \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$ e $T \begin{pmatrix} 2 \\ 1 \end{pmatrix} = \begin{pmatrix} 3 \\ 5 \end{pmatrix}$. Calcolare $T \begin{pmatrix} 9 \\ 12 \end{pmatrix}$.

**Svolgimento:** 
1. Cerchiamo di esprimere il vettore di cui vogliamo l'immagine come combinazione lineare dei vettori noti. In questo caso notiamo che $\begin{pmatrix} 9 \\ 12 \end{pmatrix} = 3 \begin{pmatrix} 3 \\ 4 \end{pmatrix}$. Ancora, $\begin{pmatrix} 3 \\ 4 \end{pmatrix} = \begin{pmatrix} 1 \\ 3 \end{pmatrix} + \begin{pmatrix} 2 \\ 1 \end{pmatrix}$.
2. Dunque $\begin{pmatrix} 9 \\ 12 \end{pmatrix} = 3 \left( \begin{pmatrix} 1 \\ 3 \end{pmatrix} + \begin{pmatrix} 2 \\ 1 \end{pmatrix} \right)$.
3. Sfruttiamo l'additività e l'omogeneità di $T$:
   $$ \begin{aligned} 
   T \begin{pmatrix} 9 \\ 12 \end{pmatrix} &= T \left( 3 \begin{pmatrix} 1 \\ 3 \end{pmatrix} + 3 \begin{pmatrix} 2 \\ 1 \end{pmatrix} \right) \\
   &= 3 \cdot T \begin{pmatrix} 1 \\ 3 \end{pmatrix} + 3 \cdot T \begin{pmatrix} 2 \\ 1 \end{pmatrix} \\
   &= 3 \begin{pmatrix} 2 \\ 1 \end{pmatrix} + 3 \begin{pmatrix} 3 \\ 5 \end{pmatrix} \\
   &= \begin{pmatrix} 6 \\ 3 \end{pmatrix} + \begin{pmatrix} 9 \\ 15 \end{pmatrix} = \begin{pmatrix} 15 \\ 18 \end{pmatrix} 
   \end{aligned} $$

---

## 5. Applicazioni Notevoli
* **Identità ($Id_V$):** $T(v) = v$.
* **Applicazione Nulla:** $T(v) = \mathbf{0}_W$.
* **Applicazione delle coordinate:** Se $\mathcal{B}$ è una base di $V$, la funzione $F_\mathcal{B}: V \to \mathbb{R}^n$ che associa $v \mapsto [v]_\mathcal{B}$ è un **isomorfismo** (applicazione lineare biiettiva).
* **Derivazione e Integrazione:** Nello spazio dei polinomi (o funzioni differenziabili), le operazioni di derivata e integrale sono lineari (es. $D(f+g) = D(f) + D(g)$ e $D(\lambda f) = \lambda D(f)$).

---
## Collegamenti
* **Back:** [[00_Applicazioni_Lineari_MOC|MOC Applicazioni Lineari]]
* **Focus Successivo:** [[Nucleo e Immagine]]
* **Focus Correlato:** [[Isomorfismi]]
