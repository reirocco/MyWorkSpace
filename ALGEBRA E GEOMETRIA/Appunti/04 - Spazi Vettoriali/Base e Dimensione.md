---
tags:
  - matematica
  - algebra/spazi_vettoriali
aliases:
  - Dimensione
  - Teorema delle Basi
  - Completamento Base
---
# Base e Dimensione

Una delle nozioni più importanti in Algebra Lineare è quella di "Base". Una base è un sistema di riferimento "essenziale" per uno spazio vettoriale.

## Definizione di Base
Una $n$-upla ordinata $\mathcal{B} = (v_1, \dots, v_n)$ è una **Base** dello spazio vettoriale $V$ se valgono **entrambe** le seguenti condizioni:
1. **Generano $V$**: $V = \text{Span}(v_1, \dots, v_n)$.
2. **Sono Linearmente Indipendenti**: $c_1 v_1 + \dots + c_n v_n = \mathbf{0} \implies c_1 = \dots = c_n = 0$.

> [!abstract] Dimensione e Teorema Fondamentale
> - Il **Teorema Fondamentale degli Spazi Vettoriali** afferma che se uno spazio $V$ ammette una base formata da $n$ vettori, allora ogni insieme di $k$ vettori con $k > n$ è *sicuramente linearmente dipendente*.
> - Di conseguenza, **tutte le basi** di un dato spazio vettoriale $V$ hanno lo **stesso numero di elementi**.
> - Questo numero magico è la **Dimensione** dello spazio: $\dim(V) = n$.

>[!WARNING]  Differenza tra Rango e Dimensione
>Esiste un teorema che lega il rango alla dimensione in questo modo:
>$$rk(A) = dim( \text{Spazio delle Colonne})$$
>dove lo **spazio delle colonne** non è un numero. È un **territorio geometrico** (un sottospazio vettoriale). Per la precisione, è l'insieme di _tutte le possibili combinazioni lineari_ dei vettori colonna della matrice.
>- **Il Rango è "l'osservazione algebrica":** Ti metti sopra la **matrice** e conti quante righe o colonne sono linearmente indipendenti. È un calcolo puramente numerico.
 >- **La Dimensione è "l'osservazione geometrica":** Ti metti dentro lo **spazio vettoriale** generato da quelle colonne e guardi quanti vettori servono per formare una base. È un concetto di "spazio fisco" (una retta, un piano, uno spazio 3D).

>[!example]- Che cosa rapprensenta la dimensione e che legame ha con i sottospazi?
> ==La dimensione è il numero di vettori di cui è composta una base==, questi vettori devono essere **linearmente indipendenti** e **generatori**: 
>	- **Essere indipendenti significa che l'unica combinazione lineare per ottenere il vettore nullo è porre tutti i coefficienti dei vettori a 0;**
>	- **Essere generatori significa che la loro combinazione lineare mi descrive tutto lo spazio vettoriale in cui si trovano. **
>Se ho uno Span di vettori linearmente indipendenti e la sua dimensione è uguale a quella dello spazio in cui mi trovo, allora i vettori dello Span sono sicuramente una base dello spazio vettoriale $R^n$, dove n è il numero di vettori che compongono lo span.
>Se invece ho uno Span di vettori linearmente indipendenti e la sua dimensione è inferiore a quella dello Spazio vettoriale, allora sono base dello Span ma non sono base dello spazio vettoriale ( non lo ricoprono tutto).

> [!tip] Teorema delle Basi
> In uno spazio vettoriale $V$ di dimensione $n$, presi $n$ vettori, essi costituiscono una base se soddisfano **una sola** delle due condizioni (generatori o indipendenti). L'altra condizione viene gratis!
> Dunque in $\mathbb{R}^n$, presi $n$ vettori, per verificare che formino una base basta metterli a matrice e calcolarne il **determinante**. Se $\det \neq 0$, formano una base.

## Completamento di Base
Dati $p$ vettori linearmente indipendenti in uno spazio di dimensione $n$ (con $p < n$), si possono sempre trovare altri $n-p$ vettori per "completarli" in modo da formare una base dell'intero spazio. (Spesso in $\mathbb{R}^n$ si usano i vettori della base canonica).


> [!TIP] Teorema delle Coordinate
> Sia V uno spazio vettoriale. Allora $(v1 , . . . , vn )$ è una base di $V$ $\iff$ per ogni $v ∈ V$ esistono e  sono univocamente determinati $α1 , . . . , αn ∈ R$ tali che $v = α1 v1 + . . . + αn vn$ . 

Dove, per analogia :
- $V$ è lo spazio vettoriale in cui mi trovo ( La stanza);
- ($v_{1}$,...,$vn$) è la base (sono le frecce che mi descrivono le direzioni in cui posso muovermi)
- $v$ è un punto nello spazio V
- ($a_{1}$,...,$a_{n}$) sono le coordinate reali
- $v = α1 v1 + . . . + αn vn$  è la combinazione lineare che mi descrive il punto $v$ nello spazio, e il teorema ci dice che esiste una unica combinazione di coordinate che combinate ai vettori mi descrive un punto in $V$

>[!SUCCESS]- **Il teorema in soldoni:** 
>Garantisce che per qualsiasi punto ($v$) tu scelga nella stanza, esisterà **una e una sola combinazione unica di passi** ($\alpha$) in grado di portarti esattamente su quel punto usando quelle frecce. Se ci fossero più combinazioni o nessuna, quel gruppo di frecce non sarebbe una base.
 
> [!info]- Dimostrazione: Teorema delle Coordinate
> Se $\mathcal{B} = (v_1, \dots, v_n)$ è una base, ogni vettore $v \in V$ si scrive in modo **unico** come combinazione lineare.
> L'esistenza è data dal fatto che i $v_i$ generano $V$. Per l'unicità: supponiamo per assurdo ci siano due scritture $v = a_1 v_1 + \dots + a_n v_n$ e $v = b_1 v_1 + \dots + b_n v_n$.
> Sottraendo membro a membro: $\mathbf{0} = (a_1-b_1)v_1 + \dots + (a_n-b_n)v_n$.
> Dato che i $v_i$ sono linearmente indipendenti (essendo base), tutti i coefficienti devono essere zero. Pertanto $a_i - b_i = 0 \implies a_i = b_i$ per ogni $i$. La scrittura è unica.

## Collegamenti
- Back: [[00_Spazi_Vettoriali_MOC|MOC Spazi Vettoriali]]
- Previous: [[Span e Generatori]]
- Next: [[Coordinate e Isomorfismo con Rn]]
