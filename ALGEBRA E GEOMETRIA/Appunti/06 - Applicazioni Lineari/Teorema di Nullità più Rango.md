---
tags:
  - matematica
  - algebra/applicazioni_lineari
aliases:
  - Nullità + Rango
  - Dimensioni
  - Teorema della Dimensione
---
# Teorema di Nullità più Rango (Teorema della Dimensione)

Il Teorema di Nullità più Rango (noto anche come *Teorema della Dimensione*) è l'equazione di bilancio fondamentale dell'Algebra Lineare. Stabilisce un legame quantitativo inossidabile tra il nucleo e l'immagine di un'applicazione lineare.

---

## 1. Il Teorema Nullità + Rango

> [!abstract] Enunciato
> Sia $T: V \to W$ un'applicazione lineare, con $V$ spazio vettoriale di dimensione **finita**. Allora la somma della dimensione del nucleo e della dimensione dell'immagine è sempre uguale alla dimensione dello spazio vettoriale di partenza $V$.
> $$ \dim(\ker(T)) + \dim(\text{Im}(T)) = \dim(V) $$

**Terminologia Storica:**
- La dimensione del nucleo, $\dim(\ker(T))$, è chiamata **Nullità** dell'applicazione.
- La dimensione dell'immagine, $\dim(\text{Im}(T))$, è chiamata **Rango** dell'applicazione (questo corrisponde al rango della matrice associata).

>[!TIP]-  Il Significato Profondo (Metafora del "Budget")
La dimensione del dominio, $\dim(V)$, può essere vista come la quantità totale di "informazione" disponibile. Quando passiamo questa informazione attraverso la trasformazione $T$, il budget viene speso esattamente in due modi mutuamente esclusivi:
>1. Una parte viene **schiacciata** (mappata in zero) e scompare. Questo "scarto" è misurato dalla Nullità.
>2. La parte rimanente **sopravvive** al viaggio e va a formare la struttura dell'immagine in arrivo. Questa parte preservata è misurata dal Rango.
>Nessuna dimensione si crea e nessuna si distrugge "per magia": la loro somma deve restituire il budget iniziale.

---

## 2. Conseguenze Logiche (Heuristics d'Esame)

Le implicazioni di questa semplice formula sono potentissime per risolvere test o esercizi teorici a occhio. Siano $n = \dim(V)$ (partenza) e $m = \dim(W)$ (arrivo).

1. **Se Partenza > Arrivo ($n > m$):** 
   $T$ **NON PUÒ MAI** essere **iniettiva**.
   >[!TIP]- *Dimostrazione:*
   > L'immagine è contenuta in $W$, quindi al massimo $\dim(\text{Im}) = m$. Per il teorema, $\dim(\ker) = n - \dim(\text{Im}) \ge n - m$. Poiché $n > m$, $\dim(\ker) \ge 1 > 0$. Il nucleo non è banale, l'iniettività fallisce strutturalmente.

2. **Se Partenza < Arrivo ($n < m$):**
   $T$ **NON PUÒ MAI** essere **suriettiva**.
   >[!TIP]- *Dimostrazione:*
   > La dimensione massima dell'immagine è limitata da ciò che abbiamo in partenza (cioè $n$). Quindi $\dim(\text{Im}) \le n$. Siccome $n < m$, si ha che $\dim(\text{Im}) < \dim(W)$. L'immagine non riempirà mai tutto l'arrivo.

3. **Se Partenza = Arrivo ($n = m$):** (Il caso quadrato)
   Qui accade la magia: **Iniettività $\iff$ Suriettività $\iff$ Biiettività**.
   >[!TIP]- *Dimostrazione:* 
   >- Se iniettiva $\implies \dim(\ker) = 0 \implies 0 + \dim(\text{Im}) = n$. Poiché l'arrivo è $n$, $\text{Im} = W \implies$ suriettiva.
   >- Se suriettiva $\implies \dim(\text{Im}) = n \implies \dim(\ker) + n = n \implies \dim(\ker) = 0 \implies$ iniettiva.

---

## 3. Applicazione in Esercizio Pratico

> [!question] Test:
> Esiste un'applicazione lineare *suriettiva* $T: \mathbb{R}^2 \to \mathbb{R}^4$?

**Soluzione Analitica tramite il Teorema:**
1. Dimensione Dominio $n=2$, Dimensione Codominio $m=4$.
2. Se $T$ fosse suriettiva, dovrebbe essere $\dim(\text{Im}(T)) = \dim(\mathbb{R}^4) = 4$.
3. Applichiamo Nullità+Rango:
   $$ \dim(\ker(T)) + \dim(\text{Im}(T)) = 2 $$
4. Sostituendo 4 all'immagine otteniamo:
   $$ \dim(\ker(T)) + 4 = 2 \implies \dim(\ker(T)) = -2 $$
5. È impossibile che la dimensione di uno spazio (il nucleo) sia negativa.
6. **Conclusione:** L'ipotesi iniziale è falsa. Non può esistere un'applicazione siffatta.

---
## Collegamenti
* **Back:** [[00_Applicazioni_Lineari_MOC|MOC Applicazioni Lineari]]
* **Previous:** [[Nucleo e Immagine]]
* **Next:** [[Matrice Associata]]
