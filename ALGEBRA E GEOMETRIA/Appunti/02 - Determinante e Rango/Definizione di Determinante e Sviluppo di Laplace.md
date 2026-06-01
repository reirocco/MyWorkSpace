---
tags:
  - matematica
  - algebra/determinante
aliases:
  - Sviluppo di Laplace
  - Complemento Algebrico
  - Cofattore
---
# Definizione di Determinante e Sviluppo di Laplace

Il **determinante** è una funzione $\det: M_n \to \mathbb{R}$ che associa a ogni matrice quadrata uno scalare che ne riassume alcune proprietà geometriche e algebriche fondamentali (come l'invertibilità).

## Definizione Ricorsiva
- Per una matrice $1 \times 1$, $A = (a_{11})$, si ha $\det A = a_{11}$.
- Per una matrice $n \times n$ con $n > 1$, il determinante è definito tramite lo **sviluppo lungo la prima riga**:
$$
\det A = \sum_{k=1}^{n} (-1)^{1+k} a_{1k} \det A_{1k}
$$
Dove $A_{ij}$ è la **matrice complementare** di $a_{ij}$, ottenuta eliminando la riga $i$ e la colonna $j$.

## Teorema: Sviluppo di Laplace
Il determinante può essere calcolato sviluppando lungo **qualsiasi** riga $i$ o colonna $j$:

1. **Sviluppo lungo la riga $i$:**
   $$\det A = \sum_{k=1}^{n} (-1)^{i+k} a_{ik} \det A_{ik}$$
2. **Sviluppo lungo la colonna $j$:**
   $$\det A = \sum_{k=1}^{n} (-1)^{j+k} a_{kj} \det A_{kj}$$

> [!abstract] Cofattore (o Complemento Algebrico)
> Il termine $C_{ij} = (-1)^{i+j} \det A_{ij}$ viene chiamato **cofattore** dell'elemento $a_{ij}$. Lo sviluppo di Laplace diventa quindi: $\det A = \sum a_{ik} C_{ik}$.

> [!tip] Quale riga/colonna scegliere?
> Per minimizzare i calcoli, scegli sempre la riga o la colonna che contiene il **maggior numero di zeri**.

> [!question]- Esercizio Pratico
> Calcola il determinante della matrice:
> $$
> A = \begin{pmatrix} 1 & 2 & -1 \\ 3 & 0 & -1 \\ 1 & 0 & -2 \end{pmatrix}
> $$
> 
> **Soluzione passo-passo:**
> La colonna 2 contiene due zeri. Sviluppiamo lungo la **seconda colonna**:
> 1. Individuiamo i segni: la posizione $(1,2)$ ha segno $(-1)^{1+2} = -$.
> 2. $\det A = (-1) \cdot 2 \cdot \det \begin{pmatrix} 3 & -1 \\ 1 & -2 \end{pmatrix} + 0 \cdot (\dots) + 0 \cdot (\dots)$
> 3. Calcoliamo il minore $2 \times 2$: $(3 \cdot -2) - (-1 \cdot 1) = -6 + 1 = -5$.
> 4. Risultato finale: $(-2) \cdot (-5) = 10$.

## Collegamenti
- Back: [[00_Determinante_Rango_MOC|MOC Determinante e Rango]]
- Next: [[Regola di Sarrus]]
