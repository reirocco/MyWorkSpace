---
tags:
  - matematica
  - algebra/preliminari
aliases:
  - Iniettiva
  - Suriettiva
  - Biiettiva
---
# Funzioni

Dati due insiemi $A$ e $B$, una funzione $f: A \to B$ è una legge che associa ad ogni elemento $a \in A$ uno e un solo elemento $b \in B$.
Definiamo quattro concetti fondamentali legati a questa associazione:

- **Dominio ($A$)**: L'insieme di partenza, ovvero l'insieme di tutti i valori di input su cui la funzione è definita. Affinché $f$ sia una vera funzione, *ogni* elemento del dominio deve avere un corrispondente associato in $B$.
- **Codominio ($B$)**: L'insieme di arrivo "dichiarato". È l'insieme che contiene tutti i *potenziali* valori di output della funzione, prima ancora di sapere quali verranno effettivamente raggiunti.
- **Immagine ($\text{Im}(f)$ o $f(A)$)**: L'insieme di tutti gli output *effettivamente* prodotti dalla funzione. In simboli: $\text{Im}(f) = \{f(a) \in B : a \in A\}$. Notare che $\text{Im}(f)$ è un sottoinsieme del codominio $B$, ma non coincide necessariamente con tutto $B$.
- **Controimmagine (o pre-immagine)**: Dato un elemento (o un sottoinsieme) del codominio, la sua controimmagine è l'insieme di tutti gli elementi del dominio che vi vengono "mappati" dalla funzione. Se prendiamo $b \in B$, la sua controimmagine è $f^{-1}(b) = \{a \in A : f(a) = b\}$. (Questo insieme può essere vuoto, avere un elemento, o averne molti).

## Iniettività, Suriettività, Biiettività

1. **Iniettiva**: Ad elementi distinti corrispondono immagini distinte.
   $f(a_1) = f(a_2) \implies a_1 = a_2$ (oppure $a_1 \neq a_2 \implies f(a_1) \neq f(a_2)$).
2. **Suriettiva**: L'immagine della funzione ricopre tutto il codominio. 
   Per ogni $b \in B$, esiste almeno un $a \in A$ tale che $f(a) = b$.
3. **Biiettiva** (o Biunivoca): Sia iniettiva che suriettiva.

> [!abstract] Condizione per l'Invertibilità
> Una funzione $f: A \to B$ è **invertibile** (esiste $f^{-1}: B \to A$) **se e solo se** è biiettiva.

> [!tip] Riorganizzare Dominio e Codominio
> Se una funzione non è iniettiva, si può "renderla" tale restringendo il suo dominio.
> Se non è suriettiva, la si può rendere tale considerando come codominio esattamente la sua immagine $f(A)$.

## Cardinalità
Se $A$ e $B$ sono insiemi finiti:
- Se esiste $f$ iniettiva, $|A| \le |B|$.
- Se esiste $f$ suriettiva, $|A| \ge |B|$.
- Se esiste $f$ biiettiva, $|A| = |B|$.

## Collegamenti
- Back: [[00_Nozioni_Preliminari_MOC|MOC Nozioni Preliminari]]
- Previous: [[Logica]]
- Next: [[Polinomi e Radici]]
