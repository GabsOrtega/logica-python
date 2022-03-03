nome = str(input('Digite seu nome completo: ')).strip()
divnome = nome.split()
print("""Seu nome é: {}
Primeiro: {}
Ultimo: {}""".format(nome, divnome[0], divnome[len(divnome)-1]))