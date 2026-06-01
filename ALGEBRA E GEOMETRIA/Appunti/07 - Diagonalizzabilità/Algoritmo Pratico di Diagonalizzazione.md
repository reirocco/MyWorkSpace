---
tags:
  - matematica
  - algebra/diagonalizzabilità
aliases:
  - Algoritmo diagonalizzazione
---

# Algoritmo Pratico di Diagonalizzazione

Sei all'esame, ti viene data una matrice $A \in M_n$ e ti si chiede di verificare se è diagonalizzabile e, se lo è, di trovare $D$ e $M$ (dove $D = M^{-1}AM$).

## Gli Step

1. **Trova il Polinomio Caratteristico**
   Calcola $p(\lambda) = \det(A - \lambda I)$ e trovarne le radici.
   *Se ci sono radici complesse non reali, fermati: NON è diagonalizzabile su $\mathbb{R}$.*

2. **Determina le Molteplicità Algebriche ($m_a$)**
   Segna quante volte compare ogni radice. Se hai $n$ radici distinte ($m_a=1$ per tutti), la matrice è diagonalizzabile di sicuro. Vai allo step 4.

3. **Verifica le Molteplicità Geometriche ($m_g$)**
   Per gli autovalori "problematici" con $m_a > 1$, calcola il rango della matrice $(A - \lambda I)$.
   $m_g(\lambda) = n - \text{rg}(A - \lambda I)$.
   - Se $m_g = m_a$ per tutti, la matrice è **diagonalizzabile**.
   - Se per anche un solo autovalore $m_g < m_a$, fermati: **NON è diagonalizzabile**.

4. **Trova le Basi degli Autospazi**
   Per ogni autovalore $\lambda$, risolvi il sistema omogeneo $(A - \lambda I)X = \mathbf{0}$. L'insieme delle soluzioni è l'autospazio $E(\lambda)$. Trova una base per esso.

5. **Costruisci le Matrici $D$ e $M$**
   - **Matrice Diagonale $D$**: Metti gli autovalori trovati sulla diagonale principale (ripetuti tante volte quanto la loro $m_a$). Tutto il resto è zero.
   - **Matrice di Passaggio $M$**: Metti in colonna gli autovettori di base trovati nello Step 4. 
   *(Attenzione: L'ordine delle colonne in $M$ DEVE corrispondere all'ordine in cui hai posizionato gli autovalori in $D$!).*

> [!question]- Esercizio Pratico
> Mostra i passi logici (senza calcoli) per diagonalizzare una matrice $A$ $3\times 3$ con polinomio $(2-\lambda)^2(1-\lambda)=0$.
> 
> **Soluzione passo-passo:**
> 1. Autovalori: $\lambda_1 = 2$ ($m_a = 2$), $\lambda_2 = 1$ ($m_a = 1$).
> 2. Controlliamo $\lambda_1 = 2$: verifichiamo che $\text{rg}(A - 2I) = 3 - 2 = 1$. Se sì, è diagonalizzabile.
> 3. Risolviamo $(A-2I)X = \mathbf{0}$ trovando base $(v_1, v_2)$. Risolviamo $(A-I)X = \mathbf{0}$ trovando base $(v_3)$.
> 4. Costruiamo $M = (v_1 | v_2 | v_3)$. Costruiamo $D = \text{diag}(2, 2, 1)$.

## Collegamenti
- Back: [[00_Diagonalizzabilita_MOC|MOC Diagonalizzabilità]]
- Previous: [[Criterio di Diagonalizzabilità]]
