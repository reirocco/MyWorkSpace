---
tags:
  - matematica
  - algebra/diagonalizzabilità
aliases:
  - Molteplicità Algebrica
  - Molteplicità Geometrica
  - m_a e m_g
---

# Molteplicità Algebrica e Geometrica

Ad ogni autovalore $\lambda$ trovato durante lo studio di un endomorfismo, sono intrinsecamente associati due numeri interi positivi, detti **Molteplicità**. La relazione tra questi due numeri decide le sorti della diagonalizzabilità dell'intera matrice.

---

## 1. Molteplicità Algebrica $m_a(\lambda)$

La molteplicità algebrica è un concetto puramente algebrico, legato al Teorema Fondamentale dell'Algebra e ai polinomi.

> [!abstract] Definizione
> La **Molteplicità Algebrica** $m_a(\lambda)$ di un autovalore $\lambda$ è il suo "peso" come radice del polinomio caratteristico $p_A(t)$.
> In altre parole, è il massimo esponente intero $k \ge 1$ per il quale il termine $(t - \lambda)^k$ divide il polinomio caratteristico.

* **Esempio:** Se il polinomio caratteristico è $p_A(t) = (t - 2)^3 (t - 5)$, allora:
  - L'autovalore $\lambda_1 = 2$ ha $m_a(2) = 3$.
  - L'autovalore $\lambda_2 = 5$ ha $m_a(5) = 1$ (si dice radice semplice).

* **Proprietà:** La somma di tutte le molteplicità algebriche delle radici reali e complesse è sempre esattamente $n$ (il grado del polinomio/dimensione della matrice).

---

## 2. Molteplicità Geometrica $m_g(\lambda)$

La molteplicità geometrica è un concetto spaziale. Definisce quanto è "largo" lo spazio degli autovettori (l'autospazio) associato all'autovalore.

> [!abstract] Definizione
> La **Molteplicità Geometrica** $m_g(\lambda)$ di un autovalore $\lambda$ è la dimensione del suo Autospazio $E_\lambda = \ker(A - \lambda I)$.
> Operativamente, si calcola tramite il Teorema di Nullità più Rango:
> $$ m_g(\lambda) = \dim(\ker(A - \lambda I)) = n - \text{rango}(A - \lambda I) $$

* **Significato Strutturale:** Indica quanti autovettori *linearmente indipendenti* sono associati all'autovalore $\lambda$.

---

## 3. Il Limite Ferreo (La Relazione di Disuguaglianza)

I due concetti, pur provenienti da logiche diverse, sono collegati da una disuguaglianza fondamentale dell'Algebra Lineare.

> [!important] Teorema della Disuguaglianza delle Molteplicità
> Per ogni autovalore $\lambda$ reale, vale **sempre** la seguente catena di disuguaglianze:
> $$ 1 \le m_g(\lambda) \le m_a(\lambda) \le n $$

**Spiegazione Pratica per l'Esame:**
1. **$m_g(\lambda) \ge 1$ (Il limite inferiore):**
   Se $\lambda$ è un autovalore, **esiste per forza** almeno un autovettore non nullo a lui associato. Quindi il suo autospazio ha dimensione almeno 1. Se calcoli il rango della matrice $(A - \lambda I)$ e ottieni esattamente $n$ (rango massimo), la nullità è 0, il che significa che hai sbagliato a risolvere il polinomio caratteristico: $\lambda$ NON è un autovalore!
2. **$m_g(\lambda) \le m_a(\lambda)$ (Il limite superiore):**
   La dimensione geometrica dello spazio vettoriale generato (il numero di frecce indipendenti) **non può mai eccedere** la molteplicità teorica della radice nel polinomio. Se in un esercizio ti ritrovi un autospazio di dimensione 3, ma l'autovalore appariva solo al quadrato nel polinomio ($m_a = 2$), c'è un errore nei calcoli del rango.

Se per *tutti* gli autovalori avviene il "miracolo" in cui la geometria si espande fino a toccare il limite dell'algebra ($m_g = m_a$), l'endomorfismo si definisce **diagonalizzabile**.

---
## Collegamenti
* **Back:** [[00_Diagonalizzabilita_MOC|MOC Diagonalizzabilità]]
* **Previous:** [[Autovalori e Autovettori]]
* **Next:** [[Criterio di Diagonalizzabilità]]
