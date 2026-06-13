---
tags:
  - matematica
  - geometria
aliases:
  - Prodotto Vettore
  - Regola della Mano Destra
  - Prodotto Vettoriale
---
# Prodotto Vettoriale in $\mathbb{R}^3$

Mentre il *Prodotto Scalare* è un'operazione universale che mastica due vettori di qualsiasi dimensione per sputare un singolo numero, il **Prodotto Vettoriale** ($v \wedge w$, oppure $v \times w$) è un'anomalia magica esclusiva dello spazio tridimensionale $\mathbb{R}^3$ (e pochissimi altri casi esoterici). Masticando due vettori, esso partorisce un **terzo vettore** che gode di proprietà ortogonali perfette.

---

## 1. Definizione e Formula di Calcolo

Il metodo più mnemonico e sistematico per calcolare il prodotto vettoriale consiste nello sviluppare un "determinante formale" lungo la sua prima riga.
Nella prima riga vengono inseriti i versori base canonici di $\mathbb{R}^3$: $\vec{i}, \vec{j}, \vec{k}$. Nelle due righe successive si inseriscono ordinatamente le componenti dei vettori $v$ e $w$.

> [!abstract] Calcolo Analitico
> Siano $v = (v_x, v_y, v_z)^T$ e $w = (w_x, w_y, w_z)^T$. Il prodotto vettoriale è:
> $$ v \wedge w = \det \begin{pmatrix} \vec{i} & \vec{j} & \vec{k} \\ v_x & v_y & v_z \\ w_x & w_y & w_z \end{pmatrix} = \begin{pmatrix} v_y w_z - v_z w_y \\ - (v_x w_z - v_z w_x) \\ v_x w_y - v_y w_x \end{pmatrix} $$

*Attenzione al segno meno del termine centrale derivante dallo sviluppo di Laplace!*

---

## 2. Proprietà Fondamentali (Direzione, Verso, Modulo e Algebriche)

Il vettore emergente possiede caratteristiche geometriche e algebriche rigidissime:

1. **Direzione (Ortogonalità Assoluta):**
   Il vettore risultante $v \wedge w$ è **sempre, simultaneamente perpendicolare** sia a $v$ che a $w$.
   $$ \langle (v \wedge w), v \rangle = 0 \quad \text{e} \quad \langle (v \wedge w), w \rangle = 0 $$
   Questa è la sua utilità principe: generare una normale comune.

2. **Verso (Regola della Mano Destra):**
   Punta le dita della mano destra lungo il primo vettore $v$. Chiudi le dita ruotandole verso il secondo vettore $w$ lungo l'angolo più piccolo. Il pollice alzato indica inflessibilmente il verso di $v \wedge w$.
   *Conseguenza diretta:* Invertire l'ordine dei fattori significa chiudere la mano al contrario (pollice verso il basso). L'operatore non è commutativo, ma **antisimmetrico**: 
   $$ v \wedge w = - (w \wedge v) $$

