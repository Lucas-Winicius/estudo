from time import sleep
from random import randint

print("""SUAS OPÇOES:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA """)
v1 = int(input('QUAL A SUA JOGADA? '))

v2 = randint(0, 2)

print('')
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('')

if v2 == 0:
    print('-='*12)
    print('COMPUTADOR JOGOU PEDRA')
    if v1 == 0:
        print('JOGADOR JOGOU PEDRA')
        print('-='*12)
        print('EMPATE!')
    elif v1 == 1:
        print('JOGADOR JOGOU PAPEL')
        print('-='*12)
        print('JOGADOR VENCEU!')
    elif v1 == 2:
        print('JOGADOR JOGOU TESOURA')
        print('-='*12)
        print('COMPUTADOR VENCEU!')
    else:
        print('-='*12)
        print('ERRO...')
        sleep(3)
        print('CARREGANDO...')
        sleep(6.30)
        print('')
        print('JOGADA INVALIDA!')

elif v2 == 1:
    print('-=' * 12)
    print('COMPUTADOR JOGOU PAPEL')
    if v1 == 0:
        print('JOGADOR JOGOU PEDRA')
        print('-=' * 12)
        print('COMPUTADOR VENCEU!')
    elif v1 == 1:
        print('JOGADOR JOGOU PAPEL')
        print('-=' * 12)
        print('EMPATE!')
    elif v1 == 2:
        print('JOGADOR JOGOU TESOURA')
        print('-=' * 12)
        print('JOGADOR VENCEU!')
    else:
        print('-=' * 12)
        print('ERRO...')
        sleep(3)
        print('CARREGANDO...')
        sleep(6.30)
        print('')
        print('JOGADA INVALIDA!')

elif v2 == 2:
    print('-=' * 12)
    print('COMPUTADOR JOGOU TESOURA')
    if v1 == 0:
        print('JOGADOR JOGOU PEDRA')
        print('-=' * 12)
        print('JOGADOR VENCEU!')
    elif v1 == 1:
        print('JOGADOR JOGOU PAPEL')
        print('-=' * 12)
        print('COMPUTADOR VENCEU!')
    elif v1 == 2:
        print('JOGADOR JOGOU TESOURA')
        print('-=' * 12)
        print('EMPATE!')
    else:
        print('-=' * 12)
        print('ERRO...')
        sleep(3)
        print('CARREGANDO...')
        sleep(6.30)
        print('')
        print('JOGADA INVALIDA!')

