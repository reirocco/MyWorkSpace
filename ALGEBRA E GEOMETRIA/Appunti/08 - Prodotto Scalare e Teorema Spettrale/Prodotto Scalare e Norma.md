---
tags:
  - matematica
  - algebra/prodotto_scalare
aliases:
  - Prodotto Scalare
  - Norma Euclidea
  - Ortogonali
  - Angolo tra vettori
---
# Prodotto Scalare Standard e Norma in $\mathbb{R}^n$

Finora abbiamo studiato gli spazi vettoriali da un punto di vista puramente "elastico" (somma e moltiplicazione per scalare). In questa struttura, non esiste il concetto di "lunghezza" di un vettore né di "angolo" tra due vettori. Il **Prodotto Scalare** è l'operatore metrico che introduce la geometria all'interno dell'algebra.

---

## 1. Il Prodotto Scalare Standard

Dati due vettori colonna $v, w \in \mathbb{R}^n$, il **prodotto scalare standard** (o canonico) è definito analiticamente come la somma dei prodotti delle rispettive componenti.

> [!abstract] Definizione Analitica
> Il prodotto scalare standard $\langle v, w \rangle$ (spesso indicato anche con $v \cdot w$) è definito tramite il prodotto tra matrici:
> $$ \langle v, w \rangle = v^T \cdot w = \sum_{i=1}^n v_i w_i = v_1 w_1 + v_2 w_2 + \dots + v_n w_n $$
> Il risultato è un **singolo numero reale** (uno scalare), NON un vettore.

>[!WARNING] Il **Prodotto Scalare**  calcola la proiezione di un vettore su un'altro
### La magia del Prodotto Scalare ($\vec{QP} \cdot \mathbf{n}$)

In algebra lineare, esiste un'operazione che serve proprio a calcolare il prodotto tra due vettori e il coseno dell'angolo compreso tra loro. Questa operazione è il prodotto scalare.

La definizione matematica di prodotto scalare tra $\vec{QP}$ e $\mathbf{n}$ è:
$$ \vec{QP} \cdot \mathbf{n} = \|\vec{QP}\| \cdot \|\mathbf{n}\| \cdot \cos(\theta) $$

Guarda bene questa uguaglianza. Al suo interno c'è il pezzo $\|\vec{QP}\| \cdot \cos(\theta)$, che abbiamo detto essere proprio la nostra distanza $d$!
### Proprietà Fondamentali (Assiomi)
L'operatore $\langle \cdot, \cdot \rangle : \mathbb{R}^n \times \mathbb{R}^n \to \mathbb{R}$ gode di quattro proprietà intrinseche (che definiscono, più in generale, qualsiasi prodotto scalare astratto):
1. **Simmetria (o Commutatività):** 
   $\langle v, w \rangle = \langle w, v \rangle \quad \forall v, w$
2. **Additività:** 
   $\langle u+v, w \rangle = \langle u, w \rangle + \langle v, w \rangle$
3. **Omogeneità:** 
   $\langle \lambda v, w \rangle = \lambda \langle v, w \rangle$
   *(Queste ultime due insieme formano la **Bilinearità**: il prodotto scalare è lineare sia nel primo che nel secondo argomento).*
4. **Definita Positività:** 
   $\langle v, v \rangle \ge 0 \quad \forall v \in \mathbb{R}^n$, e inoltre $\langle v, v \rangle = 0 \iff v = \mathbf{0}$.

---

## 2. La Norma Euclidea (Lunghezza)

Avendo introdotto il prodotto scalare, possiamo misurare la lunghezza di un vettore calcolando il prodotto scalare di un vettore con se stesso.

> [!abstract] Definizione di Norma
> La **Norma** (o lunghezza euclidea) di un vettore $v$, indicata con $\|v\|$, è definita come la radice quadrata del suo prodotto scalare con se stesso:
> $$ \|v\| = \sqrt{\langle v, v \rangle} = \sqrt{v_1^2 + v_2^2 + \dots + v_n^2} $$

- **Versori:** Un vettore $v$ la cui norma è esattaemnte $1$ ($\|v\| = 1$) si chiama **versore**.
- **Normalizzazione:** Se abbiamo un vettore non nullo $w$ e vogliamo costruire un versore $u$ che abbia la stessa identica direzione e verso di $w$, lo **normalizziamo** dividendolo per la sua lunghezza:
  $$ u = \frac{1}{\|w\|} w $$

### Disuguaglianze Notevoli
La norma innesca due tra le disuguaglianze più importanti dell'intera matematica:
1. **Disuguaglianza di Cauchy-Schwarz:**
   Il valore assoluto del prodotto scalare è sempre schiacciato dal prodotto delle singole norme.
   $$ |\langle v, w \rangle| \le \|v\| \cdot \|w\| $$
2. **Disuguaglianza Triangolare:**
   La strada più breve tra due punti è una linea retta. In un triangolo formato dai vettori, un lato è sempre minore della somma degli altri due.
   $$ \|v + w\| \le \|v\| + \|w\| $$

---

## 3. Ortogonalità e Angoli

La formula di Cauchy-Schwarz ci permette di definire l'angolo $\theta$ compreso tra due vettori in qualsiasi dimensione $n$, semplicemente isolandolo geometricamente:
$$ \cos(\theta) = \frac{\langle v, w \rangle}{\|v\| \cdot \|w\|} $$

Questa formula rivela il concetto più vitale: l'ortogonalità (la perpendicolarità).
Poiché $\cos(90^\circ) = 0$, due vettori sono ortogonali quando il loro prodotto scalare si annulla.

> [!important] Vettori Ortogonali
> Due vettori $v, w \in \mathbb{R}^n$ si dicono **ortogonali** (indicato con $v \perp w$) se e solo se:
> $$ \langle v, w \rangle = 0 $$
> **Teorema di Pitagora in $\mathbb{R}^n$:** Se $v \perp w$, allora vale sempre $\|v+w\|^2 = \|v\|^2 + \|w\|^2$.



---
## Collegamenti
* **Back:** [[00_Prodotto_Scalare_MOC|MOC Prodotto Scalare]]
* **Next:** [[Complemento Ortogonale]]
