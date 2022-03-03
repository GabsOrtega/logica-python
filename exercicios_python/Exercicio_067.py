tab = c = 0

while True:
    tab = int(input('Digite o valor da tabuada que deseja: '))
    c = 0
    if tab < 0:
        break
    print('=-' * 20)
    for c in range(1, 11):
        print(f'{tab} x {c} = {tab*c}')
    print('=-'*20)
print('GERADOR DE TABUADA ENCERRADO!')
