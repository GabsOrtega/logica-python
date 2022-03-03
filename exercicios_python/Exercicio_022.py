nome = str(input('Digite seu nome completo: '))
nome.strip()
nomeminusculo = nome.lower()
nomemaiusculo = nome.upper()
nomeletras = nome.split()
# nometotal = len(nome) - nome.count(' ')
nometotal = len(''.join(nomeletras))
primeironome = len(nomeletras[0])

print("""Seu nome completo é: {}.
Seu nome em maiusculas {}.
Seu nome em minusculas {}.
Seu nome possui {} letras sem espaços
E o primeiro nome possui {} letras""".format(nome, nomemaiusculo, nomeminusculo, nometotal, primeironome))