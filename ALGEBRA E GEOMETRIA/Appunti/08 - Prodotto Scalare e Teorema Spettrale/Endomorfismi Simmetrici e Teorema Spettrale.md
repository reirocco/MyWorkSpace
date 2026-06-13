---
tags:
  - matematica
  - algebra/prodotto_scalare
  - algebra/diagonalizzabilità
aliases:
  - Teorema Spettrale
  - Endomorfismo Simmetrico
  - Matrice Simmetrica
  - Diagonalizzazione Ortogonale
---
# Endomorfismi Simmetrici e Teorema Spettrale

Il Teorema Spettrale rappresenta il vertice dell'Algebra Lineare. È il punto di convergenza assoluta in cui i concetti di prodotto scalare, ortogonalità e diagonalizzazione si fondono in un unico, maestoso risultato strutturale.

---

## 1. Endomorfismi e Matrici Simmetriche

Il soggetto di questo teorema sono le matrici simmetriche.

> [!abstract] Definizione Analitica e Geometrica
> Una matrice $A \in M_n(\mathbb{R})$ si dice **simmetrica** se coincide con la sua trasposta: $A = A^T$.
> Un endomorfismo $T: \mathbb{R}^n \to \mathbb{R}^n$ si dice **simmetrico** (o autoaggiunto) se, per ogni scelta di vettori $v, w$, la matrice scambia liberamente di posto all'interno del prodotto scalare:
> $$ \langle T(v), w \rangle = \langle v, T(w) \rangle $$
> *(Un endomorfismo è simmetrico se e solo se la sua matrice associata rispetto a una base ortonormale è simmetrica).*

---

## 2. Il Teorema Spettrale (Enunciato)

> [!important] Il Teorema Spettrale (Caso Reale)
> Se $A$ è una matrice reale e simmetrica, allora **$A$ è sempre diagonalizzabile tramite una matrice ortogonale**.
> 
> Esiste cioè una matrice ortogonale $M$ (tale che $M^{-1} = M^T$) e una matrice diagonale $D$ tali che:
> $$ D = M^T \cdot A \cdot M $$

Questo teorema non dice solo che la matrice è diagonalizzabile. Dice una cosa profondamente più forte: la base di autovettori può essere scelta in modo da essere **Ortonormale**. 

### I "Tre Miracoli" del Teorema Spettrale
Dietro questo enunciato si nascondono tre proprietà clamorose che valgono **ESCLUSIVAMENTE** per le matrici simmetriche reali:
1. **Miracolo Algebrico (Tutti Autovalori Reali):** Il polinomio caratteristico di una matrice simmetrica non genera mai radici complesse. Ha sempre $n$ radici rigorosamente in $\mathbb{R}$ (contate con molteplicità).
2. **Miracolo Dimensionale (Sempre Diagonalizzabile):** Il dramma $m_a \neq m_g$ non esiste. Per una matrice simmetrica reale, la molteplicità algebrica coincide *sempre e in ogni caso* con la molteplicità geometrica per ogni autovalore. Se all'esame stai diagonalizzando una matrice simmetrica e ottieni $m_a \neq m_g$, c'è indiscutibilmente un errore di calcolo.
3. **Miracolo Geometrico (Ortogonalità degli Autospazi):** Autovettori relativi ad autovalori **distinti** non sono solo linearmente indipendenti, sono **strettamente perpendicolari**. Il prodotto scalare tra di essi è garantitamente zero.

---

## 3. Algoritmo di Diagonalizzazione Ortogonale

Come operare all'esame se l'esercizio chiede di "diagonalizzare ortogonalmente" una matrice simmetrica $A$?

1. **Calcola gli Autovalori:** Determina le radici di $p_A(\lambda) = 0$. (Ricorda: saranno tutti reali).
2. **Calcola gli Autospazi:** Per ogni autovalore, risolvi $(A-\lambda I)X = \mathbf{0}$ per trovare la base dell'autospazio.
3. **Ortogonalizza (Gram-Schmidt):**
   - Se l'autospazio ha dimensione 1 (l'autovalore è semplice), il vettore trovato va bene così (dovrai solo normalizzarlo).
   - Se l'autospazio ha dimensione $\ge 2$ (autovalori doppi o tripli), i vettori della base che hai trovato *potrebbero non essere perpendicolari tra loro*! Devi forzarli a esserlo applicando l'[[Basi Ortogonali e Gram-Schmidt|Algoritmo di Gram-Schmidt]] a quei soli vettori.
4. **Normalizza:** Prendi tutti i vettori e dividili per la loro norma per renderli versori (lunghezza 1).
5. **Costruisci le Matrici:**
   - Inserisci gli autovalori in $D$.
   - Inserisci le basi ortonormalizzate come *colonne* in $M$.
   Il gioco è fatto. Ora puoi affermare fieramente che $D = M^T A M$.

---
## Collegamenti
* **Back:** [[00_Prodotto_Scalare_MOC|MOC Prodotto Scalare]]
* **Previous:** [[Matrici Ortogonali]]
