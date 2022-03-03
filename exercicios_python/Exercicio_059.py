n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))

menu = 0
resultado = 0

while menu != 5:
    menu = int(input('''----- MENU -----
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa
'''))
    if menu == 1:
        resultado = n1 + n2
        print('{} + {} = {}'.format(n1, n2, resultado))
    elif menu == 2:
        resultado = n1*n2
        print('{} * {} = {}'.format(n1, n2, resultado))
    elif menu == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        else:
            print('{} é maior que {}'.format(n2, n1))
    elif menu == 4:
        n1 = float(input('Digite um valor: '))
        n2 = float(input('Digite outro valor: '))
    elif menu == 5:
        print('Finalizando...')
    else:
        print('Opção inválida!')
print('Finish!!')
