n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

'''if n1 > n2 and n1 > n3:
    print('Maior número é {}'.format(n1))
if n2 > n1 and n2 > n3:
    print('Maior número é {}'.format(n2))
if n3 > n1 and n3 > n2:
    print('Maior número é {}'.format(n3))
if n1 < n2 and n1 < n3:
    print('Menor número {}'.format(n1))
if n2 < n1 and n2 < n3:
    print('Menor número {}'.format(n2))
if n3 < n1 and n3 < n2:
    print('Menor número {}'.format(n3))'''

menor = n1

if n2 < n1 and n2 < n3:
    menor = n2

if n3 < n1 and n3 < n2:
    menor = n3
print('Menor número {}'.format(menor))

maior = n1

if n2 > n1 and n2 > n3:
    maior = n2

if n3 > n1 and n3 > n2:
    maior = n3
print('Maior número {}'.format(maior))