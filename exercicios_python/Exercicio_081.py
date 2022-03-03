continuar = 'S'
valores = []
cont = 0
num = 0
while continuar != 'N':
    num = int(input('Digite um valor: '))
    valores.append(num)
    cont += 1
    continuar = str(input('Deseja continuar? [S/N]: ')).upper()[0]
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja continuar? [S/N]: ')).upper()[0]
print(f'A quantidade de números digitados foi de: {cont}')
print(f'Lista em ordem decrescente: {valores.sort(reverse=True)}')
if 5 in valores:
    print(f'O valor 5 foi digitado e sua posição é: {valores.index(5)}')
else:
    print('O valor 5 não foi digitado!')
