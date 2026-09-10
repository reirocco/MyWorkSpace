---
tags:
  - reticoli
  - algebra-booleana
  - algebra
type: atomic
unit: 2
---

# Reticoli e Reticoli Booleani

Un **Reticolo** (Lattice) è una struttura matematica che funge da ponte tra la teoria degli insiemi (e degli ordini) e l'algebra astratta (le operazioni).

## Definizione di Reticolo

Un POSET $(L, \le)$ è un **Reticolo** se e solo se:
> **Ogni coppia** di elementi $\{x, y\}$ ammette sempre sia un Estremo Superiore ($\sup$) che un Estremo Inferiore ($\inf$).

In un reticolo si definiscono due operazioni binarie fondamentali (simili a somma e prodotto):
- **Join (Unione, $\lor$):** $x \lor y = \sup\{x, y\}$
- **Meet (Intersezione, $\land$):** $x \land y = \inf\{x, y\}$

Grazie a queste operazioni, il reticolo diventa una struttura algebrica $(L, \lor, \land)$ in cui valgono proprietà di Idempotenza, Commutatività, Associatività e le **Leggi di Assorbimento**:
$x \lor (x \land y) = x \quad \text{e} \quad x \land (x \lor y) = x$

> [!EXAMPLE] L'insieme delle parti come Reticolo
> L'insieme delle parti $\mathcal{P}(A)$, ordinato tramite l'inclusione $\subseteq$, è il reticolo perfetto.
> Dati due insiemi $X$ e $Y$:
> - L'estremo superiore ($X \lor Y$) è l'**Unione** $X \cup Y$.
> - L'estremo inferiore ($X \land Y$) è l'**Intersezione** $X \cap Y$.

---

## Reticoli Distributivi, Limitati e Complementati

### 1. Reticoli Limitati
Un reticolo si dice **limitato** se possiede un **Minimo globale** (chiamato $0$) e un **Massimo globale** (chiamato $1$).
- $x \lor 0 = x \quad \text{e} \quad x \land 1 = x$
- $x \lor 1 = 1 \quad \text{e} \quad x \land 0 = 0$

### 2. Reticoli Distributivi
Un reticolo è distributivo se gli operatori $\lor$ e $\land$ si distribuiscono l'uno sull'altro:
- $x \land (y \lor z) = (x \land y) \lor (x \land z)$
- $x \lor (y \land z) = (x \lor y) \land (x \lor z)$

### 3. Reticoli Complementati
In un reticolo limitato (con $0$ e $1$), si dice che un elemento $y$ è il **complemento** di $x$ se:
- $x \lor y = 1$
- $x \land y = 0$
Se *ogni* elemento possiede almeno un complemento, il reticolo è complementato.

---

## Reticoli Booleani

> [!IMPORTANT] Algebra di Boole
> Un **Reticolo Booleano** (o Algebra di Boole) è un reticolo che è contemporaneamente:
> **Limitato + Distributivo + Complementato**.
> In un reticolo distributivo, se il complemento esiste, è **unico** e si indica con $x'$ o $\bar{x}$.

Nei reticoli booleani valgono le **Leggi di De Morgan**, le stesse della logica proposizionale e degli insiemi.

> [!TIP] Riconoscere un Reticolo Booleano all'Esame
> Per verificare se un diagramma di Hasse rappresenta un reticolo booleano, usa queste due scorciatoie (che sono Teoremi di Struttura):
> 1. Un reticolo non può essere booleano se contiene un sotto-reticolo a forma di "Pentagono" (N5) o "Diamante" (M3). Questi due violano la distributività.
> 2. Se è booleano e finito, il numero totale di elementi **deve essere una potenza di 2** ($2^n$). Se l'insieme ha 6 o 10 elementi, escludi a priori che sia un'algebra di Boole!

---

## Note Correlate
- [[01.0 - MoC Relazioni di Equivalenza e d'Ordine|Unità 2 MoC]]
- [[Elementi Notevoli negli Insiemi Ordinati]]
- [[Sintassi e Semantica della Logica Proposizionale]]
