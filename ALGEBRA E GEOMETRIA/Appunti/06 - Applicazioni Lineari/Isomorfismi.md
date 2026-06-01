---
tags:
  - matematica
  - algebra/applicazioni_lineari
aliases:
  - Isomorfismo
  - Isomorfi
---
# Isomorfismi

Un **Isomorfismo** è un'applicazione lineare $T: V \to W$ che è **biiettiva** (sia iniettiva che suriettiva).

Se tra due spazi vettoriali esiste un isomorfismo, si dice che i due spazi sono **isomorfi** ($V \cong W$). Dal punto di vista algebrico, due spazi isomorfi sono indistinguibili: hanno le stesse proprietà, cambia solo il "nome" (o la natura) degli elementi.

## Caratterizzazione
Un'applicazione lineare tra spazi di dimensione finita è un isomorfismo **se e solo se**:
1. $\dim(V) = \dim(W)$ (gli spazi hanno la stessa dimensione).
2. Il determinante della matrice quadrata associata è non nullo ($\det(A) \neq 0$).

> [!important] Proprietà Conservate dagli Isomorfismi
> Un isomorfismo è il "trasporto perfetto":
> - Se $v_1, \dots, v_k$ sono linearmente indipendenti, anche $T(v_1), \dots, T(v_k)$ lo sono.
> - Se formano una base in $V$, le loro immagini formano una base in $W$.
> - Manda sottospazi di dimensione $k$ in sottospazi di dimensione $k$.

## Collegamenti
- Back: [[00_Applicazioni_Lineari_MOC|MOC Applicazioni Lineari]]
- Previous: [[Matrice Associata]]
