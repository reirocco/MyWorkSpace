---
tags:
  - matematica
  - algebra/matrici
aliases:
  - Matrice Invertibile
  - Inversa di una matrice
  - Gruppo Lineare
  - GL(n)
---

# Matrici Invertibili

## Definizione
Una matrice **quadrata** $A \in M_n$ si dice **invertibile** se esiste un'altra matrice $B \in M_n$ tale che:
$$
AB = BA = I_n
$$
Se un tale $B$ esiste, la matrice prende il nome di **Inversa di $A$** e si denota con $A^{-1}$.

> [!abstract] Proprietà Fondamentali
> 1. Se l'inversa esiste, essa è **unica**.
> 2. L'inversa dell'identità è l'identità stessa: $I_n^{-1} = I_n$.
> 3. L'inversa dell'inversa è la matrice di partenza: $(A^{-1})^{-1} = A$.
> 4. **Inversa del prodotto:** $(AB)^{-1} = B^{-1} A^{-1}$ (Importante: l'ordine si inverte!).
> 5. **Inversa della Trasposta:** $^t(A^{-1}) = (^tA)^{-1}$.

> [!info]- Dimostrazione: Unicità dell'inversa
> Supponiamo che $B$ e $C$ siano due diverse inverse per $A$. Allora, per ipotesi, $AB = I$, $BA = I$ e $AC = I$, $CA = I$.
> Utilizzando la proprietà associativa:
> $C = C \cdot I = C(AB) = (CA)B = I \cdot B = B$.
> Quindi $C = B$, le due inverse sono identiche.

> [!info]- Dimostrazione: Inversa della Trasposta $^t(A^{-1}) = (^tA)^{-1}$
> Basta notare che sfruttando la proprietà della trasposta del prodotto: $^tA \cdot ^t(A^{-1}) = ^t(A^{-1}A) = ^tI_n = I_n$.
> E allo stesso modo $^t(A^{-1}) \cdot ^tA = ^t(AA^{-1}) = ^tI_n = I_n$.
> Ma allora per l'unicità dell'inversa, l'inversa di $^tA$ è esattamente $^t(A^{-1})$.

> [!info]- Dimostrazione: Inversa del prodotto $(AB)^{-1} = B^{-1}A^{-1}$
> Verifichiamo che il prodotto faccia l'identità:
> $(AB)(B^{-1}A^{-1}) = A(BB^{-1})A^{-1} = A I_n A^{-1} = AA^{-1} = I_n$.
> $(B^{-1}A^{-1})(AB) = B^{-1}(A^{-1}A)B = B^{-1} I_n B = B^{-1}B = I_n$.
> Dunque, per l'unicità, l'inversa di $AB$ è $B^{-1}A^{-1}$.
## Gruppo Lineare $GL(n, \mathbb{R})$
L'insieme di tutte le matrici invertibili di ordine $n$, preso rispetto all'operazione di prodotto righe per colonne, costituisce un "gruppo" matematico. Viene denotato con:
$$
GL(n, \mathbb{R}) = \{ A \in M_n : A \text{ è invertibile} \}
$$

> [!question]- Esercizio Pratico (Verifica Inversa)
> Data la matrice:
> $A = \begin{pmatrix} 0 & -1 \\ 1 & 2 \end{pmatrix}$
> Verifica se $B = \begin{pmatrix} 1 & 1/2 \\ -1/2 & 0 \end{pmatrix}$ è la sua inversa.
> *(Nota: I numeri dell'esercizio potrebbero differire ma lo scopo è testare $AB=I$).*
>
> **Soluzione passo-passo:**
> Se $B$ è l'inversa di $A$, calcolando il prodotto $(A \cdot B)$ dovremmo ottenere $I_2$.
> $AB = \begin{pmatrix} 0 & -1 \\ 1 & 2 \end{pmatrix} \begin{pmatrix} 1 & 1/2 \\ -1/2 & 0 \end{pmatrix}$
> Riga 1, Colonna 1: $0 \cdot 1 + (-1) \cdot (-1/2) = 1/2 \neq 1$.
> Dato che il primo elemento non è $1$ (e dovrebbe ricreare l'Identità), $B$ **non** è l'inversa di $A$. 
> 
> *(Controesercizio: Prova con $B = \begin{pmatrix} 1 & 1/2 \\ 1/2 & 0 \end{pmatrix}$ ecc...)*

## Collegamenti
- Back: [[01 - Matrici]]
- Previous: [[Prodotto Righe per Colonne]]
