frase = str(input('Digite uma frase qualquer: ')).strip().upper()
vzsA = frase.count('A')
posP = frase.find('A')+1
posF = frase.rfind('A')+1

print("""Sua frase foi: {}. 
As vezes que aparece a letra 'A' são: {} vezes
A posição da primeira letra 'A' é {}
A posição da ultima letra 'A' é {}
""".format(frase, vzsA, posP, posF))



