extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
           'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
continuar = 'S'
num = 0
while continuar != 'N':
    while True:
        num = int(input('Digite um número de 0 a 20: '))
        if 0 <= num <= 20:
            break
    print(f'O numero {num} por extenso é: {extenso[num]}')
    continuar = str(input('Deseja continuar? [S/N]: ')).upper()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja continuar? [S/N]: ')).upper()

