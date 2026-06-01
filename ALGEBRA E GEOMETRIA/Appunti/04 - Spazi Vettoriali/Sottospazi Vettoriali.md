---
tags:
  - matematica
  - algebra/spazi_vettoriali
aliases:
  - Sottospazio vettoriale
---
# Sottospazi Vettoriali

Un sottoinsieme $W \subseteq V$ (con $W \neq \emptyset$) di uno spazio vettoriale $V$ è un **sottospazio vettoriale** se esso stesso è uno spazio vettoriale rispetto alle operazioni ereditate da $V$. 

Per verificare se $W$ è un sottospazio, bastano due controlli di **chiusura**:
1. **Chiusura rispetto alla somma**: $\forall w_1, w_2 \in W \implies w_1 + w_2 \in W$.
2. **Chiusura rispetto al prodotto**: $\forall c \in \mathbb{R}, \forall w \in W \implies c \cdot w \in W$.

> [!tip] Test Veloce (Lo Zero)
> Poiché un sottospazio deve essere chiuso rispetto al prodotto, se prendiamo $c = 0$, otteniamo $0 \cdot w = \mathbf{0}_V \in W$. 
> **Se il vettore nullo $\mathbf{0}_V$ NON appartiene a $W$, allora $W$ NON è un sottospazio vettoriale!** (Questo è il test più rapido per scartare opzioni nei quiz).

> [!abstract] Sottospazi Geometrici (Teorema)
> Un sottoinsieme $S \subseteq \mathbb{R}^n$ è un sottospazio vettoriale di $\mathbb{R}^n$ **se e solo se** è l'insieme delle soluzioni di un sistema lineare **omogeneo** $AX = \mathbf{0}$.

> [!info]- Dimostrazione del Teorema
> Se $S$ è dato dalle soluzioni di $AX = \mathbf{0}$, allora per $X_1, X_2 \in S$:
> $A(X_1 + X_2) = AX_1 + AX_2 = \mathbf{0} + \mathbf{0} = \mathbf{0} \implies X_1 + X_2 \in S$.
> Per $c \in \mathbb{R}$: $A(cX_1) = c(AX_1) = c(\mathbf{0}) = \mathbf{0} \implies cX_1 \in S$.
> Essendo chiuso per somma e prodotto e contenendo $\mathbf{0}$ ($A\mathbf{0} = \mathbf{0}$), $S$ è un sottospazio vettoriale.

> [!question]- Esercizio Pratico
> Stabilisci se $W = \{ (x, y, z) \in \mathbb{R}^3 : x + y = 1 \}$ è un sottospazio vettoriale.
> 
> **Soluzione passo-passo:**
> 1. Facciamo il test dello zero. Il vettore nullo di $\mathbb{R}^3$ è $(0,0,0)$.
> 2. Sostituiamo nell'equazione: $0 + 0 = 0 \neq 1$.
> 3. Il vettore nullo non appartiene a $W$. Dunque $W$ **non è** un sottospazio vettoriale (si tratta invece di un [[Sottospazi Affini|Sottospazio Affine]]).

## Collegamenti
- Back: [[00_Spazi_Vettoriali_MOC|MOC Spazi Vettoriali]]
- Previous: [[Definizione di Spazio Vettoriale]]
- Next: [[Span e Generatori]]
