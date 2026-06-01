Cerchiamo di dare un senso a tutto ciò che abbiamo studiato fino ad ora e iniziamo a muoverci nello spazio fissando un sistema di riferimento. 
Il sistema da  noi usato è un sistema cartesiano quindi prediamo una ==Base Ortonormale== come la base canonica e fissiamo ==l'origine 0== delgi assi.

>[!IMPORTANT] Un Punto P è un sottospazio affine di dimensione 0 e lo identifichiamo con un vettore: $$P=\begin{pmatrix} x_{1} \\ x_{2} \\\dots \\ x_{3} \end{pmatrix}$$

 Definiziamo la **Distanza tra due punti** come $$\text{dist}(P,U)=||U-P|| = \sqrt{ (p_{1}-u_{1})^2 + \dots+(p_{n}u_{n})^2 }$$
 >[!NOTE] come la formula della norma ma usando la differenza tra i due vettori (deltaP)
 
## Punto medio
Siamo $U$ e $V$ due punti di $R^n$ definisco il Punto medio come $$\overline{UV} =\frac{1}{2} \begin{pmatrix}
u_{1}+v_{1} \\
u_{2}+v_{2}+ \\
\dots \\
u_{n}+v_{n}
\end{pmatrix} $$ ## Baricentro
il Baricentro ( o punto di incontro delle mediane) si applica quando si hanno 3 punti e si trova come per il punto medio ma dividendo per 3 $$\overline{UVW} =\frac{1}{3} \begin{pmatrix}
u_{1}+v_{1}+w_{1} \\
u_{2}+v_{2}+w_{2} \\
\dots \\
u_{n}+v_{n}+w_{n}
\end{pmatrix} $$
## Iperpiano
Un iperpiano è un sottospazio affine di dimensione $n-1$
è definita da una equazione lineare di n incognite $$a_{1}x_{1}+a_{2}x_{2}+\dots+a_{nx_{n}}=0$$
dove i coefficienti $(a_{1},\dots,a_{n}) \neq(0,0,...,0)$

>[!IMPORTANTE] 
>OGNI EQUAZIONE CHE SIA LINEARMENTE INDIPENDENTE MANGIA UNA DIMENSIONE:
>>una retta è un iperpiano di $R^2$
>>un piano è un iperpiano di $R^3$
>>>una retta in $R^1$ in un piano in $R^2$ è descritta da  $2-1 = 1$ eq. cartesiana
>>>un piano in $R^2$ in uno spazio in $R^3$ è descritta da  $3-2 = 1$ eq. cartesiana
>>>una retta in $R^1$ in uno spazio in $R^3$ è descritta da  $3-1 = 2$ eq. cartesiane

## Prodotto vettoriale
Si annota come $v \wedge w$ e si usa per trovare le equazioni cartesiane di uno spazio. Si mettono in riga (o colonna) i vettori del punto/piano/spazio ( ovviamente i vettori della base) e come terza colonna si aggiunge il vettore dei versori$$v \wedge d = \det \begin{pmatrix}
\vec{i} & \vec{j} & \vec{k} \\
x_{1} & y_{1} & z_{1} \\
x_{2} & y_{2} & z_{2}
\end{pmatrix}$$Risolvendo il determinante si otterrà una forma del tipo $$(y_{1}z_{2}-y_{2}z_{1})\vec{i}-(x_{1}z_{2}-x_{2}z_{1})\vec{j}+(x_{1}y_{2}-x_{2}y_{1})\vec{k}$$ da qui è lampante che le equazioni cartesiane dei nostri vettori sono i termini dentro le parentesi per ogni versore $$\begin{pmatrix}
y_{1}-z_{1} \\
-x_{1}z_{2}+x_{2}z_{1} \\
x_{1}y_{2}-x_{2}y_{1}
\end{pmatrix}$$ 
> il prodotto vettoriale  è:
> Bilineare 
> >Distributiva
> >omogenea
> antisimmetrico

>[!WARNING] il risultato del prodotto vettoriale è un vettore ortogonale, il complemento ortogonale è lo spazio in cui vivono tutti i prodotti vettoriali
## Rette
una retta $r$ è un [[Sottospazio Affine]] di dimensione 1. Dati due punti $P^1$ e $P^2$ , la retta $\vec{P^1P^2}:=P_{2}-P_{1}$ e prende il nome di ==vettore direttore della retta r==.

>[!NOTE] Rette parallele
> Due rette si dicono ==parallele== se i loro vettori direttori sono proporzionali

==UNA RETTA = UN PUNTO E UN VETTORE DIRETTORE==
Possiamo scrivere la retta come un punto e un vettore che ne da la direzione. (vettore direttore)

Possiamo ricavare le Equazioni parametriche con la formula $P=P_{1}+tv$
per ricordarsi la formula si può dire "parto da un punto $P_{1}$ e mi muovo lungo la direzione $v$ per un tempo $t$" il che è una similitudine con il moto rettilineo uniforme.

## Genesi dell'Equazione Cartesiana del Piano in $\mathbb{R}^3$
Un **Piano** di $R^3$ è un [Sottospazio Affine] di dimensione 2. Dati 3 punti non allineati $P_{1},P_{2},P_{3}$ passa un unico piano. 
> il vettore $\vec{P_{1}P_{2}}$ è un vettore direttore del piano alfa
> un piano ha 2 vettori direttori linearmente indipendenti

### 1. Definizione Affine (Equazione Parametrica)
Si parte dal concetto che un piano $\alpha$ è definito da un punto fisso $P_1$ e due vettori direttori $v, w$ linearmente indipendenti. Ogni punto $P$ del piano si raggiunge tramite la combinazione:
$$P = P_1 + t \cdot v + s \cdot w \quad \text{con } t, s \in \mathbb{R}$$

### 2. Isolamento del Vettore Variabile (Spostamento a Sinistra)
Spostando il punto noto $P_1$ a sinistra, isoliamo il vettore che "collega" il punto noto al punto generico $P(x,y,z)$. Questo vettore deve essere interamente contenuto nella "giacitura" del piano:
$$(P - P_1) = t \cdot v + s \cdot w$$
### 3. Interpretazione tramite lo Span
L'uguaglianza precedente implica che il vettore variabile $(P - P_1)$ è una **combinazione lineare** dei vettori della base $\{v, w\}$. In termini di sottospazi vettoriali:
$$(P - P_1) \in \text{Span}\{v, w\}$$

### 4. Condizione di Dipendenza Lineare (Rango)
Poiché $(P - P_1)$ appartiene allo Span di $v$ e $w$, l'aggiunta di $(P - P_1)$ alla matrice dei direttori non può aumentarne la dimensione. La matrice risultante deve avere rango pari a 2:
$$\text{rk}(P - P_1 \mid v \mid w) = 2$$

### 5. L'Equazione Cartesiana (Determinante)
In $\mathbb{R}^3$, una matrice $3 \times 3$ con rango 2 ha necessariamente il determinante nullo. Imponendo questa condizione, si eliminano i parametri $t$ e $s$:
$$\det \begin{pmatrix} x - x_1 & v_x & w_x \\ y - y_1 & v_y & w_y \\ z - z_1 & v_z & w_z \end{pmatrix} = 0$$

### 6. Risultato Finale
Sviluppando il determinante (es. con Laplace), si ottiene la relazione lineare tra le coordinate:
$$ax + by + cz + d = 0$$
Dove il vettore $n = (a, b, c)$ è il **vettore normale** all'iperpiano, calcolabile anche come prodotto vettoriale $v \wedge w$. 



## Vettore normale ad un iperpiano

