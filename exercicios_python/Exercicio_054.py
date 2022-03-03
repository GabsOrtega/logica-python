from datetime import date

atual = date.today().year
maioridade = 0
menoridade = 0

for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}° pessoa: '.format(c)))
    idade = atual - ano
    if idade >= 21:
        maioridade += 1
    else:
        menoridade += 1
print('{} pessoas já são maiores de idade'.format(maioridade))
print('{} pessoas ainda são menores de idade'.format(menoridade))
