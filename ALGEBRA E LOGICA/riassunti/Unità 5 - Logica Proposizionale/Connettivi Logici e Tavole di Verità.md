---
tags:
  - connettivi
  - tavole-verita
  - implicazione
  - logica-proposizionale
type: atomic
unit: 5
---

# Connettivi Logici e Tavole di Verità

I **Connettivi Logici** sono gli operatori che permettono di costruire formule complesse a partire da proposizioni semplici. Il loro comportamento semantico è definito esaurientemente dalle **Tavole di Verità**.

## I Cinque Connettivi Fondamentali

Assumiamo $1 = \text{Vero}$ (V) e $0 = \text{Falso}$ (F).

### 1. Negazione (NOT, $\neg P$)
Inverte il valore di verità.
- $\neg 1 = 0$
- $\neg 0 = 1$

### 2. Congiunzione (AND, $P \land Q$)
Vera **solo se** entrambe sono vere. (Corrisponde all'intersezione negli insiemi).
| P | Q | $P \land Q$ |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | **1** |

### 3. Disgiunzione (OR Inclusivo, $P \lor Q$)
Vera se **almeno una** è vera. Falsa solo se entrambe sono false. (Corrisponde all'unione).
| P | Q | $P \lor Q$ |
|---|---|---|
| 0 | 0 | **0** |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

*(Nota: Esiste anche lo XOR, "OR Esclusivo", vero se esattamente una è vera e l'altra falsa, ma si usa meno di frequente in logica di base).*

---

## Il Connettivo più Insidioso: L'Implicazione

### 4. Implicazione Materiale ($P \rightarrow Q$)
Si legge "Se $P$, allora $Q$". $P$ è detto Antecedente, $Q$ è il Conseguente.
È **FALSA in un solo caso**: quando la premessa è vera e la conseguenza è falsa.
Se la premessa è falsa, l'implicazione è **sempre vera** (a prescindere dalla conseguenza).
| P | Q | $P \rightarrow Q$ |
|---|---|---|
| 0 | 0 | **1** | *(Ex Falso Quodlibet)* |
| 0 | 1 | **1** | *(Ex Falso Quodlibet)* |
| 1 | 0 | **0** | *(L'unico caso falso!)* |
| 1 | 1 | 1 |

> [!EXAMPLE] L'Implicazione controintuitiva
> "Se sei a Roma, allora sei in Italia".
> Se sei a Milano ($P=0$), sei in Italia ($Q=1$). L'implicazione è salva (Vera).
> Se sei a Parigi ($P=0$), non sei in Italia ($Q=0$). L'implicazione è salva (Vera).
> L'unica cosa che rende la frase falsa è trovare qualcuno che è a Roma ($P=1$) ma magicamente non si trova in Italia ($Q=0$).

### 5. Doppia Implicazione (Co-implicazione, $P \leftrightarrow Q$)
Vera se e solo se $P$ e $Q$ hanno lo **stesso identico valore di verità**.
| P | Q | $P \leftrightarrow Q$ |
|---|---|---|
| 0 | 0 | **1** |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | **1** |

---

## Tip d'Esame

> [!TIP] Come tradurre l'Implicazione a Mente
> Negli esercizi di conversione in Forma Normale, devi sbarazzarti della freccia. La regola d'oro da memorizzare immediatamente è l'identità fondamentale dell'implicazione materiale:
> **$P \rightarrow Q \equiv \neg P \lor Q$**
> E per negarla (quando ti chiedono di scrivere la negazione logica di un teorema):
> **$\neg(P \rightarrow Q) \equiv P \land \neg Q$** (Prometto $P$ ma NON mantengo $Q$).

---

## Note Correlate
- [[05.0 - MoC Logica|Unità 5 MoC]]
- [[Tautologie, Contraddizioni e Equivalenze Logiche]]
- [[Forme Normali (FNC e FND)]]
