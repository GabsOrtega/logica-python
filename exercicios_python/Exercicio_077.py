palavras = ('PYTHON', 'PROGRAMACAO', 'TECLADO', 'MOUSE', 'NOTEBOOK', 'CELULAR',
'CADEIRA', 'GAMER', 'CONSOLE', 'JOGOS', 'MERCADO', 'GITHUB')

for c in palavras:
     print(f'\nNa palavra {c} temos as vogais: ', end='')
     for letra in c:
         if letra.lower() in 'aeiou':
             print(letra, end=' ')

