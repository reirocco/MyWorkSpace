---
tags:
  - sottogruppi
  - algebra
  - teoria-dei-gruppi
type: atomic
unit: 3
---

# Sottogruppi e Criterio dei Sottogruppi

Un **Sottogruppo** è, intuitivamente, un gruppo più piccolo nascosto all'interno di un gruppo più grande, che usa esattamente le stesse "regole del gioco".

## Definizione di Sottogruppo

Dato un gruppo $(G, \ast)$, un sottoinsieme non vuoto $H \subseteq G$ è un **sottogruppo** di $G$ (e si scrive $H \le G$) se $H$ stesso forma un gruppo rispetto alla medesima operazione $\ast$ ristretta ad $H$.

Ogni gruppo possiede almeno due sottogruppi banali:
1. Il gruppo stesso: $G$
2. Il sottogruppo identico, contenente solo l'elemento neutro: $\{e\}$

---

## Il Criterio (Test) dei Sottogruppi

Per verificare se un sottoinsieme $H$ è un sottogruppo, non c'è bisogno di testare di nuovo tutti i 4 assiomi dei gruppi. L'associatività, essendo vera in $G$, "scende" automaticamente in $H$.
Basta verificare due condizioni (Criterio in 2 passi):
1. **Chiusura:** $\forall h_1, h_2 \in H \implies h_1 \ast h_2 \in H$
2. **Inversi:** $\forall h \in H \implies h^{-1} \in H$
*(Se non è vuoto, queste due condizioni assicurano che contenga anche l'elemento neutro $e$).*

> [!IMPORTANT] Criterio Compatto (in 1 passo)
> Il test si può compattare in un'unica formidabile condizione.
> $H \le G \iff (H \neq \emptyset) \land (\forall x, y \in H \implies x \ast y^{-1} \in H)$
> (In notazione additiva: $x - y \in H$).

> [!EXAMPLE] Dimostrazione con il Criterio
> Dimostriamo che i numeri pari $2\mathbb{Z}$ formano un sottogruppo dei numeri interi $(\mathbb{Z}, +)$.
> **1.** $2\mathbb{Z}$ è non vuoto (contiene $0 = 2 \cdot 0$).
> **2. Applico il Criterio Compatto Additivo ($x - y \in H$):**
> Siano $x, y \in 2\mathbb{Z}$. Allora esistono interi $k, j$ tali che $x = 2k$ e $y = 2j$.
> Calcoliamo la differenza: $x - y = 2k - 2j = 2(k - j)$.
> Poiché $(k - j)$ è un intero, $x - y$ è multiplo di 2, quindi appartiene a $2\mathbb{Z}$.
> **Conclusione:** $2\mathbb{Z} \le \mathbb{Z}$.

---

## Centro e Centralizzante (Sottogruppi Speciali)

Alcuni sottogruppi nascono in modo naturale studiando la commutatività all'interno di un gruppo $G$.

- **Il Centro del Gruppo, $Z(G)$:**
  È l'insieme di tutti gli elementi di $G$ che commutano con *ogni altro* elemento di $G$.
  $$Z(G) = \{ z \in G \mid zx = xz \quad \forall x \in G \}$$
  $Z(G)$ è sempre un sottogruppo di $G$ (ed è pure un sottogruppo normale). Se $G$ è abeliano, $Z(G) = G$.

- **Il Centralizzante di un elemento $a$, $C(a)$:**
  È l'insieme degli elementi di $G$ che commutano specificamente con l'elemento $a$.
  $$C(a) = \{ x \in G \mid xa = ax \}$$

---

## Tip d'Esame

> [!TIP] Intersezione vs Unione
> Un classico trabocchetto dei test a risposta multipla:
> - L'**intersezione** di due sottogruppi ($H_1 \cap H_2$) è **SEMPRE** un sottogruppo.
> - L'**unione** di due sottogruppi ($H_1 \cup H_2$) **NON È MAI** un sottogruppo, a meno che uno dei due non sia completamente contenuto nell'altro ($H_1 \subseteq H_2$ o viceversa).
> Prova a pensare in $(\mathbb{Z}, +)$: unisci i pari ($2\mathbb{Z}$) e i multipli di tre ($3\mathbb{Z}$). $2$ è pari, $3$ è multiplo di tre. Ma $2+3=5$ non sta in nessuno dei due!

---

## Note Correlate
- [[03.0 - MoC Teoria dei Gruppi|Unità 3 MoC]]
- [[Definizione di Gruppo ed Esempi Fondamentali]]
- [[Sottogruppi Normali e Gruppo Quoziente]]
