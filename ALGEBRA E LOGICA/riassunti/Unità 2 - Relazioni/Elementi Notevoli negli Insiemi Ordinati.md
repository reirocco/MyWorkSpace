---
tags:
  - ordine
  - massimale
  - estremo-superiore
  - algebra
type: atomic
unit: 2
---

# Elementi Notevoli negli Insiemi Ordinati

All'interno di un insieme parzialmente ordinato (POSET) $(A, \le)$, è possibile identificare degli elementi con caratteristiche speciali. La distinzione tra questi elementi è fondamentale, poiché in un ordine *parziale* concetti come "il più grande" non sono sempre univoci come nell'ordine totale.

---

## Massimale / Minimale vs. Massimo / Minimo

### Elemento Massimo e Minimo
- **Massimo (Globale):** Un elemento $M \in A$ è il massimo se è maggiore o uguale a **tutti** gli altri elementi di $A$. ($\forall x \in A, x \le M$). Se esiste, è **unico**.
- **Minimo (Globale):** Un elemento $m \in A$ è il minimo se è minore o uguale a **tutti** gli altri. ($\forall x \in A, m \le x$). Se esiste, è **unico**.

### Elementi Massimali e Minimali
Nei POSET possono esserci elementi "in cima" o "in fondo" a percorsi che però non sono confrontabili tra loro.
- **Massimale:** Un elemento $x$ è massimale se **non c'è nessuno strettamente maggiore di lui**. (Non esiste $y \in A$ tale che $x < y$).
- **Minimale:** Un elemento $x$ è minimale se **non c'è nessuno strettamente minore di lui**. (Non esiste $y \in A$ tale che $y < x$).

> [!NOTE] Relazione Cruciale
> - Il Massimo, se esiste, è certamente un massimale (ed è l'unico!).
> - Possono esistere più elementi massimali in un POSET. Se ce n'è più di uno, allora **non esiste** il Massimo assoluto.
> - *(Idem per il minimo/minimale)*.
> Nel diagramma di Hasse: i massimali sono i "nodi senza fili che salgono"; i minimali sono i "nodi senza fili che scendono".

---

## Maggioranti, Minoranti ed Estremi

Prendiamo un **sottoinsieme** $S \subseteq A$.

### Maggioranti e Minoranti
- Un elemento $x \in A$ è un **maggiorante** per $S$ se $x$ è maggiore o uguale a tutti gli elementi di $S$. ($\forall s \in S, s \le x$).
- Un elemento $y \in A$ è un **minorante** per $S$ se $y$ è minore o uguale a tutti gli elementi di $S$. ($\forall s \in S, y \le s$).
*(Attenzione: maggioranti e minoranti devono stare in $A$, ma non per forza in $S$!)*

### Sup (Estremo Superiore) e Inf (Estremo Inferiore)
L'insieme di tutti i maggioranti (se non è vuoto) è un sotto-POSET.
- **Estremo Superiore ($\sup S$):** È il **minimo dei maggioranti**. Cioè, tra tutti gli elementi che stanno sopra tutto $S$, è quello "più in basso".
- **Estremo Inferiore ($\inf S$):** È il **massimo dei minoranti**.

> [!EXAMPLE] Analisi delle Differenze
> Consideriamo l'intervallo aperto di numeri reali $S = (0, 1)$ nell'insieme $A = \mathbb{R}$.
> - **Massimo di S:** Non esiste, perché non c'è un numero più grande in $(0, 1)$.
> - **Maggioranti di S:** Qualsiasi numero $\ge 1$ (es. $1, 2, 5.5, 100$).
> - **Estremo Superiore (Sup) di S:** È l'elemento $1$, poiché è il più piccolo tra i maggioranti.
> Notare come $1 \notin S$. Se $S$ fosse stato $[0, 1]$, allora il Massimo sarebbe stato $1$, e coinciderebbe col Sup.

---

## Tip d'Esame

> [!TIP] Come scovare le differenze in Hasse
> - Quando cerchi il **Maggiorante** di due elementi (es. $x, y$), devi trovare i nodi a cui si può arrivare "salendo" **sia da $x$ che da $y$**.
> - Il **Sup($x, y$)** sarà il primissimo nodo che incontri seguendo la regola precedente (il minimo dei maggioranti). Se due maggioranti sono inconfrontabili e non ce n'è uno minimo, allora il Sup non esiste.
> - Confondere Massimo e Massimale è l'errore più penalizzato negli scritti. Se ci sono "due cime" scollegate nel grafo, scrivi subito: "Non c'è Massimo assoluto. I massimali sono...".

---

## Note Correlate
- [[01.0 - MoC Relazioni di Equivalenza e d'Ordine|Unità 2 MoC]]
- [[Relazioni d'Ordine e Diagrammi di Hasse]]
- [[Reticoli e Reticoli Booleani]]
