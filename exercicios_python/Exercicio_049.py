n = int(input('Digite o número que deseja a tabuada: '))

for c in range(1, 11):
    print('{} X {} = {}'.format(n, c, n*c))