3. **Modulo (Area del Parallelogramma):**
   La lunghezza del vettore risultante ha un significato geometrico pazzesco. Essa è esattamente uguale all'**Area del Parallelogramma** costruito sui lati $v$ e $w$.
   $$ \| v \wedge w \| = \|v\| \cdot \|w\| \cdot \sin\theta $$
   (In cui $\theta$ è l'angolo compreso, $0 \le \theta \le \pi$. Il seno è sempre positivo, garantendo una lunghezza positiva).

4. **Non-Associatività (Trappola Teorica):**
   A differenza del prodotto normale tra numeri, il prodotto vettoriale **NON è associativo**. L'ordine in cui si eseguono i prodotti multipli cambia drasticamente il risultato:
   $$ (u \wedge v) \wedge w \neq u \wedge (v \wedge w) $$
   *Controesempio classico (spesso chiesto nei test):* Consideriamo i versori base. 
   $(\vec{i} \wedge \vec{j}) \wedge \vec{j} = \vec{k} \wedge \vec{j} = -\vec{i}$.
   Invece, se associamo in modo diverso: $\vec{i} \wedge (\vec{j} \wedge \vec{j}) = \vec{i} \wedge \mathbf{0} = \mathbf{0}$.
   Dato che $-\vec{i} \neq \mathbf{0}$, la proprietà associativa fallisce.


> [!important] Il Test di Parallelismo
> Cosa succede se i due vettori sono paralleli (o coincidenti)? L'angolo $\theta$ è $0^\circ$ o $180^\circ$, quindi il seno è $0$. L'area si schiaccia e si azzera.
> Di conseguenza: due vettori sono proporzionali/paralleli $\iff v \wedge w = \mathbf{0}$.

---

## 3. Applicazioni Cardine per gli Esami

Il prodotto vettoriale trasforma i problemi ostici di Geometria Analitica 3D in banali calcoli meccanici.

### Trovare l'equazione di un piano passante per 3 punti
Dati tre punti non allineati $A, B, C$:
1. Costruisci due vettori-lato che partono dallo stesso vertice (es. $\vec{AB} = B - A$ e $\vec{AC} = C - A$).
2. Calcola $\vec{AB} \wedge \vec{AC}$. Il risultato è un vettore perpendicolare a entrambi i lati, quindi è il vettore normale del piano $\mathbf{n} = (a, b, c)^T$.
3. Prendi i coefficienti e scrivi $ax + by + cz + d = 0$. Trova $d$ sostituendo le coordinate del punto $A$.

### Trovare l'area di un Triangolo nello spazio
I tre punti $A, B, C$ formano un triangolo che non è altro che la metà esatta del parallelogramma generato dai loro vettori lati. L'area si calcola senza mai calcolare basi, altezze o angoli complessi:
$$ \text{Area}_{\triangle} = \frac{1}{2} \| \vec{AB} \wedge \vec{AC} \| $$

---

## 4. Esercizi Propedeutici Svolti

> [!example]- Esercizio 1: Calcolo Diretto
> **Testo:** Dati i vettori $v = (1, -2, 3)^T$ e $w = (2, 0, 1)^T$, calcolare $v \wedge w$.
> 
> **Soluzione:**
> Impostiamo il determinante formale:
> $$ v \wedge w = \det \begin{pmatrix} \vec{i} & \vec{j} & \vec{k} \\ 1 & -2 & 3 \\ 2 & 0 & 1 \end{pmatrix} $$
> Sviluppiamo per la prima riga:
> - Componente $\vec{i}$: $(-2)(1) - (3)(0) = -2$
> - Componente $\vec{j}$ (con segno meno!): $-[(1)(1) - (3)(2)] = -[1 - 6] = 5$
> - Componente $\vec{k}$: $(1)(0) - (-2)(2) = 0 - (-4) = 4$
> Il vettore risultante è $(-2, 5, 4)^T$. 
> *(Puoi verificare che il prodotto scalare del risultato sia con v che con w è zero!)*

> [!example]- Esercizio 2: Area del Triangolo
> **Testo:** Calcolare l'area del triangolo i cui vertici sono $A(1, 0, 0), B(0, 1, 0)$ e $C(0, 0, 1)$.
> 
> **Soluzione:**
> 1. Troviamo i due vettori che partono da A:
>    $$ \vec{AB} = B - A = (-1, 1, 0)^T $$
>    $$ \vec{AC} = C - A = (-1, 0, 1)^T $$
> 2. Calcoliamo il loro prodotto vettoriale $\vec{n} = \vec{AB} \wedge \vec{AC}$:
>    $$ \vec{n} = \det \begin{pmatrix} \vec{i} & \vec{j} & \vec{k} \\ -1 & 1 & 0 \\ -1 & 0 & 1 \end{pmatrix} $$
>    $$ \vec{n} = \vec{i}(1-0) - \vec{j}(-1-0) + \vec{k}(0 - (-1)) = (1, 1, 1)^T $$
> 3. L'area del triangolo è la metà del modulo di questo vettore normale:
>    $$ \text{Area}_{\triangle} = \frac{1}{2} \| (1, 1, 1)^T \| = \frac{1}{2}\sqrt{1^2 + 1^2 + 1^2} = \frac{\sqrt{3}}{2} $$

---
## Collegamenti
* **Back:** [[00_Geometria_MOC|MOC Geometria]]
* **Previous:** [[Punti e Distanze]]
* **Next:** [[Rette nello Spazio]]
