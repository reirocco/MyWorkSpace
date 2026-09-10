---
tags:
  - esercizi
  - scheda3
  - gruppi
  - permutazioni
  - lagrange
type: exercise_sheet
unit: 3
---

# Scheda 3: Teoria dei Gruppi e Permutazioni

Questa nota sintetizza gli esercizi guida relativi alla **teoria dei gruppi**, all'algebra delle **permutazioni** e alle applicazioni del **Teorema di Lagrange**.

---

## 1. Calcolo con Permutazioni in $S_n$

### Esempio Tipo
> Siano $\sigma = (1 \; 3 \; 4)(2 \; 5)$ e $\tau = (1 \; 2 \; 5 \; 3)$ in $S_5$.
> 1. Calcolare $\sigma \circ \tau$.
> 2. Determinare l'ordine $o(\sigma \circ \tau)$.
> 3. Determinare il segno $\text{sgn}(\sigma \circ \tau)$.

### Procedura Risolutiva
1. **Composizione (da destra a sinistra):**
   - $1 \xrightarrow{\tau} 2 \xrightarrow{\sigma} 5$
   - $5 \xrightarrow{\tau} 3 \xrightarrow{\sigma} 4$
   - $4 \xrightarrow{\tau} 4 \xrightarrow{\sigma} 1$
   - $2 \xrightarrow{\tau} 5 \xrightarrow{\sigma} 2$
   - $3 \xrightarrow{\tau} 1 \xrightarrow{\sigma} 3$
   - Risultato: $\sigma \circ \tau = (1 \; 5 \; 4)(2)(3) = (1 \; 5 \; 4)$.
2. **Ordine:** $\sigma \circ \tau$ è un 3-ciclo $\implies o(\sigma \circ \tau) = 3$.
3. **Segno:** Un 3-ciclo è pari, infatti $(1 \; 5 \; 4) = (1 \; 4)(1 \; 5)$ (2 trasposizioni) $\implies \text{sgn} = +1$.

---

## ⭕ 2. Subgruppi e Teorema di Lagrange

### Esempio Tipo
> Trovare tutti i sottogruppi del gruppo ciclico $\mathbb{Z}_{12}$.

### Procedura Risolutiva
Per il Teorema sui gruppi ciclici, esiste un unico sottogruppo per ogni divisore $d \mid 12$:
- Divisori di 12: $d \in \{1, 2, 3, 4, 6, 12\}$.
- $d=1 \implies \{[0]\}$.
- $d=2 \implies \langle [6] \rangle = \{[0], [6]\}$.
- $d=3 \implies \langle [4] \rangle = \{[0], [4], [8]\}$.
- $d=4 \implies \langle [3] \rangle = \{[0], [3], [6], [9]\}$.
- $d=6 \implies \langle [2] \rangle = \{[0], [2], [4], [6], [8], [10]\}$.
- $d=12 \implies \mathbb{Z}_{12}$.

---

## Note Correlate
- [[03.0 - MoC Gruppi|Unità 3 MoC]]
- [[Gruppo delle Permutazioni Sn]]
- [[Classi Laterali e Teorema di Lagrange]]
- [[Gruppi Ciclici e Generatori]]
