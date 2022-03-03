from random import randint
from time import sleep

print('\033[35m='*25)
print('\033[32mBem vindo!')
print('\033[35m='*25)

jogador = int(input('''\033[mDigite o número da jogada:
1 - Pedra
2 - Papel
3 - Tesoura
'''))

computador = randint(1, 3)

if jogador == 1 and computador == 1:
    print('Você escolheu Pedra!')
    print('O Computador escolheu Pedra!')
    print('\033[33mPROCESSANDO...')
    sleep(2)
    print('\033[34mEMPATE!! Ninguém ganhou!')
elif jogador == 1 and computador == 2:
    print('Você escolheu Pedra!')
    print('O Computador escolheu Papel!')
    print('\033[33mPROCESSANDO...')
    sleep(2)
    print('\033[31mYOU LOSE!!!')
elif jogador == 1 and computador == 3:
    print('Você escolheu Pedra!')
    print('O Computador escolheu Tesoura!')
    print('\033[33mPROCESSANDO...')
    sleep(2)
    print('\033[32mYOU WIN!!!')
elif jogador == 2 and computador == 1:
    print('Você escolheu Papel!')
    print('O Computador escolheu Pedra!')
    print('\033[0;33mPROCESSANDO...')
    sleep(2)
    print('\033[32mYOU WIN!!!')
elif jogador == 2 and computador == 2:
    print('Você escolheu Papel!')
    print('O Computador escolheu Papel!')
    print('\033[0;33mPROCESSANDO...')
    sleep(2)
    print('\033[34mEMPATE!! Ninguem ganhou!')
elif jogador == 2 and computador == 3:
    print('Você escolheu Papel!')
    print('O Computador escolheu Tesoura!')
    print('\033[0;33mPROCESSANDO...')
    sleep(2)
    print('\033[0;31mYOU LOSE!!!')
elif jogador == 3 and computador == 1:
    print('Você escolheu Tesoura!')
    print('O Computador escolheu Pedra')
    print('\033[0;33mPROCESSANDO...')
    sleep(2)
    print('\033[31mYOU LOSE!!!')
elif jogador == 3 and computador == 2:
    print('Você escolheu Tesoura!')
    print('O Computador escolheu Papel!')
    print('\033[0;33mPROCESSANDO...')
    sleep(2)
    print('\033[32mYOU WIN!!!')
elif jogador == 3 and computador == 3:
    print('Você escolheu Tesoura!')
    print('O Computador escolheu Tesoura!')
    print('\033[0;33mPROCESSANDO...')
    sleep(2)
    print('\033[34mEMPATE!! Ninguem ganhou!')
else:
    print('Opção inválida!')
print('\033[1;36mFim de Jogo!')
print('\033[35m='*25)
