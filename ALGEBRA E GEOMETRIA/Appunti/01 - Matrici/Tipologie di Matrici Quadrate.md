---
tags:
  - matematica
  - algebra/matrici
aliases:
  - Matrice Quadrata
  - Matrice Triangolare
  - Matrice Diagonale
  - Matrice Simmetrica
  - Matrice Antisimmetrica
---
# Tipologie di Matrici Quadrate

Una matrice quadrata $A \in M_n$ ha un eguale numero di righe e colonne ($m = n$).
In queste matrici esiste una **Diagonale Principale** costituita dagli elementi $a_{11}, a_{22}, \dots, a_{nn}$.

## 1. Matrici Triangolari
- **Triangolare Superiore:** tutti gli elementi **sotto** la diagonale sono nulli ($a_{ij} = 0$ per $i > j$).
- **Triangolare Inferiore:** tutti gli elementi **sopra** la diagonale sono nulli ($a_{ij} = 0$ per $i < j$).

## 2. Matrici Diagonali
Una matrice si dice **diagonale** se tutti gli elementi *fuori* dalla diagonale sono nulli ($a_{ij} = 0$ per $i \neq j$).
È contemporaneamente triangolare superiore e inferiore. 
L'esempio per eccellenza è la **Matrice Identità $I_n$** e i suoi multipli scalari $\lambda I_n$.

## 3. Matrici Simmetriche e Antisimmetriche (Vedi: [[Trasposta di una Matrice]])
- **Matrice Simmetrica:** se $A = ^tA$, ovvero se $a_{ij} = a_{ji}$ per ogni $i,j$. La matrice è simmetrica rispetto alla sua diagonale.
- **Matrice Antisimmetrica:** se $A = -^tA$, ovvero $a_{ij} = -a_{ji}$ per ogni $i,j$.
  > [!danger] Proprietà essenziale (Matrice Antisimmetrica)
  > Gli elementi sulla diagonale principale di una matrice antisimmetrica devono necessariamente essere nulli. Infatti $a_{ii} = -a_{ii} \iff 2a_{ii} = 0 \iff a_{ii}=0$.

> [!question]- Esercizio Pratico
> Stabilisci il tipo delle seguenti matrici:
> $A_1 = \begin{pmatrix} 1 & -1 & 0 \\ -1 & 0 & 3 \\ 0 & 3 & 2 \end{pmatrix}$ e $A_2 = \begin{pmatrix} 0 & 2 & 3 \\ -2 & 0 & 1 \\ -3 & -1 & 0 \end{pmatrix}$
> 
> **Soluzione passo-passo:**
> - In $A_1$ vediamo che l'elemento in $(1,2)$ è $-1$ pari a $(2,1)$. Elemento in $(1,3)$ è $0$, pari a $(3,1)$. Elemento in $(2,3)$ è $3$, pari a $(3,2)$. La matrice è **simmetrica** in quanto $a_{ij} = a_{ji}$.
> - In $A_2$ notiamo zeri sulla diagonale. L'elemento $(1,2)$ è $2$, opposto a $(2,1)$ che è $-2$. Lo stesso vale per gli altri elementi simmetrici alla diagonale. Dunque $a_{ij} = -a_{ji}$ determinando una matrice **antisimmetrica**.

## Collegamenti
- Back: [[01 - Matrici]]
- Previous: [[Trasposta di una Matrice]]
- Next: [[Prodotto Righe per Colonne]]
