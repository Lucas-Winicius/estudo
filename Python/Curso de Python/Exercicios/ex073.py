times = 'Flamengo', 'Palmeiras', 'Grêmio', 'Internacional',\
        'Athletico Paranaense', 'Santos', 'Corinthians', 'São Paulo',\
        'Atlético Mineiro', 'Cruzeiro', 'Bahia', 'Fluminense',\
        'Botafogo', 'Ceará', 'Chapecoense', 'Vasco da Gama', \
        'América Mineiro', 'Fortaleza', 'Atlético Goianiense', 'Sport'

print('-='*50)
print(f'LISTA DE TIMES DO BRASILEIRAO: {times}')
print('-='*50)
print(f'OS 5 PRIEIROS SAO: {times[:6]}')
print('-='*50)
print(f'OS 4 ULTIMOS SAO: {times[-4:]}')
print('-='*50)
print(f'TIMES EM ORDEM ALFABETICA: {sorted(times)}')
print('-='*50)
for pos, comid in enumerate(times):
    if comid == 'Chapecoense':
        n = pos
print(f'O CHAPEOENSE ESTA NA {n}ª POSIÇAO')
del(n)