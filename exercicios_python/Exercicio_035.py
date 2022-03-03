print('='*20)
print('Analisador de Triângulos')
print('='*20)
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

if s1+s2 > s3 and s2+s3 > s1 and s1+s3 > s2:
    print('Com essas três retas É POSSÍVEL formar um triângulo.')
else:
    print('Com essas três retas NÃO É POSSÍVEL formar um triângulo.')