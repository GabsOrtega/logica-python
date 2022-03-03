from random import randint
from time import sleep
num = soma = venceu = 0
cond = ''

print('='*20)
print('PAR OU ÍMPAR')
print('='*20)

while True:
    num = int(input('Digite o valor desejado: '))
    cond = str(input('Você quer par ou impar? [P/I]').upper().strip()[0])
    computador = randint(0, 10)
    soma = num + computador
    print('='*20)
    if cond == 'P':
        print(f'Você escolheu PAR e o valor {num}')
        print(f'Computador escolheu IMPAR e o valor {computador}')
        print('PROCESSANDO...')
        print('='*20)
        sleep(2)
        print(f'A soma é igual a {soma}')
        if soma % 2 == 0:
            print('-' * 20)
            print('DEU PAR')
            print('Você venceu!')
            print('Computador perdeu!')
            venceu += 1
            print('-' * 20)
        else:
            print('-' * 20)
            print('DEU IMPAR')
            print('Computador venceu!')
            print('Você perdeu!')
            print('-' * 20)
            break
    if cond == 'I':
        print('=-'*20)
        print(f'Você escolheu Impar e o valor {num}')
        print(f'Computador escolheu par e o valor {computador}')
        print('PROCESSANDO...')
        print('=-' * 20)
        sleep(2)
        print(f'A soma é igual a {soma}')
        if soma % 2 == 0:
            print('-'*20)
            print('Deu PAR')
            print('Você perdeu!')
            print('Computador ganhou!')
            print('-' * 20)
            break
        else:
            print('-' * 20)
            print('Deu IMPAR')
            print('Você venceu!')
            print('Computador perdeu!')
            print('-' * 20)
            venceu += 1
    elif cond != 'P' and 'I':
        print('=-' * 20)
        print('Apenas PAR/IMPAR [P/I] são aceitos!')
        print('=-' * 20)
print('=-'*20)
print(f'GAME OVER! Você venceu {venceu} vezes')
print('Finalizando programa...')
print('=-'*20)
