---
tags:
  - matematica
  - algebra/matrici
aliases:
  - Somma di Matrici
  - Moltiplicazione per Scalare
---
# Operazioni su Matrici

All'interno dell'insieme $M_{m,n}$, si definiscono due operazioni principali:

## 1. Somma tra Matrici
Se $A = (a_{ij})$ e $B = (b_{ij})$ sono due matrici appartenenti a $M_{m,n}$ (stessa forma o taglia), la loro somma si ottiene sommando gli elementi corrispondenti:
$$
A + B = (a_{ij} + b_{ij}) \in M_{m,n}
$$

> [!danger] Attenzione! (Errore Comune)
> Non si possono sommare due matrici di **taglia diversa**. Se provi a sommare $A \in M_{2,3}$ con $B \in M_{2,2}$, l'operazione non è definita.

## 2. Moltiplicazione per uno Scalare
Data una matrice $A = (a_{ij}) \in M_{m,n}$ e una costante reale (scalare) $\lambda \in \mathbb{R}$, il prodotto è ottenuto moltiplicando **ogni elemento** della matrice per lo scalare:
$$
\lambda \cdot A = (\lambda \cdot a_{ij}) \in M_{m,n}
$$

## Proprietà
Per ogni $A, B, C \in M_{m,n}$ e per ogni scalare $\lambda, \mu \in \mathbb{R}$:
1. **Associativa ($+$):** $(A+B)+C = A+(B+C)$
2. **Elemento neutro ($+$):** Esiste matrice Nulla $0_{m,n}$ tale che $A + 0 = A$
3. **Opposto ($+$):** $A + (-A) = 0$
4. **Commutativa ($+$):** $A + B = B + A$
5. **Associativa ($\cdot$):** $\lambda \cdot (\mu \cdot A) = (\lambda \cdot \mu) \cdot A$
6. **Distributiva 1:** $(\lambda + \mu) \cdot A = \lambda \cdot A + \mu \cdot A$
7. **Distributiva 2:** $\lambda \cdot (A + B) = \lambda \cdot A + \lambda \cdot B$
8. **Elemento neutro ($\cdot$):** $1 \cdot A = A$

> [!TIP] La classificazione delle strutture algebriche
> 1) **Magma (o Gruppoide)**: Ha solo la ==chiusura==. Prendi due elementi, li combini e il risultato è ancora dentro l'insieme. Fine. Non vale nient'altro. 
> 2) **Semigruppo**: Ha ==chiusura + associatività==. È esattamente quello che hai chiesto tu. L'operazione non esce dall'insieme e le parentesi non contano. 
> 3) **Monoide**: Ha ==chiusura + associatività + elemento neutro==. È un semigruppo che in più ha un elemento "fantasma" che non fa nulla. 
> 4) **Gruppo**: Ha ==chiusura + associatività + elemento neutro + elemento inverso==. La struttura completa di cui parlavamo prima. 
> 5) **Gruppo Abeliano**: Ha== tutte e 4 le proprietà del gruppo + la commutatività.==


> [!question]- Esercizio Pratico
> Siano:
> $$
> A = \begin{pmatrix} -1 & 0 & 1 \\ 1 & 2 & 3 \end{pmatrix}, \quad B = \begin{pmatrix} \sqrt{3} & 2 & 1 \\ 2 & 1 & 0 \end{pmatrix}
> $$
> Calcola la matrice $A + B$.
> 
> **Soluzione passo-passo:**
> La somma si esegue elemento per elemento. Entrambe le matrici sono in $M_{2,3}$ quindi l'operazione è possibile.
> $$
> A+B = \begin{pmatrix} -1 + \sqrt{3} & 0 + 2 & 1 + 1 \\ 1 + 2 & 2 + 1 & 3 + 0 \end{pmatrix} = \begin{pmatrix} \sqrt{3} - 1 & 2 & 2 \\ 3 & 3 & 3 \end{pmatrix}
> $$

> [!question]- Esercizio: Matrici Simmetriche
> Date due matrici simmetriche $A = (a_{ij})$ e $B = (b_{ij})$ di ordine $n$ e dato $\lambda \in \mathbb{R}$, dimostrare che $A + B$ è simmetrica e $\lambda \cdot A$ è simmetrica.
> 
> **Soluzione passo-passo:**
> 6. Per mostrare che $A+B$ è simmetrica, calcoliamo la sua trasposta. Sfruttando le proprietà della trasposta: $^t(A + B) = ^tA + ^tB$.
> 7. Poiché $A$ e $B$ sono simmetriche per ipotesi, sappiamo che $^tA = A$ e $^tB = B$.
> 8. Sostituendo: $^t(A + B) = A + B$. Dunque $A+B$ è simmetrica.
> 9. Per $\lambda \cdot A$: calcoliamo $^t(\lambda \cdot A)$. Per le proprietà, lo scalare esce dalla trasposizione: $^t(\lambda \cdot A) = \lambda \cdot ^tA$.
> 10. Essendo $A$ simmetrica ($^tA = A$), otteniamo $\lambda \cdot A$. Quindi $\lambda \cdot A$ è simmetrica.

> [!question]- Esercizio: Matrici Antisimmetriche
> Date due matrici antisimmetriche $A = (a_{ij})$ e $B = (b_{ij})$ di ordine $n$ e dato $\lambda \in \mathbb{R}$, dimostrare che $A+B$ è antisimmetrica e $\lambda \cdot A$ è antisimmetrica.
> 
> **Soluzione passo-passo:**
> 11. Essendo antisimmetriche, per ipotesi vale $^tA = -A$ e $^tB = -B$.
> 12. Calcoliamo la trasposta della somma: $^t(A + B) = ^tA + ^tB = -A - B = -(A + B)$. Quindi $A+B$ è antisimmetrica.
> 13. Per il prodotto scalare: $^t(\lambda \cdot A) = \lambda \cdot ^tA = \lambda \cdot (-A) = -(\lambda \cdot A)$. Dunque $\lambda \cdot A$ è antisimmetrica.

## Collegamenti
- Back: [[01 - Matrici]]
- Previous: [[Definizione e Notazione di Matrice]]
- Next: [[Dipendenza Lineare di Matrici]]
