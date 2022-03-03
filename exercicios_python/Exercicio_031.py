distancia = float(input('Digite a distância de uma viagem em KM: '))
if distancia <= 200:
    preco = distancia*0.50
    print('A distância da viagem é de: {}KM'.format(distancia))
    print('Preço da passagem por KM: R$0.50')
else:
    print('A distãncia da viagem é de: {}KM'.format(distancia))
    print('Preço da passagem por KM: R$0.45')
    preco = distancia*0.45
#preco = distancia * 0.50 if distancia <= 200 else preco = distancia * 0.45
print('O preço da passagem é de: R${:.2f}'.format(preco))