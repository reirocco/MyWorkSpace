---
tags:
  - matematica
  - algebra/diagonalizzabilità
aliases:
  - Criterio di Diagonalizzabilità
  - Teorema Spettrale
---

# Criterio di Diagonalizzabilità

Per diagonalizzare una matrice $A \in M_n$, ci serve trovare una **base di autovettori**. Il criterio ci dice esattamente quando questo è possibile.

## Il Criterio Generale
Un endomorfismo $T$ (o matrice $A$) di dimensione $n$ è **diagonalizzabile se e solo se** valgono *entrambe* le seguenti condizioni:
1. **Tutti gli autovalori sono reali**. (La somma delle loro molteplicità algebriche deve fare $n$).
2. **Per ogni autovalore, la molteplicità algebrica coincide con la molteplicità geometrica**: 
   $$ m_a(\lambda) = m_g(\lambda) \quad \forall \lambda $$

> [!info]- Dimostrazione
> Se $m_a(\lambda) = m_g(\lambda)$ per ogni autovalore, allora sommando le dimensioni di tutti gli autospazi otteniamo esattamente $n$. Poiché autovettori di autovalori distinti sono indipendenti, l'unione delle basi dei vari autospazi fornisce esattamente $n$ vettori linearmente indipendenti, ovvero una **base** dell'intero spazio.

## Corollario (Autovalori Distinti)
Un caso in cui il criterio è garantito senza fare calcoli:
> Se un polinomio caratteristico di grado $n$ ha **$n$ radici reali e distinte** (tutte $m_a = 1$), allora la matrice è **sicuramente diagonalizzabile**.

*Perché? Essendo $1 \le m_g \le m_a$, se $m_a = 1$, allora per forza anche $m_g = 1$. L'uguaglianza è verificata.*

> [!danger] L'Errore Opposto
> Se una matrice ha autovalori *coincidenti* ($m_a > 1$), **potrebbe comunque essere diagonalizzabile**! (Es. la matrice Identità ha autovalore 1 con $m_a=n$ e $m_g=n$). In questi casi bisogna obbligatoriamente calcolare la molteplicità geometrica con il rango per scoprirlo.

## Collegamenti
- Back: [[00_Diagonalizzabilita_MOC|MOC Diagonalizzabilità]]
- Previous: [[Molteplicità Algebrica e Geometrica]]
- Next: [[Algoritmo Pratico di Diagonalizzazione]]
