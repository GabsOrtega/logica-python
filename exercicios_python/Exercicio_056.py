media = 0
mulher = 0
maisvelho = ''
iddvelho = 0
for c in range(1, 5):
    print('----- {}° PESSOA -----'.format(c))
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: [M/F]: ').upper())
    media += idade
    if c == 1 and sexo == 'M':
        maisvelho = nome
        iddvelho = idade
    if sexo == 'M' and idade > iddvelho:
        maisvelho = nome
        iddvelho = idade
    if sexo == 'F' and idade > 20:
        mulher += 1

mediatot = media / 4
print('A média de idade dessas pessoas é de: {}'.format(mediatot))
print('O nome homem mais velho é {} e tem {} anos'.format(maisvelho, iddvelho))
print('{} mulheres tem menos de 20 anos'.format(mulher))
