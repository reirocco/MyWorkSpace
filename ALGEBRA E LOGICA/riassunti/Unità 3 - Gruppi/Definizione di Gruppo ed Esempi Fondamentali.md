---
tags:
  - gruppi
  - algebra
  - gruppi-abeliani
type: atomic
unit: 3
---

# Definizione di Gruppo ed Esempi Fondamentali

Il **Gruppo** è la struttura algebrica centrale di tutta l'Algebra Astratta. Cattura matematicamente il concetto di "simmetria".

## Definizione Formale

Un insieme $G$ equipaggiato con un'operazione binaria $\ast$ forma un **Gruppo** $(G, \ast)$ se soddisfa questi quattro assiomi:
1. **Chiusura:** $\forall a, b \in G, \quad a \ast b \in G$
2. **Associatività:** $\forall a, b, c \in G, \quad (a \ast b) \ast c = a \ast (b \ast c)$
3. **Elemento Neutro:** $\exists e \in G \mid \forall a \in G, \quad a \ast e = e \ast a = a$
4. **Esistenza dell'Inverso:** $\forall a \in G, \exists a^{-1} \in G \mid a \ast a^{-1} = a^{-1} \ast a = e$

Se in più l'operazione è **commutativa** ($a \ast b = b \ast a$), il gruppo si dice **Gruppo Abeliano**.

> [!NOTE] Legge di Cancellazione
> Nei gruppi vale sempre la legge di cancellazione, sia a destra che a sinistra.
> Se $a \ast b = a \ast c$, allora $b = c$. (Basta moltiplicare a sinistra per $a^{-1}$).

---

## Esempi Fondamentali

### 1. Gruppi Additivi (Spesso Abeliani)
L'operazione è la somma ($+$), il neutro è $0$, l'inverso di $a$ è l'opposto $-a$.
- **$(\mathbb{Z}, +)$, $(\mathbb{Q}, +)$, $(\mathbb{R}, +)$**: Sono tutti gruppi abeliani.
- **$(\mathbb{Z}_n, +)$**: L'insieme delle classi di resto modulo $n$ è un gruppo rispetto all'addizione modulare.
- **$(\mathbb{N}, +)$ NON è un gruppo**: Manca l'elemento opposto per $n > 0$.

### 2. Gruppi Moltiplicativi
L'operazione è il prodotto ($\cdot$), il neutro è $1$, l'inverso di $a$ è $a^{-1} = \frac{1}{a}$.
- **$(\mathbb{R}^*, \cdot)$**: I reali esclusi lo $0$ (che non ha inverso).
- **$U(\mathbb{Z}_n)$ o $\mathbb{Z}_n^*$**: Il gruppo degli **elementi invertibili modulo $n$**. È formato da tutti e soli i $[k]$ tali che $\text{MCD}(k, n) = 1$. L'operazione è la moltiplicazione.

### 3. Gruppi Non Abeliani (Simmetrie e Funzioni)
- **Gruppo Simmetrico ($S_n$)**: Tutte le permutazioni di $n$ elementi con l'operazione di composizione di funzioni. Non è commutativo per $n \ge 3$.
- **Gruppo Lineare Generale ($GL(n, \mathbb{R})$)**: Tutte le matrici $n \times n$ invertibili, con il prodotto tra matrici.

> [!EXAMPLE] L'inverso del Prodotto
> Nei gruppi vale la fondamentale regola del calzino-scarpa per l'inverso del prodotto:
> $$(a \ast b)^{-1} = b^{-1} \ast a^{-1}$$
> L'ordine si inverte! (Metto prima i calzini, poi le scarpe. Per svestirmi, tolgo prima le scarpe e poi i calzini).

---

## Tip d'Esame

> [!TIP] Come definire le notazioni
> - **Notazione Additiva:** Si usa **solo ed esclusivamente** per i gruppi abeliani. Se usi il simbolo $+$ per un gruppo non commutativo, farai inorridire il professore. $a+a = 2a$.
> - **Notazione Moltiplicativa:** Può essere usata per tutti i gruppi (abeliani o non). Spesso il segno $\cdot$ si omette. L'elemento neutro si chiama a volte $1$ o $e$. $a \cdot a = a^2$.

---

## Note Correlate
- [[03.0 - MoC Teoria dei Gruppi|Unità 3 MoC]]
- [[Strutture Algebriche e Operazioni Binarie]]
- [[Sottogruppi e Criterio dei Sottogruppi]]
