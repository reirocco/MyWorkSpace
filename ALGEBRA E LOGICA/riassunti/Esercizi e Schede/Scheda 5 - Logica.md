---
tags:
  - esercizi
  - scheda5
  - logica
  - fnc
  - tableaux
type: exercise_sheet
unit: 5
---

# Scheda 5: Logica Proposizionale e Tableaux

Questa nota riassume gli esercizi tipici d'esame sulla **Logica Proposizionale**, la trasformazione in **Forma Normale Congiuntiva (FNC)** e la risoluzione con **Tableaux Semantici**.

---

## 1. Conversione in Forma Normale Congiuntiva (FNC)

### Esempio Tipo
> Convertire in FNC la formula $F = (P \rightarrow Q) \rightarrow R$.

### Procedura Risolutiva
1. **Elimina le implicazioni:**
   - $P \rightarrow Q \equiv \neg P \lor Q$.
   - $F \equiv (\neg P \lor Q) \rightarrow R \equiv \neg(\neg P \lor Q) \lor R$.
2. **Applica De Morgan per spingere la negazione:**
   - $\neg(\neg P \lor Q) \equiv \neg(\neg P) \land \neg Q \equiv P \land \neg Q$.
   - Quindi $F \equiv (P \land \neg Q) \lor R$.
3. **Applica la legge distributiva di $\lor$ su $\land$:**
   - $(P \land \neg Q) \lor R \equiv (P \lor R) \land (\neg Q \lor R)$.
4. **Risultato in FNC:** $(P \lor R) \land (\neg Q \lor R)$.

---

## 2. Verifica di Tautologia tramite Tableaux Semantici

### Esempio Tipo
> Dimostrare tramite il metodo dei Tableaux che $A = ((P \rightarrow Q) \land P) \rightarrow Q$ (Modus Ponens) è una tautologia.

### Procedura Risolutiva
1. **Radice per Refutazione:** Poni $\neg A$:
   $$\neg (((P \rightarrow Q) \land P) \rightarrow Q)$$
2. **Applica regola $\alpha$ su $\neg(\phi \rightarrow \psi)$:**
   - Ramo unico contenente:
     1. $(P \rightarrow Q) \land P$
     2. $\neg Q$
3. **Applica regola $\alpha$ su congiunzione (1):**
   - Ramo unico contenente:
     3. $P \rightarrow Q$
     4. $P$
4. **Applica regola $\beta$ su implicazione (3):**
   - **Ramo Sinistro:** contiene $\neg P$. Troviamo $P$ (da 4) e $\neg P \implies$ **CHIUSO ($\times$)**.
   - **Ramo Destro:** contiene $Q$. Troviamo $\neg Q$ (da 2) e $Q \implies$ **CHIUSO ($\times$)**.
5. **Conclusione:** Tutti i rami sono chiusi $\implies \neg A$ è insoddisfacibile $\implies A$ **è una TAUTOLOGIA**.

---

## Note Correlate
- [[05.0 - MoC Logica Proposizionale|Unità 5 MoC]]
- [[Forme Normali (FNC e FND)]]
- [[Alberi di Decisione e Semantica Formale]]
- [[Tautologie, Contraddizioni e Equivalenze Logiche]]
