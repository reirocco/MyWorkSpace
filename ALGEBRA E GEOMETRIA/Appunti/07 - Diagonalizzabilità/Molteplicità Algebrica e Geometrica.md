---
tags:
  - matematica
  - algebra/diagonalizzabilità
aliases:
  - Molteplicità Algebrica
  - Molteplicità Geometrica
---

# Molteplicità Algebrica e Geometrica

Ad ogni autovalore $\lambda$ sono associati due numeri interi (molteplicità) che ne descrivono il comportamento.

## Molteplicità Algebrica $m_a(\lambda)$
È il numero di volte in cui $\lambda$ è radice del polinomio caratteristico. Ovvero, la massima potenza $k$ per cui $(x - \lambda)^k$ divide il polinomio caratteristico.
*Conta "quante volte l'autovalore appare nell'equazione".*

## Molteplicità Geometrica $m_g(\lambda)$
È la **dimensione del suo Autospazio** $E(\lambda)$. Si calcola con il teorema del rango:
$$ m_g(\lambda) = \dim(\ker(A - \lambda I)) = n - \text{rg}(A - \lambda I) $$
*Conta "quanti autovettori linearmente indipendenti genera l'autovalore".*

## Relazione Fondamentale
Esiste un limite ferreo tra questi due numeri:
$$ 1 \le m_g(\lambda) \le m_a(\lambda) $$
- **Almeno 1**: Un autovalore vero ha sempre almeno un autovettore associato.
- **Mai maggiore dell'algebrica**: La dimensione geometrica dello spazio generato non può superare la sua molteplicità come radice del polinomio.

> [!danger] Attenzione agli Errori (Heuristics)
> Se in un esercizio calcoli $m_g(\lambda)$ e ti viene $0$ (cioè $\text{rg}(A-\lambda I) = n$), significa che hai sbagliato a trovare la radice! L'autovalore **deve** abbassare il rango.
> Allo stesso modo, se $m_g(\lambda) > m_a(\lambda)$, hai fatto un errore di calcolo nel rango.

## Collegamenti
- Back: [[00_Diagonalizzabilita_MOC|MOC Diagonalizzabilità]]
- Previous: [[Autovalori e Autovettori]]
- Next: [[Criterio di Diagonalizzabilità]]
