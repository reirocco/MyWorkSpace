---
tags:
  - matematica
  - algebra/diagonalizzabilità
aliases:
  - Algoritmo diagonalizzazione
  - Ricerca della Matrice D e P
---
# Algoritmo Pratico di Diagonalizzazione

L'applicazione del Criterio di Diagonalizzabilità a una matrice concreta richiede di eseguire una sequenza algoritmica di calcoli molto specifica. 
Dato un esercizio del tipo: *"Stabilire se la matrice $A \in M_n$ è diagonalizzabile e, in caso affermativo, trovare una matrice invertibile $P$ e una matrice diagonale $D$ tali che $D = P^{-1} A P$"*, occorre seguire questi step:

---

## Step 1: Il Polinomio Caratteristico e gli Autovalori
Costruisci la matrice $(A - \lambda I)$, sottraendo l'incognita $\lambda$ a tutti gli elementi della diagonale principale.
Calcola il determinante $p(\lambda) = \det(A - \lambda I)$ per trovare il polinomio caratteristico.
- **Risolvi $p(\lambda) = 0$** per determinare gli autovalori (le radici).
- *Attenzione al Campo:* Se stai lavorando su $\mathbb{R}$ e trovi radici complesse coniugate (es. $\lambda^2 + 1 = 0$), puoi fermarti immediatamente: **la matrice NON è diagonalizzabile su $\mathbb{R}$** poiché non tutti gli autovalori appartengono al campo.

## Step 2: Molteplicità Algebriche
Per ogni autovalore $\lambda_i$, annota la sua molteplicità algebrica $m_a(\lambda_i)$ (il numero di volte in cui è radice del polinomio).
- **Shortcut (Autovalori Distinti):** Se la matrice ha dimensione $n$ e hai trovato $n$ autovalori **distinti** (cioè tutti con $m_a = 1$), per il Corollario del criterio sai già che **la matrice è diagonalizzabile con certezza**. Puoi saltare lo Step 3 e passare diretto allo Step 4.

## Step 3: Molteplicità Geometriche (Il test vero e proprio)
Per ogni autovalore $\lambda_i$ che ha $m_a > 1$ (gli "autovalori doppi, tripli, ecc."), devi calcolarne la molteplicità geometrica:
1. Sostituisci il numero $\lambda_i$ all'interno della matrice $(A - \lambda I)$.
2. Calcola il **Rango** di questa matrice numerica.
3. Determina $m_g(\lambda_i) = n - \text{rango}(A - \lambda_i I)$.

> [!important] Il Bivio Decisivo
> - Se per *anche un solo* autovalore risulta $m_g(\lambda_i) < m_a(\lambda_i)$, la procedura fallisce. **La matrice NON è diagonalizzabile.** L'esercizio è finito.
> - Se per *ogni* autovalore risulta $m_g(\lambda_i) = m_a(\lambda_i)$, la matrice **è diagonalizzabile**. Procedi.

## Step 4: Calcolo degli Autospazi
Per costruire la matrice di passaggio $P$, abbiamo bisogno degli autovettori.
Per ogni autovalore $\lambda_i$, risolvi il sistema lineare omogeneo associato:
$$ (A - \lambda_i I) \begin{pmatrix} x_1 \\ \dots \\ x_n \end{pmatrix} = \begin{pmatrix} 0 \\ \dots \\ 0 \end{pmatrix} $$
Risolvendo il sistema, otterrai una base dell'autospazio $E_{\lambda_i}$. Raccogli tutti questi vettori di base in un unico insieme. Poiché la matrice è diagonalizzabile, l'unione di queste basi ti darà esattamente $n$ autovettori linearmente indipendenti.

## Step 5: Costruzione di $D$ e $P$
Ora hai tutti i pezzi per assemblare la risposta.
- **La Matrice Diagonale $D$:** Costruisci una matrice $n \times n$ posizionando gli autovalori trovati sulla diagonale principale, *ripetuti un numero di volte pari alla loro molteplicità*. Tutti gli altri elementi sono zero.
- **La Matrice di Passaggio $P$ (o $M$):** Costruisci una matrice le cui **colonne** sono i vettori della base di autovettori trovati allo Step 4.

> [!warning] Ordine Vincolante!
> L'ordine in cui metti gli autovettori nelle colonne di $P$ **DEVE corrispondere esattamente** all'ordine in cui hai posizionato i relativi autovalori sulla diagonale di $D$.
> *Esempio: Se in $D$ il primo numero sulla diagonale è $\lambda = 2$, allora la prima colonna di $P$ deve essere obbligatoriamente un autovettore relativo all'autovalore 2.*

---

## Esempio Logico

Consideriamo $A \in M_3(\mathbb{R})$ con polinomio $p(\lambda) = -\lambda(\lambda - 3)^2$.
1. **Autovalori e $m_a$:** $\lambda_1 = 0$ ($m_a = 1$), $\lambda_2 = 3$ ($m_a = 2$).
2. **Molteplicità geometrica:** Per $\lambda_1=0$, $m_a=1 \implies m_g=1$ per forza. Dobbiamo testare solo $\lambda_2=3$. 
   Se calcolando $\text{rango}(A - 3I)$ otteniamo $1$, allora $m_g(3) = 3 - 1 = 2$.
   Siccome $m_g(3) = m_a(3) = 2$, la matrice è diagonalizzabile.
3. **Autospazi:** 
   - $(A - 0I)x = \mathbf{0} \implies$ Troviamo 1 vettore $v_1$.
   - $(A - 3I)x = \mathbf{0} \implies$ Troviamo 2 vettori $v_2, v_3$.
4. **Assemblaggio:**
   $P = \begin{pmatrix} | & | & | \\ v_1 & v_2 & v_3 \\ | & | & | \end{pmatrix}$ e $D = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 3 \end{pmatrix}$

---
## Collegamenti
* **Back:** [[00_Diagonalizzabilita_MOC|MOC Diagonalizzabilità]]
* **Previous:** [[Criterio di Diagonalizzabilità]]
