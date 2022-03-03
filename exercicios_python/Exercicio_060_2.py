from math import factorial

num = int(input('Digite um número: '))
f = factorial(num)
print('Calculando o fatorial de {}!'.format(num))
for contador in range(num, -1, -1):
    print('{}'.format(contador), end='')
    print(' x ' if contador > 0 else ' = ', end='')
print('{}'.format(f), end='')