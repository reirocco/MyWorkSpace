---
tags:
  - matematica
  - algebra/applicazioni_lineari
aliases:
  - Nullità + Rango
  - Dimensioni
---

# Teorema di Nullità più Rango

Il Teorema di Nullità più Rango (o Teorema della Dimensione) è probabilmente la formula più utile in tutta l'Algebra Lineare applicata. 

## Il Teorema
Sia $T: V \to W$ un'applicazione lineare, dove $V$ è uno spazio di dimensione finita. Allora:
$$ \dim(\ker(T)) + \dim(\text{Im}(T)) = \dim(V) $$

> [!important] Il significato
> La "dimensione del dominio" ($\dim V$) è come un "budget" di informazioni. L'applicazione $T$ spende questo budget in due modi:
> - Una parte viene distrutta/schiacciata nello zero (misurata da $\dim(\ker(T))$, detta *nullità*).
> - La parte rimanente sopravvive e genera l'immagine (misurata da $\dim(\text{Im}(T))$, detta *rango*).

## Conseguenze Logiche (Heuristics d'Esame)
Siano $\dim(V) = n$ e $\dim(W) = m$.
1. **Se $n > m$**: $T$ **NON PUÒ** essere iniettiva.
   *Perché? L'immagine è un sottospazio di $W$, quindi $\dim(\text{Im}(T)) \le m$. Per Nullità+Rango, $\dim(\ker) = n - \dim(\text{Im}) \ge n - m > 0$. Essendo $\dim(\ker) > 0$, il nucleo non è banale.*
2. **Se $n < m$**: $T$ **NON PUÒ** essere suriettiva.
   *Perché? La dimensione massima dell'immagine è limitata dal dominio: $\dim(\text{Im}(T)) \le n$. Poiché $n < m$, l'immagine non può mai riempire l'intero $W$ di dimensione $m$.*
3. **Se $n = m$**: $T$ è iniettiva $\iff$ $T$ è suriettiva $\iff$ $T$ è un isomorfismo.

> [!question]- Esercizio Pratico
> Esiste un'applicazione lineare *iniettiva* $T: \mathbb{R}^3 \to \mathbb{R}^2$?
> 
> **Soluzione:**
> 1. In questo caso $n=3$ (dominio) e $m=2$ (codominio).
> 2. Se $T$ fosse iniettiva, $\ker(T) = \{0\} \implies \dim(\ker) = 0$.
> 3. Per Nullità+Rango: $0 + \dim(\text{Im}(T)) = 3 \implies \dim(\text{Im}(T)) = 3$.
> 4. Ma l'immagine è sottospazio di $\mathbb{R}^2$, non può avere dimensione 3! (Assurdo).
> 5. Quindi: **No, non esiste.**

## Collegamenti
- Back: [[00_Applicazioni_Lineari_MOC|MOC Applicazioni Lineari]]
- Previous: [[Nucleo e Immagine]]
- Next: [[Matrice Associata]]
