quatro = (int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite mais um número: ')),
    int(input('Digite o último número: ')))

print(f'Foi digitado 4 valores: {quatro}')

print(f'O valor 9 apareceu {quatro.count(9)} vezes')
if 3 in quatro:
    print(f'A Posição do primeiro 3 é: {quatro.index(3)+1}°')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')

print('Os valores digitados foram: ', end='')
for n in quatro:
    if n % 2 == 0:
        print(n, end=' ')



