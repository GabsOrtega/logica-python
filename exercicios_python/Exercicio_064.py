'''num = 0
c = 0
soma = 0'''

num = c = soma = 0

while num != 999:
    num = int(input('Digite um número inteiro [999 para parar]: '))
    if num != 999:
        c += 1
        soma += num
print('Você digitou {} números'.format(c))
print('E a soma deles é igual a {}'.format(soma))
