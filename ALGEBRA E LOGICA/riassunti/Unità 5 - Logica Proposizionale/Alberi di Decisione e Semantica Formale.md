---
tags:
  - alberi-decisione
  - semantica
  - tableaux
  - logica-proposizionale
type: atomic
unit: 5
---

# Alberi di Decisione e Semantica Formale

Oltre alle noiose tabelle di verità, esistono metodi grafici e logici molto più eleganti ed efficienti per verificare la soddisfacibilità o la validità di una formula. I più noti sono gli Alberi di Decisione (Semantic Tableaux) e gli Alberi Semantici (BDD).

## Alberi Semantici (Valutazione per ramificazione)

Un albero di decisione esplora le assegnazioni di verità spezzando il problema. Invece di fare una tabella gigante, scegliamo una variabile (es. $P$) e creiamo due rami:
- Ramo Sinistro: Assumo $P = 1$ (Vero)
- Ramo Destro: Assumo $P = 0$ (Falso)

Sostituisco questo valore nella formula, la semplifico, e poi procedo ricorsivamente con le altre variabili.

> [!EXAMPLE] Valutazione ad Albero
> Formula: $F = (P \lor Q) \land \neg P$
> **Passo 1 (Scelgo P):**
> - *Ramo P=1:* Sostituisco. $F = (1 \lor Q) \land 0$. Poiché $1 \lor Q$ fa $1$, diventa $1 \land 0$, che fa $0$. Questo ramo muore (Falso).
> - *Ramo P=0:* Sostituisco. $F = (0 \lor Q) \land 1$. Diventa $Q \land 1$, che fa semplicemente $Q$.
> **Passo 2 (Scelgo Q sul ramo rimasto vivo):**
> - *Sotto-ramo Q=1:* La formula diventa 1. **(Soluzione Trovata!)**
> - *Sotto-ramo Q=0:* La formula diventa 0.
> **Conclusione:** La formula è soddisfacibile se pongo $P=0$ e $Q=1$.

---

## Metodo dei Tableaux Semantici (Alberi di Refutazione)

Il metodo dei *Tableaux* è un algoritmo puramente sintattico potentissimo per dimostrare che una formula è una Tautologia. Si basa sul ragionamento per Assurdo (Refutazione).

**Come funziona per dimostrare che $F$ è Tautologia:**
1. Scrivo alla radice dell'albero la **negazione** della formula: $\neg F$.
2. Applico le regole di espansione (derivate da De Morgan e dai connettivi) per smontare la formula in sottoformule più semplici.
   - *Regole "Alpha" (senza ramificazione):* Un AND ($\land$) vero implica che entrambi i pezzi siano veri. Scrivo i due pezzi uno sotto l'altro.
   - *Regole "Beta" (con ramificazione):* Un OR ($\lor$) vero implica che o uno o l'altro sia vero. L'albero si biforca in due rami.
3. Se in un ramo compare sia una variabile $P$ che la sua negazione $\neg P$, c'è una contraddizione. Il ramo si dice **Chiuso** (spesso indicato con una X).
4. **Esito:** Se TUTTI i rami si chiudono, significa che assumere $\neg F$ porta invariabilmente all'assurdo. Quindi $F$ è una Tautologia! Se anche un solo ramo resta aperto, $F$ non è una tautologia (e il ramo aperto ti fornisce proprio i valori per falsificarla).

---

## Tip d'Esame

> [!TIP] Strategia per Disegnare i Tableaux
> L'albero si espande in larghezza ad ogni regola Beta (OR).
> Per evitare di disegnare un albero mostruosamente largo (che non ti starà nel foglio protocollo), **applica sempre prima tutte le regole Alpha (AND)**. Le regole Alpha allungano il ramo verticalmente senza sdoppiarlo. Solo quando sei costretto, applica le regole Beta.
> Inoltre, appena un ramo si chiude con una contraddizione, marcalo con una X e **fermati** lì per quel ramo! Non continuare a smontare formule su un ramo già morto.

---

## Note Correlate
- [[05.0 - MoC Logica|Unità 5 MoC]]
- [[Sintassi e Semantica della Logica Proposizionale]]
- [[Tautologie, Contraddizioni e Equivalenze Logiche]]
