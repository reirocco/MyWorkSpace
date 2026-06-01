Sia $T(v):V \to W$ una [[Applicazione Lineare]] il Nucleo di T è la controimmagine di $0_{w}$ tramite T : $$\ker T := \{ v \in V : T(v) \to 0_W \}$$
l'immagine  di T è : $$\operatorname{Im} T := \{T(v) \in W : v \in V\}$$
### 1. Qual'è l'ambiente (lo Spazio) in cui mi trovo?

Il kernel $\ker(t)$ è un sottospazio vettoriale del dominio $V$, mentre l'immagine $\text{Im}(t)$ è un sottospazio vettoriale del codominio $W$.

Possiamo dire che T è 
- suriettiva $\iff$ $\text{Im}(T) = W$ 
- iniettiva $\iff$ $\ker(T) = \{0_{v}\}$.

**Posso sapere ancora prima di vedere la dimensione del Nucleo e dell'Immagine?**
#### Teorema Nullità + Rango ^def-teorema-nullita-rango
Sia una applicazione lineare come la precedente 
$$\text{dim}(V) = \text{dim}(ker(T))+\text{dim}(\text{Im}(T))$$

### 2. Applicazione lineare associata alla matrice A

Sia A $\in$ $M_{m,n}$ e sia $$L_{a} : R^n \to R^m$$ definita da $L_{a}(X) = AX$ allora:
- l'immagine è il sottospazio di $R^m$ generato dalle colonne
- la dimensione di $\text{im}(L_{a}) = \text{rk(A)}$
- il $Ker(L_{a}) =$ soluzioni del sistema lineare omogeneo
- la dimensione $Ker(L_{a}) = n - \text{rk}(A)$ per Rouchè-Capelli

### 3. Flusso di Lavoro (Workflow)
per trovare il kernel di una applicazione lineare devo
1) scrivere la matrice associata alla base canonica della mia applicazione $M_{\mathcal{E}_W}^{\mathcal{E}_V}(T)$
2) risolvere il sistema con gauss-Jordan (o sostituzione), possono accadere due cose:
	1) il rango massimo e il nucleo è il vettore nullo. abbiamo finito
	2) il rango non è massimo e ci sono uno o più parametri liberi.
3) Se ci troviamo con il caso 1 abbiamo finito, con il caso 2 dobbiamo scegliere i parametri liberi ed assegnarli una lettera, portarli a dx e ridurre con gauss-jordan fino ad ottenere a sx la matrice identità. 
   ==come scelgo i parametri liberi?==
   prendiamo la matrice $$ A = \begin{pmatrix} 1 & 0 & 2 \\ 2 & -1 & 4 \\ 1 & -1 & 2 \end{pmatrix} $$
   la riduciamo con G-J e otteniamo 
   $$ A = \begin{pmatrix} 1 & 0 & 2 \\ 0 & -1 & 0 \\ 0 & 0 & 0 \end{pmatrix} $$
   prendiamo la riga con soli zeri come parametro libero ( nel caso di più righe a zero significa che avremmo più parametri liberi) e gli assegniamo una lettera (t, s, k, etc). assegnamoli la lettera $t$ e portiamo la colonna nel lato dx ( tutti i valori contenuti nella colonna al di fuori della $t$ dovranno cambiare di segno)$$
\left(
\begin{array}{cc|c}
1 & 0 & -2t \\
0 & 1 & 0 \\
0 & 0 & t
\end{array}
\right)
$$
4) la matrice è già ridotta, se non lo fosse portiamo la parte di sinistra a matrice identità.
5) prendiamo la parte dei termini noti poniamo la t a 1 e scriviamo il risultato come Span (il kernel è un sottospazio vettoriale di del dominio)$$ \text{Span} = \begin{pmatrix}-2 \\
0 \\
1
\end{pmatrix}$$
Per trovare l'immagine devo semplicemente riprendere i calcoli fatti precedentemente, trovare le colonne con i pivot e scriverle come Span (Perchè anche l'immagine è un sottospazio vettoriale!! ma del Codominio).
$$\text{Span} =  \begin{pmatrix} 1 & 0  \\ 2 & -1 \\ 1 & -1 \end{pmatrix}$$

