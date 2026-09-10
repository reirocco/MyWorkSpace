---
tags:
  - omomorfismi-anelli
  - nuclei-ideali
  - algebra
type: atomic
unit: 4
---

# Omomorfismi di Anelli

Come per i gruppi, un **Omomorfismo di Anelli** è una funzione che mappa un anello $R$ in un anello $S$ preservando l'intera struttura algebrica. Ma poiché negli anelli ci sono due operazioni (somma e prodotto), la funzione deve rispettarle entrambe.

## Definizione Formale

Una funzione $f: R \rightarrow S$ tra due anelli è un omomorfismo se per ogni $a, b \in R$ valgono simultaneamente:
1. $f(a + b) = f(a) + f(b)$ *(Preserva l'addizione)*
2. $f(a \cdot b) = f(a) \cdot f(b)$ *(Preserva la moltiplicazione)*

**Casi Speciali:**
- Se l'omomorfismo è biettivo (iniettivo e suriettivo), si chiama **Isomorfismo** di Anelli ($R \cong S$).
- Se l'omomorfismo va da un anello verso se stesso ($f: R \to R$), si chiama **Endomorfismo**.

### Omomorfismi Unitari
Se sia $R$ che $S$ sono anelli unitari (hanno l'elemento $1$), molti autori richiedono un terzo assioma:
3. $f(1_R) = 1_S$ *(L'unità va nell'unità)*.
Questa condizione non è automatica come per l'elemento neutro additivo ($f(0) = 0$).

---

## Nucleo e Immagine (Ritorno agli Ideali)

Anche per gli anelli definiamo il Nucleo (Kernel) e l'Immagine:
- $\text{Im}(f) = \{ f(r) \mid r \in R \}$. È un sotto-anello di $S$.
- $\text{Ker}(f) = \{ r \in R \mid f(r) = 0_S \}$.

> [!IMPORTANT] Il Nucleo è un Ideale!
> Nel mondo dei gruppi, il nucleo era un Sottogruppo Normale.
> Nel mondo degli anelli, il nucleo di un omomorfismo è sempre un **Ideale** dell'anello di partenza $R$ (e viceversa, ogni ideale è il nucleo di qualche omomorfismo!).
> Infatti, se $x \in \text{Ker}(f)$ (cioè $f(x)=0$) e $r \in R$, calcoliamo $f(r \cdot x) = f(r) \cdot f(x) = f(r) \cdot 0 = 0$. Quindi $r \cdot x$ "cade" ancora nel nucleo, dimostrando la magica proprietà assorbente.

---

## Teorema Fondamentale di Omomorfismo per Anelli

Il parallelismo con i gruppi è totale. Il Primo Teorema d'Omomorfismo per gli anelli afferma:
> Se $f: R \rightarrow S$ è un omomorfismo di anelli, allora l'anello quoziente $R / \text{Ker}(f)$ è isomorfo all'immagine $\text{Im}(f)$.
> $$ \frac{R}{\text{Ker}(f)} \cong \text{Im}(f) $$

---

## Tip d'Esame

> [!TIP] Come dimostrare che un omomorfismo è l'unico possibile
> A volte ti si chiede di trovare *tutti* gli omomorfismi da $\mathbb{Z}$ a un altro anello unitario $R$. In realtà, ce n'è sempre e solo **uno**!
> Se richiediamo $f(1) = 1_R$, per preservare le somme dovrà essere:
> $f(2) = f(1+1) = f(1) + f(1) = 1_R + 1_R$
> In generale, $f(n) = n \cdot 1_R$.
> La struttura di $\mathbb{Z}$ è così rigida (è generato dall'unità 1) che l'immagine di 1 fissa le immagini di tutti gli altri numeri, lasciando zero gradi di libertà.

---

## Note Correlate
- [[04.0 - MoC Anelli e Campi|Unità 4 MoC]]
- [[Definizione di Anello e Domini di Integrità]]
- [[Ideali e Anelli Quoziente]]
