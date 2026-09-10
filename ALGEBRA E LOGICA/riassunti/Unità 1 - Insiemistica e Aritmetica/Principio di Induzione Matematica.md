---
tags:
  - induzione
  - logica-matematica
  - dimostrazioni
  - algebra
type: atomic
unit: 1
---

# Principio di Induzione Matematica

Il **Principio di Induzione Matematica** è un metodo di dimostrazione fondamentale per affermare che una proprietà $P(n)$ è vera per tutti i numeri naturali $n \in \mathbb{N}$ (oppure per ogni $n \ge n_0$).

Può essere visualizzato metaforicamente come l'effetto domino:
1. Devi essere in grado di abbattere la prima tessera (Base Induttiva).
2. Devi essere sicuro che la caduta di una tessera qualsiasi comporti la caduta della successiva (Passo Induttivo).

---

## Il Procedimento (Le Due Fasi)

La dimostrazione si compone sempre di due passaggi inseparabili:

### 1. Passo Base (Base dell'Induzione)
Si dimostra che la proprietà $P(n)$ è vera per il primo numero naturale considerato, solitamente $n = 0$ o $n = 1$.
$$P(n_0) \text{ è VERA}$$

### 2. Passo Induttivo
Si assume per ipotesi che la proprietà sia vera per un generico $n = k \ge n_0$ (**Ipotesi Induttiva**) e, usando questa assunzione, si dimostra formalmente che essa è vera anche per il successivo, cioè per $n = k + 1$ (**Tesi Induttiva**).
$$P(k) \implies P(k+1) \quad \forall k \ge n_0$$

Se entrambe le condizioni sono soddisfatte, allora $P(n)$ è vera $\forall n \ge n_0$.

> [!EXAMPLE] Dimostrazione Classica (Somma dei primi $n$ interi)
> Dimostriamo che $S_n = \sum_{i=1}^n i = \frac{n(n+1)}{2}$.
> **1. Passo Base:** Per $n = 1$, la somma del primo numero è $1$. La formula dà $\frac{1(1+1)}{2} = \frac{2}{2} = 1$. Il passo base regge.
> **2. Passo Induttivo:** Assumiamo vero che per $k$ si abbia $\sum_{i=1}^k i = \frac{k(k+1)}{2}$ (Ipotesi Induttiva).
> Dobbiamo dimostrare la tesi per $k+1$, cioè che $\sum_{i=1}^{k+1} i = \frac{(k+1)(k+2)}{2}$.
> Scriviamo: $\sum_{i=1}^{k+1} i = \left(\sum_{i=1}^k i\right) + (k+1)$.
> Sostituiamo l'ipotesi induttiva: $= \frac{k(k+1)}{2} + (k+1)$.
> Mettendo a denominatore comune: $= \frac{k(k+1) + 2(k+1)}{2}$.
> Raccogliendo $(k+1)$: $= \frac{(k+1)(k+2)}{2}$. La tesi è dimostrata.

---

## Forme Alternative dell'Induzione

### Induzione Forte (o Completa)
Nel passo induttivo forte, si assume che la proprietà sia vera **non solo per $k$**, ma per **tutti i valori precedenti fino a $k$**.
**Ipotesi:** $P(n_0), P(n_0+1), \dots, P(k)$ sono vere.
**Tesi:** $P(k+1)$ è vera.
*Viene spesso utilizzata nell'Aritmetica, ad esempio nella dimostrazione del Teorema Fondamentale dell'Aritmetica.*

---

## Tip d'Esame

> [!TIP] Consigli per le Dimostrazioni all'Esame
> - **Dichiara sempre esplicitamente l'Ipotesi Induttiva:** I docenti valutano severamente chi salta questo passaggio. Scrivi "Assumiamo per ipotesi induttiva che $P(k)$ sia vera...".
> - **Sottolinea dove usi l'ipotesi:** Durante i passaggi algebrici del passo induttivo, quando sostituisci o sfrutti l'ipotesi, indicalo chiaramente a margine (es. "*(per ipotesi induttiva)*").
> - **Non barare sui passaggi algebrici:** Non saltare direttamente dal primo termine del passo induttivo al risultato finale; il cuore dell'esercizio è far vedere che sai manipolare l'espressione in modo da far saltar fuori il termine atteso.

---

## Note Correlate
- [[01.0 - MoC Insiemistica e Aritmetica|Unità 1 MoC]]
- [[Divisibilità e Algoritmo di Euclide]]
