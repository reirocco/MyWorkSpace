---
tags:
  - matematica
  - algebra/sistemi
aliases:
  - Cramer
---
# Teorema di Cramer

Il **Teorema di Cramer** fornisce una formula esplicita per risolvere sistemi lineari **quadrati** ($m = n$) che ammettono un'unica soluzione.

## Condizione di Applicabilità
Un sistema $AX = B$ può essere risolto con Cramer se e solo se:
1. È un sistema quadrato (numero equazioni = numero incognite).
2. La matrice incompleta $A$ è non singolare, ovvero **$\det A \neq 0$**.

## La Soluzione
L'incognita $j$-esima ($x_j$) è data dal rapporto:
$$ x_j = \frac{\det A_j}{\det A} $$
Dove $A_j$ è la matrice ottenuta sostituendo la $j$-esima colonna di $A$ con la colonna dei termini noti $B$.

> [!tip] Heuristics d'Esame
> Anche se Cramer è teoricamente elegante, computazionalmente è molto lento per sistemi grandi ($n \ge 4$). Usalo principalmente per sistemi $2 \times 2$ o $3 \times 3$ quando i coefficienti non sono troppo complicati o quando devi discutere parametri.

> [!info]- Dimostrazione (Teorema di Cramer)
> **(Esistenza e Unicità)**: Supponiamo che il sistema ammetta un'unica soluzione. Questo significa che le soluzioni sono $\infty^0$. Per il Teorema di Rouché-Capelli, $\text{rg}(A) = n$, cioè $\det(A) \neq 0$. Viceversa, se $\det(A) \neq 0$, allora $A$ è invertibile, ed esiste $A^{-1}$. Ponendo $X = A^{-1}B$, verifichiamo che è soluzione: $A(A^{-1}B) = (AA^{-1})B = I \cdot B = B$. È unica perché data un'altra soluzione $X'$ si ha: $X' = I X' = (A^{-1}A)X' = A^{-1}(AX') = A^{-1}B = X$.
> **(Formula delle componenti)**: La $i$-esima componente del vettore $X = A^{-1}B$ si ottiene moltiplicando la $i$-esima riga di $A^{-1}$ per $B$. Ricordando che $A^{-1} = \frac{1}{\det A} \, ^t(\text{Cof} A)$, l'operazione equivale proprio allo sviluppo di Laplace del determinante della matrice $A_i$ (dove la colonna $i$ è sostituita da $B$), espanso rispetto alla colonna $i$-esima. Da cui $x_i = \det(A_i) / \det A$.

> [!question]- Esercizio Pratico
> Risolvi col metodo di Cramer:
> $$ \begin{cases} x + y = 3 \\ 2x - y = 0 \end{cases} $$
> 
> **Soluzione passo-passo:**
> 1. $\det A = \begin{vmatrix} 1 & 1 \\ 2 & -1 \end{vmatrix} = -1 - 2 = -3$. (Diverso da zero, Cramer applicabile).
> 2. Calcoliamo $\det A_x$ (sostituiamo colonna 1 con $B = \begin{pmatrix} 3 \\ 0 \end{pmatrix}$):
>    $\det A_x = \begin{vmatrix} 3 & 1 \\ 0 & -1 \end{vmatrix} = -3$.
> 3. Calcoliamo $\det A_y$ (sostituiamo colonna 2 con $B = \begin{pmatrix} 3 \\ 0 \end{pmatrix}$):
>    $\det A_y = \begin{vmatrix} 1 & 3 \\ 2 & 0 \end{vmatrix} = 0 - 6 = -6$.
> 4. Troviamo le incognite:
>    $x = \frac{-3}{-3} = 1$, $y = \frac{-6}{-3} = 2$.

## Collegamenti
- Back: [[00_Sistemi_Lineari_MOC|MOC Sistemi Lineari]]
- Previous: [[Sistemi Lineari Omogenei]]
