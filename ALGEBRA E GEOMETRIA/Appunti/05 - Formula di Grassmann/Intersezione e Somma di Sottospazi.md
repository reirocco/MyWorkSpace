---
tags:
  - matematica
  - algebra/spazi_vettoriali
aliases:
  - Intersezione di sottospazi
  - Somma di sottospazi
---
# Intersezione e Somma di Sottospazi

Dati due sottospazi vettoriali $U$ e $W$ dello stesso spazio $V$, possiamo "combinarli" in due modi principali. Notiamo che la semplice **unione** $U \cup W$ **NON è quasi mai un sottospazio** (ad esempio, l'unione dell'asse $x$ e dell'asse $y$ non contiene i punti fuori dagli assi, quindi non è chiusa per somma).

## 1. Sottospazio Intersezione
Il sottospazio intersezione è formato da tutti i vettori che appartengono **sia** a $U$ **sia** a $W$:
$$ U \cap W = \{ v \in V : v \in U \text{ e } v \in W \} $$
- $U \cap W$ è **sempre** un sottospazio vettoriale.
- **Calcolo pratico:** Si calcola unendo a sistema le *equazioni cartesiane* di $U$ e di $W$. Le soluzioni del sistema unito formano l'intersezione.

## 2. Sottospazio Somma
Il sottospazio somma è formato da tutti i possibili vettori ottenuti sommando un vettore di $U$ con un vettore di $W$:
$$ U + W = \{ u + w \in V : u \in U, w \in W \} $$
- $U + W$ è il *più piccolo* sottospazio vettoriale che contiene sia $U$ che $W$.
- **Calcolo pratico:** Si prendono i generatori (le basi) di $U$ e i generatori di $W$ e li si mettono insieme: $\text{Span}(u_1, \dots, u_k, w_1, \dots, w_p)$. Per trovare una base della somma, si estraggono i vettori linearmente indipendenti da questo grande insieme (ad esempio, mettendoli in matrice e calcolando i pivot).

> [!info]- Dimostrazione: L'intersezione è un Sottospazio
> Poiché $U$ e $W$ sono sottospazi, $\mathbf{0}_V \in U$ e $\mathbf{0}_V \in W$, dunque $\mathbf{0}_V \in U \cap W$.
> Siano $v_1, v_2 \in U \cap W$ e $c \in \mathbb{R}$.
> Poiché appartengono a $U$, $v_1+v_2 \in U$ e $c \cdot v_1 \in U$.
> Poiché appartengono a $W$, $v_1+v_2 \in W$ e $c \cdot v_1 \in W$.
> Quindi la somma e il prodotto per scalare appartengono a $U \cap W$.

## Collegamenti
- Back: [[00_Grassmann_MOC|MOC Formula di Grassmann]]
- Next: [[Formula di Grassmann]]
