---
tags:
  - matematica
  - geometria
aliases:
  - Retta
  - Rette sghembe
  - Rette parallele
  - Parametrizzazione della retta
---
# Rette nello Spazio $\mathbb{R}^3$

Nello spazio, una retta è il più semplice degli oggetti geometrici unidimensionali. Algebricamente è un sottospazio affine di dimensione 1. Per costruire o descrivere univocamente una retta $r$, l'informazione minima necessaria consta di due elementi: un **Punto di Passaggio** ($P_0$) che ancora la retta allo spazio, e un **Vettore Direttore** ($v$) che ne indica l'inclinazione.

---

## 1. Rappresentazioni Algebriche

### Rappresentazione Parametrica
L'approccio cinematico: immagina un punto materiale che si muove nel tempo $t$ partendo da $P_0$ e spostandosi alla velocità del vettore $v$. L'insieme di tutte le posizioni raggiunte è la retta.
$$ P(t) = P_0 + t \cdot v \quad \forall t \in \mathbb{R} $$
In forma esplicita di coordinate vettoriali, la retta si esprime come sistema:
$$ r: \begin{cases} x = x_0 + t \cdot v_x \\ y = y_0 + t \cdot v_y \\ z = z_0 + t \cdot v_z \end{cases} $$

### Rappresentazione Cartesiana
Nello spazio tridimensionale, non è possibile racchiudere una retta in una singola equazione (una equazione definisce un piano). Una retta cartesiana è necessariamente vista come l'**intersezione di due piani non paralleli**.
$$ r: \begin{cases} \alpha: ax + by + cz + d = 0 \\ \beta: a'x + b'y + c'z + d' = 0 \end{cases} $$

> [!tip] Trovare il Vettore Direttore da Equazioni Cartesiane
> Se una retta è data dall'intersezione di due piani con vettori normali $\mathbf{n}_\alpha = (a, b, c)^T$ e $\mathbf{n}_\beta = (a', b', c')^T$, la retta sarà perpendicolare a entrambi questi vettori. 
> Perciò, il **Vettore Direttore** $v_r$ si calcola istantaneamente usando il prodotto vettoriale:
> $$ v_r = \mathbf{n}_\alpha \wedge \mathbf{n}_\beta = \det \begin{pmatrix} \vec{i} & \vec{j} & \vec{k} \\ a & b & c \\ a' & b' & c' \end{pmatrix} $$

---

## 2. Posizioni Reciproche tra Due Rette in $\mathbb{R}^3$

Mentre nel piano euclideo le rette possono solo intersecarsi o essere parallele, nello spazio 3D si sblocca un grado di libertà aggiuntivo, creando quattro scenari geometrici distinti.

1. **Rette Incidenti:**
   - Hanno direzioni diverse (vettori direttori non proporzionali).
   - Condividono **esattamente un punto** di intersezione.
   - Poiché si incrociano, identificano sempre un unico piano che le contiene entrambe.
2. **Rette Parallele Coincidenti:**
   - I vettori direttori sono proporzionali ($v_r = k \cdot v_s$).
   - Condividono *tutti* i punti. (Se prendi un punto di $r$, noterai che soddisfa le equazioni di $s$).
3. **Rette Parallele Distinte:**
   - I vettori direttori sono proporzionali.
   - Non condividono *nessun* punto. La loro distanza è strettamente maggiore di zero. Identificano un unico piano che le contiene.
4. **Rette Sghembe:**
   - È il caso che sconvolge l'intuizione bidimensionale.
   - Hanno vettori direttori *non* proporzionali, eppure **non si intersecano mai**. 
   - È letteralmente impossibile trovare un piano nello spazio che le contenga entrambe. Sono "su due binari di altitudini diverse".

> [!abstract] Heuristic d'Esame: Rette Complanari
> Rette incidenti e rette parallele (sia coincidenti che distinte) godono della proprietà di poter essere "schiacciate" su un singolo foglio: sono **Rette Complanari**. Le rette sghembe sono le uniche che sfuggono a un singolo piano e sono definite **Non Complanari**.

