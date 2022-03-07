expressao = str(input('Digite a expressão desejada: '))
pilha = []

for s in expressao:
    if s == '(':
        pilha.append('(')
    elif s == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')

if len(pilha) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está incorreta!')