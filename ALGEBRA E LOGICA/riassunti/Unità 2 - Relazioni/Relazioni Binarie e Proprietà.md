---
tags:
  - relazioni
  - prodotto-cartesiano
  - proprieta
  - algebra
type: atomic
unit: 2
---

# Relazioni Binarie e Proprietà

Una **relazione binaria** $R$ tra due insiemi $A$ e $B$ è un sottoinsieme del prodotto cartesiano $A \times B$.
$$R \subseteq A \times B$$
Se una coppia $(a, b)$ appartiene a $R$, scriviamo $aRb$ e diciamo che "$a$ è in relazione con $b$".

Quando $A = B$, parliamo di una **relazione sull'insieme $A$** ($R \subseteq A \times A$).

---

## Proprietà delle Relazioni (su uno stesso insieme $A$)

Data una relazione $R$ sull'insieme $A$, essa può godere di una o più delle seguenti proprietà:

### 1. Riflessiva
Ogni elemento è in relazione con se stesso.
$$\forall a \in A, \quad aRa$$
*Esempio: La relazione "$\le$" sui numeri reali. $3 \le 3$.*

### 2. Antiriflessiva
Nessun elemento è in relazione con se stesso.
$$\forall a \in A, \quad \neg(aRa)$$
*Esempio: La relazione "$<$" (strettamente minore). Non è mai vero che $3 < 3$.*

### 3. Simmetrica
Se $a$ è in relazione con $b$, allora $b$ è in relazione con $a$.
$$\forall a, b \in A, \quad aRb \implies bRa$$
*Esempio: "Essere fratelli". Se Marco è fratello di Luca, Luca è fratello di Marco.*

### 4. Antisimmetrica
Se $a$ è in relazione con $b$ e $b$ è in relazione con $a$, allora $a$ e $b$ devono coincidere.
$$\forall a, b \in A, \quad (aRb \land bRa) \implies a = b$$
*Esempio: La divisibilità ($|$). Se $a|b$ e $b|a$ in $\mathbb{N}$, allora $a=b$.*

### 5. Transitiva
Se $a$ è in relazione con $b$ e $b$ è in relazione con $c$, allora $a$ è in relazione con $c$.
$$\forall a, b, c \in A, \quad (aRb \land bRc) \implies aRc$$
*Esempio: "Essere maggiore di". Se $x > y$ e $y > z$, allora $x > z$.*

> [!EXAMPLE] Analisi di una Relazione
> Sia $A = \{1, 2, 3\}$ e $R = \{(1,1), (2,2), (3,3), (1,2), (2,1)\}$.
> - **Riflessiva?** Sì, contiene $(1,1), (2,2), (3,3)$.
> - **Simmetrica?** Sì, c'è $(1,2)$ e anche $(2,1)$.
> - **Antisimmetrica?** No, perché ci sono $(1,2)$ e $(2,1)$ ma $1 \neq 2$.
> - **Transitiva?** Sì (l'unica catena non banale è $1R2 \land 2R1 \implies 1R1$, che è presente).

---

## Tip d'Esame

> [!TIP] Dimostrare l'Antisimmetria
> Nelle dimostrazioni matematiche su insiemi infiniti, per dimostrare l'antisimmetria si deve sempre partire dall'ipotesi $aRb$ E $bRa$. Si mettono a sistema le due condizioni algebriche e si deduce logicamente che $a = b$. Non tentare di dimostrarlo provando tutti i numeri!

---

## Note Correlate
- [[01.0 - MoC Relazioni di Equivalenza e d'Ordine|Unità 2 MoC]]
- [[Relazioni di Equivalenza e Classi di Equivalenza]]
- [[Relazioni d'Ordine e Diagrammi di Hasse]]
