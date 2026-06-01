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

# Autovalori e Autovettori

Nello studio di un endomorfismo $T: V \to V$ (o di una matrice $A \in M_n$), ci interessano le direzioni "speciali" che non vengono ruotate, ma solo allungate o accorciate.

## Definizione
Un vettore $v \neq \mathbf{0}$ si dice **Autovettore** relativo all'**Autovalore** $\lambda \in \mathbb{R}$ se:
$$ A \cdot v = \lambda \cdot v $$
- geometricamente, l'immagine del vettore ha la stessa direzione del vettore di partenza.
- il vettore nullo **non** può mai essere un autovettore per definizione.
- L'autovalore $\lambda$ può invece essere zero! (In tal caso $A \cdot v = \mathbf{0}$, quindi $v \in \ker(A)$).

## Il Polinomio Caratteristico
La condizione $Av = \lambda v$ si può riscrivere come $(A - \lambda I)v = \mathbf{0}$.
Affinché questo sistema omogeneo abbia soluzioni non banali ($v \neq \mathbf{0}$), la matrice $(A - \lambda I)$ deve avere determinante nullo:
$$ p_A(\lambda) = \det(A - \lambda I) = 0 $$
Questo è il **Polinomio Caratteristico**. 
Gli **autovalori** di $A$ sono esattamente le **radici** del polinomio caratteristico.
- È un polinomio di grado $n$.
- Il termine noto è $\det(A)$.
- Il prodotto degli autovalori è $\det(A)$, la loro somma è $\text{traccia}(A)$.

## L'Autospazio
L'**Autospazio** relativo all'autovalore $\lambda$, denotato con $E(\lambda)$, è l'insieme di tutti gli autovettori relativi a $\lambda$ unito al vettore nullo:
$$ E(\lambda) = \ker(A - \lambda I) = \{ v \in \mathbb{R}^n : (A - \lambda I)v = \mathbf{0} \} $$
- È sempre un sottospazio vettoriale di $\mathbb{R}^n$.

> [!abstract] Proprietà Fondamentale
> **Autovettori relativi ad autovalori diversi sono linearmente indipendenti.** (Questo è cruciale per poter formare una base).

## Collegamenti
- Back: [[00_Diagonalizzabilita_MOC|MOC Diagonalizzabilità]]
- Previous: [[Matrici Simili]]
- Next: [[Molteplicità Algebrica e Geometrica]]
