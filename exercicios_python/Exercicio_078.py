valores = []

for pos, v in enumerate(range(0, 5)):
    valores.append(int(input(f'Digite um número na posição {pos}: ')))

maior = max(valores)
menor = min(valores)
posmaior = valores.index(maior)
posmenor = valores.index(menor)

print(f'O maior valor dessa lista é: {maior} e as suas posições são: ', end='')
for pos2, n in enumerate(valores):
    if n == maior:
        print(pos2, end=' ')
print(f'\nO menor valor dessa lista é: {menor} e as suas posições são: ', end='')

for pos2, n in enumerate(valores):
    if n == menor:
        print(pos2, end=' ')







