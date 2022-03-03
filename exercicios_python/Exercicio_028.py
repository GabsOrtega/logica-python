# import random

from random import randint # importa apenas a estrutura randint da biblioteca random

from time import sleep # importa apenas a estrutura sleep da biblioteca time


num = randint(0, 5) # escolhe um número entre 0 e 5 usando o modulo random estrutura randint

user = int(input('Digite o número que você acha que é: ')) # Usuário tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if user == num: # Condicional verdadeiro retornando que vc ganhou
    print('Parabéns!! Você venceu!')
    print('O número que o computador escolheu foi: {}'.format(num))
else: # Condicional falso informando que vc perdeu
    print('Que pena, tente de novo! Você perdeu!')
    print('O número que o computador escolheu foi: {}'.format(num))

