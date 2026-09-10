---
id: "Scheduling_Dischi"
tipo: zettel
tag: [tecnologia, ingegneria, sistemi_operativi, I/O, disco, scheduling]
creato: 2026-08-20
fonti: [Luca Spalazzi/Sistemi Operativi U5]
collegamenti: [[[File_System]]]
---

# 📌 Gestione I/O e Scheduling dei Dischi

## 1. Architettura dell'I/O
I dispositivi si dividono tipicamente in:
- **Dispositivi a Blocchi (Block Devices):** Permettono l'accesso diretto e randomico a blocchi di dimensione fissa (es. dischi magnetici, SSD).
- **Dispositivi a Caratteri (Character Devices):** Trasferiscono un flusso sequenziale di byte, senza struttura a blocchi o possibilità di "seek" (es. tastiera, mouse, porte seriali).
- **Dispositivi di Rete:** Gestiti tramite l'interfaccia delle *socket*.

L'interazione tra CPU e dispositivi avviene tramite i **Device Driver** e i controller hardware, utilizzando registri (Comando, Stato, Dati) tramite *Memory-Mapped I/O* o istruzioni speciali.
Le tecniche di I/O sono:
1. **I/O Programmato (Busy-Waiting):** La CPU interroga continuamente lo stato del dispositivo (spreco di CPU).
2. **I/O ad Interruzioni (Interrupt-driven):** Il dispositivo invia un interrupt hardware alla CPU quando ha terminato.
3. **DMA (Direct Memory Access):** Un chip dedicato trasferisce i blocchi di dati tra disco e memoria principale senza gravare sulla CPU; invia un solo interrupt a fine trasferimento.

## 2. Struttura del Disco Magnetico
A basso livello, un disco rigido tradizionale è organizzato in:
- **Piatti (Platters)**, ognuno con due *superfici*.
- **Tracce (Tracks)** concentriche su ogni superficie.
- **Settori (Sectors)**, le porzioni minime di una traccia (tipicamente 512 byte o 4KB).
- **Cilindri (Cylinders):** L'insieme delle tracce con lo stesso raggio su tutti i piatti.

> [!TIP]
> Indirizzo Fisico: `<superficie, cilindro, settore>`
> Indirizzo Logico: un array mono-dimensionale di blocchi ($0 \dots N$).

### Tempo di Accesso
Il tempo per leggere/scrivere un blocco è dato da:
$$ T_{accesso} = T_{ricerca} + T_{latenza\_rotazionale} + T_{trasferimento} $$
- **Tempo di ricerca (Seek Time):** Tempo per muovere la testina sul cilindro giusto. È il costo dominante.
- **Latenza di rotazione:** Tempo affinché il settore passi sotto la testina.

## 3. Algoritmi di Scheduling del Disco
Lo scopo dello scheduling del disco è minimizzare il **Seek Time** complessivo ordinando le richieste pendenti di I/O.

### 3.1 First Come First Served (FCFS)
Le richieste vengono servite nel rigoroso ordine di arrivo.
- *Pro:* Equo, nessuna starvation.
- *Contro:* Pessimo per le prestazioni, causa movimenti erratici e lunghissimi della testina.

### 3.2 Shortest Seek Time First (SSTF)
Seleziona sempre la richiesta più vicina alla posizione corrente della testina.
- *Pro:* Riduce drasticamente i movimenti della testina rispetto a FCFS.
- *Contro:* Causa **Starvation** per le richieste destinate ai cilindri più estremi se arrivano continue richieste centrali.

### 3.3 SCAN (Algoritmo dell'Ascensore)
La testina parte da un'estremità del disco e si muove verso l'altra, servendo le richieste che incontra sul percorso. Raggiunta la fine, inverte la direzione.

### 3.4 C-SCAN (Circular SCAN)
Simile a SCAN, ma quando raggiunge la fine, ritorna immediatamente all'inizio (o viceversa) **senza servire alcuna richiesta nel tragitto di ritorno**. Tratta i cilindri come una lista circolare, garantendo tempi di attesa più uniformi.

### 3.5 LOOK e C-LOOK
Sono varianti "intelligenti" di SCAN e C-SCAN: la testina inverte la direzione non appena ha servito l'*ultima richiesta* in quella direzione, senza arrivare fino all'estremo fisico del disco.

---

> [!NOTE] Esercizio Tipico (Scheduling Dischi)
> **Problema:** Una coda di richieste I/O sui cilindri è `98, 183, 37, 122, 14, 124, 65, 67`. La testina si trova inizialmente sul cilindro `53` e (per gli algoritmi direzionali) si sta muovendo verso i cilindri superiori (verso il 199). Calcolare i cilindri attraversati.
> 
> **Svolgimento FCFS:** 
> Percorso: 53 $\rightarrow$ 98 $\rightarrow$ 183 $\rightarrow$ 37 $\rightarrow$ 122 $\rightarrow$ 14 $\rightarrow$ 124 $\rightarrow$ 65 $\rightarrow$ 67. Movimento totale = 640 cilindri.
> 
> **Svolgimento SSTF:** 
> Cerca il più vicino a 53: 65, poi 67, 37, 14, 98, 122, 124, 183. 
> Percorso: 53 $\rightarrow$ 65 $\rightarrow$ 67 $\rightarrow$ 37 $\rightarrow$ 14 $\rightarrow$ 98 $\rightarrow$ 122 $\rightarrow$ 124 $\rightarrow$ 183. Movimento totale = 236 cilindri.
> 
> **Svolgimento SCAN:** 
> Va verso l'alto (fino a 199): 65, 67, 98, 122, 124, 183, 199. Poi inverte e scende: 37, 14. 
> Movimento totale = 208 cilindri. (Con *LOOK* si fermerebbe a 183 senza arrivare a 199).

---

## 4. Scheduling dell'I/O in Linux
I sistemi Linux moderni utilizzano diversi scheduler scambiabili dinamicamente (`cat /sys/block/<device>/queue/scheduler`):

- **Noop:** Semplicemente una coda FIFO. Esegue pochissimo overhead. Usato tipicamente per i dischi a stato solido (**SSD**) o storage di rete, dove i tempi di seek (fisici) non esistono.
- **Deadline Scheduler:** Mantine diverse code (es. letture, scritture). Oltre all'ordinamento logico dei blocchi per minimizzare il seek, assegna un *tempo di scadenza (expiration time)* alle richieste (FIFO). Se una richiesta sta per scadere, viene servita immediatamente, impedendo la *starvation* causata dagli algoritmi puri come l'SSTF.
- **CFQ (Completely Fair Queueing):** Crea una coda separata per ogni processo e distribuisce la banda del disco in modalità *Round Robin*, basandosi anche sulla priorità del processo. È spesso il default per i dischi meccanici standard.
