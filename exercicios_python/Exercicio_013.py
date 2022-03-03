sal = float(input('Digite seu salário: R$'))
aumento = sal*(15/100)
newsal = sal+aumento
print('Seu salário antigo era de: R${:.2f}Seu novo salário é de: R$ {:.2f}'.format(sal, newsal))
