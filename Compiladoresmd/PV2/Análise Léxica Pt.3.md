
## Autômatos Finitos Não Deterministas(NFA)

- A partir de uma nova entrada, pode-se ter várias saídas;
- Todo DFA é um NFA;
- Na definição, a única diferença se encontra na função de transição;


abb: 1 - a -> 2 - b -> 4 - e -> 2 - b -> 4
ab+: 1 - a -> 2 - b -> 4 - e -> 2 -b -> 4 - e -> 2 - b -> 4 ...
ab*: 1 - a -> 3 - e -> 4 - e -> 2 - b -> 4 - e -> 2 - b -> 4
b*: 1 - e -> 4 - e -> 2 - b -> 4 - e -> 2 - b -> 4 ...

![[Pasted image 20250917162056.png]]

![[Pasted image 20250917163350.png]]

### Construção de Thompson

- Criação de NFAs a partir de uma expressão regular.

- Passos:
	- 1) Construímos um NFA para cada subexpressão;
	- 2) utilizamos e-transições para juntar cada pedaço de uma expressão regular e formar uma máquina correspondente à expressão toda;
	- 3) Cada operação de um REGEX pode ser obtida pela conexão de NFAs das subexpressões.
- #### Concatenação
	- A regEx tem o estado inicial de r e o estado de aceitação s.
	- ![[Pasted image 20250929154252.png]]
- #### União
	- É adicionado um novo estado inicial e um novo estado de aceitação r | s.
	 ![[Pasted image 20250929154339.png]]
- #### Repetição (Fecho * )
	- Para que cadeias vazias sejam aceitas, inserimos uma e-transição do novo estado inicial para o estado de aceitação.
	- ![[Pasted image 20250929154649.png]]
- #### Repetição (Mais +)
	- A repetição aparece na nova e-transição do estado de aceitação de r para seu estado inicial.
	 ![[Pasted image 20250929154802.png]]


Exemplo 5

ab | a

1)
-> 1 - a -> 2
-> 1 - b -> 2

2)

-> 1 - a -> 2 - e -> 3 - b -> 4

3)

   -e-> 1 - a -> 2 - e -> 3 - b -> 4
|                                                    |
5                                        - e - > 6      
|                                      |
   -e-> 5 - a -> 6 - e -> 6

![[Pasted image 20250929155535.png]]

![[Pasted image 20250929155654.png]]


### Transformação AFN para AFD

8 passos

##### Passo 1

- Construir a tabela de transição

![[Pasted image 20251006154026.png]]

##### Passo 2

- Construir a tabela de transições do AFD através do produto cartesiano dos estados do AFN, incluindo como último conjunto o vazio:

![[Pasted image 20251006154135.png]]

##### Passo 3

Construir a tabela a partir da outra menor(exemplo no excel)

##### Passos 4 e 5

Eliminar casos desnecessários - casos inalcançáveis

No exemplo os estados s1, s3 e s6 não aparecem na tabela (são eliminados)

![[Pasted image 20251006155903.png]]

Essa tabela passa ser:

![[Pasted image 20251006160025.png]]

##### Passo 6

- Montar o AFD
![[Pasted image 20251006160046.png]]

##### Passo 7

- Eliminar os estados que não possuem saída para outro estado e não são finais
![[Pasted image 20251006160131.png]]

##### Passo 8

- Testar


![[Pasted image 20251006162206.png]]

#### AFN (com e-transição) para AFD

- O e-fecho de um único estado s é definido como sendo o conjunto de estados atingíveis por uma série com zero ou mais e-transições;
- O conjunto é denotado por s com uma barra em cima;
- O e-fecho de um estado sempre inclui o próprio estado.

##### Passo 1

- Escrever o e-fecho do primeiro estado e muda-se o nome dele (A, por exemplo)
##### Passo 2

- Cria-se uma tabela de transição com (Estado do AFN, Estado do AFD e todas os valores de estado);

##### Passo 3

- Computa-se as transições de caracteres

![[Pasted image 20251008155548.png]]![[Pasted image 20251008155557.png]]![[Pasted image 20251008155559.png]]     ![[Pasted image 20251008155615.png]]
{1,2,4}a = {3} = {2,3,4} = B - apenas do 2 eu recebo o 'a';

   ![[Pasted image 20251008155627.png]]![[Pasted image 20251008155628.png]]![[Pasted image 20251008155629.png]]
{2,3,4}a = {3} = {2,3,4} = B

##### Passo 4

- O processo anterior é repetido até que novos estados e transições não sejam mais criados.

##### Passo 5

- Escreve-se os estados de aceitação(borda dupla);

##### Passo 6

- Desenhar o AFD resultante.


