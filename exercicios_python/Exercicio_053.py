frase = str(input('Digite uma frase qualquer: ').upper())
espaco = frase.strip() # tira os espacos do final e do começo
div = espaco.split() # faz divisao a cada espaco
junto = ''.join(div) # junta a divisao com um termo entre: ''
inverso = ''
inverso = junto[::-1]
'''for c in range(len(junto)-1, -1, -1):
    inverso += junto[c]'''
print('O inverso de {} é {}'.format(junto, inverso))
if junto == inverso:
    print('A frase digitada é um palindromo!')
else:
    print('A frase digitada não é um palindromo!')

