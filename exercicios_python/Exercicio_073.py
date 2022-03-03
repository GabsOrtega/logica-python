Times = ('Flamengo', 'Palmeiras', 'Atlético Mineiro', 'Grêmio', 'Athletico Paranaense', 'Santos', 'São Paulo',
         'Intenacional', 'Fluminense', 'Corinthians', 'Fortaleza', 'Bahia', 'Ceará', 'Cruzeiro', 'América Mineiro',
         'Atlético Goianiense', 'Chapecoense', 'Botafogo', 'Vasco da Gama', 'Red Bull Bragantino')

print('-=' * 20)
print('Lista de times do Brasileirão:', Times)
print('-=' * 20)
print('Os 5 primeiros colocados são:', Times[0:5])
print('-=' * 20)
print('Os últimos 4 colocados são:', Times[-4:])
print('-=' * 20)
print('Times em ordem alfabética:', sorted(Times))
print('-=' * 20)
print('A posição do time da Chapecoense na tabela é:', Times.index('Chapecoense') + 1)
