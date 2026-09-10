---
tags:
  - campi
  - caratteristica
  - algebra
type: atomic
unit: 4
---

# Definizione di Campo e Caratteristica

I **Campi** (Fields in inglese) rappresentano la struttura algebrica "ideale" per fare i conti. Nei campi, non solo si può sommare, sottrarre e moltiplicare (come negli anelli), ma si può sempre **dividere** per qualsiasi elemento non nullo.

## Definizione Formale di Campo

Un **Campo** $(K, +, \cdot)$ è un anello commutativo unitario (con $1 \neq 0$) in cui **ogni elemento non nullo possiede un inverso moltiplicativo**.

In termini di assiomi di gruppo, significa che:
1. $(K, +)$ è un Gruppo Abeliano (con neutro $0$).
2. $(K \setminus \{0\}, \cdot)$ è un **Gruppo Abeliano** (con neutro $1$).
3. Vale la proprietà distributiva del prodotto rispetto alla somma.

> [!IMPORTANT] Teorema del Campo Finito
> Poiché in un campo tutti gli elementi non nulli sono invertibili, è impossibile trovare due elementi non nulli il cui prodotto sia zero (se $ab=0$, moltiplico per $a^{-1}$ e ottengo $b=0$). Quindi:
> **Ogni campo è un Dominio di Integrità.**
> *(Il viceversa è falso in generale. $\mathbb{Z}$ è un dominio ma non è un campo, perché 2 non ha inverso in $\mathbb{Z}$).*
>
> TUTTAVIA: **Ogni Dominio di Integrità FINITO è un Campo.** (Teorema fondamentale!).

> [!EXAMPLE] Campi Famosi
> - $\mathbb{Q}, \mathbb{R}, \mathbb{C}$ sono campi infiniti.
> - $\mathbb{Z}_p$ (classi di resto modulo $p$, con $p$ **primo**) è un campo finito (o Campo di Galois, $GF(p)$). Tutte le classi non nulle sono invertibili.

---

## Caratteristica di un Anello/Campo

Cosa succede se, in un campo, iniziamo a sommare l'elemento neutro $1$ a se stesso ripetutamente?
$1 + 1 + 1 + \dots + 1$

La **Caratteristica** di un anello unitario $R$, indicata con $\text{char}(R)$, è il più piccolo numero intero positivo $n$ tale che:
$$ \underbrace{1 + 1 + \dots + 1}_{n \text{ volte}} = 0 $$
Se questa somma non fa mai zero (indipendentemente da quanti "1" sommiamo), si dice che l'anello ha **caratteristica $0$**.

- $\text{char}(\mathbb{Z}) = \text{char}(\mathbb{Q}) = \text{char}(\mathbb{R}) = 0$. (Infatti $1+1=2 \neq 0$).
- $\text{char}(\mathbb{Z}_n) = n$. (Perché in modulo $n$, $n$ volte $1$ fa esattamente $n \equiv 0$).

> [!IMPORTANT] Caratteristica di un Dominio / Campo
> La caratteristica di un dominio di integrità (e quindi di qualsiasi campo) può essere **solo 0 oppure un numero Primo $p$**. Non esistono campi di caratteristica 6.

---

## Tip d'Esame

> [!TIP] Calcolare l'inverso in $\mathbb{Z}_p$
> Quando sei in un campo $\mathbb{Z}_p$ e devi trovare l'inverso di $[a]$, usa il **Piccolo Teorema di Fermat**:
> $a^{p-1} \equiv 1 \pmod p$
> Questo implica che l'inverso è dato da $a^{p-2}$.
> Esempio: inverso di 3 in $\mathbb{Z}_7$. Calcola $3^{7-2} = 3^5 = 243$. In modulo $7$: $243 = 7 \cdot 34 + 5$. Quindi $3^{-1} \equiv 5 \pmod 7$. (E infatti $3 \cdot 5 = 15 \equiv 1 \pmod 7$).

---

## Note Correlate
- [[04.0 - MoC Anelli e Campi|Unità 4 MoC]]
- [[Definizione di Anello e Domini di Integrità]]
- [[Anelli di Polinomi e Divisibilità]]
