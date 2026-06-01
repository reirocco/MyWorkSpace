---
tags:
  - matematica
  - algebra/sistemi
aliases:
  - AX=B
  - Notazione matriciale sistemi
---

# Definizione di Sistema Lineare e Notazione Matriciale

Un **sistema lineare** $\Sigma$ di $m$ equazioni in $n$ incognite $x_1, \dots, x_n$ è un insieme di equazioni di primo grado della forma:

$$
\begin{cases}
a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n = b_1 \\
a_{21}x_1 + a_{22}x_2 + \dots + a_{2n}x_n = b_2 \\
\vdots \\
a_{m1}x_1 + a_{m2}x_2 + \dots + a_{mn}x_n = b_m
\end{cases}
$$

## Rappresentazione Matriciale
Il sistema può essere compresso nell'equazione matriciale:
$$ A \cdot X = B $$

Dove:
- **Matrix incompleta ($A \in M_{m,n}$):** Contiene i coefficienti $a_{ij}$.
- **Vector delle incognite ($X \in M_{n,1}$):** La colonna $(x_1, \dots, x_n)^T$.
- **Vector dei termini noti ($B \in M_{m,1}$):** La colonna $(b_1, \dots, b_m)^T$.

> [!abstract] Matrice Completa $(A|B)$
> La matrice $C = (A|B) \in M_{m, n+1}$ si ottiene affiancando la colonna $B$ alla matrice $A$. È lo strumento principale per applicare il [[Teorema di Rouché-Capelli]].

## Classificazione delle Soluzioni
Un sistema può essere:
- **Compatibile:** Ammette almeno una soluzione.
  - *Determinato:* Unica soluzione.
  - *Indeterminato:* Infinite soluzioni.
- **Incompatibile:** Non ammette soluzioni (sistema impossibile).

> [!tip] Visualizzazione Geometrica (2 incognite)
> In $\mathbb{R}^2$, ogni equazione lineare rappresenta una retta. Risolvere il sistema significa trovare l'intersezione tra queste rette.

## Collegamenti
- Back: [[00_Sistemi_Lineari_MOC|MOC Sistemi Lineari]]
- Next: [[Teorema di Rouché-Capelli]]
