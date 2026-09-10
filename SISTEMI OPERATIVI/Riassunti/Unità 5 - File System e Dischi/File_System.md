---
id: "File_System"
tipo: zettel
tag: [tecnologia, ingegneria, sistemi_operativi, memoria, file_system, disco, allocazione]
creato: 2026-08-20
fonti: [Luca Spalazzi/Sistemi Operativi U5]
collegamenti: [[[Gestione_Memoria]]]
---

# 📌 Gestione del File System

## 1. Il Concetto di File
Un **file** è un tipo di dato astratto fornito dal Sistema Operativo (SO) per nascondere agli utenti la complessità dell'hardware di memorizzazione. Mappa uno *spazio logico contiguo* di indirizzi su memorie di massa non volatili.
Ogni file ha degli **attributi** (nome, identificatore, tipo, locazione, dimensione, permessi di protezione RWX, data/ora e proprietario), memorizzati nella directory.

## 2. Directory
La directory è essa stessa un file speciale che mappa nomi di file ad attributi e blocchi di dati.
- **Tipi di organizzazione:**
  - *A singolo livello:* Unica per tutti (problema di conflitti sui nomi).
  - *A due livelli:* Una directory per ogni utente.
  - *Ad albero:* Modello gerarchico standard con path assoluti e relativi.
  - *A grafo aciclico:* Permette la condivisione tramite *hard link* e *symbolic link* (Unix).
  - *A grafo generale:* Permette cicli. Richiede algoritmi per evitare loop infiniti durante l'attraversamento.

> [!NOTE]
> Il **Mounting** è l'operazione che permette di innestare un file system esterno in un punto della gerarchia esistente (*mount point*), rendendolo accessibile.

## 3. Metodi di Allocazione dei File su Disco
Il SO deve mappare i blocchi logici del file in blocchi fisici del disco (settori).

### 3.1 Allocazione Contigua
Ogni file occupa un insieme continuo di blocchi su disco.
- *Vantaggi:* Accesso sequenziale e diretto estremamente veloci. Semplice da gestire.
- *Svantaggi:* Frammentazione esterna (buchi non utilizzabili), difficile far crescere un file nel tempo.

### 3.2 Allocazione Concatenata (Linked)
Ogni file è una lista concatenata (linked list) di blocchi sparsi nel disco. Ogni blocco contiene un puntatore al blocco successivo.
- *Vantaggi:* Nessuna frammentazione esterna. Facile espansione.
- *Svantaggi:* L'accesso diretto (casuale) è inesistente o lentissimo (bisogna scorrere la lista dall'inizio). Spazio perso per i puntatori.
- **FAT (File-Allocation Table):** Variante dell'allocazione concatenata usata da MS-DOS. I puntatori non sono nei blocchi, ma raccolti in una tabella caricata interamente in RAM per velocizzare le ricerche.

### 3.3 Allocazione Indicizzata
Tutti i puntatori ai blocchi di un file sono raccolti in un unico blocco, detto **Tabella Indice** (Index block o *i-node* in UNIX).
- *Vantaggi:* Permette l'accesso diretto (random) ai blocchi. Nessuna frammentazione esterna.
- *Svantaggi:* Spreco di spazio se il file è molto piccolo (serve un intero blocco indice). Se il file è enorme, un solo blocco indice non basta (serve uno schema a più livelli combinati come nel File System di Unix BSD, dove un *i-node* ha blocchi diretti, indiretti singoli, doppi e tripli).

## 4. Gestione dello Spazio Libero
Il SO deve tracciare quali blocchi fisici sono liberi.
- **Vettore di bit (Bit vector):** 1 bit per ogni blocco (0 = libero, 1 = occupato). Semplice e veloce per trovare blocchi contigui (bit-wise operations), ma richiede molta RAM se il disco è grande.
- **Lista concatenata (Linked list):** Il primo blocco libero contiene un puntatore al successivo e così via. Non spreca RAM, ma è lento trovarne tanti contigui.

## 5. Caching e Buffering
- **Buffering:** Memoria transitoria per bilanciare differenze di velocità tra dispositivi (es. CPU vs disco) o gestire il trasferimento asincrono di dati di dimensioni diverse. Esempi: Buffer singolo, doppio buffer, circolare.
- **Caching del Disco:** Utilizzo di una porzione di RAM per mantenere i blocchi del disco usati di recente o che si prevede di utilizzare presto (Principio di località). Sfrutta algoritmi come LRU o LFU. Da notare la possibilità di usare un *RAM Disk*.

## 6. Il File System in Linux
In Linux il sistema è *stratificato*.
1. **Virtual File System (VFS):** Uno strato di astrazione Object-Oriented che definisce l'API comune (operazioni standard come open, read, write) valida per **qualsiasi** file system concreto, nascondendone i dettagli. Tratta `inode-object` e `file-object`.
2. **File System Concreti:**
   - **Ext2:** Basato su UFS, suddivide il disco in gruppi di blocchi. Alloca le strutture dati in modo ravvicinato.
   - **Ext3 / Ext4:** File system con *Journaling*. Ogni transazione di scrittura viene prima appuntata in un log (il journal) in modo sequenziale (*commit*) prima di essere applicata ai dati veri e propri. Garantisce un rapido *recovery* in caso di crash.
   - **ProcFS:** File system virtuale in memoria che funge da interfaccia di comunicazione con il Kernel. I file al suo interno non esistono su disco ma sono finestre sullo stato dei processi attivi e del sistema.
   - **NFS (Network File System):** File system di rete che permette di montare directory remote in modo trasparente, passando tramite RPC.
