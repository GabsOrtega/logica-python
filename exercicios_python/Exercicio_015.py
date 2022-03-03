km = float(input('Qual foi a quantidade de km rodado? '))
dias = int(input('Qual foi a quantidade de dias alugado?: '))
preco = (dias*60) + (0.15*km)
print('O preço total a pagar é de: R${:.2f}'.format(preco))