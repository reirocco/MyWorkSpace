---
tags:
  - divisibilita
  - mcd
  - algoritmo-euclide
  - identita-bezout
  - algebra
type: atomic
unit: 1
---
# Divisibilità e Algoritmo di Euclide

Nel dominio dei numeri interi ($\mathbb{Z}$), lo studio della divisibilità e dei numeri primi costituisce la base per l'intera teoria dell'aritmetica modulare.

## Divisione Euclidea e Divisibilità

> [!NOTE] Teorema della Divisione Euclidea
> Dati due interi $a, b \in \mathbb{Z}$ con $b \neq 0$, esistono e sono **unici** due interi $q$ (quoziente) e $r$ (resto) tali che:
> $$a = b \cdot q + r \quad \text{con} \quad 0 \le r < |b|$$

Se il resto $r = 0$, diciamo che **$b$ divide $a$** e scriviamo **$b \mid a$**.
Questo significa che esiste un intero $k$ tale che $a = b \cdot k$.

### Proprietà Fondamentali
1. Se $a \mid b$ e $a \mid c$, allora $a \mid (xb + yc)$ per ogni intero $x, y$.
2. Se $a \mid b$ e $b \mid a$, allora $a = \pm b$.
3. Se $a \mid b$ e $b \mid c$, allora $a \mid c$ (transitività).

---

## Massimo Comun Divisore (MCD)

Il **Massimo Comun Divisore** tra due interi $a$ e $b$ non nulli, indicato con $MCD(a,b)$ o semplicemente $(a,b)$, è il più grande intero positivo che divide contemporaneamente sia $a$ che $b$.
Se $\text{MCD}(a, b) = 1$, allora $a$ e $b$ si dicono **coprimi** (o primi tra loro).

### Algoritmo di Euclide (delle divisioni successive)
Questo algoritmo è il metodo più efficiente (anche a livello computazionale) per calcolare l'MCD senza dover fattorizzare i numeri. Si basa sul principio che:
$$\text{MCD}(a, b) = \text{MCD}(b, r) \quad \text{dove } a = bq + r$$

> [!EXAMPLE] Calcolo dell'MCD con Algoritmo di Euclide
> Calcoliamo l'MCD tra $252$ e $105$:
>  Per prima cosa calcoliamo il quoziente dividendo $a e b$ e prendendo la parte intera della divisione:
> 1.$\frac{252}{105}=2,4 \to q=2$
> 2. $252 = 105 \cdot 2 + 42$
> 3. $105 = 42 \cdot 2 + 21$
> 4. $42 = 21 \cdot 2 + 0 \implies \text{Resto 0!}$
> L'ultimo resto non nullo (in questo caso $21$) è l'MCD. Quindi $\text{MCD}(252, 105) = 21$.

---

## Identità di Bézout

> [!IMPORTANT] Teorema di Bézout
> Dati $a, b \in \mathbb{Z}$, se $d = \text{MCD}(a, b)$, allora esistono sempre due interi $x, y \in \mathbb{Z}$ (detti coefficienti di Bézout) tali che:
> $$ax + by = d$$
> Tali coefficienti non sono unici.

**Corollario (Coprimalità):** Due interi $a, b$ sono coprimi ($\text{MCD}=1$) *se e solo se* esistono $x, y \in \mathbb{Z}$ tali che $ax + by = 1$.

L'algoritmo di Euclide Esteso permette di calcolare materialmente i coefficienti risalendo le divisioni dell'algoritmo standard al contrario.

> [!EXAMPLE] Trovare i coefficienti di Bézout
> Riprendendo l'esempio precedente, isoliamo i resti:
> Dalla 2: $21 = 105 - 42 \cdot 2$
> Dalla 1: $42 = 252 - 105 \cdot 2$
> Sostituendo il 42 nella prima equazione:
> $21 = 105 - (252 - 105 \cdot 2) \cdot 2$
> $21 = 105 - 252 \cdot 2 + 105 \cdot 4$
> $21 = 105 \cdot 5 + 252 \cdot (-2)$
> I coefficienti di Bézout sono $x = -2$ (per $a=252$) e $y = 5$ (per $b=105$).

---

## Tip d'Esame

> [!TIP] Non scomporre mai!
> All'esame universitario, a meno che i numeri non siano banali o tu non venga esplicitamente autorizzato, **non calcolare l'MCD tramite la scomposizione in fattori primi**. Usa sempre l'Algoritmo di Euclide. La scomposizione non generalizza bene negli algoritmi crittografici e i docenti di Logica si aspettano la forma euclidea.
> L'Identità di Bézout è fondamentale per trovare gli Inversi Modulari (vedi nota successiva). Allenati a fare l'Euclide Esteso al contrario senza confonderti con i segni.

---

## Note Correlate
- [[01.0 - MoC Insiemistica e Aritmetica|Unità 1 MoC]]
- [[Congruenze e Aritmetica Modulare]]
- [[Anelli di Polinomi e Divisibilità]]
