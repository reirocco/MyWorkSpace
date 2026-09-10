---
id: "Sincronizzazione"
tipo: zettel
tag: [tecnologia, ingegneria, sistemi_operativi, concorrenza, semafori, mutex, monitor]
creato: 2026-08-20
fonti: [Luca Spalazzi/Sistemi Operativi U2b]
collegamenti: [[[Processi_e_Thread]], [[Stallo_e_Attesa_Indefinita]]]
---

# 📌 Sincronizzazione tra Processi e Thread

## 1. Concorrenza e Cooperazione
I processi possono essere **Indipendenti** (non interagiscono tra loro) o **Cooperanti** (l'esecuzione di uno dipende dall'altro). La cooperazione offre vantaggi come la condivisione delle informazioni e l'accelerazione dell'elaborazione, ma richiede meccanismi di **Interprocess Communication (IPC)**.

Esistono due modelli fondamentali di IPC:
1. **Memoria Condivisa (Shared Memory):** Più veloce, ma richiede sincronizzazione manuale esplicita per evitare conflitti.
2. **Scambio di Messaggi (Message Passing):** Il Sistema Operativo fornisce primitive (`send` e `receive`) per lo scambio. Può essere sincrono (bloccante) o asincrono, diretto o indiretto (tramite *mailbox*).

## 2. Corsa Critica (Race Condition)
Una **Corsa Critica** si verifica quando più processi accedono e manipolano dati condivisi concorrentemente, e il valore finale dipende dall'ordine imponderabile con cui le istruzioni vengono schedulate (interleaving). 

Per risolverlo, si individua una **Sezione Critica**: la porzione di codice in cui un processo accede alle risorse condivise.

### 2.1 Requisiti di una soluzione per la Sezione Critica
Qualsiasi algoritmo per la sezione critica deve soddisfare **tre requisiti**:
1. **Mutua Esclusione:** Se il processo $P_i$ è nella sezione critica, nessun altro processo può esservi.
2. **Progresso (Assenza di Deadlock):** Se la sezione critica è libera e dei processi vogliono entrarvi, la scelta del prossimo processo non può essere rimandata indefinitamente.
3. **Attesa Limitata (Assenza di Starvation):** Un processo non deve attendere un tempo infinito prima di ottenere l'accesso.

## 3. Algoritmi Software e Supporto Hardware

### 3.1 Supporto Hardware (TSL e CAS)
I processori moderni forniscono istruzioni hardware **atomiche** (indivisibili) per la sincronizzazione:
- **Test-and-Set (TSL):** Legge il vecchio valore di una variabile booleana e contestualmente la imposta a `true`.
- **Compare-and-Swap (CAS):** Aggiorna una variabile solo se il suo valore attuale corrisponde a quello atteso. In Java, è esposto tramite classi come `AtomicBoolean` (`getAndSet()`, `compareAndExchange()`).

### 3.2 L'Algoritmo del Fornaio (Lamport's Bakery Algorithm)
Per gestire $n$ processi in software senza istruzioni hardware speciali, si usa l'algoritmo del fornaio. Come in panetteria, ogni processo pesca un "biglietto" incrementale. Chi ha il biglietto col numero più basso entra. A parità di numero, entra il processo con il PID (o indice) minore.
> [!TIP]
> In linguaggi come Java, per l'algoritmo del fornaio i campi condivisi devono essere dichiarati `volatile` per impedire al compilatore e alla cache della CPU di riordinare l'esecuzione delle istruzioni di flag/controllo.

## 4. Astrazioni di Sincronizzazione

Le primitive basate sull'attesa attiva (*Spinlock* con cicli `while(true)`) sprecano cicli CPU (Busy Waiting). Per evitarlo, si usano primitive basate sul context switch.

### 4.1 Semafori (Dijkstra)
Un semaforo $S$ è una variabile intera accessibile solo tramite due operazioni atomiche:
- `wait(S)` (o `acquire` o $P$): se $S > 0$ decrementa $S$, altrimenti sospende il processo mettendolo in coda.
- `signal(S)` (o `release` o $V$): incrementa $S$ e, se ci sono processi in coda, ne risveglia uno.

Esistono due varianti:
- **Semaforo Contatore:** Dominio intero. Serve per gestire l'accesso a pool di risorse (es. posti auto).
- **Semaforo Binario (Mutex):** Assume solo valori 0 o 1. Un Mutex (Mutual Exclusion) assicura che **solo chi ha acquisito il lock può rilasciarlo**, al contrario del semaforo generale. (In Java implementato da `ReentrantLock`).

### 4.2 Monitor
I Monitor sono costrutti ad alto livello tipici della programmazione Object-Oriented (es. `synchronized` in Java).
- Racchiudono i dati condivisi (privati) e le operazioni (metodi pubblici).
- **Mutua esclusione implicita:** Solo un thread alla volta può eseguire un metodo all'interno del monitor.
- Le **Variabili Condition** permettono di sincronizzarsi per condizioni specifiche. I metodi esposti sono `wait()` (sospende e rilascia il lock), `notify()` (risveglia un thread a caso), `notifyAll()` (risveglia tutti i thread in coda per re-valutare la condizione).

## 5. Problemi Classici di Sincronizzazione

### 5.1 Produttore - Consumatore (Buffer Limitato)
* **Situazione:** Un produttore inserisce dati in un buffer finito di $N$ posizioni; un consumatore li estrae.
* **Sincronizzazione necessaria:** Il produttore si ferma se il buffer è pieno (`Semaphore nFree = N`); il consumatore si ferma se il buffer è vuoto (`Semaphore nItems = 0`); l'accesso all'array richiede un `Mutex`.

### 5.2 Lettori e Scrittori
* **Situazione:** Dati condivisi tra lettori (solo lettura) e scrittori (lettura e scrittura). Più lettori possono leggere contemporaneamente, ma gli scrittori richiedono accesso esclusivo assoluto.

### 5.3 I Cinque Filosofi a Cena
* **Situazione:** 5 filosofi rotondi, 5 bacchette. Servono due bacchette (dx e sx) per mangiare.
* **Rischio:** Deadlock! Se tutti prendono la bacchetta sinistra contemporaneamente, rimangono in attesa infinita di quella destra.
* **Soluzione:** Costringere uno ad essere asimmetrico, o usare l'astrazione a Monitor introducendo uno stato (HUNGRY, THINKING, EATING) e condition variables per notificare i vicini.
