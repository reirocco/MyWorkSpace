## Tassonomia di Flynn
sono stati catalogate le macchine in grado di eseguire istruzioni in base al numero di istruzioni e dati in input, si definiscono :SI $\to$ single instruction, MI $\to$ multiple instruction, SD $\to$ single data flow, MD $\to$ multiple data flow e la loro combinazioni descrivono le tipologie di architetture che si possono avere:
- SISD $\to$ singolo flusso di istruzioni in ingresso elaborati sequenzialmente ottenendo un singolo flusso di dati
- SIMD  $\to$ singolo flusso di istruzioni applicato a più flussi di dati (più processori elaborano le stesse istruzioni ma su dati diversi).
- MISD $\to$ molteplici flussi di istruzioni vengono eseguiti sullo stesso flusso dati
- MIMD $\to$ molteplici fussi di istruzioni vengono eseguiti su unità computazionali diverse su diversi flussi di dati
## Topologie rete MIMD
le connessioni tra i vari calcolatori sono garantite dalle seguenti topologie:
- Stella
- Anello
- griglia
- doppio toro
- cubo
- ipercubo
queste topologie vengono implementate tramite l'ausilio di apparati che lavorano a livello 3 o inferiore nello stack ISO/OSI come switch, router, hub, cavi di rete etc..
Possiamo dividere il mondo dei sistemi in WAN e LAN, rispettivamente Wide Area Network e Local Area Network
## Sistema operativo SO
i suoi ruoli principali sono quelli di eseguire i programmi dell'utente, ovvero semplificare i lavori manuali con approcci automatici e semplici. L'unica componente che è sempre in esecuzione è il ==kernel==, tutto il resto che è in esecuzione sulla macchina viene denominato ==applicativo==. Gestire l'interazione tra l'utente e il computer è il compito dell' ==interfaccia== la quale permette graficamente di accedere alle memorie le quali sono state scritte tramite un ==allocatore di risorse== che gestisce a livello generale le allocazioni delle risorse del pc in modo efficiente. Per ultimo il sistema operativo si occupa di controllare l'esecuzione dei programmi utente e le operazioni di I/O tramite il ==programma di controllo==.
### classificazione
possiamo classificarli in 
Batch $\to$ Un solo job + SO in memoria. la cpu si dedica ad un solo job
Multitasking $\to$ Diversi job + SO in memoria, la cpu si smezza tra i vari job.
22