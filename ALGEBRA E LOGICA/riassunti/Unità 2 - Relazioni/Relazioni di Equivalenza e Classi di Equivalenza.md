---
tags:
  - equivalenza
  - classi-equivalenza
  - proprieta
  - algebra
type: atomic
unit: 2
---

# Relazioni di Equivalenza e Classi di Equivalenza

Una **Relazione di Equivalenza** è una particolare relazione binaria che astrae il concetto di "uguaglianza". Serve a raggruppare elementi che, pur essendo distinti, condividono una determinata caratteristica che li rende "equivalenti" per i nostri scopi.

## Definizione Formale

Una relazione $R$ su un insieme $A$ si dice di **equivalenza** (spesso indicata con il simbolo $\sim$) se è contemporaneamente:
1. **Riflessiva:** $\forall a \in A, \quad a \sim a$
2. **Simmetrica:** $\forall a, b \in A, \quad a \sim b \implies b \sim a$
3. **Transitiva:** $\forall a, b, c \in A, \quad (a \sim b \land b \sim c) \implies a \sim c$

> [!EXAMPLE] L'Aritmetica Modulare
> La congruenza modulo $n$ ($a \equiv b \pmod n$) è l'esempio per eccellenza di relazione di equivalenza su $\mathbb{Z}$.
> Essa infatti gode delle tre proprietà (R, S, T) raggruppando i numeri interi in base al loro resto nella divisione per $n$.

---

## Classi di Equivalenza

Data una relazione di equivalenza $\sim$ su $A$, la **classe di equivalenza** di un elemento $x \in A$, denotata con $[x]$ o $\bar{x}$, è l'insieme di tutti gli elementi di $A$ che sono equivalenti a $x$:
$$[x] = \{ y \in A \mid y \sim x \}$$
L'elemento $x$ prende il nome di **rappresentante** della classe. Qualsiasi elemento della classe può essere scelto come rappresentante: se $y \in [x]$, allora $[y] = [x]$.

### Proprietà Fondamentali delle Classi
Le classi di equivalenza obbediscono a una regola ferrea (che porterà al concetto di partizione):
- Due classi di equivalenza o sono **perfettamente coincidenti** o sono **completamente disgiunte**.
- Non esistono "vie di mezzo" (nessuna intersezione parziale).
Formalmente: $\forall x, y \in A, \quad [x] = [y] \iff x \sim y \iff [x] \cap [y] \neq \emptyset$.

---

## Tip d'Esame

> [!TIP] Come Scegliere il Rappresentante
> Se ti viene chiesto di elencare le classi di equivalenza, cerca sempre di usare come rappresentanti gli elementi più "semplici" o "canonici". Ad esempio, nella congruenza modulo 5, scrivi le classi come $[0], [1], [2], [3], [4]$. Evita di usare $[15]$ al posto di $[0]$, anche se formalmente corretto: il docente apprezzerà la forma ridotta.

---

## Note Correlate
- [[01.0 - MoC Relazioni di Equivalenza e d'Ordine|Unità 2 MoC]]
- [[Relazioni Binarie e Proprietà]]
- [[Insieme Quoziente e Partizioni]]
