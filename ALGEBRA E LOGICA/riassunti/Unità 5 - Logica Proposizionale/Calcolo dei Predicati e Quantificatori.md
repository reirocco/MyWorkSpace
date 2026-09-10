---
tags:
  - calcolo-predicati
  - quantificatori
  - logica-primo-ordine
  - logica
type: atomic
unit: 5
---

# Calcolo dei Predicati e Quantificatori

La Logica Proposizionale ha un limite enorme: è "cieca" rispetto al contenuto delle proposizioni. Può maneggiare la frase $P=$ "Tutti gli uomini sono mortali", ma non sa analizzare la struttura interna ("uomini", "mortali").
Per scendere nel dettaglio, serve il **Calcolo dei Predicati (Logica del Primo Ordine - FOL)**.

## Predicati e Variabili

- **Predicato:** È una funzione logica che restituisce Vero o Falso a seconda degli argomenti che le vengono passati. Si indica con lettere maiuscole. Es: $P(x)$ = "$x$ è un numero pari". $M(x, y)$ = "$x$ è maggiore di $y$".
- **Dominio (o Universo del Discorso):** L'insieme degli oggetti su cui variano le variabili (es. l'insieme degli esseri umani, oppure $\mathbb{N}$).
- **Variabili e Costanti:** Le lettere minuscole ($x, y$) sono variabili che "girano" nel dominio. Le costanti (es. $c$) indicano oggetti specifici.

---

## I Quantificatori: Universale ($\forall$) ed Esistenziale ($\exists$)

Per trasformare un predicato con variabili "libere" in un'affermazione che sia indiscutibilmente vera o falsa (proposizione chiusa), dobbiamo "quantificare" le variabili.

### 1. Quantificatore Universale ($\forall$)
Si legge "Per ogni", "Tutti".
L'espressione $\forall x, P(x)$ è vera se e solo se $P(x)$ è vero per **qualsiasi** elemento del Dominio.
*Esempio: In $\mathbb{Z}$, l'affermazione $\forall x, (x + 1 > x)$ è Vera.*

### 2. Quantificatore Esistenziale ($\exists$)
Si legge "Esiste almeno un", "Qualche".
L'espressione $\exists x, P(x)$ è vera se esiste **almeno un** elemento nel Dominio per cui $P(x)$ è vero.
*Esempio: In $\mathbb{Z}$, l'affermazione $\exists x, (x^2 = 4)$ è Vera (basta prendere $x=2$ o $x=-2$).*

---

## Negazione dei Quantificatori (Leggi di De Morgan estese)

Cosa succede quando mettiamo un NOT ($\neg$) davanti a un quantificatore? Le due regole d'oro da scolpire nella pietra sono:

1. **Non tutti sono... $\equiv$ Esiste qualcuno che non è...**
   $$\neg (\forall x, P(x)) \quad \equiv \quad \exists x, \neg P(x)$$
   *(Per smentire che "Tutti i cigni sono bianchi", basta trovare l'esistenza di un singolo cigno NON bianco).*

2. **Non esiste nessun... $\equiv$ Tutti non sono...**
   $$\neg (\exists x, P(x)) \quad \equiv \quad \forall x, \neg P(x)$$
   *(Dire "Non esiste nessun asino che vola" equivale a dire "Tutti gli asini non volano").*

> [!IMPORTANT] Scambiare l'ordine dei quantificatori cambia il senso!
> L'ordine in cui si scrivono i quantificatori è vitale.
> - $\forall x, \exists y \mid x < y$: "Per ogni numero esiste un numero più grande". (Vero in $\mathbb{N}$: i numeri sono infiniti).
> - $\exists y, \forall x \mid x < y$: "Esiste un numero $y$ che è contemporaneamente più grande di tutti i numeri $x$". (Falso in $\mathbb{N}$: ci vorrebbe un numero infinito che domina tutti).

---

## Tip d'Esame

> [!TIP] Tradurre dal Linguaggio Naturale
> Un errore catastrofico comune negli esami è sbagliare il connettivo quando si traduce dall'italiano alle formule FOL:
> 1. Con il **$\forall$ (Per ogni)**, si usa (quasi) sempre l'**Implicazione ($\rightarrow$)**.
>    *Frase:* "Tutti gli studenti sono bravi".
>    *Sbagliato:* $\forall x, (Studente(x) \land Bravo(x))$. (Significa "Tutti gli oggetti dell'universo sono studenti e sono bravi!").
>    *Corretto:* $\forall x, (Studente(x) \rightarrow Bravo(x))$.
> 2. Con l'**$\exists$ (Esiste)**, si usa (quasi) sempre l'**AND ($\land$)**.
>    *Frase:* "Esiste uno studente bravo".
>    *Sbagliato:* $\exists x, (Studente(x) \rightarrow Bravo(x))$. (La freccia è vera se l'antecedente è falso. Quindi l'affermazione sarebbe resa vera dall'esistenza di una sedia!).
>    *Corretto:* $\exists x, (Studente(x) \land Bravo(x))$.

---

## Note Correlate
- [[05.0 - MoC Logica|Unità 5 MoC]]
- [[Sintassi e Semantica della Logica Proposizionale]]
