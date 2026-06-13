---
tags:
  - matematica
  - geometria
aliases:
  - Ipersfera
  - Sfera
  - Circonferenza
  - Intersezione sfera piano
---
# Sfere e Circonferenze nello Spazio

Nello studio della Geometria Analitica non piana, dopo i sottospazi lineari (rette, piani), lo step successivo sono i luoghi geometrici generati da proprietà metriche. La Sfera è la forma per eccellenza: il luogo dei punti dello spazio aventi tutti uguale distanza da un punto fissato.

---

## 1. La Sfera in $\mathbb{R}^3$

Sia $C = (x_c, y_c, z_c)$ il centro di rotazione, e sia $r \ge 0$ la distanza fissa (raggio).
Per definizione, un punto $P(x,y,z)$ appartiene alla sfera $\mathcal{S}$ se e solo se $d(P, C) = r$.
Elevando al quadrato per rimuovere la radice del Teorema di Pitagora, otteniamo l'**Equazione in Forma Normale**:

$$ \mathcal{S}: (x - x_c)^2 + (y - y_c)^2 + (z - z_c)^2 = r^2 $$

Sviluppando tutti i quadrati, riordinando i monomi e accorpando i termini noti in costanti generiche, otteniamo l'**Equazione Sviluppata**:

$$ \mathcal{S}: x^2 + y^2 + z^2 + ax + by + cz + d = 0 $$

### Reverse Engineering: Dalla formula sviluppata ai dati geometrici
Molto spesso gli esercizi forniscono l'equazione già sviluppata, chiedendoti di verificare se si tratti di una sfera, ed estrarne le coordinate. 
Ricompletando i quadrati (o applicando meccanicamente le formule derivate), scopriamo che:
- **Il Centro** è banalmente metà dei coefficienti dei termini di primo grado, cambiati di segno:
  $$ C = \left( -\frac{a}{2}, -\frac{b}{2}, -\frac{c}{2} \right) $$
- **Il Raggio** emerge dal termine noto residuo:
  $$ r = \sqrt{\left(-\frac{a}{2}\right)^2 + \left(-\frac{b}{2}\right)^2 + \left(-\frac{c}{2}\right)^2 - d} $$

