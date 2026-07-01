---
id: "202607011240"
tipo: zettel
tag: [tecnologia, architettura_calcolatori, cpu, elaborazione]
creato: 2026-07-01
fonti: [Luca Spalazzi/Sistemi Operativi U1b]
collegamenti: [[[202607011231_Fondamenti_Sistemi_Operativi]]]
---

# 📌 Architettura della CPU e Ciclo Fetch-Decode-Execute

## 1. Contesto e Motivazione
Il fondamento teorico di qualsiasi sistema di elaborazione è il modo in cui il processore esegue il codice. Il Sistema Operativo deve conoscere intimamente questa architettura per gestire i salvataggi di contesto (Context Switch) e le interruzioni (Interrupts). La CPU opera secondo un ciclo continuo noto come *Fetch-Decode-Execute*, interagendo con la memoria centrale tramite bus di sistema (Dati, Indirizzi e Controllo).

> **Definizione:** Il *Ciclo di Istruzione* (Fetch-Decode-Execute) è il processo sequenziale attraverso cui un computer recupera un'istruzione dalla memoria, determina cosa richiede e la esegue.

## 2. Nucleo Teorico ed Elaborazione Tecnica
L'architettura interna della CPU si basa su registri specifici che orchestrano il flusso di dati e istruzioni:
- **PC (Program Counter):** Contiene l'indirizzo di memoria della prossima istruzione da eseguire.
- **IR (Instruction Register):** Contiene l'istruzione attualmente in fase di decodifica ed esecuzione.
- **MAR (Memory Address Register):** Interfaccia verso il Bus Indirizzi. Contiene l'indirizzo della locazione di memoria da leggere o scrivere.
- **MDR (Memory Data Register):** Interfaccia verso il Bus Dati. Contiene il dato letto dalla memoria o pronto per essere scritto.
- **ALU (Arithmetic Logic Unit):** Esegue le operazioni logico-matematiche.
- **ACC (Accumulatore):** Registro operativo principale per risultati temporanei.

> **Consiglio:** Fai attenzione a non confondere il ruolo del MAR e del MDR: il MAR comunica solo sul *Bus Indirizzi* in modalità Write-Only (dalla CPU alla memoria), mentre il MDR comunica bidirezionalmente sul *Bus Dati*.

### 2.1 Il Procedimento del Ciclo di Funzionamento
1. **Fetch (Prelievo):** 
   - L'indirizzo contenuto nel PC viene copiato nel MAR. 
   - La CPU invia un segnale di LETTURA sul Bus di Controllo.
   - La memoria invia l'istruzione sul Bus Dati, che viene catturata dal MDR.
   - Il contenuto del MDR viene copiato nell'IR. 
   - Il PC viene incrementato (es. PC = PC + 4 in architetture a 32-bit).
2. **Decode (Decodifica):** La Control Unit (CU) interpreta l'Opcode dell'istruzione nell'IR e attiva i circuiti logici corrispondenti. Se ci sono operandi, si calcolano gli indirizzi effettivi.
3. **Execute (Esecuzione):** L'operazione viene eseguita dall'ALU (se logico-matematica) o dai registri (se operazione di load/store in memoria). L'eventuale risultato viene salvato.
4. **Interrupt Check:** Al termine dell'esecuzione, prima di ricominciare il fetch, la CPU verifica se vi sono segnali di interrupt hardware pendenti. Se presenti, salva il PC ed entra nella routine di gestione.

### 2.2 Diagramma del Flusso di Esecuzione

```mermaid
graph TD
    Start((Inizio)) --> Fetch
    Fetch[1. FETCH<br>PC -> MAR<br>Mem[MAR] -> MDR<br>MDR -> IR<br>PC++] --> Decode
    Decode[2. DECODE<br>Decodifica IR<br>Calcolo Indirizzi] --> Execute
    Execute[3. EXECUTE<br>Esecuzione ALU/Memoria] --> IntCheck
    IntCheck{4. Interrupt<br>Pendenti?}
    IntCheck -- No --> Fetch
    IntCheck -- Sì --> HandleInt[Salvataggio Contesto<br>PC = Indirizzo ISR]
    HandleInt --> Fetch
```

## 3. Modello Matematico / Formalizzazione
Il tempo di esecuzione di un programma ($T$) in una CPU scalare è dato dalla legge del calcolo delle prestazioni (Iron Law of Processor Performance):

$$ T = N_{istruzioni} \times CPI \times T_{clock} $$

Dove:
- $N_{istruzioni}$ = Numero totale di istruzioni del programma.
- $CPI$ = Cicli di clock medi per istruzione (Cycles Per Instruction).
- $T_{clock}$ = Periodo di clock della CPU (inverso della Frequenza, $1/f$).

Le moderne architetture tentano di abbassare il CPI tramite *Pipelining* (sovrapposizione delle fasi di fetch, decode ed execute per istruzioni sequenziali).

### 3.1 Esercizio Pratico
**Problema:** Un programma è composto da $2 \times 10^6$ istruzioni. La CPU ha una frequenza di clock di 2 GHz. In media, un'istruzione richiede 1.5 cicli di clock per essere completata (grazie a una pipeline parzialmente efficiente). Calcola il tempo di esecuzione totale del programma. Se si volesse dimezzare il tempo di esecuzione migliorando solo la frequenza, quale dovrebbe essere la nuova frequenza?

**Procedimento:**
1. Parametri forniti: $N_{istruzioni} = 2 \times 10^6$, $CPI = 1.5$, Frequenza $f = 2 \text{ GHz} = 2 \times 10^9 \text{ Hz}$.
2. Calcoliamo $T_{clock} = \frac{1}{f} = \frac{1}{2 \times 10^9} = 0.5 \times 10^{-9} \text{ secondi} = 0.5 \text{ ns}$.
3. Calcoliamo il tempo di esecuzione con la CPU Performance Equation:
   $$ T = (2 \times 10^6) \times 1.5 \times (0.5 \times 10^{-9}) $$
   $$ T = 3 \times 10^6 \times 0.5 \times 10^{-9} = 1.5 \times 10^{-3} \text{ secondi} = 1.5 \text{ ms} $$
4. Per dimezzare il tempo ($T' = 0.75 \text{ ms}$) agendo solo sulla frequenza (che è inversamente proporzionale al tempo di esecuzione), la frequenza deve raddoppiare.
5. Frequenza richiesta = $2 \text{ GHz} \times 2 = 4 \text{ GHz}$.

## 4. Riferimenti Incrociati (Zettelkasten)
- **Nota Upstream (Concetto più generale):** [[Sistema di Elaborazione]]
- **Note Downstream (Specifiche/Esempi):** [[Gestione Interrupt]], [[Pipelining Architetturale]]
- **Note Correlate (Orizzontali):** [[202607011241_Gerarchia_Memoria]]
