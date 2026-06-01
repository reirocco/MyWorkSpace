Consideriamo due sottospazi $V,W \in R^n$;
Una [[Applicazione Lineare]] $T(v) : V \to W$ è un isomorfismo $\iff$ T è biettiva, ovvero se è sia suriettiva che iniettiva:
- iniettiva se $\text{ker}(T(v)) = 0_{w}$
- suriettiva se $\text{Im}(T(v)) = W$

> Se biunivoca $V$ e $W$ si dicono ==Isomorfi==
## Correlazione dei sottospazi
Se $T : V \to W$ isomorfismo esiste una correlazione della caratterizzazione dei vettori trasformati da $V \to W$.
Presi $v_{1},v_{2},\dots,v_{k}$ vettori di V allora 
- sono dipendenti in V $\iff$ $T(v_{1}),T(v_{2}),\dots,T(v_{k})$ lo sono anche in W
- generano V $\iff$ $T(v_{1}),T(v_{2}),\dots,T(v_{k})$generano W
- sono Base di V $\iff$$T(v_{1}),T(v_{2}),\dots,T(v_{k})$ sono Base di W

## Caratterizzazione degli isomorfismi
L'applicazione $T$ è un **isomorfismo** se e solo se sono soddisfatte le seguenti condizioni:

1. **Uguaglianza delle Dimensioni**: 
   $$\dim(V) = \dim(W) = n$$
2. **Invertibilità della Matrice Associata**: 
   La matrice $A = M_{\mathcal{B}}^{\mathcal{B}'}(T)$ è invertibile, ovvero $\det(A) \neq 0$.

---

## Proprietà della Matrice Associata
Sia $A$ la matrice associata a $T$ rispetto alle basi $\mathcal{B}$ e $\mathcal{B}'$. Valgono i seguenti punti:

* **Corrispondenza Biunivoca**: $T$ è biettiva $\iff A$ è una matrice quadrata con rango massimo ($rank(A) = n$).
* **L'Inversa dell'Applicazione**: Se $T$ è un isomorfismo, esiste l'applicazione inversa $T^{-1}: W \to V$. La matrice associata a $T^{-1}$ è l'inversa della matrice di $T$:
  $$M_{\mathcal{B}'}^{\mathcal{B}}(T^{-1}) = [M_{\mathcal{B}}^{\mathcal{B}'}(T)]^{-1}$$

> [!NOTE] Osservazione Geometrica
> Un isomorfismo preserva la struttura dello spazio vettoriale. Se $\dim(V) = \dim(W)$, i due spazi sono essenzialmente "copie speculari" l'uno dell'altro, e la matrice invertibile $A$ funge da "ponte" perfetto tra le due basi.
