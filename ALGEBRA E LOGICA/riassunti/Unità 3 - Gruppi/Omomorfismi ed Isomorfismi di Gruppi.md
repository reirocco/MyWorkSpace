---
tags:
  - omomorfismi
  - isomorfismi
  - nucleo
  - algebra
type: atomic
unit: 3
---

# Omomorfismi ed Isomorfismi di Gruppi

Quando studiamo strutture algebriche diverse, vogliamo capire se si comportano "allo stesso modo" pur avendo "vestiti" diversi (es. addizione in $\mathbb{R}$ vs moltiplicazione in $\mathbb{R}^+$). Le funzioni che traducono il linguaggio di un gruppo nel linguaggio di un altro sono dette **Omomorfismi**.

## Omomorfismo di Gruppi

Siano $(G, \ast)$ e $(H, \circ)$ due gruppi (nota: le operazioni possono essere diverse!).
Una funzione $f: G \rightarrow H$ si dice **Omomorfismo** se "rispetta la struttura", cioè se l'immagine della composizione è uguale alla composizione delle immagini:
> **$\forall a, b \in G, \quad f(a \ast b) = f(a) \circ f(b)$**

### Proprietà Fondamentali (che "scendono" gratis)
Se $f$ è un omomorfismo:
1. $f(e_G) = e_H$ (Manda il neutro nel neutro)
2. $f(a^{-1}) = [f(a)]^{-1}$ (Manda gli inversi negli inversi)

---

## Nucleo (Kernel) e Immagine

I due indicatori fondamentali per analizzare un omomorfismo sono:

- **Immagine ($\text{Im} f$):** L'insieme di tutti gli elementi "colpiti" in $H$.
  $$\text{Im} f = \{ h \in H \mid \exists g \in G, f(g) = h \}$$
  $\text{Im} f$ è sempre un *sottogruppo di $H$*. Se $\text{Im} f = H$, la funzione è *suriettiva* (Epimorfismo).

- **Nucleo ($\text{Ker} f$):** L'insieme di tutti gli elementi di $G$ che vengono "schiacciati" sull'elemento neutro di $H$.
  $$\text{Ker} f = \{ g \in G \mid f(g) = e_H \}$$
  $\text{Ker} f$ è sempre un *sottogruppo normale di $G$*.

> [!IMPORTANT] Il Teorema del Nucleo
> Un omomorfismo $f$ è **iniettivo (Monomorfismo)** se e solo se il suo nucleo è banale, ovvero:
> **$\text{Ker} f = \{ e_G \}$**
> (Cioè, solo il neutro di $G$ va a finire nel neutro di $H$. Nessun altro elemento vi "schianta" sopra).

---

## Isomorfismi (Cloni Matematici)

Un **Isomorfismo** è un omomorfismo che è **biettivo** (sia iniettivo che suriettivo).
Se esiste un isomorfismo tra due gruppi $G$ e $H$, si dice che sono isomorfi ($G \cong H$).

> [!NOTE] Cosa significa essere isomorfi?
> Significa che $G$ e $H$ sono, da un punto di vista algebrico astratto, **esattamente lo stesso gruppo**, solo con i nomi degli elementi cambiati. Hanno la stessa tabella di Cayley, lo stesso reticolo dei sottogruppi, gli elementi hanno gli stessi ordini.
> *Esempio:* La funzione esponenziale $f(x) = e^x$ è un isomorfismo tra $(\mathbb{R}, +)$ e $(\mathbb{R}^+, \cdot)$. Infatti $e^{x+y} = e^x \cdot e^y$. Trasforma la somma in prodotto perfettamente!

---

## Tip d'Esame

> [!TIP] Come dimostrare che NON sono isomorfi
> Dimostrare che due gruppi sono isomorfi richiede trovare la funzione biettiva. Ma per dimostrare che NON lo sono, basta trovare una proprietà "strutturale" divergente (Invarianti Algebrici). Cose da controllare (se una fallisce, non sono isomorfi):
> 1. Cardinalità: $|G| \neq |H|$? Non isomorfi.
> 2. Commutatività: Uno è abeliano e l'altro no? Non isomorfi.
> 3. Generatori: Uno è ciclico e l'altro no? Non isomorfi.
> 4. **Ordini degli elementi:** Conta quanti elementi di ordine 2 (o 3, etc.) ci sono. Se $G$ ha un elemento di ordine 4 e $H$ ne ha zero, allora non possono essere isomorfi! (Esempio classico: $\mathbb{Z}_4$ vs $V_4$ di Klein).

---

## Note Correlate
- [[03.0 - MoC Teoria dei Gruppi|Unità 3 MoC]]
- [[Definizione di Gruppo ed Esempi Fondamentali]]
- [[Teorema Fondamentale di Omomorfismo per Gruppi]]
