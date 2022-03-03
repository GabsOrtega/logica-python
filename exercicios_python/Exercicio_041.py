from datetime import date
nascimento = int(input('Digite seu ano de nascimento: '))
ano = date.today().year

idade = ano - nascimento

if idade <= 9:
    print('Você tem {} anos'.format(idade))
    print('Categoria: \033[1;34mMIRIM')
elif idade > 9 and idade <= 14:
    print('\033[mVocê tem {} anos'.format(idade))
    print('Categoria: \033[1;34mINFANTIL')
elif idade > 14 and idade <= 19:
    print('\033[mVocê tem {} anos'.format(idade))
    print('Categoria: \033[1;34mJUNIOR')
elif idade > 19 and idade <= 25:
    print('\033[mVocê tem {} anos'.format(idade))
    print('Categoria: \033[1;34mSÊNIOR')
elif idade > 25:
    print('\033[mVocê tem {} anos'.format(idade))
    print('Categoria: \033[1;34mMASTER')