---
### Scenario A: Rette Parallele Coincidenti
Le due rette occupano lo stesso identico spazio geometrico, sovrapponendosi in ogni punto.

* **Condizione sui Vettori:** I vettori direttori sono proporzionali (linearmente dipendenti).
  $$\vec{v}_r = k \cdot \vec{v}_s$$
* **Condizione sui Punti:** Condividono tutti i punti dello spazio. 
* **Algoritmo di Verifica:** 1. Estrai un punto qualsiasi $P_s$ dalla retta $s$.
  2. Sostituisci le sue coordinate nelle equazioni cartesiane di $r$.
  3. Se il sistema è soddisfatto, le rette coincidono.
---
### Scenario B: Rette Parallele Distinte
Le rette corrono nella stessa direzione senza mai incontrarsi. La loro distanza minima è strettamente maggiore di zero.

* **Condizione sui Vettori:** I vettori direttori sono proporzionali (linearmente dipendenti).
  $$\vec{v}_r = k \cdot \vec{v}_s$$
* **Condizione sui Punti:** Non condividono alcun punto di intersezione.
* **Geometria Associata:** Identificano **un unico piano complanare $\alpha$** che le contiene entrambe.
* **Algoritmo di Verifica:**
  1. Verificato il parallelismo dei vettori, estrai un punto $P_s$ da $s$.
  2. Sostituisci $P_s$ nelle cartesiane di $r$. Se non è soddisfatto, le rette sono distinte.
  3. Per trovare il piano comune $\alpha$, calcola il vettore congiungente $\overrightarrow{P_rP_s}$ e imposta il determinante $3 \times 3$ usando il **prodotto misto** (complanarietà):
     $$\det \begin{pmatrix} X - P_s \\ \vec{v}_{\text{comune}} \\ \overrightarrow{P_rP_s} \end{pmatrix} = 0$$
---
### Scenario C: Rette Incidenti
Le rette giacciono sullo stesso piano e si incrociano in un unico punto geometrico.

* **Condizione sui Vettori:** I vettori direttori **non** sono proporzionali.
  $$\vec{v}_r \neq k \cdot \vec{v}_s$$
* **Condizione sui Punti:** Condividono esattamente un punto di intersezione $P$.
* **Geometria Associata:** Identificano sempre un unico piano che le contiene entrambe.
* **Algoritmo di Verifica:**
  1. Metti a sistema le equazioni delle due rette (utilizzando la riduzione di **Gauss-Jordan** sulla matrice completa).
  2. Se il sistema ammette un'unica soluzione compatibile, il sistema restituisce le coordinate del punto di intersezione $P(x,y,z)$.
---
### Scenario D: Rette Sghembe
Questo scenario rompe completamente l'intuizione bidimensionale del piano: le rette non sono parallele, eppure non si intersecano mai poiché viaggiano a quote o altitudini differenti.

* **Condizione sui Vettori:** I vettori direttori **non** sono proporzionali.
  $$\vec{v}_r \neq k \cdot \vec{v}_s$$
* **Condizione sui Punti:** Non hanno alcun punto in comune. Il sistema lineare associato risulta *incompatibile* (impossibile).
* **Geometria Associata:** **Non esiste alcun piano** in grado di contenerle entrambe contemporaneamente.
* **Algoritmo di Verifica:**
  1. Costruisci la matrice unendo i vettori direttori $\vec{v}_r, \vec{v}_s$ e il vettore che unisce due punti qualsiasi delle rette $\overrightarrow{P_rP_s}$.
  2. Calcola il determinante della matrice $3 \times 3$.
  3. Se il determinante è **diverso da zero** ($\det \neq 0$), i tre vettori non sono complanari. Di conseguenza, le rette sono ufficialmente sghembe.


### 2.1 Il Dubbio Cruciale: Determinante VS Prodotto Scalare
Perché per trovare il piano $\beta$ (perpendicolare a $r$) non posso mettere in colonna $(X-P)$, $\vec{v}_1$ e $\vec{v}_2$ dentro un determinante?

La risposta sta nella differenza drastica tra il concetto geometrico di **complanarietà** e quello di **ortogonalità**. Ognuno di questi due concetti richiede un operatore matematico specifico.

