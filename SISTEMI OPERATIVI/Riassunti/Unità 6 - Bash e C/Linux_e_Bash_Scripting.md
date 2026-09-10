---
id: "Linux_e_Bash_Scripting"
tipo: zettel
tag: [tecnologia, ingegneria, sistemi_operativi, linux, bash, scripting, shell]
creato: 2026-08-20
fonti: [Ing. Fernando Negozi / Sistemi Operativi U6]
collegamenti: [[[Programmazione_C_Processi_Syscall]]]
---

# 📌 Pratica in Linux: Bash Scripting

## 1. La Shell e gli Script
La **shell** è l'interprete dei comandi che funge da interfaccia tra l'utente e il sistema operativo. Permette di lanciare sia *comandi interni* (interpretati nativamente dalla shell) sia *comandi esterni* (eseguibili caricati dal disco in memoria).

Uno **script** è un file di testo contenente un elenco di comandi di sistema eseguiti in modo sequenziale. Fornisce i costrutti tipici della programmazione (variabili, cicli, condizioni) e serve ad automatizzare procedure tediose o complesse.

### La Shebang (`#!`)
Ogni script Bash ben formato deve iniziare con una direttiva speciale chiamata **Shebang**, che indica al sistema operativo quale interprete lanciare per eseguire lo script.
```bash
#!/bin/bash
# Questo è un commento
echo "Hello World"
exit 0
```

> [!WARNING]
> Affinché il sistema operativo permetta l'esecuzione di un file script, questo deve avere il permesso di "esecuzione" impostato: `chmod +x nomescript.sh`

## 2. Variabili e Parametri

In Bash non c'è una tipizzazione forte; tutto è gestito come stringa o numero a seconda del contesto.
Non bisogna usare spazi intorno all'uguale durante l'assegnazione.
```bash
NOME="Mario"
echo "Ciao, mi chiamo $NOME"
```

### Parametri Posizionali
Quando si invoca uno script da linea di comando, è possibile passargli argomenti. La shell popola automaticamente alcune variabili speciali:
- `$0`: Il nome dello script eseguito.
- `$1`, `$2`, `...`: Il primo, il secondo parametro, ecc.
- `$#`: Il numero totale dei parametri passati.
- `$*` o `$@`: Tutti i parametri passati.
- `$?`: Codice di uscita (exit status) dell'ultimo comando eseguito (0 significa successo).

## 3. Costrutti di Controllo (If/Else)
L'istruzione `if` utilizza il costrutto `[ ]` (che è un alias per il comando `test`) per valutare le condizioni.

```bash
#!/bin/bash
if [ $1 -gt 10 ]; then
    echo "Il primo parametro è maggiore di 10"
elif [ $1 -eq 10 ]; then
    echo "Il primo parametro è esattamente 10"
else
    echo "Il primo parametro è minore di 10"
fi
```
> [!TIP]
> **Operatori Comuni:**
> `-eq` (uguale), `-ne` (diverso), `-gt` (maggiore), `-lt` (minore), `-ge` (maggiore o uguale), `-le` (minore o uguale).
> Sui file si usa: `-e file` (esiste), `-f file` (è un file regolare), `-d dir` (è una directory).

## 4. Cicli (For e While)

### Ciclo For
Utile per iterare su un elenco o sui file in una directory.
```bash
#!/bin/bash
# Stampa tutti i file .txt nella cartella corrente
for FILE in *.txt; do
    echo "Trovato: $FILE"
done
```

### Ciclo While
Ripete fintanto che una condizione è vera.
```bash
#!/bin/bash
CONTATORE=1
while [ $CONTATORE -le 5 ]; do
    echo "Ciclo numero $CONTATORE"
    CONTATORE=$((CONTATORE + 1))
done
```

## 5. Ridirezione e Pipe
La potenza della shell deriva dalla facilità di combinare l'output di più programmi indipendenti.

- **Ridirezione (`> ` e `>>`):** Invia l'output (stdout) su file. `>` sovrascrive, `>>` accoda.
- **Ridirezione Input (`<`):** Prende l'input da un file invece che dalla tastiera.
- **Pipe (`|`):** Collega l'output standard (stdout) di un programma direttamente all'input standard (stdin) di un altro.

**Esercizio d'esempio:** Creare uno script che trova i tre file più pesanti in una cartella.
```bash
#!/bin/bash
# 1. Usa 'ls' per elencare i file per dimensione (-S) in formato lungo (-l)
# 2. Salta la prima riga di totale (tail -n +2)
# 3. Prende i primi tre risultati (head -n 3)
ls -lS | tail -n +2 | head -n 3
```
