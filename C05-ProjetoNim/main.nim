type
  Pessoa = object
    nome: string

proc apresentar(p: Pessoa) =
  echo "Olá, eu sou ", p.nome

var joao = Pessoa(nome: "João")

# Duas formas equivalentes:
apresentar(joao)
joao.apresentar()

