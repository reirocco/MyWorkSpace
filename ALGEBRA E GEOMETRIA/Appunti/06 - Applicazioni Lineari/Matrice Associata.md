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
# Matrice Associata

L'idea geniale dell'Algebra Lineare è che **ogni** applicazione lineare tra spazi di dimensione finita può essere "tradotta" in una matrice, trasformando lo studio delle funzioni nello studio di sistemi lineari (dove si applica l'[[Algoritmo di Eliminazione di Gauss]]).

## Definizione di Matrice Associata
Siano $V$ e $W$ spazi vettoriali. Fissiamo una base $\mathcal{B} = (v_1, \dots, v_n)$ in $V$ e una base $\mathcal{B}'$ in $W$.
La **matrice associata** $M_{\mathcal{B}', \mathcal{B}}(T)$ è costruita mettendone **in colonna** le coordinate delle immagini dei vettori della base $\mathcal{B}$:
$$ M_{\mathcal{B}', \mathcal{B}}(T) = \Big( F_{\mathcal{B}'}(T(v_1)) \Big| F_{\mathcal{B}'}(T(v_2)) \Big| \dots \Big| F_{\mathcal{B}'}(T(v_n)) \Big) $$

> [!tip] Regola Pratica (in $\mathbb{R}^n$)
> Se $T: \mathbb{R}^n \to \mathbb{R}^m$ ed entrambe le basi sono quelle **canoniche**, la matrice associata $A$ si ottiene semplicemente prendendo i coefficienti delle variabili di $T(x_1, \dots, x_n)$ e mettendoli in riga.

## Teorema della Matrice Associata (Il Calcolo)
Questa matrice serve a una cosa fondamentale: calcolare le immagini attraverso un banale prodotto riga per colonna. Per ogni vettore $v \in V$:
$$ F_{\mathcal{B}'}(T(v)) = M_{\mathcal{B}', \mathcal{B}}(T) \cdot F_{\mathcal{B}}(v) $$
In parole: "Le coordinate dell'immagine sono uguali alla matrice associata moltiplicata per le coordinate del vettore di partenza".

## Relazione con Rango e Nucleo
Sia $A$ la matrice associata a $T$. Allora:
1. $\dim(\text{Im}(T)) = \text{rg}(A)$. (L'immagine è generata dalle colonne di $A$).
2. $\dim(\ker(T)) = n - \text{rg}(A)$. (Il nucleo corrisponde alle soluzioni del sistema omogeneo $AX = \mathbf{0}$).

## Matrice di Cambiamento di Base
Un caso particolare di matrice associata è quando $T = \text{Id}$ (l'identità, che non fa nulla ai vettori).
Se calcoliamo $M_{\mathcal{B}', \mathcal{B}}(\text{Id})$, stiamo solo esprimendo i vettori della base vecchia $\mathcal{B}$ usando le coordinate della base nuova $\mathcal{B}'$. Questa si chiama **Matrice di Cambiamento di Base**. 
È sempre una matrice invertibile e serve a "tradurre" le coordinate da un sistema di riferimento all'altro:
$$ X_{\text{nuovo}} = M \cdot X_{\text{vecchio}} $$

## Collegamenti
- Back: [[00_Applicazioni_Lineari_MOC|MOC Applicazioni Lineari]]
- Previous: [[Teorema di Nullità più Rango]]
- Next: [[Isomorfismi]]
