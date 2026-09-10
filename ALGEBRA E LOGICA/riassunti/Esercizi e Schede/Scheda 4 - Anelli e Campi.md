---
tags:
  - esercizi
  - scheda4
  - anelli
  - polinomi
  - ruffini
type: exercise_sheet
unit: 4
---

# Scheda 4: Anelli, Polinomi e Campi

Questa nota riassume gli esercizi pratici su **divisione tra polinomi**, verifica dell'**irreducibilità** e fattorizzazione in anelli $K[x]$.

---

## 1. Divisione con Resto tra Polinomi in $\mathbb{Z}_p[x]$

### Esempio Tipo
> Calcolare il quoziente ed il resto della divisione di $f(x) = x^4 + 2x^3 + 3x + 1$ per $g(x) = x^2 + 2$ in $\mathbb{Z}_5[x]$.

### Procedura Risolutiva
Utilizza la classica divisione in colonna ricordando di operare tutti i calcoli sui coefficienti modulo 5:
- $x^4 / x^2 = x^2$.
- Moltiplica: $x^2(x^2 + 2) = x^4 + 2x^2$.
- Sottrai in $\mathbb{Z}_5$: $(x^4 + 2x^3 + 3x + 1) - (x^4 + 2x^2) = 2x^3 + 3x^2 + 3x + 1$.
- Prosegui finché il resto non ha grado $< 2$.

---

## 2. Studio dell'Irreducibilità

### Esempio Tipo
> Stabilire se $f(x) = x^3 + x + 1$ è irreducibile in $\mathbb{Z}_3[x]$.

### Procedura Risolutiva
1. Poiché $\text{deg}(f) = 3$, $f(x)$ è irreducibile $\iff$ non ha radici in $\mathbb{Z}_3 = \{[0], [1], [2]\}$.
2. **Test delle Radici:**
   - $f(0) = 0 + 0 + 1 = 1 \neq 0$.
   - $f(1) = 1 + 1 + 1 = 3 \equiv 0 \pmod 3$.
3. Poiché $x=1$ è una radice ($f(1) = 0$), per il Teorema di Ruffini $(x - 1)$ divide $f(x)$.
4. **Conclusione:** $f(x)$ è **riducibile** su $\mathbb{Z}_3[x]$.

---

## Note Correlate
- [[04.0 - MoC Anelli e Campi|Unità 4 MoC]]
- [[Definizione di Anello e Domini di Integrità]]
- [[Anelli di Polinomi e Divisibilità]]
- [[Definizione di Campo e Caratteristica]]
