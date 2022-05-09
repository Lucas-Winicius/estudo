from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}

ranking = dict()

print('VALORES SORTEADOS:')
for k, v in jogo.items():
        print(f'{k} TIROU {v} NO DADO')
        sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*35)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
        print(f'   - {i+1}º LUGAR: {v[0]} COM {v[1]}')
        sleep(1)