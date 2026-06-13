---
tags:
  - matematica
  - geometria
aliases:
  - Punto Medio
  - Baricentro
  - Distanza punto retta
  - Distanza punto piano
  - Distanza Euclidea
---
# Punti e Distanze nello Spazio Affine

In uno spazio affine $\mathbb{R}^n$ dotato di un sistema di riferimento cartesiano ortonormale, i concetti geometrici elementari si traducono in calcoli vettoriali precisi. Un punto $P$ è completamente identificato dalle coordinate del vettore che lo congiunge con l'origine del sistema (il raggio vettore).

---

## 1. Punti Notevoli

Siano $P_1, P_2, \dots, P_k$ punti in $\mathbb{R}^n$, identificati dalle loro coordinate.

- **Punto Medio:** Il punto che divide a metà il segmento congiungente $P_1$ e $P_2$ si ottiene operando la media aritmetica componente per componente:
  $$ M = \frac{P_1 + P_2}{2} $$
- **Baricentro (Centroide):** Il baricentro di un poligono (o simplesso) con $k$ vertici generalizza l'idea del punto medio. È il punto di equilibrio geometrico della figura:
  $$ G = \frac{P_1 + P_2 + \dots + P_k}{k} $$

---

## 2. Distanza tra Due Punti

La distanza tra due punti nello spazio euclideo non è altro che la **Norma Euclidea** del vettore che li congiunge, ovvero il vettore differenza. Questo è l'applicazione diretta del Teorema di Pitagora in $n$ dimensioni.

> [!abstract] Distanza Euclidea
> Dati due punti $P_1 = (x_1, y_1, z_1)$ e $P_2 = (x_2, y_2, z_2)$ in $\mathbb{R}^3$, la loro distanza $d(P_1, P_2)$ è definita come:
> $$ d(P_1, P_2) = \|P_2 - P_1\| = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2 + (z_2-z_1)^2} $$

---

## 3. Distanza tra un Punto e un Iperpiano

Un iperpiano è un sottospazio affine di dimensione $n-1$. In $\mathbb{R}^2$ è una **retta**, in $\mathbb{R}^3$ è un **piano**. La distanza minima da un punto $P_0$ all'iperpiano si misura sempre lungo la retta ortogonale all'iperpiano passante per $P_0$.

> [!tip] Formula della Distanza Punto-Iperpiano
> Se l'iperpiano ha equazione cartesiana $\alpha: ax + by + cz + d = 0$ e il punto è $P_0(x_0, y_0, z_0)$, la distanza si calcola algebricamente valutando l'equazione del piano nel punto e dividendo per la norma del vettore normale $\mathbf{n}_\alpha = (a, b, c)^T$:
> $$ d(P_0, \alpha) = \frac{|a x_0 + b y_0 + c z_0 + d|}{\sqrt{a^2 + b^2 + c^2}} $$
> 
> *Nota: Il modulo a numeratore è fondamentale perché le distanze sono quantità strettamente non negative. Il termine all'interno del modulo indica algebricamente "da che parte" dell'iperpiano si trova il punto.*

### Approfondimento: Capire la Formula in $\mathbb{R}^3$

Esistono due modi principali per calcolare e capire questa distanza: uno prettamente geometrico-vettoriale (tramite le proiezioni) e uno analitico (la classica formula "algebrica").

