---
tags:
  - matematica
  - algebra/sistemi
aliases:
  - Rouché-Capelli
---
# Teorema di Rouché-Capelli

Il **Teorema di Rouché-Capelli** è il cardine della teoria dei sistemi lineari: stabilisce se un sistema è risolvibile e quante soluzioni possiede in base al rango delle sue matrici associate.

## Il Teorema
Sia $AX = B$ un sistema lineare con $m$ equazioni e $n$ incognite. Il sistema è **compatibile** (ha almeno una soluzione) se e solo se il rango della matrice incompleta $A$ è uguale al rango della matrice completa $(A|B)$:
$$ \text{rk}(A) = \text{rk}(A|B) $$

### Numero di Soluzioni
Se il sistema è compatibile ($\text{rk } A = \text{rk } (A|B) = r$), allora:
1. Se $r = n$ (rango uguale al numero di incognite), il sistema ha **una e una sola soluzione**.
2. Se $r < n$, il sistema ha **infinite soluzioni** che dipendono da $n - r$ parametri liberi. Si scrive che il sistema ha $\infty^{n-r}$ soluzioni.

> [!important] Parametri Liberi
> I parametri liberi rappresentano i "gradi di libertà" del sistema. Se hai 3 incognite e $r=2$, avrai $\infty^1$ soluzioni, ovvero le soluzioni formeranno una retta nello spazio.

> [!info]- Dimostrazione: Teorema di Rouché-Capelli
> Il sistema $AX = B$ ammette soluzioni se e solo se $B$ è combinazione lineare delle colonne di $A$. Da questo, per le proprietà del rango (rango dopo aggiunta di una linea), segue che $\text{rg}(A) = \text{rg}(C)$. 
> Viceversa, se $\text{rg}(A) = \text{rg}(C)$, si ha che $B$ deve essere combinazione lineare delle colonne di $A$, altrimenti il rango sarebbe aumentato di $1$ nel passaggio dalla matrice incompleta $A$ alla completa $C$. Quindi il sistema ha soluzione.

> [!question]- Esercizio Pratico
> Stabilisci se il sistema è risolvibile:
> $$
> \begin{cases} x + 2y - z = 1 \\ 2x + 4y - 2z = 0 \end{cases}
> $$
> 
> **Soluzione passo-passo:**
> 1. Scriviamo $A = \begin{pmatrix} 1 & 2 & -1 \\ 2 & 4 & -2 \end{pmatrix}$. Notiamo che la seconda riga è il doppio della prima. Quindi $\text{rk } A = 1$.
> 2. Scriviamo $(A|B) = \begin{pmatrix} 1 & 2 & -1 & 1 \\ 2 & 4 & -2 & 0 \end{pmatrix}$.
> 3. Vediamo se $\text{rk}(A|B) = 1$: consideriamo il minore formato dalle colonne 1 e 4: $\begin{vmatrix} 1 & 1 \\ 2 & 0 \end{vmatrix} = 0 - 2 = -2 \neq 0$. Quindi $\text{rk}(A|B) = 2$.
> 4. Poiché $\text{rk } A = 1 \neq 2 = \text{rk } (A|B)$, il sistema è **incompatibile** (nessuna soluzione).

## Collegamenti
- Back: [[00_Sistemi_Lineari_MOC|MOC Sistemi Lineari]]
- Next: [[Sistemi Lineari Omogenei]]
