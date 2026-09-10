---
tags:
  - esercizi
  - scheda2
  - relazioni
  - equivalenza
  - hasse
type: exercise_sheet
unit: 2
---

# Scheda 2: Relazioni di Equivalenza e d'Ordine

Questa nota raccoglie la tipologia di esercizi relativi alle **relazioni binarie**, alla costruzione delle **classi di equivalenza** e all'analisi dei **diagrammi di Hasse**.

---

## 1. Verifica di Relazione di Equivalenza e Classi

### Esempio Tipo
> Su $\mathbb{Z}$, si consideri la relazione $x \sim y \iff 4 \mid (x^2 - y^2)$.
> Dimostrare che è di equivalenza e determinare le classi di equivalenza.

### Procedura Risolutiva
1. **Riflessiva:** $x^2 - x^2 = 0$, $4 \mid 0$. (OK)
2. **Simmetrica:** $4 \mid (x^2 - y^2) \implies 4 \mid -(x^2 - y^2) \implies 4 \mid (y^2 - x^2)$. (OK)
3. **Transitiva:** $x^2 - y^2 = 4k$, $y^2 - z^2 = 4h \implies x^2 - z^2 = 4(k+h)$. (OK)
4. **Classi di Equivalenza:**
   Scomponi $x^2 - y^2 = (x-y)(x+y)$. Nota che $x^2 \pmod 4 \in \{0, 1\}$.
   - Le classi sono $[0]$ (i numeri pari) e $[1]$ (i numeri dispari).

---

## 2. Analisi Poset e Diagramma di Hasse

### Esempio Tipo
> Considera l'insieme dei divisori di 30: $D_{30} = \{1, 2, 3, 5, 6, 10, 15, 30\}$ ordinato per divisibilità.
> Tracciare il diagramma di Hasse e trovare massimali, minimali, massimo, minimo.

### Procedura Risolutiva
1. **Livelli del Diagramma:**
   - Livello 0: 1 (minimo globale).
   - Livello 1 (Primi): 2, 3, 5.
   - Livello 2 (Prodotti di due primi): 6, 10, 15.
   - Livello 3: 30 (massimo globale).
2. **Elementi Notevoli:**
   - **Minimo:** 1.
   - **Massimo:** 30.
   - **Reticolo:** È un reticolo Booleano isomorfo a $(\mathcal{P}(\{2,3,5\}), \subseteq)$.

---

## Note Correlate
- [[02.0 - MoC Relazioni di Equivalenza e d'Ordine|Unità 2 MoC]]
- [[Relazioni di Equivalenza e Classi di Equivalenza]]
- [[Relazioni d'Ordine e Diagrammi di Hasse]]
- [[Reticoli e Reticoli Booleani]]
