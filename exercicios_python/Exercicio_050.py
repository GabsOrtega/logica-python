s = 0
cont = 0
for rept in range(1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
        cont += 1
print('A soma dos {} números digitados que são pares é: {}'.format(cont, s))
