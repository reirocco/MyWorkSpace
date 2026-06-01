---
tags:
  - matematica
  - algebra/applicazioni_lineari
aliases:
  - Funzione Lineare
  - Omomorfismo
  - Linearità
---
# Definizione di Applicazione Lineare

Siano $V$ e $W$ due spazi vettoriali sullo stesso campo (es. $\mathbb{R}$). 
Un'**applicazione lineare** (o trasformazione lineare) $T: V \to W$ è una funzione che soddisfa due assiomi fondamentali:

1. **Additività:** $T(v_1 + v_2) = T(v_1) + T(v_2)$ per ogni $v_1, v_2 \in V$.
2. **Omogeneità:** $T(c \cdot v) = c \cdot T(v)$ per ogni $c \in \mathbb{R}$ e $v \in V$.

Queste due proprietà si possono unire nel principio di conservazione delle combinazioni lineari:
$$ T(c_1 v_1 + c_2 v_2) = c_1 T(v_1) + c_2 T(v_2) $$

> [!important] Conseguenza Fondamentale: Lo Zero
> Un'applicazione lineare manda **SEMPRE** il vettore nullo del dominio nel vettore nullo del codominio:
> $$ T(\mathbf{0}_V) = \mathbf{0}_W $$
> Se hai una funzione in cui $T(\mathbf{0}_V) \neq \mathbf{0}_W$ (es. ha un termine noto tipo $T(x) = x + 3$), **NON È LINEARE**!

> [!abstract] Determinazione Unica
> Per definire *univocamente* un'applicazione lineare $T: V \to W$, è sufficiente assegnare le immagini dei vettori di una **base** di $V$. Poiché ogni altro vettore si scrive in modo unico come combinazione della base, la sua immagine sarà determinata per linearità.

## Esempi Notevoli
- **Identità**: $\text{Id}(v) = v$.
- **Applicazione Nulla**: $T(v) = \mathbf{0}_W$.
- **Moltiplicazione per Matrice**: Dato $A \in M_{m,n}$, la funzione $L_A: \mathbb{R}^n \to \mathbb{R}^m$ definita da $L_A(v) = Av$ è lineare.

## Collegamenti
- Back: [[00_Applicazioni_Lineari_MOC|MOC Applicazioni Lineari]]
- Next: [[Nucleo e Immagine]]
