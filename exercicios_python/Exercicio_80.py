valores = []

for pos, cont in enumerate(range(1, 6)):
    num = int(input('Digite um número: '))
    if cont == 1:
        valores.append(num)
        print('Valor adicionado ao final da lista...')
    else:
        if cont == 2:
            if num > valores[0]:
                valores.append(num)
                print('Adicionado ao final da lista')
            elif num < valores[0]:
                valores.insert(0, num)
                print('Valor adicionado ao início da lista')
        if cont == 3:
            if num > valores[-1]:
                valores.append(num)
                print('Adicionado ao final da lista')
            elif num < valores[0]:
                valores.insert(0, num)
                print('Adicionado ao começo da lista')
            elif num > valores[0] and num < valores[-1]:
                valores.insert(1, num)
                print('Adicionado na posição 1 da lista')
        if cont == 4:
            if num > valores[-1]:
                valores.append(num)
                print('Adicionado ao final da lista')
            elif num < valores[0]:
                valores.insert(0, num)
                print('Adicionado no início da lista')
            elif num > valores[0] and num < valores[-1] and num < valores[1]:
                valores.insert(1, num)
                print('Adicionado na posição 1 da lista')
            elif num > valores[0] and num < valores[-1] and num > valores[1] and num > valores[2]:
                valores.insert(2, num)
                print('Adicionado na posição 3 da lista')
        if cont == 5:
            if num > valores[-1]:
                valores.append(num)
                print('Adicionado ao final da lista')
            elif num < valores[0]:
                valores.insert(0, num)
                print('Adicionado ao início da lista')
            elif num > valores[0] and num < valores[-1] and num < valores[1]:
                valores.insert(1, num)
                print('Adicionado na posição 1 da lista')
            elif num > valores[0] and num < valores[-1] and num > valores[1] and num > valores[2]:
                valores.insert(3, num)
                print('Adicionado na posição 3 da lista')


print(f'Lista: {valores}')
