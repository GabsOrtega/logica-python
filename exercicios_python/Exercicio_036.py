valor = float(input('\033[31mDigite o valor da casa: \033[32mR$'))
sal = float(input('\033[31mDigite o salário do comprador: \033[32mR$'))
anos = int(input('\033[31mEm quantos anos você vai pagar a casa? '))

meses = (anos*12)
prestacao = valor/meses
excedente = sal*(30/100)

print('\033[35mO valor da casa é de: \033[32mR${:.2f}'.format(valor))
print('\033[35mO salário do comprador da casa é de: \033[32mR${:.2f}'.format(sal))
print('\033[35mO valor da prestação mensal será de: \033[32mR${:.2f} \033[35mem {} \033[32manos'.format(prestacao, anos))

if prestacao <= excedente:
    print('\033[32mParabens! Seu empréstimo foi aceito!')
    print('O valor das parcelas \033[32mR${:.2f} \033[36mNÃO EXCEDEU \033[35m30% \033[32mR${:.2f} \033[36mdo seu salário!'.format(prestacao, excedente))
elif prestacao > excedente:
    print('\033[31mInfelizmente seu empréstimo foi negado!')
    print('\033[33mO valor das parcelas \033[32mR${:.2f} \033[31mEXCEDEU \033[35m30% \033[32mR${:.2f} \033[33mdo seu salário!'.format(prestacao, excedente))

print('\033[33mTenha um Bom dia!')