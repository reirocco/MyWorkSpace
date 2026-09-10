---
tags:
  - gruppi-ciclici
  - generatori
  - ordine-elemento
  - algebra
type: atomic
unit: 3
---

# Gruppi Ciclici e Generatori

I **Gruppi Ciclici** sono i gruppi più semplici in assoluto da studiare. Sono gruppi in cui ogni elemento può essere generato ripetendo l'operazione su un unico elemento "seme", chiamato **generatore**.

## Generazione e Gruppo Ciclico

Dato un gruppo $G$ e un suo elemento $g \in G$, definiamo il **sottogruppo generato da $g$**, indicato con $\langle g \rangle$, come l'insieme di tutte le potenze (positive, negative e nulla) di $g$:
$$\langle g \rangle = \{ g^k \mid k \in \mathbb{Z} \}$$
*(In notazione additiva, sarebbe l'insieme di tutti i multipli $\{ k \cdot g \mid k \in \mathbb{Z} \}$).*

> [!IMPORTANT] Definizione di Gruppo Ciclico
> Un gruppo $G$ si dice **ciclico** se esiste almeno un elemento $g \in G$ capace di generare l'intero gruppo. In tal caso, si scrive $G = \langle g \rangle$.
> **Ogni gruppo ciclico è obbligatoriamente commutativo (Abeliano).**

---

## ⏱ Ordine di un Elemento vs Ordine del Gruppo

- **Ordine di un Gruppo, $|G|$:** È semplicemente il numero di elementi contenuti nell'insieme $G$.
- **Ordine di un Elemento, $o(g)$:** È il più piccolo intero positivo $n$ tale che $g^n = e$ (dove $e$ è l'elemento neutro).
  Se un tale $n$ non esiste, si dice che l'elemento ha **ordine infinito**.

**Teorema Cruciale:** L'ordine di un elemento $g$ coincide esattamente con l'ordine (cioè la cardinalità) del sottogruppo da esso generato:
$$o(g) = |\langle g \rangle|$$
Corollario: Un gruppo finito $G$ di ordine $n$ è ciclico se e solo se contiene almeno un elemento di ordine $n$.

---

## Esempi di Gruppi Ciclici

1. **$(\mathbb{Z}, +)$ è un gruppo ciclico infinito.**
   I suoi generatori sono $+1$ e $-1$. Infatti, ogni intero si ottiene sommando o sottraendo $1$ più volte. $\mathbb{Z} = \langle 1 \rangle = \langle -1 \rangle$.
2. **$(\mathbb{Z}_n, +)$ è un gruppo ciclico finito di ordine $n$.**
   La classe $[1]$ è sempre un generatore. Ma ce ne possono essere altri!

> [!EXAMPLE] Trovare i generatori di $\mathbb{Z}_6$
> Il gruppo è $\mathbb{Z}_6 = \{0, 1, 2, 3, 4, 5\}$. Cerchiamo quali elementi hanno ordine 6.
> - $\langle 1 \rangle = \{1, 2, 3, 4, 5, 0\} \implies \text{Generatore!}$
> - $\langle 2 \rangle = \{2, 4, 0\} \implies \text{Non genera tutto. Ordine } 3$.
> - $\langle 3 \rangle = \{3, 0\} \implies \text{Non genera tutto. Ordine } 2$.
> - $\langle 4 \rangle = \{4, 2, 0\} \implies \text{Non genera. Ordine } 3$.
> - $\langle 5 \rangle = \{5, 4, 3, 2, 1, 0\} \implies \text{Generatore!}$
> I generatori sono $[1]$ e $[5]$. Nota che $\text{MCD}(1, 6) = 1$ e $\text{MCD}(5, 6) = 1$.

---

## Tip d'Esame

> [!TIP] Trovare tutti i generatori in un colpo solo
> Se sai che un gruppo ciclico ha ordine $n$ ed è generato da un certo $g$, allora un qualsiasi altro elemento della forma $g^k$ sarà anch'esso un generatore **se e solo se $k$ è coprimo con $n$** (cioè $\text{MCD}(k, n) = 1$).
> Il numero totale di generatori di un gruppo ciclico di ordine $n$ è dato dalla **Funzione indicatrice di Eulero $\phi(n)$**, che conta quanti numeri minori di $n$ sono coprimi con $n$.
> Esempio al volo: Quanti generatori ha un gruppo ciclico di ordine 10? I numeri coprimi con 10 sono 1, 3, 7, 9. Quindi ne ha 4.

---

## Note Correlate
- [[03.0 - MoC Teoria dei Gruppi|Unità 3 MoC]]
- [[Definizione di Gruppo ed Esempi Fondamentali]]
- [[Classi Laterali e Teorema di Lagrange]]
