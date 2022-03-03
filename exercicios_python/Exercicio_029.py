v = float(input('Digite a velocidade do carro: '))

if v <= 80:
    print('Sua velocidade é de: {}KM/H'.format(v))
    print('Ufa! Você não foi multado!')
else:
    multa = (v-80)*7
    print('Sua velocidade é de: {}KM/H'.format(v))
    print('Você foi multado!')
    print('Valor da multa: R${:.2f}'.format(multa))