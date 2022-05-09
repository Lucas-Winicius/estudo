t = 0
m = 0
me = 0
ma = 0
p = 'S'

while p != 'N':
    n1 = float(input('DIGITE UM NUMERO: '))
    me = n1
    if n1 > ma:
        ma = n1
    if n1 == ma:
        ma = n1
    if n1 < me:
        me = n1
    if n1 == me:
        me = n1
    t = t + 1
    m = m + n1
    p = str(input('QUER CONTINUAR? [S/N]')).upper()
    print()
    if p != 'S' and p != 'N':
        p = 'N'
        print('ERRO COMANDO INVALIDO')
        print()
        print('TENTE NOVAMENTE...')
        print()
print(f'VOCE DIGITOU {t} NUMEROS EA MEDIA FOI {m / t:.2f}')
print(f'O MAIOR VALOR FOI {ma} E O MENOR FOI {me}')