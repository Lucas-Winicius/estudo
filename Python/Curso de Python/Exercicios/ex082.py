list = []
par = []
impar = []

while True:
    v = int(input('DIGITE UM VALOR: '))
    list.append(v)
    c = str(input('QUER CONTINUAR [S/N]? ')).strip().upper()
    if c == 'S':
        print()
    elif c == 'N':
        print('FINALIZANDO...')
        break
    else:
        print('VALOR INVALIDO')
        print('FINALIZANDO...')

for c in list:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print('-='*35)
print(f'A LISTA COMPLETA E {list}')
print(f'A LISTA DE PARES E {par}')
print(f'A LISTA DOS IMPARES E {impar}')