proc somaAte(limite: int): int =
  var total = 0
  var i = 1

  while i <= limite:
    total += i
    i += 1

  return total

let n = 10
echo "Somando de 1 até ", n, ": ", somaAte(n)

echo ""

for i in 1 .. 5:

  if i mod 2 == 0:
    echo i, " é par"
  else:
    echo i, " é ímpar"


echo "Digite sua nota (A-D) :"
var notas = readLine (stdin)

case notas
of "A": echo "Não fez mais que a obrigação!"
of "B": echo "Boa nota!"
of "C": echo "Podia ser melhor!"
of "D": echo "Melhore!"
else: echo "Nota inválida!"

type
  Pessoa = object
    nome: string

proc apresentar(p: Pessoa) =
  echo "Olá, eu sou ", p.nome

var joao = Pessoa(nome: "João")

# Duas formas equivalentes:
apresentar(joao)
joao. apresentar()




