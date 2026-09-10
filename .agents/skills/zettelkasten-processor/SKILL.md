---
name: zettelkasten-processor
description: Analizza materiale didattico (PDF, slide, appunti grezzi) ed estrae, corregge e rielabora i concetti in note atomiche Zettelkasten e Map of Content (MoC) per Obsidian.
---

# SKILL: Zettelkasten Knowledge Processor & Synthesizer (Obsidian Academic Edition)

## Descrizione
Questa skill trasforma materiale didattico grezzo (slide, PDF, appunti di lezione, trascrizioni) in un vault **Zettelkasten professionale e strutturato su Obsidian**. 
Agendo come un docente universitario ed esperto Instructional Designer, la skill applica la decomposizione atomica dei concetti, corregge errori logici o formalismi imperfetti, ed esprime la conoscenza attraverso definizioni rigorose, spiegazioni intuitive ("in soldoni"), callout nativi Obsidian, formule LaTeX pulite e una rete dinamica di collegamenti bidirezionali (WikiLinks).

---

## Principi Fondamentali & Architettura Vault

### 1. Organizzazione delle Cartelle e Nomenclatura
- **Cartelle di Capitolo/Unità:** Il corso viene suddiviso in cartelle numerate (es. `01 - Matrici`, `Unità 1 - Insiemistica e Aritmetica`, `04 - Spazi Vettoriali`).
- **MOC di Corso (Root MOC):** File unico situato nella root dei riassunti (es. `000 - NomeCorso MoC.md` o `Indice NomeCorso.md`) che offre una panoramica globale delle unità didattiche.
- **MOC di Capitolo/Unità:** Ogni cartella contiene un file Map of Content dedicato (es. `00_Spazi_Vettoriali_MOC.md` o `02.0 - MoC Relazioni di Equivalenza e d'Ordine.md`) che mappa la gerarchia concettuale dell'unità.

### 2. Principio di Atomicità (Regola d'Oro Zettelkasten)
- **1 File Markdown = 1 Singolo Concetto/Idea Fondamentale.**
- Se un argomento trattato nel materiale di partenza copre più teoremi, definizioni o concetti indipendenti, **deve essere scisso in più note atomiche distinte**, interconnesse tramite WikiLink (`[[Nome Nota]]`).

---

## Workflow Operativo

### Fase 1: Analisi, Diagnosi e Pulizia
1. **Analisi Critica del Materiale:** Leggi attentamente gli appunti o le slide fornite.
2. **Correzione di Errori ed Inesattezze:** Identifica e correggi autonomamente sviste, imprecisioni notazionali, contraddizioni logiche o passaggi matematici errati presenti nel testo sorgente.
3. **Rielaborazione Personale Accademica:** Riscrivi i concetti con un linguaggio chiaro, rigoroso e orientato alla comprensione profonda a lungo termine, evitando il mero copia-incolla.

### Fase 2: Decomposizione Atomica & Mapping Concettuale
1. Individua i mattoni concettuali isolabili (definizioni, teoremi, algoritmi, strutture algebriche).
2. Assegna a ogni nota atomica un titolo chiaro e univoco (es. `Base e Dimensione.md`, `Insieme Quoziente e Partizioni.md`).
3. Definisci il flusso di lettura (Prerequisiti $\rightarrow$ Concetto Principale $\rightarrow$ Estensioni / Conseguenze).

### Fase 3: Rielaborazione a Doppio Livello (Rigore + Intuizione)
Ogni nota deve coniugare:
- **Rigore Formale:** Definizioni matematiche esatte, notazione pulita, dimostrazioni logiche.
- **Intuizione Concettuale ("In Soldoni"):** Spiegazioni ad alto livello, analogie della vita reale o metafore visive (es. pezzi di un puzzle per le partizioni, la matematica dell'orologio per l'aritmetica modulare, i passi in una stanza per i vettori di base).

---

## Formato Standard dei File Markdown

### A. Template Nota Atomica (`type: atomic`)

```markdown
---
tags:
  - [materia]
  - [materia/sub-argomento]
aliases:
  - [Nome Alternativo 1]
  - [Nome Alternativo 2]
type: atomic
unit: [Numero o Nome Unità]
created: {{YYYY-MM-DD}}
source: "[Nome del documento o slide di origine]"
---

# [Titolo del Concetto Atomico]

[Breve paragrafo introduttivo o inquadramento contestuale del concetto].

> [!abstract] Cos'è [Nome Concetto]?
> Breve definizione formale e ad alto livello (2-3 righe), chiara ed essenziale.

## Spiegazione Formale e Notazione

[Trattazione approfondita ed esplicativa del concetto. Formule matematiche inline con $...$ o in blocco $$...$$ per le equazioni principali].

### [Sotto-paragrafo o Caso Particolare]
[Dettagli algebrici/teorici aggiuntivi].

> [!WARNING] [Titolo Trappola o Distinzione Critica]
> Evidenzia sottigliezze concettuali, differenze tra termini simili (es. Rango vs Dimensione) o errori ricorrenti.

> [!SUCCESS]- **Il concetto in soldoni:**
> [Metafora intuitiva o spiegazione semplificata ad alto livello. Es: la metafora della stanza, dell'orologio, del puzzle].

> [!info]- Dimostrazione: [Titolo del Teorema]
> [Passaggi formali della dimostrazione logico-matematica].

---

## Tip d'Esame

> [!tip] [Titolo del Suggerimento / Scorciatoia Risolutiva]
> Regole mnemoniche, strategie d'esame o trucchi per verificare al volo la correttezza dei calcoli.

> [!question]- Esercizio Pratico
> **Testo dell'esercizio:** [Traccia dell'esercizio tipico d'esame]
> 
> **Soluzione passo-passo:**
> 1. [Primo passaggio motivato]
> 2. [Secondo passaggio con calcolo in LaTeX]
> 3. **Conclusione:** [Risultato finale]

---

## Collegamenti
- Back: [[XX_NomeCapitolo_MOC|MOC NomeCapitolo]]
- Previous: [[Nota Precedente Correlata]]
- Next: [[Nota Successiva Correlata]]
- Related: [[Altra Nota Collegata]]
```

