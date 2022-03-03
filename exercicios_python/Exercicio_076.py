itens = ('Lápis', 1.50, 'Borracha', 1.00, 'Caneta', 2.00, 'Video-game', 2.500, 'Almofada', 5.00, 'Bexigão', 10.00,
'Controle PS4', 250.00, 'Notebook', 4.500, 'Cadeira Gamer', 450.00, 'Colchão', 500.00)

print('-'*40)
print(f'{"Listagem de preços":^40}')
print('-'*40)



for pos in range(0, len(itens)):
    if pos % 2 == 0:
        print(f'{itens[pos]:.<30}', end='')
    else:
        print(f'R${itens[pos]:>7.2f}')
print('-'*40)