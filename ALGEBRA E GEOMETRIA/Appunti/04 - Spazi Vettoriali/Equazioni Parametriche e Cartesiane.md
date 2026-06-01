---
tags:
  - matematica
  - algebra/spazi_vettoriali
aliases:
  - Equazioni Parametriche
  - Equazioni Cartesiane
  - Codimensione
---
# Equazioni Parametriche e Cartesiane

Sia $W \subseteq \mathbb{R}^n$ un sottospazio vettoriale di dimensione $k$.
Abbiamo due modi distinti ma complementari per rappresentare l'appartenenza di un vettore $X = (x_1, \dots, x_n)^T$ a $W$.

## 1. Equazioni Parametriche (Tramite Generatori)
Se conosciamo una base di $W$, diciamo $w_1, \dots, w_k$, allora ogni vettore $X \in W$ si scrive come combinazione lineare di questa base:
$$ X = t_1 w_1 + t_2 w_2 + \dots + t_k w_k $$
Al variare dei parametri $t_1, \dots, t_k \in \mathbb{R}$, otteniamo tutti e soli i vettori di $W$. 
> Per generare un sottospazio di dimensione $k$, servono **$k$ parametri liberi**.
> **Dimensione come numero di vettori**

## 2. Equazioni Cartesiane (Tramite Rango)
Sappiamo che $X \in W \iff$ $X$ è linearmente dipendente dai generatori $w_1, \dots, w_k$.
Se costruiamo una matrice affiancando in colonna i vettori $w_1, \dots, w_k$ e per ultima la colonna generica $X$, questa matrice $(n \times (k+1))$ deve avere rango $k$.
Applicando il [[Teorema degli Orlati]], imponiamo che gli orlati di ordine $k+1$ abbiano tutti **determinante uguale a zero**.

Le equazioni che otteniamo annullando questi determinanti costituiscono un sistema omogeneo. 
> Per descrivere un sottospazio di dimensione $k$ in $\mathbb{R}^n$, sono necessarie e sufficienti **$n - k$ equazioni cartesiane linearmente indipendenti**. 
> Il numero $n - k$ si chiama **Codimensione** di $W$.

> [!tip] Da Parametriche a Cartesiane
> Il passaggio consiste proprio nello scrivere la matrice con i generatori e il vettore $(x,y,z)$, calcolare i determinanti dei minori "orlati" e porli a zero. Queste saranno le tue equazioni!

> [!question]- Esercizio Pratico
> Trova l'equazione cartesiana del piano $W$ in $\mathbb{R}^3$ generato da $w_1 = (1, 0, 1)^T$ e $w_2 = (0, 1, 1)^T$.
> 
> **Soluzione passo-passo:**
> 1. Dimensione $n=3$, dimensione di $W = k = 2$. Ci aspettiamo $3-2=1$ equazione cartesiana.
> 2. Costruiamo la matrice: $\begin{pmatrix} 1 & 0 & x \\ 0 & 1 & y \\ 1 & 1 & z \end{pmatrix}$.
> 3. Questa matrice $3 \times 3$ deve avere determinante nullo per far sì che la terza colonna sia dipendente dalle prime due.
> 4. Sviluppiamo il determinante (es. lungo la prima riga): $1 \cdot (z - y) - 0 + x \cdot (0 - 1) = z - y - x$.
> 5. L'equazione cartesiana è: $x + y - z = 0$.

## Collegamenti
- Back: [[00_Spazi_Vettoriali_MOC|MOC Spazi Vettoriali]]
- Previous: [[Coordinate e Isomorfismo con Rn]]
- Next: [[Sottospazi Affini]]
