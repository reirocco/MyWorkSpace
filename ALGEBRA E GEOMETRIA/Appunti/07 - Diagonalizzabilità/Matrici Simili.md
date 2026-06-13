---
tags:
  - matematica
  - algebra/diagonalizzabilità
  - algebra/matrici
aliases:
  - Matrice Simile
  - Endomorfismo
---
# Matrici Simili e Invarianti di Similitudine

In Algebra Lineare, la rappresentazione matriciale di un endomorfismo dipende unicamente dalla base scelta. Cambiando la base di riferimento, cambiano le coordinate e, di conseguenza, cambia la matrice associata. Le **matrici simili** sono due facce della stessa medaglia: matrici all'apparenza diverse che descrivono esattamente la stessa trasformazione geometrica.

---

## 1. Definizione Analitica di Similitudine

Sia $T: V \to V$ un **endomorfismo** (un'applicazione lineare in cui dominio e codominio coincidono) di uno spazio vettoriale di dimensione finita $n$.
Se fissiamo una base $\mathcal{B}$, l'endomorfismo è rappresentato da una matrice $A = M_{\mathcal{B}, \mathcal{B}}(T) \in M_n(\mathbb{R})$.
Se scegliamo una differente base $\mathcal{B}'$, l'endomorfismo sarà rappresentato da un'altra matrice $D = M_{\mathcal{B}', \mathcal{B}'}(T)$.

> [!abstract] Definizione
> Due matrici quadrate $A, B \in M_n(\mathbb{R})$ si dicono **simili** se esiste una matrice invertibile $P \in M_n(\mathbb{R})$ tale che:
> $$ B = P^{-1} \cdot A \cdot P $$
> (Oppure, in modo equivalente, $P \cdot B = A \cdot P$).

**Significato Strutturale della Matrice $P$:**
Nella formula di similitudine, la matrice $P$ non è un oggetto astratto: rappresenta la **matrice di cambiamento di base**.
- Essa "traduce" le coordinate dalla vecchia base alla nuova base.
- $P^{-1} A P$ significa operativamente:
  1. $P$: Traccia un vettore dalle nuove coordinate a quelle vecchie.
  2. $A$: Applica la trasformazione lineare usando le vecchie regole.
  3. $P^{-1}$: Riporta il risultato indietro nelle nuove coordinate.

---

## 2. Invarianti di Similitudine

Poiché due matrici simili descrivono *esattamente la stessa funzione geometrica* rispetto a sistemi di coordinate differenti, esse condividono tutte le proprietà intrinseche della funzione. Tali proprietà sono chiamate **Invarianti**.

Siano $A$ e $B$ due matrici simili. Esse hanno in comune:

1. **Stesso Determinante:**
   Per il Teorema di Binet:
   $$ \det(B) = \det(P^{-1}AP) = \det(P^{-1}) \det(A) \det(P) = \frac{1}{\det(P)} \det(A) \det(P) = \det(A) $$
2. **Stessa Traccia:**
   La somma degli elementi sulla diagonale principale non cambia.
3. **Stesso Rango:**
   Moltiplicare per matrici invertibili non altera il rango.
4. **Stesso Polinomio Caratteristico:**
   $$ \begin{aligned} p_B(\lambda) &= \det(B - \lambda I) = \det(P^{-1}AP - \lambda P^{-1}IP) \\
   &= \det(P^{-1}(A - \lambda I)P) = \det(A - \lambda I) = p_A(\lambda) \end{aligned} $$
5. **Stessi Autovalori (con le stesse Molteplicità Algebriche):**
   Conseguenza diretta dell'avere lo stesso polinomio caratteristico.

> [!danger] Condizione Necessaria, NON Sufficiente
> Avere lo stesso determinante, la stessa traccia e lo stesso polinomio caratteristico è **necessario** affinché due matrici siano simili, ma in generale **non è sufficiente**. Esistono matrici con stesso polinomio che *non* sono simili (accade quando le loro molteplicità geometriche differiscono).

---

## 3. Il Ruolo della Diagonalizzazione

Perché ci interessa la similitudine? 
La matrice più facile con cui lavorare in assoluto è la **Matrice Diagonale**. In una matrice diagonale il calcolo delle potenze $A^k$, il determinante, il rango e l'inversa sono triviali: basta elevare/invertire i singoli elementi della diagonale!

**La Teoria della Diagonalizzazione** si riassume in una sola domanda: 
> *Esiste una base (la base "magica" di $P$) per cui la mia complicata matrice $A$ risulta simile a una matrice diagonale $D$?*

Se la risposta è sì, la matrice $A$ è detta **Diagonalizzabile**, e si ha $A = P \cdot D \cdot P^{-1}$. Le colonne di $P$ non sono altro che gli autovettori dell'endomorfismo!

---
## Collegamenti
* **Back:** [[00_Diagonalizzabilita_MOC|MOC Diagonalizzabilità]]
* **Next:** [[Autovalori e Autovettori]]
