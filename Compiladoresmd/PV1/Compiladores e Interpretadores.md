
### Compiladores

Compilador é um programa que recebe um programa na entrada em uma LP e traduz esse código em um programa equivalente, denominado programa objeto.
Front-End(Análise e Geração de código intermediário);
Back-End (Síntese - otimização e geração do código alvo).
Entre a análise semântica e a geração do código intermediário, há o tratador de erros e a tabela de símbolos <if, keyword> - agrupamento de tokens
Análise Léxica analisa cada termo  e utiliza os tokens;
Análise Sintática utiliza os tokens por meio de uma árvore sintática - if (a > 10 {}) - esse erro daria na análise léxica;
Analise Semântica realiza a coerção;
Geração de Código Intermediário - as representações intermediárias devem ter algumas propriedades: 
Otimização do código - 
Geração do código alvo - gerada a saída do código Assembly

#### Compilação Cruzada

- Técnica utilizada para compilar programas de uma plataforma Y a partir de uma plataforma X, onde esses 2 são distintos (Ex.: Arduíno, sistemas embarcados).

### Outros programas

1. Pré-Processador (Preprocessor) - Programa ativado pelo compilador que apaga comentários, incluir arquivos e bibliotecas, colocar funções constantes e constantes universais nos lugares devidos.
	Bibliotecas Estáticas (import e # define) e Dinâmicas (.dll e .lib - arquivos de extensão)

### Interpretadores

- Programa capaz de interpretar instruções de alto nível(linguagem fonte), executando-as diretamente. Isso faz com que a velocidade seja bem mais lenta do que linguagens que apresentam compiladores, mas deixa a linguagem mais legível e simples(menos línguas de código)

### Compiladores Híbridos

- Java tem alta portabilidade;
- O compilador converte o código para um bytecode e depois esse bytecode é interpretado pela JVM.



