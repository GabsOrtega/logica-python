algo = input('\033[0;35mDigite algo: \033[m')
print('\033[0;31mO tipo primitivo desse valor é: \033[1;36m', type(algo))
print('\033[0;31mÉ alfabetico? \033[1;36m', algo.isalpha())
print('\033[0;31mÉ númerico? \033[1;36m', algo.isnumeric())
print('\033[0;31mÉ tudo maisculo? \033[1;36m', algo.isupper())
print('\033[0;31mÉ tudo minusculo? \033[1;36m', algo.islower())
print('\033[0;31mSó tem espaço? \033[1;36m', algo.isspace())
print('\033[0;31mÉ alfanumerico? \033[1;36m', algo.isalnum())
print('\033[0;31mEstá capitalizada? \033[1;36m', algo.istitle())
