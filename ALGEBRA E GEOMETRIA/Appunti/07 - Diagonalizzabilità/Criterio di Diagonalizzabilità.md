---
tags:
  - matematica
  - algebra/diagonalizzabilità
aliases:
  - Criterio di Diagonalizzabilità
  - Endomorfismo Diagonalizzabile
---
# Criterio di Diagonalizzabilità

L'obiettivo della diagonalizzazione è trovare una **base di autovettori**. Se lo spazio vettoriale ha dimensione $n$, dobbiamo trovare $n$ autovettori linearmente indipendenti. Quando ciò è possibile, l'endomorfismo $T$ (o la matrice $A$) si dice **diagonalizzabile** e assume, rispetto a tale base, una forma matriciale $D$ diagonale, in cui i numeri sulla diagonale principale sono proprio gli autovalori.

Il **Criterio di Diagonalizzabilità** stabilisce esattamente le condizioni necessarie e sufficienti affinché questo avvenga.

---

## 1. Molteplicità (Richiamo)

Per comprendere il criterio, richiamiamo le due tipologie di molteplicità per un autovalore $\lambda$:
* **Molteplicità Algebrica $m_a(\lambda)$:** È il numero di volte in cui $\lambda$ è radice del polinomio caratteristico (il suo "peso" algebrico).
* **Molteplicità Geometrica $m_g(\lambda)$:** È la dimensione del suo autospazio, ovvero il numero di autovettori linearmente indipendenti che esso genera. Si calcola come $m_g(\lambda) = \dim(E_\lambda) = n - \text{rango}(A - \lambda I)$.

Vale sempre la disuguaglianza fondamentale:
$$ 1 \le m_g(\lambda) \le m_a(\lambda) \le n $$

---

## 2. Il Teorema (Criterio Generale)

> [!abstract] Criterio di Diagonalizzabilità
> Una matrice $A \in M_n(\mathbb{R})$ è **diagonalizzabile su $\mathbb{R}$ se e solo se** valgono **entrambe** le seguenti condizioni:
> 
> 1. **Fattorizzazione completa:** Il polinomio caratteristico $p_A(t)$ ammette $n$ radici reali, contate con la loro molteplicità algebrica. (In altre parole, la somma delle molteplicità algebriche di tutti gli autovalori reali deve fare $n$).
> 2. **Coincidenza delle molteplicità:** Per **ogni** autovalore $\lambda_i$, la molteplicità algebrica deve coincidere con la molteplicità geometrica:
>    $$ m_a(\lambda_i) = m_g(\lambda_i) \quad \forall i $$

### La Dimostrazione (Logica del Teorema)
Se vale il criterio, sommiamo le dimensioni di tutti gli autospazi: $\sum m_g(\lambda_i)$. Per la condizione (2), questa somma è $\sum m_a(\lambda_i)$, che per la condizione (1) fa esattamente $n$. Poiché autovettori di autovalori distinti sono linearmente indipendenti, l'unione delle basi dei vari autospazi non ha sovrapposizioni e fornisce in totale $n$ vettori linearmente indipendenti. Abbiamo quindi costruito una base dell'intero spazio formata da autovettori.

---

## 3. Corollario degli Autovalori Distinti (Heuristic d'Esame)

Esiste un caso molto fortunato in cui la diagonalizzabilità è garantita senza dover calcolare alcun rango o autospazio.

> [!success] Teorema (Condizione Sufficiente)
> Se il polinomio caratteristico di una matrice di ordine $n$ ha **$n$ radici reali e distinte**, allora la matrice è **sicuramente diagonalizzabile**.

**Perché funziona?**
Se le $n$ radici sono distinte, significa che la molteplicità algebrica di ciascun autovalore è esattamente $1$ ($m_a = 1$). 
Poiché vale sempre che $1 \le m_g \le m_a$, se $m_a = 1$, la molteplicità geometrica è costretta in una "morsa" e deve per forza essere anch'essa $1$ ($m_g = 1$). L'uguaglianza $m_a = m_g$ è automaticamente verificata per tutti gli autovalori!

---

## 4. Attenzione agli Autovalori Coincidenti (Trappola)

> [!danger] L'Errore Comune
> Molti studenti credono che se un autovalore ha molteplicità algebrica $m_a > 1$, la matrice NON sia diagonalizzabile. **È FALSO**.
> Se un autovalore ha $m_a > 1$, la matrice *potrebbe* comunque essere diagonalizzabile. Semplicemente, il criterio sufficiente (sopra) non si applica. Sei obbligato a **calcolare il rango** di $(A - \lambda I)$ per verificare se anche $m_g = m_a$.
> 
> *Esempio banale:* La matrice Identità $I_n$ è banalmente diagonale (quindi diagonalizzabile). Essa ha l'autovalore $1$ con molteplicità algebrica $m_a = n$. Ma $(I - 1\cdot I) = \mathbf{0}$, matrice di rango zero. Quindi $m_g = n - 0 = n$. L'uguaglianza $m_a = m_g = n$ è verificata.

---
## Collegamenti
* **Back:** [[00_Diagonalizzabilita_MOC|MOC Diagonalizzabilità]]
* **Previous:** [[Molteplicità Algebrica e Geometrica]]
* **Next:** [[Algoritmo Pratico di Diagonalizzazione]]
