# 📐 La Giacitura: Definizione e Proprietà Geometriche

La **giacitura** è il sottospazio vettoriale che definisce l'orientamento di un oggetto geometrico (retta, piano o iperpiano). ==Rappresenta la "direzione pura" dell'oggetto, privata della sua posizione specifica nello spazio.==

---

### 🔹 1. Definizione Concettuale
Un sottospazio affine $S$ (come una retta o un piano) è definito da un punto $P_1$ e dalla sua giacitura $V$:
- **Sottospazio Affine**: $S = P_1 + V$.
- **Parallelismo**: Due sottospazi sono paralleli se e solo se hanno la stessa giacitura (ovvero se i vettori che le generano sono gli stessi o proporzionali).
- **Visualizzazione**: La giacitura è l'oggetto "gemello" che passa per l'origine degli assi $(0,0,0)$.

---

### 🔹 2. Estrazione della Giacitura

Esistono due modi principali per identificare la giacitura a seconda della descrizione dell'oggetto:

#### A. Dalla forma Parametrica (Base della Giacitura)
==La giacitura è lo **Span** dei vettori direttori dell'oggetto.==
- **Retta**: La giacitura è generata da un solo vettore direttore $v$.
  - $V_r = \text{Span}\{v\}$.
- **Piano**: La giacitura è generata da due vettori direttori $\{v, w\}$ linearmente indipendenti.
  - $V_\alpha = \text{Span}\{v, w\}$.

#### B. Dalla forma Cartesiana (Equazione Omogenea)
Per un iperpiano (o un piano in $\mathbb{R}^3$), la giacitura si ottiene ponendo a zero il termine noto $d$.
- **Equazione Iperpiano**: $ax + by + cz + d = 0$.
- **Equazione Giacitura**: $ax + by + cz = 0$.

---

### 🔹 3. Proprietà e Ortogonalità
La giacitura è strettamente legata al concetto di **complemento ortogonale**:

1. **Vettore Normale**: Il vettore normale $\vec{n} = (a, b, c)$ di un iperpiano è ortogonale a ogni vettore della sua giacitura.
2. **Relazione Ortogonale**: $(\text{Giacitura})^\perp = \text{Span}\{\vec{n}\}$.
3. **Verifica di Appartenenza**: Un vettore $v$ appartiene alla giacitura di un iperpiano se il loro prodotto scalare è nullo: $\langle \vec{n}, \vec{v} \rangle = 0$.

---

### Cheat Sheet Rapido

| Oggetto       | Dimensione | Base della Giacitura        | Equazione Giacitura                      |
| :------------ | :--------- | :-------------------------- | :--------------------------------------- |
| **Punto**     | 0          | $\emptyset$                 | Tutte le coordinate nulle                |
| **Retta**     | 1          | $\{v\}$ (Vettore Direttore) | $n-1$ equazioni omogenee                 |
| **Piano**     | 2          | $\{v, w\}$ (Indipendenti)   | 1 equazione omogenea (in $\mathbb{R}^3$) |
| **Iperpiano** | $n-1$      | $n-1$ vettori indipendenti  | $a_1x_1 + \dots + a_nx_n = 0$            |
