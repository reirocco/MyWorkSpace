---
tags:
  - matematica
  - algebra/rango
  - algebra/gauss
aliases:
  - Riduzione a scala
  - Gauss-Jordan
---
# Algoritmo di Eliminazione di Gauss

L'**Algoritmo di Gauss** è la procedura sistematica per trasformare qualsiasi matrice $M_{m,n}$ in una matrice a scala tramite **operazioni elementari di riga**, senza alterarne il rango.

## Operazioni Elementari (ammesse)
Le tre operazioni che non cambiano il rango sono:
1. **Scambiare** due righe ($R_i \leftrightarrow R_j$).
2. **Moltiplicare** una riga per uno scalare non nullo ($R_i \to \lambda R_i, \lambda \neq 0$).
3. **Sommare** a una riga il multiplo di un'altra ($R_i \to R_i + \lambda R_j$).

## Passaggi dell'Algoritmo
1. Se la prima colonna è nulla, passa alla seconda. Cerca un elemento non nullo nella colonna (preferibilmente in $a_{11}$). Se è zero, scambia la riga con una sottostante.
2. Usa il pivot trovato ($a_{11}$) per azzerare tutti gli elementi sottostanti nella stessa colonna tramite l'operazione (3).
3. Ripeti il processo sulla sottomatrice ottenuta eliminando la riga e la colonna correntemente processate.

> [!danger] Avvertenza Orale/Scritto
> Mentre il rango non cambia con queste operazioni, il **determinante** cambia segno con lo scambio (1) e viene moltiplicato per $\lambda$ con l'operazione (2). Sii cauto!

> [!info]- Dimostrazione: Invarianza del Rango e Riduzione
> **Invarianza del rango**: Se $B$ è ottenuta da $A$ tramite operazioni elementari di riga, allora $\text{rg}(B) = \text{rg}(A)$. Per le proprietà (e) ed (f) del determinante, il minore che realizza il rango di $A$ (di ordine $r$ e det $\neq 0$) rimane un minore di $B$ con determinante non nullo.
> **Riduzione a scala**: Consideriamo la prima colonna non nulla e poniamola in prima posizione. Usiamo la prima operazione per avere un $a_{11} \neq 0$. Per azzerare un elemento $a_{i1}$ sottostante, sommiamo alla riga $i$ il multiplo $-a_{i1}/a_{11}$ della prima riga. Iterando il processo colonna per colonna, ignorando le righe già usate come pivot, si giunge sempre in un numero finito di passi a una matrice a scala avente lo stesso rango dell'originale.

> [!question]- Esercizio Pratico (Riduzione)
> Riduci a scala $A = \begin{pmatrix} 1 & 2 & -1 & 0 \\ 2 & 4 & -2 & 0 \\ 1 & 1 & 0 & 1 \end{pmatrix}$ e calcolane il rango.
> 
> **Soluzione passo-passo:**
> 1. Usiamo $a_{11}=1$ come pivot. Azzeriamo sotto:
>    - $R_2 \to R_2 - 2R_1: \begin{pmatrix} 1 & 2 & -1 & 0 \\ 0 & 0 & 0 & 0 \\ 1 & 1 & 0 & 1 \end{pmatrix}$
>    - $R_3 \to R_3 - R_1: \begin{pmatrix} 1 & 2 & -1 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & -1 & 1 & 1 \end{pmatrix}$
> 2. Scambiamo $R_2$ e $R_3$ per portare la riga nulla in fondo:
>    - $R_2 \leftrightarrow R_3: \begin{pmatrix} 1 & 2 & -1 & 0 \\ 0 & -1 & 1 & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix}$
> 3. La matrice è a scala. Ha 2 righe non nulle.
> 4. Conclusione: $\text{rk} A = 2$.

## Variante di Gauss-Jordan (Matrice a Scala Ridotta)

L'**Algoritmo di Gauss-Jordan** estende il metodo di Gauss al fine di ottenere una **matrice a scala ridotta** (o *Reduced Row Echelon Form*, RREF). Una matrice a scala è ridotta se:
1. I pivot di ogni riga non nulla sono pari a $1$.
2. In ogni colonna in cui è presente un pivot, tutti gli altri elementi (sia sopra che sotto) sono nulli.

### Come si fa
Dopo aver ottenuto una matrice a scala con il normale algoritmo di Gauss (fase *forward*):
1. **Normalizzazione:** Dividi ogni riga per il proprio pivot per farlo diventare $1$ ($R_i \to \frac{1}{a_{ii}} R_i$).
2. **Eliminazione all'indietro (backward phase):** Partendo dall'ultimo pivot in basso a destra, usa l'operazione di somma (3) per azzerare tutti gli elementi **sopra** di esso.
3. Procedi a ritroso verso il primo pivot in alto a sinistra.

### Usi e Applicazioni principali
- **Calcolo della Matrice Inversa:** È il metodo standard ed efficiente per calcolare l'inversa di una matrice quadrata $A$. Si crea una matrice aumentata affiancando la matrice identità: $(A | I)$. Applicando Gauss-Jordan sull'intera matrice fino ad ottenere a sinistra l'identità $(I | B)$, la matrice $B$ risultante sarà esattamente $A^{-1}$.
- **Risoluzione di Sistemi Lineari:** Se applicato alla matrice completa $(A|b)$ di un sistema lineare, Gauss-Jordan restituisce direttamente i valori delle incognite sulla colonna dei termini noti, senza richiedere la "sostituzione all'indietro" (back-substitution).
- **Calcolo del Nucleo (Kernel):** Riducendo la matrice in forma RREF (Reduced Row Echelon Form), le equazioni che definiscono il nucleo diventano esplicite, rendendo immediata l'estrazione di una base.

## Collegamenti
- Back: [[00_Determinante_Rango_MOC|MOC Determinante e Rango]]
- Previous: [[Matrici a Scala e Pivot]]
