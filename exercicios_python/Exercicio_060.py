num = int(input('Diigte um número: '))
contador = num
f = 1
print('Calculando o fatorial de {}!'.format(num))
while contador > 0:
    print('{}'.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end ='')
    f *= contador ## f = f * contador
    contador -= 1
print('{}'.format(f), end='')







