peso = float(input('Digite seu peso: '))
alt = float(input('Digite sua altura: '))

imc = peso / (alt**2)

print('Seu IMC é {:.1f}'.format(imc))

if imc < 18.5:
    print('Abaixo do Peso!')
elif 18.5 <= imc < 25:
    print('Peso ideal!')
elif 25 <= imc < 30:
    print('Sobrepeso!')
elif 30 <= imc < 40:
    print('Obesidade!')
elif imc >= 40:
    print('Obesidade mórbida')
