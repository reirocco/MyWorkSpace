---
tags:
  - matematica
  - algebra/matrici
aliases:
  - Combinazioni lineari matrici
  - Dipendenza Lineare
  - Indipendenza Lineare
---

# Dipendenza e Indipendenza Lineare (Matrici)

## Combinazione Lineare
Una **combinazione lineare** di un insieme di matrici $A_1, A_2, \dots, A_k \in M_{m,n}$ è una matrice così formata:
$$
\lambda_1 A_1 + \lambda_2 A_2 + \dots + \lambda_k A_k
$$
dove $\lambda_1, \dots, \lambda_k$ sono coefficienti (scalari) in $\mathbb{R}$.

## Definizioni Principali

Le matrici $A_1, \dots, A_k$ si dicono:
1. **Linearmente Dipendenti** (L.D.): se esistono coefficienti $\lambda_1, \dots, \lambda_k$ **non tutti nulli** tali che:
$$
\lambda_1 A_1 + \dots + \lambda_k A_k = 0
$$

2. **Linearmente Indipendenti** (L.I.): se l'**unica** combinazione lineare che dà la matrice nulla è quella con tutti i coefficienti uguali a zero:
$$
\lambda_1 A_1 + \dots + \lambda_k A_k = 0 \iff \lambda_1 = \dots = \lambda_k = 0
$$

> [!abstract] Teorema della Dipendenza Lineare
> Le matrici $A_1, \dots, A_k$ sono linearmente dipendenti **se e solo se** almeno una è combinazione lineare delle altre.

> [!info]- Dimostrazione (Teorema)
> **( $\implies$ )** Supponiamo per semplicità che $A_1 = \lambda_2 A_2 + \dots + \lambda_k A_k$.
> Allora $A_1 - \lambda_2 A_2 - \dots - \lambda_k A_k = 0$. Questa è una combinazione lineare a coefficienti non tutti nulli (il coefficiente di $A_1$ è $1 \neq 0$) che dà la matrice nulla, dunque sono L.D.
> **( $\impliedby$ )** Supponiamo che esistano $\alpha_1, \dots, \alpha_k \in \mathbb{R}$ non tutti nulli tali che $\alpha_1 A_1 + \dots + \alpha_k A_k = 0$. Assumiamo $\alpha_1 \neq 0$.
> Allora possiamo isolare $A_1$:
> $$
> A_1 = - \frac{\alpha_2}{\alpha_1} A_2 - \dots - \frac{\alpha_k}{\alpha_1} A_k
> $$
> Ovvero $A_1$ è combinazione lineare delle restanti matrici.

> [!tip] Regole d'oro rapide (Casi Speciali)
> - **Una singola matrice** $A \neq 0$ pesa da sola è sempre **Lineare Indipendente**.
> - Un insieme che **contiene la matrice nulla** $0$ è sempre **L.D.**
> - **Due matrici** sono L.D. *se e solo se* sono una multiplo scalare dell'altra.

> [!question]- Esercizio Pratico
> Stabilisci se $A_1 = \begin{pmatrix} 1 & 2 & 3 \end{pmatrix}$, $A_2 = \begin{pmatrix} 0 & 4 & 1 \end{pmatrix}$ e $A_3 = \begin{pmatrix} 2 & 0 & 5 \end{pmatrix}$ sono L.D. o L.I.
> 
> **Soluzione passo-passo:**
> Dobbiamo cercare sennò se una è combinazione delle altre o se $\lambda_1 A_1 + \lambda_2 A_2 + \lambda_3 A_3 = 0$ ha soluzioni non banali.
> Notiamo che $2 A_1 - A_2$:
> $2 \begin{pmatrix} 1 & 2 & 3 \end{pmatrix} - \begin{pmatrix} 0 & 4 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 4 & 6 \end{pmatrix} - \begin{pmatrix} 0 & 4 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 0 & 5 \end{pmatrix} = A_3$
> Poiché $2A_1 - A_2 - A_3 = 0$ è una combinazione lineare nulla con coefficienti non nulli $(2, -1, -1)$, le matrici sono **Linearmente Dipendenti**.

## Collegamenti
- Back: [[01 - Matrici]]
- Previous: [[Operazioni su Matrici]]
