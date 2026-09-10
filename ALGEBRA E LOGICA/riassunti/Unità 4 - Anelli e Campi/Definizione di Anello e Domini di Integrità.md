---
tags:
  - anelli
  - domini-integrita
  - zero-divisori
  - algebra
type: atomic
unit: 4
---

# Definizione di Anello e Domini di Integrità

Un **Anello** è una struttura algebrica che generalizza l'aritmetica dei numeri interi. A differenza dei gruppi, in un anello abbiamo **due** operazioni binarie (solitamente chiamate somma e prodotto) che interagiscono tra loro tramite la proprietà distributiva.

## Definizione di Anello

Un insieme $R$ dotato di due operazioni $(+, \cdot)$ è un **Anello** se soddisfa tre blocchi di assiomi:
1. **Rispetto alla Somma:** $(R, +)$ è un **Gruppo Abeliano**.
   *(L'elemento neutro si denota con $0$, l'inverso di $a$ con $-a$ e vale la proprietà commutativa $a+b=b+a$).*
2. **Rispetto al Prodotto:** $(R, \cdot)$ è un **Semigruppo**.
   *(Il prodotto è un'operazione chiusa e associativa).*
3. **Distributività:** Il prodotto si distribuisce sulla somma (sia a destra che a sinistra).
   $$a \cdot (b + c) = (a \cdot b) + (a \cdot c) \quad \text{e} \quad (a + b) \cdot c = (a \cdot c) + (b \cdot c)$$

### Classificazioni Aggiuntive
- **Anello Commutativo:** Se il prodotto è commutativo ($a \cdot b = b \cdot a$).
- **Anello Unitario:** Se esiste un elemento neutro per il prodotto (denotato con $1$ o $1_R$).
  *(Molti autori moderni richiedono l'esistenza dell'1 direttamente nella definizione base di Anello, quindi fai attenzione al libro di testo!).*

> [!EXAMPLE] Esempi di Anelli
> - $(\mathbb{Z}, +, \cdot)$: È l'anello commutativo unitario per eccellenza.
> - $M_n(\mathbb{R})$ (matrici $n \times n$): È un anello unitario, ma **non commutativo**.
> - I numeri pari $(2\mathbb{Z}, +, \cdot)$: Formano un anello commutativo, ma **privo di unità** (non c'è l'1).

---

## Divisori dello Zero e Domini di Integrità

Negli anelli, il prodotto di due elementi non nulli **può fare zero**.

- **Divisore dello Zero:** Un elemento $a \neq 0$ si dice divisore dello zero se esiste un $b \neq 0$ tale che $a \cdot b = 0$ oppure $b \cdot a = 0$.

> [!IMPORTANT] Dominio di Integrità
> Un anello commutativo unitario (con $1 \neq 0$) si dice **Dominio di Integrità** se **NON possiede divisori dello zero**.
> In un dominio di integrità vale la *legge di annullamento del prodotto*: $ab = 0 \implies a = 0 \text{ oppure } b = 0$.
> **Esempio:** $\mathbb{Z}$ è un dominio.
> **Controesempio:** $\mathbb{Z}_6$ NON è un dominio, perché $[2] \cdot [3] = [6] \equiv [0] \pmod 6$, pur essendo $[2]$ e $[3]$ diversi da zero.

Nei domini di integrità vale la **legge di cancellazione per il prodotto**: se $ab = ac$ (con $a \neq 0$), allora $b = c$. (Negli anelli generici questa cosa è falsa!).

---

## Tip d'Esame

> [!TIP] Come capire se $\mathbb{Z}_n$ è un dominio
> In $\mathbb{Z}_n$, i divisori dello zero sono esattamente quelle classi di resto $[k]$ che non sono invertibili, cioè quelle per cui $\text{MCD}(k, n) > 1$.
> Di conseguenza, $\mathbb{Z}_n$ è un dominio di integrità **se e solo se $n$ è un numero primo**. Se $n$ è composto, esisteranno sempre divisori dello zero.

---

## Note Correlate
- [[04.0 - MoC Anelli e Campi|Unità 4 MoC]]
- [[Definizione di Campo e Caratteristica]]
- [[Omomorfismi di Anelli]]
