
O Analisador Léxico é responsável por ler os caracteres, agrupá-los em lexemas(termos não caracterizados pela linguagem) e produzir na saída um conjunto de tokens(termos caracterizados pela linguagem) para cada lexema do programa fonte.

Problemas léxicos: Estruturas(keywords) escritas de forma incorreta, variáveis iniciando com dígitos, variáveis com nomes de keywords padrões da linguagem, variáveis com caracteres especiais(Java aceita, mas C não).

OBS.: Deixar de inserir um parênteses em um if em C não seria um problema léxico, já que todas as outras estruturas seguem as normas da linguagem e são reconhecidas. O problema seria sintático.

OBS2.: Erro de indentação em python é léxico.

### Lexema

Conjunto de termos não caracterizados pela linguagem.

### Token

Conjunto de termos caracterizados pela linguagem.

## Expressões Regulares (Regex)

### Conceitos fundamentais:

A) Alfabeto

- UTF-8;
- ASCII;
- Alfabeto Binário: Σ = {0,1}

B) String

- Cadeia finita de símbolos escolhidos de algum alfabeto;
- String vazia(**ε**): zero ocorrências de símbolos;
- Comprimento da String: indica o número de posições de uma string |010111| = 6;
- Conjunto de todas as Strings sobre um alfabeto Σ é denotado Σ*.

C) Linguagem

- Conjunto de Strings organizadas de acordo com padrões específicos

### Operadores fundamentais

A) União - Soma dos conjuntos de Strings
B) Concatenação - L.M ou LM - Junção de dois conjuntos repetindo os termos
C) Fechamento (Fecho de Kleene) - L* - conjunto de Strings que podem ser formadas tomando-se qualquer número de Strings de L(Linguagem), sempre terá o vazio 
Ex.: Se L = {0,1}, então L* consiste no conjunto de quaisquer Strings formadas por O´s e 1´s - como **ε**, 0, 1, 01, 00, 11, 0101, etc.

![[Pasted image 20250818154830.png]]

Identificadores da linguagem C para variáveis: letra(letra | dígito)*
Inicia com letra e depois vem ou uma letra ou um dígito, sendo * representativo do fecho de Kleene e indica que pode haver repetições

#### Precedências das Operações

1) Fecho de Kleene * associativo à esquerda;
2) Concatenação associativo à esquerda;
3) | tem a menor prioridade e também associativo à esquerda.

#### Outros operadores

A) Qualquer caracter sozinho(.): Operador . (ponto) reconhece um único caracter qualquer do alfabeto;
Ex.: ab. = {aba, abb}
Ex.: a.b. = {aaba, aabb, abba, abbb}

B) Uma ou mais instâncias (+): representa o fechamento positivo de algo. Indica que deve existir pelo menos uma instância e também é associativo à esquerda;
Ex.: a+ = {a, aa, aaa} - no mínimo 1 a ou infinitas
Ex.: ba+ = {ba, baa, baaa} - só faz efeito sobre o a (sem parênteses)

C) Zero ou uma instância (?): O operador ? indica zero ou uma ocorrência de um caracter e também é associativo à esquerda;
Ex.: ab? = {a, ab}
Ex.: a?b? = {**ε**, a, b, ab}

##### Diferença entre a+ e a* (prova)

a+ = {a, aa, aaa, ...}
a* = {**ε**, a, aa, aaa, ...}

### Exemplos

Σ = {a, b, c}

A) a | b : {a, b}
B) (a | b)(a | b) - concatenação: {ab, aa, ba, bb}
C) a*: {**ε**, a, aa, aaa, ...}
D) (a | b)* : {**ε**, a, b, aa, bb, aabaabb, ...}
E) a | a * b: {a, b, ab, aab aaab, ...}
F) (a | b)+c: {ac, bc, abc, bac, aac, bbc, ...}
G) (a | b)ab: {aab, bab}
H) abc? : {ab, abc}
I) a?bc.: {bca, bcb, bcc, abca, abcb, abcc} - acabar com a, b ou c(símbolos da linguagem) 
J) (a | bc)* : {**ε**, a, bc, aa, bcbc, abc, bca, ...}

## Extenção para Expressões Regulares

Classe de Caracteres

[ a - z ] : todas as letras minúsculas
[ ab ] : a ou b
[ . ] : literal ponto
[^ a-z ] : não pode ter nenhuma minúscula
[ a-z^] : {a^, b^, d^...}
[a-d]{1,} = (a|b|c|d)+ : {ada, aba, b, c, ...}

Números inteiros negativos:

![[Pasted image 20250820155749.png]]

Apenas vogais:

![[Pasted image 20250820155935.png]]

Inatel:

![[Pasted image 20250820160258.png]]

Nome de usuário de 3 a 15 linhas

![[Pasted image 20250820160651.png]]

CEP

![[Pasted image 20250820160828.png]]

Email

![[Pasted image 20250820161221.png]]

Email Inatel

![[Pasted image 20250820161916.png]]

Horas

![[Pasted image 20250820162328.png]]

Exemplo 4

![[Pasted image 20250820164601.png]]

## Python

import re -  ==importando a biblioteca RegEx==

txt = "Os melhores engenheiros são da Argentina ou Brasil"

x = re.search("^Os .* Brasil$", txt) - Busca

txt = "oi, boi"
x = re.findall("oi", txt) - busca todas as ocorrências de um termo dentro de uma string
x = re.findall("[aeiou]", txt) - busca todas as vogais em um texto

print('quantidade:',len(x))

x.span() - retorna a posição inicial e final do match(inclusive, exclusive) - uma ocorrência por vez
for match in re.finditer("r[a-z]+o", txt):
	print(match.span()) - Mostra todas as ocorrências dentro de um txt

x.group() - mostra a ocorrência de uma regex dentro de um txt, pode ser utilizado com o finditer para mostrar todas as ocorrências

x = re.split(";", txt) - separa o texto em cada ;

x = re.sub("[aeiou]", " * ", txt) - substitui o valor em 0 por 1

