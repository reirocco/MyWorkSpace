---
tags:
  - teorema-omomorfismo
  - quoziente
  - isomorfismo
  - algebra
type: atomic
unit: 3
---

# Teorema Fondamentale di Omomorfismo per Gruppi

Il Teorema Fondamentale (o Primo Teorema) d'Omomorfismo chiude il cerchio tra tre concetti cruciali: Omomorfismi, Nuclei (Kernel) e Gruppi Quoziente.

## L'Enunciato del Teorema

Sia $f: G \rightarrow H$ un omomorfismo tra due gruppi.
Sappiamo che l'immagine $\text{Im}(f)$ è un sottogruppo di $H$ e il nucleo $\text{Ker}(f)$ è un sottogruppo **normale** di $G$.

Poiché $\text{Ker}(f)$ è normale, ha senso costruire il gruppo quoziente $G / \text{Ker}(f)$.

> [!IMPORTANT] Teorema di Isomorfismo
> Il Teorema afferma che il quoziente di $G$ rispetto al Nucleo è "esattamente uguale" all'Immagine. In termini formali, esiste un **Isomorfismo** naturale:
> $$ \frac{G}{\text{Ker}(f)} \cong \text{Im}(f) $$

*(Questo ci dice che, a meno di "collassare" in un unico punto tutti gli elementi che condividono lo stesso output, il comportamento di un omomorfismo è in realtà un isomorfismo mascherato!).*

---

## Corollari e Conseguenze Computazionali

Il teorema ci regala la formula per l'ordine (cardinalità):
Dal Teorema di Lagrange, sappiamo che $|G / \text{Ker}(f)| = \frac{|G|}{|\text{Ker}(f)|}$.
Quindi, per il Primo Teorema d'Omomorfismo, abbiamo:
$$|\text{Im}(f)| = \frac{|G|}{|\text{Ker}(f)|}$$
Ossia, **$|G| = |\text{Ker}(f)| \cdot |\text{Im}(f)|$**.

> [!EXAMPLE] Come usare il teorema per limitare le possibilità
> Immagina di dover studiare un omomorfismo $f: \mathbb{Z}_6 \rightarrow \mathbb{Z}_4$.
> 1. $\text{Im}(f)$ deve essere un sottogruppo di $\mathbb{Z}_4$. Quindi la sua cardinalità deve dividere 4 (può essere 1, 2, o 4).
> 2. $\text{Ker}(f)$ deve essere un sottogruppo di $\mathbb{Z}_6$.
> 3. Dal Teorema di Isomorfismo: $|\text{Im}(f)|$ deve dividere anche la cardinalità di $\mathbb{Z}_6$ (perché $|\text{Im}(f)| = 6 / |\text{Ker}|$).
> Quali numeri dividono *sia* 4 che 6? Solo 1 e 2.
> - Se $|\text{Im}(f)| = 1$, allora la funzione mappa tutto a zero (omomorfismo banale).
> - Se $|\text{Im}(f)| = 2$, allora la funzione mappa $\mathbb{Z}_6$ sul sottogruppo $\{0, 2\}$ di $\mathbb{Z}_4$. L'isomorfismo non potrà MAI essere suriettivo (perché $|\text{Im}(f)|$ non potrà mai essere 4)!

---

## Tip d'Esame

> [!TIP] La Strategia della "Dimostrazione Indiretta"
> Se in un esercizio ti viene chiesto di dimostrare che un certo quoziente bizzarro $\frac{G}{N}$ è isomorfo a un gruppo "pulito" $H$ (ad esempio $\frac{\mathbb{R}}{\mathbb{Z}} \cong S^1$), **non definire la mappa direttamente dal quoziente!**
> È un incubo mostrare che la mappa è "ben definita" sulle classi.
>
> **Usa il Teorema Fondamentale invece:**
> 1. Definisci l'omomorfismo "standard" $f: G \rightarrow H$.
> 2. Dimostra che $f$ è suriettivo (così $\text{Im}(f) = H$).
> 3. Dimostra che $\text{Ker}(f) = N$.
> 4. Cita: *"Per il Primo Teorema d'Omomorfismo, $\frac{G}{\text{Ker}(f)} \cong \text{Im}(f) \implies \frac{G}{N} \cong H$."* Fine della dimostrazione con punteggio pieno.

---

## Note Correlate
- [[03.0 - MoC Teoria dei Gruppi|Unità 3 MoC]]
- [[Omomorfismi ed Isomorfismi di Gruppi]]
- [[Sottogruppi Normali e Gruppo Quoziente]]
