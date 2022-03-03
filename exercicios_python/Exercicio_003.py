n1 = int(input('\033[0;34mDigite um número: \033[m'))
n2 = int(input('\033[0;34mDigite outro número: \033[m'))
soma = n1+n2
print('\033[0;33mA soma entre \033[4;36m{} \033[0;33me \033[3;36m{} \033[0;33mé igual a: \033[4;36m{}'.format(n1, n2, soma))