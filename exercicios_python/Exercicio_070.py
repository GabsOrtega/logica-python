nome = continuar = barato = ''
preco = total = prodmil = cont = menor = 0

while True:
    print('=-'*20)
    print('CADASTRO DE PRODUTOS')
    print('=-'*20)
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto R$'))
    cont += 1
    total += preco
    if preco > 1000:
        prodmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print('=-'*20)
print(f'O total gasto na compra foi de R${total:.2f}')
print(f'Há {prodmil} produtos que custam mais de R$1000.00')
print(f'O nome do produto mais barato é {barato} e custa R${menor}')
print('=-'*20)
