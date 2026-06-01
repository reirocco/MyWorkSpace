
# Prodotto scalare ^prodotto-scalare
Presi due vettori $V,W \in R^n$  il loro prodotto scalare è: $$<v,w> = ^tV*W = v_{1}w_{1}+v_{2}w_{2}+\dots+v_{n}w_{n}$$TIP. prodotto riga per colonna, si ottiene un valore reale
è ==bilineare, simmetrico, definito positivo, non degenere==( [[8. PRODOTTO SCALARE e TEOREMA SPETTRALE.pdf#page=4]])
	
Se il prodotto scale di due vettori è 0 si dice che i due vettori sono ==ortogonali o perpendicolari== e si indica con $v \perp w$.
___
Potremmo pensare al prodotto scalare ==$<v,w>$ come quanto il vettore $v$ va nella stessa direzione del vettore $w$==.
___
![[prodotto_scalare.png|391]]

## Norma^norma
La norma ( o modulo) è la lunghezza di un vettore  $$||V||= \sqrt{ <v,v>} = \sqrt{ v_{1}^2 +v_{2}^2+\dots+v_{n}^2 }$$essendo una somma il risultato $\in R$.
TIP. il teorema di pitagora è la norma di 2 vettori, più avanti la useremo per calcolare le la distanza tra punti nello spazio.

## Angolo compreso ^coseno-angolo
$$\cos(\hat{vw}) = \frac{<v,w>}{||v||*||w||}$$ dimostrazione con disuguaglianza di couchy-swarz e angoli ortogonali, la disuguaglianza ti dice che il valore massimo che si può attribuire al coseno è 1 e che la proiezione di $u$ su $v$ al massimo è lunga quanto il vettore $v$
___
> [!NOTE] Possiamo vederlo come: $$P_{w}(v)= \frac{\text{quanto il vettore v va nella stessa direzione di w}}{\text{norma di v * norma di w}}$$
## Proiezione ortogonale di $u$ su $v$
$$P_{v}(u)= \frac{<u,v>}{<v,v>}v$$
con semplici calcoli possiamo ricondurre $P_{v}(u)$ ad una forma che frutta il coseno al numeratore ed al denominatore.