> [!danger] Condizione di Realtà (Trappola d'Esame)
> Un'equazione del tipo $x^2 + y^2 + z^2 \dots = 0$ NON è sempre una sfera reale. 
> Il radicando all'interno della formula del raggio **deve essere strettamente positivo**. Se è negativo, l'equazione descrive l'insieme vuoto (sfera immaginaria). Se fa zero, la sfera degenera in un singolo punto coincidente col centro.

---

## 2. Intersezione Sfera - Piano (La Circonferenza)

In due dimensioni ($\mathbb{R}^2$), la circonferenza gode di un'equazione propria e indipendente. 
In tre dimensioni ($\mathbb{R}^3$), non esiste la "singola equazione di una circonferenza". Una circonferenza (essendo un oggetto unidimensionale curvo incastonato nello spazio 3D) è geometricamente generata **solo come il taglio di una Sfera da parte di un Piano**.

La sua rappresentazione analitica è quindi obbligatoriamente un sistema vincolato:
$$ \gamma: \begin{cases} x^2 + y^2 + z^2 + ax + by + cz + d = 0 & (\text{La Sfera che fornisce la curvatura}) \\ \alpha x + \beta y + \gamma z + \delta = 0 & (\text{Il Piano che la 'affetta'}) \end{cases} $$

### Studio del Taglio (Distanza Centro-Piano)
Sia $\mathcal{S}$ una sfera di raggio $r$ e centro $C$, affettata dal piano $\pi$. 
Per capire cosa succede, si calcola la distanza tra il centro della sfera e il piano: $d = \text{dist}(C, \pi)$.

1. **Piano Esterno:** $d > r$. (Il coltello manca il frutto). L'intersezione è l'insieme vuoto.
2. **Piano Tangente:** $d = r$. L'intersezione è un punto singolo. Il vettore dal centro al punto è esattamente il vettore normale del piano!
3. **Piano Secante:** $d < r$. (Il taglio perfetto). L'intersezione è una vera e propria **circonferenza** nello spazio.

> [!abstract] Raggio e Centro della Circonferenza Sezione
> Quando il piano taglia la sfera, i dati del "disco" generato si calcolano puramente con la geometria elementare euclidea:
> 1. **Raggio $R_{\gamma}$:** Applicando Pitagora al triangolo rettangolo interno formato da $r$ (ipotenusa) e $d$ (cateto), il raggio della circonferenza è $R_{\gamma} = \sqrt{r^2 - d^2}$. Se $d=0$ (il piano passa per il centro), la circonferenza è una *circonferenza massima* e il suo raggio coincide con quello della sfera.
> 2. **Centro $C_{\gamma}$:** Il centro della nuova circonferenza non è altro che la **proiezione ortogonale** del centro della sfera $C$ sul piano $\pi$. (Per trovarlo: si crea la retta passante per $C$ perpendicolare a $\pi$, e si fa sistema con $\pi$).

---

## 3. Esercizi Propedeutici Svolti

> [!example]- Esercizio 1: Da Sviluppata a Centro e Raggio
> **Testo:** Verificare se l'equazione $x^2 + y^2 + z^2 - 2x + 4y - 6z + 5 = 0$ rappresenta una sfera reale e in tal caso determinarne centro e raggio.
> 
> **Soluzione:**
> I coefficienti sono $a=-2, b=4, c=-6, d=5$.
> 1. Calcoliamo il centro dividendo i coefficienti per $-2$:
>    $$ C = \left(-\frac{-2}{2}, -\frac{4}{2}, -\frac{-6}{2}\right) = (1, -2, 3) $$
> 2. Applichiamo la formula del raggio:
>    $$ r = \sqrt{\left(\frac{a}{2}\right)^2 + \left(\frac{b}{2}\right)^2 + \left(\frac{c}{2}\right)^2 - d} $$
>    $$ r = \sqrt{1^2 + (-2)^2 + 3^2 - 5} = \sqrt{1 + 4 + 9 - 5} = \sqrt{9} = 3 $$
> Poiché il radicando (9) è strettamente positivo, l'equazione rappresenta una sfera reale con centro $C(1, -2, 3)$ e raggio $r = 3$.

> [!example]- Esercizio 2: Raggio della Circonferenza Intersezione
> **Testo:** Data la sfera $\mathcal{S}$ di centro $C=(0, 0, 0)$ e raggio $r=5$, e il piano $\pi: 2x - y + 2z - 9 = 0$. Verificare che il piano tagli la sfera e calcolare il raggio della circonferenza di intersezione $\gamma$.
> 
> **Soluzione:**
> 1. Calcoliamo la distanza del centro della sfera dal piano:
>    $$ d(C, \pi) = \frac{|2(0) - 1(0) + 2(0) - 9|}{\sqrt{2^2 + (-1)^2 + 2^2}} = \frac{|-9|}{\sqrt{4+1+4}} = \frac{9}{\sqrt{9}} = \frac{9}{3} = 3 $$
> 2. Confrontiamo la distanza col raggio della sfera:
>    Poiché $d = 3 < r = 5$, il piano è secante e crea una circonferenza reale.
> 3. Troviamo il raggio della circonferenza $R_{\gamma}$ con Pitagora:
>    $$ R_{\gamma} = \sqrt{r^2 - d^2} = \sqrt{5^2 - 3^2} = \sqrt{25 - 9} = \sqrt{16} = 4 $$

---
## Collegamenti
* **Back:** [[00_Geometria_MOC|MOC Geometria]]
* **Previous:** [[Piani nello Spazio]]
