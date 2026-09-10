---
tags:
  - polinomi
  - ruffini
  - radici
  - irriducibilita
  - algebra
type: atomic
unit: 4
---

# Anelli di Polinomi e Divisibilità

Se $R$ è un anello (solitamente un dominio o un campo), possiamo costruire l'anello dei polinomi a coefficienti in $R$, denotato con $R[x]$.
Gli elementi di $R[x]$ sono espressioni del tipo:
$$p(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0$$
dove $a_i \in R$.

> [!NOTE] Proprietà Ereditate
> L'anello dei polinomi $R[x]$ eredita molte proprietà dell'anello dei coefficienti $R$:
> - Se $R$ è un Dominio di Integrità, allora anche $R[x]$ lo è.
> - Se $R$ è un Campo (es. $\mathbb{Q}, \mathbb{R}, \mathbb{Z}_p$), allora $R[x]$ si comporta quasi esattamente come l'anello degli interi $\mathbb{Z}$ (è un Dominio ad Ideali Principali). In particolare, in $K[x]$ si può fare l'**Algoritmo di Euclide** per la divisione.

---

## Divisione Euclidea tra Polinomi

Sia $K$ un campo. Dati due polinomi $A(x), B(x) \in K[x]$ con $B(x) \neq 0$, esistono e sono unici due polinomi $Q(x)$ (quoziente) e $R(x)$ (resto) tali che:
$$A(x) = B(x) Q(x) + R(x)$$
con $\text{grado}(R) < \text{grado}(B)$ oppure $R(x) = 0$.
*(Se $R(x) = 0$, $B(x)$ divide $A(x)$).*

> [!EXAMPLE] Divisione in $\mathbb{Z}_5[x]$
> Dividiamo $2x^2 + 3x + 1$ per $x + 2$ in $\mathbb{Z}_5[x]$.
> Ricorda che i coefficienti devono essere sommati/sottratti modulo 5. (Sottrarre 2 equivale ad aggiungere 3).
> - $2x^2 / x = 2x$.
> - Moltiplico $2x(x+2) = 2x^2 + 4x$.
> - Sottraggo: $(2x^2 + 3x + 1) - (2x^2 + 4x) = -x + 1 \equiv 4x + 1 \pmod 5$.
> - $4x / x = 4$.
> - Moltiplico $4(x+2) = 4x + 8 \equiv 4x + 3 \pmod 5$.
> - Sottraggo: $(4x + 1) - (4x + 3) = -2 \equiv 3 \pmod 5$.
> Risultato: $Q(x) = 2x + 4$, Resto $R(x) = 3$.

---

## Radici e Teorema di Ruffini

Un elemento $\alpha \in K$ è una **radice** (o zero) di $p(x)$ se $p(\alpha) = 0$.

> [!IMPORTANT] Teorema di Ruffini
> Un polinomio $p(x)$ ha una radice $\alpha$ se e solo se è divisibile per il binomio lineare $(x - \alpha)$.
> Corollario fondamentale: Un polinomio di grado $n$ a coefficienti in un **campo** ha *al massimo* $n$ radici.

---

## Polinomi Irriducibili

In analogia ai numeri primi in $\mathbb{Z}$, un polinomio si dice **irriducibile** se non può essere fattorizzato (scomposto) nel prodotto di due polinomi di grado strettamente inferiore.

- Se il grado è $1$ ($ax+b$), il polinomio è sempre irriducibile.
- Se il grado è $2$ o $3$, il polinomio è irriducibile **se e solo se non ha radici** nel campo. *(Per trovarle nei campi finiti $\mathbb{Z}_p$, basta provare a sostituire tutti gli elementi da $0$ a $p-1$ e vedere se qualcuno fa $0$)*.
- Se il grado è $\ge 4$, può essere riducibile (prodotto di due polinomi di grado 2) anche senza avere radici!

---

## Tip d'Esame

> [!TIP] Come capire se il campo è giusto
> Spesso agli esami si chiede se un polinomio è irriducibile specificando il campo. Il risultato cambia radicalmente!
> Esempio: $x^2 + 1$.
> - In $\mathbb{R}[x]$: Non ha radici reali. È irriducibile.
> - In $\mathbb{C}[x]$: Ha radici $i$ e $-i$. Si scompone in $(x-i)(x+i)$. È riducibile.
> - In $\mathbb{Z}_2[x]$: Sostituisco $1$. $1^2 + 1 = 2 \equiv 0 \pmod 2$. Ha radice $1$! Si scompone in $(x+1)(x+1)$. È riducibile.
> Controlla *sempre* su quale campo stai lavorando prima di rispondere.

---

## Note Correlate
- [[04.0 - MoC Anelli e Campi|Unità 4 MoC]]
- [[Definizione di Anello e Domini di Integrità]]
- [[Definizione di Campo e Caratteristica]]
