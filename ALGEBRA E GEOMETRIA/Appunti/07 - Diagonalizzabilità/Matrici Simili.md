---
tags:
  - matematica
  - algebra/diagonalizzabilità
  - algebra/matrici
aliases:
  - Matrice Simile
  - Endomorfismo
---

# Matrici Simili

Un **endomorfismo** è un'applicazione lineare $T: V \to V$ (dominio e codominio coincidono). 
Se fissiamo una base $\mathcal{B}$ di $V$, otteniamo una matrice associata $A = M_{\mathcal{B}, \mathcal{B}}(T)$ che è una matrice quadrata $n \times n$.
Se scegliamo un'altra base $\mathcal{B}'$, otterremo una matrice diversa $D$.

## Definizione di Similitudine
Due matrici quadrate $A, D \in M_n$ si dicono **simili** se esiste una matrice invertibile $P$ (che fa da "traduttore" tra le basi) tale che:
$$ D = P^{-1} A P $$
Se $A$ e $D$ sono simili, esse rappresentano **lo stesso endomorfismo** scritto in due basi diverse.

## Invarianti di Similitudine
Poiché rappresentano la stessa funzione, due matrici simili condividono molte proprietà fondamentali (dette invarianti):
1. **Determinante**: Per il Teorema di Binet, $\det(D) = \det(P^{-1} A P) = \det(P^{-1}) \cdot \det(A) \cdot \det(P) = \det(A)$.
2. **Traccia**: La somma degli elementi sulla diagonale principale.
3. **Polinomio Caratteristico**: $\det(D - \lambda I) = \det(A - \lambda I)$. (E quindi hanno gli stessi autovalori).
4. **Rango**.

> [!important] L'Obiettivo della Diagonalizzabilità
> Una matrice $A$ è **diagonalizzabile** se è simile a una matrice **diagonale** $D$. Lavorare con matrici diagonali è infinitamente più semplice (il prodotto, le potenze e l'inversa si calcolano in un attimo), per questo cerchiamo la base "magica" che rende la matrice diagonale.

## Collegamenti
- Back: [[00_Diagonalizzabilita_MOC|MOC Diagonalizzabilità]]
- Next: [[Autovalori e Autovettori]]
