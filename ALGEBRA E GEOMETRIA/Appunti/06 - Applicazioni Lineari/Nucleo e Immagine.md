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

# Nucleo e Immagine

Ogni applicazione lineare $T: V \to W$ possiede due sottospazi intrinseci fondamentali: il Nucleo (nel dominio) e l'Immagine (nel codominio).

## 1. Nucleo (Ker)
Il **Nucleo** (o Kernel) di $T$ è l'insieme di tutti i vettori del dominio che vengono "schiacciati" nello zero del codominio:
$$ \ker(T) = \{ v \in V : T(v) = \mathbf{0}_W \} $$
- $\ker(T)$ è sempre un **sottospazio vettoriale** di $V$.

> [!abstract] Teorema sull'Iniettività
> Un'applicazione lineare $T$ è **iniettiva se e solo se** il suo nucleo è banale:
> $$ T \text{ è iniettiva} \iff \ker(T) = \{ \mathbf{0}_V \} $$
> *(Dimostrazione: Se $\ker(T) = \{0\}$ e $T(v_1) = T(v_2)$, allora $T(v_1 - v_2) = \mathbf{0} \implies v_1 - v_2 = \mathbf{0} \implies v_1 = v_2$)*.

## 2. Immagine (Im)
L'**Immagine** di $T$ è l'insieme di tutti i vettori di $W$ che sono raggiungibili da almeno un vettore di $V$:
$$ \text{Im}(T) = \{ T(v) \in W : v \in V \} $$
- $\text{Im}(T)$ è sempre un **sottospazio vettoriale** di $W$.
- Se $(v_1, \dots, v_n)$ è una base di $V$, allora i vettori trasformati *generano* l'immagine:
  $$ \text{Im}(T) = \text{Span}(T(v_1), \dots, T(v_n)) $$

> [!abstract] Suriettività
> Un'applicazione lineare $T$ è **suriettiva se e solo se** la sua immagine ricopre tutto il codominio:
> $$ T \text{ è suriettiva} \iff \text{Im}(T) = W $$

## Collegamenti
- Back: [[00_Applicazioni_Lineari_MOC|MOC Applicazioni Lineari]]
- Previous: [[Definizione di Applicazione Lineare]]
- Next: [[Teorema di Nullità più Rango]]
