largura = float(input('\033[34mDigite a largura em metros da parede: '))
altura = float(input('Digite a altura em metros da parede: '))
area = (largura*altura)
litro = area/2
print('\033[35mA dimensão dessa parede é de: \033[33m{}\033[35mx\033[33m{}'.format(largura, altura))
print('\033[35mA área dessa parede é de: \033[33m{}'.format(area))
print('\033[35mA quantidade de tinta necessária para pintar a parede é de: \033[33m{} \033[35mlitros'.format(litro))