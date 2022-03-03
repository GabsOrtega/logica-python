metros = float(input('\033[0;33mDigite a quantidade de metros: '))
km = metros*0.001
hm = metros*0.01
dam = metros*10
dm = metros*0.1
cent = metros*100
mili = metros*1000
print('\033[0;35mValor escolhido em metros: \033[1;36m{}\033[0;35m. \n Convertido em Quilômetros: \033[1;36m{}\033[0;35mkm \n Convertido em hectometros? \033[1;36m{}\033[0;35mhm \n Convertido em decimetro \033[1;36m{}\033[0;35mdm \n Convertido em decametros: \033[1;36m{}\033[0;35mdam\n Convertido em Centimetros: \033[1;36m{:.0f}\033[0;35mcm. \n Convertido em milimetros: \033[1;36m{:.0f}\033[0;35mmm'.format(metros, km, hm, dam, dm, cent, mili))