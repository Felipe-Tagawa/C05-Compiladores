import re

txt = "Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz."

# Código que substitua todas as palavras maiores que 5 caracteres por astericos (*).

print(re.sub("[A-Za-zÇçãéÉÃ]{6,}", "*", txt))

# Código que retorne uma lista apenas das palavras que contém caracteres com acentos.

for match in re.finditer("[A-Za-zç]*[ãÃéÉíÍóÓúÚõÕ][A-Za-zç]*", txt):
    print(match.group())

# Código que em um único REGEX, troque as letras maiúsculas por minúsculas, e vice-versa.

print(re.sub("[a-zA-ZçãéÉ]", lambda match: match.group().swapcase(), txt))

# Código que retorna a posição inicial e final da maior palavra do texto.

print(re.search(max(txt.split(), key=len).rstrip(","), txt).span())

# Código que retorna uma lista apenas com as palavras que possuam de 2 a 6 letras.

for match in re.finditer(r"\b[A-Za-zçéÉ]{2,6}\b", txt):
    print(match.group())

# Código que retorna uma lista de Strings que deverão ser quebradas toda vez que for encontrada uma letra maiúscula.

print(re.split("[A-ZÉ]", txt))

# Código que retorne todas as palavras que contenham vogais.

for match in re.finditer("[A-Za-zç]*[aAeEiIOouUéÉãÃ][A-Za-zç]*", txt):
    print(match.group())

# Código que responda quantas letras o texto base possui.

print(len(re.findall(r"[A-Za-zÁÉÍÓÚÀÃÕáéíóúàãõçÇ]", txt)))




