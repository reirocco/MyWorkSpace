---
tags:
  - classi-laterali
  - cosets
  - teorema-lagrange
  - algebra
type: atomic
unit: 3
---

# Classi Laterali e Teorema di Lagrange

Quando si ha un sottogruppo $H \le G$, è possibile usarlo come un "timbro" per ricoprire l'intero gruppo $G$. Questa traslazione del sottogruppo genera le **Classi Laterali**.

## Le Classi Laterali (Cosets)

Dato un sottogruppo $H$ del gruppo $G$, per ogni elemento $g \in G$ si definiscono:
- **Classe Laterale Sinistra:** $gH = \{ gh \mid h \in H \}$
- **Classe Laterale Destra:** $Hg = \{ hg \mid h \in H \}$

Se il gruppo $G$ è abeliano (o se il sottogruppo $H$ è normale, vedi note successive), le classi sinistre e destre coincidono ($gH = Hg$).
*L'elemento $g$ è detto rappresentante della classe.*

> [!NOTE] Proprietà Fondamentali
> 1. $g$ appartiene sempre alla sua classe $gH$ (poiché $e \in H \implies g \cdot e = g \in gH$).
> 2. Due classi laterali (entrambe sinistre o destre) o sono **identiche** o sono **completamente disgiunte**. Non si incrociano mai a metà.
> 3. Tutte le classi laterali di $H$ hanno la **stessa cardinalità** di $H$. (Hanno tutte lo stesso numero di elementi).
> Pertanto, le classi laterali formano una **Partizione** del gruppo $G$!

---

## Il Teorema di Lagrange

Il Teorema di Lagrange è forse il teorema più importante sui gruppi finiti. Si basa sull'idea che, poiché le classi laterali partizionano $G$ in "fette" tutte uguali e larghe $|H|$, allora il numero totale di elementi di $G$ deve essere un multiplo del numero di elementi di $H$.

> [!IMPORTANT] Enunciato del Teorema
> Se $G$ è un gruppo finito e $H$ è un suo sottogruppo ($H \le G$), allora **l'ordine di $H$ (la sua cardinalità) deve dividere l'ordine di $G$.**
> $$|H| \mid |G|$$
> (Cioè il resto della divisione $|G| / |H|$ è $0$).

Il numero di classi laterali distinte (cioè quante "fette" ci sono) si chiama **Indice del Sottogruppo** e si indica con $[G : H]$.
Dal teorema segue la formula: **$|G| = [G : H] \cdot |H|$**

### Corollari Potentissimi
Dal Teorema di Lagrange derivano conseguenze enormi che semplificano la vita negli esercizi:
1. **L'ordine di ogni elemento $g \in G$ divide l'ordine di $G$.** (Perché l'ordine di $g$ genera un sottogruppo ciclico).
2. Di conseguenza, elevando qualsiasi elemento all'ordine del gruppo, si ottiene l'identità: **$g^{|G|} = e$** $\forall g \in G$.
3. **Se un gruppo ha ordine primo (es. 7, 11), allora è obbligatoriamente Ciclico.** (Non potendo avere sottogruppi propri, l'ordine di ogni elemento non nullo deve essere $p$, generando l'intero gruppo).

---

## Tip d'Esame

> [!TIP] Come usare Lagrange al Contrario (per escludere i sottogruppi)
> Il Teorema di Lagrange è una condizione *necessaria, ma non sufficiente* (eccezion fatta per i gruppi ciclici). Se l'ordine non divide, il sottogruppo **non può esistere**.
> *Esempio tipico da orale:* "Esiste un sottogruppo di ordine 5 nel gruppo alterno $A_4$?"
> L'ordine di $A_4$ è $4! / 2 = 12$. Poiché $5$ non divide $12$, Lagrange ci dice immediatamente: NO, impossibile. Risposta chiusa in due secondi senza fare calcoli!

---

## Note Correlate
- [[03.0 - MoC Teoria dei Gruppi|Unità 3 MoC]]
- [[Sottogruppi e Criterio dei Sottogruppi]]
- [[Insieme Quoziente e Partizioni]]
