---
tags:
  - matematica
  - algebra/prodotto_scalare
aliases:
  - Gram-Schmidt
  - Ortogonalizzazione
  - Base Ortonormale
  - Base Ortogonale
---
# Basi Ortogonali e Ortonormali (Gram-Schmidt)

I sistemi di assi obliqui ("storti") complicano spaventosamente i calcoli geometrici. Un'equazione diventa pulita, elegante e veloce da elaborare quando i vettori che la descrivono sono a $90^\circ$ tra loro e hanno lunghezza pari a $1$.

---

## 1. Definizioni: Ortogonale vs Ortonormale

Sia $\mathcal{B} = \{v_1, v_2, \dots, v_n\}$ una base di uno spazio vettoriale.

1. **Base Ortogonale:** Una base in cui ogni vettore è strettamente perpendicolare a tutti gli altri.
   $$ \langle v_i, v_j \rangle = 0 \quad \forall i \neq j $$
   *Teorema:* Vettori ortogonali (non nulli) sono automaticamente e inevitabilmente linearmente indipendenti.
2. **Base Ortonormale:** È una base ortogonale in cui, per di più, tutti i vettori sono **versori** (hanno lunghezza esattamente $1$).
   $$ \langle v_i, v_i \rangle = \|v_i\|^2 = 1 \quad \forall i $$

### Il "Superpotere" delle Basi Ortogonali (Coefficienti di Fourier)
Il motivo principale per cui amiamo le basi ortogonali è la disarmante facilità con cui si trovano le coordinate di un vettore. 
In una base normale devi risolvere un intero sistema lineare. In una base **Ortogonale** $\{u_1, \dots, u_n\}$, se $v = c_1 u_1 + \dots + c_n u_n$, la singola coordinata $c_i$ si isola istantaneamente (proiettando):
$$ c_i = \frac{\langle v, u_i \rangle}{\langle u_i, u_i \rangle} = \frac{\langle v, u_i \rangle}{\|u_i\|^2} $$
Se la base è addirittura **Ortonormale**, il denominatore vale 1, e la formula si sgretola in pura semplicità: 
$$ c_i = \langle v, u_i \rangle $$

---

## 2. L'Algoritmo di Gram-Schmidt

Gram-Schmidt è un algoritmo costruttivo potentissimo. Consente di prendere una base "storta" qualsiasi e "raddrizzarla", costruendo iterativamente una base ortogonale che descrive esattamente lo stesso spazio.

**Problema:** Data una base generica $(v_1, v_2, \dots, v_k)$ di un sottospazio $V$, costruire una base ortogonale $(w_1, w_2, \dots, w_k)$ di $V$.

> [!abstract] La Ricetta Passo-Passo
> L'idea è: si tiene un vettore fermo, e dai vettori successivi si sottraggono le "ombre" (le proiezioni ortogonali) che essi gettano sui vettori precedenti.
> 
> 1. **Il Primo Pilastro:** 
>    Il primo vettore viene preso intatto.
>    $$ w_1 = v_1 $$
> 2. **Il Secondo Vettore:** 
>    Prendiamo $v_2$ e gli depuriamo la componente che andava nella direzione di $w_1$.
>    $$ w_2 = v_2 - \left( \frac{\langle v_2, w_1 \rangle}{\langle w_1, w_1 \rangle} \right) w_1 $$
> 3. **Il Terzo Vettore:** 
>    Prendiamo $v_3$ e gli sottraiamo le proiezioni sia lungo $w_1$ sia lungo $w_2$.
>    $$ w_3 = v_3 - \left( \frac{\langle v_3, w_1 \rangle}{\langle w_1, w_1 \rangle} \right) w_1 - \left( \frac{\langle v_3, w_2 \rangle}{\langle w_2, w_2 \rangle} \right) w_2 $$
> 4. **Passo $k$-esimo generale:**
>    Si continua analogamente sottraendo le proiezioni lungo tutti i $w$ calcolati in precedenza.

> [!tip] Passo Finale: Normalizzazione
> L'algoritmo di Gram-Schmidt, così formulato, produce una base **Ortogonale**.
> Per farla diventare una base **Ortonormale** (come spesso richiesto all'esame, specialmente nel Teorema Spettrale), occorre dividere ciascun vettore $w_i$ per la sua lunghezza:
> $$ u_i = \frac{1}{\|w_i\|} w_i $$

---
## Collegamenti
* **Back:** [[00_Prodotto_Scalare_MOC|MOC Prodotto Scalare]]
* **Previous:** [[Complemento Ortogonale]]
* **Next:** [[Matrici Ortogonali]]
