---
id: "Gestione_Memoria"
tipo: zettel
tag: [tecnologia, ingegneria, sistemi_operativi, memoria, paginazione, segmentazione, linux]
creato: 2026-08-20
fonti: [Luca Spalazzi/Sistemi Operativi U4]
collegamenti: [[[Processi_e_Thread]]]
---

# 📌 Gestione della Memoria Principale e Virtuale

## 1. Introduzione e Indirizzamento
Per essere eseguito, un programma deve risiedere nella memoria principale. La CPU genera **Indirizzi Logici (o Virtuali)**, mentre la memoria vede **Indirizzi Fisici**.
La **MMU (Memory Management Unit)** è l'hardware responsabile della traduzione a tempo di esecuzione dall'indirizzo logico a quello fisico.
- **Swapping:** I processi possono essere temporaneamente trasferiti dalla memoria principale al disco (swap-out) e viceversa (swap-in) per liberare spazio.

## 2. Allocazione Contigua
La memoria viene assegnata in un singolo blocco contiguo per ogni processo.
- **Partizioni Fisse:** La memoria è divisa in regioni di dimensione predefinita. Genera **Frammentazione Interna** (spazio sprecato all'interno di una partizione allocata perché il processo è più piccolo).
- **Partizioni Variabili:** Il SO mantiene una lista di "buchi" (spazi liberi) e li alloca su richiesta. Genera **Frammentazione Esterna** (spazio libero totale sufficiente, ma non contiguo). Si risolve tramite *compattazione* (molto costosa).
- **Algoritmi di allocazione:** 
  - *First-fit:* primo buco grande abbastanza.
  - *Best-fit:* il buco più piccolo tra quelli sufficienti.
  - *Worst-fit:* il buco più grande.

## 3. Paginazione (Paging)
Supera la necessità di allocazione contigua dividendo la memoria fisica in blocchi fissi detti **Frame** (es. 4KB) e la memoria logica in blocchi della stessa dimensione detti **Pagine**.
- Un indirizzo logico è diviso in `(p, d)`, dove $p$ è il numero di pagina e $d$ è l'offset.
- La **Tabella delle Pagine (Page Table)** mappa ogni pagina $p$ in un frame fisico $f$.
- Per mitigare il costo di un doppio accesso in memoria (uno per la tabella, uno per il dato), si usa il **TLB (Translation Look-aside Buffer)**, una velocissima memoria cache associativa integrata nella MMU.
- **Vantaggi:** Elimina la frammentazione esterna. **Svantaggi:** Può causare frammentazione interna nell'ultima pagina.

## 4. Segmentazione
Più vicina alla visione del programmatore. La memoria logica è divisa in **Segmenti** di dimensione variabile (es. un segmento per il codice, uno per lo stack, uno per l'heap).
L'indirizzo logico è `(s, d)`. La Tabella dei Segmenti contiene una *base* (indirizzo fisico di partenza) e un *limite* (lunghezza) per ogni segmento.

---

## 5. Memoria Virtuale e Paginazione su Richiesta (Demand Paging)
Lo spazio di indirizzamento virtuale può essere molto più grande della memoria fisica disponibile. Non tutto il programma deve essere in memoria contemporaneamente: le pagine vengono caricate dal disco solo quando servono.
Se un processo cerca di accedere ad una pagina non caricata in memoria fisica (bit di validità = 0), si verifica un **Page Fault**.

### 5.1 Algoritmi di Sostituzione delle Pagine
Se si verifica un Page Fault e non ci sono frame liberi, bisogna scegliere una "pagina vittima" da scaricare (swap-out).
1. **FIFO (First-In, First-Out):** Sostituisce la pagina in memoria da più tempo. Soffre dell'**Anomalia di Belady** (aumentando i frame disponibili, il numero di page fault può paradossalmente aumentare).
2. **Ottimo (OPT):** Sostituisce la pagina che non verrà usata per il periodo di tempo più lungo. È solo teorico.
3. **LRU (Least Recently Used):** Sostituisce la pagina usata meno di recente. Non soffre dell'anomalia di Belady.
4. **Seconda Chance (Algoritmo dell'Orologio):** Approssima l'LRU usando un *Reference Bit*. Se la pagina vittima scelta ha il bit a 1, le viene data una "seconda chance" azzerando il bit e si passa alla successiva (trattata in modo circolare).

> [!NOTE] Esercizio Tipico (Page Replacement)
> Data una stringa di riferimenti (es. `1, 2, 3, 4, 1, 2, 5...`) e $N$ frame inizialmente vuoti, applicare gli algoritmi FIFO o LRU e contare quanti Page Fault si verificano. Ogni caricamento iniziale in un frame vuoto conta come un Page Fault.

### 5.2 Allocazione dei Frame ai Processi
- **Assegnazione Uniforme:** $m$ frame divisi ugualmente per $n$ processi ($m/n$).
- **Assegnazione Proporzionale:** Basata sulla dimensione virtuale del processo.
- Può essere **Globale** (un processo può rubare frame a un altro, causando variazione del proprio page-fault rate) o **Locale** (ogni processo sostituisce solo le proprie pagine).

### 5.3 Thrashing (Paginazione Degenere)
Se un processo non ha abbastanza frame per ospitare la sua **Località** (l'insieme di pagine correntemente in uso), genererà continui page fault. Il sistema passa tutto il tempo a fare swapping invece di eseguire calcoli: questo stato di collasso prestazionale è il **Thrashing**. Si mitiga usando il *Working Set Model*.

---

## 6. Gestione della Memoria in Linux
Linux divide la gestione in due sottosistemi:
1. **Memoria Fisica:**
   - *Zoned Buddy Allocator:* Alloca/dealloca frame fisici (pagine) unendo e dividendo blocchi di dimensione pari a potenze di 2 per minimizzare la frammentazione.
   - *Slab Allocator:* Usato dal kernel per allocare piccoli oggetti pre-dimensionati (es. `task_struct`, inodi). Raccoglie oggetti su blocchi continui di memoria minimizzando lo spreco.
2. **Memoria Virtuale:**
   - Lo spazio virtuale del processo è diviso in **Regioni** (`vm_area_struct`), come `.text`, `.data`, heap.
   - Il demone `kswapd` scansiona periodicamente le pagine per il replacement usando due code LRU-like (Active e Inactive list), implementando una variazione della "seconda chance".
