---
id: "Programmazione_C_Processi_Syscall"
tipo: zettel
tag: [tecnologia, ingegneria, sistemi_operativi, c, processi, linux, fork]
creato: 2026-08-20
fonti: [Ing. Fernando Negozi / Sistemi Operativi U6]
collegamenti: [[[Processi_e_Thread]], [[Linux_e_Bash_Scripting]]]
---

# 📌 Programmazione di Sistema in C (Linux)

## 1. Introduzione alle System Call
In Linux, i programmi interagiscono con il kernel tramite le chiamate di sistema (**System Call**). Tali chiamate vengono avvolte (wrapped) da librerie C standard come la `glibc`, rendendo l'utilizzo più trasparente per il programmatore.

L'inclusione di header come `<unistd.h>`, `<sys/types.h>` e `<sys/wait.h>` è essenziale per manipolare processi e gestire l'I/O a basso livello.

## 2. Creazione di Processi: La `fork()`
La system call base per generare processi in Linux è `fork()`.
Essa crea un clone esatto del processo chiamante. I due processi (Padre e Figlio) proseguono la loro esecuzione dalla riga successiva alla `fork()`, avendo però due spazi di indirizzamento completamente separati.

La funzione restituisce un intero (`pid_t`) che funge da "smistatore" logico:
- Restituisce **0** al processo *Figlio*.
- Restituisce il **PID** del figlio appena nato al processo *Padre*.
- Restituisce **-1** in caso di errore.

### Esempio Pratico
```c
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    pid_t pid = fork();

    if (pid < 0) {
        perror("Errore nella fork");
        return 1;
    } else if (pid == 0) {
        // --- Spazio del Figlio ---
        printf("Sono il processo FIGLIO. Mio PID: %d, Mio Padre: %d\n", getpid(), getppid());
    } else {
        // --- Spazio del Padre ---
        printf("Sono il processo PADRE. Mio PID: %d. Ho creato il figlio: %d\n", getpid(), pid);
        
        // Il padre aspetta la terminazione del figlio per evitare processi "Zombie"
        wait(NULL);
        printf("Il figlio è terminato.\n");
    }

    return 0;
}
```

> [!CAUTION] Processi Zombie e Orfani
> Se il padre termina prima del figlio, il figlio diventa un processo **Orfano** e viene "adottato" dal processo `init` (PID 1).
> Se il figlio termina, ma il padre non esegue mai la `wait()` per raccoglierne lo stato di ritorno (exit code), la riga descrittiva del figlio rimane nella tabella dei processi allocando memoria inutile. Questo processo è detto **Zombie**.

## 3. Sovrascrivere l'immagine del processo: La famiglia `exec()`
Mentre `fork` clona lo stato attuale, le funzioni `exec()` sostituiscono l'intero spazio di memoria, codice e dati del processo corrente con un nuovo programma eseguibile letto dal disco. La funzione `exec` **non ritorna mai**, a meno che non fallisca.

Tipicamente, per eseguire un programma esterno, si effettua la combo `fork` + `exec` nel figlio.

```c
#include <stdio.h>
#include <unistd.h>

int main() {
    if (fork() == 0) {
        // Nel figlio invochiamo il comando "ls -l"
        execlp("ls", "ls", "-l", NULL);
        // Questa riga viene eseguita solo se execlp fallisce!
        perror("Exec fallita");
    }
    wait(NULL);
    return 0;
}
```

## 4. Comunicazione Inter-Processo: Le Pipe (`pipe()`)
Le Pipe rappresentano un condotto unidirezionale (simplex) usato per far comunicare due processi imparentati (solitamente Padre e Figlio). 
La system call `pipe(int fd[2])` crea due File Descriptor:
- `fd[0]`: per leggere (Read end).
- `fd[1]`: per scrivere (Write end).

> [!TIP]
> Quando si crea una pipe in combinazione con una `fork()`, il processo che deve leggere *chiude* il lato di scrittura, e il processo che deve scrivere *chiude* il lato di lettura, per mantenere la direzionalità corretta e consentire l'invio dell'EOF.

### Esempio Pratico
Un padre genera una stringa e la invia tramite pipe al figlio.
```c
#include <stdio.h>
#include <unistd.h>
#include <string.h>

int main() {
    int fd[2];
    char buffer[100];
    char messaggio[] = "Ciao figlio, studia Sistemi Operativi!";

    if (pipe(fd) == -1) {
        perror("Pipe fallita"); return 1;
    }

    if (fork() == 0) {
        // Lato Figlio (Lettore)
        close(fd[1]); // Chiude il lato di scrittura
        read(fd[0], buffer, sizeof(buffer));
        printf("Il figlio ha ricevuto: %s\n", buffer);
        close(fd[0]);
    } else {
        // Lato Padre (Scrittore)
        close(fd[0]); // Chiude il lato di lettura
        write(fd[1], messaggio, strlen(messaggio) + 1);
        close(fd[1]);
        wait(NULL);
    }
    return 0;
}
```
