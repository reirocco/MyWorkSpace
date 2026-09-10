---
tags:
  - normali
  - quoziente
  - algebra
type: atomic
unit: 3
---

# Sottogruppi Normali e Gruppo Quoziente

Non tutti i sottogruppi si comportano in modo "educato" quando trasliamo le classi laterali. Quelli che lo fanno si chiamano Sottogruppi Normali e ci permettono di creare una nuova struttura: il Gruppo Quoziente.

## Sottogruppi Normali

Un sottogruppo $N \le G$ si dice **Normale** in $G$ (e si scrive $N \trianglelefteq G$) se per ogni $g \in G$, la classe laterale sinistra coincide esattamente con la classe laterale destra:
$$gN = Ng \quad \forall g \in G$$

> [!IMPORTANT] Condizione Equivalente (Coniugio)
> In pratica, la definizione precedente si testa usando l'operazione di coniugio.
> $N \trianglelefteq G \iff \forall n \in N, \forall g \in G, \quad g n g^{-1} \in N$
> (Cioè, se "chiudo a panino" un elemento di $N$ in mezzo a $g$ e $g^{-1}$, il risultato non scappa da $N$).

**Fatti Utili:**
- Nei gruppi Abeliani, **tutti** i sottogruppi sono normali.
- Il centro del gruppo $Z(G)$ è sempre un sottogruppo normale.
- Il nucleo ($\text{Ker} f$) di un qualsiasi omomorfismo è sempre un sottogruppo normale (e viceversa!).

---

## Il Gruppo Quoziente $G/N$

Se abbiamo la garanzia che $N$ è normale ($N \trianglelefteq G$), allora l'insieme di tutte le classi laterali (che partizionano $G$) diventa a sua volta un Gruppo!

Chiamiamo questo nuovo insieme **Gruppo Quoziente**: $G/N = \{ gN \mid g \in G \}$

La nuova operazione binaria tra le "fette" (classi laterali) si definisce in modo naturalissimo:
$$(aN) \ast (bN) = (a \ast b)N$$
*(La normalità è il pre-requisito vitale affinché questa operazione sia "ben definita", cioè non dipenda dai rappresentanti scelti $a$ e $b$).*

> [!EXAMPLE] L'Orologio come Quoziente
> Pensiamo a $(\mathbb{Z}, +)$.
> I multipli di $n$ formano un sottogruppo: $n\mathbb{Z}$.
> Poiché $\mathbb{Z}$ è abeliano, $n\mathbb{Z} \trianglelefteq \mathbb{Z}$ (è normale).
> L'insieme quoziente è $\mathbb{Z} / n\mathbb{Z}$. Che cos'è?
> Le classi sono del tipo $a + n\mathbb{Z}$. L'operazione è $(a+n\mathbb{Z}) + (b+n\mathbb{Z}) = (a+b)+n\mathbb{Z}$.
> Questa non è altro che la costruzione formale delle classi di resto!
> Quindi, $\mathbb{Z} / n\mathbb{Z} = \mathbb{Z}_n$.

---

## Tip d'Esame

> [!TIP] L'Indice di un Sottogruppo
> Una regola salvavita: **Qualsiasi sottogruppo di indice 2 è automaticamente Normale**.
> Se ti trovi davanti a un gruppo di 10 elementi e trovi un sottogruppo di 5 elementi, il suo indice (numero di classi) è $10/5 = 2$. Senza fare calcoli di coniugio, puoi subito scrivere a margine "Il sottogruppo è normale perché ha indice 2" per poi usarlo nel quoziente. È un teorema potentissimo che salva molto tempo.

---

## Note Correlate
- [[03.0 - MoC Teoria dei Gruppi|Unità 3 MoC]]
- [[Classi Laterali e Teorema di Lagrange]]
- [[Insieme Quoziente e Partizioni]]
- [[Teorema Fondamentale di Omomorfismo per Gruppi]]
