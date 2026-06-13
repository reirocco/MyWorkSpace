---
tags:
  - matematica
  - algebra/applicazioni_lineari
aliases:
  - Ker
  - Im
  - Nucleo
  - Immagine
  - Iniettività
  - Suriettività
---
# Nucleo e Immagine (Ker e Im)

Ogni applicazione lineare $T: V \to W$ possiede due "ombre" strutturali che ci raccontano tutto sul suo comportamento: il **Nucleo** (che vive nello spazio di partenza $V$) e l'**Immagine** (che vive nello spazio di arrivo $W$).

---

## 1. Il Nucleo (Ker)

Il **Nucleo** (o *Kernel*, indicato con $\ker(T)$ o $\text{Ker}(T)$) è l'insieme di tutti quei vettori del dominio che l'applicazione $T$ "distrugge", ovvero che vengono mappati nel vettore nullo del codominio.

**Definizione Formale:**
$$ \ker(T) = \{ v \in V : T(v) = \mathbf{0}_W \} $$

> [!tip] Proprietà del Nucleo
> - Il vettore nullo del dominio appartiene *sempre* al nucleo: $\mathbf{0}_V \in \ker(T)$.
> - $\ker(T)$ è sempre un **[[Sottospazi Vettoriali|Sottospazio vettoriale]]** di $V$.
>   *(Dimostrazione: se $u, v \in \ker(T)$, allora $T(u+v) = T(u)+T(v) = \mathbf{0}+\mathbf{0} = \mathbf{0}$, quindi $u+v \in \ker(T)$. Idem per il prodotto per scalare).*

### Ker e Iniettività

Il Nucleo è il sensore perfetto per diagnosticare l'iniettività.

> [!abstract] Teorema sull'Iniettività
> Un'applicazione lineare $T$ è **iniettiva se e solo se** il suo nucleo è banale (contiene solo il vettore nullo).
> $$ T \text{ è iniettiva} \iff \ker(T) = \{ \mathbf{0}_V \} \iff \dim(\ker(T)) = 0 $$
> 
> **Dimostrazione:**
> - *Se è iniettiva:* Poiché $T(\mathbf{0}_V) = \mathbf{0}_W$, se esistesse un $v \neq \mathbf{0}_V$ tale che $T(v) = \mathbf{0}_W$, avremmo due elementi distinti con la stessa immagine. Assurdo. Quindi l'unico elemento in $\ker$ è $\mathbf{0}_V$.
> - *Se il nucleo è banale:* Supponiamo $T(v_1) = T(v_2)$. Sfruttando la linearità: $T(v_1) - T(v_2) = \mathbf{0} \implies T(v_1 - v_2) = \mathbf{0}$. Questo significa che il vettore $(v_1 - v_2)$ appartiene al nucleo. Ma se il nucleo contiene solo lo zero, deve essere $v_1 - v_2 = \mathbf{0} \implies v_1 = v_2$. Dimostrando l'iniettività.

---

## 2. L'Immagine (Im)

L'**Immagine** (indicata con $\text{Im}(T)$) è l'insieme di tutti i "bersagli colpiti" nel codominio. Costituisce lo spazio dei valori effettivamente raggiungibili dall'applicazione.

**Definizione Formale:**
$$ \text{Im}(T) = \{ w \in W : \exists v \in V, T(v) = w \} = \{ T(v) : v \in V \} $$

> [!tip] Proprietà dell'Immagine
> - Anche $\text{Im}(T)$ è sempre un **sottospazio vettoriale** (questa volta di $W$).
> - **Generazione dell'Immagine:** Se $\mathcal{B} = \{v_1, \dots, v_n\}$ è una base (o un qualsiasi insieme di generatori) per $V$, allora le loro immagini generano lo spazio $\text{Im}(T)$:
>   $$ \text{Im}(T) = \text{Span}(T(v_1), T(v_2), \dots, T(v_n)) $$
>   Questo è cruciale per calcolarla operativamente!

### Immagine e Suriettività

L'immagine misura la capacità di $T$ di ricoprire lo spazio di arrivo.

> [!abstract] Teorema sulla Suriettività
> Un'applicazione lineare $T: V \to W$ è **suriettiva se e solo se** la sua immagine coincide con l'intero codominio $W$.
> $$ T \text{ è suriettiva} \iff \text{Im}(T) = W \iff \dim(\text{Im}(T)) = \dim(W) $$

---

>[!WARNING] Calcolo Pratico (Esempio d'Esame)
>Consideriamo $T: \mathbb{R}^3 \to \mathbb{R}^2$ definita da $T(x,y,z) = (x+y, y+z)$.
>
>**1. Calcolo del Nucleo:**
Dobbiamo risolvere il sistema $T(x,y,z) = (0,0)$:
$$ \begin{cases} x + y = 0 \\ y + z = 0 \end{cases} \implies \begin{cases} x = -y \\ z = -y \end{cases} $$
I vettori del nucleo sono della forma $(-y, y, -y) = y(-1, 1, -1)$. 
Una base del nucleo è $\mathcal{B}_{\ker} = \{(-1, 1, -1)\}$. Dimensione: 1.
Essendo $\dim(\ker) \neq 0$, $T$ **non è iniettiva**.
>
>**2. Calcolo dell'Immagine:**
>Valutiamo $T$ sui vettori della base canonica $e_1, e_2, e_3$ di $\mathbb{R}^3$:
>- $T(1,0,0) = (1, 0)$
>- $T(0,1,0) = (1, 1)$
>- $T(0,0,1) = (0, 1)$
>
>L'immagine è generata da: $\text{Im}(T) = \text{Span}\{(1,0), (1,1), (0,1)\}$.
>I primi due vettori $(1,0)$ e $(1,1)$ sono linearmente indipendenti e formano una base per l'immagine. 
>Dimensione: 2.
>Poiché $\dim(\text{Im}(T)) = 2 = \dim(\mathbb{R}^2)$, $T$ **è suriettiva**.

---
## Collegamenti
* **Back:** [[00_Applicazioni_Lineari_MOC|MOC Applicazioni Lineari]]
* **Previous:** [[Definizione di Applicazione Lineare]]
* **Next:** [[Teorema di Nullità più Rango]]
