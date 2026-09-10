---
id: "Stallo_e_Attesa_Indefinita"
tipo: zettel
tag: [tecnologia, ingegneria, sistemi_operativi, concorrenza, deadlock, algoritmo_banchiere]
creato: 2026-08-20
fonti: [Luca Spalazzi/Sistemi Operativi U2c]
collegamenti: [[[Processi_e_Thread]], [[Sincronizzazione]]]
---

# 📌 Stallo (Deadlock) e Attesa Indefinita (Starvation)

## 1. Definizioni
- **Deadlock (Stallo):** Due o più processi sono bloccati in attesa permanente di un evento che può essere causato solo da uno dei processi bloccati. (Es. due processi attendono ciascuno la risorsa bloccata dall'altro).
- **Starvation (Attesa Indefinita):** Un processo pronto per l'esecuzione non ottiene mai le risorse necessarie perché vengono continuamente assegnate ad altri processi (es. a causa di politiche di priorità rigide).

## 2. Le Condizioni di Coffman per il Deadlock
Affinché si verifichi uno stallo, devono essere vere **contemporaneamente** quattro condizioni necessarie:
1. **Mutua esclusione:** Le risorse coinvolte non sono condivisibili (es. una stampante o un file in scrittura).
2. **Possesso e attesa (Hold and Wait):** Un processo trattiene almeno una risorsa ed è in attesa di acquisirne di nuove trattenute da altri.
3. **Assenza di prelazione (No Preemption):** Le risorse non possono essere sottratte forzatamente; solo il processo che le detiene può rilasciarle volontariamente.
4. **Attesa circolare:** Esiste un ciclo chiuso di processi $\{P_0, P_1, ..., P_n\}$ tale che $P_0$ attende $P_1$, $P_1$ attende $P_2$, e così via fino a $P_n$ che attende $P_0$.

## 3. Grafo di Assegnazione delle Risorse
Lo stato del sistema può essere modellato come un grafo orientato bipartito:
- Nodi $P$ (Processi) e nodi $R$ (Risorse, che possono avere istanze multiple).
- Arco di **richiesta:** $P_i \rightarrow R_j$.
- Arco di **assegnazione:** $R_j \rightarrow P_i$.

> [!TIP]
> Se il grafo non contiene cicli $\implies$ **No Deadlock**.
> Se il grafo contiene un ciclo $\implies$ **Possibile Deadlock**. (Se ogni risorsa ha una singola istanza, il ciclo è condizione sufficiente per il deadlock).

## 4. Metodi di Gestione dello Stallo
I Sistemi Operativi possono adottare diverse strategie:
1. **Ignorare il problema (Algoritmo dello Struzzo):** Si assume che i deadlock siano rari. È l'approccio usato da gran parte dei SO (incluso UNIX e Windows) perché più economico.
2. **Prevenzione (Prevention):** Intervenire staticamente per invalidare almeno una delle quattro condizioni di Coffman (es. imporre un ordine globale di acquisizione delle risorse per negare l'attesa circolare).
3. **Evitamento (Avoidance) - *Algoritmo del Banchiere*:** Il sistema decide dinamicamente ad ogni richiesta se concedere la risorsa manterrà il sistema in uno **Stato Sicuro**.
4. **Rilevamento e Ripristino:** Lasciare che il deadlock accada, individuarlo periodicamente e intervenire (es. terminando brutalmente i processi o facendo il rollback tramite prelazione delle risorse).

---

## 5. L'Algoritmo del Banchiere (Dijkstra, 1972)
Per risorse a istanza multipla, si usa l'algoritmo del banchiere per garantire l'evitamento dello stallo.
Ogni processo dichiara a priori il **massimo** numero di risorse di cui avrà bisogno (`Max`).

### Strutture Dati:
- `Available[m]`: Vettore delle risorse attualmente disponibili.
- `Max[n][m]`: Matrice della richiesta massima per ogni processo.
- `Allocation[n][m]`: Matrice delle risorse attualmente assegnate.
- `Need[n][m]`: Matrice delle risorse ancora necessarie (`Need = Max - Allocation`).

### 5.1 Esercizio Pratico: Algoritmo del Banchiere
**Problema:** Dato il seguente stato, determinare se il sistema è in uno stato sicuro e, in caso affermativo, trovare una sequenza sicura.

*Risorse Totali:* A(10), B(5), C(7).
*Stato Corrente:*
| Processo | Allocation (A B C) | Max (A B C) | Available (A B C) |
|----------|--------------------|-------------|-------------------|
| P0       | 0 1 0              | 7 5 3       | 3 3 2             |
| P1       | 2 0 0              | 3 2 2       |                   |
| P2       | 3 0 2              | 9 0 2       |                   |
| P3       | 2 1 1              | 2 2 2       |                   |
| P4       | 0 0 2              | 4 3 3       |                   |

**Svolgimento:**
1. **Calcolo matrice Need** (`Need = Max - Allocation`):
   - P0: 7 4 3
   - P1: 1 2 2
   - P2: 6 0 0
   - P3: 0 1 1
   - P4: 4 3 1
2. **Ricerca Sequenza Sicura:**
   - Inizialmente `Work = Available = (3 3 2)`.
   - Possiamo soddisfare P1? Sì, perché `Need(P1) = (1 2 2) <= (3 3 2)`. P1 esegue e rilascia: `Work = Work + Alloc(P1) = (3 3 2) + (2 0 0) = (5 3 2)`.
   - Possiamo soddisfare P3? Sì, `Need(P3) = (0 1 1) <= (5 3 2)`. P3 esegue: `Work = (5 3 2) + (2 1 1) = (7 4 3)`.
   - Possiamo soddisfare P4? Sì, `Need(P4) = (4 3 1) <= (7 4 3)`. P4 esegue: `Work = (7 4 3) + (0 0 2) = (7 4 5)`.
   - Possiamo soddisfare P0? Sì, `Need(P0) = (7 4 3) <= (7 4 5)`. P0 esegue: `Work = (7 4 5) + (0 1 0) = (7 5 5)`.
   - Possiamo soddisfare P2? Sì, `Need(P2) = (6 0 0) <= (7 5 5)`. P2 esegue: `Work = (7 5 5) + (3 0 2) = (10 5 7)`.
3. **Risultato:** Tutti i processi hanno terminato. La sequenza `<P1, P3, P4, P0, P2>` è **Sicura**. Il sistema è in uno **stato sicuro** e non andrà in deadlock.

---

## 6. Prevenzione della Starvation (Aging)
L'attesa indefinita spesso scaturisce da algoritmi di scheduling basati su priorità strette, dove i processi a bassa priorità non vengono mai eseguiti.
- **Soluzione:** Implementare l'**Aging (invecchiamento)**. La priorità di un processo aumenta gradualmente proporzionalmente al tempo in cui rimane in attesa nel sistema.
