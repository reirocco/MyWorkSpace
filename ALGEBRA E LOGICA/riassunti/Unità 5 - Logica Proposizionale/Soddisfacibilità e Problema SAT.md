---
tags:
  - soddisfacibilita
  - sat
  - np-completo
  - complessita
  - logica
type: atomic
unit: 5
---

# Soddisfacibilità e Problema SAT

Il problema della **Soddisfacibilità Booleana (SAT)** è forse il problema algoritmico più famoso e studiato di tutta l'Informatica Teorica, trovandosi al cuore della Teoria della Complessità Computazionale.

## Cos'è la Soddisfacibilità?

Una formula proposizionale si dice **soddisfacibile** se esiste *almeno una* assegnazione di verità alle sue variabili che la rende Vera.
- Se nessuna assegnazione la rende vera, è una **Contraddizione** (Insoddisfacibile).
- Se tutte le assegnazioni la rendono vera, è una **Tautologia** (Valida).

*(Una tautologia è ovviamente soddisfacibile, ma una formula soddisfacibile non è per forza una tautologia).*

## Il Problema SAT

Il **Problema SAT** (Boolean Satisfiability Problem) chiede:
> "Data una formula logica arbitraria, scrivi un algoritmo capace di rispondere in modo efficiente SI/NO alla domanda: La formula è soddisfacibile?"

### L'Apparente Semplicità
Sembra un problema banale: basta scrivere la Tavola di Verità e controllare se nella colonna finale c'è almeno un "1".
Il problema è l'**esplosione combinatoria**: se la formula ha $n$ variabili, la tabella avrà $2^n$ righe.
- Per 10 variabili: 1.024 righe (il computer ci mette una frazione di millisecondo).
- Per 300 variabili: $2^{300}$ righe (un numero infinitamente superiore agli atomi nell'universo visibile. Nemmeno il supercomputer più veloce del mondo finirebbe mai il calcolo).

---

## NP-Completezza e SAT Solvers

SAT è stato il primo problema dimostrato essere **NP-Completo** (Teorema di Cook-Levin, 1971).
Questo significa due cose:
1. Se qualcuno indovina l'assegnazione giusta, è facilissimo e veloce verificare che sia effettivamente corretta.
2. Se esistesse un algoritmo capace di risolvere SAT in modo "veloce" (in tempo polinomiale $P$), allora **tutti** i problemi complessi del mondo (crittografia, logistica, biologia) diventerebbero risolvibili velocemente ($P = NP$). Attualmente si ritiene che ciò sia impossibile.

> [!NOTE] SAT Solvers Moderni
> Nonostante la pessima complessità teorica "nel caso peggiore", gli informatici hanno sviluppato programmi incredibilmente intelligenti chiamati **SAT Solvers** (es. MiniSAT, Z3).
> Questi programmi accettano in input formule rigorosamente scritte in **Forma Normale Congiuntiva (FNC)** e usano euristiche avanzate (come l'algoritmo DPLL) per saltare intere porzioni della tabella di verità, riuscendo a risolvere casi pratici industriali con milioni di variabili in pochi secondi.

---

## Tip d'Esame

> [!TIP] Riduzione a SAT
> Negli esercizi più complessi o nei progetti informatici pratici, ti capiterà di dover risolvere un puzzle logico (es. Sudoku, colorazione di grafi). Il trucco non è scrivere un algoritmo per il Sudoku! Il trucco è **tradurre le regole del Sudoku in una gigantesca formula FNC** e darla in pasto a un SAT Solver pre-esistente. Questa tecnica si chiama "Riduzione" ed è il pane quotidiano dell'Informatica.

---

## Note Correlate
- [[05.0 - MoC Logica|Unità 5 MoC]]
- [[Tautologie, Contraddizioni e Equivalenze Logiche]]
- [[Forme Normali (FNC e FND)]]
