---
tags:
  - matematica
  - algebra/preliminari
aliases:
  - Polinomio
  - Radici di un Polinomio
  - Teorema Fondamentale dell'Algebra
---
# Polinomi e Radici

I polinomi e le loro radici sono tra i concetti più importanti dell'algebra. Mettiamo in chiaro questi concetti "traducendoli" in modo visivo e pratico, spiegando cosa significano davvero punto per punto.

### 1. Cos'è un Polinomio?
Un polinomio non è altro che una somma di termini (chiamati monomi). Ogni termine è composto da un coefficiente numerico (un numero reale) e da una variabile $x$ elevata a una potenza intera positiva.
L'espressione formale si scrive matematicamente così:
$$ P(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0 $$

- **Il Grado ($n$)**: È l'esponente più alto della $x$ che compare nel polinomio (a patto che il suo coefficiente $a_n$ non sia zero). Determina il "comportamento" generale del polinomio.
- **I Coefficienti ($a_i$)**: Sono i numeri reali che moltiplicano le $x$. Ad esempio, in $P(x) = 3x^2 - 5x + 2$, i coefficienti sono $3$, $-5$ e $2$.

### 2. Cos'è una Radice (o Zero)?
Graficamente, un polinomio individua una curva su un piano cartesiano.
Una radice (o zero) è un valore numerico $c$ che, sostituito alla $x$, fa "azzerare" il polinomio. Ovvero: $P(c) = 0$.
Dal punto di vista geometrico, le radici reali sono i punti in cui il grafico del polinomio interseca l'asse delle ascisse ($x$).

### 3. Il Teorema di Ruffini (La Scomposizione)
Il Teorema di Ruffini crea un ponte perfetto tra l'algebra (le divisioni) e l'analisi (gli zeri di una funzione). Dice che:
$$ \text{Se } P(c) = 0 \iff P(x) \text{ è divisibile esattamente per } (x - c) $$
Cosa significa? Che se scopri che un numero $c$ è una radice, puoi "tirare fuori" quel blocco dal polinomio, riscrivendolo come:
$$ P(x) = (x - c) \cdot Q(x) $$
Dove $Q(x)$ è un nuovo polinomio più piccolo (di grado $n-1$). Questo è alla base della scomposizione in fattori.

**Esempio Pratico**
Prendiamo $P(x) = x^2 - 3x + 2$. Proviamo a sostituire $x = 2$:
$$ P(2) = 2^2 - 3(2) + 2 = 4 - 6 + 2 = 0 $$
Dato che il risultato è $0$, allora $c = 2$ è una radice.
Per il Teorema di Ruffini, $P(x)$ deve essere divisibile per $(x - 2)$. Infatti, se scomponiamo il polinomio, otteniamo: $P(x) = (x - 2)(x - 1)$.

### 4. La Molteplicità Algebrica
Non tutte le radici "pesano" allo stesso modo. A volte, lo stesso fattore $(x - c)$ compare più di una volta nella scomposizione.
La molteplicità algebrica ($m$) è semplicemente il numero di volte che una radice si ripete. Se un polinomio può essere diviso per $(x - c)^m$ ma non per una potenza superiore, allora $c$ è una radice con molteplicità $m$.

- **Molteplicità = 1 (Radice singola)**: Il grafico attraversa l'asse $x$ in modo netto.
- **Molteplicità = 2 (Radice doppia)**: Il grafico rimbalza sull'asse $x$ (è un punto di tangenza, come il vertice di una parabola).
- **Molteplicità = 3 (Radice tripla)**: Il grafico attraversa l'asse $x$ ma "flette" leggermente (un flesso a tangente orizzontale).

**Esempio**
Sia $P(x) = (x - 5)^3 (x + 2)$.
- $c = 5$ è una radice con molteplicità algebrica 3.
- $c = -2$ è una radice con molteplicità algebrica 1.

Un fatto fondamentale (legato al Teorema Fondamentale dell'Algebra): se contiamo ogni radice con la sua molteplicità, un polinomio di grado $n$ avrà sempre esattamente $n$ radici (considerando anche i numeri complessi).

La formula generale per scomporre un polinomio conoscendo tutte le sue radici ($c_1, c_2, \dots, c_n$) è:
$$P(x) = a_n(x - c_1)(x - c_2)\dots(x - c_n)$$

> [!abstract] Teorema Fondamentale dell'Algebra
> Se $p(x)$ è un polinomio di grado $n$ a coefficienti reali (o complessi), allora la somma delle molteplicità algebriche delle sue radici **valutate nei complessi ($\mathbb{C}$)** è esattamente $n$. 
>I.E. la somma delle molteplicità algebriche di tutte le radici (reali e complesse) è sempre uguale al grado del polinomio.

> [!tip] Teorema di Viète
> Se $p(x)$ ha coefficienti interi, le sue (eventuali) radici razionali si trovano tra le frazioni $\pm \frac{a}{b}$, dove $a$ è un divisore del termine noto ($a_0$) e $b$ è un divisore del coefficiente direttivo ($a_n$).
> Se $a_n = 1$, le possibili radici razionali sono solo i divisori interi del termine noto.

> [!question]- Esercizio Pratico
> Trova le possibili radici razionali di $p(x) = x^3 + 3x^2 - 4x - 12$.
> 
> **Soluzione passo-passo:**
> 1. Il coefficiente direttivo è $1$. Il termine noto è $-12$.
> 2. Per il Teorema di Viète, le possibili radici razionali sono i divisori interi di $-12$.
> 3. L'insieme dei candidati è: $\{\pm 1, \pm 2, \pm 3, \pm 4, \pm 6, \pm 12\}$.
> 4. Testando $x=2$: $p(2) = 8 + 12 - 8 - 12 = 0$. Dunque $2$ è radice!

## Collegamenti
- Back: [[00_Nozioni_Preliminari_MOC|MOC Nozioni Preliminari]]
- Previous: [[Funzioni]]
- Next: [[Sommatorie e Induzione]]
