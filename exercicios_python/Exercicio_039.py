from datetime import date

nascimento = int(input('Digite seu ano de nascimento: '))
ano = date.today().year
idade = ano - nascimento

print('Quem nasceu em {} tem anos {} em {}'.format(nascimento, idade, ano))

if idade < 18:
    saldo = 18 - idade
    recorrente = ano + saldo
    print('Você ainda não tem 18 anos!')
    print('O tempo que falta para seu alistamento é de: {} anos'.format(saldo))
    print('Seu alistamento será em {}'.format(recorrente))
elif idade == 18:
    print('Já está na hora de você se alistar no exercíto!')
elif idade > 18:
    print('Já passou do tempo do alistamento!')
    saldo = idade - 18
    passado = ano - saldo
    print('O tempo que passou do prazo de alistamento foi: {} anos'.format(saldo))
    print('Seu alistamento foi em {}'.format(passado))

