c = 0
armazenar = 0

PT = int(input('Digite o Primeiro Termo da PA: '))
razao = int(input('Digite a razão da PA: '))
armazenar += PT
while c < 10:
    print('{} -> '.format(armazenar), end='')
    armazenar += razao
    c += 1
print('Acabou')