#### 1. L'Iperpiano e il Punto
Definiamo i nostri elementi in $\mathbb{R}^3$:
- **Il punto P:** un punto nello spazio di coordinate $P=(x_0, y_0, z_0)$.
- **L'iperpiano $\pi$:** definito dall'equazione cartesiana $ax+by+cz+d=0$.
- **Il vettore normale $\mathbf{n}$:** I coefficienti formano il vettore $\mathbf{n} = (a, b, c)^T$. Questo vettore è perpendicolare a qualsiasi vettore che giace sul piano e dà la direzione della retta più corta (la verticale), ma non ha una posizione fissa (indica solo un'orientazione).

#### 2. L'Approccio Geometrico (L'Ombra e la Proiezione)
Immagina un punto qualsiasi $Q=(x_1, y_1, z_1)$ che giace sul piano $\pi$ (quindi $ax_1+by_1+cz_1+d=0$).
Se tracciamo un vettore che va da $Q$ al nostro punto esterno $P$, otteniamo il vettore obliquo (o "storto") $\vec{QP}$:
$$ \vec{QP} = P - Q = \begin{pmatrix} x_0 - x_1 \\ y_0 - y_1 \\ z_0 - z_1 \end{pmatrix} $$

La distanza minima tra $P$ e il piano non è la lunghezza di $\vec{QP}$, ma l'altezza del triangolo rettangolo che si forma. Immagina di posizionare una torcia e proiettare l'ombra del vettore storto $\vec{QP}$ lungo la retta verticale tracciata dal vettore normale $\mathbf{n}$.
Geometricamente, questa distanza è la **proiezione scalare** del vettore $\vec{QP}$ lungo la direzione del vettore normale $\mathbf{n}$.

Usando il prodotto scalare, la lunghezza di questa proiezione (e quindi la distanza) è:
$$ dist(P, \pi) = \frac{|\vec{QP} \cdot \mathbf{n}|}{\|\mathbf{n}\|} $$
Dove $\|\mathbf{n}\| = \sqrt{a^2+b^2+c^2}$ è la lunghezza del vettore normale.

**Perché funziona con qualsiasi punto Q?**
Se prendi un punto $Q$ molto lontano sul piano, il vettore $\vec{QP}$ sarà molto lungo, ma anche molto inclinato (l'angolo $\theta$ con la verticale aumenta).
In trigonometria, il cateto verticale è:
$$ \text{Distanza} = \|\vec{QP}\| \cdot \cos(\theta) $$
Quando $Q$ si allontana, $\|\vec{QP}\|$ aumenta, ma $\cos(\theta)$ diminuisce compensando perfettamente l'aumento di lunghezza. L'ombra sulla verticale avrà sempre la stessa altezza.
**Allora perché nella formula facciamo $\vec{QP} \cdot \mathbf{n}$ se cerchiamo una distanza?**
Il motivo è che noi geometricamente **non conosciamo il valore dell'angolo $\theta$** (né il suo coseno). Per calcolare quel numero senza conoscere l'angolo, usiamo il prodotto scalare come trucco algebrico.
La formula del prodotto scalare (che è un'operazione che sputa fuori un numero scalare, non un vettore) è:
$$ \vec{QP} \cdot \mathbf{n} = \|\vec{QP}\| \cdot \|\mathbf{n}\| \cdot \cos(\theta) $$

Se guardi bene il membro di destra, puoi riorganizzarlo così:
$$ \vec{QP} \cdot \mathbf{n} = \underbrace{\Big( \|\vec{QP}\| \cdot \cos(\theta) \Big)}_{\text{La distanza } d} \cdot \|\mathbf{n}\| $$
Quindi:
$$ \vec{QP} \cdot \mathbf{n} = d \cdot \|\mathbf{n}\| $$

Come vedi, fare il prodotto scalare $\vec{QP} \cdot \mathbf{n}$ non serve a trovare una direzione e un verso (quello lo farebbe il prodotto vettoriale o la proiezione vettoriale). Genera un numero che contiene al suo interno sia la distanza $d$ sia la lunghezza "di disturbo" del vettore normale.
Per isolare la sola distanza $d$, dobbiamo "togliere" la lunghezza di $\mathbf{n}$ che dà fastidio. Per farlo, dividiamo tutto per $\|\mathbf{n}\|$ (e usiamo il modulo per garantire un risultato positivo):
$$ d = \frac{|\vec{QP} \cdot \mathbf{n}|}{\|\mathbf{n}\|} $$

In sintesi, usiamo $\vec{QP} \cdot \mathbf{n}$ al numeratore puramente come "trucco algebrico" per far emergere il valore di $\|\vec{QP}\|\cos(\theta)$ senza doverlo calcolare esplicitamente con complessi calcoli trigonometrici tridimensionali.

#### 3. La Formula Analitica (Sviluppo Algebrico) 
Esplicitando il prodotto scalare a numeratore:
$$ \vec{QP} \cdot \mathbf{n} = a(x_0 - x_1) + b(y_0 - y_1) + c(z_0 - z_1) $$
$$ \vec{QP} \cdot \mathbf{n} = (ax_0 + by_0 + cz_0) - (ax_1 + by_1 + cz_1) $$
Poiché il punto $Q$ appartiene al piano, soddisfa l'equazione $ax_1 + by_1 + cz_1 + d = 0$, il che significa che:
$$ -(ax_1 + by_1 + cz_1) = d $$
Sostituendo questa uguaglianza (che fa "sparire" magicamente le coordinate del punto incognito $Q$), otteniamo il numeratore della formula analitica:
$$ \vec{QP} \cdot \mathbf{n} = ax_0 + by_0 + cz_0 + d $$
Mettendo tutto insieme con il denominatore e il valore assoluto per garantire una distanza positiva, arriviamo alla formula esplicita della distanza punto-piano:
$$ dist(P, \pi) = \frac{|ax_0 + by_0 + cz_0 + d|}{\sqrt{a^2 + b^2 + c^2}} $$

> [!note] Eleganza Algebrica
> Il numeratore non è altro che l'equazione del piano in cui al posto delle variabili sono state sostituite le coordinate del punto $P$. Se il punto si trova già sul piano, l'equazione si annulla e la distanza è giustamente zero.

>[!ERROR] Visualizzazione grafica
>INSERENDO LE COORDINATE DEL PUNTO P IN $\pi$ SI OTTIENE IL TERMINE NOTO DEL SOTTOSPAZIO AFFINE DOVE RISIEDE P
>Con tutti questi calcoli a livello grafico si deve pensare che noi vogliamo trovare prima il sottospazio affine al nostro piano, ovvero dobbiamo trovare il piano che contiene il punto P parallelo al nostro piano di partenza. fatto questo basta sottrarre i coefficienti per trovare la "quota" nel nostro piano passante per il punto rispetto al nostro $\pi$. 
>**Perchè dividiamo per $||n||$** ? La "Quota" fa riferimento al fatto che i vettori che compongono il piano $\pi$ non si sa se sono ortonormali, se lo fossero la norma verrebbe 1.
---

## 4. Distanze Complesse nello Spazio $\mathbb{R}^3$

Non tutte le distanze hanno formule chiuse veloci. A volte è necessario eseguire una costruzione geometrica o usare il Prodotto Vettoriale.

### Distanza Punto-Retta in $\mathbb{R}^3$
Non si può usare la formuletta precedente perché una retta in 3D ha *due* equazioni. Ci sono due strategie:
1. **Geometrica (Proiezione):** Costruisci il piano $\alpha$ perpendicolare alla retta $r$ e passante per $P_0$. Trova il punto di intersezione $H = r \cap \alpha$. La distanza cercata è la lunghezza del segmento $d(P_0, H)$.
2. **Algebrica (Prodotto Vettoriale):** Se $r$ ha vettore direttore $v$ e passa per $P_1$:
   $$ d(P_0, r) = \frac{\|(P_1-P_0) \wedge v\|}{\|v\|} $$

### Distanza tra Rette Sghembe
Due rette sono sghembe se non si intersecano e non sono parallele (non ammettono un piano che le contenga entrambe).
Per trovare la loro minima distanza:
1. Siano $r$ ed $s$ le due rette, con vettori direttori $v_r$ e $v_s$.
2. Costruisci un piano $\alpha$ che contiene $r$ e che è parallelo a $s$. (Per farlo, il suo vettore normale sarà $\mathbf{n} = v_r \wedge v_s$, e passerà per un punto di $r$).
3. Prendi un punto *qualsiasi* $P_s \in s$ e usa la formula della distanza Punto-Piano tra $P_s$ e il piano $\alpha$.

---

## 5. Esercizi Propedeutici Svolti

> [!example]- Esercizio 1: Distanza tra due punti
 **Testo:** Calcolare la distanza tra i punti $P_1 = (1, 2, -1)$ e $P_2 = (4, -2, 11)$.
>
> **Soluzione:**
> Utilizziamo la formula della distanza euclidea:
> $$ d(P_1, P_2) = \sqrt{(4 - 1)^2 + (-2 - 2)^2 + (11 - (-1))^2} $$
> $$ d(P_1, P_2) = \sqrt{(3)^2 + (-4)^2 + (12)^2} $$
> $$ d(P_1, P_2) = \sqrt{9 + 16 + 144} = \sqrt{169} = 13 $$

> [!example]- Esercizio 2: Distanza Punto-Piano
> **Testo:** Calcolare la distanza tra il punto $P = (2, -1, 3)$ e il piano $\pi: 3x - 2y + z - 4 = 0$.
> 
> **Soluzione:**
> Individuiamo prima il vettore normale del piano: $\mathbf{n} = (3, -2, 1)^T$.
> Applichiamo direttamente la formula analitica:
> $$ d(P, \pi) = \frac{|ax_0 + by_0 + cz_0 + d|}{\sqrt{a^2 + b^2 + c^2}} $$
> Sostituiamo le coordinate del punto e i coefficienti del piano:
> $$ d(P, \pi) = \frac{|3(2) - 2(-1) + 1(3) - 4|}{\sqrt{3^2 + (-2)^2 + 1^2}} $$
> $$ d(P, \pi) = \frac{|6 + 2 + 3 - 4|}{\sqrt{9 + 4 + 1}} = \frac{|7|}{\sqrt{14}} $$
> Razionalizzando il denominatore:
> $$ d(P, \pi) = \frac{7\sqrt{14}}{14} = \frac{\sqrt{14}}{2} $$

> [!example]- Esercizio 3: Distanza Punto-Retta (con prodotto vettoriale)
> **Testo:** Calcolare la distanza tra il punto $P_0 = (1, 0, 2)$ e la retta $r$ passante per $P_1 = (0, 1, 1)$ con vettore direttore $v = (1, 1, -1)^T$.
> 
> **Soluzione:**
> Utilizziamo la formula con il prodotto vettoriale: $d(P_0, r) = \frac{\|(P_1-P_0) \wedge v\|}{\|v\|}$.
> 1. Calcoliamo il vettore $(P_1 - P_0)$:
>    $$ P_1 - P_0 = (0-1, 1-0, 1-2)^T = (-1, 1, -1)^T $$
> 2. Calcoliamo il prodotto vettoriale $(P_1 - P_0) \wedge v$:
>    $$ \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ -1 & 1 & -1 \\ 1 & 1 & -1 \end{vmatrix} = \mathbf{i}(-1 - (-1)) - \mathbf{j}(1 - (-1)) + \mathbf{k}(-1 - 1) = (0, -2, -2)^T $$
> 3. Calcoliamo le norme:
>    $$ \|(P_1-P_0) \wedge v\| = \sqrt{0^2 + (-2)^2 + (-2)^2} = \sqrt{8} = 2\sqrt{2} $$
>    $$ \|v\| = \sqrt{1^2 + 1^2 + (-1)^2} = \sqrt{3} $$
> 4. Calcoliamo la distanza finale:
>    $$ d(P_0, r) = \frac{2\sqrt{2}}{\sqrt{3}} = \frac{2\sqrt{6}}{3} $$

---
## Collegamenti
* **Back:** [[00_Geometria_MOC|MOC Geometria]]
* **Next:** [[Prodotto Vettoriale]]
