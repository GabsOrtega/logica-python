n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

media = (n1+n2)/2

if media < 5:
    print('Sua média é \033[31m{:.1f}'.format(media))
    print('\033[1;31mREPROVADO!')
elif media >= 5 and media <= 6.9:
    print('\033[mSua média é \033[36m{:.1f}'.format(media))
    print('\033[1;36mRECUPERAÇÃO!')
elif media >= 7:
    print('\033[mSua média é \033[32m{:.1f}'.format(media))
    print('\033[1;32mAPROVADO!')