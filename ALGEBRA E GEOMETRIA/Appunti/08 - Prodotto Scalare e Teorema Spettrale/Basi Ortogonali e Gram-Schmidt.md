---
tags:
  - matematica
  - algebra/prodotto_scalare
aliases:
  - Gram-Schmidt
  - Ortogonalizzazione
  - Base Ortonormale
---

# Basi Ortogonali e Gram-Schmidt

Lavorare con un sistema di assi "storti" è complicato. La matematica diventa molto più semplice se possiamo usare basi formate da vettori tra loro perpendicolari e di lunghezza 1.

## Basi Ortonormali
Una base si dice:
- **Ortogonale** se tutti i suoi vettori sono mutualing perpendicolari (il prodotto scalare di ogni coppia è $0$). *Teorema: vettori ortogonali non nulli sono sempre linearmente indipendenti*.
- **Ortonormale** se è ortogonale E ogni vettore ha norma $1$ (sono versori).

In una base ortogonale, calcolare le coordinate di un vettore $v$ è facilissimo: basta usare il **Coefficiente di Fourier**. La coordinata $c_i$ rispetto al vettore $v_i$ è:
$$ c_i = \frac{\langle v, v_i \rangle}{\langle v_i, v_i \rangle} $$

## Algoritmo di Ortogonalizzazione di Gram-Schmidt
Se abbiamo una base generica $(v_1, \dots, v_n)$ e vogliamo "raddrizzarla" in una base ortogonale $(w_1, \dots, w_n)$, usiamo Gram-Schmidt:

1. **Primo vettore**: lo teniamo così com'è.
   $$ w_1 = v_1 $$
2. **Secondo vettore**: prendiamo $v_2$ e gli "togliamo" la sua proiezione lungo $w_1$.
   $$ w_2 = v_2 - \frac{\langle v_2, w_1 \rangle}{\langle w_1, w_1 \rangle} w_1 $$
3. **Terzo vettore**: prendiamo $v_3$ e gli togliamo le proiezioni lungo $w_1$ e $w_2$.
   $$ w_3 = v_3 - \frac{\langle v_3, w_1 \rangle}{\langle w_1, w_1 \rangle} w_1 - \frac{\langle v_3, w_2 \rangle}{\langle w_2, w_2 \rangle} w_2 $$
4. E così via.

> [!tip] Passo Finale: Ortonormalizzare
> Al termine del processo avrai vettori ortogonali. Per farli diventare una base ortonormale, devi normalizzarli, dividendo ciascun vettore $w_i$ per la sua norma $\|w_i\|$:
> $$ u_i = \frac{w_i}{\|w_i\|} $$

## Collegamenti
- Back: [[00_Prodotto_Scalare_MOC|MOC Prodotto Scalare]]
- Previous: [[Complemento Ortogonale]]
- Next: [[Matrici Ortogonali]]
