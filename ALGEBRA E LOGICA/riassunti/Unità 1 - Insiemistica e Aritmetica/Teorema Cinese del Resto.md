---
tags:
  - teorema-cinese
  - sistemi-congruenziali
  - aritmetica-modulare
  - algebra
type: atomic
unit: 1
---

# Teorema Cinese del Resto

Il **Teorema Cinese del Resto (TCR)** fornisce una condizione sufficiente per la risolubilità di sistemi di equazioni congruenziali lineari e offre un metodo per costruire esplicitamente la soluzione.

## Il Teorema

Dato un sistema di $k$ equazioni congruenziali della forma:
$$
\begin{cases}
x \equiv c_1 \pmod{n_1} \\
x \equiv c_2 \pmod{n_2} \\
\dots \\
x \equiv c_k \pmod{n_k}
\end{cases}
$$

> [!IMPORTANT] Enunciato
> Se i moduli $n_1, n_2, \dots, n_k$ sono **a due a due coprimi** (ossia $\text{MCD}(n_i, n_j) = 1$ per ogni $i \neq j$), allora il sistema ammette un'unica soluzione modulo $N = n_1 \cdot n_2 \cdots n_k$.

Se i moduli **non** sono a due a due coprimi, il sistema ammette soluzioni solo se $c_i \equiv c_j \pmod{\text{MCD}(n_i, n_j)}$ per ogni coppia $i, j$.

---

## Procedimento Costruttivo (Metodo Standard)

Per risolvere il sistema, seguiamo l'algoritmo costruttivo dettato dalla dimostrazione del TCR:
1. Calcoliamo il modulo totale: $N = n_1 \cdot n_2 \cdots n_k$.
2. Per ogni equazione $i$, calcoliamo $N_i = \frac{N}{n_i}$ (cioè il prodotto di tutti gli altri moduli).
3. Per ogni $i$, calcoliamo l'inverso moltiplicativo $y_i$ di $N_i$ modulo $n_i$. Risolviamo cioè l'equazione $N_i y_i \equiv 1 \pmod{n_i}$. *(Questo è garantito perché i moduli sono coprimi).*
4. La soluzione generale del sistema si calcola sommando i prodotti:
   $$x = \sum_{i=1}^{k} c_i \cdot N_i \cdot y_i \pmod N$$

> [!EXAMPLE] Risoluzione Passo-Passo
> Risolvere:
> $\begin{cases} x \equiv 2 \pmod 3 \\ x \equiv 3 \pmod 5 \\ x \equiv 2 \pmod 7 \end{cases}$
> - **Coprimalità:** $\text{MCD}(3,5)=\text{MCD}(5,7)=\text{MCD}(3,7)=1$. OK.
> - **1. Modulo totale:** $N = 3 \cdot 5 \cdot 7 = 105$.
> - **2. Calcolo degli $N_i$:**
>   - $N_1 = 105 / 3 = 35$
>   - $N_2 = 105 / 5 = 21$
>   - $N_3 = 105 / 7 = 15$
> - **3. Calcolo degli inversi $y_i$ (risolvo $N_i y_i \equiv 1 \pmod{n_i}$):**
>   - $35 y_1 \equiv 1 \pmod 3 \implies 2 y_1 \equiv 1 \pmod 3 \implies y_1 = 2$.
>   - $21 y_2 \equiv 1 \pmod 5 \implies 1 y_2 \equiv 1 \pmod 5 \implies y_2 = 1$.
>   - $15 y_3 \equiv 1 \pmod 7 \implies 1 y_3 \equiv 1 \pmod 7 \implies y_3 = 1$.
> - **4. Soluzione finale:**
>   - $x = (c_1 \cdot N_1 \cdot y_1) + (c_2 \cdot N_2 \cdot y_2) + (c_3 \cdot N_3 \cdot y_3)$
>   - $x = (2 \cdot 35 \cdot 2) + (3 \cdot 21 \cdot 1) + (2 \cdot 15 \cdot 1)$
>   - $x = 140 + 63 + 30 = 233$
>   - Modulo $105$: $233 = 105 \cdot 2 + 23 \implies x \equiv 23 \pmod{105}$.

---

## Tip d'Esame

> [!TIP] Gestire le Equazioni Iniziali
> Attenzione! Prima di applicare il TCR, assicurati che il sistema sia nella "forma canonica", cioè con la $x$ avente coefficiente 1: $1x \equiv c \pmod n$. Se nel compito trovi un'equazione come $3x \equiv 2 \pmod 5$, **devi prima risolverla** trovando $x \equiv 4 \pmod 5$, e solo a quel punto inserire il 4 nel calcolo del TCR.

---

## Note Correlate
- [[01.0 - MoC Insiemistica e Aritmetica|Unità 1 MoC]]
- [[Congruenze e Aritmetica Modulare]]
