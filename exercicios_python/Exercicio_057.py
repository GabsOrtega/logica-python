sexo = 'a'
while sexo != 'F' and sexo != 'M':
    sexo = str(input('\033[mDigite seu sexo [M/F]: ').upper().strip()[0])
    if sexo != 'M' and sexo != 'F':
        print('\033[31mDigite um valor válido!!')
print('Sexo {} registrado com sucesso!'.format(sexo))

