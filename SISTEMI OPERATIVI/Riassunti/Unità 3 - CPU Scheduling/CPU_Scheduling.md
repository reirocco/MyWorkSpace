---
id: "CPU_Scheduling"
tipo: zettel
tag: [tecnologia, ingegneria, sistemi_operativi, scheduling, linux, cfs, cpu]
creato: 2026-08-20
fonti: [Luca Spalazzi/Sistemi Operativi U3]
collegamenti: [[[Processi_e_Thread]]]
---

# 📌 CPU Scheduling

## 1. Ciclo di Esecuzione e Scheduler
L'esecuzione di un processo consiste in un'alternanza di **CPU burst** (fasi di elaborazione attiva) e **I/O burst** (fasi di attesa di dispositivi). 
- **Processi I/O-bound:** Trascorrono più tempo in operazioni di I/O, sono caratterizzati da numerosi e brevi CPU burst.
- **Processi CPU-bound:** Trascorrono più tempo a fare computazione (calcoli), presentano pochi ma lunghi CPU burst.

### 1.1 Livelli di Scheduling
1. **Job Scheduler (Lungo termine):** Decide quali processi ammettere in memoria. Controlla il grado di multiprogrammazione. È lento e invocato raramente.
2. **Middle-term Scheduler:** Regola l'eccesso di multiprogrammazione per evitare il *Thrashing*, spostando temporaneamente i processi dalla memoria al disco (*Swap-out* e *Swap-in*).
3. **CPU Scheduler (Breve termine):** Seleziona il prossimo processo in stato `ready` a cui assegnare la CPU. È velocissimo e viene invocato frequentemente (ogni millisecondo). L'azione materiale di assegnazione è eseguita dal **Dispatcher**, il quale effettua il *context switch*.

## 2. Criteri di Scheduling
Un buon algoritmo mira a:
- **Massimizzare:** Utilizzo CPU e Produttività (Throughput - processi completati per unità di tempo).
- **Minimizzare:** Tempo di Completamento (*Turnaround time*), Tempo di Attesa (tempo speso nella ready queue) e Tempo di Risposta.

## 3. Algoritmi di Scheduling per Monoprocessore

### 3.1 First-Come, First-Served (FCFS)
La CPU viene assegnata nell'ordine di arrivo. È un algoritmo **Non-Preemptive** (senza prelazione).
- **Svantaggio:** *Effetto Convoglio* (Convoy effect). I processi molto brevi rimangono bloccati ad attendere che un lungo processo CPU-bound finisca, causando un pessimo tempo medio di attesa.

### 3.2 Shortest Job First (SJF)
Assegna la CPU al processo con il *CPU burst* successivo più breve. È **matematicamente ottimale** per minimizzare il tempo medio di attesa.
- Esiste sia in versione Non-Preemptive, sia **Preemptive** (nota anche come *Shortest-Remaining-Time-First, SRTF*).
- **Problema:** Come conoscere la lunghezza del prossimo burst? La si *stima* basandosi sulla media esponenziale dei burst passati: $\tau_{n+1} = \alpha t_n + (1 - \alpha) \tau_n$.

### 3.3 Priority Scheduling
Ad ogni processo viene assegnata una priorità e viene eseguito quello con priorità massima.
- **Problema:** *Starvation* (Attesa indefinita). I processi a bassa priorità rischiano di non essere mai eseguiti.
- **Soluzione:** *Aging* (Invecchiamento). La priorità di un processo viene gradualmente innalzata man mano che aspetta nella ready queue.

### 3.4 Round Robin (RR)
Preemptive. Ogni processo riceve un **quanto di tempo** (Time slice, $q$). Scaduto il quanto, il processo viene sospeso e ri-accodato circolarmente.
- Se $q$ è molto grande, RR degenera nel FCFS.
- Se $q$ è troppo piccolo, l'overhead del context switch riduce drasticamente le prestazioni.

### 3.5 Code Multilivello (Multilevel Queue e Feedback)
La ready queue viene frammentata (es. foreground e background) assegnando un algoritmo diverso per ogni coda (es. RR per i processi interattivi, FCFS per i batch).
- Nel **Multilevel Feedback Queue**, i processi si muovono dinamicamente tra le code: un processo che esaurisce troppi quanti (CPU-bound) viene "degradato" a code con priorità inferiore, ma quanti più lunghi.

---

## 4. Scheduling su Multiprocessore

Nel contesto multicore (Symmetric Multiprocessing - SMP), si introducono nuovi concetti:
- **Affinità con il processore (Processor Affinity):** Mantenere un thread sulla stessa CPU (o nodo NUMA) per sfruttare i dati già presenti nella cache L1/L2.
- **Bilanciamento del carico:** *Push migration* (spostare attivamente processi verso CPU scariche) e *Pull migration* (CPU libere si prendono processi dalle code piene).
- **Gang Scheduling / Coscheduling:** Allocare i thread legati ad un unico job su processori fisici paralleli per lo stesso "time slice", in modo che possano cooperare in modo sincrono.

---

## 5. Lo Scheduling in Linux

Linux adotta due classi principali di scheduling basate sulle priorità (scala da 0 a 139):

### 5.1 Real-Time (Classe `sched_rt`)
Priorità da 0 a 99. Usa algoritmi simili al Round Robin. Sfrutta 100 code, implementate tramite una mappa di bit (bitmap), garantendo un tempo di selezione di $O(1)$.

### 5.2 Completely Fair Scheduler - CFS (Classe `sched_fair`)
Copre i processi *time-sharing* normali (priorità da 100 a 139).
- Il valore `nice` (da -20 a +19) determina il peso del processo.
- Non utilizza una coda classica, ma un albero rosso-nero (**Red-Black Tree**).
- Il parametro di ordinamento è il **virtual runtime (vruntime)**: il tempo di CPU speso, normalizzato dal suo peso.
- Ad ogni tick, il CFS seleziona per l'esecuzione il task con il `vruntime` minore, localizzato sul *nodo più a sinistra* del RB-Tree.
- Il tempo di selezione è di conseguenza limitato e l'inserimento o rimozione ha un costo di $O(\log n)$.

> [!NOTE] Esercizio Tipico (FCFS, SJF, RR)
> Calcolare il diagramma di Gantt e il tempo medio di attesa.
> - **Tempo di attesa** di un processo = (Tempo di inizio esecuzione) - (Tempo di Arrivo). In caso di prelazione (es. RR, SRTF), si sommano anche i ritardi in cui il processo è stato sospeso per far eseguire altri.
> - **Tempo di Completamento (Turnaround)** = (Tempo di fine esecuzione) - (Tempo di Arrivo).
