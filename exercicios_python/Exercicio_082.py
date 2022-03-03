completa = []
par = []
impar = []

continuar = 'S'
while continuar != 'N':
    num = int(input('Digite um número: '))
    completa.append(num)
    continuar = str(input('Deseja continuar? [S/N]: ')).upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).upper()[0]

print(f'A lista completa é: {completa}')

for c in completa:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)

print(f'A lista de pares é: {par}')
print(f'A lista de ímpares é? {impar}')
