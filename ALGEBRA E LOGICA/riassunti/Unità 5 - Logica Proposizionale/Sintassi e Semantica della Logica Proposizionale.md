---
tags:
  - logica-proposizionale
  - sintassi
  - semantica
  - formule-ben-formate
type: atomic
unit: 5
---

# Sintassi e Semantica della Logica Proposizionale

La Logica Proposizionale è lo studio delle proposizioni (affermazioni che possono essere vere o false) e di come esse si combinano. Come ogni linguaggio di programmazione, possiede una sintassi (le regole grammaticali) e una semantica (il significato).

## Sintassi (La Forma)

La sintassi definisce quali stringhe di simboli sono "valide". Non ci interessa ancora se siano vere o false, ma solo se sono "scritte bene".

L'alfabeto della logica proposizionale comprende:
1. **Variabili Proposizionali:** $P, Q, R, p_1, p_2 \dots$ (Rappresentano frasi semplici come "Piove").
2. **Connettivi Logici:** $\neg, \land, \lor, \rightarrow, \leftrightarrow$.
3. **Simboli Ausiliari:** Parentesi tonde $(, )$.

### Formule Ben Formate (FBF)
Una stringa è una **FBF (o formula proposizionale)** se è costruita secondo queste regole ricorsive:
- *Regola base:* Ogni variabile proposizionale da sola è una FBF.
- *Regola induttiva 1:* Se $A$ è una FBF, allora anche $(\neg A)$ è una FBF.
- *Regola induttiva 2:* Se $A$ e $B$ sono FBF, allora anche $(A \land B)$, $(A \lor B)$, $(A \rightarrow B)$ e $(A \leftrightarrow B)$ sono FBF.
- *Chiusura:* Nient'altro è una FBF.

*(Per comodità si omettono le parentesi esterne o si seguono le regole di precedenza: prima $\neg$, poi $\land, \lor$, infine $\rightarrow, \leftrightarrow$).*

> [!EXAMPLE] Riconoscere le FBF
> - $P \land (Q \rightarrow \neg R)$: È una FBF.
> - $P \land \lor Q$: **NON** è una FBF. Errore di sintassi.
> - $P \rightarrow$: **NON** è una FBF.

---

## Semantica (Il Significato)

La semantica si occupa di assegnare un **valore di verità** (Vero o Falso, 1 o 0) alle Formule Ben Formate.

Una **Assegnazione di Verità (o Valutazione)**, spesso indicata con $v$ o $I$, è una funzione che mappa l'insieme delle variabili proposizionali nell'insieme $\{0, 1\}$.
$$v: \{P_1, P_2, \dots\} \rightarrow \{0, 1\}$$

Una volta fissato il valore di base per le singole letterine (es. $v(P)=1, v(Q)=0$), il valore di verità dell'intera formula viene calcolato in modo deterministico e univoco "risalendo l'albero sintattico" usando le definizioni dei connettivi (Tavole di Verità).

> [!NOTE] La Separazione Cruciale
> La sintassi vive nel mondo astratto dei simboli. La semantica vive nel mondo dei valori.
> Due formule sintatticamente diverse (es. $P \rightarrow Q$ e $\neg P \lor Q$) possono avere la stessa semantica (Equivalenza Logica), proprio come in matematica $2+2$ e $1+3$ sono scritture diverse per lo stesso numero.

---

## Tip d'Esame

> [!TIP] Albero Sintattico (Sottoformule)
> Quando ti si chiede di trovare tutte le "sottoformule" di una FBF, parti dai rami più esterni (i connettivi principali) e smonta la formula ricorsivamente, senza dimenticare di includere le singole variabili proposizionali e la formula intera stessa!
> Esempio: Sottoformule di $P \land \neg Q$:
> 1. $P \land \neg Q$ (tutta)
> 2. $P$
> 3. $\neg Q$
> 4. $Q$

---

## Note Correlate
- [[05.0 - MoC Logica|Unità 5 MoC]]
- [[Connettivi Logici e Tavole di Verità]]
