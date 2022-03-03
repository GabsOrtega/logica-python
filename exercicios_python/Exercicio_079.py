continuar = 'S'
valores = []
while continuar != 'N':
    num = int(input('Digite um número: '))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com Sucesso!')
    else:
        print('Valor Duplicado, não irei adicioná-lo')
    continuar = str(input('Deseja continuar? [S/N]: ')).upper()[0]
    while 'S' != continuar != 'N':
        continuar = str(input('Deseja continuar? [S/N]: ')).upper()[0]
valores.sort()
print(f'Lista: {valores}')
