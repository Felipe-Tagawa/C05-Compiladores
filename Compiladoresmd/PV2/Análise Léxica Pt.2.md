## Autômatos Finitos (Máquina de Estados Finitos)

- Modelo computacional e também um mecanismo de reconhecimento (gráfico). Um autômato verifica se uma palavra W pertence a uma linguagem L.

![[Pasted image 20250915153946.png]]

String 'abaac' é válida
S1 - a -> S2;
S2 - b -> S1;
S1 - a -> S2;
S2 - a -> S2;
S2 - c -> S4 (estado final - só é válida se acabar em S4).

#### Aplicações

- Comportamento de circuitos digitais;
- Examinar grandes corpos de texto;
- Softwares de verificação de sistemas como protocolos de comunicações;
- Utilizados na construção de Analisadores Léxicos.

### Conceitos Importantes

1) Fita de Entrada: String que será validada/informação a ser processada;
2) Unidade de Controle: indica o Estado Atual da máquina;
3) Função de Transição do Autômato - determina o novo estado da máquina(grafos).

### Tipos

1) Autômatos Finitos Deterministas (DFA) - o sistema pode somente assumir um ÚNICO estado bem determinado;
2) Autômatos Finitos Não Deterministas (NFA) - o sistema pode assumir um CONJUNTO de estados alternativos;
3) Autômatos Finitos com movimentos vazios (NFA-e - o sistema pode assumir um conjunto de estados mesmo sem ler qualquer símbolo).

#### Simbologias

##### A = (Q, Σ, δ, q0, F)

A - Nome do DFA;
Q - Conjunto de Estados;
Σ - Conjunto de símbolos de entrada;
δ - Função de transição;
q0 é o Estado Inicial;
F é o conjunto de estados de aceitação (ou o estado onde pode acontecer uma finalização).
* * Simboliza o Estado Final.
- -> Simboliza o Estado Inicial.

Exemplo

![[Pasted image 20250915160136.png]]

Q = {1,2};
Σ = {letra, dígito};
δ: (1,letra) = 2; (2, letra) = 2; (2, dígito) = 2;
q0: 1
F: {2} - círculo duplo;

JFLAP

Números Inteiros:

![[Pasted image 20250915161723.png]]

Números Flutuantes:

![[Pasted image 20250915161958.png]]

0 seguido de 1s ou 1s:

![[Pasted image 20250915163948.png]]

3 'a's consecutivos:

![[Pasted image 20250915164708.png]]
