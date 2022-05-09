from random import randint
from time import sleep
vi = 0

while True:
    co = randint(0, 10)
    nf = 'A'
    print('-'*30)
    print(' '*3,'JOGO DO PAR OU IMPAR')
    print('-'*30)
    print('')
    player = int(input('DIGITE UM VALOR [0/10]: '))
    to = player + co
    if player > 10 or player < 0:
        print('JOGADA INVALIDA')
        print('TENTE NOVAMENTE...')
        print('UM HUMANO TEM NO MAXIMO 10 DEDOS NA MAO')
        break


    jogada = str(input(('IMPAR OI PAR? [I/P] '))).strip().upper()
    if jogada != 'P' and jogada != 'I':
        print('JOGADA INVALIDA...')
        print('TENTE (I) PARA IMPAR')
        print('TENTE (P) PARA PAR')
        print('TENTE NOVAMENTE')
        break
    print('')
    if to % 2 == 0:
        nf = 'P'
    elif to % 2 != 0:
        nf = 'I'

    if jogada == nf:
        print('CONTANDO OS DEDOS...')
        sleep(3)
        print()
        print(f'O COMPUTADOR JOGOU {co}')
        print(f'E VOCE JOGOU {player}')
        print(f'OS 2 JUNTOS JOGARAM {to}')
        vi = vi + 1
        print()
        print('-'*15)
        print('PARABENS VOCE VENCEU')
        print(f'NUMEROS DE VITORIAS {vi}')
        print('REINICIANDO O JOGO...')
        print('-'*15)
        sleep(5)
        print('')
    else:
        print('CONTANDO DEDOS...')
        print()
        sleep(3)
        print('DERROTA!')
        print()
        print('O TOTAL DA SOMA ENTRE OS NUMEROS:')
        print(f'COMPUTADOR JOGOU: {co}')
        print(f'VOCE JOGOU: {player}')
        print(f'TOTAL: {co + player}')
        if nf == 'P':
            print('SENDO ASSIM UM NUMERO PAR')
        if nf == 'I':
            print('SENDO ASSIM UM NUMERO IMPAR')
        print()
        if vi >= 1:
            print(f'VOCE VENCEU {vi} VEZES')
            print('PARABENS')
        else:
            print('QUE PENA VOCE NAO TEVE NENHUMA VITORIA')
        break

