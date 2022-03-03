n = int(input('Digite um número inteiro: '))
tot = 0
for primo in range(1, n+1):
    if n % primo == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(primo))
print('\033[mO número {} foi divisivel {} vezes'.format(n, tot))

if tot == 2:
    print('E por isso ele é primo')
else:
    print('E por isso ele não é primo')