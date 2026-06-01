---
tags:
  - matematica
  - algebra/prodotto_scalare
aliases:
  - Teorema Spettrale
  - Endomorfismo Simmetrico
  - Matrice Simmetrica
---

# Endomorfismi Simmetrici e Teorema Spettrale

Siamo al culmine del corso. Abbiamo visto la Diagonalizzabilità e i Prodotti Scalari; ora li uniamo.

## Endomorfismi Simmetrici
Un endomorfismo $T: \mathbb{R}^n \to \mathbb{R}^n$ si dice **simmetrico** se la matrice a esso associata rispetto alla base canonica (o a qualsiasi base ortonormale) è **simmetrica** ($A = A^T$).
La condizione di simmetria equivale a questa proprietà sul prodotto scalare:
$$ \langle T(v), w \rangle = \langle v, T(w) \rangle \quad \forall v,w $$

## Il Teorema Spettrale
Questo è forse il teorema più importante dell'Algebra Lineare Reale.

> [!important] Enunciato
> **Ogni matrice quadrata reale e simmetrica è sempre diagonalizzabile tramite una base ORTONORMALE.**
> Equivalentemente: Esiste sempre una matrice ortogonale $M$ (con $M^{-1} = M^T$) tale che $M^T A M = D$, dove $D$ è diagonale.

In questo scenario magico si verificano miracoli algebrici:
1. **Autovalori Reali**: Una matrice simmetrica non può avere autovalori complessi. Sono tutti rigorosamente reali.
2. **Nessun problema di molteplicità**: Per le matrici simmetriche vale *sempre* $m_a(\lambda) = m_g(\lambda)$. (Quindi se all'esame ti viene $m_a \neq m_g$ su una simmetrica, hai sbagliato i calcoli!).
3. **Autospazi Ortogonali**: Autovettori relativi ad autovalori *diversi* non sono solo indipendenti, ma sono letteralmente **perpendicolari** ($\langle v_1, v_2 \rangle = 0$).

## Come "Diagonalizzare Ortogonalmente" (Algoritmo Pratico)
1. Trovi gli autovalori (e saranno tutti reali).
2. Trovi una base per ogni autospazio.
3. Se un autospazio ha dimensione $\ge 2$, potresti aver trovato una base di autovettori non perpendicolari. Per "raddrizzarla" e renderla ortogonale, le applichi l'[[Basi Ortogonali e Gram-Schmidt|Algoritmo di Gram-Schmidt]].
4. **Normalizzi** tutti gli autovettori trovati dividendo ciascuno per la sua lunghezza.
5. Inserisci gli autovettori in colonna nella matrice $M$. Ora hai una matrice ortogonale che diagonalizza la tua simmetrica!

## Collegamenti
- Back: [[00_Prodotto_Scalare_MOC|MOC Prodotto Scalare]]
- Previous: [[Matrici Ortogonali]]
