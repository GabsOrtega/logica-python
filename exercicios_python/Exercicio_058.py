from random import randint
from time import sleep


jogador = 11
cont = 0
computador = 0
computador = randint(0, 10)
while jogador != computador:
    jogador = int(input('Digite o número que você deseja [0/10]: '))
    cont += 1
    print('PROCESSANDO....')
    sleep(2)
    if jogador == computador:
        print('Parabéns você acertou!')
        print('O computador escolheu o número: {} e você escolheu o número {}'.format(computador, jogador))
    elif jogador > computador:
        print('Tente um número menor!')
    elif jogador < computador:
        print('Tente um número maior')
print('Foi preciso {} tentativas'.format(cont))
print('Fim de Jogo!')