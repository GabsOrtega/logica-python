# import random
import random
from random import choice

aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4]

## SEMPRE COLOQUE TODA LISTA ENTRE []
escolhido = choice(lista)
print('O Aluno escolhido foi: {}'.format(lista))

