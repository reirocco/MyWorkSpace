---
tags:
  - matematica
  - algebra/diagonalizzabilità
aliases:
  - Autovalore
  - Autovettore
  - Polinomio Caratteristico
  - Autospazio
---
# Autovalori, Autovettori e Polinomio Caratteristico

Nello studio di un endomorfismo $T: V \to V$ (o della corrispondente matrice quadrata $A \in M_n$), l'azione dell'applicazione può risultare complessa. Esistono però delle direzioni "privilegiate" nello spazio in cui l'applicazione si comporta nel modo più semplice possibile: come una banale moltiplicazione scalare (una dilatazione o contrazione).

---

## 1. Definizione Geometrica e Algebrica

> [!abstract] Definizione di Autovettore e Autovalore
> Sia $T: V \to V$ un endomorfismo. Un vettore $v \in V$, **non nullo** ($v \neq \mathbf{0}$), si dice **Autovettore** per $T$ se esiste uno scalare $\lambda \in \mathbb{R}$ tale che:
> $$ T(v) = \lambda v $$
> Lo scalare $\lambda$ prende il nome di **Autovalore** associato all'autovettore $v$.

In forma matriciale, se $A$ è la matrice associata, l'equazione diventa:
$$ A \cdot v = \lambda v $$

**Osservazioni Fondamentali:**
- **Il vettore nullo è escluso a priori.** (Perché $A \cdot \mathbf{0} = \lambda \cdot \mathbf{0}$ è un'identità banale per *qualsiasi* $\lambda$, priva di contenuto geometrico).
- **L'autovalore può essere zero.** Se $\lambda = 0$, significa che $A \cdot v = \mathbf{0} \cdot v = \mathbf{0}$. Questo implica che l'autovettore $v$ appartiene al nucleo dell'applicazione, $v \in \ker(A)$. Di conseguenza, se 0 è autovalore, la matrice ha nucleo non banale e *non è invertibile*.

---

## 2. Il Polinomio Caratteristico

Come calcolare operativamente gli autovalori? Riscriviamo l'equazione di definizione spostando tutto allo stesso membro:
$$ Av - \lambda v = \mathbf{0} \implies (A - \lambda I)v = \mathbf{0} $$
(Dove $I$ è la matrice identità di ordine $n$).

Questa è un'equazione di un sistema lineare omogeneo. Affinché esista un autovettore $v \neq \mathbf{0}$ (soluzione non banale), la matrice quadrata $(A - \lambda I)$ **deve essere singolare** (cioè non invertibile).
La condizione di singolarità impone che il determinante sia nullo:
$$ p_A(\lambda) = \det(A - \lambda I) = 0 $$

Questa equazione è detta **Equazione Caratteristica**. La funzione $p_A(\lambda)$ è il **Polinomio Caratteristico** della matrice $A$. 
Gli **autovalori** di $A$ sono esattamente le **radici reali** del suo polinomio caratteristico.

### Proprietà del Polinomio Caratteristico
Sia $A \in M_n(\mathbb{R})$ e $p_A(\lambda)$ il suo polinomio caratteristico.
1. **Grado:** $p_A(\lambda)$ è un polinomio di grado $n$. Dunque ha al massimo $n$ radici reali.
2. **Termine noto:** È sempre uguale al determinante della matrice originaria: $p_A(0) = \det(A)$.
3. **Somma e Prodotto:** 
   - La somma degli autovalori (contati con molteplicità) è pari alla **Traccia** di $A$ ($\text{tr}(A) = \sum a_{ii}$).
   - Il prodotto degli autovalori è pari al **Determinante** di $A$.
   Queste ultime proprietà (Teorema di Viète) sono *fondamentali* all'esame per verificare a mente se gli autovalori trovati sono corretti.

---

## 3. L'Autospazio

Una volta trovato un autovalore $\lambda$, andiamo alla ricerca di *tutti* i suoi relativi autovettori. 

> [!abstract] Definizione di Autospazio
> L'**Autospazio** relativo all'autovalore $\lambda$, denotato con $E_\lambda$ o $V_\lambda$, è l'insieme di tutti gli autovettori relativi a $\lambda$, a cui si aggiunge il vettore nullo.
> $$ E_\lambda = \{ v \in \mathbb{R}^n : (A - \lambda I)v = \mathbf{0} \} = \ker(A - \lambda I) $$

- L'autospazio è un **sottospazio vettoriale** di $\mathbb{R}^n$ (poiché coincide con il nucleo della matrice $(A-\lambda I)$).
- Risolvere $(A-\lambda I)v = \mathbf{0}$ significa risolvere il sistema lineare omogeneo ad esso associato per trovare una base dell'autospazio.

### Indipendenza degli Autovettori (Teorema)
Un teorema strutturale decisivo dell'Algebra Lineare afferma che:
> **Autovettori relativi ad autovalori DISTINTI sono linearmente indipendenti.**
*(La dimostrazione si fa per induzione. L'idea è che autovettori di autovalori diversi "puntano" in direzioni fondamentali distinte dello spazio, non allineabili).*

Questo teorema è il motore che ci permetterà di costruire basi diagonalizzanti.

---
## Collegamenti
* **Back:** [[00_Diagonalizzabilita_MOC|MOC Diagonalizzabilità]]
* **Previous:** [[Matrici Simili]]
* **Next:** [[Molteplicità Algebrica e Geometrica]]
