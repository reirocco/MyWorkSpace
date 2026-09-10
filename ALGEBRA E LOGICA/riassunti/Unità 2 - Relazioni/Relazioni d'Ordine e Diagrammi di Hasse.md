---
tags:
  - ordine
  - hasse
  - poset
  - algebra
type: atomic
unit: 2
---

# Relazioni d'Ordine e Diagrammi di Hasse

Mentre le relazioni di equivalenza astraggono il concetto di uguaglianza, le **Relazioni d'Ordine** astraggono il concetto di "maggiore/minore", permettendo di strutturare gerarchicamente gli elementi di un insieme.

## Definizione di Relazione d'Ordine (POSET)

Una relazione $R$ su un insieme $A$ (spesso indicata col simbolo $\le$) si dice di **ordine (parziale)** se è contemporaneamente:
1. **Riflessiva:** $\forall a \in A, \quad a \le a$
2. **Antisimmetrica:** $\forall a, b \in A, \quad (a \le b \land b \le a) \implies a = b$
3. **Transitiva:** $\forall a, b, c \in A, \quad (a \le b \land b \le c) \implies a \le c$

Un insieme $A$ dotato di una relazione d'ordine parziale si chiama **Poset** (Partially Ordered Set) e si indica con la coppia $(A, \le)$.

### Ordine Totale vs. Ordine Parziale
- **Ordine Totale (o Lineare):** Se per ogni coppia di elementi $a, b \in A$, vale sempre $a \le b$ oppure $b \le a$. (Tutti gli elementi sono confrontabili). Esempio: I numeri Reali con la normale disuguaglianza.
- **Ordine Parziale:** Esistono elementi **inconfrontabili**, per cui non vale né $a \le b$ né $b \le a$. Esempio: La relazione di inclusione $\subseteq$ tra gli insiemi; $\{1\} \not\subseteq \{2\}$ e $\{2\} \not\subseteq \{1\}$.

---

## Diagrammi di Hasse

I **Diagrammi di Hasse** sono lo strumento grafico standard per visualizzare insiemi parzialmente ordinati (POSET) finiti. Permettono di "pulire" il grafo della relazione rimuovendo gli archi ridondanti.

### Come costruire un Diagramma di Hasse:
1. Disegna un punto (nodo) per ogni elemento dell'insieme $A$.
2. **Regola dell'Alto-Basso:** Se $a \le b$ e $a \neq b$, disegna il nodo $b$ più in alto (o allo stesso livello) del nodo $a$.
3. **Archi di Copertura:** Traccia un arco (senza freccia) da $a$ a $b$ **solo se** $b$ *copre* $a$.
   - *$b$ copre $a$ se $a \le b$ e non esiste alcun elemento $x$ intermedio tale che $a \le x \le b$.*
4. **Omissioni:** Non tracciare i cappi (proprietà riflessiva, sono impliciti) e non tracciare archi deducibili per transitività.

> [!EXAMPLE] L'Insieme dei Divisori
> Sia $A = \{1, 2, 3, 6\}$ con la relazione di divisibilità "$|$".
> Costruiamo Hasse:
> - $1$ divide tutti, quindi sta alla base.
> - $2$ e $3$ sono divisibili per $1$, ma non si dividono tra loro (sono sullo stesso livello, inconfrontabili).
> - $6$ è divisibile sia per $2$ che per $3$, quindi sta in cima.
> Il diagramma assomiglia a un "diamante": il $6$ sopra collegato al $2$ e al $3$, i quali a loro volta si collegano all'$1$ in basso.

---

## Tip d'Esame

> [!TIP] Come tracciare Hasse senza sbagliare
> L'errore più comune negli scritti è tracciare troppi archi.
> Se hai tracciato un arco da $a$ verso $b$, e uno da $b$ verso $c$, **non devi assolutamente** tracciare un arco da $a$ a $c$. È ridondante e ti toglieranno punti. La transitività si "legge" seguendo i percorsi, non disegnando scorciatoie!

---

## Note Correlate
- [[01.0 - MoC Relazioni di Equivalenza e d'Ordine|Unità 2 MoC]]
- [[Elementi Notevoli negli Insiemi Ordinati]]
