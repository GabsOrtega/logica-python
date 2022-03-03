c = 1
armazenar = 0

PT = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
armazenar += PT
a = 0
mais = 10
total = 0
while mais != 0:
    total += mais
    while c <= total:
        print('{} -> '.format(armazenar), end='')
        armazenar += razao
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos quer mostrar a mais?'))
print('Progressão finalizada com {} termos'.format(total))




