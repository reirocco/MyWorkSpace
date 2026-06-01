---
tags:
  - matematica
  - algebra/spazi_vettoriali
aliases:
  - Spazio vettoriale
  - Assiomi spazio vettoriale
---
# Definizione di Spazio Vettoriale

Uno **spazio vettoriale** $(V, +, \cdot)$ su $\mathbb{R}$ è un insieme $V \neq \emptyset$ (i cui elementi sono detti *vettori*) dotato di due operazioni:
- **Somma**: $+: V \times V \to V$
- **Prodotto per scalare**: $\cdot: \mathbb{R} \times V \to V$

Queste operazioni devono soddisfare **8 proprietà assiomatiche**:
1. Associatività della somma.
2. Esistenza dell'Elemento Neutro ($\mathbf{0}_V$).
3. Esistenza dell'Opposto ($-v$).
4. Commutatività della somma.
*(Queste prime 4 dicono che $(V, +)$ è un gruppo abeliano)*
5. Associatività del prodotto: $(ab)v = a(bv)$.
6. Elemento neutro del prodotto: $1 \cdot v = v$.
7. Distributività rispetto alla somma vettoriale: $a(v_1 + v_2) = av_1 + av_2$.
8. Distributività rispetto alla somma scalare: $(a+b)v = av + bv$.

> [!abstract] Esempi Classici
> - $\mathbb{R}^n$: Lo spazio delle $n$-uple di numeri reali (vettori colonna).
> - $M_{m,n}$: Lo spazio delle matrici $m \times n$.
> - $\mathbb{R}[x]$: L'insieme dei polinomi a coefficienti reali.

> [!danger] L'importanza dello Zero
> Ogni spazio vettoriale **deve** contenere il vettore nullo $\mathbf{0}_V$. L'insieme vuoto non è mai uno spazio vettoriale. L'insieme $\{\mathbf{0}_V\}$ è lo spazio vettoriale "banale" o di dimensione zero.

## Collegamenti
- Back: [[00_Spazi_Vettoriali_MOC|MOC Spazi Vettoriali]]
- Next: [[Sottospazi Vettoriali]]
