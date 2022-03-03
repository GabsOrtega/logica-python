media = num = contador = maior = menor = mediatot = 0
continuar = 'S'
while continuar != 'N':
    num = int(input('Digite um número inteiro: '))
    contador += 1
    media += num
    if contador == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    continuar = str(input('Deseja continuar? [S/N]').upper().strip()[0])
mediatot = media/contador
print('A média entre todos os {} números digitados foi de: {}'.format(contador, mediatot))
print('O maior número digitado foi: {} e o menor númnero digitado foi: {}'.format(maior, menor))
