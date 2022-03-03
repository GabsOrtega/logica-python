preco = float(input('Digite o preço do produto: R$'))
desconto = preco*(5/100)
newpreco = preco-desconto
print('O preço do produto que era de {}, ele obteve um desconto de 5% de desconto, ficando: R${:.2f}'.format(preco, newpreco))