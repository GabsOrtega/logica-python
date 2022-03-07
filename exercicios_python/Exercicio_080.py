valores = []

for cont in range(1, 6):
    num = int(input('Digite um número: '))
    if cont == 1 or num > valores[-1]:
        valores.append(num)
        print('Valor adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print(f'Lista: {valores}')


