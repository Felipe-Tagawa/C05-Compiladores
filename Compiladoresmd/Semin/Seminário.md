
### História e Surgimento da Linguagem

**Nim** (anteriormente conhecida como _Nimrod_) é uma [linguagem de programação compilada](https://pt.wikipedia.org/wiki/Linguagem_compilada "Linguagem compilada") de [alto nível](https://pt.wikipedia.org/wiki/Linguagem_de_alto_n%C3%ADvel "Linguagem de alto nível"), estaticamente tipada, de propósito geral, que é desenvolvida por Andreas Rumpf e foi lançada em [2008](https://pt.wikipedia.org/wiki/2008 "2008").
O desenvolvimento iniciou em [2004](https://pt.wikipedia.org/wiki/2004 "2004"), escrito em [Object Pascal](https://pt.wikipedia.org/wiki/Object_Pascal "Object Pascal") (usando o [Free Pascal](https://pt.wikipedia.org/wiki/Free_Pascal "Free Pascal")) e [Python](https://pt.wikipedia.org/wiki/Python "Python"). Entretanto, a primeira versão capaz de [compilar](https://pt.wikipedia.org/wiki/Compila%C3%A7%C3%A3o "Compilação") a si mesma foi lançada em [22 de agosto](https://pt.wikipedia.org/wiki/22_de_agosto "22 de agosto") 2008 (versão 0.6.0).

### Paradigma e Domínio de Aplicação (onde / para o que é utilizada?)

- Multiparadigma;
- Por ser uma linguagem de propósito geral, foi projetada para ser usada em uma ampla variedade de tarefas e domínios de aplicação, como C++, Java e Python;
- Principais aplicações: desenvolvimento de sistemas, aplicações web (backend e frontend), jogos e projetos de IA, por ser uma linguagem com alta performance, flexível e eficiente.

### Escopo, variáveis e tipos de dados

- A linguagem é estaticamente tipada, com tipagem forte e inferência de tipos, o que significa que, na maior parte das vezes, o compilador deduz o tipo de variável automaticamente a partir do valor atribuído.
- let (declaração de variáveis estáticas) e var(declaração de variáveis mutáveis).

### Estruturas de controle (decisão e repetição)

- Estruturas de decisão
	- if/elif/else
		- A declaração if é a forma mais comum de estrutura de decisão. O Nim também suporta elif (uma abreviação para "else if") para verificar condições adicionais.
	- Case
		- A declaração case é usada para corresponder a um valor contra vários padrões. É semelhante à declaração switch em outras linguagens, mas com a exigência de que todos os casos possíveis sejam cobertos (com a cláusula else atuando como um "coringa").
- Estruturas de repetição (laços)
	- While
		- O laço while executa um bloco de código repetidamente enquanto uma condição for verdadeira. É útil quando o número de iterações não é conhecido de antemão.
	- for
		- O laço for itera sobre um intervalo de valores ou uma estrutura de dados. O Nim suporta iteradores, e a sintaxe for os usa de forma natural.
		- for i in 1..5:
			  echo "Número: ", i
     - O Nim usa a indentação para definir blocos de código. A declaração 'block' pode ser usada para criar um novo escopo local. Ela também pode ser rotulada, o que é útil para sair de laços aninhados.

### Funções / Métodos

Em Nim, a distinção entre funções e métodos é crucial, mas a sintaxe pode ser confusa para iniciantes devido ao recurso de "Sintaxe de Chamada de Função Uniforme" (UFCS). Os conceitos são definidos da seguinte forma: 

- **proc (procedimento)**: Similar a uma função em outras linguagens. A resolução da chamada é estática, ou seja, determinada em tempo de compilação.
- **method (método)**: Oferece despacho dinâmico (despacho virtual). A implementação correta é escolhida em tempo de execução, dependendo do tipo de objeto real.
- **Sintaxe de Chamada de Função Uniforme (UFCS)**: Permite que você chame um 'proc' ou method de maneira que pareça que o primeiro argumento é um objeto chamando um método. Por exemplo, echo(x) pode ser escrito como x.echo().

### Características extras (como vantagens em relação às outras linguagens)

Compilação e desempenho

- **Velocidade de C, simplicidade de Python:** Nim compila para código nativo (via C, C++ ou JavaScript), o que resulta em um desempenho de execução próximo ao de C, mas com uma sintaxe que lembra Python. Isso permite que os desenvolvedores escrevam código de alto nível e legível, mas que seja executado com alta velocidade.
- **Compilação cruzada (multiplataforma):** A capacidade de compilar para diferentes _backends_ (C, C++, Objective-C ou JavaScript) permite que Nim seja uma linguagem universal. O mesmo código pode ser facilmente compilado para executar em diferentes plataformas. 

Gerenciamento de memória

- **Coletor de lixo opcional e flexível:** Nim oferece opções flexíveis para gerenciamento de memória. Embora tenha um coletor de lixo automático, ele é opcional, personalizável e até substituível. Isso permite que o desenvolvedor escolha a abordagem que melhor se adapta à sua aplicação, desde gerenciamento automático até manual, como o de Rust.
- **Segurança em tempo de compilação:** A linguagem possui um sistema de tipos que permite detectar erros de gerenciamento de recursos, incluindo memória, ainda em tempo de compilação. 

Metaprogramação

- **Macros avançadas:** Nim possui um poderoso sistema de macros, que permite a manipulação do código em tempo de compilação. As macros procedurais e higiênicas dão aos desenvolvedores a capacidade de estender a linguagem de forma expressiva e segura.
- **Programação genérica e templates:** Junto com as macros, os recursos de programação genérica e _templates_ (modelos) permitem a criação de código altamente flexível e reutilizável, reduzindo a duplicação e aumentando a expressividade.




