idade = contidd = conth = contmenor = 0
sexo = continuar = ''

while True:
    print('=-'*20)
    print('CADASTRO DE PESSOAS')
    print('=-' * 20)
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
    if idade >= 18:
        contidd += 1
    if sexo == 'M':
        conth += 1
    if sexo == 'F' and idade < 20:
        contmenor += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'O número de pessoas com mais de 18 anos é de {contidd}')
print(f'Foi cadastrados {conth} Homens')
print(f'{contmenor} Mulheres tem menos de 20 anos')
