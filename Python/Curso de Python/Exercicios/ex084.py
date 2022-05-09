lista = list()
tlista = list()
tot = 0
ma = 0
me = 0

while True:
    n = str(input('NOME: ')).strip().title()
    tlista.append(n)
    p = float(input('PESO: '))
    tlista.append(p)
    if p >= ma:
        ma = p
    if tot == 0:
        me = p
    else:
        if p <= me:
            me = p
    tot = tot + 1
    lista.append(tlista[:])
    tlista.clear()
    n = str(input('DESEJA CONTINUAR? [S/N] ')).strip().upper()
    if n == 'S':
        print()
    elif n == 'N':
        print('FINALIZANDO...')
        print()
        break
    else:
        print('COMANDO INVALIDO!')
        print('FINALIZANDO...')
        print()
        break
print(f'AO TODO,  VOCE CADASTROU {tot} PESSOAS')
print(f'O MAIOR PESO FOI DE {ma:.1f}. PESO DE ', end='')

for c in lista:
    if c[1] == ma:
        print(c[0], end=' ')

print(f'\nO MENOR PESO FOI DE {me:.1f}. PESO DE ', end='')

for c in lista:
    if c[1] == me:
        print(c[0], end=' ')
print()
print()
