---
tags:
  - matematica
  - algebra/preliminari
aliases:
  - Calcolo Combinatorio
  - Fattoriale
  - Coefficiente Binomiale
---

# Combinatoria

## Il Fattoriale
Il **fattoriale** di un numero $n \in \mathbb{N}$ (indicato con $n!$) è il prodotto di tutti i numeri interi positivi minori o uguali a $n$.
$$ n! = n \cdot (n-1) \cdot (n-2) \cdot \dots \cdot 1 $$
Per convenzione, $0! = 1$.
- Il fattoriale $n!$ rappresenta il numero di **modi per ordinare** (permutare) un insieme di $n$ elementi distinti.

## Coefficiente Binomiale (Combinazioni)
Quanti modi abbiamo per scegliere $k$ elementi estratti da un insieme di $n$ elementi (senza badare all'ordine)?
La risposta è il **coefficiente binomiale**:
$$ \binom{n}{k} = \frac{n!}{k!(n-k)!} $$

> [!tip] Proprietà Utile
> $\binom{n}{k} = \binom{n}{n-k}$. (Scegliere quali elementi tenere è equivalente a scegliere quali scartare).

> [!question]- Esercizio Pratico
> Quante partite si giocano nel girone di andata di un torneo con 20 squadre (ognuna gioca contro tutte le altre 1 volta)?
> 
> **Soluzione passo-passo:**
> 1. Dobbiamo scegliere tutte le possibili coppie ($k=2$) a partire da $20$ elementi ($n=20$).
> 2. Applichiamo la formula delle combinazioni:
>    $$ \binom{20}{2} = \frac{20!}{2!(20-2)!} = \frac{20!}{2! \cdot 18!} $$
> 3. Semplificando il fattoriale ($20! = 20 \cdot 19 \cdot 18!$):
>    $$ \frac{20 \cdot 19}{2} = 10 \cdot 19 = 190 $$

## Collegamenti
- Back: [[00_Nozioni_Preliminari_MOC|MOC Nozioni Preliminari]]
- Previous: [[Sommatorie e Induzione]]
