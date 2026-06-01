---
tags:
  - matematica
  - algebra/spazi_vettoriali
aliases:
  - Coordinate
  - Isomorfismo
---
# Coordinate e Isomorfismo con $\mathbb{R}^n$

Grazie al Teorema delle Coordinate (vedi [[Base e Dimensione]]), una volta fissata una base, possiamo rappresentare vettori astratti come "semplici" colonne di numeri. 

## L'Applicazione delle Coordinate
Sia $V$ uno spazio vettoriale e $\mathcal{B} = (v_1, \dots, v_n)$ una sua base. Per ogni vettore $v \in V$, esso si scrive in modo univoco come:
$$ v = c_1 v_1 + c_2 v_2 + \dots + c_n v_n $$
I coefficienti $(c_1, \dots, c_n)$ prendono il nome di **coordinate** del vettore $v$ rispetto alla base $\mathcal{B}$.

L'applicazione $F_{\mathcal{B}}: V \to \mathbb{R}^n$ che associa ad ogni vettore la colonna delle sue coordinate:
$$ F_{\mathcal{B}}(v) = \begin{pmatrix} c_1 \\ \vdots \\ c_n \end{pmatrix} $$
è un **[[Isomorfismi|Isomorfismo]]** di spazi vettoriali.

> [!TIP] Chiameremo Coordinate di $v$ rispetto alla base $B$ il vettore dei coefficienti $(c_{1},\dots , c_{n})$

> [!abstract] Potenza dell'Isomorfismo
> Questo significa che, dal punto di vista strutturale, **tutti** gli spazi vettoriali di dimensione $n$ sono "uguali" (isomorfi) a $\mathbb{R}^n$. Lavorare con le matrici o con i polinomi di grado $\le 2$ è esattamente come lavorare con i vettori di $\mathbb{R}^3$, basta operare sulle loro coordinate!

## Proprietà Conservate
L'isomorfismo conserva la lineare dipendenza e indipendenza:
- $v_1, \dots, v_k \in V$ sono indipendenti $\iff$ le loro coordinate $F_{\mathcal{B}}(v_1), \dots, F_{\mathcal{B}}(v_k) \in \mathbb{R}^n$ sono indipendenti (e puoi metterle in matrice per calcolare il rango).

> [!question]- Esercizio Pratico
> Nello spazio dei polinomi di grado $\le 2$, $\mathbb{R}_{\le 2}[x]$, consideriamo la base canonica $\mathcal{B} = (x^2, x, 1)$.
> Quali sono le coordinate del polinomio $p(x) = 3x^2 - 5$?
> 
> **Soluzione passo-passo:**
> 1. Esprimiamo $p(x)$ come combinazione lineare della base: $p(x) = 3 \cdot (x^2) + 0 \cdot (x) + (-5) \cdot (1)$.
> 2. I coefficienti di questa combinazione lineare sono $3, 0, -5$.
> 3. Le coordinate sono quindi la colonna: $F_{\mathcal{B}}(p(x)) = \begin{pmatrix} 3 \\ 0 \\ -5 \end{pmatrix} \in \mathbb{R}^3$.

## Collegamenti
- Back: [[00_Spazi_Vettoriali_MOC|MOC Spazi Vettoriali]]
- Previous: [[Base e Dimensione]]
- Next: [[Equazioni Parametriche e Cartesiane]]
