valor = float(input('Digite o valor a ser pago pelo produto: R$'))
pagamento = int(input('''Digite o número conforme informado abaixo:
[ 1 ] - À Vista no DINHEIRO ou CHEQUE - 10% de desconto
[ 2 ] - À Vista no CARTÃO - 5% de desconto
[ 3 ] - PARCELADO EM ATÉ 2X NO CARTÃO - PREÇO NORMAL
[ 4 ] - PARCELADO EM ATÉ 3X ou MAIS - 20% de JUROS
'''))

if pagamento == 1:
    desconto = valor - (valor*(10/100))
    print('Valor SEM DESCONTO: R${}'.format(valor))
    print('Valor COM DESCONTO R${}'.format(desconto))
elif pagamento == 2:
    desconto = valor - (valor*(5/100))
    print('Valor SEM DESCONTO R${}'.format(valor))
    print('Valor COM DESCONTO R${}'.format(desconto))
elif pagamento == 3:
    print('Preço normal R${}'.format(valor))
    parcela = valor/2
    print('Compra parcelada em 2x de {}'.format(parcela))
elif pagamento == 4:
    juros = valor + (valor*(20/100))
    totparcela = int(input('Quantas parcelas? '))
    parcela = juros / totparcela
    print('Sua compra será parcelada em {}x e você irá pagar R${:.2f} COM JUROS'.format(totparcela, parcela))
    print('O preço total de: R$ {:.2f} foi para R$ {:.2f} COM JUROS'.format(valor, juros))
else:
    print('Não existe esse método de pagamento!')

print('Tenha um Bom Dia!')
