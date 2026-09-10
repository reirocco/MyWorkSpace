---
tags:
  - ideali
  - anelli-quoziente
  - algebra
type: atomic
unit: 4
---

# Ideali e Anelli Quoziente

Come i sottogruppi normali servono a costruire i Gruppi Quoziente, così gli **Ideali** sono particolari "sotto-anelli" che permettono di costruire gli **Anelli Quoziente**.

## Definizione di Ideale

Un sottoinsieme $I$ di un anello $R$ è un **Ideale** di $R$ (e si scrive $I \trianglelefteq R$) se:
1. $(I, +)$ è un **sottogruppo** del gruppo additivo $(R, +)$. (Significa che se prendi due elementi in $I$, la loro differenza sta in $I$).
2. **Proprietà Assorbente:** Per ogni $x \in I$ e per ogni $r \in R$ (qualsiasi elemento dell'anello), il prodotto $r \cdot x \in I$ e $x \cdot r \in I$.

> [!NOTE] La metafora del buco nero
> La proprietà assorbente è la vera forza dell'ideale. Assomiglia a un buco nero o al concetto di "pari": se moltiplichi un numero pari ($I$) per *qualsiasi* altro numero, pari o dispari ($R$), il risultato "viene risucchiato" e rimane pari ($I$).

### Ideali Principali
Se $R$ è un anello commutativo unitario, l'ideale generato da un singolo elemento $a \in R$ è l'insieme di tutti i multipli di $a$:
$(a) = \{ r \cdot a \mid r \in R \}$.
Questo si chiama **Ideale Principale**. In $\mathbb{Z}$, **tutti** gli ideali sono principali.

---

## L'Anello Quoziente $R/I$

Poiché $(I, +)$ è un sottogruppo di $(R, +)$ (che è abeliano), $I$ è sicuramente un sottogruppo normale. Possiamo quindi creare l'insieme quoziente $R/I$ formato dalle classi laterali (che ora chiamiamo "classi di resto"):
$$R/I = \{ a + I \mid a \in R \}$$

Per far diventare questo insieme un **Anello Quoziente**, dobbiamo potervi sommare e moltiplicare le classi:
1. $(a + I) + (b + I) = (a + b) + I$
2. $(a + I) \cdot (b + I) = (a \cdot b) + I$

> [!IMPORTANT] Perché servono gli Ideali?
> La condizione 2 (moltiplicazione tra classi) è "ben definita" (cioè il risultato non cambia se scelgo rappresentanti diversi) **SE E SOLO SE** $I$ gode della proprietà assorbente (cioè è un ideale)! Un semplice sotto-anello non basta.

---

## Ideali Primi e Massimali

Due tipi speciali di ideali caratterizzano le proprietà dell'anello quoziente risultante:

- **Ideale Primo:** Se $ab \in I \implies a \in I$ oppure $b \in I$.
  *(Teorema: $R/I$ è un Dominio di Integrità $\iff$ $I$ è un Ideale Primo).*
- **Ideale Massimale:** Se non esiste alcun ideale proprio racchiuso tra $I$ ed $R$.
  *(Teorema: $R/I$ è un Campo $\iff$ $I$ è un Ideale Massimale).*
  Poiché ogni campo è un dominio, ogni ideale massimale è anche primo.

> [!EXAMPLE] Ideali in $\mathbb{Z}$
> In $\mathbb{Z}$, gli ideali sono del tipo $n\mathbb{Z}$.
> Se $n$ è un numero composto (es. 6), l'ideale $6\mathbb{Z}$ non è primo (infatti $\mathbb{Z}/6\mathbb{Z} = \mathbb{Z}_6$ non è un dominio).
> Se $n=p$ è un numero primo, $p\mathbb{Z}$ è sia primo che massimale (infatti $\mathbb{Z}/p\mathbb{Z} = \mathbb{Z}_p$ è un campo).

---

## Tip d'Esame

> [!TIP] Trovare gli Ideali in un Campo
> Domanda trabocchetto fissa: "Quali sono gli ideali del campo $\mathbb{R}$ o del campo $\mathbb{Z}_5$?".
> Ricorda il Teorema: **I campi non hanno ideali propri**. Gli unici ideali in un campo sono l'ideale banale $\{0\}$ e l'intero campo stesso. Questo perché se un ideale contiene un elemento $a \neq 0$, poiché nei campi tutto è invertibile, contiene $a^{-1} \cdot a = 1$. E se un ideale contiene l'unità 1, per la proprietà assorbente deve "risucchiare" tutto l'anello ($r \cdot 1 = r \in I$).

---

## Note Correlate
- [[04.0 - MoC Anelli e Campi|Unità 4 MoC]]
- [[Definizione di Anello e Domini di Integrità]]
- [[Definizione di Campo e Caratteristica]]
- [[Omomorfismi di Anelli]]