---

### B. Template Map of Content (`type: moc`)

```markdown
---
tags:
  - [materia]
  - [materia/sub-argomento]
  - moc
aliases:
  - MOC [Nome Capitolo]
type: moc
unit: [Numero Unità]
---

# MOC: [Nome del Capitolo / Unità Didattica]

[Breve descrizione sintetica dell'argomento trattato nell'Unità Didattica e dei suoi obiettivi formativi].

---

## Roadmap dei Concetti

### 1. [Primo Blocco Logico]
- [[Nome Nota Atomica 1]]: Sintesi telegrafica del contenuto della nota.
- [[Nome Nota Atomica 2]]: Sintesi telegrafica del contenuto della nota.

### 2. [Secondo Blocco Logico]
- [[Nome Nota Atomica 3]]: Sintesi telegrafica del contenuto della nota.
- [[Nome Nota Atomica 4]]: Sintesi telegrafica del contenuto della nota.

---

## Materiale di Riferimento
- [[Slide/0X_NomeFile.pdf|Slide: Titolo Lezione]]
- [[Riassunti/Capitolo_0X.pdf|Dispensa Ufficiale]]

---

## ⬅ Ritorno
- [[000 - NomeCorso MoC|Torna alla Map of Content Principale]]
```

---

## Regole Rigide di Stile, Notazione e Callout

### 1. Divieto Assoluto di Emoji nel Testo
- **NIENTE EMOJI** nel testo o nei titoli dei paragrafi. 
- L'espressività e il contrasto visivo devono essere affidati **esclusivamente** ai callout nativi di Obsidian (`[!abstract]`, `[!tip]`, `[!warning]`, `[!question]`, `[!important]`, `[!success]`, `[!info]`).

### 2. Guida ai Callout Obsidian

| Tipo Callout | Sintassi | Utilizzo Specifico |
| :--- | :--- | :--- |
| **Abstract / Definizioni** | `> [!abstract]` | Definizioni formali iniziali e inquadramenti concettuali. |
| **Warning / Caution** | `> [!WARNING]` | Trappole d'esame, errori concettuali frequenti, distinzioni critiche. |
| **Success / In soldoni** | `> [!SUCCESS]-` | Spiegazione intuitiva, "in soldoni", analogie pratiche (collapsibile con `-`). |
| **Tip d'Esame** | `> [!tip]` | Trucchi risolutivi, regole mnemoniche, metodi veloci di calcolo. |
| **Esercizi Pratici** | `> [!question]-` | Problemi d'esame svolti passo-passo con soluzione (collapsibile con `-`). |
| **Dimostrazioni** | `> [!info]-` | Dimostrazioni matematiche rigorose (collapsibili con `-`). |
| **Importante / Note** | `> [!IMPORTANT]` | Teoremi chiave o enunciati di primaria importanza. |

### 3. Convenzioni LaTeX
- Spaziatura pulita all'interno delle formule: `$a \in A$` e non `$a\in A$`.
- Blocchi centrati per equazioni chiave o definizioni formali lunghe:
  $$ \frac{R}{\text{Ker}(f)} \cong \text{Im}(f) $$
- Uso di `\text{...}` per definire nomi di insiemi o operatori nelle formule (es. `\text{Ker}(f)`, `\text{Span}(v_1, \dots, v_n)`).
- Simboli insiemistici ed algebrici corretti: `\mathbb{R}^n`, `\mathbb{Z}_n`, `\equiv`, `\pmod n`, `\subseteq`, `\forall`, `\exists`.

### 4. Evidenziazioni per l'Assimilazione Visiva
- Usa il markup nativo `==testo evidenziato==` per porre l'accento su asserzioni chiave o concetti da memorizzare a colpo d'occhio.

### 5. Collegamenti Bidirezionali (WikiLinks)
- Tutti i concetti citati devono essere linkati mediante `[[Nome Esatto Nota]]`.
- Ogni nota deve terminare obbligatoriamente con la sezione `## Collegamenti` (o `## Note Correlate`) contenente il link di ritorno alla MOC di capitolo e i puntatori alle note antecedenti, successive e correlate.
