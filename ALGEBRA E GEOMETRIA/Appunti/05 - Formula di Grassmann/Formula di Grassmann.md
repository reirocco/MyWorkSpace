---
tags:
  - matematica
  - algebra/spazi_vettoriali
aliases:
  - Formula di Grassmann
---
# Formula di Grassmann

La **Formula di Grassmann** stabilisce una relazione dimensionale fondamentale tra due sottospazi vettoriali, la loro intersezione e la loro somma.

## Il Teorema
Siano $U$ e $W$ due sottospazi di uno spazio vettoriale $V$ di dimensione finita. Allora:
$$ \dim(U + W) + \dim(U \cap W) = \dim(U) + \dim(W) $$

O equivalentemente:
$$ \dim(U + W) = \dim(U) + \dim(W) - \dim(U \cap W) $$

> [!abstract] Interpretazione Intuitiva
> Se sommiamo le dimensioni di $U$ e $W$, stiamo "contando due volte" la dimensione della loro intersezione (i vettori che condividono). Sottraendo una volta l'intersezione, otteniamo la dimensione dello spazio complessivo che generano uniti ($U+W$).

> [!question]- Esercizio Pratico (Heuristic)
> Siano $U$ e $W$ due piani (dimensione 2) distinti in $\mathbb{R}^3$, entrambi passanti per l'origine. Quanto vale la dimensione della loro intersezione?
> 
> **Soluzione:**
> 1. Trattandosi di piani distinti non paralleli (passano per l'origine), essi generano tutto $\mathbb{R}^3$. Quindi $\dim(U+W) = 3$.
> 2. Sappiamo che $\dim(U) = 2$ e $\dim(W) = 2$.
> 3. Applichiamo Grassmann: $\dim(U \cap W) = \dim(U) + \dim(W) - \dim(U+W) = 2 + 2 - 3 = 1$.
> 4. Conclusione: Due piani distinti passanti per l'origine in $\mathbb{R}^3$ si intersecano sempre in una **retta** ($\dim = 1$).

## Collegamenti
- Back: [[00_Grassmann_MOC|MOC Formula di Grassmann]]
- Previous: [[Intersezione e Somma di Sottospazi]]
- Next: [[Somma Diretta e Supplementari]]
