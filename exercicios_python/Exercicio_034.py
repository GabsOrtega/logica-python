sal = float(input('Digite seu salário: R$'))

if sal > 1250:
    aumento = sal * (10 / 100)
    salnew = sal + aumento
else:
    aumento = sal * (15 / 100)
    salnew = sal + aumento
print('''Salário antigo: R${:.2f}
Seu novo salário é de: R${:.2f}'''.format(sal, salnew))
