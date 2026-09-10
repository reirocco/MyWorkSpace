---
tags:
  - insieme-quoziente
  - partizioni
  - relazioni
  - algebra
type: atomic
unit: 2
---

# Insieme Quoziente e Partizioni

Questa nota esplora il legame profondo e biunivoco che esiste tra le relazioni di equivalenza (viste in precedenza) e le partizioni di un insieme. È uno dei concetti astratti più potenti dell'algebra.

## Partizione di un Insieme

Una **partizione** di un insieme $A$ è una famiglia $P = \{A_1, A_2, \dots, A_k\}$ di sottoinsiemi di $A$ (detti blocchi della partizione) che soddisfa tre condizioni fondamentali:
1. **Nessun blocco è vuoto:** $A_i \neq \emptyset$ per ogni $i$.
2. **I blocchi sono mutuamente disgiunti:** $A_i \cap A_j = \emptyset$ per ogni $i \neq j$.
3. **L'unione di tutti i blocchi copre l'intero insieme:** $\bigcup_{i} A_i = A$.

*Metafora:* Pensa a un intero puzzle (l'insieme $A$). I singoli pezzi del puzzle sono la partizione. Nessun pezzo è fatto d'aria (1), i pezzi non si sovrappongono (2) e unendo tutti i pezzi riottieni il quadro completo (3).

---

## L'Insieme Quoziente

Se su un insieme $A$ è definita una relazione di equivalenza $\sim$, l'insieme di **tutte e sole le classi di equivalenza distinte** prende il nome di **Insieme Quoziente** e si indica con $A/\sim$.
$$A/\sim = \{ [x] \mid x \in A \}$$

> [!EXAMPLE] Esempio Notevole: $\mathbb{Z}_n$
> L'insieme delle classi di resto modulo $n$, denotato come $\mathbb{Z}_n = \{[0], [1], \dots, [n-1]\}$, non è altro che l'insieme quoziente di $\mathbb{Z}$ rispetto alla relazione di congruenza modulo $n$.
> Quindi $\mathbb{Z}_n = \mathbb{Z} / \equiv_n$.

---

## Il Teorema Fondamentale (Equivalenza ↔ Partizione)

Esiste una corrispondenza biunivoca perfetta:
1. **Da Equivalenza a Partizione:** Ogni relazione di equivalenza su $A$ genera un Insieme Quoziente $A/\sim$, il quale costituisce automaticamente una partizione di $A$. *(Le classi sono disgiunte e coprono tutto l'insieme)*.
2. **Da Partizione a Equivalenza:** Data una qualsiasi partizione $P$ di $A$, è sempre possibile definire in modo unico una relazione di equivalenza $\sim_P$, stabilendo che $x \sim_P y$ se e solo se $x$ e $y$ appartengono allo stesso blocco della partizione.

---

## Tip d'Esame

> [!TIP] Come contare le relazioni di equivalenza
> Negli esercizi in cui si chiede "Quante relazioni di equivalenza esistono su un insieme di $n$ elementi?", la risposta equivale a chiedersi "In quanti modi posso partizionare un insieme di $n$ elementi?".
> Questo numero è dato dai **Numeri di Bell** $B_n$.
> Ad esempio, per $A=\{a,b,c\}$ ($n=3$):
> - 1 blocco da 3: $\{\{a,b,c\}\}$
> - 3 blocchi da 1 e 1 da 2: $\{\{a,b\},\{c\}\}, \{\{a,c\},\{b\}\}, \{\{b,c\},\{a\}\}$
> - 3 blocchi da 1: $\{\{a\},\{b\},\{c\}\}$
> Totale: 5 relazioni di equivalenza possibili (perché $B_3 = 5$).

---

## Note Correlate
- [[01.0 - MoC Relazioni di Equivalenza e d'Ordine|Unità 2 MoC]]
- [[Relazioni di Equivalenza e Classi di Equivalenza]]
