Un **sottospazio affine** è, intuitivamente, un sottospazio vettoriale che è stato "spostato" (traslato) rispetto all'origine. Mentre un sottospazio vettoriale deve obbligatoriamente contenere lo zero, quello affine può trovarsi ovunque nello spazio.

---

## 1. Definizione Formale
Sia $V$ uno spazio vettoriale su un campo $K$. Un sottoinsieme $S \subseteq V$ si dice **sottospazio affine** se esiste un punto $P \in V$ (vettore di appoggio) e un sottospazio vettoriale $W \subseteq V$ (detto **giacitura**) tale che:

$$S = P + W = \{ P + \mathbf{w} \mid \mathbf{w} \in W \}$$ ^definizione-formale

> [!abstract] Elementi Chiave
> - **Punto $P$**: Un qualsiasi vettore che appartiene a $S$.
> - **Giacitura $W$**: L'insieme dei vettori "direttori" che definiscono l'orientamento di $S$. ^giacitura

---

## 2. Proprietà e Caratteristiche
* **Dimensione**: La dimensione del sottospazio affine $S$ è per definizione la dimensione della sua giacitura: $\dim(S) = \dim(W)$.
* **Parallelismo**: Due sottospazi affini sono paralleli se hanno la stessa giacitura $W$.
* **Sistemi Lineari**: L'insieme delle soluzioni di un sistema lineare non omogeneo $A\mathbf{x} = \mathbf{b}$ è un sottospazio affine. ^proprieta-sistemi

[Image of a 2D affine subspace plane in 3D space not passing through the origin]

---

## 3. Rappresentazioni Matematiche

### Forma Parametrica
Si ottiene usando il punto $P$ e una base della giacitura $\{\mathbf{v_1}, \dots, \mathbf{v_k}\}$:
$$\mathbf{x} = P + \lambda_1 \mathbf{v_1} + \dots + \lambda_k \mathbf{v_k}$$

### Forma Cartesiana
Un sottospazio affine di $\mathbb{R}^n$ può essere visto come l'insieme dei punti che soddisfano un sistema di equazioni lineari:
$$A\mathbf{x} = \mathbf{b}$$

---

## 4. Note Correlate
- [[Vettori#Dipendenza Lineare]]
- [[Matrici#Rango]]
- [[Geometria#Iperpiani]]

#geometria #algebra-lineare #matematica