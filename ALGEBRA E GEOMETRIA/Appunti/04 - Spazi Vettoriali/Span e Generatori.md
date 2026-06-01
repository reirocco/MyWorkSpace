---
tags:
  - matematica
  - algebra/spazi_vettoriali
aliases:
  - Generatori
  - Spazio Generato
  - Insieme di generatori
---
# Span e Generatori

Dato uno spazio vettoriale $V$ e $k$ vettori $v_1, v_2, \dots, v_k \in V$, lo **Span** (o spazio generato) è l'insieme di tutte le possibili combinazioni lineari di questi vettori:
$$ \text{Span}(v_1, \dots, v_k) = \{ c_1 v_1 + \dots + c_k v_k : c_1, \dots, c_k \in \mathbb{R} \} $$

## Proprietà dello Span
1. **Sottospazio Più Piccolo:** $\text{Span}(v_1, \dots, v_k)$ è un sottospazio vettoriale di $V$ ed è il *più piccolo* sottospazio che contiene i vettori $v_1, \dots, v_k$.
2. **Generatori:** I vettori $v_1, \dots, v_k$ si dicono **generatori** dello spazio $\text{Span}(v_1, \dots, v_k)$.
3. **Dipendenza:** Se un vettore $v$ è combinazione lineare di $v_1, \dots, v_k$, allora aggiungerlo allo Span non "ingrandisce" lo spazio:
   $$ \text{Span}(v_1, \dots, v_k, v) = \text{Span}(v_1, \dots, v_k) $$

> [!info]- Dimostrazione: Span è Sottospazio
> Dobbiamo mostrare che $W = \text{Span}(v_1, \dots, v_k)$ è chiuso rispetto a somma e prodotto.
> Siano $w_1, w_2 \in W$. Essi sono combinazioni lineari dei generatori:
> $w_1 = a_1 v_1 + \dots + a_k v_k$ e $w_2 = b_1 v_1 + \dots + b_k v_k$.
> $w_1 + w_2 = (a_1+b_1)v_1 + \dots + (a_k+b_k)v_k$. Questa è ancora una combinazione lineare dei $v_i$, dunque appartiene a $W$.
> Se $c \in \mathbb{R}$, $c \cdot w_1 = (c a_1)v_1 + \dots + (c a_k)v_k \in W$. 
> Dunque lo Span è un sottospazio vettoriale.

> [!question]- Esercizio Pratico
> In $\mathbb{R}^3$, lo Span dei vettori $v_1 = (1, 0, 0)$ e $v_2 = (0, 1, 0)$ che cos'è geometricamente?
> 
> **Soluzione passo-passo:**
> 1. Un vettore generico dello Span è dato da $c_1 v_1 + c_2 v_2$.
> 2. Calcolando la combinazione: $c_1(1,0,0) + c_2(0,1,0) = (c_1, 0, 0) + (0, c_2, 0) = (c_1, c_2, 0)$.
> 3. L'insieme generato contiene tutti e soli i vettori che hanno la terza componente nulla ($z = 0$).
> 4. Geometricamente, questo è il **piano $xy$**.

## Collegamenti
- Back: [[00_Spazi_Vettoriali_MOC|MOC Spazi Vettoriali]]
- Previous: [[Sottospazi Vettoriali]]
- Next: [[Base e Dimensione]]
