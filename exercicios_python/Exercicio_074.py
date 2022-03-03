from random import randint

maior = 0
menor = 0
aleat = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10),
         randint(0, 10))

print('Os valores sorteados foram: ', end='')
for n in aleat:
    print(f'{n}', end=' ')

print(f'\nO maior número sorteado é: {max(aleat)}') ### NUMERO MAIOR DA ALEAT
print(f'O menor número sorteado é: {min(aleat)}') ### NUMERO MENOR DA ALEAT