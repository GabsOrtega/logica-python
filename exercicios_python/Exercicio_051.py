primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo = primeiro + (10-1) * razao
for a in range(primeiro, decimo + razao, razao):
    print(a, end=' ')
