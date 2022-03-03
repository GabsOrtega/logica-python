r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1+r2 > r3 and r2+r3 > r1 and r3+r1 > r2:
    print('É POSSÍVEL FORMAR UM TRIÂNGULO COM ESTES SEGMENTOS DE RETA')
    if r1 == r2 and r2 == r3:
        print('TRIÂNGULO EQUILÁTERO')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('TRIÂNGULO ISÓSCELES')
    elif r1 != r2 and r2 != r3 and r3 != r1:
        print('TRIÂNGULO ESCALENO')
else:
    print('NÃO É POSSÍVEL FORMAR UM TRIÂNGULO!')