---
tags:
  - matematica
  - geometria
aliases:
  - Piano
  - Vettore normale
  - Fascio di piani
---
# Piani nello Spazio

Un piano $\alpha$ nello spazio affine tridimensionale $\mathbb{R}^3$ è un sottospazio di dimensione 2. Geometricamente, per "fissare" un piano nello spazio si possono seguire due filosofie costruttive: 
1. Posizionarlo partendo da un punto e muovendosi lungo un "pavimento" costruito su due vettori direttori.
2. Ancorarlo con un "chiodo perpendicolare", fissando un punto di passaggio e un **vettore normale** a cui tutto il piano deve rimanere perpendicolare. Questa seconda via è quella prediletta per la sua eleganza algebrica.

---

## 1. Rappresentazioni Analitiche

### L'Equazione Cartesiana
L'equazione più diffusa per un piano è una singola equazione lineare in tre variabili, poiché in $\mathbb{R}^3$, vincolare un'equazione significa perdere 1 grado di libertà ($3 - 1 = 2$ dimensioni rimanenti).
$$ \alpha: ax + by + cz + d = 0 $$
Il segreto geometrico più prezioso dell'equazione cartesiana è che i coefficienti delle variabili formano istantaneamente il **Vettore Normale** del piano, ovvero la freccia che punta perpendicolarmente alla sua superficie:
$$ \mathbf{n}_\alpha = \begin{pmatrix} a \\ b \\ c \end{pmatrix} $$

### L'Equazione Parametrica
Descrive la superficie come un tessuto intrecciato da due fili (i due vettori direttori linearmente indipendenti $v$ e $w$), partendo dal punto $P_0$:
$$ \alpha: \begin{cases} x = x_0 + t \cdot v_x + s \cdot w_x \\ y = y_0 + t \cdot v_y + s \cdot w_y \\ z = z_0 + t \cdot v_z + s \cdot w_z \end{cases} \quad \forall t,s \in \mathbb{R} $$

> [!tip] Teorema del Passaggio Rapido
> Se hai le equazioni parametriche di un piano con direzioni $v$ e $w$, il suo vettore normale si calcola al volo come il prodotto vettoriale delle due direzioni!
> $$ \mathbf{n}_\alpha = v \wedge w $$
> Trovato $\mathbf{n}_\alpha = (a, b, c)^T$, scrivi $ax+by+cz+d=0$ e sostituisci il punto $P_0$ per scoprire il valore del termine noto $d$.

---

## 2. Posizioni Reciproche Nello Spazio

I vettori normali sono i "portavoce" dei piani. Tutta l'analisi delle intersezioni si riduce allo studio dei loro normali.

* **Piani Paralleli:** Due piani sono paralleli se i loro normali sono proporzionali. Hanno equazioni cartesiane in cui le costanti $(a,b,c)$ sono identiche (o multiple), e differiscono solo nel termine noto $d$.
* **Piani Ortogonali:** Due piani sono a $90^\circ$ se i loro vettori normali sono ortogonali ($\langle \mathbf{n}_\alpha, \mathbf{n}_\beta \rangle = 0$).

### Posizione Retta-Piano
Sia $\alpha$ un piano di normale $\mathbf{n}_\alpha$ e $r$ una retta con vettore direttore $v_r$.
* **Retta Parallela al Piano:** La retta non interseca il piano. Ciò accade se "scorre" ortogonalmente al "chiodo" del piano, ovvero: $\langle v_r, \mathbf{n}_\alpha \rangle = 0$.
* **Retta Ortogonale al Piano:** La retta "buca a piombo" la superficie. Succede se la sua direzione è esattamente parallela al vettore normale, ovvero $v_r = k \cdot \mathbf{n}_\alpha$.

---

## 3. Fasci di Piani (Arma Fine di Mondo per gli Esami)

Uno dei problemi più classici è: *"Trova l'equazione del piano che passa per una retta $r$ e per un punto esterno $Q$."*
Invece di costruire parametriche lunghe e soggette a errori, si usa il **Fascio di Piani**.

Se la retta $r$ è definita in forma cartesiana come intersezione di due piani:
$$ r: \begin{cases} \alpha: P_1(x,y,z) = 0 \\ \beta: P_2(x,y,z) = 0 \end{cases} $$
L'insieme di **tutti gli infiniti piani** che ruotano attorno alla retta $r$ (l'asse del fascio) ha un'equazione cartesiana data dalla pura combinazione lineare dei due piani originali:
$$ \lambda \cdot P_1(x,y,z) + \mu \cdot P_2(x,y,z) = 0 $$
All'atto pratico, ponendo $\lambda = 1$ e $\mu = k$, l'equazione diventa formidabilmente:
$$ P_1(x,y,z) + k \cdot P_2(x,y,z) = 0 $$
Per trovare il piano esatto passante per il punto $Q(x_q, y_q, z_q)$, si sostituiscono semplicemente le coordinate di $Q$ nelle variabili $x, y, z$. Questo restituirà una semplice equazione in cui l'unica incognita è $k$. Risolto $k$ e sostituito indietro, otterrai l'equazione del piano perfetto in un istante.

---

## 4. Esercizi Propedeutici Svolti

> [!example]- Esercizio 1: Equazione del piano noto normale e punto
> **Testo:** Trovare l'equazione cartesiana del piano $\alpha$ passante per il punto $P=(1, -2, 3)$ e perpendicolare al vettore $\mathbf{n} = (2, 1, -1)^T$.
> 
> **Soluzione:**
> 1. Sapendo che i coefficienti $a, b, c$ dell'equazione cartesiana corrispondono alle componenti del vettore normale, impostiamo l'equazione:
>    $$ \alpha: 2x + 1y - 1z + d = 0 $$
> 2. Imponiamo il passaggio per il punto $P=(1, -2, 3)$ sostituendone le coordinate per trovare $d$:
>    $$ 2(1) + 1(-2) - 1(3) + d = 0 \implies 2 - 2 - 3 + d = 0 \implies d = 3 $$
> 3. L'equazione finale è:
>    $$ \alpha: 2x + y - z + 3 = 0 $$

> [!example]- Esercizio 2: Uso del Fascio di Piani
> **Testo:** Trovare l'equazione del piano passante per l'asse $z$ e per il punto $Q=(1, 2, 1)$.
> 
> **Soluzione:**
> 1. L'asse $z$ è dato dall'intersezione dei piani $x=0$ e $y=0$. Le equazioni cartesiane della retta $r$ sono:
>    $$ r: \begin{cases} x = 0 \\ y = 0 \end{cases} $$
> 2. Costruiamo l'equazione del fascio di piani che ha per asse $r$:
>    $$ x + k \cdot y = 0 $$
> 3. Imponiamo il passaggio per $Q=(1, 2, 1)$ sostituendo le sue coordinate $x=1, y=2$:
>    $$ 1 + k \cdot 2 = 0 \implies 2k = -1 \implies k = -\frac{1}{2} $$
> 4. Sostituiamo $k$ nel fascio:
>    $$ x - \frac{1}{2}y = 0 $$
>    Moltiplicando per 2 per eliminare la frazione, l'equazione finale del piano cercato è:
>    $$ 2x - y = 0 $$

---
## Collegamenti
* **Back:** [[00_Geometria_MOC|MOC Geometria]]
* **Previous:** [[Rette nello Spazio]]
* **Next:** [[Circonferenze e Sfere]]
