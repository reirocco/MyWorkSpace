---
tags:
  - permutazioni
  - gruppo-simmetrico
  - cicli
  - algebra
type: atomic
unit: 3
---

# Gruppo delle Permutazioni $S_n$

Il **Gruppo Simmetrico $S_n$** (o Gruppo delle Permutazioni) è uno dei gruppi più importanti in algebra. Per il Teorema di Cayley, "tutti" i gruppi finiti possono essere visti come sottogruppi di un qualche $S_n$.

## Definizioni Base

Una **permutazione** su un insieme $A$ di $n$ oggetti (di solito $A = \{1, 2, \dots, n\}$) è una funzione **biettiva** (iniettiva e suriettiva) da $A$ in se stesso.
L'insieme di tutte queste funzioni, equipaggiato con l'operazione di **composizione di funzioni** ($\circ$), forma il gruppo $S_n$.

- **L'ordine di $S_n$** (il numero totale di permutazioni) è $n!$ (n fattoriale).
- Per $n \ge 3$, il gruppo $S_n$ **non è abeliano**.

### Notazione a Matrice (o a due righe)
Una permutazione può essere scritta elencando gli elementi del dominio in alto e le loro immagini in basso:
$$ \sigma = \begin{pmatrix} 1 & 2 & 3 & 4 \\ 2 & 4 & 3 & 1 \end{pmatrix} $$
In questo esempio: $1 \to 2$, $2 \to 4$, $3 \to 3$, $4 \to 1$.

---

## Notazione in Cicli Disgiunti

La notazione a matrice è ingombrante. È preferibile scomporre ogni permutazione nel prodotto di **cicli disgiunti**.
Un ciclo della forma $(a_1 \; a_2 \; \dots \; a_k)$ significa che $a_1 \to a_2$, $a_2 \to a_3, \dots, a_k \to a_1$.
(Gli elementi non elencati rimangono fissi).

> [!EXAMPLE] Conversione in Cicli
> Riprendiamo la permutazione $\sigma$ di prima.
> Parto da $1$: l'$1$ va in $2$. Il $2$ va in $4$. Il $4$ torna in $1$. Ho chiuso il primo ciclo: $(1 \; 2 \; 4)$.
> L'elemento $3$ va in $3$ (è un punto fisso). I punti fissi di solito si omettono.
> Quindi, in notazione ciclica, $\sigma = (1 \; 2 \; 4)$.
> La **lunghezza** di questo ciclo è 3.

**Teorema:** Ogni permutazione si può scomporre in modo unico (a meno dell'ordine) in un prodotto di cicli disgiunti.
> [!IMPORTANT] I cicli disgiunti commutano!
> Sebbene $S_n$ non sia commutativo, se due cicli non hanno elementi in comune, possono essere scambiati:
> $(1 \; 2)(3 \; 4) = (3 \; 4)(1 \; 2)$.

---

## Ordine di una Permutazione e Trasposizioni

L'**ordine** di un ciclo è pari alla sua lunghezza.
Se una permutazione è scritta come prodotto di cicli disgiunti, il suo ordine complessivo è il **Minimo Comune Multiplo (MCM)** delle lunghezze dei singoli cicli.
*(Esempio: La permutazione $(1 \; 2)(3 \; 4 \; 5)$ ha ordine $\text{MCM}(2, 3) = 6$. Significa che va applicata 6 volte per tornare all'identità).*

### Trasposizioni (Segno della Permutazione)
Una **trasposizione** è un ciclo di lunghezza 2, cioè uno scambio di due soli elementi, es. $(1 \; 2)$.
Qualsiasi permutazione può essere scritta come prodotto di trasposizioni.
Un ciclo $(a_1 \; a_2 \; \dots \; a_k)$ si decompone in:
$$(a_1 \; a_k)(a_1 \; a_{k-1}) \dots (a_1 \; a_2)$$

- Una permutazione si dice **Pari** se si decompone in un numero pari di trasposizioni.
- Si dice **Dispari** se si decompone in un numero dispari di trasposizioni.
*(Il segno della permutazione è cruciale per calcolare i determinanti in algebra lineare).*

---

## Tip d'Esame

> [!TIP] Scomposizione: Da Destra o da Sinistra?
> Quando componi due permutazioni $f \circ g$, devi fare estrema attenzione alla convenzione adottata dal docente.
> Essendo composizione di funzioni ($f(g(x))$), la regola aurea matematica impone di leggere **da Destra verso Sinistra**. Prima applichi $g$, poi il risultato finisce in $f$.
> Tuttavia, alcuni testi di Algebra adottano la convezione contraria. Prima dell'esame, controlla sempre gli appunti del professore su questo dettaglio microscopico che rischia di sfalsare tutti i conti!

---

## Note Correlate
- [[03.0 - MoC Teoria dei Gruppi|Unità 3 MoC]]
- [[Strutture Algebriche e Operazioni Binarie]]
