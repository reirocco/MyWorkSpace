---
tags:
  - congruenze
  - aritmetica-modulare
  - classi-resto
  - algebra
type: atomic
unit: 1
---
# Congruenze e Aritmetica Modulare

L'**Aritmetica Modulare** è un sistema aritmetico per gli interi in cui i numeri "si avvolgono su se stessi" raggiungendo un certo valore, chiamato **modulo**. È la matematica dell'orologio.

## Definizione di Congruenza

Fissato un intero $n > 0$, diciamo che due interi $a$ e $b$ sono **congrui modulo $n$**, e scriviamo:
$$a \equiv b \pmod n$$
se $n$ divide la loro differenza $(a - b)$. In modo equivalente:
- $a$ e $b$ hanno lo stesso resto quando divisi per $n$.
- Esiste un intero $k$ tale che $a = b + kn$.

> [!NOTE] Relazione di Equivalenza
> La congruenza modulo $n$ è una **relazione di equivalenza** (riflessiva, simmetrica e transitiva). Essa partiziona l'insieme degli interi $\mathbb{Z}$ in $n$ sottoinsiemi disgiunti, chiamati **classi di resto**.

L'insieme di tutte le classi di resto modulo $n$ è denotato con **$\mathbb{Z}_n$**:
$$\mathbb{Z}_n = \{[0]_n, [1]_n, \dots, [n-1]_n\}$$

---

## Operazioni in $\mathbb{Z}_n$

Le operazioni di somma e prodotto sono "ben definite" (compatibili con le classi di resto):
Se $a \equiv c \pmod n$ e $b \equiv d \pmod n$, allora:
1. $a + b \equiv c + d \pmod n$
2. $a \cdot b \equiv c \cdot d \pmod n$

### Invertibilità e Elementi Inversi

Non tutti gli elementi in $\mathbb{Z}_n$ hanno un inverso moltiplicativo (cioè un elemento $x$ tale che $a \cdot x \equiv 1 \pmod n$).
> [!IMPORTANT] Criterio di Invertibilità
> Una classe $[a] \in \mathbb{Z}_n$ è invertibile se e solo se $\text{MCD}(a, n) = 1$ (ovvero se $a$ ed $n$ sono coprimi).
> L'inverso si calcola tramite l'Identità di Bézout: $ax + ny = 1 \implies ax \equiv 1 \pmod n \implies x = a^{-1} \pmod n$.

> [!EXAMPLE] Trovare un Inverso Modulare
> Trovare l'inverso di $3 \pmod{10}$.
> Verifichiamo: $\text{MCD}(3, 10) = 1$. L'inverso esiste.
> Cerchiamo $x$ tale che $3x \equiv 1 \pmod{10}$.
> Senza Euclide Esteso (visti i numeri piccoli): proviamo i multipli.
> $3 \cdot 7 = 21$. Poiché $21 = 10 \cdot 2 + 1$, allora $21 \equiv 1 \pmod{10}$.
> Quindi l'inverso di $3$ in $\mathbb{Z}_{10}$ è $[7]_{10}$.

---

## Equazioni Congruenziali Lineari

Un'equazione congruenziale lineare si presenta nella forma:
$$ax \equiv c \pmod n$$

**Teorema di Risolubilità:**
L'equazione ha soluzioni se e solo se $d = \text{MCD}(a, n)$ divide $c$.
Se $d \mid c$, l'equazione ha esattamente $d$ soluzioni distinte modulo $n$.
*Procedimento risolutivo:*
1. Si divide tutta l'equazione (anche il modulo!) per $d$, ottenendo $a'x \equiv c' \pmod{n'}$.
2. Si trova l'inverso di $a'$ modulo $n'$.
3. Si moltiplica l'inverso per $c'$ per trovare la soluzione base $x_0$.
4. Le altre $d-1$ soluzioni si trovano aggiungendo multipli di $n'$ a $x_0$.

---

## Tip d'Esame

> [!TIP] Errori Frequenti
> - **Divisione per un numero non coprimo:** Nelle congruenze **non si può** semplicemente "dividere" a destra e a sinistra. Se devi semplificare $ax \equiv ay \pmod n$, puoi farlo solo se dividi anche il modulo $n$ per il $\text{MCD}(a, n)$.
> - Se il modulo è un numero primo $p$, allora $\mathbb{Z}_p$ è un Campo: *tutti* gli elementi non nulli sono invertibili! In questi casi, il Piccolo Teorema di Fermat aiuta molto: $a^{p-1} \equiv 1 \pmod p$.

---

## Note Correlate
- [[01.0 - MoC Insiemistica e Aritmetica|Unità 1 MoC]]
- [[Divisibilità e Algoritmo di Euclide]]
- [[Teorema Cinese del Resto]]
- [[Definizione di Campo e Caratteristica]]
