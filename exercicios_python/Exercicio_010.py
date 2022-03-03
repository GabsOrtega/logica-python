real = float(input('\033[0;31mDigite sua quantidade de dinheiro: \033[0;32mR$'))
dolar = real/5.53
euro = real/6.34
print('''\033[35mVocê pode comprar: \033[32mUS${:.2f}
\033[35mOu você pode comprar: \033[33m€{:.2f}'''.format(dolar, euro))