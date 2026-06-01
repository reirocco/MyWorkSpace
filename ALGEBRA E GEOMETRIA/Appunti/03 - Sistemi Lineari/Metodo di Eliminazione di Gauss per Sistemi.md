---
tags:
  - matematica
  - algebra/sistemi
  - algebra/gauss
aliases:
  - Sistemi a scala
---
# Metodo di Eliminazione di Gauss per Sistemi

Il metodo di Gauss applicato ai sistemi lineari consiste nel ridurre a scala la **matrice completa $(A|B)$** tramite operazioni elementari per poi risolvere il sistema semplificato risultante (procedimento di "sostituzione all'indietro").

## Procedura
1. Scrivi la matrice completa $(A|B)$.
2. Applica l'[[Algoritmo di Eliminazione di Gauss]] per trasformare la parte sinistra (matrice $A$) in una matrice a scala. 
   - *Nota:* Le operazioni fatte sulle righe di $A$ devono essere applicate anche ai termini noti in $B$.
3. Leggi il rango di $A$ e $(A|B)$ per verificare la compatibilità via [[Teorema di Rouché-Capelli]].
4. Se il sistema è compatibile, riscrivilo partendo dall'ultima riga non nulla e risolvi "salendo".

> [!abstract] Vantaggio di Gauss
> A differenza di Cramer, Gauss funziona per **qualsiasi** sistema (non necessariamente quadrato) e permette di trovare facilmente le infinite soluzioni in presenza di parametri liberi.

> [!question]- Esercizio Pratico
> Risolvi:
> $$ \begin{cases} x - y + z = 1 \\ 2x - 2y + z = 0 \\ y + z = -1 \end{cases} $$
> 
> **Soluzione passo-passo:**
> 1. Matrice completa: $(A|B) = \begin{pmatrix} 1 & -1 & 1 & | & 1 \\ 2 & -2 & 1 & | & 0 \\ 0 & 1 & 1 & | & -1 \end{pmatrix}$
> 2. Riduzione a scala:
>    - $R_2 \to R_2 - 2R_1: \begin{pmatrix} 1 & -1 & 1 & | & 1 \\ 0 & 0 & -1 & | & -2 \\ 0 & 1 & 1 & | & -1 \end{pmatrix}$
>    - Scambio $R_2 \leftrightarrow R_3: \begin{pmatrix} 1 & -1 & 1 & | & 1 \\ 0 & 1 & 1 & | & -1 \\ 0 & 0 & -1 & | & -2 \end{pmatrix}$
> 3. Sostituzione all'indietro:
>    - Dalla 3ª riga: $-z = -2 \implies z = 2$.
>    - Dalla 2ª riga: $y + z = -1 \implies y + 2 = -1 \implies y = -3$.
>    - Dalla 1ª riga: $x - y + z = 1 \implies x - (-3) + 2 = 1 \implies x + 5 = 1 \implies x = -4$.
> 4. Soluzione: $(-4, -3, 2)$.

## Collegamenti
- Back: [[00_Sistemi_Lineari_MOC|MOC Sistemi Lineari]]
- Previous: [[Teorema di Cramer]]