#### 1. Il Determinante $3 \times 3$ (Costruisce Parallelismo)
Quando inserisci in matrice il vettore generico $X-P$ e due vettori direttori $\vec{v}_1, \vec{v}_2$, stai imponendo un **prodotto misto nullo**. 

$$\det \begin{pmatrix} x - x_0 & y - y_0 & z - z_0 \\ v_{1x} & v_{1y} & v_{1z} \\ v_{2x} & v_{2y} & v_{2z} \end{pmatrix} = 0$$

* **Cosa dice alla matematica:** *"Trova quel piano che contiene il punto $P$ e si sviluppa **parallelamente** alle direzioni di $\vec{v}_1$ e $\vec{v}_2$ (i vettori scorrono SUL piano)."*
* **Perché qui fallisce:** Il testo ti chiede un piano **perpendicolare** alla retta $r$, non parallelo. Se usassi il vettore direttore di $r$ dentro il determinante, costringeresti il piano a sdraiarsi in parallelo alla retta, ottenendo l'esatto contrario di ciò che ti è stato chiesto. Inoltre, ti mancherebbe una seconda direzione coerente per completare la terza riga della matrice.



#### 2. Il Prodotto Scalare (Costruisce Perpendicolarità)
Quando il testo usa la parola chiave **PERPENDICOLARE** (o ortogonale), l'attrezzo corretto è il prodotto scalare posto uguale a zero ($\vec{u} \cdot \vec{v} = 0$). Non serve un determinante perché non stai cercando direzioni che scorrono *sul* piano, ma stai usando l'unico vettore normale $\vec{n}$ che lo trafigge a $90^\circ$.

$$\vec{n} \cdot \overrightarrow{PX} = 0 \implies a(x-x_0) + b(y-y_0) + c(z-z_0) = 0$$

* **Cosa dice alla matematica:** *"Prendi il punto fisso $P$, e fai in modo che qualsiasi punto mobile $X(x,y,z)$ nello spazio formi un vettore $\overrightarrow{PX}$ che sia a $90^\circ$ rispetto al palo verticale $\vec{n}$."*
* **Il vantaggio algebrico:** Non devi inventarti vettori di supporto o fare calcoli complessi con matrici. Ti basta un solo punto e un solo vettore.

---

>[!SUCCESS] 💡 Regola Mnemonica per lo Scritto
>* **Testo chiede PARALLELO / COMPLANARE:** Ti servono frecce che scorrono *lungo* il piano $\implies$ Usi il **DETERMINANTE**.
>* **Testo chiede PERPENDICOLARE / ORTOGONALE:** Ti serve una freccia che *trafigge* il piano $\implies$ Usi il **PRODOTTO SCALARE**.


## 3. Algoritmi di Passaggio

### Da Cartesiane a Parametriche (Risoluzione Sistema)
L'approccio più rapido è scegliere una delle tre variabili (solitamente $z$) come variabile libera, imporla pari a $t$ ($z = t$), e risolvere il sistema lineare derivante dai due piani ricavando $x(t)$ e $y(t)$ per sostituzione.

### Da Parametriche a Cartesiane (Teorema degli Orlati)
Se si ha una retta in forma parametrica e si vogliono le equazioni dei due piani che la generano, la via più rigorosa (e spesso richiesta all'esame) usa le matrici. 
Si imposta una matrice contenente la differenza delle coordinate generiche dal punto di passaggio, affiancata al vettore direttore. Affinché il punto $(x,y,z)$ appartenga alla retta, le due colonne devono essere linearmente dipendenti, quindi il rango di questa matrice $3 \times 2$ deve essere esattamente 1.
Imponendo che tutti i determinanti dei minori di ordine 2 siano nulli (per il **Teorema degli Orlati** o di Kronecker), si ottengono direttamente le equazioni cartesiane (ne bastano 2 non proporzionali):
$$ \text{rango} \begin{pmatrix} x - x_0 & v_x \\ y - y_0 & v_y \\ z - z_0 & v_z \end{pmatrix} = 1 \implies \begin{cases} \det \begin{pmatrix} x - x_0 & v_x \\ y - y_0 & v_y \end{pmatrix} = 0 \\ \det \begin{pmatrix} x - x_0 & v_x \\ z - z_0 & v_z \end{pmatrix} = 0 \end{cases} $$

---

## 4. Esercizio Tipico: La Retta Perpendicolare e Incidente

Un classico problema d'esame richiede, dati una retta $r$ e un punto esterno $P$, di trovare l'unica retta $s$ che passa per $P$ e che sia contemporaneamente **incidente** e **perpendicolare** a $r$.
L'algoritmo infallibile in 3 step è il seguente:
1. **Costruzione del piano ausiliario $\alpha$**: Scrivi l'equazione del piano passante per $P$ e *perpendicolare* a $r$. (Il vettore direttore $v_r$ della retta diventerà direttamente il vettore normale $\mathbf{n}_\alpha$ del piano).
2. **Intersezione (Il punto base $Q$)**: Trova il punto esatto $Q$ di intersezione tra la retta originaria $r$ e il piano ausiliario $\alpha$ appena creato, mettendo a sistema le loro equazioni.
3. **Costruzione della retta finale**: La retta $s$ cercata è semplicemente la retta che passa per i due punti $P$ e $Q$. Il suo vettore direttore sarà banalmente la differenza di coordinate $\vec{PQ}$.

---

## 5. Esercizi Propedeutici Svolti

> [!example]- Esercizio 1: Retta per due punti (Parametrica e Cartesiana)
> **Testo:** Trovare le equazioni parametriche e cartesiane della retta passante per i punti $A=(1, 0, -1)$ e $B=(2, 2, 3)$.
> 
> **Soluzione:**
> 1. Troviamo il vettore direttore $v = \vec{AB} = B - A$:
>    $$ v = (2-1, 2-0, 3-(-1))^T = (1, 2, 4)^T $$
> 2. Scriviamo le equazioni parametriche scegliendo $A$ come punto di passaggio:
>    $$ r: \begin{cases} x = 1 + t \\ y = 0 + 2t \\ z = -1 + 4t \end{cases} $$
> 3. Per trovare la forma cartesiana ricaviamo il parametro $t$ dalla prima ($t = x - 1$) e lo sostituiamo nelle altre due:
>    $$ \begin{cases} y = 2(x - 1) \\ z = -1 + 4(x - 1) \end{cases} \implies \begin{cases} 2x - y - 2 = 0 \\ 4x - z - 5 = 0 \end{cases} $$

> [!example]- Esercizio 2: Intersezione di due rette
> **Testo:** Date le rette $r: \begin{cases} x = t \\ y = 1 + t \\ z = 2 - t \end{cases}$ e $s: \begin{cases} x = 1 + 2s \\ y = 2 + s \\ z = 1 + s \end{cases}$, stabilire se sono incidenti e, in caso affermativo, trovare il punto di intersezione.
> 
> **Soluzione:**
> Uguagliamo le coordinate per vedere se esiste una coppia $(t, s)$ che dà lo stesso punto.
> 1. Impostiamo il sistema tra le componenti omonime:
>    $$ \begin{cases} t = 1 + 2s \\ 1 + t = 2 + s \\ 2 - t = 1 + s \end{cases} $$
> 2. Sostituiamo $t$ dalla prima nella seconda:
>    $$ 1 + (1 + 2s) = 2 + s \implies 2 + 2s = 2 + s \implies s = 0 $$
> 3. Se $s=0$, allora $t = 1 + 2(0) = 1$.
> 4. Verifichiamo la terza equazione con $t=1, s=0$:
>    $$ 2 - 1 = 1 + 0 \implies 1 = 1 \quad \text{(Verificato!)} $$
> Essendo il sistema compatibile, le rette sono incidenti. 
> Sostituendo $t=1$ nelle equazioni di $r$ (o $s=0$ in $s$), otteniamo il punto d'intersezione $P$:
> $$ P = (1, 1+1, 2-1) = (1, 2, 1) $$

---
## Collegamenti
* **Back:** [[00_Geometria_MOC|MOC Geometria]]
* **Previous:** [[Prodotto Vettoriale]]
* **Next:** [[Piani nello Spazio]]
